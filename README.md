# Binance CryptoBox Bot – Guía rápida

Este bot te permite canjear automáticamente códigos de Binance CryptoBox que aparecen en ciertos canales de Telegram.  
**Te avisa cuando tus headers/cookies expiren, para que solo edites un archivo y sigas usando el bot sin reiniciarlo.**

---

## 🧩 Requisitos

- Python 3.8 o superior
- [Telegram API ID y API HASH](https://my.telegram.org/)
- Cuenta de Binance (para obtener headers/cookies)
- Acceso a los canales de Telegram con los códigos

---

## ⚡ Instalación

1. **Clona o descarga este repositorio**
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Configuración paso a paso

### 1. Consigue tus datos de Telegram

- Ve a [https://my.telegram.org/](https://my.telegram.org/)
- Inicia sesión y genera tu **API ID** y **API HASH**

### 2. Consigue tus headers/cookies de Binance

1. Entra a [https://www.binance.com/uk-UA/my/wallet/account/payment/cryptobox](https://www.binance.com/uk-UA/my/wallet/account/payment/cryptobox) desde tu navegador.
2. Abre las **herramientas de desarrollador** (F12 o clic derecho → Inspeccionar).
3. Ve a la pestaña **Network** (Red).
4. Canjea manualmente cualquier código (puede ser uno inválido).
5. Busca una petición a la URL similar a:
   ```
   https://www.binance.com/bapi/pay/v1/private/binance-pay/gift-box/code/grabV2
   ```
6. Haz clic en esa petición y busca la sección **Headers** (Encabezados).
7. Copia **todos los headers** que aparecen ahí, incluyendo el header **Cookie**.
8. Pégalos en el archivo `headers.json`, reemplazando los valores de ejemplo.

**Ejemplo:**
```json
{
    "User-Agent": "tu_user_agent",
    "bnc-uuid": "tu_bnc_uuid",
    "device-info": "tu_device_info",
    "clienttype": "web",
    "csrftoken": "tu_csrftoken",
    "fvideo-id": "tu_fvideo_id",
    "fvideo-token": "tu_fvideo_token",
    "x-trace-id": "tu_x_trace_id",
    "x-ui-request-trace": "tu_x_ui_request_trace",
    "lang": "uk-UA",
    "Referer": "https://www.binance.com/uk-UA/my/wallet/account/payment/cryptobox",
    "Cookie": "tus_cookies_completos"
}
```
- **NO borres ninguna clave.** Si un valor no aparece, déjalo vacío: `"clave": ""`
- **No agregues ni elimines comas fuera de lugar.**

### 3. Configura tu información de Telegram

Edita el archivo `source/config.py` y pon tu `API_ID` y `API_HASH`:

```python
API_ID: int = 1234567
API_HASH: str = "abcd1234abcd1234abcd1234abcd1234"
```

Opcional: puedes cambiar el nombre del cliente o los IDs de los canales en `CHATS`.

---

## 🚀 Uso

1. Asegúrate de editar `headers.json` y `source/config.py` correctamente.
2. Ejecuta el bot:
   ```bash
   python main.py
   ```
3. El bot se conectará a Telegram y empezará a escuchar los canales configurados.

---

## 🟡 Cuando los headers/cookies expiran

- El bot te avisará en la consola con un mensaje tipo:
  ```
  ¡Tus headers/cookies han expirado! Actualízalos en headers.json.
  ```
- **Solo necesitas volver a repetir el paso 2** (copiar headers nuevos de Binance y pegarlos en `headers.json`).
- **No es necesario reiniciar el bot**, solo guarda el archivo para que el bot los use la próxima vez.

---

## 🛟 Preguntas Frecuentes

### ¿Cada cuánto caducan los headers/cookies?
- Depende, pero normalmente cada 1-7 días. Si ves el mensaje de expirados, repite el procedimiento.

### ¿Cómo sé qué canales escuchar?
- Los IDs están en `CHATS` en `source/config.py`. Puedes añadir o quitar los que quieras.

### ¿Se puede correr en un VPS o servidor?
- Sí, solo asegúrate de tener Python y acceso a tus archivos.

---

## 💡 Consejos

- **No compartas tus headers/cookies ni tu API_HASH/ID.**
- Si tienes dudas sobre cómo copiar los headers, busca tutoriales de "obtener headers con DevTools" en YouTube.
- Si el formato de los códigos cambia, ajusta la expresión regular en `lib/telegram.py` o `main.py`.

---

¡Listo!  
Si sigues estos pasos tendrás el bot funcionando y podrás actualizar tus headers/cookies fácilmente cuando expiren, sin reiniciar el bot.
