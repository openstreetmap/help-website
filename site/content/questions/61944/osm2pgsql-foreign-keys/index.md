+++
type = "question"
title = "osm2pgsql foreign keys"
description = '''I am building an application for a customer in which they will type the name of a place (i.e. the name column on planet_osm_polygon of a osm2pgsql imported database) and get a boundary. I was successful in setting up the system, and I&#x27;ve been able to optimize the planet_osm_polygon table for trigram...'''
date = "2018-02-03T15:09:00Z"
lastmod = "2018-02-04T17:40:00Z"
weight = 61944
keywords = [ "relation", "postgresql", "osm2pgsql", "postgis" ]
aliases = [ "/questions/61944" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql foreign keys](/questions/61944/osm2pgsql-foreign-keys)

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
<span id="post-61944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61944-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am building an application for a customer in which they will type the name of a place (i.e. the name column on planet_osm_polygon of a osm2pgsql imported database) and get a boundary. I was successful in setting up the system, and I've been able to optimize the planet_osm_polygon table for trigram searching (with pg_trgm). The system now works -- awesome!</p>
<p>However, I'd like to "join" the tags column from the planet_osm_rels table by the osm_id provided in results from planet_osm_polygon. I understand that osm2pgsql does not provide any foreign key constraints. With that said, I'd like to know:</p>
<p>If it possible for me to add this foreign key relationship myself?</p>
<p>Any recommendations for re-approaching the problem are welcome.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Feb '18, 15:09</strong></p>
<img src="https://secure.gravatar.com/avatar/03e2e09758441a64720603b8ad0bf9f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ethanhinson&#39;s gravatar image" />
<p><span>ethanhinson</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ethanhinson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61944" class="comments-container">
&#10;</div>
<div id="comment-tools-61944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61944-form-container" class="comment-form-container">
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

<span id="61950"></span>

<div id="answer-container-61950" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61950-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no reasonable way to add foreign keys to this schema.</p>
<p>The way to accomplish this is to make sure you use the --hstore-all option. This will create a new column on the polygon table (planet_osm_polygon in my case) which contains all the tags associated with that particular polygon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '18, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/03e2e09758441a64720603b8ad0bf9f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ethanhinson&#39;s gravatar image" />
<p><span>ethanhinson</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ethanhinson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61950" class="comments-container">
&#10;</div>
<div id="comment-tools-61950" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61950-form-container" class="comment-form-container">
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

