+++
type = "question"
title = "how to get parent ways of some way"
description = '''hi i wanna take parent ways of some way three times, its possible with this method https://www.openstreetmap.org/api/0.6/way/id.json https://www.openstreetmap.org/api/0.6/node/ways.json but i must send request 6 time to get my desire result  can i make it one request with overpass api ?  btw , if wo...'''
date = "2020-07-08T09:05:00Z"
lastmod = "2020-07-08T13:49:00Z"
weight = 75595
keywords = [ "ways", "overpass", "nodes" ]
aliases = [ "/questions/75595" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to get parent ways of some way](/questions/75595/how-to-get-parent-ways-of-some-way)

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
<span id="post-75595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75595-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi</p>
<p>i wanna take parent ways of some way three times, its possible with this method</p>
<p><a href="https://www.openstreetmap.org/api/0.6/way/id.json">https://www.openstreetmap.org/api/0.6/way/id.json</a></p>
<p><a href="https://www.openstreetmap.org/api/0.6/node/ways.json">https://www.openstreetmap.org/api/0.6/node/ways.json</a></p>
<p>but i must send request 6 time to get my desire result</p>
<p>can i make it one request with overpass api ?</p>
<p>btw , if would be awesome if add nearest highway to result :D</p>
<pre><code>[out:json];
way(325887398);
way(around:200)[highway~&quot;residential|secondary&quot;];
out;</code></pre>
<p>thx for helping</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '20, 09:05</strong></p>
<img src="https://secure.gravatar.com/avatar/cce2674789c49c07dfc3f7f8e7bdc22a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryzexsp&#39;s gravatar image" />
<p><span>ryzexsp</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryzexsp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jul '20, 09:51</strong> </span></p>
</div>
</div>
<div id="comments-container-75595" class="comments-container">
<span id="75596"></span>
<div id="comment-75596" class="comment">
<div id="post-75596-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Could you expand/clarity. Post the overpass routines. What's in id.json &amp; ways.json? What does "three times" mean?</p>
</div>
<div id="comment-75596-info" class="comment-info">
<span class="comment-age">(08 Jul '20, 09:36)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="75597"></span>
<div id="comment-75597" class="comment">
<div id="post-75597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://www.openstreetmap.org/api/0.6/way/325887398.json">https://www.openstreetmap.org/api/0.6/way/325887398.json</a></p>
<p>its an way id , through this way i take first parent node</p>
<p><a href="https://www.openstreetmap.org/api/0.6/node/3325093995/ways.json">https://www.openstreetmap.org/api/0.6/node/3325093995/ways.json</a></p>
<p>through this i take first parent way</p>
<p>i do this three times to get parent ways</p>
<p>"three times" i want take parent of way1 which is for example way2, and take parent of way2 which is way3 , and take parent of way3 which is way4</p>
<p>and nearest secondary way and end</p>
</div>
<div id="comment-75597-info" class="comment-info">
<span class="comment-age">(08 Jul '20, 09:58)</span> <span class="comment-user userinfo">ryzexsp</span>
</div>
</div>
<span id="75605"></span>
<div id="comment-75605" class="comment">
<div id="post-75605-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There are neither parent ways not parent nodes in the OSM data model.</p>
<p>Ways -do- have member nodes (which carry the geometry), and a specific node can be a member of multiple ways, typically, but not always, are junctions and connections between ways (where the the end node of a way will be an end node of another way).</p>
</div>
<div id="comment-75605-info" class="comment-info">
<span class="comment-age">(08 Jul '20, 13:49)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-75595" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75595-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

