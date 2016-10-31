.PHONY: cloud inventory docker_inventory docker_cloud groups clean

containers = provision_docker_host_one provision_docker_host_two provision_docker_host_three provision_docker_host_four provision_docker_host_five optimus ironhide megatron starscream

all: cloud inventory docker_inventory docker_cloud groups

cloud:
	docker rm -f $(containers) || true
	ansible-playbook -i inventory playbook_cloud_iface.yml

inventory:
	docker rm -f $(containers) || true
	ansible-playbook -i inventory playbook_inventory_iface.yml

docker_inventory:
	docker rm -f $(containers) || true
	ansible-playbook -i inventory playbook_inventory_iface_docker_connection.yml

docker_cloud:
	docker rm -f $(containers) || true
	ansible-playbook -i inventory playbook_cloud_iface_docker_connection.yml

groups:
	docker rm -f $(containers) || true
	ansible-playbook -i inventory groups.yml

clean:
	docker rm -f $(containers) || true
