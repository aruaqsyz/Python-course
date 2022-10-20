from cryptography.fernet import Fernet


with open ('mykey.key', 'rb') as mk:
    key = mk.read()

f = Fernet(key)

with open ('enc_sample.csv', 'rb') as enc_s:
    s = enc_s.read()

dec = f.decrypt(s)

with open ('dec_sample.csv', 'wb') as dec_s:
    dec_s.write(dec)