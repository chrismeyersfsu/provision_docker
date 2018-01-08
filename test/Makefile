.PHONY: cloud inventory docker_inventory docker_cloud groups clean

containers = provision_docker_host_one provision_docker_host_two provision_docker_host_three provision_docker_host_four provision_docker_host_five optimus ironhide megatron starscreamo hcwohl

all: cloud inventory docker_inventory docker_cloud groups network_mode docker_links docker_publish docker_volumes_inventory docker_volumes_cloud

clean_command = docker rm -f $(containers) || true

cloud:
	$(clean_command)
	ansible-playbook -i inventory playbook_cloud_iface.yml

inventory:
	$(clean_command)
	ansible-playbook -i inventory playbook_inventory_iface.yml

docker_inventory:
	$(clean_command)
	ansible-playbook -i inventory playbook_inventory_iface_docker_connection.yml

docker_cloud:
	$(clean_command)
	ansible-playbook -i inventory playbook_cloud_iface_docker_connection.yml

groups:
	$(clean_command)
	ansible-playbook -i inventory groups.yml

network_mode:
	$(clean_command)
	ansible-playbook -i inventory playbook_verify_network.yml

docker_links:
	$(clean_command)
	ansible-playbook -i inventory playbook_verify_links.yml

docker_volumes_inventory:
	$(clean_command)
	ansible-playbook -i inventory playbook_inventory_iface_volumes.yml

docker_volumes_cloud:
	$(clean_command)
	ansible-playbook -i inventory playbook_cloud_iface_volumes.yml

docker_publish:
	$(clean_command)
	ansible-playbook -i inventory playbook_verify_publish.yml

clean:
	$(clean_command)
