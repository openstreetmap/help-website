+++
type = "question"
title = "how to get way OSM ID lat, lon from postgresql database?"
description = '''Hi I extracted and have written a postgresql database using the following tool. https://imposm.org/docs/imposm3/latest/ I want to extract lat, lon of the way points of a given way OSM ID using psql command. How can I do this ? Thanks.'''
date = "2019-01-21T04:03:00Z"
lastmod = "2020-07-15T17:10:00Z"
weight = 67652
keywords = [ "psql", "imposm", "postgresql", "postgres" ]
aliases = [ "/questions/67652" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to get way OSM ID lat, lon from postgresql database?](/questions/67652/how-to-get-way-osm-id-lat-lon-from-postgresql-database)

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
<span id="post-67652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67652-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I extracted and have written a postgresql database using the following tool. <a href="https://imposm.org/docs/imposm3/latest/">https://imposm.org/docs/imposm3/latest/</a></p>
<p>I want to extract lat, lon of the way points of a given way OSM ID using psql command. How can I do this ?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-psql" rel="tag" title="see questions tagged &#39;psql&#39;">psql</span> <span class="post-tag tag-link-imposm" rel="tag" title="see questions tagged &#39;imposm&#39;">imposm</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '19, 04:03</strong></p>
<img src="https://secure.gravatar.com/avatar/6e2121d6c9e20a3805619795e5640f56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mkandula&#39;s gravatar image" />
<p><span>mkandula</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mkandula has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67652" class="comments-container">
&#10;</div>
<div id="comment-tools-67652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67652-form-container" class="comment-form-container">
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

<span id="67654"></span>

<div id="answer-container-67654" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67654-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Imposm is optimized for rendering OSM data, and is not really suitable for a more general purpose spatial database, most people will use osm2pgsql for that.</p>
<p>In particular imposm will create separate tables for each mapping that you have defined, so you will need to see what table the objects you are interested were mapped to query that for the geometry column by osm_id and then step through the linestring to retrieve the individual coordinate pairs (both imposm and osm2pgsql schemas don't have a direct way to access individual, untagged way nodes once the data has been imported with SQL).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '19, 07:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-67654" class="comments-container">
&#10;</div>
<div id="comment-tools-67654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67654-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75708"></span>

<div id="answer-container-75708" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75708-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-75708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>for those who ask for : lon, lat from planet_osm_nodes, here is your response : "select lon::numeric/10000000 as lon, lat::numeric/10000000 as lat from planet_osm_nodes".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '20, 05:03</strong></p>
<img src="https://secure.gravatar.com/avatar/dfa634dabd6dbf14e4eb454ff60740d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abdelkader&#39;s gravatar image" />
<p><span>Abdelkader</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abdelkader has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75708" class="comments-container">
<span id="75727"></span>
<div id="comment-75727" class="comment">
<div id="post-75727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The post was not about a database in the osm2psgl schema, so your answer is nonsense.</p>
</div>
<div id="comment-75727-info" class="comment-info">
<span class="comment-age">(15 Jul '20, 17:10)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-75708" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75708-form-container" class="comment-form-container">
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

