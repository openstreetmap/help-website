+++
type = "question"
title = "Packet length varies a lot between 2 iscsi adapter cards"
description = '''I am running tests on 2 different types of iscsi adapter cards on linux. The test method is to call rsync to copy a folder with large amount of data files from the data center to a local hard drive. The wireshark shows that one test transfers TCP packets of 12 to 14 KBytes in the &quot;length&quot; column, th...'''
date = "2014-01-14T20:01:00Z"
lastmod = "2014-01-15T22:31:00Z"
weight = 28895
keywords = [ "cards", "iscsi", "adapter" ]
aliases = [ "/questions/28895" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Packet length varies a lot between 2 iscsi adapter cards](/questions/28895/packet-length-varies-a-lot-between-2-iscsi-adapter-cards)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28895-score" class="post-score" title="current number of votes">0</div><span id="post-28895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running tests on 2 different types of iscsi adapter cards on linux. The test method is to call rsync to copy a folder with large amount of data files from the data center to a local hard drive. The wireshark shows that one test transfers TCP packets of 12 to 14 KBytes in the "length" column, the other only shows 1KBytes. Both of them show TCP windows size 64KBytes. Could you provide any information to explain why the second card transmits such small packet?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cards" rel="tag" title="see questions tagged &#39;cards&#39;">cards</span> <span class="post-tag tag-link-iscsi" rel="tag" title="see questions tagged &#39;iscsi&#39;">iscsi</span> <span class="post-tag tag-link-adapter" rel="tag" title="see questions tagged &#39;adapter&#39;">adapter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '14, 20:01</strong></p><img src="https://secure.gravatar.com/avatar/7301bf58bb60c18ccb516caf5a52d453?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rsync&#39;s gravatar image" /><p><span>rsync</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rsync has no accepted answers">0%</span></p></div></div><div id="comments-container-28895" class="comments-container"></div><div id="comment-tools-28895" class="comment-tools"></div><div class="clear"></div><div id="comment-28895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28896"></span>

<div id="answer-container-28896" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28896-score" class="post-score" title="current number of votes">1</div><span id="post-28896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"one test transfers TCP packets of 12 to 14 KBytes in the "length" columumn "</p><p>This is only possible if Segmentation Offload is enabled on the NIC. So the other card might not support it.</p><p>You can check with <code>ethtool -k eth0</code> whether TCP segmentation offload is supported.</p><p>Is the MSS option in the 3-way handshake the same over both interfaces?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '14, 22:55</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-28896" class="comments-container"><span id="28930"></span><div id="comment-28930" class="comment"><div id="post-28930-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the reply, mrEEde.</p><p>You are right about the tcp segmentation offload setting. The first card has it enabled, but the second on was disabled. Following you suggestion, I turned on the segmentation Offload on the second card. I can see the TCP flow rate getting better, but the rsync performance seems not changes much. Also wireshark still shows the frame length is about 1K for the second card. I assume that the frame length had contributed the rsync performance difference between the 2 cards.</p><p>The MTU in both cases is set to 1500. And "ethtool -k" displays the same offload settings on both cards. I had not found a way to check the MSS yet. Any other settings could make such a difference in frame length?<br />
</p></div><div id="comment-28930-info" class="comment-info"><span class="comment-age">(15 Jan '14, 10:45)</span> <span class="comment-user userinfo">rsync</span></div></div><span id="28947"></span><div id="comment-28947" class="comment"><div id="post-28947-score" class="comment-score"></div><div class="comment-text"><p>Without a trace it is all guessing. Can you provide a sample trace including the 3-way handshake for both interfaces to <a href="http://cloudshark.org">http://cloudshark.org</a></p></div><div id="comment-28947-info" class="comment-info"><span class="comment-age">(15 Jan '14, 22:31)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-28896" class="comment-tools"></div><div class="clear"></div><div id="comment-28896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

