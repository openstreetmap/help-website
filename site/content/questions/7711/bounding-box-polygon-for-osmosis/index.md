+++
type = "question"
title = "bounding-box polygon for osmosis"
description = '''Hi, I would like to ask if somebody knows some way, software or an algorithm which can expands existing downloaded polygon in *.poly file.  I mean I would like to move each node of the polygon more outside to create bigger polygon area.  Thank in advance'''
date = "2011-09-07T11:52:00Z"
lastmod = "2011-09-09T08:30:00Z"
weight = 7711
keywords = [ "extract", "polygon", "osmosis", "software" ]
aliases = [ "/questions/7711" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [bounding-box polygon for osmosis](/questions/7711/bounding-box-polygon-for-osmosis)

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
<span id="post-7711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7711-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I would like to ask if somebody knows some way, software or an algorithm which can expands existing downloaded polygon in *.poly file.</p>
<p>I mean I would like to move each node of the polygon more outside to create bigger polygon area.</p>
<p>Thank in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-software" rel="tag" title="see questions tagged &#39;software&#39;">software</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Sep '11, 11:52</strong></p>
<img src="https://secure.gravatar.com/avatar/e8343c2fdfd08fea47ea8a0dc5210607?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MrX1&#39;s gravatar image" />
<p><span>MrX1</span><br />
<span class="score" title="46 reputation points">46</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MrX1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7711" class="comments-container">
&#10;</div>
<div id="comment-tools-7711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7711-form-container" class="comment-form-container">
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

<span id="7747"></span>

<div id="answer-container-7747" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7747-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you are (probably) looking for is a <a href="http://stackoverflow.com/questions/1109536/an-algorithm-for-inflating-deflating-offsetting-buffering-polygons">polygon buffer</a>. There are various tools which generate buffers. Some of them:</p>
<ul>
<li>PostGIS has a <a href="http://www.postgis.org/documentation/manual-svn/ST_Buffer.html-">ST_Buffer</a> function</li>
<li>JTS also provides buffering functions: <a href="http://lin-ear-th-inking.blogspot.com/2008/10/improvements-to-jts-buffering.html">http://lin-ear-th-inking.blogspot.com/2008/10/improvements-to-jts-buffering.html</a></li>
</ul>
<p>I'm not sure they directly support .poly files, though. You will probably need to transform .poly to something these tools can work with.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '11, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-7747" class="comments-container">
&#10;</div>
<div id="comment-tools-7747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7747-form-container" class="comment-form-container">
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

