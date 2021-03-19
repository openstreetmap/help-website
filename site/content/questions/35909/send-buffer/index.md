+++
type = "question"
title = "Send buffer"
description = '''Hi,if send buffer is 64k, is there any chance that tcp/ip stack can send more than that lets say 128k before waiting for an ack.Receive window is always greater than 128k.'''
date = "2014-09-01T05:56:00Z"
lastmod = "2014-09-02T20:54:00Z"
weight = 35909
keywords = [ "tcp" ]
aliases = [ "/questions/35909" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Send buffer](/questions/35909/send-buffer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35909-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,if send buffer is 64k, is there any chance that tcp/ip stack can send more than that lets say 128k before waiting for an ack.Receive window is always greater than 128k.</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '14, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p>kishan pandey<br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-35909" class="comments-container"></div><div id="comment-tools-35909" class="comment-tools"></div><div class="clear"></div><div id="comment-35909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35944"></span>

<div id="answer-container-35944" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35944-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've seen Windows 7 do this, yes. iperf will report the send buffer as 64k, but it will put 128k on the wire before waiting for an ACK from the receiver. I don't have a great answer as to why, but one thought from someone was due to a direct copy memory mechanism. Details from Chris in the comments here: <a href="http://packetbomb.com/how-to-troubleshoot-throughput-and-tcp-windows/">http://packetbomb.com/how-to-troubleshoot-throughput-and-tcp-windows/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '14, 20:54</strong></p><img src="https://secure.gravatar.com/avatar/31a520375abb3ce54cec49f68af6a11c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karyrogers&#39;s gravatar image" /><p>karyrogers<br />
<span class="score" title="66 reputation points">66</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karyrogers has one accepted answer">100%</span></p></div></div><div id="comments-container-35944" class="comments-container"><span id="35959"></span><div id="comment-35959" class="comment"><div id="post-35959-score" class="comment-score"></div><div class="comment-text"><p>Thanks rogers</p></div><div id="comment-35959-info" class="comment-info"><span class="comment-age">(03 Sep '14, 05:17)</span> kishan pandey</div></div></div><div id="comment-tools-35944" class="comment-tools"></div><div class="clear"></div><div id="comment-35944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

