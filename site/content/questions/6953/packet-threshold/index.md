+++
type = "question"
title = "Packet threshold"
description = '''Is there a way for Wireshark to give a notification when a certain number of packets/second (or other time interval) are transmitted from a given protocol? On a LAN recently, one computer was sending five thousand emails a second (not sure on the cause, obviously something malicious) and the staff d...'''
date = "2011-10-18T04:35:00Z"
lastmod = "2011-10-18T06:59:00Z"
weight = 6953
keywords = [ "threshold", "lan" ]
aliases = [ "/questions/6953" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet threshold](/questions/6953/packet-threshold)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6953-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way for Wireshark to give a notification when a certain number of packets/second (or other time interval) are transmitted from a given protocol? On a LAN recently, one computer was sending five thousand emails a second (not sure on the cause, obviously something malicious) and the staff did not realize it until the ISP handling the requests turned the service off.</p></div><div id="question-tags" class="tags-container tags">threshold lan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '11, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/158084d6388317e23ca0b785a244de17?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ben%20Thomas&#39;s gravatar image" /><p>Ben Thomas<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ben Thomas has no accepted answers">0%</span></p></div></div><div id="comments-container-6953" class="comments-container"></div><div id="comment-tools-6953" class="comment-tools"></div><div class="clear"></div><div id="comment-6953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6955"></span>

<div id="answer-container-6955" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6955-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately you can't, but that kind of thing is more or less a task for a network monitoring solution, not a packet capture solution like Wireshark. Take a look at Netflow collectors, and have the routers/switches send NetFlow statistics to one of them, which can then aggregate and monitor thresholds of IPs and Ports as well as Packets and Bytes transmitted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '11, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-6955" class="comments-container"><span id="6968"></span><div id="comment-6968" class="comment"><div id="post-6968-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info</p></div><div id="comment-6968-info" class="comment-info"><span class="comment-age">(18 Oct '11, 13:30)</span> Ben Thomas</div></div></div><div id="comment-tools-6955" class="comment-tools"></div><div class="clear"></div><div id="comment-6955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

