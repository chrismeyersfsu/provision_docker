# Change Log

## [**Next release**](https://galaxy.ansible.com/mongrelion/docker)

**Closed issues:**

- Clarify supported Docker versions [\#46](https://github.com/mongrelion/ansible-role-docker/issues/46)

**Merged pull requests:**

- alternative test scenario [\#50](https://github.com/mongrelion/ansible-role-docker/pull/50) ([paulfantom](https://github.com/paulfantom))
- move tests to molecule 2.x [\#49](https://github.com/mongrelion/ansible-role-docker/pull/49) ([paulfantom](https://github.com/paulfantom))
- Add docker-common package to be removed before installation [\#48](https://github.com/mongrelion/ansible-role-docker/pull/48) ([lukas-bednar](https://github.com/lukas-bednar))
- better docker\_version support [\#47](https://github.com/mongrelion/ansible-role-docker/pull/47) ([paulfantom](https://github.com/paulfantom))

## [0.1.1](https://galaxy.ansible.com/mongrelion/docker) (2018-05-01)
**Closed issues:**

- docker-compose ? [\#39](https://github.com/mongrelion/ansible-role-docker/issues/39)
- Adding user\(s\) to docker group [\#38](https://github.com/mongrelion/ansible-role-docker/issues/38)
- Auto-release? [\#34](https://github.com/mongrelion/ansible-role-docker/issues/34)
- Unify variable naming [\#32](https://github.com/mongrelion/ansible-role-docker/issues/32)
- Move away from installation script [\#31](https://github.com/mongrelion/ansible-role-docker/issues/31)
- Can we start Tagging releases please [\#27](https://github.com/mongrelion/ansible-role-docker/issues/27)
- Support for proxy in docker daemon is missing [\#25](https://github.com/mongrelion/ansible-role-docker/issues/25)
- `docker daemon` is not supported on Linux. Please run `dockerd` directly [\#22](https://github.com/mongrelion/ansible-role-docker/issues/22)
- Integration tests [\#13](https://github.com/mongrelion/ansible-role-docker/issues/13)

**Merged pull requests:**

- Typo: variable name reference [\#44](https://github.com/mongrelion/ansible-role-docker/pull/44) ([giannidallatorre](https://github.com/giannidallatorre))
- Automatically create releases and changelog [\#43](https://github.com/mongrelion/ansible-role-docker/pull/43) ([paulfantom](https://github.com/paulfantom))
- Allow adding users to docker group for priviledged access [\#42](https://github.com/mongrelion/ansible-role-docker/pull/42) ([paulfantom](https://github.com/paulfantom))
- docker-compose support [\#41](https://github.com/mongrelion/ansible-role-docker/pull/41) ([paulfantom](https://github.com/paulfantom))
- readme update [\#40](https://github.com/mongrelion/ansible-role-docker/pull/40) ([paulfantom](https://github.com/paulfantom))
- ansible 2.5 [\#37](https://github.com/mongrelion/ansible-role-docker/pull/37) ([paulfantom](https://github.com/paulfantom))
- Remove installation script [\#36](https://github.com/mongrelion/ansible-role-docker/pull/36) ([paulfantom](https://github.com/paulfantom))
- Cleanup [\#35](https://github.com/mongrelion/ansible-role-docker/pull/35) ([paulfantom](https://github.com/paulfantom))
- integration tests [\#30](https://github.com/mongrelion/ansible-role-docker/pull/30) ([paulfantom](https://github.com/paulfantom))
- Change location of systemd service file [\#28](https://github.com/mongrelion/ansible-role-docker/pull/28) ([paulfantom](https://github.com/paulfantom))

## [0.1.0](https://galaxy.ansible.com/mongrelion/docker) (2018-03-20)
**Implemented enhancements:**

- any plans to support for Ubuntu 14.04, 16.04 ? [\#3](https://github.com/mongrelion/ansible-role-docker/issues/3)
- Support different versions of Docker Engine with official Docker and Rancher setup scripts [\#12](https://github.com/mongrelion/ansible-role-docker/pull/12) ([marcusianlevine](https://github.com/marcusianlevine))
- Syntax change and some variables [\#2](https://github.com/mongrelion/ansible-role-docker/pull/2) ([brucellino](https://github.com/brucellino))

**Fixed bugs:**

- Deploy breaks in 1.12 b/c docker.socket no longer part of distro [\#1](https://github.com/mongrelion/ansible-role-docker/issues/1)

**Closed issues:**

- md5sum of docker setup script changed. [\#19](https://github.com/mongrelion/ansible-role-docker/issues/19)
- Role blocks when docker is already installed [\#16](https://github.com/mongrelion/ansible-role-docker/issues/16)
- docker\_storagedriver is not expanded correctly [\#7](https://github.com/mongrelion/ansible-role-docker/issues/7)

**Merged pull requests:**

- Proxy Settings for docker [\#29](https://github.com/mongrelion/ansible-role-docker/pull/29) ([ageekymonk](https://github.com/ageekymonk))
- Using dockerd as docker daemon has been deprecated [\#24](https://github.com/mongrelion/ansible-role-docker/pull/24) ([ageekymonk](https://github.com/ageekymonk))
- Limit reloading the systemctl daemon to distributions using systemd [\#21](https://github.com/mongrelion/ansible-role-docker/pull/21) ([zanewestover](https://github.com/zanewestover))
- Add yum-utils as dependency [\#20](https://github.com/mongrelion/ansible-role-docker/pull/20) ([petr-balogh](https://github.com/petr-balogh))
- Since 17.06.2 md5 checksum changed to new one [\#18](https://github.com/mongrelion/ansible-role-docker/pull/18) ([petr-balogh](https://github.com/petr-balogh))
- Only run install script when docker is not installed [\#17](https://github.com/mongrelion/ansible-role-docker/pull/17) ([mhutter](https://github.com/mhutter))
- Use 17.06 as default version [\#15](https://github.com/mongrelion/ansible-role-docker/pull/15) ([mhutter](https://github.com/mhutter))
- Make daemon.json settings configurable [\#10](https://github.com/mongrelion/ansible-role-docker/pull/10) ([mhutter](https://github.com/mhutter))
- Added support for Ubuntu 17.04 repo [\#9](https://github.com/mongrelion/ansible-role-docker/pull/9) ([snoby](https://github.com/snoby))
- \(resolve conflict in dbichko's fork\) set debian repository based on major version only [\#8](https://github.com/mongrelion/ansible-role-docker/pull/8) ([nerab](https://github.com/nerab))
- Only update apt-cache when needed [\#4](https://github.com/mongrelion/ansible-role-docker/pull/4) ([drwahl](https://github.com/drwahl))



\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*