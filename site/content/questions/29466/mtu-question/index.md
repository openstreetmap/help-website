+++
type = "question"
title = "MTU question"
description = '''If a router&#x27;s WAN interface is configured for an MTU of 1500, I should not be able to send an non-fragmented packet over 1500 outside, but it gets through. where does it find room for another 14 bytes?  Thanks http://www.cloudshark.org/captures/a00ef83e9e99 ping 8.8.8.8 -l 1472 -f Pinging 8.8.8.8 wi...'''
date = "2014-02-05T09:58:00Z"
lastmod = "2014-02-05T10:47:00Z"
weight = 29466
keywords = [ "wan", "1500", "mtu" ]
aliases = [ "/questions/29466" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [MTU question](/questions/29466/mtu-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29466-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If a router's WAN interface is configured for an MTU of 1500, I should not be able to send an non-fragmented packet over 1500 outside, but it gets through.</p><p>where does it find room for another 14 bytes?</p><p>Thanks</p><p><a href="http://www.cloudshark.org/captures/a00ef83e9e99">http://www.cloudshark.org/captures/a00ef83e9e99</a></p><p>ping 8.8.8.8 -l 1472 -f</p><p>Pinging 8.8.8.8 with 1472 bytes of data:<br />
Reply from 8.8.8.8: bytes=64 (sent 1472) time=43ms TTL=46<br />
Reply from 8.8.8.8: bytes=64 (sent 1472) time=34ms TTL=46<br />
Reply from 8.8.8.8: bytes=64 (sent 1472) time=35ms TTL=46<br />
Reply from 8.8.8.8: bytes=64 (sent 1472) time=34ms TTL=46<br />
</p><p>Ping statistics for 8.8.8.8: Packets: Sent = 4, Received = 4, Lost = 0 (0% loss), Approximate round trip times in milli-seconds: Minimum = 34ms, Maximum = 43ms, Average = 36ms</p></div><div id="question-tags" class="tags-container tags">wan 1500 mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '14, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span> </br></br></p></div></div><div id="comments-container-29466" class="comments-container"></div><div id="comment-tools-29466" class="comment-tools"></div><div class="clear"></div><div id="comment-29466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29468"></span>

<div id="answer-container-29468" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29468-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>MTU size is the largest ip.len that is getting through. For ethernet you need to add 14 bytes header <img src="https://osqa-ask.wireshark.org/upfiles/Selection_036.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '14, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-29468" class="comments-container"></div><div id="comment-tools-29468" class="comment-tools"></div><div class="clear"></div><div id="comment-29468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

