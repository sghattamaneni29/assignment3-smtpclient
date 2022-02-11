from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = '\r\n My message'
    endmsg = '\r\n.\r\n'

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    emailserver = ('smtp.gmail.com', 25)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(emailserver)
    recv = clientSocket.recv(1024).decode()
    #print(recv)

    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    message1 = clientSocket.recv(1024).decode()
    #print(message1)
    #if message1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    fromMail = 'MAIL FROM:<stlsea0804@smtp.gmail.com>\r\n'
    clientSocket.send(fromMail.encode())
    message2 = clientSocket.recv(1024)
    #print (message2)

    # Send RCPT TO command and handle server response.
    toMail = 'RCPT TO:<stlsea0804@smtp.gmail.com>\r\n'
    clientSocket.send(toMail.encode())
    message3 = clientSocket.recv(1024)
    #print (message3)
    #if message3[:3] != '250':
        #print ('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    message4 = clientSocket.recv(1024)
    #print (message4)
    #if message4[:3] != '250':
        #print ('250 reply not received from server.')

    # Send message data.
    #print ('Send message data')
    clientSocket.send('To: stlsea0804@smtp.gmail.com'.encode())
    clientSocket.send('From: stlsea0804@smtp.gmail.com'.encode())
    clientSocket.send('Subject: Hi.. There..This is a test'.encode())
    clientSocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    #print ('Message ends with a single period')
    clientSocket.send(endmsg.encode())
    clientSocket.send(msg.encode())
    message7 = clientSocket.recv(1024)
    #if message7[:3] != '250':
        #print ("250 reply not received from server.")
    # Fill in end

    # Send QUIT command and handle server response.
    quit = 'Quit\r\n'
    clientSocket.send(quit.encode())
    message8 = clientSocket.recv(1024)
    #print (message8)
    #if message8[:3] != '250':
       # print ('250 reply not received from server.')


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')