+++
type = "question"
title = "Administrative Boundaries&#x27; Lat/Long"
description = '''Hi, I&#x27;ve only discovered OSM tonight so please forgive me if this is a stupid question. I&#x27;m wanting to extract the lat/long of the boundaries of certain administrative divisions. For example, I want the lat/long of the borders of all the states in the USA and of the divisions of the UK (such as East...'''
date = "2012-05-23T23:29:00Z"
lastmod = "2012-05-25T16:02:00Z"
weight = 12917
keywords = [ "boundaries", "administrative", "admin_boundary", "longitude", "latitude" ]
aliases = [ "/questions/12917" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Administrative Boundaries' Lat/Long](/questions/12917/administrative-boundaries-latlong)

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
<span id="post-12917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12917-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've only discovered OSM tonight so please forgive me if this is a stupid question.</p>
<p>I'm wanting to extract the lat/long of the boundaries of certain administrative divisions. For example, I want the lat/long of the borders of all the states in the USA and of the divisions of the UK (such as East of England, South West England, etc).</p>
<p>What's the best way to extract this information?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '12, 23:29</strong></p>
<img src="https://secure.gravatar.com/avatar/2e3cc5bf4846515a43d14f3d191234e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nmpolo&#39;s gravatar image" />
<p><span>nmpolo</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nmpolo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12917" class="comments-container">
&#10;</div>
<div id="comment-tools-12917" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12917-form-container" class="comment-form-container">
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

<span id="12922"></span>

<div id="answer-container-12922" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12922-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nmpolo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can get a file containing all such information for UK with the call</p>
<pre><code>http://overpass-api.de/api/interpreter?data=[timeout:900][out:json];(rel[admin_level=4](50.0,-10.0,62.0,2.0);&gt;&gt;;);out;</code></pre>
<p>Note that such a call may take up to 15 minutes and yield a file of several megabyte size. "(50.0,-10.0,62.0,2.0)" is the bounding box with latitude, then longitude, then lat and lon for the upper boundary and draw a boundary around UK. "[admin_level=4]" is the level of most important intra-nation borders. The levels are explained <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative#admin_level">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '12, 08:28</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-12922" class="comments-container">
&#10;</div>
<div id="comment-tools-12922" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12922-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12954"></span>

<div id="answer-container-12954" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12954-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Shapes are available for UK at <a href="http://download.geofabrik.de/osm/europe/great_britain.shp.zip">geofabrik</a>. They don't seem to be available for US, so you can pay geofabrik or extract them with overpass-api (as explained by Roland) or osmosis.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '12, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-12954" class="comments-container">
&#10;</div>
<div id="comment-tools-12954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12954-form-container" class="comment-form-container">
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

