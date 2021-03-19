+++
type = "question"
title = "Help analyzing SSL"
description = '''Hi, I have an intermittent problem with SSL on our local network. We have a proxy on the network but all ssl traffic should be untouched.  The hand-off of http traffic is achieved through these iptable rules (where .23 is the proxy): iptables -t mangle -A PREROUTING -p tcp --dport 80 -j MARK --set-m...'''
date = "2013-10-08T09:12:00Z"
lastmod = "2013-10-08T10:37:00Z"
weight = 25746
keywords = [ "ssl", "ssl_connection" ]
aliases = [ "/questions/25746" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help analyzing SSL](/questions/25746/help-analyzing-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25746-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have an intermittent problem with SSL on our local network. We have a proxy on the network but all ssl traffic should be untouched.</p><p>The hand-off of http traffic is achieved through these iptable rules (where .23 is the proxy):</p><pre><code>iptables -t mangle -A PREROUTING -p tcp --dport 80 -j MARK --set-mark 3
ip rule add fwmark 3 table 2
ip route add default via 192.168.0.23 dev br0 table 2</code></pre><p>When the problem happens, I can't for example open an SSL site from Chrome, but going to Firefox magically helps. Then the trouble disappears and I can use that site again. Sometimes refreshing the page helps. Other people in the office with the same wired connections may have no problem going to the site though. Weird stuff like that.</p><p>So, I took a capture of the traffic while the problem was happening, but I can't understand due to insufficient knowledge in the area what is abnormal in the sequence.</p><p>How could I post the capture?</p><p>EDIT: I've put the capture here: <a href="https://docs.google.com/file/d/0B8FF7jZJwuoUNExMdHB2eFZ1WU0/edit?usp=sharing">https://docs.google.com/file/d/0B8FF7jZJwuoUNExMdHB2eFZ1WU0/edit?usp=sharing</a></p><p>Thanks for any help!</p></div><div id="question-tags" class="tags-container tags">ssl ssl_connection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '13, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/d4e855a28dbcc327042084be99f6147b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="surge&#39;s gravatar image" /><p>surge<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="surge has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Oct '13, 09:20</p></div></div><div id="comments-container-25746" class="comments-container"><span id="25748"></span><div id="comment-25748" class="comment"><div id="post-25748-score" class="comment-score"></div><div class="comment-text"><p>The capture file contains only traffic for the POP3S port (995). So, yes it is SSL, but unrelated to a proxy and/or a browser (chrome). Maybe a user downloaded his mail via POP3S. Are you sure you posted the right capture file?</p></div><div id="comment-25748-info" class="comment-info"><span class="comment-age">(08 Oct '13, 09:40)</span> Kurt Knochner ♦</div></div><span id="25750"></span><div id="comment-25750" class="comment"><div id="post-25750-score" class="comment-score"></div><div class="comment-text"><p>Oops, yeah, not sure what I was thinking. Should have at least looked at the remote address and seen that it's one of mine :)</p><p>Anyway, I was able capture another set, this time (i hope) more to the point.</p><p>Here it is: <a href="https://docs.google.com/file/d/0B8FF7jZJwuoUVmFzNmFrQkQ3QWc/edit?usp=sharing">https://docs.google.com/file/d/0B8FF7jZJwuoUVmFzNmFrQkQ3QWc/edit?usp=sharing</a></p><p>I already see that the proxy somehow wedges in on the ssl conversation ("Gremlins ate your request" is a message from our proxy), but i'm not sure why.</p><p>Thanks for any insight.</p></div><div id="comment-25750-info" class="comment-info"><span class="comment-age">(08 Oct '13, 10:24)</span> surge</div></div></div><div id="comment-tools-25746" class="comment-tools"></div><div class="clear"></div><div id="comment-25746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25752"></span>

<div id="answer-container-25752" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25752-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you look at the content, you will see this:</p><pre><code>400 Bad Request
Server: squid
Mime-Version: 1.0
Date: Tue, 08 Oct 2013 17:01:29 GMT
Content-Type: text/html
Content-Length: 3677
X-Squid-Error: ERR_INVALID_REQ 0
X-Cache: MISS from ipcop
Connection: close</code></pre><p>If I compare the two capture files, I can see that the HTTPS request is sent to MAC address of an Intel device (probably your proxy), while the POP3S request ist sent to a Netgear MAC address (probably your Internet router).</p><p>So, the HTTPS request <strong>is</strong> forwarded to the proxy. Looks like the iptables rules you posted are not complete.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '13, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Oct '13, 13:18</p></div></div><div id="comments-container-25752" class="comments-container"><span id="25753"></span><div id="comment-25753" class="comment"><div id="post-25753-score" class="comment-score"></div><div class="comment-text"><p>The netgear is our router, you're right.</p><blockquote><p>So, the HTTPS request is forwarded to the proxy. Looks like the posted iptables you posted is not complete. However, it could also be a wrong proxy config in the browser. Can you post a screen shot of that please?</p></blockquote><p>I'm on Linux and when I go the proxy settings, it says</p><p>"Google Chrome is using your computer's system proxy settings to connect to the network."</p><p>In my /etc/network/interfaces I have</p><pre><code>auto eth0
iface eth0 inet static
address 192.168.0.3
netmask 255.255.255.0
network 192.168.0.0
broadcast 192.168.0.255
gateway 192.168.0.1</code></pre><p>Now, the router runs ddwrt and here is the more complete set of rules from the router:</p><pre><code> echo &quot;131072&quot; &gt; /sys/module/nf_conntrack/parameters/hashsize
 iptables -t mangle -A PREROUTING -p tcp -s 192.168.0.0/24 --dport 80 -d 64.18.218.22 -j ACCEPT
 iptables -t mangle -A PREROUTING -p tcp -s 192.168.0.0/24 --dport 80 -d 199.166.4.42 -j ACCEPT
 iptables -t mangle -A PREROUTING -p tcp -s 192.168.0.0/24 --dport 80 -d 192.168.0.0/24 -j ACCEPT
 iptables -t mangle -A PREROUTING -p tcp --dport 80 -s 192.168.0.118 -j ACCEPT
 iptables -t mangle -A PREROUTING -p tcp --dport 80 -s 192.168.0.24  -j ACCEPT
 iptables -t mangle -A PREROUTING -p tcp --dport 80 -s 192.168.0.23  -j ACCEPT
 iptables -t mangle -A PREROUTING -p tcp --dport 80 -j MARK --set-mark 3
 ip rule add fwmark 3 table 2
 ip route add default via 192.168.0.23 dev br0 table 2
 prefix=/proc/sys/net/ipv4/netfilter/ip_conntrack
 echo 600 &gt; ${prefix}_generic_timeout
 echo 1800 &gt; ${prefix}_udp_timeout
 echo 1800 &gt; ${prefix}_udp_timeout_stream
 echo 3600 &gt; ${prefix}_tcp_timeout_established
 echo 120 &gt; ${prefix}_tcp_timeout_syn_sent
 echo 60 &gt; ${prefix}_tcp_timeout_syn_recv
 echo 120 &gt; ${prefix}_tcp_timeout_fin_wait
 echo 120 &gt; ${prefix}_tcp_timeout_time_wait
 echo 10 &gt; ${prefix}_tcp_timeout_close
 echo 60 &gt; ${prefix}_tcp_timeout_close_wait
 echo 30 &gt; ${prefix}_tcp_timeout_last_ackG</code></pre></div><div id="comment-25753-info" class="comment-info"><span class="comment-age">(08 Oct '13, 11:02)</span> surge</div></div><span id="25754"></span><div id="comment-25754" class="comment"><div id="post-25754-score" class="comment-score"></div><div class="comment-text"><p>sorry bout the formatting. the forum interface is fighting me.</p></div><div id="comment-25754-info" class="comment-info"><span class="comment-age">(08 Oct '13, 11:03)</span> surge</div></div><span id="25760"></span><div id="comment-25760" class="comment"><div id="post-25760-score" class="comment-score"></div><div class="comment-text"><p>well, those rules do not explain why the HTTPS traffic (TCP/443) is forwarded to the proxy. There must be more than just that. Can you please post the output of</p><blockquote><p>iptables-save<br />
ip route show table all<br />
ip rule show</p></blockquote><p>Some more questions:</p><ul><li>Your client is Linux. Are there iptables rules and routing rules as well?</li><li>Where did you capture the traffic?</li></ul><p>I guess you captured on the client. If so, there must be something on the client as well, because the client already sent the traffic to the proxy MAC (Intel MAC), so the iptables and routing rules on the router were not involved at all.</p></div><div id="comment-25760-info" class="comment-info"><span class="comment-age">(08 Oct '13, 13:16)</span> Kurt Knochner ♦</div></div><span id="25763"></span><div id="comment-25763" class="comment"><div id="post-25763-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but going to Firefox magically helps. <strong>Then the trouble disappears and I can use that site again</strong></p></blockquote><p>hm... that sounds like a temporary network problem, like if there was the wrong ARP entry for your default gateway. While the problem occurs, please check on your client if the ARP entry for 192.168.0.1 shows the Netgear MAC address.</p><blockquote><p>arp -an | grep 192.168.0.1</p></blockquote><p>If it's not the ARP entry, please add the information I was asking for in my last comment.</p></div><div id="comment-25763-info" class="comment-info"><span class="comment-age">(08 Oct '13, 14:00)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25752" class="comment-tools"></div><div class="clear"></div><div id="comment-25752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

