import ggwave
import pyaudio
import time
print("----> simple Gibber Link Speech stuff <----")
print("  *commands: /cmds")

def send(text):
    speech = ggwave.encode(text)
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=48000,
                    output=True)
    stream.write(speech)
    time.sleep(1)     
    stream.stop_stream()
    stream.close()
    p.terminate()

def menu():
    while True:
        usr = input("text > ")
        if usr == "/exit":
            print("bye :)")
           break
        elif usr == "/cmds":
            print("----> help <----")
            print("/cmds - Show this")
            print("/exit - exit")
        else:
            send(usr)
            
menu()
