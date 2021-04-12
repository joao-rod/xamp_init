from os import system

def get_username():
	import getpass
	return getpass.getuser()


def create_file():
	username = get_username()
	try:
		a = open(f'/home/{username}/.local/share/applications/Xamp.desktop', 'r')
	except FileNotFoundError:
		a = open(f'/home/{username}/.local/share/applications/Xamp.desktop', 'w')
		a.write(f'''
	[Desktop Entry]
	Name=Xamp
	Exec=python3 /home/{username}/xamp/init.py
	Comment=
	Terminal=false
	Icon=/opt/lampp/htdocs/favicon.ico
	Type=Application
	''')
	else:
		print('Aplicação já existe')
	finally:
		a.close()