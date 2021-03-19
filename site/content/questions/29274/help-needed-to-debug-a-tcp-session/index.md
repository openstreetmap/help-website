+++
type = "question"
title = "Help needed to debug a TCP session"
description = '''Hi I need some help to debug a simple TCP flow between a client and a server that I have recorded using Wireshark please. How should I post that flow here? Meanwhile, here is an attempt to show it:  -&amp;gt; SYN  &amp;lt;- SYN, ACK  -&amp;gt; ACK  -&amp;gt; PSH, ACK Seq=1 Ack=1  -&amp;gt; PSH, ACK Seq=13 Ack=1  -&amp;gt; ...'''
date = "2014-01-29T09:16:00Z"
lastmod = "2014-01-30T07:37:00Z"
weight = 29274
keywords = [ "tcp" ]
aliases = [ "/questions/29274" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Help needed to debug a TCP session](/questions/29274/help-needed-to-debug-a-tcp-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29274-score" class="post-score" title="current number of votes">0</div><span id="post-29274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I need some help to debug a simple TCP flow between a client and a server that I have recorded using Wireshark please. How should I post that flow here?</p><p>Meanwhile, here is an attempt to show it:</p><pre><code> -&gt;  SYN
 &lt;-  SYN, ACK
 -&gt;  ACK
 -&gt;  PSH, ACK Seq=1 Ack=1
 -&gt;  PSH, ACK Seq=13 Ack=1
 -&gt;  PSH, ACK Seq=1473 Ack=1
 &lt;-  ACK      Seq=1 Ack=13
 -&gt;  TCP Retransmission PSH, ACK Seq=13, Ack=1
 -&gt;  TCP Retransmission PSH, ACK Seq=13, Ack=1
 -&gt;  TCP Retransmission PSH, ACK Seq=13, Ack=1
 &lt;-  FIN, ACK Seq=1, Ack=13
 -&gt;  ACK Seq=549, Ack=2
&lt;snip&gt;</code></pre><p>I understand the '3-way handshake'. But what does the retransmission signify and why does it happen 3 times?</p><p>Best regards David</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '14, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/127322d117e02480a76c4efde0a67594?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidA&#39;s gravatar image" /><p><span>DavidA</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidA has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jan '14, 09:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-29274" class="comments-container"><span id="29277"></span><div id="comment-29277" class="comment"><div id="post-29277-score" class="comment-score"></div><div class="comment-text"><blockquote><p>How should I post that flow here?</p></blockquote><p>Please upload the capture file somewhere (cloudshark.org, Google drive, dropbox, etc.) and post the link here.</p></div><div id="comment-29277-info" class="comment-info"><span class="comment-age">(29 Jan '14, 10:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29274" class="comment-tools"></div><div class="clear"></div><div id="comment-29274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29318"></span>

<div id="answer-container-29318" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29318-score" class="post-score" title="current number of votes">0</div><span id="post-29318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think the problem is due to the MSS being too large to reach the destination. Packet No 5 never made it to the server and it is the first 'full-size MSS' packet of the connection.</p><pre><code> [1] -&gt;  SYN
 [2] &lt;-  SYN, ACK
 [3] -&gt;  ACK
 [4] -&gt;  PSH, ACK Seq=1 Ack=1     (tcp.len=12)
 [5] -&gt;  PSH, ACK Seq=13 Ack=1    (tcp.len=1460)  &lt;&lt;&lt; never arrives 
 [6] -&gt;  PSH, ACK Seq=1473 Ack=1  (tcp.len=???)
 [7] &lt;-  ACK      Seq=1 Ack=13  acking [4]
 [8] -&gt;  [5&#39;]   TCP Retransmission PSH, ACK Seq=13, Ack=1 &lt;&lt;&lt; never arrives 
 [9] -&gt;  [5&#39;&#39;]  TCP Retransmission PSH, ACK Seq=13, Ack=1 &lt;&lt;&lt; never arrives 
[10] -&gt;  [5&#39;&#39;&#39;] TCP Retransmission PSH, ACK Seq=13, Ack=1 &lt;&lt;&lt; never arrives 
[11] &lt;-  FIN, ACK Seq=1, Ack=13  acking [4]
[12] -&gt;  ACK Seq=549, Ack=2</code></pre><p>You might want to reduce your MTU on the route to 1400 and see if it helps...<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '14, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-29318" class="comments-container"></div><div id="comment-tools-29318" class="comment-tools"></div><div class="clear"></div><div id="comment-29318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

