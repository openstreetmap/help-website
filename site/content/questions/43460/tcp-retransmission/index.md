+++
type = "question"
title = "TCP Retransmission"
description = '''Our applications sends numerous message types between a Rabbit module and a PC. A specific message always triggers a retransmission; everytime. What would cause this? There is nothing special about this message. It is a series of bytes like the other messages. How would I go about investigating? Als...'''
date = "2015-06-22T12:58:00Z"
lastmod = "2015-06-22T15:20:00Z"
weight = 43460
keywords = [ "retransmissions" ]
aliases = [ "/questions/43460" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Retransmission](/questions/43460/tcp-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43460-score" class="post-score" title="current number of votes">0</div><span id="post-43460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Our applications sends numerous message types between a Rabbit module and a PC. A specific message always triggers a retransmission; everytime. What would cause this? There is nothing special about this message. It is a series of bytes like the other messages. How would I go about investigating? Also, a TCP Dub Ack occurs.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '15, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/59e8904e52ebacb273b13e6f9e7aacbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Impactaa&#39;s gravatar image" /><p><span>Impactaa</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Impactaa has no accepted answers">0%</span></p></div></div><div id="comments-container-43460" class="comments-container"><span id="43461"></span><div id="comment-43461" class="comment"><div id="post-43461-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. CloudShark, Google Drive, Dropbox?</p></div><div id="comment-43461-info" class="comment-info"><span class="comment-age">(22 Jun '15, 13:05)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="43462"></span><div id="comment-43462" class="comment"><div id="post-43462-score" class="comment-score"></div><div class="comment-text"><p>Yes. <a href="https://www.dropbox.com/s/pg2n27r6v5ekz87/3000P_2%20WireShark.pcapng?dl=0">https://www.dropbox.com/s/pg2n27r6v5ekz87/3000P_2%20WireShark.pcapng?dl=0</a></p></div><div id="comment-43462-info" class="comment-info"><span class="comment-age">(22 Jun '15, 13:26)</span> <span class="comment-user userinfo">Impactaa</span></div></div><span id="43464"></span><div id="comment-43464" class="comment"><div id="post-43464-score" class="comment-score"></div><div class="comment-text"><p>Can you please post the frame number in the capture file, where you believe there is something happening?</p></div><div id="comment-43464-info" class="comment-info"><span class="comment-age">(22 Jun '15, 13:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43465"></span><div id="comment-43465" class="comment"><div id="post-43465-score" class="comment-score"></div><div class="comment-text"><p>It is very regular. see frame 8497 and the many before that.</p></div><div id="comment-43465-info" class="comment-info"><span class="comment-age">(22 Jun '15, 14:04)</span> <span class="comment-user userinfo">Impactaa</span></div></div></div><div id="comment-tools-43460" class="comment-tools"></div><div class="clear"></div><div id="comment-43460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43466"></span>

<div id="answer-container-43466" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43466-score" class="post-score" title="current number of votes">0</div><span id="post-43466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The retransmission timer of the 'rabbit' is very low (lower than the delay_ACK timer in windows) so when your windows application has nothing to return (in time) the rabbit device will start retransmitting the segments before windows would 'delayed' ACK the single segment received from the rabbit device. . So either the rabbit device uses a higher Retransmission Timer or your windows must reduce its delayACK timer to avoid those retransmissions .</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '15, 15:20</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-43466" class="comments-container"></div><div id="comment-tools-43466" class="comment-tools"></div><div class="clear"></div><div id="comment-43466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

