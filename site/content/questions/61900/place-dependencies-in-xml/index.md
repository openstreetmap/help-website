+++
type = "question"
title = "Place dependencies in XML"
description = '''I&#x27;m new to OSM. I downloaded an OSM Data Extract in XML format. Now I want to parse it in order to extract all the places (regions, cities, towns, villages, suburbs. neighborhoods etc). Is there any chance to see dependencies between places? E.g. if there is a suburb, how can I see that it is a part...'''
date = "2018-01-30T13:18:00Z"
lastmod = "2018-01-30T13:45:00Z"
weight = 61900
keywords = [ "xml", "dependency", "extract", "osm" ]
aliases = [ "/questions/61900" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Place dependencies in XML](/questions/61900/place-dependencies-in-xml)

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
<span id="post-61900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61900-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM. I downloaded an OSM Data Extract in XML format. Now I want to parse it in order to extract all the places (regions, cities, towns, villages, suburbs. neighborhoods etc). Is there any chance to see dependencies between places? E.g. if there is a suburb, how can I see that it is a part of a city which is a part of a region which is a part of a country etc?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-dependency" rel="tag" title="see questions tagged &#39;dependency&#39;">dependency</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '18, 13:18</strong></p>
<img src="https://secure.gravatar.com/avatar/2f68295f95c66d405053a740cf95e31d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="siffash&#39;s gravatar image" />
<p><span>siffash</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="siffash has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61900" class="comments-container">
&#10;</div>
<div id="comment-tools-61900" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61900-form-container" class="comment-form-container">
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

<span id="61902"></span>

<div id="answer-container-61902" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61902-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-61902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="siffash has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM is a spatial dataset and the dependencies/hierarchies you are looking for are expressed by the objects being spatially "inside" each other, so a state boundary would be inside the countries boundary, a municipalities boundary inside the state boundary and so on.</p>
<p>That's the theory.</p>
<p>In real life we don't have boundaries for all such entities and in the case of non-administrative-entity places we currently don't even have an accepted modelling for areas (they will typically be represented by nodes in the absence of boundaries). And just how complete the existing data is will depend very much on what countries and regions you are looking at.</p>
<p>The other bad news is that in the OSM data model the geometry information is carried by the Node objects and "raw" OSM data doesn't contain pre-built geometries for polygons and multi-polygons that would represent the boundaries.</p>
<p>The simplest ways to get the boundary geometries and to be able to query the data spatially is to either use an <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">OverPass API/OverPass Turbo</a> server or run your own <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a> database. There are a number of libraries that will parse OSM data for you and create geometries if you want to do this on foot, most notably <a href="http://osmcode.org/">Osmium</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '18, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jan '18, 13:59</strong> </span></p>
</div>
</div>
<div id="comments-container-61902" class="comments-container">
&#10;</div>
<div id="comment-tools-61902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61902-form-container" class="comment-form-container">
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

