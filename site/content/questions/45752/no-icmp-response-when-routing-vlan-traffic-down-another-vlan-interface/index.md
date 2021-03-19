+++
type = "question"
title = "[closed] No ICMP response when routing vlan traffic down another vlan interface"
description = '''Hi, I have a 2 x linux box&#x27;s with an 600 and 601 tagged VLAN interface connected to a tagged/trunk interface on a 10Gb/s switch allowing both VLAN&#x27;s. When I route 600 traffic down 601 interface on both linux machines i can ping the 600 VLAN ip and it is being routed down the correct 601 interface. (...'''
date = "2015-09-10T03:25:00Z"
lastmod = "2015-09-10T03:25:00Z"
weight = 45752
keywords = [ "network", "vlan", "routing", "windows2008", "wireshark" ]
aliases = [ "/questions/45752" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] No ICMP response when routing vlan traffic down another vlan interface](/questions/45752/no-icmp-response-when-routing-vlan-traffic-down-another-vlan-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45752-score" class="post-score" title="current number of votes">0</div><span id="post-45752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a 2 x linux box's with an 600 and 601 tagged VLAN interface connected to a tagged/trunk interface on a 10Gb/s switch allowing both VLAN's. When I route 600 traffic down 601 interface on both linux machines i can ping the 600 VLAN ip and it is being routed down the correct 601 interface. (TICK)</p><p>The moment I introduce a windows 2008 R2 Server machine and setup the same config, i can ping the Linux box from Windows but the Linux box does not get a reply back from the Server. Wirshark running on the correct interface 601 shows it's receiving the packets down the correct interface from the Linux box but Wireshark reads ping request and the ICMP header reads "No response seen to ICMP request"</p><p>Arp entries are clean and routes have been added both ends. I have also added arp entries into both tables manually but still no joy</p><p>Any ideas would be much appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-windows2008" rel="tag" title="see questions tagged &#39;windows2008&#39;">windows2008</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '15, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/3d1652302663d2cb0c688b5089c21eef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jamie_no1&#39;s gravatar image" /><p><span>jamie_no1</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jamie_no1 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>10 Sep '15, 04:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-45752" class="comments-container"></div><div id="comment-tools-45752" class="comment-tools"></div><div class="clear"></div><div id="comment-45752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Jaap 10 Sep '15, 04:42

</div>

</div>

</div>

