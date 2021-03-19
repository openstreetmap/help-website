+++
type = "question"
title = "TCP ACK Behavior"
description = '''I&#x27;ve been doing a lot of reading to try and conclusively determine the behaviour of ACKs (specifically delayed-ACKs) over TCP. I understand the concepts of delayed-ACKs but I&#x27;m trying to figure out how the receiving device determines when/how often to send an ACK. The extract below may help determin...'''
date = "2014-12-29T02:41:00Z"
lastmod = "2014-12-29T03:25:00Z"
weight = 38762
keywords = [ "ack", "tcp" ]
aliases = [ "/questions/38762" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TCP ACK Behavior](/questions/38762/tcp-ack-behavior)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38762-score" class="post-score" title="current number of votes">0</div><span id="post-38762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been doing a lot of reading to try and conclusively determine the behaviour of ACKs (specifically delayed-ACKs) over TCP. I understand the concepts of delayed-ACKs but I'm trying to figure out how the receiving device determines when/how often to send an ACK.</p><p>The extract below may help determine what I mean - This is a single reassembled HTTP GET (to bbc.co.uk) fragmented accordingly but what has got my interested is the varying ACK response. Sometimes every packet appears to be ACK'd, sometimes every other packet (which I understand to be typical delayed-ACK behaviour), but then I also see 3, 4, or more ACK-less packets before an ACK is sent.</p><p>Can anyone possibly give me an answer as to not only why this behaviour is seen, but also how the client and server at either end would know to wait for 2 packets before an ACK, then wait for 4, etc. Have I missed anything in the packet detail itself that perhaps tells me this?</p><p><img src="http://i.imgur.com/nsyWt55.png" alt="alt text" /></p><p>Many thanks for any help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '14, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/ac6e9420368839f4b6820b64cd74fae4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MetalMike&#39;s gravatar image" /><p><span>MetalMike</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MetalMike has no accepted answers">0%</span></p></img></div></div><div id="comments-container-38762" class="comments-container"></div><div id="comment-tools-38762" class="comment-tools"></div><div class="clear"></div><div id="comment-38762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38764"></span>

<div id="answer-container-38764" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38764-score" class="post-score" title="current number of votes">4</div><span id="post-38764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MetalMike has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is not necessary to "wait" for an ACK on either side unless the advertised window of the other side was completely used (which Wireshark diagnoses as "TCP Window Full" in most cases), so it doesn't matter if the receiver acks 1,2,3 or more packets in a single ACK.</p><p>The only thing it needs to do is to ACK when its own receive window is full. This ususally never (or at least should not) happens because every other packet is ACKed. You could call this "premature" ACK, because packets are acknowledged when there really is no need - but of course it helps keeping a fluid conversation if you ACK packets in a nice rhythm. It prevents the sender having to wait until the ACK comes in when the window is full.</p><p>Other than that, the ACK rhythm is determined (often based on some kind of heuristics) by each TCP stack, so it's hard to say why it was done in a certain pattern. A typical thing is that either every other packet is ACKed, or that you see receivers acking more and more packets in a single ACK when a lot of packets are transmitted in short order.</p><p>So lets say you have a stack that is set to wait for 200ms before ACKing a new packet to see if more packets come in that it could ACK with a single packet. If packets come in fast you may have 3 or more fitting into that time frame, which would mean all of them could be ACked in one packet. If they come in slow it will only ACK 2, or sometimes even just 1 packet if the delayed ACK timer runs out before another packet comes in. This usually happens for the last packet in a transmission if there is an odd number of segments.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '14, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38764" class="comments-container"><span id="38765"></span><div id="comment-38765" class="comment"><div id="post-38765-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much Jasper, this explains it for me perfectly.</p></div><div id="comment-38765-info" class="comment-info"><span class="comment-age">(29 Dec '14, 03:25)</span> <span class="comment-user userinfo">MetalMike</span></div></div></div><div id="comment-tools-38764" class="comment-tools"></div><div class="clear"></div><div id="comment-38764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

