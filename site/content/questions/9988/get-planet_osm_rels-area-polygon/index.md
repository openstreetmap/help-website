+++
type = "question"
title = "Get planet_osm_rels area polygon"
description = '''Hello everyone. I want to get the polygon(postgis polygon) which represents some administrative area, without using josm and etc. The main purpose is after that I can grab additional info about this polygon, for example : how many lines intersect it or how many special nodes are located in it. All t...'''
date = "2012-01-15T21:13:00Z"
lastmod = "2012-01-16T08:51:00Z"
weight = 9988
keywords = [ "query", "polygon", "postgis", "area" ]
aliases = [ "/questions/9988" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get planet_osm_rels area polygon](/questions/9988/get-planet_osm_rels-area-polygon)

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
<span id="post-9988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9988-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone.</p>
<p>I want to get the polygon(postgis polygon) which represents some administrative area, without using josm and etc. The main purpose is after that I can grab additional info about this polygon, for example : how many lines intersect it or how many special nodes are located in it. All this i want to do with postgis query's.</p>
<p>I read about planet_osm_rels table, which represents some closed areas. I found out such info:</p>
<p><em>way_off</em> Offset to first way id in parts</p>
<p><em>rel_off</em> Offset to first relation id in parts</p>
<p><em>parts</em> List of node IDs, way IDs and relation IDs in this relation.</p>
<p><em>members</em> Array of members and roles, format: {member1, role1, member2, role2, ...}. Members are represented by a letter denoting their type plus their ID</p>
<p>I expected something like polygon but failed. So what columns should i use to build up needed polygon in postgis ( It will be really fine to understand also how to make it)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jan '12, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/04a50c0f1ba0dbf4a36e948646b8f47d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zzzzteph&#39;s gravatar image" />
<p><span>zzzzteph</span><br />
<span class="score" title="30 reputation points">30</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zzzzteph has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9988" class="comments-container">
&#10;</div>
<div id="comment-tools-9988" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9988-form-container" class="comment-form-container">
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

<span id="9989"></span>

<div id="answer-container-9989" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9989-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zzzzteph has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will have it much, much easier if you can find your polygon in the planet_osm_polygon table (look for something with boundary=administrative, admin_level=..). There you already have a finished PostGIS geometry.</p>
<p>The difference is that planet_osm_rels will contain your relation even if it is broken or does not make a proper polygon for another reason.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '12, 21:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9989" class="comments-container">
<span id="9991"></span>
<div id="comment-9991" class="comment">
<div id="post-9991-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh thanks! I didn't look in this table. It has all what I needed.</p>
</div>
<div id="comment-9991-info" class="comment-info">
<span class="comment-age">(15 Jan '12, 21:32)</span> <span class="comment-user userinfo">zzzzteph</span>
</div>
</div>
<span id="9992"></span>
<div id="comment-9992" class="comment">
<div id="post-9992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, and what about names ? I've got with query sometimes about 5 or 10 same area name with same osm_id. How can I manage with this problem ?</p>
</div>
<div id="comment-9992-info" class="comment-info">
<span class="comment-age">(15 Jan '12, 21:42)</span> <span class="comment-user userinfo">zzzzteph</span>
</div>
</div>
<span id="9994"></span>
<div id="comment-9994" class="comment">
<div id="post-9994-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the ID is negative then these are polygons created from a single multipolygon or boundary relation. This happens e.g. if you have a country with tons of islands and people have drawn a national boundary around each or something. You can of course collect them into a proper MULTIPOLYGON geometry in PostGIS, or you can try to select the largest, depending on what you want to do with it.</p>
</div>
<div id="comment-9994-info" class="comment-info">
<span class="comment-age">(15 Jan '12, 21:53)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="9995"></span>
<div id="comment-9995" class="comment">
<div id="post-9995-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to select city districts , it can't be more than 1 polygon,as i think. Some areas have the same name and same negative osm_id.</p>
</div>
<div id="comment-9995-info" class="comment-info">
<span class="comment-age">(15 Jan '12, 22:02)</span> <span class="comment-user userinfo">zzzzteph</span>
</div>
</div>
<span id="9998"></span>
<div id="comment-9998" class="comment">
<div id="post-9998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And what about same districts ( I mean names ) in different cities?</p>
</div>
<div id="comment-9998-info" class="comment-info">
<span class="comment-age">(16 Jan '12, 08:51)</span> <span class="comment-user userinfo">zzzzteph</span>
</div>
</div>
</div>
<div id="comment-tools-9989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9989-form-container" class="comment-form-container">
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

