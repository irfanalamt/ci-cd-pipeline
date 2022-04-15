# Setup

Here Ansible is used to configure our servers.

Currently we are in the terminal of control node.

1. Navigate to our AnsibleSetup folder in the control node
   `cd /vagrant/AnsibleSetup`
2. Update package lists
   `sudo apt-get update`
3. Install Ansible dependencies
   `sudo apt-get install ansible -y`
4. Test Ansible connectivity using ad hoc command
   `ansible nodes -i myhosts -m command -a hostname`
5. Install python simple-json on hosts
   `ansible nodes -i myhosts -m command -a 'sudo apt-get -y install python-simplejson'`
6. Run the playbook
   `ansible-playbook -i myhosts -K playbook1.yml`
7. SUCCESS!
