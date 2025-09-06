#
#
DAS GEHIRN
(production_deal_bot.py)
DIESE DATEI
STEUERT
NICHT ÄNDERN
#
DEN
BOT -
import asyncio import telegram
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters from config import BOT_TOKEN, DEAL _INTERVAL
# Wir werden die nächsten Zeilen später hinzufügen, wenn die anderen Teile fertig sind
# from comprehensive_deal_scraper
import DealScraper
# from email notification_system
import EmailSystem
# --- Befehle, die der Bot versteht
ーーー
# Dieser Befehl wird ausgeführt, wenn jemand /start tippt async def start_command (update, context):
welcome message = (
"**IHR PERSÖNLICHER DEAL
BOT**\n\n"
"Hallo! Ich bin jetzt online
und bereit, für Sie die besten Deals
zu finden. \n\n"
"Verfügbare
Befehle: \n"
"/start - Diese Nachricht
anzeigen\n"
"/deals - Die Suche nach Deals
manuell starten (Funktion kommt bald!)
\n"
"/status - Meinen aktuellen
Status prüfen"
await
update.message.reply_text (welcome_mess age, parse_mode= 'Markdown' )
# Dieser Befehl wird ausgeführt, wenn jemand /status tippt async def status_command (update, context):
await
update message. reply_text ("Status: Ich bin wach und funktioniere. Die Deal-Suche ist aktuell noch nicht aktiv.")
# --- Hauptprogramm ---
def
main ():
print ("INFO: Bot wird
gestartet...")
# Baut die Verbindung zu
Telegram auf application =
Application. builder () • token (BOT_TOKEN)
•build()
# Sagt dem Bot, welche Befehle er
kennen soll
↓
application.add_handler (CommandHandle
("start"
", start_command) )
application.add_handler (CommandHandler
'status"
(, status_command) )
print(f" INFO: Bot hört jetzt auf
Befehle. Deal-Suche startet in
1 Kürze
alle {DEAL_INTERVAL} Minuten.")
# Startet den Bot, damit er auf
Nachrichten lauschen kann application.run_polling()
if_name_ ==  ' _main_ ' :
main()
