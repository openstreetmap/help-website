+++
type = "question"
title = "Get polygon shapefile/KML for a node/location in openstreetmap"
description = '''I have about 1000 nodes/locations of interest from openstreetmap. I queried overpassturbo API to get coordinates of those 1000 locations/nodes. What I am interested in is, getting a polygon based KML/shapefile for each of those 1000 locations. So basically, let&#x27;s say I go to 1 of those 1000 location...'''
date = "2020-09-14T15:51:00Z"
lastmod = "2020-09-15T23:53:00Z"
weight = 76593
keywords = [ "openstreetmap", "overpass", "shapefile", "overpass-turbo", "kml" ]
aliases = [ "/questions/76593" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get polygon shapefile/KML for a node/location in openstreetmap](/questions/76593/get-polygon-shapefilekml-for-a-nodelocation-in-openstreetmap)

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
<span id="post-76593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76593-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have about 1000 nodes/locations of interest from openstreetmap. I queried overpassturbo API to get coordinates of those 1000 locations/nodes. What I am interested in is, getting a polygon based KML/shapefile for each of those 1000 locations. So basically, let's say I go to 1 of those 1000 locations on the map, currently I just have one location pointer for that location. But I need a whole polygon drawn for the location. For example, if it's a supermarket, I need a KML file for it such that it can show me a polygon drawn over the entire supermarket and not just a location pointer.</p>
<p>Is it possible to get that from overpassturbo API or anywhere else? Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '20, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/6b39601bea3eda27d2cbe0f1f503674f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aashay&#39;s gravatar image" />
<p><span>Aashay</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aashay has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Sep '20, 20:34</strong> </span></p>
</div>
</div>
<div id="comments-container-76593" class="comments-container">
<span id="76605"></span>
<div id="comment-76605" class="comment">
<div id="post-76605-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>post your current turbo routine.</p>
</div>
<div id="comment-76605-info" class="comment-info">
<span class="comment-age">(14 Sep '20, 19:47)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="76607"></span>
<div id="comment-76607" class="comment">
<div id="post-76607-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/1532/davef"></a><a href="https://help.openstreetmap.org/users/1532/davef">@DaveF</a></p>
<p>I am just simply querying for a few nodes of my interest from overpassturbo-api. And I get all the location pointers for my places of interest. But what I need is, a polygon of the entire place drawn for each of those location pointers. Here's a sample query im using:</p>
<p>[out:json][timeout:25]; ( node["building"="&lt;xyz&gt;"]; ); out body;</p>
</div>
<div id="comment-76607-info" class="comment-info">
<span class="comment-age">(14 Sep '20, 20:32)</span> <span class="comment-user userinfo">Aashay</span>
</div>
</div>
<span id="76608"></span>
<div id="comment-76608" class="comment">
<div id="post-76608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you want ways, why are you querying nodes?</p>
</div>
<div id="comment-76608-info" class="comment-info">
<span class="comment-age">(14 Sep '20, 21:46)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="76609"></span>
<div id="comment-76609" class="comment">
<div id="post-76609-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually, I need nodes only. Basically all I need is, let's say I have a location pointer pointing to a supermarket - I need a kml or a shape file where in there is a polygon drawn over the edges of the supermarket. Or else even an array of coordinates that run along the boundaries of the supermarket is fine. I am not sure if that is even possible with overpassturbo-api. Is there any way in which I can get this? or any alternative way to get this?</p>
</div>
<div id="comment-76609-info" class="comment-info">
<span class="comment-age">(14 Sep '20, 21:53)</span> <span class="comment-user userinfo">Aashay</span>
</div>
</div>
</div>
<div id="comment-tools-76593" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76593-form-container" class="comment-form-container">
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

<span id="76620"></span>

<div id="answer-container-76620" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76620-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Objects in OSM can be mapped as dots, as areas or as multipolygons. It's a matter of mapping preference, object complexity, available time and other factors how a mapper does it.</p>
<p>With your query you are only retrieving those buildings that have only been mapped as a single node without outline. To get all buildings you need to also query for ways and relations. As a start you can change <code>node["building"="xyz"]</code> to <code>nwr["building"="xyz"]</code>.</p>
<p>Modify your query and if you need more help please post the new query with specific questions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '20, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-76620" class="comments-container">
&#10;</div>
<div id="comment-tools-76620" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76620-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76650"></span>

<div id="answer-container-76650" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76650-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>[bbox:{{bbox}}];
wr[building=school];
out geom;</code></pre>
<p>Save as KML under Export option in Turbo</p>
<p>[bbox:{{bbox}}]; is required to limit returned data to the size of your window otherwise you'll download worldwide.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '20, 23:53</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '20, 01:17</strong> </span></p>
</div>
</div>
<div id="comments-container-76650" class="comments-container">
&#10;</div>
<div id="comment-tools-76650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76650-form-container" class="comment-form-container">
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

