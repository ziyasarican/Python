import requests
import json

apiURL = "https://api.exchangerate.host/latest?base="

givenMoney = input("Given currency type: ")
givenMoney = givenMoney.upper()
receivedMoney = input("Received currency type: ")
receivedMoney = receivedMoney.upper()
amountMoney = input("Amount of money to exchange: ")
amountMoney = int(amountMoney)

result = requests.get(apiURL+givenMoney)
result = json.loads(result.text)
unitResult = result["rates"][receivedMoney]
totalResult = float(unitResult)*amountMoney

print(f"1 {givenMoney} = {unitResult} {receivedMoney}")
print(f"{amountMoney} {givenMoney} = {totalResult} {receivedMoney}")
