+++
type = "question"
title = "Polygons not rendering after removing them from multipolygon"
description = '''Hi, I have some problems here. Some time ago I had a big relation of polygons and multipolygons. I&#x27;ve splited it up by removing all forests from relation and then I&#x27;ve removed that relation too. Now some of these polygons can&#x27;t show on the map. At my example you can see one polygon visible. I edited...'''
date = "2012-08-14T15:03:00Z"
lastmod = "2012-08-15T20:19:00Z"
weight = 15074
keywords = [ "relations", "multipolygon" ]
aliases = [ "/questions/15074" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Polygons not rendering after removing them from multipolygon](/questions/15074/polygons-not-rendering-after-removing-them-from-multipolygon)

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
<span id="post-15074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15074-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have some problems <a href="https://www.openstreetmap.org/?lat=49.395441&amp;lon=22.075842&amp;zoom=18&amp;layers=M">here</a>. Some time ago I had a big relation of polygons and multipolygons. I've splited it up by removing all forests from relation and then I've removed that relation too. Now some of these polygons can't show on the map. At my example you can see one polygon visible. I edited it by moving one of its nodes by few millimeters and submited tile for rendering. Is it a bug?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '12, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/49c537c99e134afabb80351195e07ac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrzej_aa&#39;s gravatar image" />
<p><span>andrzej_aa</span><br />
<span class="score" title="24 reputation points">24</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrzej_aa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '12, 15:04</strong> </span></p>
</div>
</div>
<div id="comments-container-15074" class="comments-container">
&#10;</div>
<div id="comment-tools-15074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15074-form-container" class="comment-form-container">
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

<span id="15112"></span>

<div id="answer-container-15112" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15112-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sounds like a bug. In the rendering tools chain, the concerned is <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pqsql</a>. You should open a ticket on the <a href="https://trac.openstreetmap.org/">OSM bug report system</a> and provide your example.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '12, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-15112" class="comments-container">
<span id="15122"></span>
<div id="comment-15122" class="comment">
<div id="post-15122-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, done.</p>
</div>
<div id="comment-15122-info" class="comment-info">
<span class="comment-age">(15 Aug '12, 20:19)</span> <span class="comment-user userinfo">andrzej_aa</span>
</div>
</div>
</div>
<div id="comment-tools-15112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15112-form-container" class="comment-form-container">
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

