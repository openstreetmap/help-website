+++
type = "question"
title = "From OSM PBF to routable road network"
description = '''I am looking for a solution to parse OSM PBF files and obtain a road network that is navigable offline. Ideally, it should split ways at intersections with other ways and country boundaries and deduce traversing options based on the oneway and access tags. I have found the following:  Atlas Valhalla...'''
date = "2019-07-06T17:17:00Z"
lastmod = "2019-07-07T22:48:00Z"
weight = 69907
keywords = [ "software", "osm.pbf", "pbf", "routing", "parsing" ]
aliases = [ "/questions/69907" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [From OSM PBF to routable road network](/questions/69907/from-osm-pbf-to-routable-road-network)

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
<span id="post-69907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69907-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking for a solution to parse OSM PBF files and obtain a road network that is navigable offline. Ideally, it should split ways at intersections with other ways and country boundaries and deduce traversing options based on the <code>oneway</code> and <code>access</code> tags.</p>
<p>I have found the following:</p>
<ul>
<li><a href="https://github.com/osmlab/atlas">Atlas</a></li>
<li><a href="https://github.com/valhalla/valhalla">Valhalla/Mjölnir</a></li>
<li><a href="https://github.com/OsmSharp/core">OsmSharp/Itinero</a></li>
</ul>
<p>But I was wondering whether there could be any more options around. I have checked the <a href="https://wiki.openstreetmap.org/wiki/Frameworks">Frameworks wiki page</a>, but the two from above that were mentioned there were listed under different categories.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-software" rel="tag" title="see questions tagged &#39;software&#39;">software</span> <span class="post-tag tag-link-osm.pbf" rel="tag" title="see questions tagged &#39;osm.pbf&#39;">osm.pbf</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jul '19, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/6ddb3ffa68da77e22f967daac3e2ea40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flogoe&#39;s gravatar image" />
<p><span>flogoe</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flogoe has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69907" class="comments-container">
&#10;</div>
<div id="comment-tools-69907" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69907-form-container" class="comment-form-container">
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

<span id="69921"></span>

<div id="answer-container-69921" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69921-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Routing">routing</a> page might be a good place to start looking. In terms of public discussions, <a href="https://wiki.openstreetmap.org/wiki/GraphHopper">GraphHopper</a> and <a href="https://wiki.openstreetmap.org/wiki/Open_Source_Routing_Machine">OSRM</a> get mentioned fairly frequently.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '19, 22:48</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-69921" class="comments-container">
&#10;</div>
<div id="comment-tools-69921" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69921-form-container" class="comment-form-container">
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

