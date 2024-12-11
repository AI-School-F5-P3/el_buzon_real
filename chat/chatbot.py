import os
import openai
import pymongo
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": message}
        ]
    )
    return response['choices'][0]['message']['content']

def save_gift_list_to_mongodb(gift_list, child_name):

    client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
    db = client["reyes_magos"]
    collection = db["gift_lists"]

    document = {
        "child_name": child_name,
        "gifts": gift_list
    }
    collection.insert_one(document)

def send_email_to_parents(child_name, gift_list, parent_email):

    sender_email = os.getenv("EMAIL_ADDRESS")
    sender_password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        raise ValueError("Email credentials not found. Please set EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")

    subject = f"Lista de Regalos de {child_name}"
    body = f"Queridos padres de {child_name},\n\nLa lista de regalos que ha pedido es:\n\n" + "\n".join(gift_list) + "\n\n¡Felices fiestas!\n\nLos Reyes Magos."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = parent_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, parent_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", e)