+++
type = "question"
title = "transfer rate timing of incomming packets"
description = '''hi all I am working with a module which claims to send packets every 100 micro seconds . but when I examine the incoming packets in wireshark i see that the intervals between incoming packets are about 400 usec. I am not sure the problem is due to whether the module or the wireshark program estimati...'''
date = "2010-12-12T01:17:00Z"
lastmod = "2010-12-12T07:52:00Z"
weight = 1319
keywords = [ "transfer.rate", "connection.speed" ]
aliases = [ "/questions/1319" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [transfer rate timing of incomming packets](/questions/1319/transfer-rate-timing-of-incomming-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1319-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all</p><p>I am working with a module which claims to send packets every 100 micro seconds . but when I examine the incoming packets in wireshark i see that the intervals between incoming packets are about 400 usec. I am not sure the problem is due to whether the module or the wireshark program estimation function</p><p>how can i find it out ? is there any other approach to find the transfer rate of my module ?</p><p>thanks alot</p></div><div id="question-tags" class="tags-container tags">transfer.rate connection.speed</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '10, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/8cb7490271657504847dc66a54fd75bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="makarbasi&#39;s gravatar image" /><p>makarbasi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="makarbasi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Dec '10, 01:19</p></div></div><div id="comments-container-1319" class="comments-container"></div><div id="comment-tools-1319" class="comment-tools"></div><div class="clear"></div><div id="comment-1319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1322"></span>

<div id="answer-container-1322" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1322-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is there a way that you can determine if there are any packets missing in a layer above IP? If so, you can capture over time and do the math to determine time/packets = interval. This would get you something to check by.<br />
</p><p>Also, worth mentioning is the pcap-ng format to get nanosecond level precision. I guess that doesn't fully rule out all of your concerns (I guess hw latency could still be a factor), but maybe worth a try.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '10, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span> </br></p></div></div><div id="comments-container-1322" class="comments-container"></div><div id="comment-tools-1322" class="comment-tools"></div><div class="clear"></div><div id="comment-1322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

