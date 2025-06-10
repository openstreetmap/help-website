+++
type = "question"
title = "Changeset query API not working"
description = '''Hi, I&#x27;m developing a tool to evaluate and detect changesets that are possibly vandalism or importation, but the changeset query API is almost always not working. Is there some problem with the API? Example of query I&#x27;m doing: https://api.openstreetmap.org/api/0.6/changesets/?bbox=-73.9830625,-33.868...'''
date = "2015-06-08T01:46:00Z"
lastmod = "2015-06-10T10:12:00Z"
weight = 43458
keywords = [ "development", "changeset", "api" ]
aliases = [ "/questions/43458" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Changeset query API not working](/questions/43458/changeset-query-api-not-working)

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
<span id="post-43458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43458-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm developing a tool to evaluate and detect changesets that are possibly vandalism or importation, but the changeset query API is almost always not working. Is there some problem with the API?</p>
<p>Example of query I'm doing: <a href="https://api.openstreetmap.org/api/0.6/changesets/?bbox=-73.9830625,-33.8689056,0.0,5.2842873&amp;time=20150427T000000,20150427T000400&amp;closed=true">https://api.openstreetmap.org/api/0.6/changesets/?bbox=-73.9830625,-33.8689056,0.0,5.2842873&amp;time=20150427T000000,20150427T000400&amp;closed=true</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '15, 01:46</strong></p>
<img src="https://secure.gravatar.com/avatar/6d55d23b692eda99ca0f187cedd3dc42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wille&#39;s gravatar image" />
<p><span>wille</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wille has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43458" class="comments-container">
<span id="43462"></span>
<div id="comment-43462" class="comment">
<div id="post-43462-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>How does the "not working" actually manifest itself? And isn't that bounding box a (very big) bit too large?</p>
</div>
<div id="comment-43462-info" class="comment-info">
<span class="comment-age">(08 Jun '15, 10:17)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="43471"></span>
<div id="comment-43471" class="comment">
<div id="post-43471-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Hi, Simon.</p>
<p>It's always loading, but it never returns a result. The bbox is very big, but the time interval is small.</p>
<p>I tried now with a small bbox and the query worked. I'll try to divide my bbox in small bboxes.</p>
<p>Thanks for the help!</p>
</div>
<div id="comment-43471-info" class="comment-info">
<span class="comment-age">(08 Jun '15, 17:22)</span> <span class="comment-user userinfo">wille</span>
</div>
</div>
</div>
<div id="comment-tools-43458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43458-form-container" class="comment-form-container">
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

<span id="43513"></span>

<div id="answer-container-43513" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43513-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>wille I suspect you are going about your project"the wrong way" You should probably be consuming the changeset replication feed <a href="http://planet.openstreetmap.org/replication/changesets/">http://planet.openstreetmap.org/replication/changesets/</a> and processing that as it comes in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '15, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-43513" class="comments-container">
&#10;</div>
<div id="comment-tools-43513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43513-form-container" class="comment-form-container">
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

