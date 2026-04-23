import subprocess
import os
import time
import ollama
import speech_recognition as sr
import asyncio
import edge_tts
import pygame

# Inicializamos el mezclador de audio una sola vez al inicio
pygame.mixer.init()

# --- MOTOR DE VOZ NEURAL (EDGE-TTS) ---
def hablar(texto):
    if not texto.strip():
        return
        
    print("(Hablando con voz neural...)")
    
    # Limpieza del texto para la voz
    texto_limpio = texto.replace('*', '').replace('#', '').replace('\n', ' ').replace('\r', '')
    
    # Elegimos una voz (es-MX-DaliaNeural es una de las mas naturales y fluidas)
    voz = "es-MX-DaliaNeural" 
    archivo_audio = "navi_voz_temp.mp3"
    
    # Funcion asincrona para generar el audio
    async def generar_audio():
        comunicar = edge_tts.Communicate(texto_limpio, voz)
        await comunicar.save(archivo_audio)
        
    # Ejecutamos la generacion
    asyncio.run(generar_audio())
    
    # Reproducimos el audio generado
    pygame.mixer.music.load(archivo_audio)
    pygame.mixer.music.play()
    
    # Esperamos a que termine de hablar antes de seguir ejecutando codigo
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
        
    # Liberamos el archivo para poder sobrescribirlo la proxima vez
    pygame.mixer.music.unload()

def iniciar_jornada():
    print("\n[NAVI ejecutando protocolo de entorno...]")
    hablar("Iniciando protocolo. Preparando tus herramientas de trabajo.")
    
    user_path = os.environ['USERPROFILE']
    ruta_edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    ruta_beyond = r"C:\Program Files\Bomgar\Access Console\banrural-access.beyondtrustcloud.com\sra-con.exe"
    ruta_brave = f"{user_path}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    ruta_scripts = r"C:\Users\amart\Desktop\Scripts Config"
    
    urls_edge = [
        "https://dev.azure.com/BDRTICprojects/",
        "https://dev.azure.com/BDRTICprojects/Dashboard%20DESA-QA/_dashboards/dashboard/203cb509-11d6-48c2-a04a-1f6a8985e593"
    ]

    if os.path.exists(ruta_brave):
        subprocess.Popen(ruta_brave)
    
    if os.path.exists(ruta_edge):
        for url in urls_edge:
            subprocess.Popen([ruta_edge, url])
            time.sleep(0.5) 

    subprocess.Popen("start msteams:", shell=True) 
    
    if os.path.exists(ruta_beyond):
        subprocess.Popen(ruta_beyond)
        
    if os.path.exists(ruta_scripts):
        subprocess.Popen(f'explorer "{ruta_scripts}"')
        
    subprocess.Popen("mstsc.exe")
    hablar("Entorno operativo. Buen turno, Angelo.")

def escuchar_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n[NAVI calibrando ruido de fondo...]")
        recognizer.adjust_for_ambient_noise(source, duration=1.5)
        
        # Ajustes de paciencia para que no corte tu voz
        recognizer.pause_threshold = 2.5 
        recognizer.non_speaking_duration = 1.0 
        
        print("[Habla ahora...]")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)
            print("[Procesando...]")
            texto = recognizer.recognize_google(audio, language="es-GT")
            print(f"Angelo: {texto}")
            return texto.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except Exception as e:
            return ""

def chat_con_navi():
    print("=== NAVI SYSTEM ONLINE ===")
    hablar("Sistemas en linea y calibrados.")
    
    mensajes = []
    
    while True:
        usuario = escuchar_voz()
        
        if not usuario:
            continue
            
        if 'salir' in usuario or 'apagar' in usuario:
            hablar("Apagando sistemas. Nos vemos.")
            break
            
        if "iniciar jornada" in usuario or "inicia jornada" in usuario:
            iniciar_jornada()
            usuario = "Confirma brevemente que la jornada inicio correctamente."
        
        mensajes.append({'role': 'user', 'content': usuario})
        print("NAVI: Pensando...")
        
        try:
            respuesta = ollama.chat(model='navi', messages=mensajes)
            texto_navi = respuesta['message']['content']
            
            # Limpiamos asteriscos o formato que afecte la voz
            texto_para_hablar = texto_navi.replace('*', '').replace('#', '')
            print(f"\nNAVI: {texto_navi}\n")
            
            # Ejecutamos la voz
            hablar(texto_para_hablar)
            
            mensajes.append({'role': 'assistant', 'content': texto_navi})
        except Exception as e:
            print(f"Error de sistema: {e}")

if __name__ == "__main__":
    chat_con_navi()