.PHONY: main groups

all: main groups

main:
	docker stop provision_docker_host_one provision_docker_host_two provision_docker_host_three optimus ironhide megatron starscream || true
	ansible-playbook -i inventory main.yml 

groups:
	docker stop provision_docker_host_one provision_docker_host_two provision_docker_host_three optimus ironhide megatron starscream || true
	ansible-playbook -i inventory groups.yml
