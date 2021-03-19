+++
type = "question"
title = "DUP ACK/ Retransmission"
description = '''I am pretty new to the networking side of things so bear with me. I am trying to figure out why it seems like our connections from the local machines on our network our timing out with our server. I decided to download wireshark to monitor the communication and I seem to have found when the errors a...'''
date = "2014-04-18T08:00:00Z"
lastmod = "2014-04-18T12:06:00Z"
weight = 31966
keywords = [ "dupackretrans" ]
aliases = [ "/questions/31966" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [DUP ACK/ Retransmission](/questions/31966/dup-ack-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31966-score" class="post-score" title="current number of votes">0</div><span id="post-31966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am pretty new to the networking side of things so bear with me. I am trying to figure out why it seems like our connections from the local machines on our network our timing out with our server. I decided to download wireshark to monitor the communication and I seem to have found when the errors are occurring. It looks like I am getting duplicate ACK and retransmissions. Is there any way to figure out why this is occurring. We have about 50 local machines and a majority of them are routinely getting these dropouts. I have tried to do some research on what could be causing this but most questions I see about this are people running in to the issue with websites. This is all internal to our office.</p><p>Here is a screenshot from wireshark <img src="http://i62.tinypic.com/2ef55bt.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dupackretrans" rel="tag" title="see questions tagged &#39;dupackretrans&#39;">dupackretrans</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '14, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/cc021aa01a1798ca2f20ab9622739d4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timbo126&#39;s gravatar image" /><p><span>timbo126</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timbo126 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Mar '15, 19:02</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-31966" class="comments-container"></div><div id="comment-tools-31966" class="comment-tools"></div><div class="clear"></div><div id="comment-31966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31971"></span>

<div id="answer-container-31971" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31971-score" class="post-score" title="current number of votes">0</div><span id="post-31971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have a similar issue. I performed a single file transfer over a point to point Ethernet connection and see this many times in the packet capture file: <a href="https://www.cloudshark.org/captures/57b5da1ba42a">https://www.cloudshark.org/captures/57b5da1ba42a</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '14, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/bc79b169a7422220c5ab0819234c3ddc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="knightmese&#39;s gravatar image" /><p><span>knightmese</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="knightmese has no accepted answers">0%</span></p></div></div><div id="comments-container-31971" class="comments-container"></div><div id="comment-tools-31971" class="comment-tools"></div><div class="clear"></div><div id="comment-31971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31972"></span>

<div id="answer-container-31972" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31972-score" class="post-score" title="current number of votes">0</div><span id="post-31972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>DUP ACKs are common in communication, it means server has not received packet sent by client. Please check transit network. There is nothing you can find out from client.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '14, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/ee0dd9b5ea44e7f8db0040e34109a712?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hardshah4&#39;s gravatar image" /><p><span>hardshah4</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hardshah4 has no accepted answers">0%</span></p></div></div><div id="comments-container-31972" class="comments-container"></div><div id="comment-tools-31972" class="comment-tools"></div><div class="clear"></div><div id="comment-31972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

