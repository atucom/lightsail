# Amazon Lightsail VPS Management Tool

This lightsail script simplifies the following tasks:

 * List/Create/Delete Lightsail instances
 * SSH into specific instances
 * Change default accept TCP/UDP ports through the firewall


## Installation
### Requirements
 * Python2.7
 * boto3

### ~/.lightsail.conf
I'm using a configuration file stored in the local user's directory to hold information about the connection. The included sample conf should be modified to fit your parameters.


## Usage

```
$ lightsail --help
usage: lightsail [-h] [--list] [--delete NAME [NAME ...]] [--ssh NAME]
                 [--create NAME] [--os debian|ubuntu]
                 [--size nano|micro|small] [--ports NAME] [--protocol NAME]
                 [--instance_name NAME]

Amazon Lightsail VPS Management Tool

optional arguments:
  -h, --help            show this help message and exit
  --list                List your Lightsail instances
  --delete NAME [NAME ...]
                        Delete your specified Lightsail instance(s)
  --ssh NAME            SSH to your Lightsail instance

New Instance Options:
  --create NAME         Create your Lightsail instance given a instance name
  --os debian|ubuntu    debian 8.7 or ubuntu 16.04(default)
  --size nano|micro|small
                        nano(.5gb & default)/micro(1gb)/small(2gb)

Firewall Management:
  --ports NAME          Change the ports allowed through the default firewall
                        (1-10,11,12,13-65535)
  --protocol NAME       all|tcp|udp. ****all will default to 0-65535
  --instance_name NAME  SSH Instance Name
```