+++
type = "question"
title = "Overpass: Erase Bbox"
description = '''Is it possible to make advanced spatial queries like erase a bbox from a polygon query? So that you get a polygon-query with a hole in it? As far as I know, it&#x27;s just possible to union different bboxs, so you get a kind of ring-query.'''
date = "2013-02-13T14:29:00Z"
lastmod = "2014-07-26T22:54:00Z"
weight = 19913
keywords = [ "overpass", "erase", "bbox", "query" ]
aliases = [ "/questions/19913" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: Erase Bbox](/questions/19913/overpass-erase-bbox)

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
<span id="post-19913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19913-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to make advanced spatial queries like erase a bbox from a polygon query? So that you get a polygon-query with a hole in it? As far as I know, it's just possible to union different bboxs, so you get a kind of ring-query.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-erase" rel="tag" title="see questions tagged &#39;erase&#39;">erase</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '13, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/2c52393df51ceb5327c1e19e3b0efbfe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mattes_tili&#39;s gravatar image" />
<p><span>Mattes_tili</span><br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mattes_tili has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '13, 14:30</strong> </span></p>
</div>
</div>
<div id="comments-container-19913" class="comments-container">
&#10;</div>
<div id="comment-tools-19913" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19913-form-container" class="comment-form-container">
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

<span id="19926"></span>

<div id="answer-container-19926" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19926-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-19926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mattes_tili has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, the unions are all that is possible at the moment. But you can use union also on <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_Polygon">polygon queries</a> which allows in principle an arbitrary geometry by stitching polygons.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '13, 12:50</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-19926" class="comments-container">
<span id="35230"></span>
<div id="comment-35230" class="comment">
<div id="post-35230-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Meanwhile this could be solved by the difference operator. See the other answer to this question.</p>
</div>
<div id="comment-35230-info" class="comment-info">
<span class="comment-age">(26 Jul '14, 22:54)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-19926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19926-form-container" class="comment-form-container">
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

