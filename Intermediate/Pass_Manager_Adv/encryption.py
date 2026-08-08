import bcrypt

def hash_pass(passw):
    return bcrypt.hashpw(passw.encode(),bcrypt.gensalt())

def check_pass(passw,old_pass):
    return bcrypt.checkpw(passw.encode(),old_pass)