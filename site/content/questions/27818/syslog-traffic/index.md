+++
type = "question"
title = "syslog traffic"
description = '''If I am capturing with wireshark on 192.168.2.10/22 computer, which is connected to a non-mirrored port of the switch, should I be seeing Syslog traffic sourced from 192.168.5.1/24 which has 192.168.3.100/22 as destination? Inter vlan routing is allowed between subnets.'''
date = "2013-12-05T07:45:00Z"
lastmod = "2014-01-05T05:52:00Z"
weight = 27818
keywords = [ "syslog" ]
aliases = [ "/questions/27818" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [syslog traffic](/questions/27818/syslog-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27818-score" class="post-score" title="current number of votes">0</div><span id="post-27818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I am capturing with wireshark on 192.168.2.10/22 computer, which is connected to a non-mirrored port of the switch, should I be seeing Syslog traffic sourced from 192.168.5.1/24 which has 192.168.3.100/22 as destination? Inter vlan routing is allowed between subnets.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-syslog" rel="tag" title="see questions tagged &#39;syslog&#39;">syslog</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '13, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p><span>net_tech</span><br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Dec '13, 08:10</strong> </span></p></div></div><div id="comments-container-27818" class="comments-container"></div><div id="comment-tools-27818" class="comment-tools"></div><div class="clear"></div><div id="comment-27818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27823"></span>

<div id="answer-container-27823" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27823-score" class="post-score" title="current number of votes">2</div><span id="post-27823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="net_tech has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>should I be seeing Syslog traffic</p></blockquote><p>Only in the following cases</p><ul><li>you believe there is no port mirroring enabled, but it is!</li><li>The Wireshark PC is the <strong>same</strong> system as the syslog server and IP 192.168.2.10 is just a secondary address on that system.</li><li>traffic to 192.168.3.100 is sent to the broadcast MAC address (ff:ff:ff:ff:ff:ff), which would be rather silly.</li><li>traffic to 192.168.3.100 is sent to a multicast MAC address (first bit of first octet eq 1). In that case the switch will flood the packet to every port in the VLAN. Reason for a multicast MAC: Some cluster software on the server 192.168.3.100 or a load balancer that handles the IP.</li><li>The switch does not know the MAC address/port relation for 192.168.3.100 (CAM table timeout) and thus it must flood the packet to every port in the VLAN. This will happen only once in a while.</li><li>The switch got flooded with (fake) MAC addresses, causing a CAM table overflow, and thus it switched to 'fail-open mode' which makes it basically a HUB. Reason: A bogus device or an attacker.</li><li>a bug in the switch firmware</li></ul><p>In all other cases you should <strong>not</strong> see that traffic in Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '13, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Dec '13, 13:27</strong> </span></p></div></div><div id="comments-container-27823" class="comments-container"><span id="27825"></span><div id="comment-27825" class="comment"><div id="post-27825-score" class="comment-score"></div><div class="comment-text"><p>none of the cases apply, but based on your answer I think it's a problem with inter vlan routing configured on the switch.</p></div><div id="comment-27825-info" class="comment-info"><span class="comment-age">(05 Dec '13, 08:42)</span> <span class="comment-user userinfo">net_tech</span></div></div><span id="27831"></span><div id="comment-27831" class="comment"><div id="post-27831-score" class="comment-score"></div><div class="comment-text"><p>this is not related to (any form of) routing. If you see a frame on a switch port where is should not appear is solely a switch problem, according to the reasons I mentioned above.</p></div><div id="comment-27831-info" class="comment-info"><span class="comment-age">(05 Dec '13, 09:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="27835"></span><div id="comment-27835" class="comment"><div id="post-27835-score" class="comment-score"></div><div class="comment-text"><p>since you edited your post with an additional case "a bug in the switch firmware". I am gonna go with it.</p><p>a mac address for 192.168.3.100 was not in switches ARP table, pinging 192.168.3.100 from the switch added the mac address to the arp table on the switch and prevented <strong>ALL</strong> network devices from seeing syslog traffic except for the device it was destined to.</p></div><div id="comment-27835-info" class="comment-info"><span class="comment-age">(05 Dec '13, 10:26)</span> <span class="comment-user userinfo">net_tech</span></div></div><span id="28584"></span><div id="comment-28584" class="comment"><div id="post-28584-score" class="comment-score"></div><div class="comment-text"><p>Here is an update on the issue. Since syslog messages are sent over UDP, 192.168.5.1/24 does not receive any acknowledgments from 192.168.3.100 and MAC address of 192.168.3.100 falls out of the MAC address table after a default time out. I said ARP table in my previous post, but I meant MAC table of the switch. According to Cisco tech support this is normal behavior and the only solution to this nuisance is to PING 192.168.3.100 from any system on either of the subnets, which by the way live on the same switch.</p></div><div id="comment-28584-info" class="comment-info"><span class="comment-age">(05 Jan '14, 05:52)</span> <span class="comment-user userinfo">net_tech</span></div></div></div><div id="comment-tools-27823" class="comment-tools"></div><div class="clear"></div><div id="comment-27823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

