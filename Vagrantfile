# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.define "instance1" do |instance1|
      instance1.vm.box = "ubuntu/trusty64"
      instance1.vm.network "private_network", ip: "192.168.1.10"
  end
  config.vm.define "instance2" do |instance2|
      instance2.vm.box = "ubuntu/trusty64"
      instance2.vm.network "private_network", ip: "192.168.1.20"
  end
end
