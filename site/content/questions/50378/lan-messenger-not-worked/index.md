+++
type = "question"
title = "Lan Messenger not worked :("
description = '''Hello. I need your help. I install Lan Messenger on my Local network computers but some users can see each other but someone can&#x27;t :(. I capture the traffic via Wireshark and need your idea to solve it. Capture file is : http://s000.tinyupload.com/?file_id=75995745116620576811 Thank you.'''
date = "2016-02-21T01:27:00Z"
lastmod = "2016-02-21T01:27:00Z"
weight = 50378
keywords = [ "lan", "messenger" ]
aliases = [ "/questions/50378" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lan Messenger not worked :(](/questions/50378/lan-messenger-not-worked)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50378-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I need your help. I install Lan Messenger on my Local network computers but some users can see each other but someone can't :(. I capture the traffic via Wireshark and need your idea to solve it. Capture file is : <a href="http://s000.tinyupload.com/?file_id=75995745116620576811">http://s000.tinyupload.com/?file_id=75995745116620576811</a></p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">lan messenger</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '16, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/1f1d393403ea997213960ee852d8f897?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hack3rcon&#39;s gravatar image" /><p>hack3rcon<br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hack3rcon has no accepted answers">0%</span></p></div></div><div id="comments-container-50378" class="comments-container"><span id="50380"></span><div id="comment-50380" class="comment"><div id="post-50380-score" class="comment-score"></div><div class="comment-text"><p>All the Lan Messenger's packets in the capture seem to be always sent to two destinations:</p><ul><li><p>the broadcast IP address of sender's own IP subnet with broadcast MAC address,</p></li><li><p>the multicast IP address with IPv4 multicast MAC address, while the sender also sends IGMPv3 membership reports for that multicast IP address.</p></li></ul><p>So my fast shot would be that</p><ul><li><p>not all computers on your LAN are in the same IP subnet,</p></li><li><p>multicast support is not available (or, more likely, only not enabled) on your switches and routers</p></li></ul><p>So only PCs sharing a subnet can see each other's Lan Messenger messages, because packets sent to broadcast destination MAC address and subnet broadcast IP address can only reach PCs within the same subnet, and multicast packets don't get anywhere as already the switch drops them.</p><p>A simultaneous capture at two machines which cannot "see each other" should confirm or deny this assumption.</p></div><div id="comment-50380-info" class="comment-info"><span class="comment-age">(21 Feb '16, 01:50)</span> sindy</div></div><span id="50381"></span><div id="comment-50381" class="comment"><div id="post-50381-score" class="comment-score"></div><div class="comment-text"><p>My network use Vlan but some computers can see each other.</p></div><div id="comment-50381-info" class="comment-info"><span class="comment-age">(21 Feb '16, 02:21)</span> hack3rcon</div></div><span id="50382"></span><div id="comment-50382" class="comment"><div id="post-50382-score" class="comment-score"></div><div class="comment-text"><p>First, please take the two simultaneous captures as I've suggested above, and post them here. If my assumption gets confirmed, it makes sense for you to:</p><ul><li><p>find and understand what is a VLAN, what is an IP subnet, and what is the difference between the two. The fact that in most LANs the mapping between VLANs and IP subnets is 1:1 (exactly one VLAN is used for exactly one IP subnet) does not mean that these two things are the same.</p></li><li><p>find what an "IP-subnet-wide" broadcast (or just IP broadcast) means, and what IP multicast means.</p></li></ul><p>"Some computers can see each other" doesn't tell us anything. Any two computers in your LAN may "see each other" at L2 (switching) level or at L3 (routing) level. And even if one of these two possibilities is true for unicast and broadcast traffic, it may not be true for multicast traffic, because handling of multicast traffic is different from handling of unicast or broadcast traffic on both L2 and L3.</p></div><div id="comment-50382-info" class="comment-info"><span class="comment-age">(21 Feb '16, 02:40)</span> sindy</div></div></div><div id="comment-tools-50378" class="comment-tools"></div><div class="clear"></div><div id="comment-50378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

