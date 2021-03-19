+++
type = "question"
title = "Not getting the ACK I&#x27;m expecting"
description = '''Hello, I&#x27;m doing some homework and my assigment is getting 6 TCP segments which start with a HTTP POST segment and then finding out when the ACK of each of those segments was received, the problem is that I have only managed to find 2 of the ACK one of the 2nd and one of the last segment. Why is it ...'''
date = "2014-04-26T14:40:00Z"
lastmod = "2014-04-27T07:06:00Z"
weight = 32202
keywords = [ "ack", "wireshark" ]
aliases = [ "/questions/32202" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Not getting the ACK I'm expecting](/questions/32202/not-getting-the-ack-im-expecting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32202-score" class="post-score" title="current number of votes">0</div><span id="post-32202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm doing some homework and my assigment is getting 6 TCP segments which start with a HTTP POST segment and then finding out when the ACK of each of those segments was received, the problem is that I have only managed to find 2 of the ACK one of the 2nd and one of the last segment. Why is it that the other ACK are not showing up?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '14, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/ed029edd87c75b038587aeb9b0d76d1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Niena&#39;s gravatar image" /><p><span>Niena</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Niena has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Apr '14, 14:40</strong> </span></p></div></div><div id="comments-container-32202" class="comments-container"><span id="32203"></span><div id="comment-32203" class="comment"><div id="post-32203-score" class="comment-score"></div><div class="comment-text"><p>Can you post the capture at <a href="http://www.cloudshark.org">http://www.cloudshark.org</a>?</p></div><div id="comment-32203-info" class="comment-info"><span class="comment-age">(26 Apr '14, 15:22)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="32210"></span><div id="comment-32210" class="comment"><div id="post-32210-score" class="comment-score"></div><div class="comment-text"><p>Google on "Delayed ACK"</p></div><div id="comment-32210-info" class="comment-info"><span class="comment-age">(26 Apr '14, 19:12)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="32211"></span><div id="comment-32211" class="comment"><div id="post-32211-score" class="comment-score"></div><div class="comment-text"><p>here's the link: <a href="https://www.cloudshark.org/captures/5deb675a0d71">https://www.cloudshark.org/captures/5deb675a0d71</a></p><p>The POST segment is the no. 29 and the segments that I'm analyzing are the no. 29, 30, 33, 37, 38 and 39. You can see that the response ACK of segment no. 30 is the no. 36.</p><p>Is there anyway I can check if this ACK is a "delayed ACK"?</p></div><div id="comment-32211-info" class="comment-info"><span class="comment-age">(26 Apr '14, 19:40)</span> <span class="comment-user userinfo">Niena</span></div></div></div><div id="comment-tools-32202" class="comment-tools"></div><div class="clear"></div><div id="comment-32202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32212"></span>

<div id="answer-container-32212" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32212-score" class="post-score" title="current number of votes">0</div><span id="post-32212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Niena has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't see the problem you report here. You only see 2 ACKs that ack an outbound segment. However there are more ACKs coming in. In fact you're getting more ACKs in between.</p><p>The reason is that your client is using TCP segmentation offload sending more than the negotiated MSS. The server acks bytes in the middle of your segments as it receives them in MSS sized segments.</p><p>In the trace example #36 acks #30 and #45 acks #39. The other acks (31-32,34-36,40,42-43) ack bytes within the large segments seen in your trace. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_045_1.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '14, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-32212" class="comments-container"><span id="32215"></span><div id="comment-32215" class="comment"><div id="post-32215-score" class="comment-score"></div><div class="comment-text"><p>So, for example ACKS 31, 32, 34 and 35 are confirmation ACKS for 29 and 30 but 36 acks 30 because it actually acknowledges the next sequence number the server is expecting to receive?</p><p>Thanks for your help :)</p></div><div id="comment-32215-info" class="comment-info"><span class="comment-age">(27 Apr '14, 07:06)</span> <span class="comment-user userinfo">Niena</span></div></div></div><div id="comment-tools-32212" class="comment-tools"></div><div class="clear"></div><div id="comment-32212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

