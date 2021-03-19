+++
type = "question"
title = "Looking for an 802.11 expert.  Missing 802.11 BlockAckReq"
description = '''I am analyzing 802.11 block ACK operation. I am seeing the initial RTS/CTS exchange, followed by a block of QoS data packets, followed by a Block ACK. The capture appears to be missing the BlockAckReq following the block of data packets. Is there some commonly used way to trigger transmission of a b...'''
date = "2011-12-22T18:49:00Z"
lastmod = "2012-10-16T05:51:00Z"
weight = 8096
keywords = [ "blockack" ]
aliases = [ "/questions/8096" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Looking for an 802.11 expert. Missing 802.11 BlockAckReq](/questions/8096/looking-for-an-80211-expert-missing-80211-blockackreq)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8096-score" class="post-score" title="current number of votes">0</div><span id="post-8096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am analyzing 802.11 block ACK operation. I am seeing the initial RTS/CTS exchange, followed by a block of QoS data packets, followed by a Block ACK. The capture appears to be missing the BlockAckReq following the block of data packets. Is there some commonly used way to trigger transmission of a block ACK that I am missing? I read something about an "implicit block ack request", but such beast appears to be related to A-MSDUs, which according to my packets are not allowed. Any thoughts?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-blockack" rel="tag" title="see questions tagged &#39;blockack&#39;">blockack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '11, 18:49</strong></p><img src="https://secure.gravatar.com/avatar/02cf4ed95be4ca7470e1bd5ed538c62d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="S_P&#39;s gravatar image" /><p><span>S_P</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="S_P has no accepted answers">0%</span></p></div></div><div id="comments-container-8096" class="comments-container"><span id="8103"></span><div id="comment-8103" class="comment"><div id="post-8103-score" class="comment-score"></div><div class="comment-text"><p>I'm not an expert for the new .11n features - but as far as I understand this topic the use of block ACKs is only requested once per session. Did you capture the whole traffic right from the association ?</p></div><div id="comment-8103-info" class="comment-info"><span class="comment-age">(23 Dec '11, 01:05)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="8145"></span><div id="comment-8145" class="comment"><div id="post-8145-score" class="comment-score"></div><div class="comment-text"><p>By my reading of the 802.11 standard, section 9.10, Block ACK operation is initially established between devices using ADDBA Request and ADDBA Response messages, which I see in the capture. Reading 9.10 (e.g., as shown in Figure 9-21), it appears that during operation, the sender of the data block requests the Block ACK with a BlockAckReq message, which should then be followed by the Block ACK from the recipient of the block. It is this BlockAckReq message that I am failing to see in the capture.</p></div><div id="comment-8145-info" class="comment-info"><span class="comment-age">(27 Dec '11, 18:20)</span> <span class="comment-user userinfo">S_P</span></div></div></div><div id="comment-tools-8096" class="comment-tools"></div><div class="clear"></div><div id="comment-8096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15033"></span>

<div id="answer-container-15033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15033-score" class="post-score" title="current number of votes">0</div><span id="post-15033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not an expert, but as far as I can tell, what you are seeing most likely is implicit Block Ack request. It is related to A-MPDU, not A-MSDU. If A-MPDU contains at least one MPDU with 'Ack Policy' field set to 'Block Ack' (zero), means it is a implicit Block Ack request. So the receiving station should respond with BlockAck frame. See 802.11n standard, 9.10.7.5 ('Generation and transmission of BlockAck by an HT STA')</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '12, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/b6959e1981d3c2bf71f9759416db943e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pcfist&#39;s gravatar image" /><p><span>pcfist</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pcfist has no accepted answers">0%</span></p></div></div><div id="comments-container-15033" class="comments-container"></div><div id="comment-tools-15033" class="comment-tools"></div><div class="clear"></div><div id="comment-15033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

