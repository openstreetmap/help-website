+++
type = "question"
title = "ACK is being sent instead of SYN,ACK"
description = '''Hi, We have a scenario like my end LB is sending SYN message and from the far end it is sending ACK message instead of sending the SYN,ACK, and again LB end it is re-transmitting the packet.  Can you please help me why far end device/server is sending ACK message directly to SYN message instead of S...'''
date = "2017-05-12T06:57:00Z"
lastmod = "2017-05-16T08:13:00Z"
weight = 61367
keywords = [ "syn+ack" ]
aliases = [ "/questions/61367" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ACK is being sent instead of SYN,ACK](/questions/61367/ack-is-being-sent-instead-of-synack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61367-score" class="post-score" title="current number of votes">0</div><span id="post-61367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, We have a scenario like my end LB is sending SYN message and from the far end it is sending ACK message instead of sending the SYN,ACK, and again LB end it is re-transmitting the packet.</p><p>Can you please help me why far end device/server is sending ACK message directly to SYN message instead of SYN,ACk, what could be the issue does we need to check at our LB side or far end server side.</p><p>Thank You, Suresh</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-syn+ack" rel="tag" title="see questions tagged &#39;syn+ack&#39;">syn+ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '17, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/8477cdc3b1237768fa9f975cc4d4c00c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Suresh%20Jothi&#39;s gravatar image" /><p><span>Suresh Jothi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Suresh Jothi has no accepted answers">0%</span></p></div></div><div id="comments-container-61367" class="comments-container"></div><div id="comment-tools-61367" class="comment-tools"></div><div class="clear"></div><div id="comment-61367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61368"></span>

<div id="answer-container-61368" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61368-score" class="post-score" title="current number of votes">0</div><span id="post-61368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Suresh-</p><p>Are you sure the ACK is in response to the SYN and not an ACK to other data?</p><p>Do you have a complete trace?</p><p>Is it possible the far-end is not performing a 3-way handshake but trying to send discrete SYN and ACK messages in response to the initial SYN as diagrammed in RFC 793 on page 27? NOTE: I've never (EVER) seen a device do this but just speculating.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '17, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/efd6c87b3ea03d76a316e1bc5cf19a07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbAtAffirmed&#39;s gravatar image" /><p><span>dbAtAffirmed</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbAtAffirmed has no accepted answers">0%</span></p></div></div><div id="comments-container-61368" class="comments-container"><span id="61435"></span><div id="comment-61435" class="comment"><div id="post-61435-score" class="comment-score"></div><div class="comment-text"><p>Suresh- I saw your trace (not sure why it doesn't show up here)... The far end looks quite broken. If you are not already running the capture on that device I would suggest you run it there (103.16.101.51) to get its point-of-view to ensure there isn't anything funny going on. /dave</p></div><div id="comment-61435-info" class="comment-info"><span class="comment-age">(16 May '17, 08:13)</span> <span class="comment-user userinfo">dbAtAffirmed</span></div></div></div><div id="comment-tools-61368" class="comment-tools"></div><div class="clear"></div><div id="comment-61368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

