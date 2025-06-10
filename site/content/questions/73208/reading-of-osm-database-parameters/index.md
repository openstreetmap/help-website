+++
type = "question"
title = "Reading of OSM database parameters"
description = '''Hi all, two days ago I asked the question entitled: &quot;Data of routes characteristics (nodes, orientation) of a pedestrian walking path&quot;. I had no answers, but only a comment, useful and I thanks, but I would like to better formulate the question. I need to know the direction (orientation towards the ...'''
date = "2020-02-23T20:51:00Z"
lastmod = "2020-02-25T00:09:00Z"
weight = 73208
keywords = [ "database", "display", "orientation", "road", "accuracy" ]
aliases = [ "/questions/73208" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Reading of OSM database parameters](/questions/73208/reading-of-osm-database-parameters)

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
<span id="post-73208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73208-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, two days ago I asked the question entitled: "Data of routes characteristics (nodes, orientation) of a pedestrian walking path". I had no answers, but only a comment, useful and I thanks, but I would like to better formulate the question. I need to know the direction (orientation towards the north) of a straight road, of which you know the street, between two known addresses (e.g. address with house number). I need to know the value with the best possible accuracy. I would like to ask if it is possible to know the value of the direction, that I suppose is stored,  by asking a question to the OSM database without calculating the value through the coordinates of the two points after reading them on the display. As you know it's difficult to position the points on the display very well and this can cause errors Thank you very much</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-orientation" rel="tag" title="see questions tagged &#39;orientation&#39;">orientation</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-accuracy" rel="tag" title="see questions tagged &#39;accuracy&#39;">accuracy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Feb '20, 20:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0b7b93f8f715fa9978fda52959b494ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SergioV&#39;s gravatar image" />
<p><span>SergioV</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SergioV has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73208" class="comments-container">
&#10;</div>
<div id="comment-tools-73208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73208-form-container" class="comment-form-container">
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

<span id="73209"></span>

<div id="answer-container-73209" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73209-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming that:</p>
<ul>
<li>you have two addresses with house numbers</li>
<li>OpenStreetMap knows these addresses i.e. Nominatim can actually geocode them to the correct location</li>
<li>the road between the two addresses is straight</li>
</ul>
<p>Then the steps required would be the following:</p>
<ul>
<li>geocode location 1 (resulting in lat1, lon1)</li>
<li>geocode location 2 (resulting in lat2, lon2)</li>
<li>calculate bearing (or heading) angle betwen lat1,lon1 and lat2,lon2 using a suitable formula (e.g. <a href="https://www.igismap.com/formula-to-find-bearing-or-heading-angle-between-two-points-latitude-longitude/)">https://www.igismap.com/formula-to-find-bearing-or-heading-angle-between-two-points-latitude-longitude/)</a></li>
</ul>
<p>This will yield precise results independent of display. However, it will give you the angle between the two address points which is not necessarily the angle of the street. If you want to be super precise, you will need to identify the street (possibly through an additional geocoding request) and retrieve its geometry, then drop the perpendicular from each of the address points to the street geometry, and use the resulting points that lie on the street for the angle calculation. This will be harder if for any reason the street should consist of multiple parts in OSM.</p>
<p>There is no web service that would do this work for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '20, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-73209" class="comments-container">
&#10;</div>
<div id="comment-tools-73209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73209-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73223"></span>

<div id="answer-container-73223" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73223-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the OSM database, ways (which are used to model streets among others) are mostly a list of nodes. Only the node have coordinates. See the OSM wiki for more details about the OSM.database model.</p>
<p>So no, the direction of the ways is not stored. And they are usually not straight if composed of more than two nodes.</p>
<p>I guess that routers (like graphhopper, OSRM, etc, see the other question) will provide the direction of each segment of a calculated route between two points.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '20, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73223" class="comments-container">
&#10;</div>
<div id="comment-tools-73223" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73223-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73224"></span>

<div id="answer-container-73224" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73224-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for the answers. So if I need to know the direction of a stretch of road accurately I have to measure the coordinates of two points belonging to the stretch of road very accurately. I can't read the coordinates of the points on the display where the OSM is represented because it's not an accurate method, unless I zoom in on the map presentation</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '20, 00:03</strong></p>
<img src="https://secure.gravatar.com/avatar/0b7b93f8f715fa9978fda52959b494ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SergioV&#39;s gravatar image" />
<p><span>SergioV</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SergioV has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73224" class="comments-container">
<span id="73225"></span>
<div id="comment-73225" class="comment">
<div id="post-73225-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. Drawing a map always incurs a loss of precision. Just how big that loss is depends on many factors, including resolution and zoom level, but also the particular map style and parameters used for drawing (for example, some maps might simplify geometries before drawing). To get best results you would first have to retrieve the data behind the map, e.g. through services like Nominatim or Overpass, and then base your computation on that.</p>
</div>
<div id="comment-73225-info" class="comment-info">
<span class="comment-age">(25 Feb '20, 00:09)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-73224" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73224-form-container" class="comment-form-container">
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

