#!/usr/bin/env python3

import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()
# messages = [b"Message 1 from client."]
messages = [[b"user1:pass1"],
[b"user2:pass2"],
[b"user3:pass3"],
[b"user4:pass4"],
[b"user5:pass5"],
[b"user6:pass6"],
[b"user7:pass7"],
[b"user8:pass8"],
[b"user9:pass9"],
[b"user10:pass10"],
[b"user11:pass11"],
[b"user12:pass12"],
[b"user13:pass13"],
[b"user14:pass14"],
[b"user15:pass15"],
[b"user16:pass16"],
[b"user17:pass17"],
[b"user18:pass18"],
[b"user19:pass19"],
[b"user20:pass20"],
[b"user21:pass21"],
[b"user22:pass22"],
[b"user23:pass23"],
[b"user24:pass24"],
[b"user25:pass25"],
[b"user26:pass26"],
[b"user27:pass27"],
[b"user28:pass28"],
[b"user29:pass29"],
[b"user30:pass30"],
[b"user31:pass31"],
[b"user32:pass32"],
[b"user33:pass33"],
[b"user34:pass34"],
[b"user35:pass35"],
[b"user36:pass36"],
[b"user37:pass37"],
[b"user38:pass38"],
[b"user39:pass39"],
[b"user40:pass40"],
[b"user41:pass41"],
[b"user42:pass42"],
[b"user43:pass43"],
[b"user44:pass44"],
[b"user45:pass45"],
[b"user46:pass46"],
[b"user47:pass47"],
[b"user48:pass48"],
[b"user49:pass49"],
[b"user50:pass50"],
[b"user51:pass51"],
[b"user52:pass52"],
[b"user53:pass53"],
[b"user54:pass54"],
[b"user55:pass55"],
[b"user56:pass56"],
[b"user57:pass57"],
[b"user58:pass58"],
[b"user59:pass59"],
[b"user60:pass60"],
[b"user61:pass61"],
[b"user62:pass62"],
[b"user63:pass63"],
[b"user64:pass64"],
[b"user65:pass65"],
[b"user66:pass66"],
[b"user67:pass67"],
[b"user68:pass68"],
[b"user69:pass69"],
[b"user70:pass70"],
[b"user71:pass71"],
[b"user72:pass72"],
[b"user73:pass73"],
[b"user74:pass74"],
[b"user75:pass75"],
[b"user76:pass76"],
[b"user77:pass77"],
[b"user78:pass78"],
[b"user79:pass79"],
[b"user80:pass80"],
[b"user81:pass81"],
[b"user82:pass82"],
[b"user83:pass83"],
[b"user84:pass84"],
[b"user85:pass85"],
[b"user86:pass86"],
[b"user87:pass87"],
[b"user88:pass88"],
[b"user89:pass89"],
[b"user90:pass90"],
[b"user91:pass91"],
[b"user92:pass92"],
[b"user93:pass93"],
[b"user94:pass94"],
[b"user95:pass95"],
[b"user96:pass96"],
[b"user97:pass97"],
[b"user98:pass98"],
[b"user99:pass99"],
[b"user100:pass100"],
[b"user101:pass101"],
[b"user102:pass102"],
[b"user103:pass103"],
[b"user104:pass104"],
[b"user105:pass105"],
[b"user106:pass106"],
[b"user107:pass107"],
[b"user108:pass108"],
[b"user109:pass109"],
[b"user110:pass110"],
[b"user111:pass111"],
[b"user112:pass112"],
[b"user113:pass113"],
[b"user114:pass114"],
[b"user115:pass115"],
[b"user116:pass116"],
[b"user117:pass117"],
[b"user118:pass118"],
[b"user119:pass119"],
[b"user120:pass120"],
[b"user121:pass121"],
[b"user122:pass122"],
[b"user123:pass123"],
[b"user124:pass124"],
[b"user125:pass125"],
[b"user126:pass126"],
[b"user127:pass127"],
[b"user128:pass128"],
[b"user129:pass129"],
[b"user130:pass130"],
[b"user131:pass131"],
[b"user132:pass132"],
[b"user133:pass133"],
[b"user134:pass134"],
[b"user135:pass135"],
[b"user136:pass136"],
[b"user137:pass137"],
[b"user138:pass138"],
[b"user139:pass139"],
[b"user140:pass140"],
[b"user141:pass141"],
[b"user142:pass142"],
[b"user143:pass143"],
[b"user144:pass144"],
[b"user145:pass145"],
[b"user146:pass146"],
[b"user147:pass147"],
[b"user148:pass148"],
[b"user149:pass149"],
[b"user150:pass150"]]

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print("starting connection", connid, "to", server_addr)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid=connid,
            msg_total=sum(len(m) for m in messages[i+1]),
            recv_total=0,
            messages=list(messages[i+1]),
            outb=b"",
        )
        sel.register(sock, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        # print("Anual Aa")
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            print("received", repr(recv_data), "from connection", data.connid)
            data.recv_total += len(recv_data)
            # hacer out de JS----------- 
            # hacer out de JS----------- 
            # hacer out de JS----------- 
            # hacer out de JS----------- 
            # hacer out de JS----------- 
            # hacer out de JS----------- 
        if not recv_data or data.recv_total == data.msg_total:
            print("closing connection", data.connid)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        # print("Bb bbcitaa")
        if not data.outb and data.messages:
            # print("jbalvin men")
            data.outb = data.messages.pop(0)
            print(data.outb)
        if data.outb:
            # print("nickyjam")
            print("sending", repr(data.outb), "to connection", data.connid)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]


if len(sys.argv) != 4:
    print("usage:", sys.argv[0], "<host> <port> <num_connections>")
    sys.exit(1)

host, port, num_conns = sys.argv[1:4]
start_connections(host, int(port), int(num_conns))

try:
    while True:
        events = sel.select(timeout=1)
        if events:
            for key, mask in events:
                service_connection(key, mask)
        # Check for a socket being monitored to continue.
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()