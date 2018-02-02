import boto.ec2
import jinja2
import subprocess


def get_ips():
    conn = boto.ec2.connect_to_region('us-east-1')
    consul_servers = conn.get_all_instances(filters={"tag:foo": "bar"})
    server_ips = []
    
    for server in consul_servers:
        for inst in server.instances:
            if inst.private_ip_address:
                if inst.state == 'running':
                server_ips.append(inst.private_ip_address)
    return server_ips

if __name__ == '__main__':
    # Load template
    templateLoader = jinja2.FileSystemLoader(searchpath="/path/to/file/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    templateFile = "config.j2"
    template = templateEnv.get_template(templateFile)
    
    # Get consul server ips
    servers = get_ips()
    
    # Write server ips to configuration
    print(template.render(foo=servers))
    path_to_json = "/path/to/file"
    with open(path_to_json,"w") as file:
        file.write(template.render(foo=servers))
        file.close()
