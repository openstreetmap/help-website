+++
type = "question"
title = "Count packets/bytes without capturing them?"
description = '''Hi, all. I hope this isn&#x27;t repeating a question that&#x27;s been asked; I did a search and couldn&#x27;t find it: I need to count throughput on my network without actually capturing packets -- it&#x27;s a lot to store, and all I want is to add up the count of packets and bytes, by source and destination. Can Wires...'''
date = "2012-09-12T11:46:00Z"
lastmod = "2012-09-12T12:11:00Z"
weight = 14215
keywords = [ "nocapture", "packets", "packetcount" ]
aliases = [ "/questions/14215" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Count packets/bytes without capturing them?](/questions/14215/count-packetsbytes-without-capturing-them)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14215-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, all. I hope this isn't repeating a question that's been asked; I did a search and couldn't find it:</p><p>I need to count throughput on my network without actually capturing packets -- it's a lot to store, and all I want is to add up the count of packets and bytes, by source and destination.</p><p>Can Wireshark do this without a hack or complicated workaround? If not, any recommendation on a solution is appreciated. Thanks!</p></div><div id="question-tags" class="tags-container tags">nocapture packets packetcount</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '12, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/019266f09f3033ff6ac69ad7e2818285?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SFMiner&#39;s gravatar image" /><p>SFMiner<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SFMiner has no accepted answers">0%</span></p></div></div><div id="comments-container-14215" class="comments-container"></div><div id="comment-tools-14215" class="comment-tools"></div><div class="clear"></div><div id="comment-14215-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14216"></span>

<div id="answer-container-14216" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14216-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is probably not the tool you'd use for this, since it in fact looks at captured packets, so you need to record them first. The type of thing you want to do is closer to using a Netflow analyzer/collector, so you should probably take a look into Netflow/Openflow.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '12, 12:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14216" class="comments-container"></div><div id="comment-tools-14216" class="comment-tools"></div><div class="clear"></div><div id="comment-14216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

