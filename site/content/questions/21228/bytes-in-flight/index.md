+++
type = "question"
title = "Bytes in flight"
description = '''Hi all,i have one query that in a normal tcp communication without sack lets say if server sends 3 segments of data each having 1290 bytes of data which client never receives(lost in transit) so upon receiving dup ack server is retransmitting 1290 bytes of data but in seq+ack analysis menu &quot;Bytes in...'''
date = "2013-05-17T09:29:00Z"
lastmod = "2013-05-20T04:11:00Z"
weight = 21228
keywords = [ "tcp" ]
aliases = [ "/questions/21228" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bytes in flight](/questions/21228/bytes-in-flight)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21228-score" class="post-score" title="current number of votes">0</div><span id="post-21228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,i have one query that in a normal tcp communication without sack lets say if server sends 3 segments of data each having 1290 bytes of data which client never receives(lost in transit) so upon receiving dup ack server is retransmitting 1290 bytes of data but in seq+ack analysis menu "Bytes in Flight" is showing 4384 bytes but question is sender has just send 1290 bytes.how bytes in flight calculated here.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '13, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-21228" class="comments-container"><span id="21229"></span><div id="comment-21229" class="comment"><div id="post-21229-score" class="comment-score"></div><div class="comment-text"><p>this doesnt add up. Do you have a trace you could post at <a href="http://cloudshark.org">http://cloudshark.org</a>? Only if not confidential.</p></div><div id="comment-21229-info" class="comment-info"><span class="comment-age">(17 May '13, 10:00)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="21299"></span><div id="comment-21299" class="comment"><div id="post-21299-score" class="comment-score"></div><div class="comment-text"><p>jasper does bytes in flight means acknowledge data,please correct me if i m wrong</p></div><div id="comment-21299-info" class="comment-info"><span class="comment-age">(20 May '13, 04:10)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="21300"></span><div id="comment-21300" class="comment"><div id="post-21300-score" class="comment-score"></div><div class="comment-text"><p>i means unacknowledged</p></div><div id="comment-21300-info" class="comment-info"><span class="comment-age">(20 May '13, 04:11)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-21228" class="comment-tools"></div><div class="clear"></div><div id="comment-21228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

