+++
type = "question"
title = "Get node ids with coordinates"
description = '''Hi, I have coordinates where there should be some nodes. Is there a way to get a node id with (lat,long). If that is not possible how to get nodes around some coordinate? I need nodes related to traffic (traffic lights etc.)'''
date = "2020-10-03T19:13:00Z"
lastmod = "2020-10-04T10:09:00Z"
weight = 76931
keywords = [ "nodes", "points" ]
aliases = [ "/questions/76931" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get node ids with coordinates](/questions/76931/get-node-ids-with-coordinates)

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
<span id="post-76931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76931-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have coordinates where there should be some nodes. Is there a way to get a node id with (lat,long). If that is not possible how to get nodes around some coordinate? I need nodes related to traffic (traffic lights etc.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-points" rel="tag" title="see questions tagged &#39;points&#39;">points</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Oct '20, 19:13</strong></p>
<img src="https://secure.gravatar.com/avatar/6373471c5df63c354214795c672c7fae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mico95&#39;s gravatar image" />
<p><span>Mico95</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mico95 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Oct '20, 19:14</strong> </span></p>
</div>
</div>
<div id="comments-container-76931" class="comments-container">
&#10;</div>
<div id="comment-tools-76931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76931-form-container" class="comment-form-container">
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

<span id="76940"></span>

<div id="answer-container-76940" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76940-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could try using the <a href="http://overpass-turbo.eu">overpass-turbo</a> service. In this example</p>
<pre><code>[out:csv(::lat, ::lon)][timeout:25];
// fetch area “Bergamo” to search in
area[name=&quot;Bergamo&quot;][admin_level=&quot;8&quot;]-&gt;.searchArea;
// gather results
(
  // query part for: “highway=traffic_light”
  node[&quot;highway&quot;=&quot;traffic_signals&quot;](area.searchArea);
);
// print results
out;</code></pre>
<p>Finds all the traffic lights in Bergamo and gives an CSV like output containing lat,lon coordinates of the nodes. You could add some more info to the <code>out:csv</code> part (for example <code>::id</code>, <code>name</code>, see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example">Wiki for more examples</a>). You have to just edit the area info. You could also use a bounding box with coordinates</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '20, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/e3dbac44db8deb4b09af6e6df914de1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mannivu&#39;s gravatar image" />
<p><span>Mannivu</span><br />
<span class="score" title="1084 reputation points"><span>1.1k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mannivu has 3 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '20, 10:10</strong> </span></p>
</div>
</div>
<div id="comments-container-76940" class="comments-container">
&#10;</div>
<div id="comment-tools-76940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76940-form-container" class="comment-form-container">
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

