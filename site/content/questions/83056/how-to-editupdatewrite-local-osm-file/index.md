+++
type = "question"
title = "How to edit/update/write local .osm file?"
description = '''Hi, I am quite new to this forum, sorry if I make any mistake. Currently I am using overpy package in python to query osm. I can get and use query results and it is quite useful for my purpose. I am using offline query with docker image.  However, I&#x27;d like to modify the .osm file in which I extracte...'''
date = "2022-01-11T20:38:00Z"
lastmod = "2022-01-12T12:21:00Z"
weight = 83056
keywords = [ "osm", "update" ]
aliases = [ "/questions/83056" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to edit/update/write local .osm file?](/questions/83056/how-to-editupdatewrite-local-osm-file)

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
<span id="post-83056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83056-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am quite new to this forum, sorry if I make any mistake. Currently I am using overpy package in python to query osm. I can get and use query results and it is quite useful for my purpose. I am using offline query with docker image. However, I'd like to modify the .osm file in which I extracted from &lt;name&gt;.osm.bz2 format. As far as I see, there is no query like API for writing, and update of the map is done via website or 3rd party tools like JOSM... I am able to parse xml file, find/get the corresponding node and edit that node/way. However, how can I <strong>add</strong> new node or <strong>remove</strong> a node from a way? I know that each way/node IDs are unique. So, I cannot directly add new node to .xml with an arbitrary ID.</p>
<p>Is there a way to do this? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '22, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/761de0d6d13397df82446f39cf1098b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alisvndk88&#39;s gravatar image" />
<p><span>alisvndk88</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alisvndk88 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '22, 20:39</strong> </span></p>
</div>
</div>
<div id="comments-container-83056" class="comments-container">
&#10;</div>
<div id="comment-tools-83056" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83056-form-container" class="comment-form-container">
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

<span id="83057"></span>

<div id="answer-container-83057" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83057-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can create nodes with arbitrary IDs (that are not already used in your file) and add them to a way in your XML, or remove nodes from a way as you please as long as you're not planning to upload the file to OSM. You can also use JOSM to modify a local osm file; if you create new objects in JOSM, it will assign negative IDs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '22, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-83057" class="comments-container">
<span id="83058"></span>
<div id="comment-83058" class="comment">
<div id="post-83058-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is not an answer for me. The .osm file I'm using is quite lage(country). I'll need to use this local file in the future over and over again. So, ID's are important and adding new node will not be easy for a .osm file with large scale. Isn't there a way or API for this purpose to add/remove/update from python etc.?</p>
</div>
<div id="comment-83058-info" class="comment-info">
<span class="comment-age">(12 Jan '22, 06:55)</span> <span class="comment-user userinfo">alisvndk88</span>
</div>
</div>
<span id="83060"></span>
<div id="comment-83060" class="comment">
<div id="post-83060-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The OSM website (and with it, the API and database) is open source (<a href="https://github.com/openstreetmap/openstreetmap-website).">https://github.com/openstreetmap/openstreetmap-website).</a> You can install your own version locally, populate that with OSM data, and then use it. You can even set up a local Overpass instance fed by that data. But it is a complex system and maybe overkill for your purpose.</p>
<p>In general, keeping your own modified version of OSM data around is often not a good idea since the moment you start making local modifications, you're losing any ability to update your data from OSM in the future.</p>
</div>
<div id="comment-83060-info" class="comment-info">
<span class="comment-age">(12 Jan '22, 08:39)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="83062"></span>
<div id="comment-83062" class="comment">
<div id="post-83062-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think osmapi python module is doing exactly what I want. It has ability to update the map using credentials...</p>
</div>
<div id="comment-83062-info" class="comment-info">
<span class="comment-age">(12 Jan '22, 12:21)</span> <span class="comment-user userinfo">alisvndk88</span>
</div>
</div>
</div>
<div id="comment-tools-83057" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83057-form-container" class="comment-form-container">
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

