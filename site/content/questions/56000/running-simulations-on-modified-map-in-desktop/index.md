+++
type = "question"
title = "running simulations on modified map in desktop"
description = '''Hi I just got into OSRM a week ago for a project. My research is in urban planning and I want to be able to change the features of urban settings like &quot;width of the bike lane&quot; or number of pedestrians walking in the certain area of the city. I understand up to downloading the .osm file and setting u...'''
date = "2017-05-03T02:23:00Z"
lastmod = "2017-05-03T08:21:00Z"
weight = 56000
keywords = [ "osrm", "simulation" ]
aliases = [ "/questions/56000" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [running simulations on modified map in desktop](/questions/56000/running-simulations-on-modified-map-in-desktop)

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
<span id="post-56000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56000-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I just got into OSRM a week ago for a project. My research is in urban planning and I want to be able to change the features of urban settings like "width of the bike lane" or number of pedestrians walking in the certain area of the city. I understand up to downloading the .osm file and setting up the servers but I am not sure how can I integrate these features into my custom map in my machine and run simulations on top of these features like finding the best bike path etc. I basically want to edit the map properties as I want and run my own simulations. It would be helpful if I get any guidance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-simulation" rel="tag" title="see questions tagged &#39;simulation&#39;">simulation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '17, 02:23</strong></p>
<img src="https://secure.gravatar.com/avatar/c4ee2c16ceed69496f629cd0acf07122?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nsuman&#39;s gravatar image" />
<p><span>nsuman</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nsuman has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 May '17, 07:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-56000" class="comments-container">
&#10;</div>
<div id="comment-tools-56000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56000-form-container" class="comment-form-container">
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

<span id="56003"></span>

<div id="answer-container-56003" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56003-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSRM might not be the best choice for this as it requires recompiling the routing graph for every adjustment you make to the routing parameters - although this will be quick if you're only running it on a city size data set.</p>
<p>Of course OSRM doesn't, by default, react to things like "width of the bike lane" or "number of pedestrians milling about in this general area". You will have to use an OSM editor like JOSM to apply some made-up tags to your streets and bike lanes (e.g. select all streets in an area, add tag "pedestrian_density=137"), then save that file (do <em>not</em> upload to OSM!), then configure OSRM via its LUA profile code to react accordingly (e.g. "if pedestrian_density &lt; 100 then assume speed of 5 km per hour, if &gt;= 100 then assume speed of 4 km per hour" or something like that), and then you can compile the routing graph and run your analyses.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '17, 08:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56003" class="comments-container">
&#10;</div>
<div id="comment-tools-56003" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56003-form-container" class="comment-form-container">
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

