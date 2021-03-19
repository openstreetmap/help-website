+++
type = "question"
title = "Difference between flow and packet"
description = '''hi i am a beginner in wireshark and work on a thesis about botnet detection. in many Articles i posed with flow IP Address and Flow Port Number in opposite of Packet IP Address and Packet Port Number. Now My Important question is this: What is The Difference between flow and packet in wireshark? can...'''
date = "2015-11-30T03:58:00Z"
lastmod = "2015-11-30T06:01:00Z"
weight = 48074
keywords = [ "flows" ]
aliases = [ "/questions/48074" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Difference between flow and packet](/questions/48074/difference-between-flow-and-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48074-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>hi i am a beginner in wireshark and work on a thesis about botnet detection. in many Articles i posed with flow IP Address and Flow Port Number in opposite of Packet IP Address and Packet Port Number. Now My Important question is this: What is The Difference between flow and packet in wireshark? can you please help me?</p></div><div id="question-tags" class="tags-container tags">flows</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '15, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/3a54827560d543b934b783f7cede5da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hamedmortazi&#39;s gravatar image" /><p>hamedmortazi<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hamedmortazi has no accepted answers">0%</span></p></div></div><div id="comments-container-48074" class="comments-container"></div><div id="comment-tools-48074" class="comment-tools"></div><div class="clear"></div><div id="comment-48074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48079"></span>

<div id="answer-container-48079" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48079-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the point of view of IP address and port, there is no difference between flow and packet.</p><p>From the vocabulary point of view, a "flow" in packet networks vernacular is a sequence of packets sent from the same source socket (a socket is a combination of IP address and port) to the same destination socket, usually for the same purpose (delivery of an amount of information which does not fit to a single packet).</p><p>Plus bear in mind that port numbers form up a separate address space for each protocol: UDP port 5060 is not the same thing as TCP port 5060, although both are IANA assigned for SIP service. And some protocols, like GRE, do not work with ports at all, only with IP addresses.</p><p>For convenience, Wireshark capture filter syntax permits to use just "port X", which has the meaning of "(protocol A and its port X) or (protocol B and its port X) or (protocol C and its port X)" etc. But it may be confusing for beginners, making the impression that port numbers are common for different protocols.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '15, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Nov '15, 06:16</p></div></div><div id="comments-container-48079" class="comments-container"><span id="48082"></span><div id="comment-48082" class="comment"><div id="post-48082-score" class="comment-score"></div><div class="comment-text"><p>hi thanks for response now my problem is this: in wireshark how can i found packets in one session ,contains many packets with same ip address in source and destination?</p></div><div id="comment-48082-info" class="comment-info"><span class="comment-age">(30 Nov '15, 06:17)</span> hamedmortazi</div></div><span id="48085"></span><div id="comment-48085" class="comment"><div id="post-48085-score" class="comment-score">1</div><div class="comment-text"><p>Go to Statistics -&gt; Conversations, you'll get a table of conversations (actually, flows) at different protocol levels. But I'm not sure I've understood your question properly.</p></div><div id="comment-48085-info" class="comment-info"><span class="comment-age">(30 Nov '15, 06:21)</span> sindy</div></div></div><div id="comment-tools-48079" class="comment-tools"></div><div class="clear"></div><div id="comment-48079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

