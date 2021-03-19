+++
type = "question"
title = "ARP Broadcast"
description = '''Hello everyone, I ran analysis on a pretty complex network so that I could find the reason that all workstations run slowly when connected to the LAN but ran fine when not connected. I plugged directly in to a switch and monitored the network traffic. Upon analysis I found that one device(server) is...'''
date = "2011-11-08T06:15:00Z"
lastmod = "2011-11-08T08:36:00Z"
weight = 7277
keywords = [ "broadcast", "switch", "slow", "network" ]
aliases = [ "/questions/7277" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ARP Broadcast](/questions/7277/arp-broadcast)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7277-score" class="post-score" title="current number of votes">0</div><span id="post-7277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I ran analysis on a pretty complex network so that I could find the reason that all workstations run slowly when connected to the LAN but ran fine when not connected. I plugged directly in to a switch and monitored the network traffic.</p><p>Upon analysis I found that one device(server) is consistently sending out ARP Broadcast over the network. It does this at intervals no higher than five seconds and often twice per one second intervals.</p><p>Since all machines must listen for this broadcast could this be the culprit in my bogged down network?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadcast" rel="tag" title="see questions tagged &#39;broadcast&#39;">broadcast</span> <span class="post-tag tag-link-switch" rel="tag" title="see questions tagged &#39;switch&#39;">switch</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '11, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/3ad88a045ae41d3a93030421593e09fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Clover&#39;s gravatar image" /><p><span>Clover</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Clover has no accepted answers">0%</span></p></div></div><div id="comments-container-7277" class="comments-container"></div><div id="comment-tools-7277" class="comment-tools"></div><div class="clear"></div><div id="comment-7277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7280"></span>

<div id="answer-container-7280" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7280-score" class="post-score" title="current number of votes">2</div><span id="post-7280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A good look at ARP packets can sometimes reveal interesting things about your network. One server sending out an ARP request every few seconds is not a big issue.</p><p>Here are a few items that I check when looking at ARP packets:</p><ol><li>Is a system ARPing for the wrong subnet?</li><li>Did all systems get a proper IP address from the DHCP server, or is a system using APIPA addresses?</li><li>Are the ARP cache timers consistent with the switches MAC address table?</li><li>Is a system sending out unsolicited ARP responses?</li></ol><p>Wireshark helps in answering some of these questions. Here are a few helpful display filters:</p><ol><li><p>Say, you are analyzing a network segment where all systems should belong to the subnet 10.1.1.0/24. You can easily spot a misconfigured address mask with <strong>arp and not (arp.src.proto_ipv4 == 10.1.1.0/24 and arp.dst.proto_ipv4 == 10.1.1.0/24)</strong> This filter should not deliver any packets.</p></li><li><p>If a system did not get an IP address it will likely use a random address from the network 169.254.0.0/16. So the filter <strong>arp.src.proto_ipv4 == 169.254.0.0/16</strong> should result in an empty packet list.</p></li><li><p>The inconsistent timers can hit you quite hard if a system has more than one NIC. That happens if packets arrive on one interface and are acknowledged with a different MAC source address. The endpoint and conversation statistics show, if one MAC address is constantly receiving traffic, but not sending.</p></li><li>For advanced statistics on IP addresses that are frequently named as source or destination of an ARP address try <strong>Edit -&gt; Preferences -&gt; Columns</strong> to add two <strong>custom columns</strong> with the fields <strong>arp.src.proto_ipv4</strong> and <strong>arp.dst.proto_ipv4</strong> Next apply the display filter <strong>arp</strong> and export the packet list to a CSV file. A pivot table in Excel works real wonders</li></ol><p>Note that the filter in section 1 will show gratuitous ARPs issued by newer Windows systems. A sender IP address of 0.0.0.0 can safely be ignored (and specified in the filter).</p><p>Display filters could be shorter and more compact. The spelling here is chosen to make it easy to read and understand.</p><p>When just looking at the broadcast packet don't forget to check a couple of extra things:</p><ul><li>IP broadcast messages, like ICMP echo request or NTP messages to a broadcast address</li><li>Weird NetBIOS host announcements or Browser messages on UDP ports 137 and 138; especially you don't want to see browser elections</li><li>Stable spanning tree (Filter <strong>stp.flags.tc == 1</strong> sould not deliver any packet)</li></ul><p>Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '11, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-7280" class="comments-container"></div><div id="comment-tools-7280" class="comment-tools"></div><div class="clear"></div><div id="comment-7280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

