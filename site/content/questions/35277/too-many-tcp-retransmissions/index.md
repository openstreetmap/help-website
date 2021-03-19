+++
type = "question"
title = "Too many tcp retransmissions"
description = '''Hi All, We are seeing too many tcp retransmissions from the exchanges we have integrated with. Here is one of the issues we are seeing, and it causes timeouts. I am very new to this, so would like some insights about how to resolve such kind of issues. I can provide a bigger set of data if required....'''
date = "2014-08-06T13:24:00Z"
lastmod = "2014-08-11T06:16:00Z"
weight = 35277
keywords = [ "tcp", "retransmissions", "timeout" ]
aliases = [ "/questions/35277" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Too many tcp retransmissions](/questions/35277/too-many-tcp-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35277-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>We are seeing too many tcp retransmissions from the exchanges we have integrated with. Here is one of the issues we are seeing, and it causes timeouts. I am very new to this, so would like some insights about how to resolve such kind of issues. I can provide a bigger set of data if required.</p><p>Attached is the screenshot.</p><p>Thanks, Dhaval <img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_Trace_14.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">tcp retransmissions timeout</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '14, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/89499a8a12cd4c580acb2dd4482b5e72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dhavalkotecha&#39;s gravatar image" /><p>dhavalkotecha<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dhavalkotecha has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 06 Aug '14, 13:27</p></div></div><div id="comments-container-35277" class="comments-container"><span id="35380"></span><div id="comment-35380" class="comment"><div id="post-35380-score" class="comment-score"></div><div class="comment-text"><blockquote><p>We are seeing <strong>too many tcp retransmissions</strong></p></blockquote><p>there is only <strong>one</strong> retransmission in your example, which is perfectly normal for almost any network out there. So, based on the information you provided so far, it's impossible to answer your question.</p><p>Oh wait... <strong>What is your question</strong>?</p></div><div id="comment-35380-info" class="comment-info"><span class="comment-age">(10 Aug '14, 08:27)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-35277" class="comment-tools"></div><div class="clear"></div><div id="comment-35277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35404"></span>

<div id="answer-container-35404" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35404-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Based on the screenshot I think the problem is <strong>the "client" not adding the tcp timestamp option in packet #4</strong> as negotiated in the 3-way handshake.<br />
Therefore the server discards this 4 byte segment and indicates the gap in packet #6 after having received a 1677 bytes out-of-order segment.<br />
200 ms later the client terminates the connection by sending a FIN packet which generates the first dup-ack for seq 1.<br />
Another <strong>1.000 ms</strong> later the client's retransmission timer expires and seq# 1 is finally retransmitted (bypassing segmentation offload this time).<br />
</p><p>What can be done?<br />
</p><ul><li>Fix the client (=Exchange?) to always add a tcp timestamp option to every segment once negotiated in the 3-way handshake</li><li>Disable the TCP Timestamp option in your Windows Server using <code>netsh int tcp set global timestamps=disabled</code></li></ul><p>It would help to add a capture file to cloudshark.org instead of just adding screenshots for detailed analysis of this kind of problems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '14, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-35404" class="comments-container"><span id="35426"></span><div id="comment-35426" class="comment"><div id="post-35426-score" class="comment-score"></div><div class="comment-text"><p>Hi mrEEde,i have a query as per my understanding a host that receives a TCP segment with a TCP timestamp must compare the current timestamp in the segment with what it considers the previous timestamp. If the timestamp is equal or greater than the previous one, it is acceptable. Otherwise, the segment should not be acknowledged. But as you said packet without timestamp so server is discarding it,so is this a normal behaviour to drop packet if it doesnt have timestamp.I tried to google it but no concrete answer found.</p></div><div id="comment-35426-info" class="comment-info"><span class="comment-age">(11 Aug '14, 23:22)</span> kishan pandey</div></div><span id="35430"></span><div id="comment-35430" class="comment"><div id="post-35430-score" class="comment-score"></div><div class="comment-text"><p>I'm not good at reading RFCs but I think RFC1323 says we always have to send a TSVal and echo what we've received...</p><p>3.2 TCP Timestamps Option</p><pre><code>  TCP is a symmetric protocol, allowing data to be sent at any time
  in either direction, and therefore timestamp echoing may occur in
  either direction.  For simplicity and symmetry, we specify that
  timestamps always be sent and echoed in both directions.  For
  efficiency, we combine the timestamp and timestamp reply fields
  into a single TCP Timestamps Option.</code></pre></div><div id="comment-35430-info" class="comment-info"><span class="comment-age">(12 Aug '14, 03:39)</span> mrEEde</div></div><span id="35431"></span><div id="comment-35431" class="comment"><div id="post-35431-score" class="comment-score"></div><div class="comment-text"><p>ok,thanks mrEEde</p></div><div id="comment-35431-info" class="comment-info"><span class="comment-age">(12 Aug '14, 04:55)</span> kishan pandey</div></div></div><div id="comment-tools-35404" class="comment-tools"></div><div class="clear"></div><div id="comment-35404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

