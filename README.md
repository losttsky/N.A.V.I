# 🧚 NAVI: Núcleo de Asistencia y Vigilancia Inteligente

**NAVI** es un asistente virtual de código abierto diseñado para automatizar flujos de trabajo de programación e integración de sistemas, optimizado para ejecutarse localmente en hardware NVIDIA (GTX 1650).

## 🌀 El Proyecto
NAVI no es solo un chatbot; es un orquestador que conecta un modelo de lenguaje (LLM) con el sistema operativo para ejecutar rutinas complejas mediante comandos de voz.

### 🛠️ Funcionalidades Principales
- **Cerebro Local:** Ejecución de Llama 3.2 (3B) mediante Ollama para privacidad total y latencia cero.
- **Automatización de Oficina:** Apertura sincronizada de herramientas bancarias (Teams, Edge, BeyondTrust, Remote Desktop).
- **Interfaz de Voz:** Reconocimiento de voz y síntesis de voz (TTS) offline.
- **Modo Gamer:** Capacidad de liberar recursos (VRAM) instantáneamente para sesiones de juego en la Acer Nitro 5.

## 🏗️ Arquitectura del Sistema
El sistema se divide en tres capas principales:

1. **Capa de Percepción:** Python (SpeechRecognition) + Micrófono.
2. **Capa de Razonamiento:** Ollama + Llama 3.2 3B (Corriendo en la GTX 1650).
3. **Capa de Ejecución:** Scripts de automatización con `pyautogui` y `subprocess`.

## 🚀 Requisitos de Hardware (Mi Setup)
- **Host:** Acer Nitro 5
- **CPU:** AMD Ryzen 5 3550H
- **GPU:** NVIDIA GTX 1650 (4GB VRAM) - *Motor de inferencia CUDA*
- **RAM:** 16GB DDR4
- **Almacenamiento:** SSD 256GB (SO) + M.2 Secundario (Modelos y Datos)

## 📋 Próximos Pasos (Roadmap)
- [ ] Configuración inicial de repositorio y entorno virtual de Python.
- [ ] Implementación del "Wake Word" (detección de la palabra 'Navi').
- [ ] Conexión con la API local de Ollama.
- [ ] Programación de la función `rutina()` para el dashboard de trabajo.
- [ ] Integración de voz de respuesta con `pyttsx3`.

---
*Diseñado por Lostt Sky - 2026*
