+++
type = "question"
title = "What are SRE and SLE?"
description = '''What do SRE and SLE stand for in the packet capture display? I&#x27;m looking at TCP packets so I assume it has something to do with windowing.'''
date = "2010-12-17T13:57:00Z"
lastmod = "2010-12-21T06:39:00Z"
weight = 1389
keywords = [ "display", "packet" ]
aliases = [ "/questions/1389" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What are SRE and SLE?](/questions/1389/what-are-sre-and-sle)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1389-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What do SRE and SLE stand for in the packet capture display? I'm looking at TCP packets so I assume it has something to do with windowing.</p></div><div id="question-tags" class="tags-container tags">display packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '10, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/9c60360bc3e38395976e6200f52d1180?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="catimossi&#39;s gravatar image" /><p>catimossi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="catimossi has no accepted answers">0%</span></p></div></div><div id="comments-container-1389" class="comments-container"></div><div id="comment-tools-1389" class="comment-tools"></div><div class="clear"></div><div id="comment-1389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1391"></span>

<div id="answer-container-1391" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1391-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>They are the Right Edge (SRE) and Left Edge (SLE) of already acknowledged data when Selective Acknowledgments are used. This prevents retransmission of this data.</p><p>See also <a href="http://tools.ietf.org/html/rfc2018">RFC 2018</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '10, 17:05</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jan '13, 14:49</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-1391" class="comments-container"></div><div id="comment-tools-1391" class="comment-tools"></div><div class="clear"></div><div id="comment-1391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1435"></span>

<div id="answer-container-1435" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1435-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>To add to Sake's post, SACK (Selective ACK) is used to identify holes in the TCP stream. This prevents the stack from having to go back to where the loss occurred and start all over. So the pkts from the normal ACK field (in the "normal" ACK field) to the LE is good to go. But from the LE to the RE, pkts were lost. So if the pkts are transferred like this (1, through 10)</p><p>10 9 8 7 6 5 4 3 2 1 ---&gt;<br />
</p><p>in normal ACK scenario, if pkt 4 is lost, it will look like this to the receiver</p><p>10 9 8 7 6 5 XX 3 2 1 ---&gt;<br />
</p><p>So the receiver will repeatedly ack saying "I need pkt 4...I need pkt 4, I need pkt 4" as other pkts (5-10) trickle in. When three of these acks are received, it triggers the fast retransmission, BTW.</p><p>When SACK is used, the receiver identifies the hole at pkt 4 position. So it doesn't throw pkts 5-10 away...instead, it sends a SACK requesting for pkt#4.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '10, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></br></p></div></div><div id="comments-container-1435" class="comments-container"><span id="17998"></span><div id="comment-17998" class="comment"><div id="post-17998-score" class="comment-score"></div><div class="comment-text"><p>sorry to raise an old question.</p><p>As per RFC I believe that packets from the LE to the RE are GOOD.</p><p>So if we have ACK=3, LE=5, RE=10,</p><p>it means that packet 4 is lost, packets 5-10 are good.</p><p>Am i missing something?</p></div><div id="comment-17998-info" class="comment-info"><span class="comment-age">(28 Jan '13, 01:46)</span> v_paranoid</div></div><span id="18005"></span><div id="comment-18005" class="comment"><div id="post-18005-score" class="comment-score"></div><div class="comment-text"><p>no, you are absolutely right</p></div><div id="comment-18005-info" class="comment-info"><span class="comment-age">(28 Jan '13, 09:53)</span> Landi</div></div><span id="18015"></span><div id="comment-18015" class="comment"><div id="post-18015-score" class="comment-score"></div><div class="comment-text"><p>Only the values in the LE and RE are not packet numbers, but sequence numbers :-)</p></div><div id="comment-18015-info" class="comment-info"><span class="comment-age">(28 Jan '13, 12:46)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-1435" class="comment-tools"></div><div class="clear"></div><div id="comment-1435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

