import sys, logging

from peer import Peer

if sys.version_info > (3, 0):
    raw_input = input

def main(argv):
    addr = None
    syncAddr = None
    for each in argv:
        if '--addr=' in each:
            if ':' in each:
                addr = each[7:]
            else:
                addr = each[7:] + ':25565'
        elif '--sync-addr=' in each:
            syncAddr = each[12:]

    logging.basicConfig(level=logging.DEBUG)
    if addr:
        peer = Peer(serverAddr=addr.split(':')[0], serverPort=addr.split(':')[1])
    else:
        peer = Peer()
    peer._initServerSock()
    peer.start()
    if syncAddr:
        peer._joinNetFromPeer(syncAddr)
        peer._syncListFromPeer(syncAddr)
    
    while True:
        try:
            raw = raw_input('')
            if raw == '':
                continue
            elif raw == 'peers':
                for (pid, host) in peer.peers.items():
                    print((pid, host))
            elif raw == 'test':
                print('test')
        except KeyboardInterrupt:
            peer.exit()
            break

if __name__ == '__main__':
    main(sys.argv)

