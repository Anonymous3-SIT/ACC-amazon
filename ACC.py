from faker import Faker
import pycountry
import barnum
from time import sleep

#Jangan direkode hehe
#coba aja mana tau beruntung yg fake jadi asli :v
#developer @Mr.TamfanX

def eng():
	jum=int(raw_input("\nAmount: "))
	delay=raw_input("Delay: ")
	for i in range(jum):
		en_us_fake=Faker()
		a = en_us_fake.first_name()
		b = en_us_fake.last_name()
		print""
		print"="*50
		print("Name\t: "+ a +' '+ b)
		print("email\t: {}@gmail.com".format(a))
		print("Address\t: "+en_us_fake.street_address())
		print("Zipcode\t: "+en_us_fake.zipcode())
		print("Phone\t: "+en_us_fake.phone_number())
		print("City\t: "+en_us_fake.city())
		no=barnum.create_cc_number()[1]
		print""
		print("CC Name\t: "+a+' '+b)
		for k in no:
			print("No.CC\t: "+k)
		print("Expired\t: "+en_us_fake.credit_card_expire())
		print"="*50
		sleep(float(delay))
	print"\n\033[35;5m\033[4mGoodBye\033[0m"
	exit()


def id():
	jum=int(raw_input("\nAmount: "))
	delay=raw_input("Delay: ")
	for i in range(jum):
		id_fake=Faker('id_ID')
		g=Faker()
		a = id_fake.name()
		print""
		print"="*50
		print("Name\t: "+a)
		print("email\t: "+id_fake.email())
		print("Phone\t: "+id_fake.phone_number())
		print("Address\t: "+id_fake.street_address())
		print("City\t: "+id_fake.city())
		print("Zipcode\t: "+g.zipcode())
		c=pycountry.countries.get(alpha_2='ID')
		print("Country\t: "+c.name)
		no=barnum.create_cc_number()[1]
		print""
		print("CC Name\t: "+a)
		for k in no:
			print("No.CC\t: "+k)
		print("Expired\t: "+g.credit_card_expire())
		print("S.Code\t: "+g.credit_card_security_code())
		print"="*50
		sleep(float(delay))
	print"\n\033[35;5m\033[4mGoodBye\033[0m"
	exit()

if __name__=="__main__":
	import os
	os.system('clear')
	print"""
     \033[32;5m\033[4mFree Credit Card for Amazon\033[0m
	     \033[32;5m\033[4mBy Mr.TamfanX\033[0m

	\033[33;5m\033[4mSelected country:\033[0m

	1]> United States
	2]> Indonesian\n"""
	a = raw_input("> ")
	if a == "1":
		eng()
	if a == "2":
		id()
