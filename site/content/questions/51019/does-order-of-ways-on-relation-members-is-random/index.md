+++
type = "question"
title = "Does order of ways on relation members is random?"
description = '''I try to create multipolygon describing border of Poland to test if some building are in this administration area. I took data from db (I imported OSM data to local db first preserving order of ways and nodes during the import). What I see is some ways in relation definition (members) are not on pro...'''
date = "2016-07-21T12:20:00Z"
lastmod = "2021-07-17T11:30:00Z"
weight = 51019
keywords = [ "ways", "import", "extract" ]
aliases = [ "/questions/51019" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Does order of ways on relation members is random?](/questions/51019/does-order-of-ways-on-relation-members-is-random)

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
<span id="post-51019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51019-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I try to create multipolygon describing border of Poland to test if some building are in this administration area. I took data from db (I imported OSM data to local db first preserving order of ways and nodes during the import). What I see is some ways in relation definition (members) are not on proper position.<br />
More info is <a href="http://gis.stackexchange.com/questions/202936/order-of-ways-in-openstreetmap-relation-data-relation-members" title="Ways">here</a>. I can't load images to this post because of insufficient reputation points...</p>
<p>The question is: should I reorder ways on relation data or it's an issue with Geofabrik data export and look for other source of OSM data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '16, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/9d6cd718cdeb41535fa4aa16477eeeb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stalek&#39;s gravatar image" />
<p><span>stalek</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stalek has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-51019" class="comments-container">
&#10;</div>
<div id="comment-tools-51019" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51019-form-container" class="comment-form-container">
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

<span id="51021"></span>

<div id="answer-container-51021" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51021-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="stalek has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do not write your own multipolygon building code. You are re-inventing the wheel. Re-use the code that already exists in osm2pgsql (PostGIS importer), libosmium (C++ processing library with Python bindings), or GDAL (has an OSM input driver and can write various output formats) instead!</p>
<p>OSM does not require that relation members be stored in the right order; this is something the software must do.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '16, 12:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-51021" class="comments-container">
<span id="51022"></span>
<div id="comment-51022" class="comment">
<div id="post-51022-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In addition, even if you were to make sure that all objects in a relation (such as a route relation) were "in order", as soon as someone edits that relation (e.g. to split a way) the objects will be "out of order" again.</p>
</div>
<div id="comment-51022-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 12:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="51031"></span>
<div id="comment-51031" class="comment">
<div id="post-51031-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't plan to draw any shapes. I have to test if some coordinates belong to some administration hierarchy (country, region, county and so on). To do it I have to create the shape of boundary to test if any point/location is withing such shape. I will take a look if PostGIS importer creates such shapes during the import (as mentioned by you). It's not a rocket science to reorder ways when I know they are in random order. btw: I use SqlServer and its spatial support to speed up things during the processing and I don't load any data to any external applications to not slow it down (it's not necessary in reality, because every complex operation on such data is easy to implement using T-SQL). It's like using many "db engine cursors" in case of external apps versus raw performance of group of queries optimized by DB engine :)</p>
<p>Thanks for the info :)</p>
</div>
<div id="comment-51031-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 13:41)</span> <span class="comment-user userinfo">stalek</span>
</div>
</div>
<span id="51034"></span>
<div id="comment-51034" class="comment">
<div id="post-51034-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>After reordering of a few ways/lines I received proper shape already, so the info from Frederik helped :)</p>
<p><img src="/upfiles/Poland_Border.png" alt="alt text" /></p>
<p>Thanks.</p>
</div>
<div id="comment-51034-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 14:20)</span> <span class="comment-user userinfo">stalek</span>
</div>
</div>
<span id="80964"></span>
<div id="comment-80964" class="comment not_top_scorer">
<div id="post-80964-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"This is something the software must do"</p>
<p>But how must the software do it? It seems that the order of the ways in the relation/members field is still not correct, from time to time it gives me discontinuous graphs. I read everywhere that ways do not need to be sorted, and sure, I can plot 16 lines separately to make a trail, but what if I want to offer a relation as a GPX file? Those need to be sorted, right?</p>
<p>Maybe the question is: Is the proper way to sort the nodes in a relation anywhere in the relation object? If so, where is it? Or do I need to write some code to find the closed "first node of a way" to the other "last node of a way" and sort based on that? Is that what the software must do?</p>
<p>Some more info on what I'm trying to do: <a href="https://stackoverflow.com/questions/68375034/plotting-openstreetmap-relations-does-not-generate-continous-lines">https://stackoverflow.com/questions/68375034/plotting-openstreetmap-relations-does-not-generate-continous-lines</a></p>
</div>
<div id="comment-80964-info" class="comment-info">
<span class="comment-age">(14 Jul '21, 13:50)</span> <span class="comment-user userinfo">FreekvH</span>
</div>
</div>
<span id="80968"></span>
<div id="comment-80968" class="comment not_top_scorer">
<div id="post-80968-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Reading your stackoverflow post, I am not sure if you are distinguishing between ordering the member ways, and ordering the nodes within each way.</p>
<p>E.g. suppose a relation runs from east to west and all members are correctly sorted from east to west. Within any given member way, the nodes might happen to run from east to west or west to east, as ways (unless they are one way streets) have an arbitrary direction. So if you are trying to order nodes within a member way you need to pick the right one of the two possible directions. That information is not contained in the relation itself. (Apologies if you already know all this).</p>
</div>
<div id="comment-80968-info" class="comment-info">
<span class="comment-age">(14 Jul '21, 15:34)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="80969"></span>
<div id="comment-80969" class="comment">
<div id="post-80969-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Other things to bear in mind</p>
<ul>
<li><p>There may be nodes or ways with specific roles, e.g. guidepost, that you probably would not want to try to sort.</p></li>
<li><p>Recreational trails in the real world are not always "sortable", there may be spurs, alternate routes etc. Recently there has been a trend to try to identify these with roles within relations (<a href="https://wiki.openstreetmap.org/wiki/Proposed_features/hiking_trail_relation_roles),">https://wiki.openstreetmap.org/wiki/Proposed_features/hiking_trail_relation_roles),</a> but you can't rely on that being the case.</p></li>
<li><p>While recreational routes ideally should be sorted by mappers who input them to OSM, not everybody does this, and there is nothing in the editors that forces them to do so. Even if a route is sorted initially, the sorting can get broken quite easily for large relations, often by mappers editing member ways for reasons unrelated to the route relation. I often find hiking relations I have carefully sorted in the past have been "unsorted" by subsequent edits.</p></li>
</ul>
</div>
<div id="comment-80969-info" class="comment-info">
<span class="comment-age">(14 Jul '21, 15:34)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="81002"></span>
<div id="comment-81002" class="comment not_top_scorer">
<div id="post-81002-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok,thanx, clear, the data model is just what it is. I do wonder how GPX trails are generated by some websites then. They probably do some math to sort based on last/first coordinates of trails.</p>
</div>
<div id="comment-81002-info" class="comment-info">
<span class="comment-age">(16 Jul '21, 15:30)</span> <span class="comment-user userinfo">FreekvH</span>
</div>
</div>
<span id="81003"></span>
<div id="comment-81003" class="comment not_top_scorer">
<div id="post-81003-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you look at the output that some tools like <a href="http://ra.osmsurround.org/index">http://ra.osmsurround.org/index</a> generate, you can see how it's arranging various pieces of relations.</p>
</div>
<div id="comment-81003-info" class="comment-info">
<span class="comment-age">(16 Jul '21, 15:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="81016"></span>
<div id="comment-81016" class="comment">
<div id="post-81016-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you have the constituent geometries in a PostGIS database as linestrings, then ST_LineMerge can usually do a pretty good job of piecing them together to make continuous lines. <a href="https://postgis.net/docs/ST_LineMerge.html">https://postgis.net/docs/ST_LineMerge.html</a></p>
</div>
<div id="comment-81016-info" class="comment-info">
<span class="comment-age">(17 Jul '21, 11:30)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51021" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-51021-form-container" class="comment-form-container">
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

