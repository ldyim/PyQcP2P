tc qdisc add dev eth0 root netem loss 10%
tc -s qdisc
