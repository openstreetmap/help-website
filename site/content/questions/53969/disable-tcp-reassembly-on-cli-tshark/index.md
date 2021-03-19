+++
type = "question"
title = "Disable TCP reassembly on CLI tshark"
description = '''I would like to get the http.time as the time between the first packet of the request and the first packet of the response. On this question they say it is possible to be done with wireshark by disabling TCP reassembly , but, how can I do it with CLI tshark, there is no information about this on the...'''
date = "2016-07-10T14:51:00Z"
lastmod = "2016-07-10T15:05:00Z"
weight = 53969
keywords = [ "http", "tshark", "tcp", "cli" ]
aliases = [ "/questions/53969" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Disable TCP reassembly on CLI tshark](/questions/53969/disable-tcp-reassembly-on-cli-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53969-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to get the http.time as the time between the first packet of the request and the first packet of the response. On <a href="https://ask.wireshark.org/questions/46537/time-since-request-httptime">this question</a> they say it is possible to be done with wireshark by disabling TCP reassembly , but, how can I do it with CLI tshark, there is no information about this on the manpage.</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">http tshark tcp cli</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '16, 14:51</strong></p><img src="https://secure.gravatar.com/avatar/37229766800b2dfee440c3c891d944b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlosvega&#39;s gravatar image" /><p>carlosvega<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlosvega has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '16, 15:05</p></div></div><div id="comments-container-53969" class="comments-container"></div><div id="comment-tools-53969" class="comment-tools"></div><div class="clear"></div><div id="comment-53969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53971"></span>

<div id="answer-container-53971" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53971-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I just found it</p><pre><code>-o tcp.desegment_tcp_streams:false</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '16, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/37229766800b2dfee440c3c891d944b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlosvega&#39;s gravatar image" /><p>carlosvega<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlosvega has one accepted answer">100%</span></p></div></div><div id="comments-container-53971" class="comments-container"></div><div id="comment-tools-53971" class="comment-tools"></div><div class="clear"></div><div id="comment-53971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

