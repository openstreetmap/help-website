+++
type = "question"
title = "how to retrieve all available nodes from OSM databse"
description = '''hello i am vinod bathini, i want to know is there any way, how to retrieve all available nodes from the OSM database. the thing i am doing thesis, i want to retrieve the complete nodes information from Saxony(Germany) osm database. so i set up the OSM database in PostgreSQL. my task i should retriev...'''
date = "2015-06-10T12:33:00Z"
lastmod = "2015-06-10T19:53:00Z"
weight = 43514
keywords = [ "geometry", "nodes", "geonames", "geoserver" ]
aliases = [ "/questions/43514" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to retrieve all available nodes from OSM databse](/questions/43514/how-to-retrieve-all-available-nodes-from-osm-databse)

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
<span id="post-43514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43514-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-43514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello</p>
<p>i am vinod bathini, i want to know is there any way, how to retrieve all available nodes from the OSM database. the thing i am doing thesis, i want to retrieve the complete nodes information from Saxony(Germany) osm database. so i set up the OSM database in PostgreSQL. my task i should retrieve the data manually or automatically with out using id's or extensions . once i retrieve the nodes information according to that information we need to develop the routing.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geometry" rel="tag" title="see questions tagged &#39;geometry&#39;">geometry</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-geonames" rel="tag" title="see questions tagged &#39;geonames&#39;">geonames</span> <span class="post-tag tag-link-geoserver" rel="tag" title="see questions tagged &#39;geoserver&#39;">geoserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jun '15, 12:33</strong></p>
<img src="https://secure.gravatar.com/avatar/f8e3312c1d6fb44b2b0cc059a6b004f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="battinivinod&#39;s gravatar image" />
<p><span>battinivinod</span><br />
<span class="score" title="20 reputation points">20</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="battinivinod has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43514" class="comments-container">
<span id="43515"></span>
<div id="comment-43515" class="comment">
<div id="post-43515-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nodes are not sufficient for routing, you will need ways, too. And maybe relations for supporting turn restrictions and other advanced routing information. See <a href="https://wiki.openstreetmap.org/wiki/Routing">routing</a> in the wiki.</p>
</div>
<div id="comment-43515-info" class="comment-info">
<span class="comment-age">(10 Jun '15, 12:59)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43514-form-container" class="comment-form-container">
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

<span id="43516"></span>

<div id="answer-container-43516" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43516-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-43516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would really really suggest reading up on OSM before you start on your thesis.</p>
<p>The complete OSM data is available from planet.openstreetmap.org , regional extracts from a number of places, for example: <a href="http://www.geofabrik.de/data/download.html">http://www.geofabrik.de/data/download.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '15, 13:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jun '15, 10:41</strong> </span></p>
</div>
</div>
<div id="comments-container-43516" class="comments-container">
&#10;</div>
<div id="comment-tools-43516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43516-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43527"></span>

<div id="answer-container-43527" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43527-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't spent time building tools that are available. For example, there are tools that do all this work for you for <a href="https://github.com/MaZderMind/osm-history-renderer/blob/master/TUTORIAL.md">full history dumps</a>. From the little we know about what you want to accomplish, I'd guess you don't need history files, just current state of the map. This can be easily accomplished using GDAl within OSgeo and then importing the result into SQLite. I'm sure there are a lot of other options too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '15, 19:53</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-43527" class="comments-container">
&#10;</div>
<div id="comment-tools-43527" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43527-form-container" class="comment-form-container">
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

