#!/usr/bin/env python2

import boto3
import ConfigParser
import os

config = ConfigParser.ConfigParser()
config.read(os.path.expanduser('~/.lightsail.conf'))

sshkeylocation = config.get('ssh','keyname')
region = config.get('ssh', 'region')
zone = config.get('ssh', 'zone')

class Lightsail():
  def __init__(self):
    '''Initiate the lightsail instance'''
    self.lightsailclient = boto3.client('lightsail', region_name=region)
    self.zone = zone

  def list_instances(self):
    return self.lightsailclient.get_instances()

  def create_instance(self, lightsail_name, blueprintid, bundleid):
    '''Creates a VPS with the specified name, blueprintid(OS), 
        and bundleid(hardware)'''
    response = self.lightsailclient.create_instances(
        instanceNames=[lightsail_name],
        availabilityZone=self.zone,
        blueprintId=blueprintid,
        bundleId=bundleid,
        keyPairName=sshkeylocation
    )
    return response

  def get_instance_info(self, lightsail_name):
    return self.lightsailclient.get_instance(instanceName=lightsail_name)

  def get_instance_ip(self, lightsail_name):
    ip = self.get_instance_info(lightsail_name)
    return ip['instance']['publicIpAddress']

  def get_instance_username(self, lightsail_name):
    username = self.get_instance_info(lightsail_name)
    return username['instance']['username']

  def delete_instance(self, lightsail_name):
    return self.lightsailclient.delete_instance(instanceName=lightsail_name)

  def connect_to_instance(self, lightsail_name):
    pass

  def put_instance_public_ports(self, lightsail_name, ports):
      return self.lightsailclient.put_instance_public_ports(portInfos=ports,
                                                            instanceName=lightsail_name)