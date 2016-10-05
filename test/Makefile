.PHONY: main groups

containers = provision_docker_host_one provision_docker_host_two provision_docker_host_three provision_docker_host_four optimus ironhide megatron starscream \
provision_docker_host_docker_conn_one provision_docker_host_docker_conn_two provision_docker_host_docker_conn_three provision_docker_host_docker_conn_four provision_docker_host_five

all: main groups

main:
	docker stop $(containers) || true
	ansible-playbook -i inventory main.yml

groups:
	docker stop $(containers) || true
	ansible-playbook -i inventory groups.yml
