import sys, logging

from MaybeP2P.peer import Peer

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

    if addr:
        peer = Peer(serverAddr=addr.split(':')[0], serverPort=addr.split(':')[1])
    else:
        peer = Peer()
    peer.start()
    if syncAddr:
        syncHost = (syncAddr.split(':')[0], int(syncAddr.split(':')[1]))
        peer.ClassicV1._joinNetFromPeer(syncHost)
        peer.ClassicV1._syncListFromPeer(syncHost)
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
                for (pid, peerInfo) in peer.ClassicV1._peersInfo.items():
                    print((pid, peerInfo.getHost()))
            elif raw.startswith('send'):
                (pid, peerinfo) = peer.ClassicV1.getPeerInfoBy(raw.split(' ')[1])
                message = raw.split(' ')[2]
                peer.ClassicV1.sendMessage(message, host=peerinfo.getHost())
        except KeyboardInterrupt:
            peer.exit()
            break

if __name__ == '__main__':
    main(sys.argv)

