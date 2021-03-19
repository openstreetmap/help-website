+++
type = "question"
title = "sending request to other server"
description = '''when one visit any website by typing an url,say google.com then source send request to various product of google.com also (example www.gstatic.com or accounts.l.google.com or clients.l.google.com ) and this request is being capture by wireshark i want to remove/filter all the packets containing url(...'''
date = "2014-04-11T07:15:00Z"
lastmod = "2014-04-11T13:15:00Z"
weight = 31752
keywords = [ "url" ]
aliases = [ "/questions/31752" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [sending request to other server](/questions/31752/sending-request-to-other-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31752-score" class="post-score" title="current number of votes">0</div><span id="post-31752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when one visit any website by typing an url,say google.com then source send request to various product of google.com also (example www.gstatic.com or accounts.l.google.com or clients.l.google.com ) and this request is being capture by wireshark</p><p>i want to remove/filter all the packets containing url(like www.gstatic.com or accounts.l.google.com or clients.l.google.com ) of the product and only wants packets containing the url one have visited(typed) i.e google.com</p><p>is it possible to do this with wireshark??? if yes ,then what is the filter to apply</p><p>please help...</p><p>thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '14, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/8b45e81e7b825ca5d14327d460018c85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Deepak1991&#39;s gravatar image" /><p><span>Deepak1991</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Deepak1991 has no accepted answers">0%</span></p></div></div><div id="comments-container-31752" class="comments-container"></div><div id="comment-tools-31752" class="comment-tools"></div><div class="clear"></div><div id="comment-31752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31760"></span>

<div id="answer-container-31760" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31760-score" class="post-score" title="current number of votes">0</div><span id="post-31760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use the below display filter and change the site name as needed:</p><pre><code>http.host == www.site.com</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '14, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-31760" class="comments-container"></div><div id="comment-tools-31760" class="comment-tools"></div><div class="clear"></div><div id="comment-31760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

