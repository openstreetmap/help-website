+++
type = "question"
title = "Missing Packets?"
description = '''I am trying to observe downstream wireless data packets from an AP to a laptop. I see the downstream RTS and upstream CTS followed by an upstream Block ACK. The packet capture appears to be missing the downstream data packets. The streaming video to the laptop is working fine, so I know that a large...'''
date = "2011-12-21T18:35:00Z"
lastmod = "2011-12-22T15:53:00Z"
weight = 8075
keywords = [ "ack", "capture", "block" ]
aliases = [ "/questions/8075" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Missing Packets?](/questions/8075/missing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8075-score" class="post-score" title="current number of votes">1</div><span id="post-8075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to observe downstream wireless data packets from an AP to a laptop. I see the downstream RTS and upstream CTS followed by an upstream Block ACK. The packet capture appears to be missing the downstream data packets. The streaming video to the laptop is working fine, so I know that a large amount of data should be flowing to it. Has anyone seen this before?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-block" rel="tag" title="see questions tagged &#39;block&#39;">block</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '11, 18:35</strong></p><img src="https://secure.gravatar.com/avatar/02cf4ed95be4ca7470e1bd5ed538c62d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="S_P&#39;s gravatar image" /><p><span>S_P</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="S_P has no accepted answers">0%</span></p></div></div><div id="comments-container-8075" class="comments-container"></div><div id="comment-tools-8075" class="comment-tools"></div><div class="clear"></div><div id="comment-8075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8077"></span>

<div id="answer-container-8077" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8077-score" class="post-score" title="current number of votes">3</div><span id="post-8077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="S_P has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yup - this happens usually when you capture your own traffic with the same wireless card with which you are connected to the AP. Your NIC has to choose either to send data or recieve data, so you won't get all the packets due to your card having to send out ACKs while capturing.</p><p>Try sniffing from another machine if my guess about your setup was correct</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '11, 02:40</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-8077" class="comments-container"><span id="8086"></span><div id="comment-8086" class="comment"><div id="post-8086-score" class="comment-score"></div><div class="comment-text"><p>Thank you!!! Your suggestion worked. I am still confused, but now less so. I was indeed streaming to the same laptop on which I was capturing. However, I was connecting to the AP using the laptop's on-board WiFi while using an AirPcap Nx USB device for passive packet capture. Could this still cause a NIC conflict? Obviously, there is a conflict somewhere. Anyway, primary problem solved. HUGELY appreciate your help!</p></div><div id="comment-8086-info" class="comment-info"><span class="comment-age">(22 Dec '11, 13:45)</span> <span class="comment-user userinfo">S_P</span></div></div><span id="8087"></span><div id="comment-8087" class="comment"><div id="post-8087-score" class="comment-score"></div><div class="comment-text"><p>The scenario you describe should <em>NOT</em> cause a NIC conflict - the NIC conflict Landi describes is a conflict between two uses of the <em>same</em> NIC, but if you're connecting with the on-board Wi-Fi NIC and sniffing with a separate AirPcap device, that's two separate devices, and the AirPcap device should, as long as it can see the radio signal from your onboard NIC, be able to see its packets just as it can see packets from NICs on other machines.</p></div><div id="comment-8087-info" class="comment-info"><span class="comment-age">(22 Dec '11, 15:09)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="8090"></span><div id="comment-8090" class="comment"><div id="post-8090-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Guy. At least I now feel better about still being a bit confused! This might be the same problem or not, but now I am seeing the RTS and CTS packets, followed by 3-5 QoS Data packets, followed by a proper Block ACK. The way I read the standard, however, I should be seeing a BlockAckReq packet, following the QoS data packets, to trigger the Block ACK. This BlockAckReq packet is missing from multiple tests, involving different respective laptops. Is the BlockAckReq packet simply optional and not used or should I be seeing it?</p></div><div id="comment-8090-info" class="comment-info"><span class="comment-age">(22 Dec '11, 15:53)</span> <span class="comment-user userinfo">S_P</span></div></div></div><div id="comment-tools-8077" class="comment-tools"></div><div class="clear"></div><div id="comment-8077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

