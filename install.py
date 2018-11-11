import os
import platform

class InstallPasswordGenerator():

    def __init__(self):
        print('+------------------------------------------------------+')
        print('|            Installing PasswordGenerator              |')
        print('|               Developed By Will Assad                |')
        print('+------------------------------------------------------+')


    def setup(self):
        if platform.system() == "Darwin":
            self.mac_osx_install_route()

    def mac_osx_install_route(self):
        os.system("chmod +x ./main.py")
        os.system('export PATH="$PATH:$HOME/bin"')
        os.system("ln -s " + os.getcwd() + "/main.py /usr/local/bin/genpass")


if __name__ == "__main__":
    installer = InstallPasswordGenerator()
    installer.setup()
