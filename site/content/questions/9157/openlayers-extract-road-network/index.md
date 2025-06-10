+++
type = "question"
title = "Openlayers extract road network"
description = '''Hello everyone , I&#x27;m new to openlayer and i have a problem and i need some help! I want to take the road network from an area and build a graph so i can take it and use it for finding sortest path . My problem is i don&#x27;t know how to take the road network and how to construct the path . I done a goog...'''
date = "2011-11-21T16:03:00Z"
lastmod = "2011-11-22T16:49:00Z"
weight = 9157
keywords = [ "graph", "openlayers", "road" ]
aliases = [ "/questions/9157" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Openlayers extract road network](/questions/9157/openlayers-extract-road-network)

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
<span id="post-9157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9157-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone , I'm new to openlayer and i have a problem and i need some help! I want to take the road network from an area and build a graph so i can take it and use it for finding sortest path . My problem is i don't know how to take the road network and how to construct the path . I done a google search and i found that i have to use OSM files but i don't know how . If you could show me some examples and point me to the right direction it would be great</p>
<p>Thanks in advance, cheers john</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '11, 16:03</strong></p>
<img src="https://secure.gravatar.com/avatar/6657f0097172b7e22c664d61d6b81095?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="john_&#39;s gravatar image" />
<p><span>john_</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="john_ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9157" class="comments-container">
&#10;</div>
<div id="comment-tools-9157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9157-form-container" class="comment-form-container">
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

<span id="9158"></span>

<div id="answer-container-9158" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9158-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can extract road networks from OpenStreetMap data and use them for routing, but OpenLayers is only used to display the result of that process.</p>
<p>Instead you'll need to get to know how OSM data is structured, the tools you can use to import it into other systems (such as pgRouting), how to perform routing queries, and only then how to display the results. If you have specific questions about OpenStreetMap you can ask them here, but otherwise a good place to start would be <a href="http://wiki.openstreetmap.org/wiki/Osm2pgrouting">osm2pgrouting</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '11, 16:20</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-9158" class="comments-container">
<span id="9182"></span>
<div id="comment-9182" class="comment">
<div id="post-9182-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So i have to create a database and load my data there but is there anothere way to do that! I want to have my road network graph stored to a file so then i can run an algorithm to find the sortest path</p>
</div>
<div id="comment-9182-info" class="comment-info">
<span class="comment-age">(22 Nov '11, 15:29)</span> <span class="comment-user userinfo">john_</span>
</div>
</div>
<span id="9185"></span>
<div id="comment-9185" class="comment">
<div id="post-9185-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>pgRouting provides most common routing algorithms anyway, so you wouldn't need to reimplement them. Also, scanning a file to find start and end points of your route would be far more resource-intensive than using a database.</p>
</div>
<div id="comment-9185-info" class="comment-info">
<span class="comment-age">(22 Nov '11, 16:16)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
<span id="9186"></span>
<div id="comment-9186" class="comment">
<div id="post-9186-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To get an overview about all routing possibilities based on OSM, have a look at the wiki at <a href="http://wiki.openstreetmap.org/wiki/Routing">http://wiki.openstreetmap.org/wiki/Routing</a> and all its sub pages.</p>
</div>
<div id="comment-9186-info" class="comment-info">
<span class="comment-age">(22 Nov '11, 16:49)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-9158" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9158-form-container" class="comment-form-container">
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

