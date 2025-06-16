+++
type = "question"
title = "Extract Building Coordinates from OSM XML (Polygons?)"
description = '''Hi, I have an OSM city map which I export in OSM XML data format and feed into a mobility simulator that pulls the road network out of the map. I now need however to parse the OSM map to get the coordinates of obstacles (buildings only considered)in the map, hopefully in CSV format as I need to impo...'''
date = "2012-12-29T13:24:00Z"
lastmod = "2012-12-31T07:49:00Z"
weight = 18751
keywords = [ "building", "polgon", "obstacles" ]
aliases = [ "/questions/18751" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract Building Coordinates from OSM XML (Polygons?)](/questions/18751/extract-building-coordinates-from-osm-xml-polygons)

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
<span id="post-18751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18751-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have an OSM city map which I export in OSM XML data format and feed into a mobility simulator that pulls the road network out of the map. I now need however to parse the OSM map to get the coordinates of obstacles (buildings only considered)in the map, hopefully in CSV format as I need to import these into a network simulator.</p>
<p>Could someone please let me know if such an xml parser exists to get the coordinates of the buildings or if not could the structure of the tags please be explained so that I can write a parser.</p>
<p>Many thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-polgon" rel="tag" title="see questions tagged &#39;polgon&#39;">polgon</span> <span class="post-tag tag-link-obstacles" rel="tag" title="see questions tagged &#39;obstacles&#39;">obstacles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '12, 13:24</strong></p>
<img src="https://secure.gravatar.com/avatar/05120e6e3dbb311df5314657b6e03548?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kerrymaid&#39;s gravatar image" />
<p><span>kerrymaid</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kerrymaid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18751" class="comments-container">
&#10;</div>
<div id="comment-tools-18751" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18751-form-container" class="comment-form-container">
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

<span id="18769"></span>

<div id="answer-container-18769" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18769-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The easiest would be to write it yourself. There are lots of libraries available for all kind of languages that read XML. The thing you want is quite specific, so there's no ready-made tool available.</p>
<p>The XML in OSM has three primitives: nodes, ways and relations. A node is just a pair of lat/lon coordinates. A way is an ordered list of nodes, and a relation is an ordered list of other types (nodes, ways and other relations). All these features have an id (in the xml denoted with the "id" attribute), these ids are used as reference (so the XML structure of an OSM way is just a list of node ids).</p>
<p>All primitives also have tags, these are stored as separate child XML elements of the type "tag".</p>
<p>So if you're interested in the buildings, you have to filter out all the ways (ways with the same start and end point are also used for surfaces) with a tag building=*, then get the nodes from those ways (via the id) and from those nodes, extract the coordinates (I don't know if you want one average coordinate per building, or if you want all nodes that represent building corners, but you can program both as you wish).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '12, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-18769" class="comments-container">
<span id="18790"></span>
<div id="comment-18790" class="comment">
<div id="post-18790-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... so your starting point to find some tools can be the OSM wiki about <a href="https://wiki.openstreetmap.org/wiki/Develop">https://wiki.openstreetmap.org/wiki/Develop</a></p>
</div>
<div id="comment-18790-info" class="comment-info">
<span class="comment-age">(31 Dec '12, 07:49)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-18769" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18769-form-container" class="comment-form-container">
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

