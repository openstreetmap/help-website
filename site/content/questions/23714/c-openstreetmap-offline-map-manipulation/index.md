+++
type = "question"
title = "c# - OpenStreetMap offline map manipulation"
description = '''I&#x27;m downlading Europe maptiles from here: http://download.geofabrik.de/ , and I want to make C# app, that will be able to manipulate the maps offline, to navigate, pin locations etc. I have developed an app using online bingmaps, but I don&#x27;t know what exactly api&#x27;s or tools and which way to use em i...'''
date = "2013-06-26T02:15:00Z"
lastmod = "2013-06-27T07:56:00Z"
weight = 23714
keywords = [ "openstreetmap", "application", "offline", "c#.net" ]
aliases = [ "/questions/23714" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [c# - OpenStreetMap offline map manipulation](/questions/23714/c-openstreetmap-offline-map-manipulation)

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
<span id="post-23714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23714-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm downlading Europe maptiles from here: <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> , and I want to make C# app, that will be able to manipulate the maps offline, to navigate, pin locations etc.</p>
<p>I have developed an app using online bingmaps, but I don't know what exactly api's or tools and which way to use em in ithis case.</p>
<p>So, if you have some suggestions or tutorials, or any indication to help me to take a shortcut through reading all this messy manuals and types, it would me welcome!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-c#.net" rel="tag" title="see questions tagged &#39;c#.net&#39;">c#.net</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '13, 02:15</strong></p>
<img src="https://secure.gravatar.com/avatar/1d99114cc205e14fcb7b0c0c44cf9ba8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mapieris&#39;s gravatar image" />
<p><span>mapieris</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mapieris has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23714" class="comments-container">
<span id="23720"></span>
<div id="comment-23720" class="comment">
<div id="post-23720-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please explain what you mean by "manipulate the maps offline". Do you want to edit the map data?</p>
</div>
<div id="comment-23720-info" class="comment-info">
<span class="comment-age">(26 Jun '13, 08:48)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="23725"></span>
<div id="comment-23725" class="comment">
<div id="post-23725-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You probably aren't downloading map TILES from <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> - what you're probably downloading from there is raw .osm data (or shape files, or one of a number of other things hosted there).</p>
<p>What are you actually trying to do? What have you downloaded that you are trying to understand?</p>
</div>
<div id="comment-23725-info" class="comment-info">
<span class="comment-age">(26 Jun '13, 12:10)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="23728"></span>
<div id="comment-23728" class="comment">
<div id="post-23728-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, I'm a bit confused from trying to read all these manuals at once.</p>
<p>Yes, "someonelse" I want to download the tiles. In general to give you a picture, I wanna built something like google maps, but in an offline mode, in a c# app.</p>
<p>Is it acheivable with that technology? what should I use?</p>
</div>
<div id="comment-23728-info" class="comment-info">
<span class="comment-age">(26 Jun '13, 14:22)</span> <span class="comment-user userinfo">mapieris</span>
</div>
</div>
<span id="23729"></span>
<div id="comment-23729" class="comment not_top_scorer">
<div id="post-23729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You said you also want to do navigation. Tiles aren't sufficient for that, you also need the underlying map data.</p>
</div>
<div id="comment-23729-info" class="comment-info">
<span class="comment-age">(26 Jun '13, 14:32)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="23730"></span>
<div id="comment-23730" class="comment not_top_scorer">
<div id="post-23730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well navigation is a second need. For the time I just need to see the map, zoom in-out, add pins, find locations.</p>
</div>
<div id="comment-23730-info" class="comment-info">
<span class="comment-age">(26 Jun '13, 14:37)</span> <span class="comment-user userinfo">mapieris</span>
</div>
</div>
<span id="23731"></span>
<div id="comment-23731" class="comment">
<div id="post-23731-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In order to find a location offline you also need some kind of database, tiles are just images without any additional information.</p>
</div>
<div id="comment-23731-info" class="comment-info">
<span class="comment-age">(26 Jun '13, 15:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="23734"></span>
<div id="comment-23734" class="comment not_top_scorer">
<div id="post-23734-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes seems reasonable. You mean something like linking each photo to a certain coord. something like orthophot, or the way bingmaps is implemented. I'm just asking is there any suggested approach. I read something about offline openstreetmaps on androids.</p>
<p>Anyway I don't I don't know, if someone can give some guideline..</p>
<p>thanks</p>
</div>
<div id="comment-23734-info" class="comment-info">
<span class="comment-age">(26 Jun '13, 20:15)</span> <span class="comment-user userinfo">mapieris</span>
</div>
</div>
<span id="23735"></span>
<div id="comment-23735" class="comment">
<div id="post-23735-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, I meant a real database capable of geocoding, like <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a> does. And the wiki is full of lists of <a href="https://wiki.openstreetmap.org/wiki/Routing/offline_routers">offline routers</a>, <a href="https://wiki.openstreetmap.org/wiki/Software/Desktop">Desktop</a> and <a href="https://wiki.openstreetmap.org/wiki/Android">Android software</a> using OSM, a description on <a href="https://wiki.openstreetmap.org/wiki/Downloading_data">obtaining OSM data</a> and so on, just search a little.</p>
</div>
<div id="comment-23735-info" class="comment-info">
<span class="comment-age">(26 Jun '13, 21:15)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="23737"></span>
<div id="comment-23737" class="comment not_top_scorer">
<div id="post-23737-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great! That's what I meant. thanks! Now about the tiles, I can download them but how can link them with the osm data so I can have offline mapping? Is that kind of easily achievable (standard methods etc) or is it a project on it self?</p>
<p>I'm aware of quadkeys since I used to use bing, is there any spec for openstreet tile system? Is there any API I can use, a control for c# etc or I have to make my own.</p>
</div>
<div id="comment-23737-info" class="comment-info">
<span class="comment-age">(26 Jun '13, 22:58)</span> <span class="comment-user userinfo">mapieris</span>
</div>
</div>
</div>
<div id="comment-tools-23714" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-23714-form-container" class="comment-form-container">
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

<span id="23744"></span>

<div id="answer-container-23744" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23744-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-23744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In one of the comments you write that you want to build "something like google maps, but in an offline mode". This would indicate you're looking for routing ("show me directions from A to B"), geocoding ("where is 1234 Somestreet, Sometown"), as well as a zoomable/pannable map (can be made from raster tiles or vector data) and possibly even a feature where people can place markers and other stuff on that map.</p>
<p>Tiles are only a very small part of this solution. To produce tiles you will need to install a tile server, likely osm2pgsql/Mapnik based; because if you download a large amount of tiles from anywhere you will be blocked for abuse. In addition to tiles you will need a local database that allows you to compute routing instructions and find locations. These are all different things that require different software. There's a lot of stuff out there already, many of which is Open Source, but it will cost you considerable time to find the bits that you could reuse in your C# application.</p>
<p>If you were hoping for some kind of ready-made library that gives you all these functions - there is none.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '13, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-23744" class="comments-container">
&#10;</div>
<div id="comment-tools-23744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23744-form-container" class="comment-form-container">
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

