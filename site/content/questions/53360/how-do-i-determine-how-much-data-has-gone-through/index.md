+++
type = "question"
title = "how do I determine how much data has gone through"
description = '''Hi All I am trying to determine how much packets or data has gone through between my server and my local machine? ISSUE: I am trying to download a file. a 10000 row CSV file downloads in less than 40 secs a 20000 row CSV file===== same time a 50000 row CSV file====== hangs and times out after 9 mins...'''
date = "2016-06-11T23:33:00Z"
lastmod = "2016-06-12T00:17:00Z"
weight = 53360
keywords = [ "packets" ]
aliases = [ "/questions/53360" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how do I determine how much data has gone through](/questions/53360/how-do-i-determine-how-much-data-has-gone-through)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53360-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All I am trying to determine how much packets or data has gone through between my server and my local machine?</p><p>ISSUE:<br />
I am trying to download a file.<br />
a 10000 row CSV file downloads in less than 40 secs<br />
a 20000 row CSV file===== same time<br />
a 50000 row CSV file====== hangs and times out after 9 mins.<br />
</p><p>I am trying to see if its my throughput pipe so i can get back to Network engineers and tell them to open it up.</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '16, 23:33</strong></p><img src="https://secure.gravatar.com/avatar/67b2195d90c158d5b04174b3c47b6abb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oradba888&#39;s gravatar image" /><p>oradba888<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oradba888 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jun '16, 23:59</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></br></p></div></div><div id="comments-container-53360" class="comments-container"></div><div id="comment-tools-53360" class="comment-tools"></div><div class="clear"></div><div id="comment-53360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53362"></span>

<div id="answer-container-53362" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53362-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Capture the whole conversation using Wireshark (means: start capturing before initiating the download and stop capturing after the transfer successfully finished or times out), and then</p><ul><li><p>choose <code>Statistics -&gt; Conversations</code> to open a list of conversations, select the tab <code>TCP</code> to see the TCP ones, and find the one you are interested in by IP addresses and ports to see the number of packets and the number of bytes which have been transferred (which is what your question was about)</p></li><li><p>find the conversation (applying a display filter <code>ip.addr == your.client.ip and ip.addr == your.server.ip</code> could be sufficient; if not, add <code>and tcp.port == your.server.port and tcp.port == your.client.port</code> to the display filter and press <code>--&gt;</code> (apply) again) and then look for lost packets, retransmissions etc. to find out what is wrong (which is what you seem to actually need).</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '16, 00:17</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div></div><div id="comments-container-53362" class="comments-container"></div><div id="comment-tools-53362" class="comment-tools"></div><div class="clear"></div><div id="comment-53362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

