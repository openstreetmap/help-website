+++
type = "question"
title = "Finding Url&#x27;s"
description = '''How would i find all of our internal Url&#x27;s, like for SharePoint sites, Printers, help desk portal and so one, also do i need domain admin right to get retrieve the data if i am already a user on the network?'''
date = "2014-05-27T15:53:00Z"
lastmod = "2014-05-27T22:42:00Z"
weight = 33120
keywords = [ "admin", "domain", "urls" ]
aliases = [ "/questions/33120" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Finding Url's](/questions/33120/finding-urls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33120-score" class="post-score" title="current number of votes">0</div><span id="post-33120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How would i find all of our internal Url's, like for SharePoint sites, Printers, help desk portal and so one, also do i need domain admin right to get retrieve the data if i am already a user on the network?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-admin" rel="tag" title="see questions tagged &#39;admin&#39;">admin</span> <span class="post-tag tag-link-domain" rel="tag" title="see questions tagged &#39;domain&#39;">domain</span> <span class="post-tag tag-link-urls" rel="tag" title="see questions tagged &#39;urls&#39;">urls</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '14, 15:53</strong></p><img src="https://secure.gravatar.com/avatar/74393373255b5eb6a5bc7e1800de8be8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yo%20momma&#39;s gravatar image" /><p><span>Yo momma</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yo momma has no accepted answers">0%</span></p></div></div><div id="comments-container-33120" class="comments-container"></div><div id="comment-tools-33120" class="comment-tools"></div><div class="clear"></div><div id="comment-33120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33121"></span>

<div id="answer-container-33121" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33121-score" class="post-score" title="current number of votes">0</div><span id="post-33121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, capture at a spot where the packets have to come through, and filter on http requests, e.g. with "http.request.method". Or use the HTTP statistics in the statistics menu.</p><p>You need local admin rights on the PC where you want to capture, it doesn't have to be a domain admin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '14, 16:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33121" class="comments-container"><span id="33125"></span><div id="comment-33125" class="comment"><div id="post-33125-score" class="comment-score"></div><div class="comment-text"><p>what do you means by capture a spot, what if i do not know any urls and what to try to find them all?</p></div><div id="comment-33125-info" class="comment-info"><span class="comment-age">(27 May '14, 21:56)</span> <span class="comment-user userinfo">Yo momma</span></div></div><span id="33127"></span><div id="comment-33127" class="comment"><div id="post-33127-score" class="comment-score"></div><div class="comment-text"><p>Why do you need all internal 'URLs'. Maybe that helps to understand your request....</p></div><div id="comment-33127-info" class="comment-info"><span class="comment-age">(27 May '14, 22:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-33121" class="comment-tools"></div><div class="clear"></div><div id="comment-33121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

