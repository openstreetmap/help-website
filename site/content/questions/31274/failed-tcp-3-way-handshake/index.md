+++
type = "question"
title = "Failed TCP 3-way handshake"
description = '''Can anyone verify what this trace is showing? From what I can tell, packet SYN packet (186) is being rejected in packet 187 with a Reset/ACK.  Then 188-190 is a normal 3-way handshake. What I don&#x27;t understand is why 187 is a RESET. Is it do to the fact that the reported window size in 187 is 0? I do...'''
date = "2014-03-28T19:31:00Z"
lastmod = "2014-03-28T21:37:00Z"
weight = 31274
keywords = [ "3-way", "tcp" ]
aliases = [ "/questions/31274" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Failed TCP 3-way handshake](/questions/31274/failed-tcp-3-way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31274-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone verify what this trace is showing? From what I can tell, packet SYN packet (186) is being rejected in packet 187 with a Reset/ACK.<br />
</p><p>Then 188-190 is a normal 3-way handshake. What I don't understand is why 187 is a RESET. Is it do to the fact that the reported window size in 187 is 0? I don't even see the MSS value being returned/echoed/agreed on in 187.</p><p>Normally this wouldn't' be of much concern to me as the handshake does eventually succeed, but in this case we are seeing this behavior a lot between these 2 hosts.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/SYN_2.bmp" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">3-way tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '14, 19:31</strong></p><img src="https://secure.gravatar.com/avatar/9501a0a9cba9c6ae399345ab0baf8b3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsuida&#39;s gravatar image" /><p>dsuida<br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsuida has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-31274" class="comments-container"></div><div id="comment-tools-31274" class="comment-tools"></div><div class="clear"></div><div id="comment-31274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31277"></span>

<div id="answer-container-31277" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31277-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The reason for the first SYN being rejected is because <strong>172.3.5.114</strong> is <strong>not a server LISTENing</strong> port <strong>58000</strong> when the SYN arrives from 172.30.5.148.</p><p>In the second 3-way-HS the roles have changed. <strong>172.4.5.114 is now the client</strong> connecting to the <strong>server at 172.30.5.148:58001</strong> .</p><p>Looking at the target port numbers it seems as those incrementing ports are dynamically allocated and negotiated between the two socket applications. If this is the case it might well be a timing issue where one side is just not fast enough to have a listening socket open when the other side's SYN packet arrives. Your screenshot doesn't show any timing information.</p><p>If you need further explanation could you possibly put the trace to <a href="http://cloudshark.org"></a><a href="http://cloudshark.org">http://cloudshark.org</a> so we can see streams 0-5 and the timing between the packets?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '14, 21:37</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-31277" class="comments-container"><span id="31279"></span><div id="comment-31279" class="comment"><div id="post-31279-score" class="comment-score"></div><div class="comment-text"><p>Ah.<br />
</p><p>So the sequence of: Client &gt; SYN Server &gt; RESET/ACK Client &gt; re-transmit Server &gt; RESET/ACK ...</p><p>Indicates the server is not listening on the requested port. Tx for the info.</p></div><div id="comment-31279-info" class="comment-info"><span class="comment-age">(29 Mar '14, 04:01)</span> dsuida</div></div><span id="31283"></span><div id="comment-31283" class="comment"><div id="post-31283-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-31283-info" class="comment-info"><span class="comment-age">(29 Mar '14, 11:04)</span> mrEEde2</div></div></div><div id="comment-tools-31277" class="comment-tools"></div><div class="clear"></div><div id="comment-31277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

