+++
type = "question"
title = "Can OSM build proximity maps?"
description = '''Hi, I want to construct proximity maps. For example, a map where each point has a color, indicating its distance from a river or a water source (lake, etc.). Is there any way of doing that with OSM? Thanks a lot, Tomer'''
date = "2022-01-26T08:14:00Z"
lastmod = "2022-02-02T08:46:00Z"
weight = 83208
keywords = [ "proximity_maps" ]
aliases = [ "/questions/83208" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can OSM build proximity maps?](/questions/83208/can-osm-build-proximity-maps)

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
<span id="post-83208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83208-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to construct proximity maps. For example, a map where each point has a color, indicating its distance from a river or a water source (lake, etc.).</p>
<p>Is there any way of doing that with OSM?</p>
<p>Thanks a lot, Tomer</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-proximity_maps" rel="tag" title="see questions tagged &#39;proximity_maps&#39;">proximity_maps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jan '22, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/694e871be57e218af3de83983be6a78d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tomermilo&#39;s gravatar image" />
<p><span>tomermilo</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tomermilo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83208" class="comments-container">
&#10;</div>
<div id="comment-tools-83208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83208-form-container" class="comment-form-container">
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

<span id="83228"></span>

<div id="answer-container-83228" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83228-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Possibly.</p>
<p>The focus of the OpenStreetMap project is the map data. There are a variety of tools around filtering extracting and rendering that data in the "ecosystem" but I'm not aware of any OSM specific tools related to your question. For the analysis you're interested in you will probably need something more generic like <a href="https://qgis.org/en/site/">QGIS</a> which <a href="https://qgis3-10-geoanalysis-un.readthedocs.io/en/latest/vector/proximity.html#distance-from-point-to-layer">sounds like</a> it might do what you're asking.</p>
<p>OSM data varies in completeness from region to region. If the <a href="https://wiki.openstreetmap.org/wiki/Map_features#Water">features</a> you are interested in are relatively complete in your area you may be able to use it in your analysis. Most contributors contribute as a hobby so if you need information that is 'authoritative' or rigorously checked you will need to seek it elsewhere. For relatively small areas tools like <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">Overpass turbo</a> can be used to download only the information you are interested in. There is a QuickOSM plugin for QGIS that can be used to download data from within the program. For larger areas you will need to download <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">extracts</a> and filter locally.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '22, 07:55</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-83228" class="comments-container">
<span id="83310"></span>
<div id="comment-83310" class="comment">
<div id="post-83310-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This was very helpful! Thanks a lot!</p>
</div>
<div id="comment-83310-info" class="comment-info">
<span class="comment-age">(02 Feb '22, 08:46)</span> <span class="comment-user userinfo">tomermilo</span>
</div>
</div>
</div>
<div id="comment-tools-83228" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83228-form-container" class="comment-form-container">
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

