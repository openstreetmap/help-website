+++
type = "question"
title = "How to query all changesets by a user since eternity?"
description = '''The main api only returns 100 changesets, but the user has more than that, how can all of their changeset be queried?'''
date = "2013-06-07T07:47:00Z"
lastmod = "2020-11-02T21:47:00Z"
weight = 23089
keywords = [ "changeset", "api", "user" ]
aliases = [ "/questions/23089" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to query all changesets by a user since eternity?](/questions/23089/how-to-query-all-changesets-by-a-user-since-eternity)

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
<span id="post-23089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23089-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-23089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The main api only returns 100 changesets, but the user has more than that, how can all of their changeset be queried?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-user" rel="tag" title="see questions tagged &#39;user&#39;">user</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '13, 07:47</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-23089" class="comments-container">
&#10;</div>
<div id="comment-tools-23089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23089-form-container" class="comment-form-container">
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

<span id="23090"></span>

<div id="answer-container-23090" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23090-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-23090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You would have to get them 100 at a time. For example</p>
<p><a href="http://api.openstreetmap.org/api/0.6/changesets?display_name=EdLoach">http://api.openstreetmap.org/api/0.6/changesets?display_name=EdLoach</a></p>
<p>returns my most recent 100 changesets. My 100th changeset (as I type) shows created_at="2013-04-19T09:29:30Z" So, my next 100 older changesets can be queried by:</p>
<p><a href="http://api.openstreetmap.org/api/0.6/changesets?display_name=EdLoach&amp;time=2001-01-01,2013-04-19T09:29:30Z">http://api.openstreetmap.org/api/0.6/changesets?display_name=EdLoach&amp;time=2001-01-01,2013-04-19T09:29:30Z</a></p>
<p>where the first time is "closed after" and the second time is "created before", so I picked an arbitrary "closed after" date before the project began. So to get the next 100 older changesets each time, use the created_by time from the last changeset returned from the previous query as the "created before" time for the next one. At some point you will either get fewer than 100 changesets returned, or an <a href="http://api.openstreetmap.org/api/0.6/changesets?display_name=EdLoach&amp;time=2006-01-01,2006-04-19T09:29:30Z">empty result (example here based on a "created before" date set before I began mapping)</a> if a user has an exact multiple of 100 changesets.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '13, 08:43</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-23090" class="comments-container">
<span id="23093"></span>
<div id="comment-23093" class="comment">
<div id="post-23093-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>But see the <a href="http://wiki.openstreetmap.org/wiki/API_usage_policy">http://wiki.openstreetmap.org/wiki/API_usage_policy</a> and don't do this for many users.</p>
</div>
<div id="comment-23093-info" class="comment-info">
<span class="comment-age">(07 Jun '13, 10:02)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="77365"></span>
<div id="comment-77365" class="comment">
<div id="post-77365-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wrote a script to query this API to obtain all changesets for a user <a href="https://github.com/andrewharvey/osm-get-user-changeset-metadata">https://github.com/andrewharvey/osm-get-user-changeset-metadata</a></p>
</div>
<div id="comment-77365-info" class="comment-info">
<span class="comment-age">(02 Nov '20, 21:47)</span> <span class="comment-user userinfo">aharvey</span>
</div>
</div>
</div>
<div id="comment-tools-23090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23090-form-container" class="comment-form-container">
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

