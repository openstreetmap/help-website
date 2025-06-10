+++
type = "question"
title = "Handle turn restriction with same from and to way"
description = '''I&#x27;m experimenting with my own routing system and have encountered a weird situation that I don&#x27;t know how to handle. Basically, an only straight on turn restriction in which the from and to ways are identical (the way is a 2 way trunk), you can find the relation here: https://www.openstreetmap.org/r...'''
date = "2021-05-18T18:02:00Z"
lastmod = "2021-05-19T18:20:00Z"
weight = 80224
keywords = [ "turn_restrictions", "routing" ]
aliases = [ "/questions/80224" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Handle turn restriction with same from and to way](/questions/80224/handle-turn-restriction-with-same-from-and-to-way)

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
<span id="post-80224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80224-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm experimenting with my own routing system and have encountered a weird situation that I don't know how to handle.</p>
<p>Basically, an only straight on turn restriction in which the from and to ways are identical (the way is a 2 way trunk), you can find the relation here: <a href="https://www.openstreetmap.org/relation/6381739">https://www.openstreetmap.org/relation/6381739</a></p>
<p>I understand that the relation is attempting to prevent the user from getting onto the east bound service road when travelling west bound on the trunk road. But the mandatory restriction is preventing my routing engine from entering the service road when coming from the west (which it should be able to do).</p>
<p>What is the correct way to handle this?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 May '21, 18:02</strong></p>
<img src="https://secure.gravatar.com/avatar/62d4beafa99dc707da2a400597901681?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Walter&#39;s gravatar image" />
<p><span>Walter</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Walter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80224" class="comments-container">
<span id="80225"></span>
<div id="comment-80225" class="comment">
<div id="post-80225-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The turn restriction is incorrectly mapped. To avoid ambiguity the from and to ways need to terminate at the via node. The way should have been split. This is also <a href="https://wiki.openstreetmap.org/wiki/Relation:restriction#cite_note-waysplit-2">documented on the wiki</a> (albeit only in a footnote).</p>
<p>I have no clue if there is any meaningful way to resolve the ambiguous turn restriction in the router. Maybe you should just ignore such wrong restrictions. On the other hand <a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=-33.18351%2C20.79298%3B-33.18337%2C20.79313">Graphhopper seems to have found a way to interpret the situation correctly</a>.</p>
</div>
<div id="comment-80225-info" class="comment-info">
<span class="comment-age">(18 May '21, 21:09)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-80224" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80224-form-container" class="comment-form-container">
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

<span id="80230"></span>

<div id="answer-container-80230" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80230-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As per TZorn and <a href="https://ahorn.lima-city.de/tr/">https://ahorn.lima-city.de/tr/</a> which appears to show that there are issues with these restrictions, I'll be simply disregarding restrictions that have the same from and to way when building the routing network.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 May '21, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/62d4beafa99dc707da2a400597901681?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Walter&#39;s gravatar image" />
<p><span>Walter</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Walter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80230" class="comments-container">
&#10;</div>
<div id="comment-tools-80230" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80230-form-container" class="comment-form-container">
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

