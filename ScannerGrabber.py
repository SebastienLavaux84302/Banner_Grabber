import socket, time, os, sys

class ScannerGrabber:
    def __init__(self, host):
        self.Tab_personalised_port = []
        self.Useful_ports = [22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
        self.Description_ports = ["SSH", "Telnet", "SMTP", "DNS", "HTTP", "POP3", "RPC", "NetBIOS", "IMAP", "HTTPS", "Microsoft-DS", "IMAP SSL", "POP3 SSL", "PPTP", "MySQL", "Remote Desktop", "VNC", "HTTP Proxy"]
        self.List_port_open = []
        self.Host = host
        self.My_Socket = 0
        self.scan_all(host)
        self.listening()

    def add_port(self, port):
        self.Tab_personalised_port.append(port)

    def scan_all(self, host):
        tab_port = self.Useful_ports
        for port in tab_port:
            My_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            My_Socket.settimeout(0.3)
            result = My_Socket.connect_ex((host, port))
            if(result == 0):
                print(f"PORT [{port}] ouvert -> {self.Description_ports[self.Useful_ports.index(port)]}")
                self.List_port_open.append(port)
                My_Socket.close()

    def connexion(self, port):
        self.My_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.My_Socket.settimeout(0.5)
        print("Connecting to :",self.Host, "on port :",port)
        try:
            self.My_Socket.connect((self.Host, port))
        except:
            print("Impossible de se connecter au port : ",port)
            
    def listening(self):
        message = "a\r\n\r\n"
        for port in self.List_port_open:
            self.connexion(port)
            print("Banner sur le port : "+ str(port))
            try:
                self.My_Socket.sendall(message.encode('utf-8'))
                print('Message send successfully')
                time.sleep(0.5)
                reply = self.My_Socket.recv(4096).decode()
                if not reply:
                    print("Aucune donnée reçu ...")
                    self.My_Socket.close()
                else:
                    print(reply)
                    self.My_Socket.close()
                    print("-" * 20)
                    print(" ")
            except socket.error:
                print('Envoie échoué')
                print("Connexion au port échoué")
                print("-" * 20)
                print(" ")
                pass

def main():
    ScannerGrabber("X.X.X.X")

if (__name__ == '__main__'):
    main()
