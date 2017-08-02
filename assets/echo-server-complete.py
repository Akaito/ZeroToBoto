# echo-server-complete.py

import socket

PORT = 4001

# TODO : Hide all this try-except low-level socket business in a module.
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setblocking(0)
try:
    listen_socket.bind(('0.0.0.0', PORT))
except socket.error as e:
    if e.errno == 98:
        print "Socket wasn't closed properly.  Wait a moment and try again."
        exit()
    raise
listen_socket.listen(0)
print 'Listening on port {}.'.format(PORT)

conns = []
quitting = False
while not quitting:
    # TODO : Have to check for connections closed by remote.
    try:
        # try to accept more connections
        try:
            conn, addr = listen_socket.accept()
        except socket.error as e:  # the normal case we expect
            if e.errno != 11:  # Resource temporarily unavailable
                raise
        else:  # someone connected
            print 'Remote {} connected.'.format(addr)
            conn.setblocking(0)
            for other_conn in conns:
                other_conn.send('{} has joined.\n'.format(addr))
            conns.append(conn)

        # try to read a message
        for conn in conns:
            try:
                data = conn.recv(256)
            except socket.error as e:  # the normal case we expect
                if e.errno != 11:  # Resource temporarily unavailable
                    raise
            else:
                if data.strip() == 'kill':
                    print 'Got kill command.'
                    quitting = True
                    break
                print 'Echoing {}'.format(data.strip())
                # echo message out to everyone
                for c in conns:
                    if c == conn:
                        continue
                    c.send(data)
    except:
        listen_socket.close()
        del listen_socket
        raise

