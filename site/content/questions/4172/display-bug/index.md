+++
type = "question"
title = "Display Bug?"
description = '''I have moved a building a little (before it was at the center of the park): http://www.openstreetmap.org/edit?lat=48.573497&amp;amp;lon=39.30047&amp;amp;zoom=18 But now it looks strange at the map: http://www.openstreetmap.org/?minlon=39.2995921&amp;amp;minlat=48.5726449&amp;amp;maxlon=39.301347&amp;amp;maxlat=48.57434...'''
date = "2011-03-29T10:00:00Z"
lastmod = "2011-03-29T10:12:00Z"
weight = 4172
keywords = [ "building", "editing", "bug" ]
aliases = [ "/questions/4172" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Display Bug?](/questions/4172/display-bug)

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
<span id="post-4172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4172-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have moved a building a little (before it was at the center of the park): <a href="http://www.openstreetmap.org/edit?lat=48.573497&amp;lon=39.30047&amp;zoom=18">http://www.openstreetmap.org/edit?lat=48.573497&amp;lon=39.30047&amp;zoom=18</a></p>
<p>But now it looks strange at the map: <a href="http://www.openstreetmap.org/?minlon=39.2995921&amp;minlat=48.5726449&amp;maxlon=39.301347&amp;maxlat=48.5743492&amp;box=yes">http://www.openstreetmap.org/?minlon=39.2995921&amp;minlat=48.5726449&amp;maxlon=39.301347&amp;maxlat=48.5743492&amp;box=yes</a></p>
<p>Why does it look correct in edit mode and wrong in display mode?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '11, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/d6cfeb2638841c642f9dfd3b326e9c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YuriLL&#39;s gravatar image" />
<p><span>YuriLL</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YuriLL has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '11, 10:05</strong> </span></p>
</div>
</div>
<div id="comments-container-4172" class="comments-container">
&#10;</div>
<div id="comment-tools-4172" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4172-form-container" class="comment-form-container">
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

<span id="4173"></span>

<div id="answer-container-4173" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4173-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="YuriLL has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It takes a while for the map to get rendered (minutes, hours or even days).</p>
<p>The map is built up of tiles, and sometimes the border of two tiles happen to cross the object one just have edited. If one tile is rendered with the new data, but then adjacent tile isn't - yet, there will be artifacts like the one you have linked to. One just have to wait and the problem will go away when all tiles covering the object have been rendered.</p>
<p>Tiles of different zoom levels are rendered at different times, so if you zoom out you will find that there are levels where the building looks OK.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '11, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-4173" class="comments-container">
&#10;</div>
<div id="comment-tools-4173" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4173-form-container" class="comment-form-container">
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

