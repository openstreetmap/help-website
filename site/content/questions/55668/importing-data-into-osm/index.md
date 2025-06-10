+++
type = "question"
title = "Importing data into OSM"
description = '''I have road data for the country of Ethiopia I would like to update on OSM. The road data came from geofabrik.de. I downloaded the shapefile version of it and started to add a few fields of my own. I needed these fields for another project. However, I started to add more data into it and would like ...'''
date = "2017-04-17T21:15:00Z"
lastmod = "2017-04-18T09:44:00Z"
weight = 55668
keywords = [ "roads", "ethiopia" ]
aliases = [ "/questions/55668" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Importing data into OSM](/questions/55668/importing-data-into-osm)

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
<span id="post-55668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55668-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have road data for the country of Ethiopia I would like to update on OSM. The road data came from geofabrik.de. I downloaded the shapefile version of it and started to add a few fields of my own. I needed these fields for another project. However, I started to add more data into it and would like to know how I can add them back to OSM now.</p>
<p>What I wanted to do was remove all the roads for Ethiopia and reimport them back into OSM. I figured this shouldn't cause any errors. I only updated the roads for Addis Ababa. I made sure all the intersections are crossed properly and there aren't any lines that's just on their own.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-ethiopia" rel="tag" title="see questions tagged &#39;ethiopia&#39;">ethiopia</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Apr '17, 21:15</strong></p>
<img src="https://secure.gravatar.com/avatar/da46f77fae7a1db2672d214911c22805?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="teddyumd&#39;s gravatar image" />
<p><span>teddyumd</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="teddyumd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55668" class="comments-container">
&#10;</div>
<div id="comment-tools-55668" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55668-form-container" class="comment-form-container">
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

<span id="55672"></span>

<div id="answer-container-55672" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55672-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>First of all, <strong>DO NOT DELETE</strong> the roads from Ethiopia. There might be a lot more data to the OpenStreetMap road data that you will be removing if you remove them all. It might remove all the local names, references, specific road surface etc. Also, it will remove names of all the mappers who have contributed towards drawing all those roads. The best way to update is to use "Replace Geometry" function of JOSM which keeps the history of all the mappers who have previously worked on a feature.</p>
<p>Secondly, if the data if from Geofabrik.de, I think that data is coming from OpenStreetMap itself. Check out this <a href="https://www.geofabrik.de/data/download.html">link</a>.</p>
<p>Thirdly, there are restrictions into importing Shapefiles and uploading directly to OpenStreetMap. Check out this <a href="http://wiki.openstreetmap.org/wiki/Software_comparison/Import_a_shapefile">link</a>.</p>
<p>So, I think you will have to go through a rigorous process of validating and updating all the data that you have (if it is indeed different data) rather than just simply removing and updating.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '17, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/c482180b767d07897d150d7b426ca4e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmahmud&#39;s gravatar image" />
<p><span>mmahmud</span><br />
<span class="score" title="638 reputation points">638</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmahmud has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-55672" class="comments-container">
&#10;</div>
<div id="comment-tools-55672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55672-form-container" class="comment-form-container">
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

