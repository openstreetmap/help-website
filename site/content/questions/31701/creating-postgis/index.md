+++
type = "question"
title = "creating PostGIS"
description = '''How do I load OSM data into a PostGIS database.'''
date = "2014-03-19T17:00:00Z"
lastmod = "2014-09-25T00:05:00Z"
weight = 31701
keywords = [ "postgis" ]
aliases = [ "/questions/31701" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [creating PostGIS](/questions/31701/creating-postgis)

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
<span id="post-31701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31701-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I load OSM data into a PostGIS database.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '14, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/cd6f9338a5588f839cbaa01a3e21aad0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deco2208&#39;s gravatar image" />
<p><span>deco2208</span><br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deco2208 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '14, 17:01</strong> </span></p>
</div>
</div>
<div id="comments-container-31701" class="comments-container">
&#10;</div>
<div id="comment-tools-31701" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31701-form-container" class="comment-form-container">
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

<span id="31702"></span>

<div id="answer-container-31702" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31702-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">switch2osm instructions</a> should help. That was written for PostGIS 1.5, so if you're using a later version some bits will be slightly different (e.g. something like <code>"psql -d gis -c 'create extension postgis;'"</code> instead of <code>"psql -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql -d gis"</code>)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Mar '14, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-31702" class="comments-container">
<span id="31751"></span>
<div id="comment-31751" class="comment">
<div id="post-31751-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't get it. I went to the site and couldn't find how to set up PostGIS.</p>
</div>
<div id="comment-31751-info" class="comment-info">
<span class="comment-age">(21 Mar '14, 23:11)</span> <span class="comment-user userinfo">deco2208</span>
</div>
</div>
<span id="31752"></span>
<div id="comment-31752" class="comment">
<div id="post-31752-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Presumably you read the bit that says "Installing postgresql / postgis"? What did you try and what did not work?</p>
</div>
<div id="comment-31752-info" class="comment-info">
<span class="comment-age">(21 Mar '14, 23:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31702" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31702-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37043"></span>

<div id="answer-container-37043" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37043-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would recommend using osm2pgsql. <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">See the page on the OSM wiki</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '14, 00:05</strong></p>
<img src="https://secure.gravatar.com/avatar/7c03aedcc479035905415829caf6dd7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mpmckenna8&#39;s gravatar image" />
<p><span>mpmckenna8</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mpmckenna8 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37043" class="comments-container">
&#10;</div>
<div id="comment-tools-37043" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37043-form-container" class="comment-form-container">
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

