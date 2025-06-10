+++
type = "question"
title = "Generating node information from point A to point B from OpenStreetMap?"
description = '''I have the OpenStreetMap database of Saxony and i want to Return a street which is between 2 given Node ID I should return in POSTGRE SQL  name Longitude and Latitude of all points between the nodes Distance (double value in km)  answer should be something like  {…,name: “Annaberger Straße”, points:...'''
date = "2015-09-29T16:56:00Z"
lastmod = "2015-09-30T14:32:00Z"
weight = 45655
keywords = [ "nearest", "nodes", "postgis", "distance" ]
aliases = [ "/questions/45655" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Generating node information from point A to point B from OpenStreetMap?](/questions/45655/generating-node-information-from-point-a-to-point-b-from-openstreetmap)

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
<span id="post-45655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45655-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the OpenStreetMap database of Saxony and i want to Return a street which is between 2 given Node ID I should return in POSTGRE SQL</p>
<ul>
<li>name</li>
<li>Longitude and Latitude of all points between the nodes</li>
<li>Distance (double value in km)</li>
</ul>
<p>answer should be something like</p>
<pre><code>{…,name: “Annaberger Straße”, points:[ {Lng, Lat}, {Lng, Lat}, …], distance: ???,…}</code></pre>
<p>i want find the distance between two nodes and also i need to return the street name, and geometries between the nodes from openstreetmap database?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nearest" rel="tag" title="see questions tagged &#39;nearest&#39;">nearest</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Sep '15, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/d1e77d2eee1edd6a09c786e11b0c87a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vinod12b&#39;s gravatar image" />
<p><span>vinod12b</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vinod12b has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '15, 20:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45655" class="comments-container">
<span id="45661"></span>
<div id="comment-45661" class="comment">
<div id="post-45661-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>do you mean routing or a straight line between the two nodes?</p>
</div>
<div id="comment-45661-info" class="comment-info">
<span class="comment-age">(29 Sep '15, 20:36)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="45664"></span>
<div id="comment-45664" class="comment">
<div id="post-45664-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Have you already imported the data into a PostgreSQL database, and if yes, how?</p>
</div>
<div id="comment-45664-info" class="comment-info">
<span class="comment-age">(29 Sep '15, 22:24)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="45670"></span>
<div id="comment-45670" class="comment">
<div id="post-45670-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>aseerel4c26- thank you and yeah straight line between two nodes ..</p>
<p>Frederik Ramm- i imported .pbf file from gofabrik to postgre sql using osm2pgsql through cmd</p>
</div>
<div id="comment-45670-info" class="comment-info">
<span class="comment-age">(30 Sep '15, 14:32)</span> <span class="comment-user userinfo">vinod12b</span>
</div>
</div>
</div>
<div id="comment-tools-45655" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45655-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

