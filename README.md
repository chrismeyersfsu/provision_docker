[![Build Status](https://travis-ci.org/mongrelion/ansible-role-docker.svg?branch=master)](https://travis-ci.org/mongrelion/ansible-role-docker)

docker
=========

Install Docker

Requirements
------------

None

Role Variables
--------------

```
- vars:
  docker_rc: no # no by default. Set to yes to install the latest Docker version (release candidates and such)
```

Dependencies
------------

None

Example Playbook
----------------
Install vanilla Docker
```
- hosts: servers
  roles:
     - mongrelion.docker
```

Install testing release of Docker
```
- hosts: servers
  roles:
     - { role: mongrelion.docker, docker_rc: yes }
```

License
-------

MIT

Author Information
------------------

You can find me on Twitter: [@mongrelion](https://twitter.com/mongrelion)
