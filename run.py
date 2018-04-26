import sys, logging

from peer import Peer

if sys.version_info > (3, 0):
    raw_input = input

def main(argv):
    addr = None
    syncAddr = None
    syncDNS = None
    for each in argv:
        if '--addr=' in each:
            if ':' in each:
                addr = each[7:]
            else:
                addr = each[7:] + ':25565'
        elif '--sync-addr=' in each:
            syncAddr = each[12:]
        elif '--sync-DNS=' in each:
            syncDNS = each[11:]

    logging.basicConfig(level=logging.DEBUG)
    if addr:
        peer = Peer(serverAddr=addr.split(':')[0], serverPort=addr.split(':')[1])
    else:
        peer = Peer()
    peer._initServerSock()
    peer.start()
    if syncAddr:
        peer.ClassicV1._joinNetFromPeer(syncAddr)
        peer.ClassicV1._syncListFromPeer(syncAddr)
    elif syncDNS:
        peer.ClassicV1._joinNetFromDNS(syncDNS)
    else:
        logging.debug('You have to manual give a peer\'s ip or DNS domain for sync.')
        logging.debug('Or peer would not sync to any net.')
        logging.debug('Unless this is first peer.')
    
    while True:
        try:
            raw = raw_input('')
            if raw == '':
                continue
            elif raw == 'peers':
                for (pid, host) in peer.ClassicV1._peers.items():
                    print((pid, host))
            elif raw == 'test':
                print('test')
        except KeyboardInterrupt:
            peer.exit()
            break

if __name__ == '__main__':
    main(sys.argv)

