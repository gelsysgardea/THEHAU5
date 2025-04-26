import datetime

def custom_print(message, msg_type="info"):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prefix = {
        "info":    "[INFO]",
        "error":   "[ERROR]",
        "success": "[SUCCESS]",
        "warn":    "[WARNING]"
    }.get(msg_type, "[INFO]")
    print(f"{prefix} {now} - {message}")