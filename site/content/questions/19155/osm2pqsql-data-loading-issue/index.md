+++
type = "question"
title = "osm2pqsql data loading issue"
description = '''Hi All, I&#x27;ve tried to load planet-latest.osm.bz2 to postgresql DB using osm2pgsql tool. After unexpectable loading process interruption I reran osm2pgsql with --append flag, but got the following error: Using projection SRS 900913 (Spherical Mercator) Setting up table: planet_osm_point Problem readi...'''
date = "2013-01-17T11:04:00Z"
lastmod = "2013-01-21T15:57:00Z"
weight = 19155
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/19155" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pqsql data loading issue](/questions/19155/osm2pqsql-data-loading-issue)

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
<span id="post-19155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19155-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I've tried to load planet-latest.osm.bz2 to postgresql DB using osm2pgsql tool. After unexpectable loading process interruption I reran osm2pgsql with --append flag, but got the following error:</p>
<p>Using projection SRS 900913 (Spherical Mercator) Setting up table: planet_osm_point Problem reading geometry information for table planet_osm_point - does it exist? Error occurred, cleaning up</p>
<p>Is there any way to continue loading process without data base rewriting?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '13, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/23c04d8569cab5c5dbc443ea3a2c837e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jurasv&#39;s gravatar image" />
<p><span>jurasv</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jurasv has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19155" class="comments-container">
&#10;</div>
<div id="comment-tools-19155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19155-form-container" class="comment-form-container">
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

<span id="19162"></span>

<div id="answer-container-19162" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19162-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Is it possible that there's a permission problem? Can you log in to the database with the same database user ID you instructed Osmosis to use and then do</p>
<pre><code>select * from geometry_columns;</code></pre>
<p>or does that result in an error message?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '13, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-19162" class="comments-container">
<span id="19235"></span>
<div id="comment-19235" class="comment">
<div id="post-19235-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My OSM planet database owner is postgres. I logged in to the DB with postgres user ID and ran sql script you sent me. The geometry_columns table is empty. Table planet_osm_point doesn't exist in the DB.</p>
</div>
<div id="comment-19235-info" class="comment-info">
<span class="comment-age">(21 Jan '13, 14:17)</span> <span class="comment-user userinfo">jurasv</span>
</div>
</div>
</div>
<div id="comment-tools-19162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19162-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19236"></span>

<div id="answer-container-19236" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19236-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Osm2pgsql uses transactions in the initial phase of data loading. If during that phase an error occurs and osm2pgsql fails, postgresql rolls back the transaction entirely, leaving no trace of the failed import in the database.</p>
<p>Only once you reach the indexing phase is it possible (or desirable performance wise) to continue a failed import, although only by manually running all the steps osm2pgsql would run for you. In all other cases you have to or are better off starting the import from scratch.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '13, 15:57</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-19236" class="comments-container">
&#10;</div>
<div id="comment-tools-19236" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19236-form-container" class="comment-form-container">
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

