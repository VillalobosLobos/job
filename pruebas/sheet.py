import requests

API_KEY = "AIzaSyA3srlSBH7u_ddDMbq8PRgKe46jtmuJSuk"
SPREADSHEET_ID = "1jLxPWm-msEPpTiCIvNnMMzTmsrgwfAEyDU_HOY6Fx1Q"
RANGE = "Hoja1!A1"  # Cambia según tu hoja

url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{RANGE}?valueInputOption=RAW&key={API_KEY}"

data = {
    "range": RANGE,
    "majorDimension": "ROWS",
    "values": [["idCliente", "nombre", "calle", "numExt", "numInt", "colonia", "deleMuni", "cp", "pais", "beneficio", "numTelefono"]]
}

response = requests.put(url, json=data)
print(response.json())
