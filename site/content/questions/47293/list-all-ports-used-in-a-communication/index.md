+++
type = "question"
title = "List all ports used in a communication"
description = '''Hi, Is there any way to list all the ports used during a communication? For example I have an UDP communication between IP-A and IP-B, how can I know which ports they use without looking all the packets? Thank you'''
date = "2015-11-05T08:43:00Z"
lastmod = "2015-11-05T08:52:00Z"
weight = 47293
keywords = [ "udp", "ports" ]
aliases = [ "/questions/47293" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [List all ports used in a communication](/questions/47293/list-all-ports-used-in-a-communication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47293-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Is there any way to list all the ports used during a communication? For example I have an UDP communication between IP-A and IP-B, how can I know which ports they use without looking all the packets? Thank you</p></div><div id="question-tags" class="tags-container tags">udp ports</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '15, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/065a787c1564a0f77c10c927f7f080b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rok&#39;s gravatar image" /><p>rok<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rok has no accepted answers">0%</span></p></div></div><div id="comments-container-47293" class="comments-container"></div><div id="comment-tools-47293" class="comment-tools"></div><div class="clear"></div><div id="comment-47293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47297"></span>

<div id="answer-container-47297" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47297-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Filter the capture to only traffic between hosts A and B, then use Statistics -&gt; Endpoints, and then select the UDP tab.</p><p>You can also add the filter straight from that dialog by right clicking an entry and then selecting "Apply As a Filter ..." but that also adds the port to the filter which isn't what you want.</p><p>You need a two host filter such as <code>(ip.src == a and ip.dst == b) or (ip.src == b and ip.dst == a)</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '15, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-47297" class="comments-container"><span id="47301"></span><div id="comment-47301" class="comment"><div id="post-47301-score" class="comment-score"></div><div class="comment-text"><p>Your first method is exactly what I want! Don't forget to select "limit to display filter". ;)</p></div><div id="comment-47301-info" class="comment-info"><span class="comment-age">(05 Nov '15, 09:22)</span> rok</div></div></div><div id="comment-tools-47297" class="comment-tools"></div><div class="clear"></div><div id="comment-47297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

