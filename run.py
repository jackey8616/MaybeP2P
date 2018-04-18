import logging
from peer import Peer

def main():
    logging.basicConfig(level=logging.DEBUG)
    peer = Peer()
    peer._initServerSock()
    peer.start()
    peer.broadcastData(peer.uuid)
    
    while True:
        try:
            raw = input('Command: ')
        except KeyboardInterrupt:
            peer.stopped = True
            peer.broadcastData('Exit')
            break

if __name__ == '__main__':
    main()

