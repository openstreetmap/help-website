+++
type = "question"
title = "Turn Restrictions for Oneway Streets and Dead Ends"
description = '''can someone help me how to do turn Restrictions on junctions one one way streets and is there can be added to make a road a dead end (cul-de-sac) '''
date = "2011-08-14T08:52:00Z"
lastmod = "2011-08-15T00:55:00Z"
weight = 7078
keywords = [ "turn_restrictions" ]
aliases = [ "/questions/7078" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Turn Restrictions for Oneway Streets and Dead Ends](/questions/7078/turn-restrictions-for-oneway-streets-and-dead-ends)

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
<span id="post-7078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7078-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>can someone help me how to do turn Restrictions on junctions one one way streets and is there can be added to make a road a dead end (cul-de-sac)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '11, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/7264e11bcea28695deb701b17fdbf7b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="darrenrobert&#39;s gravatar image" />
<p><span>darrenrobert</span><br />
<span class="score" title="73 reputation points">73</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="darrenrobert has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '11, 10:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-7078" class="comments-container">
&#10;</div>
<div id="comment-tools-7078" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7078-form-container" class="comment-form-container">
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

<span id="7079"></span>

<div id="answer-container-7079" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7079-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-7079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is not necessary to add turn restrictions on one-way streets. Simply adding the tag <code>oneway=yes</code> will implicitly create all the relevant turn restrictions. It is the responsibility of data consumers (routing software, in this case) to generate turn restrictions if these are required <strong>within</strong> the application. All software that I am aware of seems to do this successfully.</p>
<p>Obviously there may be exceptional cases (for instance a street crossing a one-way street with straight-on only restrictions), but these can be handled in the normal way by creating turn restrictions.</p>
<p>Roads which are dead-ends again can be detected as such by application software, and there is no need for any explicit tag. However, a tag does exist noexit=yes for this purpose. It is frequently used to tag streets (ways) where a complete survey has not been done, but a no exit sign exists at the entrance to the street.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '11, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-7079" class="comments-container">
<span id="7084"></span>
<div id="comment-7084" class="comment">
<div id="post-7084-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>some roads got no right turn or left turn, how do i add tham on the map</p>
</div>
<div id="comment-7084-info" class="comment-info">
<span class="comment-age">(14 Aug '11, 15:32)</span> <span class="comment-user userinfo">darrenrobert</span>
</div>
</div>
</div>
<div id="comment-tools-7079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7079-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7094"></span>

<div id="answer-container-7094" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7094-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If it is obvious (no turning to one way street) it not necessary to map it. The easiest way to create turn restrictions is registering in <a href="http://cloudmade.com">cloudmade.com</a> and using their editor Mapzen. You just click a node and it gives you a small GUI with a car to click where the car can drive - easy, intuitive, fast.<br />
Otherwise it is done with relations and adding the individual streets as roles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '11, 00:55</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-7094" class="comments-container">
&#10;</div>
<div id="comment-tools-7094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7094-form-container" class="comment-form-container">
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

