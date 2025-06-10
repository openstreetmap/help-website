+++
type = "question"
title = "Retrieve the osm_id (from Postgres DB) if I have LAT/LON"
description = '''I see that you can use nominatim with an HTTP POST for this. However, I went to the trouble of loading the OSM database into postgres, and I want to take advantage of the speed of querying it from my DB, without an HTTP call. Is there a SQL QUERY that can get the osm_ids associated with a specific l...'''
date = "2012-11-14T02:22:00Z"
lastmod = "2014-03-13T10:01:00Z"
weight = 17701
keywords = [ "latitude", "longitude", "osm_id" ]
aliases = [ "/questions/17701" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Retrieve the osm_id (from Postgres DB) if I have LAT/LON](/questions/17701/retrieve-the-osm_id-from-postgres-db-if-i-have-latlon)

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
<span id="post-17701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17701-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I see that you can use nominatim with an HTTP POST for this. However, I went to the trouble of loading the OSM database into postgres, and I want to take advantage of the speed of querying it from my DB, without an HTTP call.</p>
<p>Is there a <strong><em>SQL QUERY</em></strong> that can get the osm_ids associated with a specific latitude/longitude??</p>
<p>Thanks so much. Ive spend dozens of hours trying to figure this out!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-osm_id" rel="tag" title="see questions tagged &#39;osm_id&#39;">osm_id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '12, 02:22</strong></p>
<img src="https://secure.gravatar.com/avatar/336410459670c2fd0ea1fcf4d89e2829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sfrattura&#39;s gravatar image" />
<p><span>sfrattura</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sfrattura has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17701" class="comments-container">
&#10;</div>
<div id="comment-tools-17701" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17701-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="17704"></span>

<div id="answer-container-17704" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17704-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This depends on how you have imported the data. For an osm2pgsql import, the query would look like this:</p>
<pre><code>SELECT 
   osm_id
FROM
   planet_osm_point (or _line, or _polygon)
WHERE
   ST_DWITHIN(mypoint, way, mydistance);</code></pre>
<p>What you put for <code>mypoint</code> and <code>mydistance</code> depends on what projection your data is in; if you have imported without <code>-l</code>, i.e. your data is in spherical mercator, you would have to put something like</p>
<pre><code>ST_TRANSFORM(ST_SETSRID(ST_MAKEPOINT(mylon, mylat), 4326), 900913)</code></pre>
<p>and for <code>mydistance</code> you would put the distance in spherical mercator units, i.e. roughly metres.</p>
<p>The query will then return all IDs within the given distance of the point.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '12, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17704" class="comments-container">
&#10;</div>
<div id="comment-tools-17704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17704-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31524"></span>

<div id="answer-container-31524" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31524-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have a simliar problem trying to show some localities only having the lat long data availabe. Can you point me to a different resolution for this problem. I'm using mapserver on windows and openlayers. Thank you</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '14, 09:18</strong></p>
<img src="https://secure.gravatar.com/avatar/f8d3dff42a0bc474dd9095b69606324c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Victor1989&#39;s gravatar image" />
<p><span>Victor1989</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Victor1989 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31524" class="comments-container">
<span id="31526"></span>
<div id="comment-31526" class="comment">
<div id="post-31526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is a completely different question, and you'd be better off asking it as a separate question, fully explaining what you want to do and what your setup is.</p>
</div>
<div id="comment-31526-info" class="comment-info">
<span class="comment-age">(13 Mar '14, 10:01)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31524-form-container" class="comment-form-container">
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

