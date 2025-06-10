+++
type = "question"
title = "identifying POIS along a street"
description = '''Thank you team! Your response has always been useful for me. Please still on my ongoing project. I have successfully written a code to retrieve intersections along a given street. But the stage I am now is identifying points of interest e.g restaurant, along the street. For example, let&#x27;s say in a p...'''
date = "2022-02-14T15:23:00Z"
lastmod = "2022-02-15T15:36:00Z"
weight = 83471
keywords = [ "node" ]
aliases = [ "/questions/83471" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [identifying POIS along a street](/questions/83471/identifying-pois-along-a-street)

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
<span id="post-83471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83471-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Thank you team! Your response has always been useful for me. Please still on my ongoing project. I have successfully written a code to retrieve intersections along a given street. But the stage I am now is identifying points of interest e.g restaurant, along the street. For example, let's say in a particular area A, we have street X and Street Y. My aim is to identify all the restaurants in Street X and arrange them in order that they are in real life. So when a user is moving from point P1 to point P2 on street X, I want the user to know if he has reached a restaurant, or an intersection as he progresses on the journey towards P2. How do i get this done? I can extract intersections separately and i can also extract restaurants separately, but I do not know how to merge them and arrange them in the order that they are appear in reality on the map. Please I need your suggestions.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Feb '22, 15:23</strong></p>
<img src="https://secure.gravatar.com/avatar/d91bc4f974e22ffeb60227442e03aafa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Segunlakata&#39;s gravatar image" />
<p><span>Segunlakata</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Segunlakata has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83471" class="comments-container">
&#10;</div>
<div id="comment-tools-83471" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83471-form-container" class="comment-form-container">
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

<span id="83487"></span>

<div id="answer-container-83487" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83487-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You seem to be wanting something like a 1-D map. I wrote a <a href="http://sk53-osm.blogspot.com/2018/04/linear-or-1d-maps-from-openstreetmap.html">blog post</a> about one approach a few years ago, and very recently Robert Whittaker has implemented <a href="https://osm.mathmos.net/linear/">something rather similar</a>. In both cases I suspect that we use PostGIS to do all the hard work because it needs a range of geospatial operations such as ST_ShortestLine. You may find some ideas in my post.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '22, 15:36</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-83487" class="comments-container">
&#10;</div>
<div id="comment-tools-83487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83487-form-container" class="comment-form-container">
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

