.PHONY: cloud inventory docker_inventory docker_cloud groups clean

containers = provision_docker_host_one provision_docker_host_two provision_docker_host_three provision_docker_host_four provision_docker_host_five optimus ironhide megatron starscream

all: cloud inventory docker_inventory docker_cloud groups network_mode docker_links docker_volumes_inventory docker_volumes_cloud

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

network_mode:
	docker rm -f $(containers) || true
	ansible-playbook -i inventory playbook_verify_network.yml

docker_links:
	docker rm -f $(containers) || true
	ansible-playbook -i inventory playbook_verify_links.yml

docker_volumes_inventory: clean
	ansible-playbook -i inventory playbook_inventory_iface_volumes.yml

docker_volumes_cloud: clean
	ansible-playbook -i inventory playbook_cloud_iface_volumes.yml

clean:
	docker rm -f $(containers) || true
