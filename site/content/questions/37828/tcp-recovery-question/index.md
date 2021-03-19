+++
type = "question"
title = "TCP Recovery Question"
description = '''I have a slightly nuanced question on the recovery of TCP from packet loss. For sake of setting context, SACK is turned OFF. Additionally, we&#x27;re dealing with a Linux host using CUBIC and a NetApp Filer using New Reno. Under Wikipedia&#x27;s summarization of SACK (and why SACK is a good idea), I will base...'''
date = "2014-11-13T09:29:00Z"
lastmod = "2014-11-13T11:41:00Z"
weight = 37828
keywords = [ "congestion-control", "retransmit", "tcp" ]
aliases = [ "/questions/37828" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TCP Recovery Question](/questions/37828/tcp-recovery-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37828-score" class="post-score" title="current number of votes">0</div><span id="post-37828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a slightly nuanced question on the recovery of TCP from packet loss. For sake of setting context, SACK is turned OFF. Additionally, we're dealing with a Linux host using CUBIC and a NetApp Filer using New Reno.</p><p>Under Wikipedia's summarization of SACK (and why SACK is a good idea), I will base my question.</p><p>"Relying purely on the cumulative acknowledgment scheme employed by the original TCP protocol can lead to inefficiencies when packets are lost. For example, suppose 10,000 bytes are sent in 10 different TCP packets, and the first packet is lost during transmission. In a pure cumulative acknowledgment protocol, the receiver cannot say that it received bytes 1,000 to 9,999 successfully, but failed to receive the first packet, containing bytes 0 to 999. Thus the sender may then have to resend all 10,000 bytes."</p><p>The last sentence says <em>may</em>. This implies that it is not definitive and is probably conditional. Meaning, if SACK is <em>off</em>, the sender may need to resend all 10,000 bytes.<br />
</p><p>My recollection of this from school (a long time ago) was that if SACK was disabled we would see a full re-transmission of the TCP window from the point of the loss by the sender. However, in practice, I am not seeing that in a data stream I have been analyzing between a Linux client and a NetApp Filer over TCP NFS.</p><p>To illustrate the behavior I see, let's use Wikipedia's example, but add in a little more complexity. Say we have 10,000 bytes transmitted from the client to the Filer, and the filer receives bytes 2,000-5,000 and 7,000-10,000. In this case, because SACK is turned off, the Filer issues DUP ACKs when it notices it is missing data, only acknowledging up to the last contiguous byte of payload. Additionally, let us say that there are four missing packets in each missing gap. The Linux client then begins by sending the first missing packet after the last acknowledged byte, and then waits for the Filer to ACK it. Once ACKed, it sends the second missing packet, noticing only the last packets' payload was acknowledged and not the full window. The filer then sends an ACK back acknowledging up to the end of the second TCP packet, implying to the sender that it is missing more packets. We then start seeing the client exponentially increase RTO with each subsequent missing packet re-transmit. The nuance is that when we get to bytes 2,000-5,000, those are not re-transmitted by the client, and rather the sender is acknowledging up to byte 5,000 once data contiguous to byte 1,999 was successfully re-transmitted.</p><p>So under what circumstances will the sender retransmit bytes 2,000-5,000 (and 7,000-10,000) and when won't it, assuming SACK is off? Additionally, are there similar nuances with SACK enabled? I did read of some issues with TCP sequence randomization when using SACK, for example.</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-congestion-control" rel="tag" title="see questions tagged &#39;congestion-control&#39;">congestion-control</span> <span class="post-tag tag-link-retransmit" rel="tag" title="see questions tagged &#39;retransmit&#39;">retransmit</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '14, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/c35273db4cb55c5bf5cc1c48edadf1bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swass&#39;s gravatar image" /><p><span>swass</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swass has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-37828" class="comments-container"></div><div id="comment-tools-37828" class="comment-tools"></div><div class="clear"></div><div id="comment-37828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37829"></span>

<div id="answer-container-37829" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37829-score" class="post-score" title="current number of votes">0</div><span id="post-37829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="swass has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Modern stacks do not discard incoming packets after they have determined packet loss; they report the last sequence number right before the gap in their ACK number, but keep everything after that. There's only one condition: the incoming frames need to fit into the advertised window size, which is the buffer reserved for incoming bytes anyway.</p><p>So unless the sender sends more than the window size, everything is kept and ACKed in one single ACK as soon as the retransmission(s) came in, which totally makes sense - dropping packets after packet loss doesn't make any sense unless there is no buffer space. Of course, TCP implementation vary and there may be some that still do, but those are exotic stacks in most cases (e.g. embedded hardware where the developers don't care about getting it done right as long as it works in basic setups)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '14, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37829" class="comments-container"><span id="37834"></span><div id="comment-37834" class="comment"><div id="post-37834-score" class="comment-score"></div><div class="comment-text"><p>Thank you! This seems to address my question and makes sense. It also explains why I was told (back in the 90's) in school that the sender would retransmit the full window. The network stack has clearly evolved a lot since then.</p></div><div id="comment-37834-info" class="comment-info"><span class="comment-age">(13 Nov '14, 11:41)</span> <span class="comment-user userinfo">swass</span></div></div></div><div id="comment-tools-37829" class="comment-tools"></div><div class="clear"></div><div id="comment-37829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

