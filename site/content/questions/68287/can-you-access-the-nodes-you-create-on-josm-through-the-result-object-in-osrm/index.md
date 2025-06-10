+++
type = "question"
title = "Can you access the nodes (you create on JOSM) through the result object in OSRM?"
description = '''Hi all,  I just began using OSRM and JOSM. My workflow is that for a small area I wanted to add my gps points instead of the ones in the database (which I am able to using JOSM). Next, I join these points to make ways. Next, I do routing and get the nodes (ones I created) as an annotations object wh...'''
date = "2019-03-05T22:55:00Z"
lastmod = "2019-03-07T20:27:00Z"
weight = 68287
keywords = [ "josm", "osrm" ]
aliases = [ "/questions/68287" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can you access the nodes (you create on JOSM) through the result object in OSRM?](/questions/68287/can-you-access-the-nodes-you-create-on-josm-through-the-result-object-in-osrm)

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
<span id="post-68287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68287-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I just began using OSRM and JOSM. My workflow is that for a small area I wanted to add my gps points instead of the ones in the database (which I am able to using JOSM). Next, I join these points to make ways. Next, I do routing and get the nodes (ones I created) as an annotations object when I run the query. However, the nodes are randomly numbered because they are not stored in the database, so I cannot find the lat long values using <a href="http://api.openstreetmap.org/api/0.6/node/&#39;id&#39;.">http://api.openstreetmap.org/api/0.6/node/'id'.</a></p>
<p>My question is is there any (if any) way to being able to get the lat long value of the new nodes after running an OSRM query, without updating the main database or running an osrm server locally. Basically when a node is created (Shift + d) using lat long value, is there a way of accessing those using the OSRM result object?</p>
<p>I can try explaining this better, if am not able to already.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '19, 22:55</strong></p>
<img src="https://secure.gravatar.com/avatar/6b0f20fa88ab1aa7ca6117c8e37a8470?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shayaan_1&#39;s gravatar image" />
<p><span>shayaan_1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shayaan_1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68287" class="comments-container">
<span id="68288"></span>
<div id="comment-68288" class="comment">
<div id="post-68288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It isn't clear exactly what you're doing, or what goal you're trying to reach. It sounds like you're using the public version of OSRM, which only uses the public OSM database, not any objects you've created locally and not uploaded to the main OSM database. OSRM can never know about those.</p>
</div>
<div id="comment-68288-info" class="comment-info">
<span class="comment-age">(06 Mar '19, 00:22)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="68289"></span>
<div id="comment-68289" class="comment">
<div id="post-68289-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So I am using lat long values collected from a rtk device and want to replace them with the current nodes in the osm database. Once I get a route from A to B. I want to be able to retrieve the lat long values of the points along that route which are now the ones from the rtk device. I save the changes I made to the map using JOSM in a pbf file and then use that pbf file to be used in OSRM. The json output I get from OSRM returns the nodes along that route. Essentially I want to be able to do routing from A to B and then use the result to retrieve my data along that route. I hope this explains it better</p>
</div>
<div id="comment-68289-info" class="comment-info">
<span class="comment-age">(06 Mar '19, 02:35)</span> <span class="comment-user userinfo">shayaan_1</span>
</div>
</div>
<span id="68301"></span>
<div id="comment-68301" class="comment">
<div id="post-68301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to confirm, you're running your own instances of everything involved (including OSRM, OSM database, OSM API), and you aren't using the public instances?</p>
</div>
<div id="comment-68301-info" class="comment-info">
<span class="comment-age">(06 Mar '19, 16:50)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="68311"></span>
<div id="comment-68311" class="comment">
<div id="post-68311-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So the OSM API I use to search up nodes (i.e. <a href="http://api.openstreetmap.org/api/0.6/node/&#39;id&#39;)">http://api.openstreetmap.org/api/0.6/node/'id')</a> is not on my machine. I'm running OSRM on a pbf file which I extracted from bbbike and then edited using JOSM.</p>
</div>
<div id="comment-68311-info" class="comment-info">
<span class="comment-age">(07 Mar '19, 00:29)</span> <span class="comment-user userinfo">shayaan_1</span>
</div>
</div>
<span id="68325"></span>
<div id="comment-68325" class="comment">
<div id="post-68325-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Basically, I wanna be able to perform routing on my own data. The result from the the routing machine should be able to return 'my data'. What would be the easiest way to do it?</p>
</div>
<div id="comment-68325-info" class="comment-info">
<span class="comment-age">(07 Mar '19, 19:34)</span> <span class="comment-user userinfo">shayaan_1</span>
</div>
</div>
<span id="68326"></span>
<div id="comment-68326" class="comment not_top_scorer">
<div id="post-68326-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you have nodes that only exist in your local file, then the public editing API certainly can't tell you anything about them.</p>
</div>
<div id="comment-68326-info" class="comment-info">
<span class="comment-age">(07 Mar '19, 19:35)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="68327"></span>
<div id="comment-68327" class="comment not_top_scorer">
<div id="post-68327-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So if I were to use a local instance of the API would I then be able to save the data and access it if I used OSRM library?</p>
</div>
<div id="comment-68327-info" class="comment-info">
<span class="comment-age">(07 Mar '19, 20:27)</span> <span class="comment-user userinfo">shayaan_1</span>
</div>
</div>
</div>
<div id="comment-tools-68287" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-68287-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

