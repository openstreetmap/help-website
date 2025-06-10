+++
type = "question"
title = "Efficient approach to get center coordinate for ways via overpass"
description = '''I&#x27;m using overpy library to query overpass via python. I&#x27;d like to have a list of entities with a certain tags and their coordinates. For nodes this is straightforward. For closed ways (polygons) I&#x27;d just need the centroid lat/lon.  Often those aren&#x27;t stored in center_lat,center_lon, so I&#x27;m launchin...'''
date = "2017-10-10T16:53:00Z"
lastmod = "2017-10-11T09:03:00Z"
weight = 60042
keywords = [ "python", "overpass", "ways", "tags" ]
aliases = [ "/questions/60042" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Efficient approach to get center coordinate for ways via overpass](/questions/60042/efficient-approach-to-get-center-coordinate-for-ways-via-overpass)

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
<span id="post-60042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60042-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using overpy library to query overpass via python.</p>
<p>I'd like to have a list of entities with a certain tags and their coordinates. For nodes this is straightforward. For closed ways (polygons) I'd just need the centroid lat/lon.</p>
<p>Often those aren't stored in center_lat,center_lon, so I'm launching queries against the list of nodes associated to that ways entity.</p>
<p>This query, using get_nodes, leads to a lot of HTTP errors (apparently overpy requires to launch queries again to get this). So, I'm wondering if there's a more efficient route to get what I need (and in the mean time don't bother the servers so much).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Oct '17, 16:53</strong></p>
<img src="https://secure.gravatar.com/avatar/153ae13fa2d824ce81d0959eb6e761c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WouterDX&#39;s gravatar image" />
<p><span>WouterDX</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WouterDX has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60042" class="comments-container">
&#10;</div>
<div id="comment-tools-60042" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60042-form-container" class="comment-form-container">
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

<span id="60050"></span>

<div id="answer-container-60050" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60050-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>use "out center" as e.g. in this <a href="http://overpass-turbo.eu/s/sgj">query</a> which gives the center nodes of buildings.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '17, 04:07</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-60050" class="comments-container">
<span id="60053"></span>
<div id="comment-60053" class="comment">
<div id="post-60053-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Perfect, thanks.</p>
</div>
<div id="comment-60053-info" class="comment-info">
<span class="comment-age">(11 Oct '17, 09:03)</span> <span class="comment-user userinfo">WouterDX</span>
</div>
</div>
</div>
<div id="comment-tools-60050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60050-form-container" class="comment-form-container">
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

