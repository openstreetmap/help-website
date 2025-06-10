+++
type = "question"
title = "osm in arcgis - attributes for boundaries"
description = '''Hi,  I am trying to figure out how identify administrative regions within Vietnam. I Loaded the OSM data in ArcGIS using the OSM Editor. I then used the OSM Attribute Selector to add the osm_name field to the attribute table. I have been trying to make a map of Ha Noi but when I look on the openstre...'''
date = "2015-05-26T21:06:00Z"
lastmod = "2015-05-27T08:49:00Z"
weight = 43237
keywords = [ "hanoi", "symbol", "vietnam", "attribution", "tags" ]
aliases = [ "/questions/43237" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osm in arcgis - attributes for boundaries](/questions/43237/osm-in-arcgis-attributes-for-boundaries)

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
<span id="post-43237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43237-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying to figure out how identify administrative regions within Vietnam. I Loaded the OSM data in ArcGIS using the OSM Editor. I then used the OSM Attribute Selector to add the osm_name field to the attribute table. I have been trying to make a map of Ha Noi but when I look on the openstreetmap.org, Ha Noi is clearly labeled along with other administrative areas around the city. When working with the data loaded into my feature dataset the polygon feature class there is no Ha Noi identified as a boundary only as a Primary Highway. I guess my question is - How do I find boundary names of cities and states so that I can symbolize and label them?</p>
<p>Any help would be greatly appreciated - I'm an OSM newbie and am at a loss.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hanoi" rel="tag" title="see questions tagged &#39;hanoi&#39;">hanoi</span> <span class="post-tag tag-link-symbol" rel="tag" title="see questions tagged &#39;symbol&#39;">symbol</span> <span class="post-tag tag-link-vietnam" rel="tag" title="see questions tagged &#39;vietnam&#39;">vietnam</span> <span class="post-tag tag-link-attribution" rel="tag" title="see questions tagged &#39;attribution&#39;">attribution</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '15, 21:06</strong></p>
<img src="https://secure.gravatar.com/avatar/d83a5b97c561a7448f390b4345151dc6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aparisien&#39;s gravatar image" />
<p><span>aparisien</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aparisien has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43237" class="comments-container">
&#10;</div>
<div id="comment-tools-43237" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43237-form-container" class="comment-form-container">
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

<span id="43245"></span>

<div id="answer-container-43245" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43245-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you only just need boundary data from OSM, check out <a href="https://osm.wno-edv-service.de/boundaries/">the excellent boundaries tool</a> by wambacher.</p>
<p>Here you can download boundaries for any admin level that is correctly mapped in Openstreetmap, straight to .shp format. Click on the tiny white triangle left of the country name to drill down. The site is down right now, but it always comes back.</p>
<p>In the case of Hanoi, the most detailed boundary available seems to be at <a href="http://www.openstreetmap.org/relation/1903516">a regional level</a>. As you can see, there is also a node used as a label. This node is not included in the boundaries tool, but most of the tags of the relation itself are in the file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '15, 08:49</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-43245" class="comments-container">
&#10;</div>
<div id="comment-tools-43245" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43245-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43242"></span>

<div id="answer-container-43242" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43242-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Administrative boundaries in multipolygon form in OSM are far less complete in some, or maybe I should say many, regions than the main map may suggest. The main Standard map shows an amalgamation of true OSM multipolygons (converted to lines AFAIK for display), and line objects from unclosed ways.</p>
<p>This means that the main map is deceptively "complete", but that in reality, to get the same picture, quite a bit of clever data processing is necessary and unclosed ways must be combined with closed ways and multipolgyons.</p>
<p>In addition, many of the "name" labels visible on the OSM maps, aren't derived from administrative regions defined as <strong>boundary = x</strong>, but simply <strong>place = x</strong> tags in OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '15, 08:12</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 May '15, 08:13</strong> </span></p>
</div>
</div>
<div id="comments-container-43242" class="comments-container">
&#10;</div>
<div id="comment-tools-43242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43242-form-container" class="comment-form-container">
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

