+++
type = "question"
title = "PC don&#x27;t response after [SYN, ACK] is received"
description = '''Hi, I am trying to port a web server from 8051 to ARM but found some problem after PC received an [SYN, ACK] packet (use web browser to test my server). PC -&amp;gt; [SYN] My server-&amp;gt; [SYN, ACK] PC -&amp;gt; Can&#x27;t see my sever response and just re-transmit the [SYN] again. I look into the wireshark trace...'''
date = "2013-11-19T03:26:00Z"
lastmod = "2013-11-19T07:50:00Z"
weight = 27094
keywords = [ "ack", "syn" ]
aliases = [ "/questions/27094" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [PC don't response after \[SYN, ACK\] is received](/questions/27094/pc-dont-response-after-syn-ack-is-received)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27094-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to port a web server from 8051 to ARM but found some problem after PC received an [SYN, ACK] packet (use web browser to test my server).</p><p>PC -&gt; [SYN] My server-&gt; [SYN, ACK] PC -&gt; Can't see my sever response and just re-transmit the [SYN] again.</p><p>I look into the wireshark trace of both working (8051 server) and not working (ARM server) scenario. The reply packet from server is almost the same (except checksum, sequence number and identifier).</p><p>Can anyone give me a pointer?</p><p>Here is my trace. Both 8051 and ARM hardware addreess is the same. <a href="https://www.dropbox.com/sh/inu4urbdrgkb58x/VpXzdlSVZu">https://www.dropbox.com/sh/inu4urbdrgkb58x/VpXzdlSVZu</a></p><p>Thanks in advance. Imai</p></div><div id="question-tags" class="tags-container tags">ack syn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '13, 03:26</strong></p><img src="https://secure.gravatar.com/avatar/cf1d366a386fa3f8988d4d08f9daf784?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="imai&#39;s gravatar image" /><p>imai<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="imai has no accepted answers">0%</span></p></div></div><div id="comments-container-27094" class="comments-container"></div><div id="comment-tools-27094" class="comment-tools"></div><div class="clear"></div><div id="comment-27094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27104"></span>

<div id="answer-container-27104" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27104-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The TCP checksumm in the failing case is incorrect, so your client is validly discarding the SYN_ACK from the server. <img src="https://osqa-ask.wireshark.org/upfiles/tcp_checksum_1.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '13, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-27104" class="comments-container"><span id="27197"></span><div id="comment-27197" class="comment"><div id="post-27197-score" class="comment-score"></div><div class="comment-text"><p>Hi mrEEde, thank you very much. I found that the TCP checksum is not validated by default in Wireshark and need to enable it explicitly in the preference. After I changed the TCP checksum, everything goes well.</p><p>Thanks again! You save my life :-)</p></div><div id="comment-27197-info" class="comment-info"><span class="comment-age">(20 Nov '13, 22:48)</span> imai</div></div></div><div id="comment-tools-27104" class="comment-tools"></div><div class="clear"></div><div id="comment-27104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

