## Launch script

Tested on Ubuntu. Uncomment lines before running.

```
#!/bin/bash

#Ubuntu
#echo "sudo su" > /home/ubuntu/su.sh
#chmod +x su.sh

echo "tail -f /var/log/cloud-init-output.log" > /root/tail.sh
chmod +x /root/tail.sh

curl -O https://raw.githubusercontent.com/GlynnKershaw/openvpn-aws/master/install.sh
bash install.sh
```
