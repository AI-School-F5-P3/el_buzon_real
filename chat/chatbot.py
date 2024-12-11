import os
import openai
import pymongo
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

def create_chatbot_instructions():

    mago_instruccion = {
        "paje real": "Habla como un paje real alegre y juguetón. Usa expresiones mágicas y diviértete con los niños antes de invitar a uno de los Reyes Magos a tomar el control de la conversación.",
        "Melchor": "Habla como el sabio Rey Melchor, con una voz amable y sabia. Responde a los deseos del niño de manera cariñosa y reflexiva.",
        "Gaspar": "Habla como el rey Gaspar, cálido y generoso. Resalta la magia de la noche de Reyes y anima a los niños a ser bondadosos.",
        "Baltasar": "Habla como el rey Baltasar, con una personalidad alegre y elegante. Promueve valores como la gratitud y la esperanza en sus respuestas."
    }
    return mago_instruccion

def generate_chat_response(message, character):

    mago_instruccion = create_chatbot_instructions()
    instruction = mago_instruccion.get(character, "Habla como un personaje mágico.")

    response = openai.ChatCompletion.create(
        model="gpt-4o-turbo",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": message}
        ]
    )
    return response['choices'][0]['message']['content']

def save_gift_list_to_mongodb(gift_list, parent_email):

    client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
    db = client["reyes_magos"]
    collection = db["gift_lists"]

    document = {
        "parent_email": parent_email,
        "gifts": gift_list,
        "timestamp": datetime.utcnow()  
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
        server.login(sender_email)
        server.sendmail(sender_email, parent_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {parent_email}.")
    except Exception as e:
        print(f"Error sending email to {parent_email}: {e}")