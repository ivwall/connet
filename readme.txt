-----------

   blog.oddbit.com/post/2018-03-12-using-docker-macvlan-networks
   mxtoolbox.com/SubnetCalculator.aspx
   Input/CIDR :  10.10.89.0/25
   Range                  0 - 127

   rakhesh.com/docker/docker-host-unable-to-talk-to-container-on-macvlan-network

   -- commands executed
   sudo docker network create -d macvlan -o parent=eno1 --subnet 10.10.89.0/25 --gateway 10.10.89.1 connet


  426  sudo docker run --net=connet --ip=10.10.89.127 -itd alpine /bin/sh
  427  sudo docker run --net=connet --ip=10.10.89.126 -itd alpine /bin/sh
  428  sudo docker ps
  429  ip a
  431  sudo ip link add mac0 link eno1 type macvlan mode bridge
  434  sudo ip addr add 10.10.89.0/25 dev mac0
  443  sudo ip link set dev mac0 up
 
