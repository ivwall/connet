
blog.oddbit.com/post/2018-03-12-using-docker-macvlan-networks

sudo docker network create -d macvlan -o parent=eno1 --subnet 10.10.89.0/25 --gateway 10.10.89.1 connet
