+++
type = "question"
title = "Get Node from Coordinates (long, lat)"
description = '''I have a osm-viewer (something like JOSM) and I want to edit some data (offline ofc), like make out of a 1 lane roundabout a 3 lane one,.. I want that the user can click on a way and then edit this way. After that I need to find out on what node he is pointing and then I get with the help of the API...'''
date = "2015-09-04T13:10:00Z"
lastmod = "2016-12-27T15:25:00Z"
weight = 45053
keywords = [ "nodes", "coordinates" ]
aliases = [ "/questions/45053" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get Node from Coordinates (long, lat)](/questions/45053/get-node-from-coordinates-long-lat)

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
<span id="post-45053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45053-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a osm-viewer (something like JOSM) and I want to edit some data (offline ofc), like make out of a 1 lane roundabout a 3 lane one,..</p>
<p>I want that the user can click on a way and then edit this way. After that I need to find out on what node he is pointing and then I get with the help of the API the way:</p>
<blockquote>
<p>Ways for node: GET /api/0.6/node/#id/ways</p>
</blockquote>
<p>But the problem is I dont know how to get nodes from the Coordinates..</p>
<p>I mean Plan B would be to go through all nodes on the downloaded .osm-file and then use the found ID, to get the right way, but this would be much more code.</p>
<p>EDIT1: I have downloaded a map area wich the user has selected over the rest API (as .osm file). Now I focus my Map-Viewer (like the download osm data dialog from JOSM) on the selected area. And when the user clicks on a point on the map I get long and lat and with this data I'd like to ask the API if there are any ways on this point (I'd first ask for the nodes and over the nodeID I get the way)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '15, 13:10</strong></p>
<img src="https://secure.gravatar.com/avatar/52550724bcc20d40b0eb17ad82d19db7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlilord&#39;s gravatar image" />
<p><span>carlilord</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlilord has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Sep '15, 10:18</strong> </span></p>
</div>
</div>
<div id="comments-container-45053" class="comments-container">
<span id="53744"></span>
<div id="comment-53744" class="comment">
<div id="post-53744-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11433/carlilord">@carlilord</a> Did you succeed in accomplishing this?</p>
</div>
<div id="comment-53744-info" class="comment-info">
<span class="comment-age">(27 Dec '16, 15:25)</span> <span class="comment-user userinfo">kamalpreet</span>
</div>
</div>
</div>
<div id="comment-tools-45053" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45053-form-container" class="comment-form-container">
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

<span id="45069"></span>

<div id="answer-container-45069" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45069-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So you just want to get all (or specific) data at a specific position, i.e. inside a bounding box? Then look at the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Retrieving_map_data_by_bounding_box:_GET_.2Fapi.2F0.6.2Fmap">Retrieving map data by bounding box</a> API call.</p>
<p>If the bounding box is larger or if you need more flexible queries then take a look at <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> which also has a <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#All_data_in_a_bounding_box">all data in a bounding box</a> query.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '15, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-45069" class="comments-container">
<span id="45070"></span>
<div id="comment-45070" class="comment">
<div id="post-45070-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry thats not what I meant. I clarified my answer on EDIT1.</p>
</div>
<div id="comment-45070-info" class="comment-info">
<span class="comment-age">(05 Sep '15, 10:20)</span> <span class="comment-user userinfo">carlilord</span>
</div>
</div>
<span id="45073"></span>
<div id="comment-45073" class="comment">
<div id="post-45073-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you sure? Sounds exactly what you want to me. Grabbing nodes (or ways) in a given area. Although I don't understand why you need an API call in the first place since you already have all that information in your .osm file.</p>
</div>
<div id="comment-45073-info" class="comment-info">
<span class="comment-age">(05 Sep '15, 11:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45074"></span>
<div id="comment-45074" class="comment">
<div id="post-45074-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i know but the file could be pretty big and I'd have to do the filtering. I just wanted to know if there is an easier way over the rest API. Guess I'm building the logic myself then^^</p>
</div>
<div id="comment-45074-info" class="comment-info">
<span class="comment-age">(05 Sep '15, 11:18)</span> <span class="comment-user userinfo">carlilord</span>
</div>
</div>
</div>
<div id="comment-tools-45069" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45069-form-container" class="comment-form-container">
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

