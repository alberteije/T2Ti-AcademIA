import subprocess

# subprocess.run("calc")
# subprocess.run("notepad")

# subprocess.run(r"C:\T2Ti ERP\ERP 3.0 Programas e Fontes\Flutter\vycanis\agenda\build\windows\x64\runner\Debug\agenda.exe")
# subprocess.run("C:\\T2Ti ERP\\ERP 3.0 Programas e Fontes\\Flutter\\vycanis\\agenda\\build\\windows\\x64\\runner\\Debug\\agenda.exe")

# subprocess.run("dir", shell=True)
subprocess.run("md backup", shell=True)
subprocess.run(r"copy *.json c:\testes\python\backup", shell=True)

