+++
type = "question"
title = "Example POSTGRES queries for OSM"
description = '''Hello, I recently installed postgres and loaded some osm data in it. I&#x27;m trying to do some queries (for example getting all street names, street numbers, etc ..). Can anyone help me with some documentation about postgres query with osm ? i&#x27;m looking for any tutorial able to get me started on how to ...'''
date = "2012-03-10T17:53:00Z"
lastmod = "2012-03-16T22:58:00Z"
weight = 11102
keywords = [ "openstreetmap", "query", "postgresql" ]
aliases = [ "/questions/11102" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Example POSTGRES queries for OSM](/questions/11102/example-postgres-queries-for-osm)

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
<span id="post-11102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11102-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-11102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I recently installed postgres and loaded some osm data in it. I'm trying to do some queries (for example getting all street names, street numbers, etc ..). Can anyone help me with some documentation about postgres query with osm ? i'm looking for any tutorial able to get me started on how to query the database</p>
<p>Thanks for you help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '12, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/4278fe3108aabc288262dfe7aae8e377?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hyboga&#39;s gravatar image" />
<p><span>Hyboga</span><br />
<span class="score" title="45 reputation points">45</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hyboga has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11102" class="comments-container">
<span id="11107"></span>
<div id="comment-11107" class="comment">
<div id="post-11107-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are many different ways to load osm data into a postgres database all depending on how you want to get the data out again. Can you tell us how you imported the data and possibly what you want with the database in the end.</p>
</div>
<div id="comment-11107-info" class="comment-info">
<span class="comment-age">(10 Mar '12, 23:43)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
<span id="11121"></span>
<div id="comment-11121" class="comment">
<div id="post-11121-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Gnonthgol,</p>
<p>I loaded osm data using osm2psql, in the end i would like those data as lists (csv or else) so i can import them somewhere else.</p>
</div>
<div id="comment-11121-info" class="comment-info">
<span class="comment-age">(11 Mar '12, 13:31)</span> <span class="comment-user userinfo">Hyboga</span>
</div>
</div>
</div>
<div id="comment-tools-11102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11102-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="11264"></span>

<div id="answer-container-11264" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11264-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-11264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here is the schema of Osm2pgsql:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql/schema">https://wiki.openstreetmap.org/wiki/Osm2pgsql/schema</a></p>
<p>it contains one example and documentation of the table structure.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '12, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/ec2962c6ef6aab7940982ed25f2ca544?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheOddOne2&#39;s gravatar image" />
<p><span>TheOddOne2</span><br />
<span class="score" title="685 reputation points">685</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheOddOne2 has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-11264" class="comments-container">
&#10;</div>
<div id="comment-tools-11264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11264-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11126"></span>

<div id="answer-container-11126" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11126-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-11126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osm2pgsql stores the data in several tables according to the style you used when you imported. The geometries is stored in postgis format. For a description on how to work with the geometries read the <a href="http://www.postgis.org/documentation/manual-1.5/">postgis manual</a>. If you are unfemilear with sql there are a lot of resources out there on the internet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '12, 17:42</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11126" class="comments-container">
&#10;</div>
<div id="comment-tools-11126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11126-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11211"></span>

<div id="answer-container-11211" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11211-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-11211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can find lots of example queries in mapnik stylesheets: <a href="https://trac.openstreetmap.org/browser/applications/rendering/mapnik/osm.xml">https://trac.openstreetmap.org/browser/applications/rendering/mapnik/osm.xml</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '12, 09:25</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-11211" class="comments-container">
&#10;</div>
<div id="comment-tools-11211" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11211-form-container" class="comment-form-container">
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

