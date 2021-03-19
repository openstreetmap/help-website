+++
type = "question"
title = "i also get this on expert infos in the columns"
description = '''columns sequence tcp duplicate ack so far 34 and counting what is this?'''
date = "2014-11-08T11:39:00Z"
lastmod = "2014-11-10T00:20:00Z"
weight = 37703
keywords = [ "wireshark" ]
aliases = [ "/questions/37703" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [i also get this on expert infos in the columns](/questions/37703/i-also-get-this-on-expert-infos-in-the-columns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37703-score" class="post-score" title="current number of votes">0</div><span id="post-37703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>columns sequence tcp duplicate ack so far 34 and counting what is this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '14, 11:39</strong></p><img src="https://secure.gravatar.com/avatar/08a002781d656e49c05a3be0352280e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MostUnlikedOnPS4&#39;s gravatar image" /><p><span>MostUnlikedO...</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MostUnlikedOnPS4 has no accepted answers">0%</span></p></div></div><div id="comments-container-37703" class="comments-container"></div><div id="comment-tools-37703" class="comment-tools"></div><div class="clear"></div><div id="comment-37703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37718"></span>

<div id="answer-container-37718" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37718-score" class="post-score" title="current number of votes">0</div><span id="post-37718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you are seeing lots of duplicate acknowledgements with increasingly high dup ack numbers this means that you were sending out data at a high send rate and an early packet in the window was lost.<br />
Duplicate acks indicate the receiving TCP has seen a packet out of order - either lost or delayed - and the arrival of the 3rd dup_ack triggers a fast retransmission at the sender.<br />
This is not unusual to see and it is not indicative af a severe problem.</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '14, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-37718" class="comments-container"></div><div id="comment-tools-37718" class="comment-tools"></div><div class="clear"></div><div id="comment-37718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

