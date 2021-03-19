+++
type = "question"
title = "Continuation or non-HTTP traffic"
description = '''I got a trace where appear several times the info &quot;[TCP Fast Retransmission] Continuation or non-HTTP traffic&quot;, &quot;[TCP Previous segment lost]Continuation or non-HTTP traffic&quot; or [TCP Retransmission]Continuation or non-HTTP traffic&quot;.  This traces is from a user is downloading software or videos that s...'''
date = "2012-01-10T11:36:00Z"
lastmod = "2012-01-10T12:43:00Z"
weight = 8305
keywords = [ "traffic", "http", "trace" ]
aliases = [ "/questions/8305" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Continuation or non-HTTP traffic](/questions/8305/continuation-or-non-http-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8305-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I got a trace where appear several times the info "[TCP Fast Retransmission] Continuation or non-HTTP traffic", "[TCP Previous segment lost]Continuation or non-HTTP traffic" or [TCP Retransmission]Continuation or non-HTTP traffic".</p><p>This traces is from a user is downloading software or videos that sometimes takes 20 or 1 hour but the download is not completed. This download is from a sft server.</p><p>Please could you tell me what is this length refer?</p><p>What is the “Continuation or non-HTTP traffic”?</p><p>Do you think it is related with the downloading issue?</p><p>Thanks in advance for your help.</p></div><div id="question-tags" class="tags-container tags">traffic http trace</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '12, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/6a759cb6f0ef0f98e052f2ff859b039d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="acoria&#39;s gravatar image" /><p>acoria<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="acoria has no accepted answers">0%</span></p></div></div><div id="comments-container-8305" class="comments-container"></div><div id="comment-tools-8305" class="comment-tools"></div><div class="clear"></div><div id="comment-8305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8308"></span>

<div id="answer-container-8308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8308-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"Continuation or non-HTTP traffic" is a pretty common thing to see in traces with HTTP, usually in packets following the first with the HTTP return code. It simply tells you that this is a packet that holds further content of the page because it didn't fit into a single packet.</p><p>So unfortunately what you found is not a hint to a problem, it's just a note that this is part of a larger payload.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '12, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-8308" class="comments-container"><span id="17769"></span><div id="comment-17769" class="comment"><div id="post-17769-score" class="comment-score"></div><div class="comment-text"><p>I would like to know the way Wireshark decodes the packets to find "Continuation or non-HTTP traffic" ?</p></div><div id="comment-17769-info" class="comment-info"><span class="comment-age">(18 Jan '13, 02:02)</span> NewportMicro</div></div><span id="17770"></span><div id="comment-17770" class="comment"><div id="post-17770-score" class="comment-score"></div><div class="comment-text"><p>There is no good way to say this, but if you want to know how and why Wireshark does certain things you should get yourself a copy of the source code and track it down.</p></div><div id="comment-17770-info" class="comment-info"><span class="comment-age">(18 Jan '13, 02:10)</span> Jasper ♦♦</div></div><span id="17771"></span><div id="comment-17771" class="comment"><div id="post-17771-score" class="comment-score"></div><div class="comment-text"><p>The HTTP header "Content-Length" informs the HTTP dissector of how much data is expected and it keeps asking the TCP dissector for more until it receives the required amount.</p></div><div id="comment-17771-info" class="comment-info"><span class="comment-age">(18 Jan '13, 02:23)</span> grahamb ♦</div></div></div><div id="comment-tools-8308" class="comment-tools"></div><div class="clear"></div><div id="comment-8308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

