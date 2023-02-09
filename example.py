from fernet import Fernet


fer = Fernet(bytes("xTK6dh5CQ3LRz_fBKn1AEHfcFkNDb07jPLz2rVFjiJU==".encode("utf-8")))
cipher = "gAAAAABjhjtogjiKZA5bJrbQWJ4joSCrh3toUaJ3KR698r0LbZJv9jc5S2THuKxvyqVv6qSnPbHohdZlKj4SbGs9rGf9FVLuG2V8QCOB6h8XxKnWPW1HgKARWsBZSobb-kis7tG4-IfK"
key = fer.decrypt(bytes(cipher.encode("utf-8")))
print(key)