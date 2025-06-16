+++
type = "question"
title = "label rendering errors at Fernvale, Qld, Australia"
description = '''Hi, At this link on the map: https://www.openstreetmap.org/?lat=-27.4395&amp;amp;lon=152.726&amp;amp;zoom=14&amp;amp;layers=M near Fernvale, there are two label oddities:  Bottom left - town label Fernvale appears, but the town is also labelled correctly up to the North East already (where the town is) Top Right...'''
date = "2011-08-25T00:02:00Z"
lastmod = "2011-08-25T01:04:00Z"
weight = 7291
keywords = [ "labels", "rendering", "australia", "mapnik" ]
aliases = [ "/questions/7291" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [label rendering errors at Fernvale, Qld, Australia](/questions/7291/label-rendering-errors-at-fernvale-qld-australia)

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
<span id="post-7291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7291-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, At this link on the map: <a href="https://www.openstreetmap.org/?lat=-27.4395&amp;lon=152.726&amp;zoom=14&amp;layers=M">https://www.openstreetmap.org/?lat=-27.4395&amp;lon=152.726&amp;zoom=14&amp;layers=M</a> near Fernvale, there are two label oddities:</p>
<ol>
<li>Bottom left - town label Fernvale appears, but the town is also labelled correctly up to the North East already (where the town is)</li>
<li>Top Right - Lake Manchester label appears, but the actual lake (and it's label) already appear to the South.</li>
</ol>
<p>Looking in Potlatch I can't see the source of these spurious labels, anyone know what's going on?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-australia" rel="tag" title="see questions tagged &#39;australia&#39;">australia</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '11, 00:02</strong></p>
<img src="https://secure.gravatar.com/avatar/12ac37473087d7d6d667c276a879eec0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chas66&#39;s gravatar image" />
<p><span>chas66</span><br />
<span class="score" title="220 reputation points">220</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chas66 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7291" class="comments-container">
&#10;</div>
<div id="comment-tools-7291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7291-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="7293"></span>

<div id="answer-container-7293" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7293-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="chas66 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Those labels are from admin boundary relations.</p>
<p>Specifically <a href="https://www.openstreetmap.org/browse/relation/96375">relation 96375</a> for Fernvale and <a href="https://www.openstreetmap.org/browse/relation/91460">relation 91460</a> for Lake Manchester. Mapnik shows the label with the name in the centre of the boundary polygon. Both are admin level 10, and appear to be imported from Australian Bureau of Statistics data. I'm don't whether whether these are accurate and tagged correctly etc?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '11, 01:01</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-7293" class="comments-container">
&#10;</div>
<div id="comment-tools-7293" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7293-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7294"></span>

<div id="answer-container-7294" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7294-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect both labels come from the name of administrative boundaries with those names. A search for "Fernvale" and "Lake Manchester" returned both administrative boundaries. The search returns the rough midpoint of the boundary, which is where it will render the name. (I didn't search far enough to find the ID of the boundaries.)</p>
<p>This can be common in Australia, as towns often have administrative boundaries. (The boundaries are generally from an import from the ABS.) If you want to you can make the "place" node that also has the town name part of the admin boundary relation, so that it knows to use that node to display the label.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '11, 01:02</strong></p>
<img src="https://secure.gravatar.com/avatar/f075add936ab95d2d368f2e48f5ddc22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ebenezer&#39;s gravatar image" />
<p><span>Ebenezer</span><br />
<span class="score" title="948 reputation points">948</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ebenezer has 2 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-7294" class="comments-container">
<span id="7295"></span>
<div id="comment-7295" class="comment">
<div id="post-7295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>e.g. Lake Manchester admin boundary <a href="https://www.openstreetmap.org/?relation=91460">https://www.openstreetmap.org/?relation=91460</a> and Fernvale admin boundary <a href="https://www.openstreetmap.org/?relation=96375">https://www.openstreetmap.org/?relation=96375</a></p>
</div>
<div id="comment-7295-info" class="comment-info">
<span class="comment-age">(25 Aug '11, 01:04)</span> <span class="comment-user userinfo">Ebenezer</span>
</div>
</div>
</div>
<div id="comment-tools-7294" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7294-form-container" class="comment-form-container">
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

