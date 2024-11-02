import socket 
import time 
import os 
import json
# Define ANSI escape codes for colors
class Color:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
def clear():
    os.system("clear")

print(f"{Color.RED}Loading....")
time.sleep(1)

clear()
print(f"{Color.GREEN}Welcome To AirChat v-1.0.1\n-->\tType [help] for help and guides || Type [exit] to exit shell")

layout = f"\n{Color.RED}NEye {Color.BLUE}Terminal {Color.YELLOW} $~> {Color.GREEN}"

def airmsg():
    try:
        s_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        print(f"{Color.RED}Socket connected at [\n\t{s_connection}\n]{Color.GREEN}")
    except socket.error as error:
        print("error")
    
    s_connection.bind(('127.0.0.1', 8080))
    print(f"{Color.RED}Server is running at 127.0.0.1:8080 !")
    time.sleep(2)
    s_connection.listen(1)
    print(f"Server is running....{Color.GREEN}")

    cli_connected, address = s_connection.accept()
    print(f"{Color.YELLOW}Connected with {address}{Color.GREEN}!")

    while True:
        data_send = input(f"{Color.MAGENTA}Enter message to send : {Color.CYAN}")
        if data_send == "exit":
            s_connection.close()
            cli_connected.close()
            break

        cli_connected.sendall(data_send.encode())
        print(f"{Color.YELLOW}[i] Message Sent wait for message to received...{Color.GREEN}")
        data_recv = cli_connected.recv(1024).decode()
        print(f"{Color.YELLOW}[i] Message recv: {Color.BLUE}{data_recv}{Color.GREEN}")

def connectServer():
    try:
        client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        print(f"{Color.RED}Socket connected at [\n\t{client_connection}\n]{Color.GREEN}")
    except socket.error as error:
        print("error")

    client_connection.connect(("127.0.0.1", 8080))
    print(f"{Color.YELLOW}[i] Wait for message to received from server...{Color.GREEN}")
    while True:
        data_recv = client_connection.recv(1024).decode()
        print(f"\n\t{data_recv}\n")
   
        data_send = input(f"{Color.MAGENTA}Enter message to send : {Color.CYAN}")
        client_connection.sendall(data_send.encode())
        print(f"{Color.YELLOW}[i] Message Sent wait for message to received...{Color.GREEN}")

    client_socket.close()

class terminal:
    def __init__(self):
        while True:
            self.u_input = input(f"{layout}").lower()
            # self.timesleep = 1
            # self.timeout = 0
            self.memory = []
            self.memory.append(f"{self.u_input} ")
            self.help = f"{Color.BLUE}help\t[help and guides]\nexit\t[Exit Terminal]\nshowhis\t[Show command history]\nairmsg\t[Create chat server]\nconnserver\t [Conect with chat server]\n{Color.GREEN}" 
            # self.exit = exit() 
            self.showhis = f"""{Color.RED}[\n\t{json.dumps(self.memory, indent=5, sort_keys=False)}\n]{Color.GREEN}"""

            print("Command : ",self.u_input)
            self.countMemories = len(self.memory)
            
            if self.u_input == "help":
                print(self.help)
            elif self.u_input == "airmsg":
                airmsg()
            elif self.u_input == "connserver":
                connectServer()
            elif self.u_input == "showhis":
                print(self.showhis)
            else:
                print(f"{Color.RED}Invalid Command!{Color.GREEN}")

terminal()
