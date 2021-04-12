from os import system

def get_username():
	import getpass
	return getpass.getuser()


def create_file():
	username = get_username()
	try:
		a = open(f'/home/{username}/.local/share/applications/teste.desktop', 'r')
	except FileNotFoundError:
		a = open(f'/home/{username}/.local/share/applications/teste.desktop', 'w')
		a.write('''
	[Desktop Entry]
	Name=Teste
	Exec=python3 /home/xamp/init.py
	Comment=
	Terminal=false
	Icon=/opt/lampp/htdocs/favicon.ico
	Type=Application
	''')
	else:
		print('Aplicação já existe')
	finally:
		a.close()