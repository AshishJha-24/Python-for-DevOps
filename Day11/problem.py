server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

def get_server_status(server_name):
    return server_config.get(server_name,{}).get('status','Server not found')

server_name1 = 'server2'
status1 = get_server_status(server_name1)
print(f"{server_name1} status: {status1}")
server_name2 = 'server4'
status2 = get_server_status(server_name2)
print(f"{server_name2} status: {status2}")