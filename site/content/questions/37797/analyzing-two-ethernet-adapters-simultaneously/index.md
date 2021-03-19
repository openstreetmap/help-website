+++
type = "question"
title = "Analyzing two ethernet adapters simultaneously"
description = '''I am analyzing traffic on a server that has two ethernet adapters and each adapter is attached to a different network. When I analyze one adapter or the other I do not receive a lot of bad TCP packets. When I analyze both adapters at the same time, I receive many bad TCP packets. Is there a reason w...'''
date = "2014-11-12T12:05:00Z"
lastmod = "2014-11-13T13:03:00Z"
weight = 37797
keywords = [ "ethernet", "two-adapters", "tcp", "server" ]
aliases = [ "/questions/37797" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Analyzing two ethernet adapters simultaneously](/questions/37797/analyzing-two-ethernet-adapters-simultaneously)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37797-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am analyzing traffic on a server that has two ethernet adapters and each adapter is attached to a different network. When I analyze one adapter or the other I do not receive a lot of bad TCP packets. When I analyze both adapters at the same time, I receive many bad TCP packets. Is there a reason why that happens?</p></div><div id="question-tags" class="tags-container tags">ethernet two-adapters tcp server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '14, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/7ca141a10677638ff04e11bddedf4789?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drvenom14&#39;s gravatar image" /><p>drvenom14<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drvenom14 has no accepted answers">0%</span></p></div></div><div id="comments-container-37797" class="comments-container"></div><div id="comment-tools-37797" class="comment-tools"></div><div class="clear"></div><div id="comment-37797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37836"></span>

<div id="answer-container-37836" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37836-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>When I analyze both adapters at the same time, I receive many bad TCP packets. Is there a reason why that happens?</p></blockquote><p>That's probably because you write packets for the same TCP sessions, captured on both adapters (maybe adapter teaming), into the same capture file. As the order of the frames will be different from what Wireshark believes to be a correct TCP stream (seeing SEQ numbers before others, etc.), it might flags those frames.</p><p><strong>However</strong> that's just speculation. As you did not provide the capture I can only guess. So, please upload the capture file somewhere (google drive, dropbox, cloudshark.org) and post the link here. Please also add some details why the server has two interfaces (adapter teaming yes/no), if both adapters have an IP address of the same subnet (a lot of windows admins are doing this for good or bad reasons), etc., etc.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '14, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37836" class="comments-container"></div><div id="comment-tools-37836" class="comment-tools"></div><div class="clear"></div><div id="comment-37836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

