+++
type = "question"
title = "Set a relation for buses to circle roundabout before taking exit"
description = '''A traffic sign seen a few times, just now again on a brand new one, where certain vehicles, bus or lorry, is required to circle the roundabout as the shortcut is too tight for these vehicles. They appear well before the shortcut in form of a visual path laid out to take for these. The shortcut I&#x27;ve ...'''
date = "2020-11-11T09:09:00Z"
lastmod = "2020-11-21T18:28:00Z"
weight = 77502
keywords = [ "bus", "roundabout", "shortcut" ]
aliases = [ "/questions/77502" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Set a relation for buses to circle roundabout before taking exit](/questions/77502/set-a-relation-for-buses-to-circle-roundabout-before-taking-exit)

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
<span id="post-77502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77502-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A traffic sign seen a few times, just now again on a brand new one, where certain vehicles, bus or lorry, is required to circle the roundabout as the shortcut is too tight for these vehicles. They appear well before the shortcut in form of a visual path laid out to take for these. The shortcut I've tagged with bus=no already. How can this be expressed in a relation? thx</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-roundabout" rel="tag" title="see questions tagged &#39;roundabout&#39;">roundabout</span> <span class="post-tag tag-link-shortcut" rel="tag" title="see questions tagged &#39;shortcut&#39;">shortcut</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Nov '20, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77502" class="comments-container">
&#10;</div>
<div id="comment-tools-77502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77502-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="77503"></span>

<div id="answer-container-77503" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77503-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use a <a href="https://wiki.openstreetmap.org/wiki/Relation:restriction">restriction relation</a>n where you set the shortcut as role <code>via</code>. But why do you see that being necessary? Isn't the <code>bus=no</code> sufficient?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '20, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-77503" class="comments-container">
<span id="77504"></span>
<div id="comment-77504" class="comment">
<div id="post-77504-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The OSM simulator does not allow to check but for car, bicycle, foot, which do perfect on the shortcut/rotonda mapping introduced a few months ago, even grasps the steps which are still in construction pending railing installation. If able to emulate a bus, I'd be satisfied. Else, the question remains.</p>
</div>
<div id="comment-77504-info" class="comment-info">
<span class="comment-age">(11 Nov '20, 12:15)</span> <span class="comment-user userinfo">SekeRob</span>
</div>
</div>
<span id="77505"></span>
<div id="comment-77505" class="comment">
<div id="post-77505-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>What is "the OSM simulator"?</p>
</div>
<div id="comment-77505-info" class="comment-info">
<span class="comment-age">(11 Nov '20, 13:13)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77503-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77508"></span>

<div id="answer-container-77508" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77508-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The two examples I know of apply to all (motorised?) traffic, such as <a href="https://www.openstreetmap.org/relation/11528691">Madeley Road to Waterloo Street in Ironbridge</a> and <a href="https://www.openstreetmap.org/relation/1320565">Cowley Road to Iffley Road in Oxford</a> and both of these have been handled by standard no left turn restrictions (with via either as way or node), so as TZom suggests in their answer, you could just do similar with mention of restriction:bus as per the wiki documentation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '20, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-77508" class="comments-container">
<span id="77517"></span>
<div id="comment-77517" class="comment">
<div id="post-77517-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thx for the reply. I'll ponder on how to translate this to my current case. Meanwhile, I'll play by making the shortcut temporarily forbidden for cars and then use the simulator to see what route is spat out. I'm hoping it does what I'd expect of some navigator software, find a route. Of course bus / lorry drivers wont experience this as a first and circle around, but just like to dot the eye. cheers</p>
</div>
<div id="comment-77517-info" class="comment-info">
<span class="comment-age">(11 Nov '20, 17:16)</span> <span class="comment-user userinfo">SekeRob</span>
</div>
</div>
</div>
<div id="comment-tools-77508" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77508-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77657"></span>

<div id="answer-container-77657" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77657-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK, so took time to revisit this roundabout to check if any concluding construction work had progressed... nada, as the adjacent ferrovia is still under redesign construction, including galleria segments, the steps are still fenced off. Tested the shortcut specifying no motor-vehicles and low and behold, the cars were rerouted via the roundabout in ID, but with an immediate turn right again via the roundabout, as tight a turn, which is not the prescribed route of looping before taking the turn.</p>
<p>Anyway, now got 3 rotondas with this feature, a sign laying out how a bus, hgv or both are to circle, so bus=no hgv=no only does not work, it has to be a restrictive relation, neither allowing the immediate turn right for buses/hgv via the rotonda. So to lay it out, the restriction already in place for the shortcut with bus/hgv=no on the regular route via the roundabout</p>
<p>1) first a 'no right turn' from &gt; via(way) &gt; to 2) The relation tagged with restriction:bus=no_right_turn, restriction=no_right_turn as per proposal by EdLoach</p>
<p>EdLoach's linked samples got me on the way, will see if the JOSM issue report starts protesting. Suppose I can test this by adding restriction:motorcar=no_right_turn and put from/to in the router to see if the full loop is taken. If not, I'm on my way and close the topic.</p>
<p>Apologies for the verbosity.</p>
<p>Edit: No, router still put it directly right bypassing the shortcut, latter part proper. Will wait a few day to see if router prog needs time to get the new instructions, certainly adding oneway front of station had no immediate effect, that is 6 hours later the ID routing still takes the way against the direction.</p>
<p>TBC.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '20, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77657" class="comments-container">
&#10;</div>
<div id="comment-tools-77657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77657-form-container" class="comment-form-container">
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

