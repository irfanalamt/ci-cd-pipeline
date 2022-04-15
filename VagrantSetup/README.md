# Setup

Here Vagrant is used to create and manage virtual machines using code.
In the Vagrantfile we defined our configuration.

1. Install Vagrant
   `https://www.vagrantup.com/docs/installation`
2. Install VirtualBox
   `https://www.virtualbox.org/wiki/Downloads`
3. Start Vagrant environment and provision VM's
   `vagrant up`
4. SSH into control node
   `vagrant ssh control` //Default password = vagrant
5. Copy host file into control station hostfile
   `sudo cp /vagrant/hosts /etc/hosts`
6. Navigate to vagrant folder of control node
   `cd /vagrant`
7. Generate keypair to make hosts ssh accessible
   `ssh-keygen`
8. Copy SSH keys to servers
   `ssh-copy-id node1 && ssh-copy-id node2`
9. Test SSH access
   `ssh vagrant@node1`
10. To stop and delete everything
    `vagrant destroy -f`
11. SUCCESS!
