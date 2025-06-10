+++
type = "question"
title = "How to trace and export a road segment for input elsewhere?"
description = '''How can I trace a segment of a road and export it as a file (.kml, .shp, etc.) for import into CartoDB or some other map?'''
date = "2015-01-08T20:37:00Z"
lastmod = "2015-01-10T17:42:00Z"
weight = 40162
keywords = [ "export", "road", "trace" ]
aliases = [ "/questions/40162" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to trace and export a road segment for input elsewhere?](/questions/40162/how-to-trace-and-export-a-road-segment-for-input-elsewhere)

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
<span id="post-40162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40162-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I trace a segment of a road and export it as a file (.kml, .shp, etc.) for import into CartoDB or some other map?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '15, 20:37</strong></p>
<img src="https://secure.gravatar.com/avatar/afa10ab05d63fdba13efb1bbe36fb906?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChuckSherman&#39;s gravatar image" />
<p><span>ChuckSherman</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChuckSherman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40162" class="comments-container">
<span id="40181"></span>
<div id="comment-40181" class="comment">
<div id="post-40181-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I appreciate the answers, but I'm still floundering. What I want to do is extract the geocoordinates of a stretch of road, say one mile from point A to point B, so I can add it as a layer to CartoDB (combined with a few other bits of road, eventually) that I will highlight in my CartoDB visualization in a different color. How to I mark the section of road I want? How do I export just that part of the map (with georeferencing). Am I being clear yet?</p>
</div>
<div id="comment-40181-info" class="comment-info">
<span class="comment-age">(09 Jan '15, 20:00)</span> <span class="comment-user userinfo">ChuckSherman</span>
</div>
</div>
<span id="40199"></span>
<div id="comment-40199" class="comment">
<div id="post-40199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The answer is to pull the data required out using something like geoJSON from Overpass as SimonPoole described. You need some means of identifying the specific features you require, such as names, OSM identifiers or some other combination. If OSM features do not precisely match your needs you will need to edit the data (for instance in QGIS). An indication of your level of OSM knowledge may help in providing more information, but most of these tasks have multiple answers on this site.</p>
</div>
<div id="comment-40199-info" class="comment-info">
<span class="comment-age">(10 Jan '15, 17:42)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40162-form-container" class="comment-form-container">
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

<span id="40172"></span>

<div id="answer-container-40172" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40172-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap data is, as the name says, open data provided under an open license, there is no need to trace over a map to extract the data.</p>
<p>If you simply want to get the geometry of a small number of roads you could for example use <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> to extract the geometry in geoJSON or other formats. AFAIK CartoDB supports OSM format data in some form directly so likely you don't even have to do that.</p>
<p>Currently there is no (IMHO) reasonable way to directly do what you want, so it would likely boil down to:</p>
<ul>
<li>exporting the required road segments to an editable format (kml, gpx, geoJSON)</li>
<li>trimming to the exact length you want</li>
<li>importing in to CartoDB</li>
</ul>
<p>There are at least a dozen variants how you could do this. For example besides what I've already outlined you could simply download the area in JOSM, merge/split the road in question till it has the reuired length and then export as GPX, but likely all will require you to learn something about the OSM data format and available tools.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '15, 23:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '15, 13:27</strong> </span></p>
</div>
</div>
<div id="comments-container-40172" class="comments-container">
<span id="40182"></span>
<div id="comment-40182" class="comment">
<div id="post-40182-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>my comment is mis-posted as an answer, below.</p>
</div>
<div id="comment-40182-info" class="comment-info">
<span class="comment-age">(09 Jan '15, 20:11)</span> <span class="comment-user userinfo">ChuckSherman</span>
</div>
</div>
<span id="40184"></span>
<div id="comment-40184" class="comment">
<div id="post-40184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10297/chucksherman">@ChuckSherman</a>: not any more, right?</p>
</div>
<div id="comment-40184-info" class="comment-info">
<span class="comment-age">(09 Jan '15, 20:24)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40172" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40172-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40173"></span>

<div id="answer-container-40173" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40173-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>depending on the length of the road, you can also just navigate to the area on the map, and click the export button at the top of the page which will let you downland a .osm file of the map area</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '15, 23:38</strong></p>
<img src="https://secure.gravatar.com/avatar/9f0faef4659de616c82f448ff3f4e8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaCor&#39;s gravatar image" />
<p><span>DaCor</span><br />
<span class="score" title="1339 reputation points"><span>1.3k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaCor has one accepted answer">2%</span></p>
</div>
</div>
<div id="comments-container-40173" class="comments-container">
<span id="40183"></span>
<div id="comment-40183" class="comment">
<div id="post-40183-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>my comment is mis-posted as an answer, below.</p>
</div>
<div id="comment-40183-info" class="comment-info">
<span class="comment-age">(09 Jan '15, 20:12)</span> <span class="comment-user userinfo">ChuckSherman</span>
</div>
</div>
</div>
<div id="comment-tools-40173" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40173-form-container" class="comment-form-container">
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

