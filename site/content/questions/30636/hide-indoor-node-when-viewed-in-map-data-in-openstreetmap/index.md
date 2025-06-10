+++
type = "question"
title = "hide indoor node when viewed in map data in openstreetmap"
description = ''' Greetings. I am still new in Openstreetmap. Currently i am drawing an indoor map using JOSM for my final year project. The problem is when i view the map data of my faculty in openstreetmap. it shows all the nodes. I cant understand why it shows. It suppose to show like this from this link  can any...'''
date = "2014-02-11T12:46:00Z"
lastmod = "2014-02-16T15:36:00Z"
weight = 30636
keywords = [ "josm", "nodes", "indoor" ]
aliases = [ "/questions/30636" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [hide indoor node when viewed in map data in openstreetmap](/questions/30636/hide-indoor-node-when-viewed-in-map-data-in-openstreetmap)

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
<span id="post-30636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30636-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><img src="http://help.openstreetmap.org/upfiles/nodes_OSM.JPG" alt="alt text" /></p>
<p>Greetings. I am still new in Openstreetmap. Currently i am drawing an indoor map using JOSM for my final year project. The problem is when i view the map data of my faculty in openstreetmap. it shows all the nodes. I cant understand why it shows. It suppose to show like this from <a href="http://www.openstreetmap.org/node/2100509693#map=19/46.25549/-63.13784&amp;layers=D">this link</a></p>
<p>can anyone share with me on how to fix this matter?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '14, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/fa67c029cb445775d328af8be7e8ddcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="firdaus%20shajahan&#39;s gravatar image" />
<p><span>firdaus shaj...</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="firdaus shajahan has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-30636" class="comments-container">
<span id="30643"></span>
<div id="comment-30643" class="comment">
<div id="post-30643-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I do not understand why the data view should not show all nodes in the database. Can you explain?</p>
</div>
<div id="comment-30643-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 14:30)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="30644"></span>
<div id="comment-30644" class="comment">
<div id="post-30644-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@aseerel4c26</span> Usually it doesn't show untagged nodes that are part of a way.</p>
</div>
<div id="comment-30644-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 14:54)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30636" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30636-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="30641"></span>

<div id="answer-container-30641" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30641-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-30641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You've added the nodes to the <a href="http://www.openstreetmap.org/relation/3505091">relation you have created</a> with a role of buildingpart. I don't understand what a level relation is, but you probably don't need to include every node as well as every way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '14, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-30641" class="comments-container">
&#10;</div>
<div id="comment-tools-30641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30641-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30639"></span>

<div id="answer-container-30639" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30639-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Could you provide a link to your indoor map ? It seems the "Map Data" layer is highlighting nodes when they carry some tags (many nodes have no tags or ordinary tags like "source=<em>" or "edited_by=</em>") or when they are parts of one or more relations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '14, 13:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Feb '14, 14:06</strong> </span></p>
</div>
</div>
<div id="comments-container-30639" class="comments-container">
<span id="30659"></span>
<div id="comment-30659" class="comment">
<div id="post-30659-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this is the link <a href="http://www.openstreetmap.org/#map=19/3.25402/101.72974&amp;layers=D">http://www.openstreetmap.org/#map=19/3.25402/101.72974&amp;layers=D</a></p>
</div>
<div id="comment-30659-info" class="comment-info">
<span class="comment-age">(12 Feb '14, 00:42)</span> <span class="comment-user userinfo">firdaus shaj...</span>
</div>
</div>
</div>
<div id="comment-tools-30639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30639-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30761"></span>

<div id="answer-container-30761" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30761-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Its ok guys i managed to fix it. The problem is when i create node and close it. I need to make sure to highlight the closed node and then tag it</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '14, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/fa67c029cb445775d328af8be7e8ddcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="firdaus%20shajahan&#39;s gravatar image" />
<p><span>firdaus shaj...</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="firdaus shajahan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30761" class="comments-container">
<span id="30768"></span>
<div id="comment-30768" class="comment">
<div id="post-30768-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>can you explain, what you mean by "close" a node? And what means "highlight"?</p>
</div>
<div id="comment-30768-info" class="comment-info">
<span class="comment-age">(16 Feb '14, 15:36)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30761-form-container" class="comment-form-container">
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

