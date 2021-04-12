from os import system
import PySimpleGUI as sg
from icon_desktop import create_file

create_file()

layout = [
	[
		sg.Text(	
			'Digite sua senha root: ',
			background_color='#282a36', 
			text_color='#bd93f9', 
			font='"Fira Code" 12', 
			size=(25, 0)
		)
	],
	[
		sg.Input(
			font='"Fira Code" 12', 
			background_color='#44475a', 
			size=(35, 0), 
			key='password',
			do_not_clear=False, 
			password_char='*'
		)
	],
	[
		sg.Checkbox(
			'Manter aberto',
			background_color='#282a36',
			checkbox_color='#44475a',
			font='"Fira Code" 11',
			# enable_events=True,
			key='open'
		)
	],
	[
		sg.Text(
			font='"Fira Code" 12', 
			background_color='#282a36', 
			size=(35, 0), 
			key='label_info'
		)
	],
	[
		sg.Button(
			'Try', 
			font='"Fira Code" 12',
			button_color='#44475a'
		),
		sg.Text(
			size=(17, 0), 
			background_color='#282a36'
		),
		sg.Button(
			'Exit', 
			font='"Fira Code" 12', 
			button_color='#ff5555'
		)
	]
]

window = sg.Window('Xamp Start', layout, background_color='#282a36', size=(300, 170))

while True:
	valid = bool()
	events, values = window.read()
	if events == sg.WINDOW_CLOSED or events == 'Exit':
		break
	if events == 'Try':
		teste = system(f"echo {values['password']} | sudo -S echo 1")
		if teste == 0:
			window['label_info'].update('SUCESS: Started Xamp...', text_color='#50fa7b')
			window.refresh()
			valid = True
		else:
			window['label_info'].update('FAILED: Password error...', text_color='#ff5555')
			system("echo Failed...")
			valid = False
		
		if valid:
			system(f"echo {values['password']} | sudo -S echo Sucess && cd /opt/lampp && sudo -S ./manager-linux-x64.run")
			valid = values['open']
			if valid:
				window['label_info'].update('')
			else:
				window.close()
