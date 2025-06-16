+++
type = "question"
title = "Get most recent changeset for user"
description = '''I want to (programatically) get the most recent changeset for a user (specifically, I need the timestamp of when it was closed, if it was). There doesn&#x27;t seem to be any API means of doing this, unless I&#x27;m missing something. There isn&#x27;t a way to get user UID from username (nor can I see a way to do t...'''
date = "2014-10-28T21:29:00Z"
lastmod = "2014-10-28T22:18:00Z"
weight = 38061
keywords = [ "username", "changeset", "api" ]
aliases = [ "/questions/38061" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get most recent changeset for user](/questions/38061/get-most-recent-changeset-for-user)

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
<span id="post-38061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38061-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to (programatically) get the most recent changeset for a user (specifically, I need the timestamp of when it was closed, if it was).</p>
<p>There doesn't seem to be any API means of doing this, unless I'm missing something. There isn't a way to get user UID from username (nor can I see a way to do this manually), and there isn't a means to get changesets by user, either by UID or username (if there was a way to get a user UID e.g. on their profile page, I could start with that, but username is easier - yes I know it could change in principle).</p>
<p>I can see how to do it - the main website does it - but it isn't nice, in that it means parsing a fragment of HTML rather than properly structured XML as the API would...</p>
<p><a href="https://www.openstreetmap.org/user/">https://www.openstreetmap.org/user/</a><em>username</em>/history?list=1</p>
<p>gives a fragment of HTML, an OL and the first LI in that has an A with an href of the changeset I want, which I can then plug into the API.</p>
<p>Is there a better way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-username" rel="tag" title="see questions tagged &#39;username&#39;">username</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '14, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/fca38d0c86bee980c1649b7b94ae5090?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davidearl&#39;s gravatar image" />
<p><span>davidearl</span><br />
<span class="score" title="181 reputation points">181</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davidearl has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38061" class="comments-container">
&#10;</div>
<div id="comment-tools-38061" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38061-form-container" class="comment-form-container">
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

<span id="38062"></span>

<div id="answer-container-38062" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38062-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-38062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="davidearl has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should check the API 0.6 <code>changesets</code> method call: <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Query:_GET_.2Fapi.2F0.6.2Fchangesets">Link</a>. It comes with all the details you're looking for.</p>
<pre><code>https://api.openstreetmap.org/api/0.6/changesets?user=3582
https://api.openstreetmap.org/api/0.6/changesets?display_name=davidearl</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '14, 21:55</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Oct '14, 21:57</strong> </span></p>
</div>
</div>
<div id="comments-container-38062" class="comments-container">
<span id="38063"></span>
<div id="comment-38063" class="comment">
<div id="post-38063-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you, I completely missed that in the documentation</p>
</div>
<div id="comment-38063-info" class="comment-info">
<span class="comment-age">(28 Oct '14, 22:18)</span> <span class="comment-user userinfo">davidearl</span>
</div>
</div>
</div>
<div id="comment-tools-38062" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38062-form-container" class="comment-form-container">
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

