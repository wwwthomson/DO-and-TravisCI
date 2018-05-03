import os
import requests

def create_droplets(do_token, build_id, ssh_keys):
    url = "https://api.digitalocean.com/v2/droplets"
    data = {"names":
            [
                "master1",
                "slave1"
            ],
            "region": "nyc3",
            "size": "s-1vcpu-1gb",
            "image": "centos-7-x64",
            "ssh_keys": None,
            "backups": False,
            "ipv6": False,
            "user_data": None,
            "private_networking": True,
            "tags": ["web"]}
    print(data)
    headers = {"Authorization": "Bearer {}".format(do_token)}

    r = requests.post(url, headers=headers, json=data)
    print(r.text)
    print(r.status_code)

def delete_droplets(do_token, build_id):
    url = "https://api.digitalocean.com/v2/droplets?tag_name=web"
    headers = {"Authorization": "Bearer {}".format(do_token)}
    r = requests.delete(url, headers=headers)
    print(r.status_code)


if __name__ == "__main__":
    do_token = os.environ['DO_TOKEN']
    build_id = os.environ['TRAVIS_BUILD_ID']
    ssh_keys = os.environ['SSH_KEYS']
    print(do_token)
    print(build_id)
    print(ssh_keys)
    create_droplets(do_token, build_id, ssh_keys)
    delete_droplets(do_token, build_id)
