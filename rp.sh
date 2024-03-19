#! /usr/bin/bash

<<info

https://github.com/TreatHunter
This is remote play script. It's purpose is to controll old pc as tvstation to be contolled over ssh
v1.0.0

MIT License

Copyright (c) 2024 TreatHunter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

info

Help(){
echo
echo "commands:"
echo "ap - play link in new anonimus tab"
echo "exit - return (works everywhere)"
echo
}

AnonimusPlay(){
	apInput=""
	while [ "$apInput" != "exit" ]
	do
		echo "Enter link to open:"
		read apInput
		case "$apInput" in
			"exit") ;;
			*) (firefox --private-window "$apInput");;
		esac
	done
}

echo "Welcome to remote play"
export DISPLAY=:0
input=""
while [	"$input" != "exit" ]
do
	Help
	echo "select regime of work:"
	read input	
	case "$input" in
	"ap") AnonimusPlay;;
	esac
done

