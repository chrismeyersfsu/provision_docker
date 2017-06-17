[![Build Status](https://travis-ci.org/chrismeyersfsu/provision_docker.svg?branch=master)](https://travis-ci.org/chrismeyersfsu/provision_docker)


# provision_docker
An Ansible role to help you test your roles. Automagically create docker containers for each of your inventory hosts. Use your production inventory file to create docker containers for development and test.

<img align="center" src="https://i.imgflip.com/1dbjhv.jpg" alt="blah">

| Resource                                                                                  | Description                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Blog post](https://www.ansible.com/blog/testing-ansible-roles-with-docker)               |  Example `provision_docker` uses                                                                                                                                                                                                                                                                                      |
| [.travis.yml](https://github.com/chrismeyersfsu/provision_docker/blob/master/.travis.yml) | Example TravisCI                                                                                                                                                                                                                                                                                             |
| [Dockerfiles](https://github.com/chrismeyersfsu/provision_docker/tree/master/files)       | Curated Docker images with init system (so the `service` module works) and ssh daemon.<br> `chrismeyers/centos6` <br>`chrismeyers/centos7` <br>`chrismeyers/ubuntu12.04` <br>`ubuntu-upstart:14.04`                                                                                                                                        |
| [test/playbook_*.yml](https://github.com/chrismeyersfsu/provision_docker/tree/master/test) <br>[role-install_mongod](https://github.com/chrismeyersfsu/role-install_mongod) <br>[role-ansible_deps](https://github.com/chrismeyersfsu/role-ansible_deps) <br>[role-iptables](https://github.com/chrismeyersfsu/role-iptables) | Example `provision-docker` projects and uses.|

### **NEW** docker_connection
Works with docker for Mac, VirtualBox, VMware Fusion, docker native. Using docker_connection does not require any routing rules.
```
# inventory
[robots]
optimus image="chrismeyers/ubuntu12.04"
bumblebee image="ubuntu-upstart:14.04"
```
```yaml
# test.yml
- name: Bring up docker containers for docker connection inventory iface
  hosts: localhost
  roles:
    - role: provision_docker
      provision_docker_privileged: true,
      provision_docker_inventory_group: "{{ groups['robots'] }}"
      provision_docker_use_docker_connection: true

- hosts: robots
  tasks:
    - name: "Say hello to my new containers"
      ping:
```

| parameter                              	| required 	| default             	| choices                                                                                    	| comments                                                                                                                                                                                                                           	|
|----------------------------------------	|----------	|---------------------	|--------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| provision_docker_image                 	| no       	| chrismeyers/centos6 	| chrismeyers/centos6 chrismeyers/centos7 chrismeyers/ubuntu12.04 ubuntu-upstart:14.04 other 	| Docker image to use when starting the container. The containers listed to the left are special. The init system put back in and ssh is started. This allows for starting/stopping service via the `service` module as well as ssh. 	|
| provision_docker_privileged            	| no       	| true                	| true/false                                                                                 	| Start Docker container in privileged mode.                                                                                                                                                                                         	|
| provision_docker_inventory_group       	| no       	|                     	|                                                                                            	| List of host names that are in the inventory for which to bring up a Docker container. Note that the Docker image that you wish to bring up should be a hostvar associated with the hostname.                                      	|
| provision_docker_inventory             	| no       	|                     	|                                                                                            	| List of <name, image> pairs for which to bring up a Docker container.                                                                                                                                                              	|
| provision_docker_use_docker_connection 	| no       	| false               	| true/false                                                                                 	| Use docker_connection plugin to connect to Docker containers instead of the default ssh.                                                                                                                                           	|
| provision_docker_network 	| no       	|                    	| Some name from available networks as listed with `$ docker network ls`                                                                                 	| Specify the network that the Docker container should connect to.                                                                                                                                           	|
| provision_docker_volumes 	                | no       	|       | List of volumes to mount within the container.                                                               	|  Use docker CLI-style syntax: /host:/container[:mode].                                                                                                                                            	|
| provision_docker_volumes_from 	        | no       	|     	|  List of container names or to get volumes from.                                                                                                 	|                                                                                                                                           	|




### Mac OS X + docker-machine + VMware Fusion
`sudo /sbin/route -n add -net 172.17.0.0 -netmask 255.255.0.0 -gateway $(docker-machine ip default)`

### Mac OS X + docker-machine + VirtualBox
`provision_docker` relies on being able to ssh to containers. Thus, the ip of the container must be accessible (a route must exist). If your using docker toolbox on OS X + virtualbox containers are not routed to the host. Run the below commands to be add a route to the containers in the guest VM.
```
/usr/sbin/scutil -w State:/Network/Interface/vboxnet0/IPv4 -t 0
sudo /sbin/route -n add -net 172.17.0.0 -netmask 255.255.0.0 -gateway $(docker-machine ip)
```
The route does not persist across reboots. To persist the changes edit `/Library/LaunchDaemons/com.docker.route.plist`

```
<?xml version='1.0' encoding='UTF-8'?>
<!DOCTYPE plist PUBLIC '-//Apple//DTD PLIST 1.0//EN' 'http://www.apple.com/DTDs/PropertyList-1.0.dtd'>
<plist version='1.0'>
<dict>
  <key>Label</key>
  <string>com.docker.route</string>
  <key>ProgramArguments</key>
  <array>
    <string>bash</string>
    <string>-c</string>
    <!-- You need to adapt the vboxnet0 to the interface that suits your setup, use ifconfig to find it -->
    <string>/usr/sbin/scutil -w State:/Network/Interface/vboxnet0/IPv4 -t 0;sudo /sbin/route -n add -net 172.17.0.0 -netmask 255.255.0.0 -gateway 192.168.99.100</string>
  </array>
  <key>KeepAlive</key>
  <false/>
  <key>RunAtLoad</key>
  <true/>
  <key>LaunchOnlyOnce</key>
  <true/>
</dict>
</plist>
```

## Similar Work

* https://github.com/metacloud/molecule
* https://github.com/AerisCloud/ansible-role-test
* http://www.jeffgeerling.com/blog/testing-ansible-roles-travis-ci-github
* https://github.com/geerlingguy/ansible-role-apache
* https://github.com/neillturner/kitchen-ansible

## Projects Using provision_docker

* https://github.com/mbreisch/ssh-role
* https://github.com/mbreisch/ufw-role
* https://github.com/mbreisch/ssmtp-role
* https://github.com/mbreisch/deploy-user-role
* https://github.com/mbreisch/s3cmd-role
* https://github.com/mbreisch/unattended-upgrades-role/tree/master/tests
* https://github.com/Maarc/ansible-role-redhat-jboss-common
* https://github.com/sderen/ansible-grafana
* https://github.com/sderen/ansible-nginxgunicorn
* https://github.com/Maarc/ansible-role-redhat-jboss-web-server-httpd
* https://github.com/Maarc/ansible-role-redhat-jboss-web-server-tomcat
* https://github.com/Maarc/ansible-role-redhat-jboss-eap
* https://github.com/rhtconsulting/jboss_fuse
* https://github.com/rhtconsulting/jboss_bxms
* https://github.com/mlanin/ansible-laravel5/tree/master/roles/carlosbuenosvinos.ansistrano-deploy
* https://github.com/Maarc/ansible-role-redhat-jboss-common
* https://github.com/turkenh/ansible-role-parse-mongodb
* https://github.com/tomashavlas/ansible-role-users_profiles
* https://github.com/tomashavlas/ansible-role-system_users
* https://github.com/tomashavlas/ansible-role-authorized_keys
* https://github.com/tomashavlas/ansible-role-sudo
* https://github.com/tomashavlas/ansible-role-system_groups
* https://github.com/rhevm-qe-automation/ovirt-ansible
* https://github.com/rhevm-qe-automation/ansible-role-seal
