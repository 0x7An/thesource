## Hacking in box

This is a Vagrant Box with some development stack to create new development environments.

## OS: 
  'ubuntu/zesty64' # 17.04

### Settings for Ruby on Rails
  1.RVM   1.26.11
  2.Ruby  2.4.1
  3.Rails 4.2.1

### Postgres
  Todo 

## Elastic Stack
  Elasticsearch 1.4
  Kibana        3.1.2
  Logstash      1.4

### Settings for Anaconda  
  Todo

## Installation

1. Install [VirtualBox](http://www.virtualbox.org/)

1. Install [Vagrant](http://www.vagrantup.com/)

1. Run the following commands in a folder of your choice:

    ```
    vagrant init
    vagrant up
    ```

    This will download the Vagrant box and get it running.

## Getting started

1. Once you have installed the box as described above, SSH into the box:

    ```
    vagrant ssh
