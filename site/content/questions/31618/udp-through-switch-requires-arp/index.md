+++
type = "question"
title = "UDP through Switch requires ARP?"
description = '''Hello networks gurus, I try to achieve UDP transmission between my PC and PCB which has Ethernet Physical Layer chip. They are connected through Switch. I send UDP packets from PC ( 192.168.0.162 192.168.0.222 Length: 46 Source port: 55005 Destination port: 20678 (tool to send packets: http://packet...'''
date = "2014-04-08T02:27:00Z"
lastmod = "2014-04-08T07:22:00Z"
weight = 31618
keywords = [ "arp", "udp", "physical" ]
aliases = [ "/questions/31618" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UDP through Switch requires ARP?](/questions/31618/udp-through-switch-requires-arp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31618-score" class="post-score" title="current number of votes">0</div><span id="post-31618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello networks gurus,</p><p>I try to achieve UDP transmission between my PC and PCB which has Ethernet Physical Layer chip. They are connected through Switch. I send UDP packets from PC ( 192.168.0.162 192.168.0.222 Length: 46 Source port: 55005 Destination port: 20678 (tool to send packets: <a href="http://packetsender.com/)).">http://packetsender.com/)).</a> But any of these packets appears on PCB (I check if any packet with source port 55005 is available).</p><p>I don't understand networking very good, but I think it may be because these packets are blocked on Switch and the reason is that I don't have ARP protocol implemented on my PCB. I see in Wireshark that my PC sends ARP to ask who is 192.168.0.222, but has no response. Is that correct? ARP should be always implemented?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-physical" rel="tag" title="see questions tagged &#39;physical&#39;">physical</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '14, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/152b7c29ede1135a40bccbea0fd8817e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dansci&#39;s gravatar image" /><p><span>dansci</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dansci has no accepted answers">0%</span></p></div></div><div id="comments-container-31618" class="comments-container"></div><div id="comment-tools-31618" class="comment-tools"></div><div class="clear"></div><div id="comment-31618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31623"></span>

<div id="answer-container-31623" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31623-score" class="post-score" title="current number of votes">1</div><span id="post-31623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, ARP must be implemented, or the IP stack of the sender has no way of finding the destination MAC address to send the packet to.</p><p>This is sort of like only writing a name on a letter, but no street address/zip code/town. The post office has no chance to deliver the letter because it doesn't know where it has to go to.</p><p>BTW, just in case: for IPv6 you could leave ARP out because it is not used for IPv6 anymore, but you'd have to implement ICMPv6 instead, which is more complicated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '14, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31623" class="comments-container"><span id="31636"></span><div id="comment-31636" class="comment"><div id="post-31636-score" class="comment-score"></div><div class="comment-text"><p>Thanks.</p><p>Because it is FPGA, the simpler is better, I will stay with IPv4. In such a configuration I have to assign some MAC and IP to my device.</p><p>IP will be one from my LAN, but other PCs in LAN use DHCP config. Will it be wise enough to don't offer IP which is used already in LAN or the range of allowed/not-allowed IPs must be configured on DHCP server?</p><p>I know that there are some restrictions on MAC numbers. Can I use some artificial MAC in my network e.g. 11:22:33:44:55:66 ? Is there any non-restricted range of MAC addresses?</p></div><div id="comment-31636-info" class="comment-info"><span class="comment-age">(08 Apr '14, 07:13)</span> <span class="comment-user userinfo">dansci</span></div></div><span id="31638"></span><div id="comment-31638" class="comment"><div id="post-31638-score" class="comment-score">1</div><div class="comment-text"><p>If your device is not capable of answering to gratuitous ARP requests (which are used to check for duplicate IP addresses on the network) you should exclude the static IP of your device from the DHCP range.</p><p>You can use artificial MAC addresses as long as there is no collision with another system having the same address in the local network. And you should stay away from special MACs like those for Multicast and Broadcast.</p><p>By the way, here's the list of MAC ranges that are already in use (first three octets are the vendor octets):</p><p><a href="http://standards.ieee.org/develop/regauth/oui/oui.txt">http://standards.ieee.org/develop/regauth/oui/oui.txt</a></p></div><div id="comment-31638-info" class="comment-info"><span class="comment-age">(08 Apr '14, 07:22)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-31623" class="comment-tools"></div><div class="clear"></div><div id="comment-31623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

