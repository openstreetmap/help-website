+++
type = "question"
title = "Easy  and  fast way to save  streams (UDP and TCP)???"
description = '''If I have a trace with say 6000000 or more streams (TCP ,UDP) , is there an easy and fast way to save out each 1000000 stream to its own separate file, whether it be using tshark, editcap, gui, etc.? Or is the only way to do this to use a display filter for each stream and save as one by one (you kn...'''
date = "2015-01-07T04:21:00Z"
lastmod = "2015-01-07T10:09:00Z"
weight = 38925
keywords = [ "seperate", "flows" ]
aliases = [ "/questions/38925" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Easy and fast way to save streams (UDP and TCP)???](/questions/38925/easy-and-fast-way-to-save-streams-udp-and-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38925-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I have a trace with say 6000000 or more streams (TCP ,UDP) , is there an easy and fast way to save out each 1000000 stream to its own separate file, whether it be using tshark, editcap, gui, etc.? Or is the only way to do this to use a display filter for each stream and save as one by one (you know that it is impossible)?</p><p>Thanks a lot</p></div><div id="question-tags" class="tags-container tags">seperate flows</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '15, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/deec7afda5035771868d6acfbc90d994?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mosa&#39;s gravatar image" /><p>mosa<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mosa has no accepted answers">0%</span></p></div></div><div id="comments-container-38925" class="comments-container"></div><div id="comment-tools-38925" class="comment-tools"></div><div class="clear"></div><div id="comment-38925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38929"></span>

<div id="answer-container-38929" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38929-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at tcpflow.</p><blockquote><p><a href="https://github.com/simsong/tcpflow">https://github.com/simsong/tcpflow</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '15, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38929" class="comments-container"><span id="38934"></span><div id="comment-38934" class="comment"><div id="post-38934-score" class="comment-score"></div><div class="comment-text"><p>thank for your attention kurt but I want have pcap file for each 1000000 stream. the output of tcpflow and tcptrace are not a pcap file</p></div><div id="comment-38934-info" class="comment-info"><span class="comment-age">(07 Jan '15, 22:18)</span> mosa</div></div></div><div id="comment-tools-38929" class="comment-tools"></div><div class="clear"></div><div id="comment-38929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

