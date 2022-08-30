"""114) Crie um código em Python que teste se o site pudim está acessível pelo computador usado."""

import webbrowser

new = 2
url = "http://pudim.com.br/"
webbrowser.open(url, new=new)