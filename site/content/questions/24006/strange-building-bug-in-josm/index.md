+++
type = "question"
title = "Strange building bug in JOSM"
description = '''I don&#x27;t know if this is the right place to report it but anyway... I have encountered this bug several times. It happens when I combine several building segments into one. Suddenly one or more of the ways flies away in one of the directions of the building. Screenshots: Before combining: Before comb...'''
date = "2013-07-05T10:58:00Z"
lastmod = "2013-07-05T12:52:00Z"
weight = 24006
keywords = [ "building", "josm", "buildingtools" ]
aliases = [ "/questions/24006" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Strange building bug in JOSM](/questions/24006/strange-building-bug-in-josm)

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
<span id="post-24006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24006-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I don't know if this is the right place to report it but anyway...</p>
<p>I have encountered this bug several times. It happens when I combine several building segments into one. Suddenly one or more of the ways flies away in one of the directions of the building.</p>
<p>Screenshots: Before combining:<img src="http://i408.photobucket.com/albums/pp169/Grillmannen/husbuggutzoomad_zps3bd4bccc.png" title="Before combining" alt="Before combining" /> Before combining, zoomed in:<img src="http://i408.photobucket.com/albums/pp169/Grillmannen/husbugginzoomad_zps8afe67a6.png" title="Before combining, zoomed in" alt="Before combining, zoomed in" /> After combining ( :O ):<img src="http://i408.photobucket.com/albums/pp169/Grillmannen/husbuggefterhopslagning_zpsf2af6559.png" title="After combining" alt="After combining" /> After combining, zoomed in:<img src="http://i408.photobucket.com/albums/pp169/Grillmannen/husbuggefterhopslagninginzoomad_zps312cb50f.png" title="After combining, zoomed in" alt="After combining, zoomed in" /></p>
<p>What causes this bug, and how can I avoid it? I'm using the building tools plugin, and usually draw the seperate parts of the building with one of the marked so it follows the same angle. From what I have collected, it might have to do with some node going a bit out of the completed polygon, if that makes sense. The bug seems crazy anyway though...</p>
<p>PS: Made a bug request myself as well: <a href="http://josm.openstreetmap.de/ticket/8851#ticket%20bug">bug</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-buildingtools" rel="tag" title="see questions tagged &#39;buildingtools&#39;">buildingtools</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jul '13, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/0210a545c865c5db5159bb059fe343d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grillo&#39;s gravatar image" />
<p><span>Grillo</span><br />
<span class="score" title="345 reputation points">345</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grillo has one accepted answer">25%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '13, 11:10</strong> </span></p>
</div>
</div>
<div id="comments-container-24006" class="comments-container">
&#10;</div>
<div id="comment-tools-24006" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24006-form-container" class="comment-form-container">
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

<span id="24012"></span>

<div id="answer-container-24012" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24012-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the JOSM "combine" feature works fine only when polygons are strictly adjacent, mean not overlapping or nodes not joined to the nearest way. More than a screenshot, your bug report should provide an XML file ('save as' in JOSM) of the building blocks you want to combine (e.g. copy them to a new layout and save). This will be used as a test dataset for the developers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '13, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '13, 12:53</strong> </span></p>
</div>
</div>
<div id="comments-container-24012" class="comments-container">
&#10;</div>
<div id="comment-tools-24012" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24012-form-container" class="comment-form-container">
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

