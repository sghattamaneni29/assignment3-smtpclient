from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = '\r\n My message'
    endmsg = '\r\n.\r\n'

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    servermessage = clientSocket.recv(1024).decode()
    #print(servermessage)

    #if servermessage[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    message1 = clientSocket.recv(1024)
    #print (message1)
    #if message1[:3] != '250':
        #print ('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    fromMail = 'MAIL FROM:<stlsea0804@gmail.com>\r\n'
    clientSocket.send(fromMail.encode())
    message2 = clientSocket.recv(1024)
    #print (message2)

    # Send RCPT TO command and handle server response.
    toMail = 'RCPT TO:<stlsea0804@gmail.com>\r\n'
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
    clientSocket.send('To: stlsea0804@gmail.com'.encode())
    clientSocket.send('From: stlsea0804@gmail.com'.encode())
    clientSocket.send('Subject: Hi.. There..This is a test'.encode())
    clientSocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    #print ('Message ends with a single period')
    clientSocket.send(endmsg.encode())
    clientSocket.send(msg.encode())
    message7 = clientSocket.recv(1024)
    #if message7[:4] != '250':
        #print ("250 reply not received from server.")
    # Fill in end

    # Send QUIT command and handle server response.
    quitcommand = 'QUIT\r\n'
    clientSocket.send(quitcommand.encode())
    message8 = clientSocket.recv(1024).decode()
    #print ('message ' + message8)


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')