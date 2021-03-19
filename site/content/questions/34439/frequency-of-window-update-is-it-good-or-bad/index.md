+++
type = "question"
title = "frequency of window update is it good or bad"
description = '''Hi I was monitoring the packets communication between my client server and sql server. There is query which retrieves about 10mb of data. during which there are a lot of windows update. Also while transferring the data from sql server in half way of transfer would be TCP ACK from the client and then...'''
date = "2014-07-06T01:44:00Z"
lastmod = "2014-07-06T14:57:00Z"
weight = 34439
keywords = [ "window" ]
aliases = [ "/questions/34439" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [frequency of window update is it good or bad](/questions/34439/frequency-of-window-update-is-it-good-or-bad)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34439-score" class="post-score" title="current number of votes">0</div><span id="post-34439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I was monitoring the packets communication between my client server and sql server. There is query which retrieves about 10mb of data. during which there are a lot of windows update. Also while transferring the data from sql server in half way of transfer would be TCP ACK from the client and then after 25ms there would be window update after which only the transfer would start again. This pattern would continue till the end of transfer.<br />
Questions is 1) Is this a normal behavior while transferring large data. 2) during this transfer there where 2 window zero request also. Is having 2 window zero request for this transaction acceptable or could it be interpreted that the client machine was not able sufficient powerful enough to process this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '14, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/be8a9b2e9d87b13606c3b9e75d26e71d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scara&#39;s gravatar image" /><p><span>scara</span><br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scara has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-34439" class="comments-container"></div><div id="comment-tools-34439" class="comment-tools"></div><div class="clear"></div><div id="comment-34439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34442"></span>

<div id="answer-container-34442" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34442-score" class="post-score" title="current number of votes">0</div><span id="post-34442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Zero window is not a request. It is the client machine announcing that it has no more room in its receive buffer, which forces the sender to stop transmitting. This means that the client application is not reading the data as fast is it's coming in.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '14, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-34442" class="comments-container"></div><div id="comment-tools-34442" class="comment-tools"></div><div class="clear"></div><div id="comment-34442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

