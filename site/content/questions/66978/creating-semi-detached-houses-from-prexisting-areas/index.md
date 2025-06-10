+++
type = "question"
title = "Creating semi-detached houses from prexisting areas."
description = '''Hi, When creating semi-detached housing from already existing building outlines what is the best way to proceed? One option is to delete the area and then draw 2 semi-detached buildings in its place. Another is to edit the area and then split it to form the 2 semi-detached buildings. The last option...'''
date = "2018-11-28T21:34:00Z"
lastmod = "2018-11-29T03:33:00Z"
weight = 66978
keywords = [ "edit", "house", "history", "newbie", "josm" ]
aliases = [ "/questions/66978" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Creating semi-detached houses from prexisting areas.](/questions/66978/creating-semi-detached-houses-from-prexisting-areas)

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
<span id="post-66978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66978-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>When creating semi-detached housing from already existing building outlines what is the best way to proceed?</p>
<p>One option is to delete the area and then draw 2 semi-detached buildings in its place. Another is to edit the area and then split it to form the 2 semi-detached buildings. The last option is to copy the history (Ctrl+Shift+G in JOSM) from the original building and then paste this to one of the semi-detached buildings (I believe that the problem here though is that not both new buildings can have the same history).</p>
<p>Please could you advise on what would be optimal?</p>
<p>Many thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-edit" rel="tag" title="see questions tagged &#39;edit&#39;">edit</span> <span class="post-tag tag-link-house" rel="tag" title="see questions tagged &#39;house&#39;">house</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Nov '18, 21:34</strong></p>
<img src="https://secure.gravatar.com/avatar/868334818a6fe6b564060bdca905d9ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Charnia&#39;s gravatar image" />
<p><span>Charnia</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Charnia has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66978" class="comments-container">
&#10;</div>
<div id="comment-tools-66978" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66978-form-container" class="comment-form-container">
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

<span id="66979"></span>

<div id="answer-container-66979" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66979-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know if it's optimal, but if the outline is very simple, I find the <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Terracer">Terracer</a> plugin to be quite quick and easy. I'm not sure which of the resulting row gets the history though. Terracer ones also have the options to keep the outline way, which keeps the history spread across all of them, but as far as I'm aware it isn't particularly common to leave the outline tagged as a terrace with the individually dwellings as building:part=*.</p>
<p>If the outline is more complicated, I normally find it easiest to add nodes at the split line and Alt+X to split the building at those points.</p>
<p>Unfortunately I know of no way to share history between objects, I think this is a limitation of the data structure.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '18, 22:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-66979" class="comments-container">
&#10;</div>
<div id="comment-tools-66979" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66979-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66982"></span>

<div id="answer-container-66982" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66982-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My tendency would be to reuse the existing building for one of the objects (somehow or another). But I wouldn't worry too much about the object history, as any interesting analysis of history is going to have to deal with the tens of millions of objects that are edited without considering object history, probably by interpreting the data at points in time and comparing the points in time rather than object versions.</p>
<p>(another thing that confounds a simple object history analysis is that nodes of a way can be moved, which doesn't directly register in the way history)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '18, 03:33</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-66982" class="comments-container">
&#10;</div>
<div id="comment-tools-66982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66982-form-container" class="comment-form-container">
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

