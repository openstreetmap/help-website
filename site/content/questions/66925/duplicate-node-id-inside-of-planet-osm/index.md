+++
type = "question"
title = "Duplicate Node ID inside of planet OSM"
description = '''I have a recent planet pbf and am finding duplicate node Ids in some regions. Can someone explain to me why this is happening?  The duplicates always have different versions and changeset_ids. One of the duplicates (not always the newest or oldest) always has empty lat long data. What is going on? W...'''
date = "2018-11-26T22:53:00Z"
lastmod = "2018-11-27T19:26:00Z"
weight = 66925
keywords = [ "planet", "node", "duplicate", "osmosis" ]
aliases = [ "/questions/66925" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Duplicate Node ID inside of planet OSM](/questions/66925/duplicate-node-id-inside-of-planet-osm)

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
<span id="post-66925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66925-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a recent planet pbf and am finding duplicate node Ids in some regions. Can someone explain to me why this is happening? The duplicates always have different versions and changeset_ids. One of the duplicates (not always the newest or oldest) always has empty lat long data. What is going on? Why do these null rows not show up in a PGSnapShot load? What are these artifacts of? They don't seem numerous enough to be any sort of actual change history.</p>
<p>Example: id version user_id tstamp changeset_id</p>
<p>77875 2 131476 2009-07-08 14:52:45.0000000 1776041 Has lat long data</p>
<p>77875 51 1227748 2017-12-11 08:43:34.0000000 54543387 Has empty lat long data</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '18, 22:53</strong></p>
<img src="https://secure.gravatar.com/avatar/12e3b9b18bd7f3676c7be93c4cfe7d7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bwoods&#39;s gravatar image" />
<p><span>bwoods</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bwoods has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66925" class="comments-container">
&#10;</div>
<div id="comment-tools-66925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66925-form-container" class="comment-form-container">
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

<span id="66927"></span>

<div id="answer-container-66927" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66927-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bwoods has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't have duplicate node IDs. You have a node ID in the first line, and a relation id in the second line.</p>
<p>Each OSM object type (nodes, ways, relations) has its own number range. Node #77875 has nothing to do with relation #77875.</p>
<p>Apparently you are mis-interpreting a relation as a node; little surprise, then, that the relation has no latitude and longitude.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Nov '18, 00:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-66927" class="comments-container">
<span id="66929"></span>
<div id="comment-66929" class="comment">
<div id="post-66929-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Right you are. My SqlServer port of osmosis was writing relations to the wrong table sometimes. Good catch, thank you.</p>
</div>
<div id="comment-66929-info" class="comment-info">
<span class="comment-age">(27 Nov '18, 01:03)</span> <span class="comment-user userinfo">bwoods</span>
</div>
</div>
<span id="66939"></span>
<div id="comment-66939" class="comment">
<div id="post-66939-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15961/bwoods">@bwoods</a>: meta: Please could you <a href="/questions/34318/how-to-mark-an-answer-as-accepted-and-mark-my-question-as-answered">mark an answer as accepted</a> if it solves your problem.</p>
</div>
<div id="comment-66939-info" class="comment-info">
<span class="comment-age">(27 Nov '18, 19:26)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66927-form-container" class="comment-form-container">
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

