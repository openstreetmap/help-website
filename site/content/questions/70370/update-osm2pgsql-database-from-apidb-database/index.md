+++
type = "question"
title = "Update osm2pgsql database from apidb database"
description = '''Suppose we have two databases:  With osm2pgsql schema. With apidb schema.  Updating osm2pgsql data from apidb is quite simple, by using --replicate-apidb command, which is provided by osmosis. Do we have the opposite way to update apidb data from osm2pgsql database?'''
date = "2019-08-13T15:39:00Z"
lastmod = "2019-08-14T11:02:00Z"
weight = 70370
keywords = [ "apidb", "osm2pgsql", "osmosis" ]
aliases = [ "/questions/70370" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Update osm2pgsql database from apidb database](/questions/70370/update-osm2pgsql-database-from-apidb-database)

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
<span id="post-70370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70370-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Suppose we have two databases:</p>
<ol>
<li>With <a href="https://wiki.openstreetmap.org/wiki/Databases_and_data_access_APIs#Osm2pgsql">osm2pgsql schema</a>.</li>
<li>With <a href="https://wiki.openstreetmap.org/wiki/Databases_and_data_access_APIs#apidb">apidb schema</a>.</li>
</ol>
<p>Updating <code>osm2pgsql</code> data from <code>apidb</code> is quite simple, by using <code>--replicate-apidb</code> command, which is provided by <code>osmosis</code>.</p>
<p>Do we have the opposite way to update <code>apidb</code> data from <code>osm2pgsql</code> database?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apidb" rel="tag" title="see questions tagged &#39;apidb&#39;">apidb</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '19, 15:39</strong></p>
<img src="https://secure.gravatar.com/avatar/d77b49acd7cf6026b0c5bf860ee111c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YUNtee&#39;s gravatar image" />
<p><span>YUNtee</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YUNtee has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70370" class="comments-container">
&#10;</div>
<div id="comment-tools-70370" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70370-form-container" class="comment-form-container">
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

<span id="70371"></span>

<div id="answer-container-70371" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70371-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="YUNtee has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, it is not possible because information is lost when importing data into an osm2pgsql database. For example, it does not keep version numbers, user IDs, or timestamps, and might drop some objects altogether when they are deemed unnecessary for rendering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '19, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70371" class="comments-container">
<span id="70375"></span>
<div id="comment-70375" class="comment">
<div id="post-70375-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thanks for the answer!</p>
</div>
<div id="comment-70375-info" class="comment-info">
<span class="comment-age">(14 Aug '19, 11:02)</span> <span class="comment-user userinfo">YUNtee</span>
</div>
</div>
</div>
<div id="comment-tools-70371" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70371-form-container" class="comment-form-container">
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

