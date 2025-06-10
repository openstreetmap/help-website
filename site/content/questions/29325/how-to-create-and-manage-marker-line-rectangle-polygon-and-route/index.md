+++
type = "question"
title = "How to create and manage marker, Line, Rectangle, Polygon and route."
description = '''I am new to maps. I am playing to use the OpenStreetMap API. I want to consume this API in my asp.net web applications. I want to implement below features using OpenStreetMap API.  Create and Delete marker on map. Region Creation/Editing like Line, Rectangle, Polygon ect Create route between two or ...'''
date = "2013-12-24T11:27:00Z"
lastmod = "2014-06-07T09:44:00Z"
weight = 29325
keywords = [ "marker", "draw", "api", "polygons" ]
aliases = [ "/questions/29325" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to create and manage marker, Line, Rectangle, Polygon and route.](/questions/29325/how-to-create-and-manage-marker-line-rectangle-polygon-and-route)

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
<span id="post-29325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29325-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to maps. I am playing to use the OpenStreetMap API. I want to consume this API in my asp.net web applications. I want to implement below features using OpenStreetMap API.</p>
<ol>
<li>Create and Delete marker on map.</li>
<li>Region Creation/Editing like Line, Rectangle, Polygon ect</li>
<li>Create route between two or more points.</li>
</ol>
<p>Can any one help me how to achieve these by using OpenStreetMap API</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-draw" rel="tag" title="see questions tagged &#39;draw&#39;">draw</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Dec '13, 11:27</strong></p>
<img src="https://secure.gravatar.com/avatar/1af29e2693dbfba29fb5e79cf60fd93e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="allemahesh&#39;s gravatar image" />
<p><span>allemahesh</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="allemahesh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Dec '13, 12:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span></p>
</div>
</div>
<div id="comments-container-29325" class="comments-container">
&#10;</div>
<div id="comment-tools-29325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29325-form-container" class="comment-form-container">
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

<span id="29329"></span>

<div id="answer-container-29329" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29329-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-29329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://wiki.openstreetmap.org/wiki/API_v0.6">The osm API</a> does not have that kind of features. Its purpose is to edit the map data, not to draw markers, polygons, etc on the map.</p>
<p>To do the later, see (amonst others) the <a href="http://leafletjs.com/">leaflet</a> or <a href="http://www.openlayers.org/">openlayers</a> libraries. Some third-party websites such as <a href="http://umap.fluv.io/">umap</a> or <a href="http://share.mapbbcode.org/">mapbbshare</a> also do somthing very similar.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Dec '13, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-29329" class="comments-container">
<span id="29381"></span>
<div id="comment-29381" class="comment">
<div id="post-29381-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You might want to check here for additional widgets/components <a href="http://wiki.openstreetmap.org/wiki/Frameworks">http://wiki.openstreetmap.org/wiki/Frameworks</a></p>
</div>
<div id="comment-29381-info" class="comment-info">
<span class="comment-age">(27 Dec '13, 16:18)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-29329" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29329-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29330"></span>

<div id="answer-container-29330" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29330-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you're looking for a place to obtain data from prior to displaying it in an on-screen map, the OSM API probably isn't the best place (it's intended to be used for editing, not creating maps from). Instead, perhaps <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a> might be a place to look. It'll get you exactly the same data, but in a way that doesn't overload OSM's servers. You can also of course <a href="http://planet.osm.org">just download the data</a>.</p>
<p>With regard to routing, you're probably best just starting from <a href="http://wiki.openstreetmap.org/wiki/Routing">the wiki page</a>. There are offline routers available that you can deploy, and existing instances of them. If you want to do routing in-client you'll probably find some pointers there for that too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Dec '13, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-29330" class="comments-container">
&#10;</div>
<div id="comment-tools-29330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29330-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33769"></span>

<div id="answer-container-33769" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33769-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>found a new one:</p>
<p>have a look at <a href="http://geojson.io">http://geojson.io</a> and read its help text. You can draw geometries, display markers according to coordinate tables, overlay GPX or KML data, and finally share your map even privately.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '14, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-33769" class="comments-container">
&#10;</div>
<div id="comment-tools-33769" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33769-form-container" class="comment-form-container">
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

