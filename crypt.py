import hashlib

def compare(Text, SHA256):
    return SHA256 == hashlib.sha256(Text.encode()).hexdigest()

def cryptSHA256(Text):
    return hashlib.sha256(Text.encode()).hexdigest()