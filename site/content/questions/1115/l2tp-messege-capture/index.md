+++
type = "question"
title = "L2TP messege capture"
description = '''How can i see messeges (etc sccrq, scccn,icrq, icrp...) send by l2tp clients in wireshark? l2tp/ipsec connection is established between 2 windows machines (both windows server 2003), in captured i can see ikev1 negotiate, ppp negotiate but i cant see l2tp messeges, i&#x27;m using wireshark v1.4.0'''
date = "2010-11-24T15:30:00Z"
lastmod = "2010-11-29T04:10:00Z"
weight = 1115
keywords = [ "l2tp" ]
aliases = [ "/questions/1115" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [L2TP messege capture](/questions/1115/l2tp-messege-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1115-score" class="post-score" title="current number of votes">0</div><span id="post-1115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can i see messeges (etc sccrq, scccn,icrq, icrp...) send by l2tp clients in wireshark? l2tp/ipsec connection is established between 2 windows machines (both windows server 2003), in captured i can see ikev1 negotiate, ppp negotiate but i cant see l2tp messeges, i'm using wireshark v1.4.0</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-l2tp" rel="tag" title="see questions tagged &#39;l2tp&#39;">l2tp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '10, 15:30</strong></p><img src="https://secure.gravatar.com/avatar/dad628aaf822504141d5baa1cf68f170?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="makaraka&#39;s gravatar image" /><p><span>makaraka</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="makaraka has no accepted answers">0%</span></p></div></div><div id="comments-container-1115" class="comments-container"></div><div id="comment-tools-1115" class="comment-tools"></div><div class="clear"></div><div id="comment-1115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1118"></span>

<div id="answer-container-1118" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1118-score" class="post-score" title="current number of votes">1</div><span id="post-1118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would assume these to be <em>inside</em> the IPSec tunnel.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '10, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1118" class="comments-container"><span id="1119"></span><div id="comment-1119" class="comment"><div id="post-1119-score" class="comment-score"></div><div class="comment-text"><p>so if i trun off ipsec it should be visible in wireshark?</p></div><div id="comment-1119-info" class="comment-info"><span class="comment-age">(25 Nov '10, 03:28)</span> <span class="comment-user userinfo">makaraka</span></div></div><span id="1122"></span><div id="comment-1122" class="comment"><div id="post-1122-score" class="comment-score"></div><div class="comment-text"><p>I would assume so.</p></div><div id="comment-1122-info" class="comment-info"><span class="comment-age">(25 Nov '10, 03:51)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-1118" class="comment-tools"></div><div class="clear"></div><div id="comment-1118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1150"></span>

<div id="answer-container-1150" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1150-score" class="post-score" title="current number of votes">0</div><span id="post-1150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>ok i was trying to turn off ipsec on this tunnel and make it only l2tp without ipsec but it didn't work, microsoft help about configuring l2tp tunnel without ipsec is little (they say to add to reg one value and it should work but it doesn't), so here is my next question: is there a possibility to decrypt l2tp/ipsec messeges in wireshark to see l2tp control messeges (ie sccrq etc.) if i know preshared key used by ipsec and how can i do this?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '10, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/dad628aaf822504141d5baa1cf68f170?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="makaraka&#39;s gravatar image" /><p><span>makaraka</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="makaraka has no accepted answers">0%</span></p></div></div><div id="comments-container-1150" class="comments-container"></div><div id="comment-tools-1150" class="comment-tools"></div><div class="clear"></div><div id="comment-1150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

