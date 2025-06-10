+++
type = "question"
title = "Software for estimating road distance around a central node"
description = '''Hello, I&#x27;m searching for a software that can give me a radius of X kilometers of roads around a node. Note that it is not simple &quot;draw a circle&quot; question (like this: http://www.freemaptools.com/radius-around-point.htm), but it involves calculation of road length. The questions is more like &quot;find eve...'''
date = "2011-06-02T07:32:00Z"
lastmod = "2011-06-02T12:56:00Z"
weight = 5484
keywords = [ "graph", "location", "software" ]
aliases = [ "/questions/5484" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Software for estimating road distance around a central node](/questions/5484/software-for-estimating-road-distance-around-a-central-node)

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
<span id="post-5484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5484-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-5484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,<br />
I'm searching for a software that can give me a radius of X kilometers of roads around a node. Note that it is not simple "draw a circle" question (like this: <a href="http://www.freemaptools.com/radius-around-point.htm),">http://www.freemaptools.com/radius-around-point.htm),</a> but it involves calculation of road length. The questions is more like "find every node within X-node radius in a graph".</p>
<p>My whole idea is to find suitable locations for a picnic site as far as 50 kilometers driving from home :)</p>
<p>It would be nice if that software can also choose highways that are only for "driving" like primary, secondary, trunk, etc.</p>
<p><a href="http://www.mapnificent.net">http://www.mapnificent.net</a> is something like that, but there are limited numbers of cities around the world. And it measures not by distance but by time for travel. And it uses Google Maps, not OSM.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span> <span class="post-tag tag-link-software" rel="tag" title="see questions tagged &#39;software&#39;">software</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '11, 07:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jun '11, 07:34</strong> </span></p>
</div>
</div>
<div id="comments-container-5484" class="comments-container">
&#10;</div>
<div id="comment-tools-5484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5484-form-container" class="comment-form-container">
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

<span id="5488"></span>

<div id="answer-container-5488" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5488-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a script in OSM SVN that does that, <a href="http://svn.openstreetmap.org/applications/utils/distance_maps/">here.</a> It will require some Perl skills to get it to do your bidding though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '11, 10:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-5488" class="comments-container">
&#10;</div>
<div id="comment-tools-5488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5488-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5490"></span>

<div id="answer-container-5490" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5490-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's funny you'd ask this, because this is exactly what I was researching this morning. If you'd like to import your OSM data into a PostGIS database, you can use the pgRouting project which has a driving_distance() function which does exactly what you're looking for. Here are some references to get you started.</p>
<ul>
<li><a href="http://underdark.wordpress.com/2011/02/12/drive-time-isochrones/">Using QGIS and pgRouting</a></li>
<li><a href="http://www.carsonfarmer.com/?p=799">pgRouting, OpenStreetMap, and QGIS</a></li>
<li><a href="http://workshop.pgrouting.org/chapters/introduction.html">FOSS4G routing with pgRouting tools, OpenStreetMap road data and GeoExt</a></li>
</ul>
<p>If you'd like to search more on this subject key words to search are <em>driving distance</em> (even though the cost can be anything, like time, distance is most common), and <em>catchment area</em>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '11, 12:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ba99ad3778972fee07700e1eb36cc822?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoshD&#39;s gravatar image" />
<p><span>JoshD</span><br />
<span class="score" title="300 reputation points">300</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoshD has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-5490" class="comments-container">
&#10;</div>
<div id="comment-tools-5490" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5490-form-container" class="comment-form-container">
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

