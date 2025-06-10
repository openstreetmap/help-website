+++
type = "question"
title = "Getting a token"
description = '''I&#x27;m really confused about how to get a token. The OAuth page in the wiki has some links that seem to imply they will let me request a token but they all give error pages. Is it just that those pages are temporarily broken? Or is there some other way that is supposed to happen?'''
date = "2012-06-02T14:41:00Z"
lastmod = "2012-06-02T17:55:00Z"
weight = 13203
keywords = [ "oauth" ]
aliases = [ "/questions/13203" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting a token](/questions/13203/getting-a-token)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13203-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm really confused about how to get a token. The OAuth page in the wiki has some links that seem to imply they will let me request a token but they all give error pages. Is it just that those pages are temporarily broken? Or is there some other way that is supposed to happen?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-oauth" rel="tag" title="see questions tagged &#39;oauth&#39;">oauth</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '12, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/7f21fabe666713f3825297e6577a396c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elinw&#39;s gravatar image" />
<p><span>elinw</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elinw has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13203" class="comments-container">
&#10;</div>
<div id="comment-tools-13203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13203-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13204"></span>

<div id="answer-container-13204" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13204-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The urls on the wiki page is the urls for the service. You need to pass correct arguments to those urls to get a token. Normaly you provide those urls to the oAuth library you are using and make it to the rest.</p>
<p>You can have a look at the documentation at <a href="http://oauth.net/documentation/">oAuth.net</a> for information about how the oAuth protocol works.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '12, 15:37</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-13204" class="comments-container">
<span id="13206"></span>
<div id="comment-13206" class="comment">
<div id="post-13206-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay that makes sense, the implication to me reading the docs was that there was something else coming from OSM.</p>
</div>
<div id="comment-13206-info" class="comment-info">
<span class="comment-age">(02 Jun '12, 17:55)</span> <span class="comment-user userinfo">elinw</span>
</div>
</div>
</div>
<div id="comment-tools-13204" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13204-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

