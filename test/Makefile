.PHONY: main groups

all: main groups

main:
	ansible-playbook -i inventory main.yml 
groups:
	docker stop optimus ironhide megatron starscream || true
	ansible-playbook -i inventory groups.yml
