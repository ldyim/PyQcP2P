sudo tc qdisc add dev eth0 root netem delay 50ms
tc -s qdisc
