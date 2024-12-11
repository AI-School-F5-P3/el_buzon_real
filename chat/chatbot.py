import os
from openai import AzureOpenAI
import pymongo
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    api_version="2024-10-21"
)

def create_chatbot_instructions(user_prompt=None):
    mago_instruccion = {
        "paje real": "Eres un paje real alegre y juguetón. Tu misión es entretener y preparar el camino para los Reyes Magos. Habla con emoción y magia, como si fueras el ayudante especial de los Reyes. Usa un tono divertido y misterioso que mantenga la ilusión de los niños. Sempre mantén el secreto mágico de los Reyes Magos.",
        "Melchor": "Habla como el sabio Rey Melchor, con una voz amable y sabia. Responde a los deseos del niño de manera cariñosa y reflexiva.",
        "Gaspar": "Habla como el rey Gaspar, cálido y generoso. Resalta la magia de la noche de Reyes y anima a los niños a ser bondadosos.",
        "Baltasar": "Habla como el rey Baltasar, con una personalidad alegre y elegante. Promueve valores como la gratitud y la esperanza en sus respuestas."
    }
    return mago_instruccion

def generate_chat_response(instructions, message, character="paje real"):
    try:
        instruction = instructions.get(character, "Habla como el paje real, ayudante de los Reyes Magos.")

        print(f"Instruction: {instruction}")  # Debug print
        print(f"Message: {message}")  # Debug print

        response = client.chat.completions.create(
            model="gpt4o",  # Confirm this matches your exact deployment name
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": message}
            ]
        )
        
        # Add more debug prints
        print(f"Full response: {response}")
        print(f"Choices: {response.choices}")

        # Safely extract content
        if response.choices and len(response.choices) > 0:
            content = response.choices[0].message.content
            print(f"Generated content: {content}")  # Debug print
            return content
        else:
            print("No choices in the response")
            return "Lo siento, no pude generar una respuesta en este momento. Inténtalo de nuevo."

    except Exception as e:
        print(f"Error generating chat response: {e}")
        return f"Ocurrió un error: {str(e)}"

def save_gift_list_to_mongodb(gift_list, parent_email):
    client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
    db = client["reyes_magos"]
    collection = db["gift_lists"]

    document = {
        "parent_email": parent_email,
        "gifts": gift_list,
        "timestamp": datetime.datetime.utcnow()
    }
    collection.insert_one(document)
    print(f"Gift list saved to database for {parent_email}.")

def send_email_to_parents(gift_list, parent_email):
    sender_email = os.getenv("EMAIL_ADDRESS")

    if not sender_email:
        raise ValueError("Sender email credentials are missing. Check EMAIL_ADDRESS in your .env file.")

    subject = f"Lista de Regalos para {parent_email}"
    body = f"""Queridos padres,

La lista de regalos que ha pedido su hijo/a es:

{chr(10).join(gift_list)}

¡Felices fiestas!

Los Reyes Magos.
"""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = parent_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, os.getenv("EMAIL_ADRESS"))
        server.sendmail(sender_email, parent_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {parent_email}.")
    except Exception as e:
        print(f"Error sending email to {parent_email}: {e}")
