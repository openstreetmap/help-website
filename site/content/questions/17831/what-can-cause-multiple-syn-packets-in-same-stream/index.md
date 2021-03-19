+++
type = "question"
title = "What can cause multiple SYN Packets in same stream"
description = '''I have a laptop that is connected to a micro web server device via an old hub (Netgear EN104). The IP Assignments are: Micro web server: 10.10.6.106 Laptop: 10.10.6.222  I am noticing that, on occasion, the laptop will send two SYN packets in the same stream and the server will only ACK one of them....'''
date = "2013-01-21T15:38:00Z"
lastmod = "2013-01-21T15:44:00Z"
weight = 17831
keywords = [ "syn", "stream" ]
aliases = [ "/questions/17831" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What can cause multiple SYN Packets in same stream](/questions/17831/what-can-cause-multiple-syn-packets-in-same-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17831-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have a laptop that is connected to a micro web server device via an old hub (Netgear EN104).</p><p>The IP Assignments are:</p><pre><code>Micro web server: 10.10.6.106
Laptop: 10.10.6.222</code></pre><p>I am noticing that, on occasion, the laptop will send two SYN packets in the same stream and the server will only ACK one of them. The multiple SYN packets remind me of a type of DoS tactic, but in this case I know for sure that nothing malicious is causing the multiple SYN requests.</p><p>Here is an <a href="http://cloudshark.org/captures/feaad26b1a89">example of a stream</a> that contains two SYN packets.</p><p>I should note that most of the streams do NOT have two SYN packets, but rather contain one (which is what I would expect for all streams).</p><p>What could cause the browser client to send two SYN packets within the same stream and is there anything that I can do to avoid this from occurring?</p></div><div id="question-tags" class="tags-container tags">syn stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '13, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/1259897b9b42059302967b55c0dc2228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KTM&#39;s gravatar image" /><p>KTM<br />
<span class="score" title="76 reputation points">76</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KTM has one accepted answer">100%</span></p></div></div><div id="comments-container-17831" class="comments-container"></div><div id="comment-tools-17831" class="comment-tools"></div><div class="clear"></div><div id="comment-17831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17832"></span>

<div id="answer-container-17832" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17832-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll see multiple SYN packets at the beginning of a conversation if the first SYN does not get answered with a SYN/ACK, or that answer arrives late (in which case the "impatient" client will fire away another SYN). A typical sign of an unanswered SYN is when you can spot a delay of about 3 seconds between the SYN packets - just like in your trace.</p><p>It usually means that either the first SYN packets got lost, or the server wasn't able to answer sooner. I guess it is more of a performance problem on the server, because it replies with a SYN/ACK containing a window size of zero, which I haven't seen before as far as I remember. Also, in the next packet from the server, it again says "zero window", so this device is in some kind of trouble.</p><p>I'd say the web server is congested pretty much.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '13, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jan '13, 15:47</p></div></div><div id="comments-container-17832" class="comments-container"></div><div id="comment-tools-17832" class="comment-tools"></div><div class="clear"></div><div id="comment-17832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

