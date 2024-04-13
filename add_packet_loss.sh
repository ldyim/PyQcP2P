sudo tc qdisc add dev eth0 root netem loss 5%
tc -s qdisc
