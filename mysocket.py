import socket
 
# 클라이언트가 보내고자 하는 서버의 IP와 PORT
server_ip = "127.0.0.1"
server_port = 10353
server_addr_port = (server_ip, server_port)
 
# 보낼 메시지를 byte 배열로 바꾼다.
msg_from_client = '{"pilot_date": "2023-10-12", "pilot_time": "12:00+", "ship_name": "MSC ALIYA(2J)", "gross_ton": "140,976", "loa": "366.0", "dft": "12.5", "from_": "NT03", "to_": "PS-3", "side": "\\uc88c\\ud604", "pilot": "YSK", "tugs": "601\\ubc31\\ub8e1 801\\uc120\\uc9c4", "ds": "", "call_sign": "D5TM4 ", "imo": "9842097", "agent": "MSC KOREA", "status": "\\ub3c4\\uc120\\u00a0\\u25cb", "entry": "\\ucd9c\\ud56d", "ps": "", "rmk_com": "\\uc774\\uc0c1\\uc5c6\\uc74c[\\uc218\\uc2b5 : \\ud558\\ub9d0\\uadfc]", "rmk_agent": "", "rmk_pilot": "", "flag": "\\ubd80\\uc0b0"}'
bytes_to_send = str.encode(msg_from_client)
 
# 소켓을 UDP로 열고 서버의 IP/PORT로 메시지를 보낸다.
udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_client_socket.sendto(bytes_to_send, server_addr_port)