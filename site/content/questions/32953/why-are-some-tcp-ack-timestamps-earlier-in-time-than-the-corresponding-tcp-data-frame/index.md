+++
type = "question"
title = "Why are some TCP ACK timestamps earlier in time than the corresponding TCP data frame?"
description = '''Hi all, I am running Wireshark 1.10.7 (v1.10.7-0-g6b931a1 from master-1.10) on a Windows 7 Professional computer. Since the network card of the computer supports offloading segmentation of large TCP/IP frames, frames with a size greater than the MTU are captured by Wireshark. Now every time when the...'''
date = "2014-05-21T07:13:00Z"
lastmod = "2014-05-22T03:06:00Z"
weight = 32953
keywords = [ "ack", "timestamps", "tcp" ]
aliases = [ "/questions/32953" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why are some TCP ACK timestamps earlier in time than the corresponding TCP data frame?](/questions/32953/why-are-some-tcp-ack-timestamps-earlier-in-time-than-the-corresponding-tcp-data-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32953-score" class="post-score" title="current number of votes">0</div><span id="post-32953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am running Wireshark 1.10.7 (v1.10.7-0-g6b931a1 from master-1.10) on a Windows 7 Professional computer. Since the network card of the computer supports offloading segmentation of large TCP/IP frames, frames with a size greater than the MTU are captured by Wireshark.</p><p>Now every time when the local computer sends a frame greater than the MTU, the TCP corresponding ackowledgement is received earlier in time than the sent TCP frame, e.g.</p><pre><code>No. 1636 (16.996621000s): Transmission Control Protocol, Src Port: ctf (84), Dst Port: 55697 (55697), Seq: 36821, Ack: 10255, Len: 0, Flags: 0x010 (ACK)

No. 1657 (17.173938000s): Transmission Control Protocol, Src Port: 55697 (55697), Dst Port: ctf (84), Seq: 10255, Ack: 37161, Len: 1982, 0x0018</code></pre><p>Of course, the IP addresses of these flows are matching each other (x-&gt;y and y-&gt;x).</p><p>So, how can it be that the timestamp of the ACK is earlier in time than the corresponding TCP data frame?</p><p>Thanks, Sven</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '14, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/29fc7e1b8b26c86a12f68617a425c66f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johannes24&#39;s gravatar image" /><p><span>johannes24</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johannes24 has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 May '14, 08:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-32953" class="comments-container"></div><div id="comment-tools-32953" class="comment-tools"></div><div class="clear"></div><div id="comment-32953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32954"></span>

<div id="answer-container-32954" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32954-score" class="post-score" title="current number of votes">1</div><span id="post-32954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="johannes24 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The ACK: 10255 means that is the next expected SEQ number to be received from the other host.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '14, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-32954" class="comments-container"><span id="32955"></span><div id="comment-32955" class="comment"><div id="post-32955-score" class="comment-score"></div><div class="comment-text"><blockquote>The ACK: 10255 means that is the next expected SEQ number to be received from the other host</blockquote><p>i.e. the next sequence number to be transmitted after the ACK (if things are all running smoothly).</p><p>What you have shown is the ack for a previous packet then the next packet with the correct sequence number.</p></div><div id="comment-32955-info" class="comment-info"><span class="comment-age">(21 May '14, 08:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="32979"></span><div id="comment-32979" class="comment"><div id="post-32979-score" class="comment-score"></div><div class="comment-text"><p>Damn right! Thanks Rooster_50 and grahamb for clarification! Have a nice day!</p></div><div id="comment-32979-info" class="comment-info"><span class="comment-age">(22 May '14, 03:06)</span> <span class="comment-user userinfo">johannes24</span></div></div></div><div id="comment-tools-32954" class="comment-tools"></div><div class="clear"></div><div id="comment-32954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

