+++
type = "question"
title = "capture port-mirrored(SPAN) traffic on a VM where interface is bridged with tap interface on host"
description = '''First of all, sorry about bit clunky title. Tried to make it as informational as possible. I have a following topology in GNS3:  &quot;SW&quot; is a Cisco 3640 router with NM-16ESW 16-port 10/100 EtherSwitch Network Module. Port Fa0/0 of &quot;SW&quot; is an access port in VLAN 5. I have mirrored both Rx and Tx traffic...'''
date = "2013-02-18T15:13:00Z"
lastmod = "2013-02-19T08:28:00Z"
weight = 18722
keywords = [ "cisco", "tap", "virtualbox" ]
aliases = [ "/questions/18722" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture port-mirrored(SPAN) traffic on a VM where interface is bridged with tap interface on host](/questions/18722/capture-port-mirroredspan-traffic-on-a-vm-where-interface-is-bridged-with-tap-interface-on-host)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18722-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>First of all, sorry about bit clunky title. Tried to make it as informational as possible.</p><p>I have a following topology in <a href="http://www.gns3.net/">GNS3</a>:</p><p><img src="http://i.imgur.com/OYk7PLR.png" alt="http://i.imgur.com/OYk7PLR.png" /></p><p>"SW" is a Cisco 3640 router with NM-16ESW 16-port 10/100 EtherSwitch Network Module. Port Fa0/0 of "SW" is an access port in VLAN 5. I have mirrored both Rx and Tx traffic of port Fa0/0 to port Fa0/10:</p><pre><code>SW#sh run | i monit
monitor session 1 source interface Fa0/0
monitor session 1 destination interface Fa0/10
SW#sh monitor session 1
Session 1
---------
Source Ports:
    RX Only:       None
    TX Only:       None
    Both:          Fa0/0
Source VLANs:
    RX Only:       None
    TX Only:       None
    Both:          None
Destination Ports: Fa0/10
Filter VLANs:      None

SW#</code></pre><p>There is a Debian VM running Wireshark 1.2.11 listening on eth2 interface which is bridged with tap0 interface in Virtualbox configuration. VM eth2 interface is connected to port Fa0/10. Now if I telnet to "router" from "R1":</p><pre><code>R1#ping 10.10.10.2

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.10.10.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 4/7/16 ms
R1#telnet 10.10.10.2
Trying 10.10.10.2 ... Open

router&gt;exit

[Connection to 10.10.10.2 closed by foreign host]
R1#</code></pre><p>..I expect to see ARP, ICMP and IP traffic in Wireshark output. However, I capture only SPT and CDP traffic:</p><p><img src="http://i.imgur.com/DqcerQ8.png" alt="http://i.imgur.com/DqcerQ8.png" /></p><p>Any ideas what might cause this?</p></div><div id="question-tags" class="tags-container tags">cisco tap virtualbox</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '13, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/c153148e19e1e7c04c48a2a5c4f68b54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrtn&#39;s gravatar image" /><p>mrtn<br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrtn has no accepted answers">0%</span></p></img></div></div><div id="comments-container-18722" class="comments-container"></div><div id="comment-tools-18722" class="comment-tools"></div><div class="clear"></div><div id="comment-18722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18739"></span>

<div id="answer-container-18739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18739-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>within GNS3 you can capture traffic directly on the network connections (If Wireshark is installed on your GNS3 'host'). To figure out if the SPAN port works, capture traffic on Fa0/10 in GNS3. Select the connection, then right click and choose "capture". See here: <a href="http://www.youtube.com/watch?v=4JMPia7jW2U">http://www.youtube.com/watch?v=4JMPia7jW2U</a></p><ul><li><p>If you see the mirrored traffic on Fa0/10, you might have a problem with Virtualbox or the NIO connection to the Switch.</p></li><li><p>If you don't see the mirrored traffic on Fa0/10, there might be a problem with the SPAN feature of your switch module (firmware related) or with GNS3 itself !?!</p></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '13, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 19 Feb '13, 08:31</p></div></div><div id="comments-container-18739" class="comments-container"></div><div id="comment-tools-18739" class="comment-tools"></div><div class="clear"></div><div id="comment-18739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

