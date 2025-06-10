+++
type = "question"
title = "Download orientation of the streets"
description = '''Hi, I would like to know if it is possible to obtain information on the orientation of the streets when downloading an .osm file. That is, when opening the &#x27;lines&#x27; file in QGIS (from the .osm file) there is a column that indicates if street A has a south-north direction, street B northeast-southwest...'''
date = "2021-05-20T05:08:00Z"
lastmod = "2021-05-20T19:38:00Z"
weight = 80236
keywords = [ "direction", "orientation" ]
aliases = [ "/questions/80236" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Download orientation of the streets](/questions/80236/download-orientation-of-the-streets)

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
<span id="post-80236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80236-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I would like to know if it is possible to obtain information on the orientation of the streets when downloading an .osm file. That is, when opening the 'lines' file in QGIS (from the .osm file) there is a column that indicates if street A has a south-north direction, street B northeast-southwest, etc (or something similar). I was checking webpages that use info from OSM - as brouter.de, which are really interesting but I want to use this information to solve a Vehicle routing problem (many package delivery points from a warehouse) and they are not useful in a case like this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-direction" rel="tag" title="see questions tagged &#39;direction&#39;">direction</span> <span class="post-tag tag-link-orientation" rel="tag" title="see questions tagged &#39;orientation&#39;">orientation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '21, 05:08</strong></p>
<img src="https://secure.gravatar.com/avatar/bd9a4b44e9bad118f049b51e818555e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="puertodormido&#39;s gravatar image" />
<p><span>puertodormido</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="puertodormido has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80236" class="comments-container">
<span id="80239"></span>
<div id="comment-80239" class="comment">
<div id="post-80239-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to note that what I'm trying to get is the orientation and the direction in what the vehicles are allowed to move.</p>
</div>
<div id="comment-80239-info" class="comment-info">
<span class="comment-age">(20 May '21, 10:15)</span> <span class="comment-user userinfo">puertodormido</span>
</div>
</div>
</div>
<div id="comment-tools-80236" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80236-form-container" class="comment-form-container">
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

<span id="80238"></span>

<div id="answer-container-80238" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80238-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>you can use Qgis field calculator:</p>
<pre><code>round((atan( (yat(0) - yat( -1 ))/(xat(0) - xat( -1 ))))/$pi * 180)</code></pre>
<p>This will return angle of line in degrees at its termini.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '21, 10:08</strong></p>
<img src="https://secure.gravatar.com/avatar/d33efa30f05d8f3604e7210c48b24a8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cascafico&#39;s gravatar image" />
<p><span>Cascafico</span><br />
<span class="score" title="283 reputation points">283</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cascafico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80238" class="comments-container">
<span id="80240"></span>
<div id="comment-80240" class="comment">
<div id="post-80240-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I did not explain myself completely. What I want is the direction in what vehicles are allowed to move.</p>
</div>
<div id="comment-80240-info" class="comment-info">
<span class="comment-age">(20 May '21, 10:16)</span> <span class="comment-user userinfo">puertodormido</span>
</div>
</div>
<span id="80242"></span>
<div id="comment-80242" class="comment">
<div id="post-80242-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Vehicles can generally only travel in the same direction as the linear road, so the above angle would give you that information. Maybe you need to tell us more about what your end goal is?</p>
</div>
<div id="comment-80242-info" class="comment-info">
<span class="comment-age">(20 May '21, 17:36)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="80245"></span>
<div id="comment-80245" class="comment">
<div id="post-80245-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, we have twoway (no tag or <code>oneway=yes</code>) and oneway (<code>oneway=yes</code> or <code>oneway=-1</code>) roads in OSM.</p>
</div>
<div id="comment-80245-info" class="comment-info">
<span class="comment-age">(20 May '21, 19:38)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-80238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80238-form-container" class="comment-form-container">
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

