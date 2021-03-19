+++
type = "question"
title = "Broadcast Traffic Capture"
description = '''Can I use WireShark to capture external broadcast traffic? For example I have a program that broadcasts on port 12060 to other programs on the same machine. I want to capture that traffic between programs. I tried udp.dstport==12060 but got no packets. How do I do this?'''
date = "2015-03-09T07:47:00Z"
lastmod = "2015-03-09T10:03:00Z"
weight = 40384
keywords = [ "broadcast", "udp" ]
aliases = [ "/questions/40384" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Broadcast Traffic Capture](/questions/40384/broadcast-traffic-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40384-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I use WireShark to capture external broadcast traffic? For example I have a program that broadcasts on port 12060 to other programs on the same machine. I want to capture that traffic between programs. I tried udp.dstport==12060 but got no packets. How do I do this?</p></div><div id="question-tags" class="tags-container tags">broadcast udp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '15, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/72cf420b0a30c5825c7ab1897923d96a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="W8LIG&#39;s gravatar image" /><p>W8LIG<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="W8LIG has no accepted answers">0%</span></p></div></div><div id="comments-container-40384" class="comments-container"></div><div id="comment-tools-40384" class="comment-tools"></div><div class="clear"></div><div id="comment-40384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40392"></span>

<div id="answer-container-40392" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40392-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it can. But are you capturing on the actual interface the broadcast traffic is on? Is your application binding to the loopback interface, sending broadcast traffic? Seems likely, since your target is other programs on the same machine. You can point Wireshark at the loopback interface, and depending on the OS you can see that traffic. On Windows: no; on UN*X based systems: yes. It's all in the <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">Wiki</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '15, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40392" class="comments-container"></div><div id="comment-tools-40392" class="comment-tools"></div><div class="clear"></div><div id="comment-40392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

