+++
type = "question"
title = "Can connect to certain hosts on segment, not others"
description = '''I have a server sitting on a 192.168.194.0/24 network and a vpn connection to 10.0.3.0/24. There is no problem with the vpn. From my server at 192.168.194.10 I can ping the inside of the remote firewall at 10.0.3.2. I can also ping a remote server at 10.0.3.7. I can also ping an XP workstation at 10...'''
date = "2013-01-11T09:13:00Z"
lastmod = "2013-01-11T12:26:00Z"
weight = 17608
keywords = [ "hosts", "icmp", "dropping", "ping", "ttl" ]
aliases = [ "/questions/17608" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can connect to certain hosts on segment, not others](/questions/17608/can-connect-to-certain-hosts-on-segment-not-others)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17608-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a server sitting on a 192.168.194.0/24 network and a vpn connection to 10.0.3.0/24. There is no problem with the vpn.</p><p>From my server at 192.168.194.10 I can ping the inside of the remote firewall at 10.0.3.2.</p><p>I can also ping a remote server at 10.0.3.7.</p><p>I can also ping an XP workstation at 10.0.3.59</p><p>I however cannot ping a printer 10.0.3.8 I cannot ping a switch at 10.0.3.6 I cannot ping another XP pc at 10.0.3.60</p><p>Locally on the server 10.0.3.7 I can ping every device mentioned so far, so they all are up, they are all valid addresses/hosts, and there are no windows firewalls or anything else blocking icmp.</p><p>10.0.3.2 and 10.0.3.8 are my two devices I'm concerned with below. I tried to ping and traceroute each from 192.168.194.10 in the following.</p><p>Pings (filtering for just ICMP):</p><pre><code>39  51.820697   192.168.194.10  10.0.3.2    ICMP    78  Echo (ping) request  id=0x0001, seq=2585/6410, ttl=128
40  51.875291   10.0.3.2    192.168.194.10  ICMP    78  Echo (ping) reply    id=0x0001, seq=2585/6410, ttl=64
41  52.822254   192.168.194.10  10.0.3.2    ICMP    78  Echo (ping) request  id=0x0001, seq=2586/6666, ttl=128
42  52.875031   10.0.3.2    192.168.194.10  ICMP    78  Echo (ping) reply    id=0x0001, seq=2586/6666, ttl=64
43  53.820667   192.168.194.10  10.0.3.2    ICMP    78  Echo (ping) request  id=0x0001, seq=2587/6922, ttl=128
44  53.873994   10.0.3.2    192.168.194.10  ICMP    78  Echo (ping) reply    id=0x0001, seq=2587/6922, ttl=64
45  54.819111   192.168.194.10  10.0.3.2    ICMP    78  Echo (ping) request  id=0x0001, seq=2588/7178, ttl=128
46  54.870133   10.0.3.2    192.168.194.10  ICMP    78  Echo (ping) reply    id=0x0001, seq=2588/7178, ttl=64
49  61.760306   192.168.194.10  10.0.3.8    ICMP    78  Echo (ping) request  id=0x0001, seq=2591/7946, ttl=128
51  66.441429   192.168.194.10  10.0.3.8    ICMP    78  Echo (ping) request  id=0x0001, seq=2592/8202, ttl=128
52  71.433282   192.168.194.10  10.0.3.8    ICMP    78  Echo (ping) request  id=0x0001, seq=2593/8458, ttl=128
53  76.441170   192.168.194.10  10.0.3.8    ICMP    78  Echo (ping) request  id=0x0001, seq=2594/8714, ttl=128</code></pre><p>Notice no replies from 10.0.3.8, just 4 requests.</p><p>Tracert to 10.0.3.8:</p><pre><code>21  22.700678   192.168.194.10  10.0.3.8    NBNS    96  Name query NBSTAT *&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;
22  24.212666   192.168.194.10  10.0.3.8    NBNS    96  Name query NBSTAT *&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;
23  25.725853   192.168.194.10  10.0.3.8    NBNS    96  Name query NBSTAT *&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;
24  27.243319   192.168.194.10  10.0.3.8    ICMP    110 Echo (ping) request  id=0x0001, seq=2614/13834, ttl=1
25  27.295349   10.0.3.8    192.168.194.10  ICMP    138 Time-to-live exceeded (Time to live exceeded in transit)
26  27.295929   192.168.194.10  10.0.3.8    ICMP    110 Echo (ping) request  id=0x0001, seq=2615/14090, ttl=1
27  27.345990   10.0.3.8    192.168.194.10  ICMP    138 Time-to-live exceeded (Time to live exceeded in transit)
28  27.346555   192.168.194.10  10.0.3.8    ICMP    110 Echo (ping) request  id=0x0001, seq=2616/14346, ttl=1
29  27.401331   10.0.3.8    192.168.194.10  ICMP    138 Time-to-live exceeded (Time to live exceeded in transit)
30  27.402140   192.168.194.10  10.0.3.8    NBNS    96  Name query NBSTAT *&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;
31  28.908360   192.168.194.10  10.0.3.8    NBNS    96  Name query NBSTAT *&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;
32  30.422128   192.168.194.10  10.0.3.8    NBNS    96  Name query NBSTAT *&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;&lt;00&gt;
33  32.886648   192.168.194.10  10.0.3.8    ICMP    110 Echo (ping) request  id=0x0001, seq=2617/14602, ttl=2
34  36.412637   192.168.194.10  10.0.3.8    ICMP    110 Echo (ping) request  id=0x0001, seq=2618/14858, ttl=2
35  40.407571   192.168.194.10  10.0.3.8    ICMP    110 Echo (ping) request  id=0x0001, seq=2619/15114, ttl=2</code></pre><p>and that continues the same up to packet 41.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags">hosts icmp dropping ping ttl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '13, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/29c58be3d3185018b724cf9f0aebf8bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Willmeister&#39;s gravatar image" /><p>Willmeister<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Willmeister has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '13, 09:23</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-17608" class="comments-container"><span id="17609"></span><div id="comment-17609" class="comment"><div id="post-17609-score" class="comment-score"></div><div class="comment-text"><p>That got real ugly when i submitted it...sorry :)</p></div><div id="comment-17609-info" class="comment-info"><span class="comment-age">(11 Jan '13, 09:14)</span> Willmeister</div></div><span id="17610"></span><div id="comment-17610" class="comment"><div id="post-17610-score" class="comment-score">1</div><div class="comment-text"><p>Set the text as a "code sample", so it should be easier to read now.</p></div><div id="comment-17610-info" class="comment-info"><span class="comment-age">(11 Jan '13, 09:25)</span> cmaynard ♦♦</div></div><span id="17611"></span><div id="comment-17611" class="comment"><div id="post-17611-score" class="comment-score"></div><div class="comment-text"><p>I also uploaded the tracert capture to <a href="https://www.cloudshark.org/captures/4f231cf04349">https://www.cloudshark.org/captures/4f231cf04349</a></p><p>Thank you!</p></div><div id="comment-17611-info" class="comment-info"><span class="comment-age">(11 Jan '13, 09:27)</span> Willmeister</div></div></div><div id="comment-tools-17608" class="comment-tools"></div><div class="clear"></div><div id="comment-17608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17621"></span>

<div id="answer-container-17621" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17621-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>That is a thought, but they all have the same gateway. I can get to all the devices from another remote subnet.</p></blockquote><p>O.K. then the default gateway on subnet 10.0.3.0/24 is either not set correctly for all devices, or the connections from the <strong>other remote subnet</strong> are hidden (NAT) behind the internal IP of your firewall (10.0.3.2).</p><p>Can you please run tcpdump (or whatever capture tool your firewall provides) on the firewalls internal interface? If you see the ICMP request go to 10.0.3.8 (and 10.0.3.60), but you don't get a response, then the back route (default gateway) is not set correctly on those systems, <strong>or</strong> they have a wrong ARP cache entry for 10.0.3.2 (your firewall).</p><blockquote><p>I however cannot ping a printer 10.0.3.8 I cannot ping a switch at 10.0.3.6 I cannot ping another XP pc at 10.0.3.60</p></blockquote><p>Just a dump idea. Did you check, that there is no <strong>'historic'</strong> route for those IP addresses on the involved firewalls (both ends of the VPN tunnel)? However, then it probably would not work from another subnet either...</p><p>Are you really sure, there are packet filter rules to allow those packets on the involved firewalls?</p><p>To sum it up, please check these items:</p><ul><li><strong>double check</strong> (again ;-)) the default route on all systems you cannot reach (printer, switch, WinXP). Don't assume anything (or believe what you were told), just check it ;-))</li><li>check the routes on all involved firewalls, if there are <strong>old/historic</strong> routes for the IP addresses you cannot reach</li><li>check if the packet filters are set correctly on all involved firewalls</li><li>capture on the internal interface of your firewall (10.0.3.2) to verify that the ICMP requests really leave the firewall towards the target systems</li><li>check if there are wrong/old ARP cache entries on the systems you cannot reach (printer, switch and WinXP)</li><li>check if the WinXP system (10.0.3.60) has other interfaces in the subnet of your server (192.168.194.0/24), like VMware virtual interfaces (vmnet1, vmnet8): <strong><code>route print | find "192.168."</code></strong></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '13, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '13, 13:11</p></div></div><div id="comments-container-17621" class="comments-container"><span id="17629"></span><div id="comment-17629" class="comment"><div id="post-17629-score" class="comment-score"></div><div class="comment-text"><p>OK, it's a new customer and I have very limited access to their equipment, I'm on a box that i can ping the devices across the tunnel...and sure enough, gateway was incorrect. Pleaded for another look and sure enough...you have to be like House. Never trust the patient :) Thanks, good to have the extra advice coming in, sometimes you need to step back. Thank you!</p></div><div id="comment-17629-info" class="comment-info"><span class="comment-age">(11 Jan '13, 15:20)</span> Willmeister</div></div><span id="17647"></span><div id="comment-17647" class="comment"><div id="post-17647-score" class="comment-score"></div><div class="comment-text"><p>As I like to say during Sharkfest...if you hear hooves beating, think horses and not zebras (Unless you live in Africa, LOL)</p></div><div id="comment-17647-info" class="comment-info"><span class="comment-age">(12 Jan '13, 18:51)</span> hansangb</div></div></div><div id="comment-tools-17621" class="comment-tools"></div><div class="clear"></div><div id="comment-17621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17613"></span>

<div id="answer-container-17613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17613-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would guess that the devices you can't ping don't have default gateways/routers configured. So they can talk to anything on their subnet but nothing beyond the subnet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '13, 10:16</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-17613" class="comments-container"><span id="17614"></span><div id="comment-17614" class="comment"><div id="post-17614-score" class="comment-score"></div><div class="comment-text"><p>Printers typically don't get the usual "love" of PCs, so it is probably using the natural subnet mask of /8. And with proxy-arp turned off at the router (likely scenario), the return packets cannot make it back to you (can't get out of the local subnet). I would think the same is true for the XP.</p></div><div id="comment-17614-info" class="comment-info"><span class="comment-age">(11 Jan '13, 10:27)</span> hansangb</div></div><span id="17620"></span><div id="comment-17620" class="comment"><div id="post-17620-score" class="comment-score"></div><div class="comment-text"><p>That is a thought, but they all have the same gateway. PC's are getting the same ipconfig from DHCP and I can get to some, not others. It's also why i mentioned other types of devices, most notably the switch. I can get to all the devices from another remote subnet.</p></div><div id="comment-17620-info" class="comment-info"><span class="comment-age">(11 Jan '13, 12:13)</span> Willmeister</div></div></div><div id="comment-tools-17613" class="comment-tools"></div><div class="clear"></div><div id="comment-17613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

