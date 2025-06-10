+++
type = "question"
title = "Update planet_osm_node, way and relation table"
description = '''Hi, I have a tile server and I populated the database using osm2pgsql. I have created an application which can change the map data in the planet_osm_line table. I was wondering how I can update the planet_osm_nodes, planet_osm_ways, planet_osm_rels tables based on the changes in the planet_osm_lines...'''
date = "2013-03-10T21:37:00Z"
lastmod = "2013-03-14T20:48:00Z"
weight = 20619
keywords = [ "osm", "osm2pgsql", "planet_osm" ]
aliases = [ "/questions/20619" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Update planet_osm_node, way and relation table](/questions/20619/update-planet_osm_node-way-and-relation-table)

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
<span id="post-20619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20619-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have a tile server and I populated the database using osm2pgsql. I have created an application which can change the map data in the planet_osm_line table.</p>
<p>I was wondering how I can update the planet_osm_nodes, planet_osm_ways, planet_osm_rels tables based on the changes in the planet_osm_lines table.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '13, 21:37</strong></p>
<img src="https://secure.gravatar.com/avatar/8f19a0a6b0afe902c224e03a8eb38ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srose&#39;s gravatar image" />
<p><span>srose</span><br />
<span class="score" title="161 reputation points">161</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20619" class="comments-container">
&#10;</div>
<div id="comment-tools-20619" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20619-form-container" class="comment-form-container">
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

<span id="20625"></span>

<div id="answer-container-20625" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20625-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can't. The "lines" table is derived from the nodes/ways/rels tables and not vice versa. To achieve what you want one would have to "reverse engineer" the content of the lines table: "So, this line is made from OSM way #123456, let's see, that way would normally yield a geometry like this but the line has a different geometry; how come - maybe one of the nodes has been moved, or deleted...?" - even if you were to implement such a complex algorithm it would still be very error prone because it is possible that a node move "detected" by your algorithm has unwanted side effects. (Several ways could be using the same nodes; this means that several line geometries in your line table would be invisibly joined, and that you cannot move one without also moving the other.)</p>
<p>You might get a more helpful response if you explained <em>why</em> you want to merge back your changes; maybe there's another process that achieves the same.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '13, 00:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-20625" class="comments-container">
<span id="20638"></span>
<div id="comment-20638" class="comment">
<div id="post-20638-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, the reason is that I am using Osm2Po for route finding. When a user makes a change to the map I want to update the routing graph so it takes the users changes into account. This requires me to either create a custom parser in Osm2Po, which I have done except it uses these three tables and so it won't work. If there is another way to export my planet_osm_line table to an .osm file of .osm.pbf file that would be ok but I am not sure how to do that. I have tried using Osmosis but it doesn't seem compatible with my DB.</p>
</div>
<div id="comment-20638-info" class="comment-info">
<span class="comment-age">(11 Mar '13, 15:55)</span> <span class="comment-user userinfo">srose</span>
</div>
</div>
<span id="20686"></span>
<div id="comment-20686" class="comment">
<div id="post-20686-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Why are you updating the planet_osm_lines table in the first place? And with what tools? Who's users are making those changes? Are those valid changes you could make directly to the OSM db? In that case you could use the standard osm2pgsql diff imports which first updates the planet_osm_node/ways/rels tables and then from there updates the lines/points/polygon tables to reflect those changes.</p>
</div>
<div id="comment-20686-info" class="comment-info">
<span class="comment-age">(13 Mar '13, 05:38)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="20715"></span>
<div id="comment-20715" class="comment">
<div id="post-20715-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi, I have created an app which downloads the map data from the line table in my database and allows the user to edit it. I use the lines table so that when the user has made a change, the map will re-render to show the change on the map. This app is aimed to be independent from changes made on the actual OSM website so I can't use diffs.</p>
</div>
<div id="comment-20715-info" class="comment-info">
<span class="comment-age">(14 Mar '13, 20:48)</span> <span class="comment-user userinfo">srose</span>
</div>
</div>
</div>
<div id="comment-tools-20625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20625-form-container" class="comment-form-container">
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

