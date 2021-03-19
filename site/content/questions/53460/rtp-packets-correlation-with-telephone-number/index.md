+++
type = "question"
title = "RTP packets correlation with telephone number"
description = '''I&#x27;ve captured all the packets from the server for 5 minutes. In this time there where 3 calls made from the same client to the same supplier. When I filter the RTP packets in wireshark I do not know which RTP packets are for the 2nd call. Can you give me any hints on how to associate the RTP packets...'''
date = "2016-06-15T05:50:00Z"
lastmod = "2016-06-15T06:24:00Z"
weight = 53460
keywords = [ "rtp", "identity", "correlation" ]
aliases = [ "/questions/53460" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP packets correlation with telephone number](/questions/53460/rtp-packets-correlation-with-telephone-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53460-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've captured all the packets from the server for 5 minutes. In this time there where 3 calls made from the same client to the same supplier. When I filter the RTP packets in wireshark I do not know which RTP packets are for the 2nd call. Can you give me any hints on how to associate the RTP packets ( audio ) with the call / telephone number ? I do not know which audio is for which number...</p></div><div id="question-tags" class="tags-container tags">rtp identity correlation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '16, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/73e12c60e2d73f1d46621a04fc2504a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eduard%20Petru&#39;s gravatar image" /><p>Eduard Petru<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eduard Petru has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jun '16, 07:28</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-53460" class="comments-container"></div><div id="comment-tools-53460" class="comment-tools"></div><div class="clear"></div><div id="comment-53460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53462"></span>

<div id="answer-container-53462" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53462-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Normally Wireshark assigns RTP streams to signalling (or, to be precise, control in case of MGCP and Megaco) exchanges automatically, as it identifies RTP by the contents of SDPs exchanged between parties in the signalling. So if you use <code>Telephony -&gt; VoIP Calls</code>, you'll get a list of VoIP calls found in the capture, and if you select one or more of the items in the list and press the <code>Flow Sequence</code> button, you'll see the signalling/control protocol's messages as well as RTP streams as arrows in the ladder graph, labelled with important fields of the call control messages (like calling and called numbers) and with UDP/TCP port numbers, which allows you to identify the RTP streams.</p><p>If you select a single call, you can use the <code>&gt; Play Streams</code> button to replay the audio of that call directly from the list.</p><p>Is this an answer to your question or you've tried this and some part of it does not work?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '16, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53462" class="comments-container"><span id="53486"></span><div id="comment-53486" class="comment"><div id="post-53486-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much, I have managed somehow to correlate the port session and filter the RBT. I've also noticed there is a problem when streaming codecs G729. Thank you again.</p></div><div id="comment-53486-info" class="comment-info"><span class="comment-age">(15 Jun '16, 23:48)</span> Eduard Petru</div></div><span id="53503"></span><div id="comment-53503" class="comment"><div id="post-53503-score" class="comment-score"></div><div class="comment-text"><p>See the wiki page <a href="https://wiki.wireshark.org/HowToDecodeG729">here</a> for info about G729.</p></div><div id="comment-53503-info" class="comment-info"><span class="comment-age">(16 Jun '16, 12:57)</span> grahamb ♦</div></div></div><div id="comment-tools-53462" class="comment-tools"></div><div class="clear"></div><div id="comment-53462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

