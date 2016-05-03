[![Build Status](https://travis-ci.org/chrismeyersfsu/provision_docker.svg?branch=master)](https://travis-ci.org/chrismeyersfsu/provision_docker)


# provision_docker 
An Ansible role used to create and start docker containers for each inventory host used in a play. Useful for testing.

[Blog post](https://www.ansible.com/blog/testing-ansible-roles-with-docker) on how to use `provision_docker` to test roles.

Recomended docker images.
```
chrismeyers/centos6
chrismeyers/centos7
chrismeyers/ubuntu12.04
ubuntu-upstart:14.04
```
**Note:** The above listed images [Dockerfiles](https://github.com/chrismeyersfsu/provision_docker/blob/master/files/) are designed to run an init systems and openssh.

## Example Playbook

* [main.yml](https://github.com/chrismeyersfsu/provision_docker/blob/master/test/main.yml)
* [role-install_mongod](https://github.com/chrismeyersfsu/role-install_mongod)
* [role-ansible_deps](https://github.com/chrismeyersfsu/role-ansible_deps)
* [role-iptables](https://github.com/chrismeyersfsu/role-iptables)

## Testing w/ Travis-CI
Take a look at [.travis.yml](https://github.com/chrismeyersfsu/provision_docker/blob/master/.travis.yml) to see how to test your role using travis-ci.

## Mac OS X + docker-machine + VirtualBox
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

## Mac OS X + docker-machine + VMware Fusion
`sudo /sbin/route -n add -net 172.17.0.0 -netmask 255.255.0.0 -gateway $(docker-machine ip default)`

## Similar Work

* https://github.com/metacloud/molecule 
* https://github.com/AerisCloud/ansible-role-test
* http://www.jeffgeerling.com/blog/testing-ansible-roles-travis-ci-github
* https://github.com/geerlingguy/ansible-role-apache
* https://github.com/neillturner/kitchen-ansible
