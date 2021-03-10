from test_chrome import SendMessageFacebook

a = "https://www.facebook.com/profile.php?id=1791640577"
b = "Assalamualaikum, Maaf ganggu, saya nak promote perniagaan kecil saya. Saya nak perkenalkan sistem aplikasi untuk buat invoice atau rekod akaun secara online. Diskaun 60% limit 100 orang sahaja. Dari RM950 -----> RM285 sahaja.!! Boleh tengok demo. https://invoicemudah.com. Boleh whatsapp: https://api.whatsapp.com/send?phone=60174220665"

filename = 'C:/Users/rajan/Desktop/facebook-automation/userlist.txt'

'''fh = open(filename)
s =" "
while (s):
    s = fh.readline()'''

SendMessageFacebook(filename, b)