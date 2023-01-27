from bitChangerSDK import SDK


sdk = SDK.SDK("private_key", "public_key")
balance = sdk.Token.balance("USDTTRC")
print(balance)