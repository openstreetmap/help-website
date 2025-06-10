+++
type = "question"
title = "Bus routes that travel back and forth"
description = '''If a bus route travels back and forth between two places (sometimes taking a different route slightly in one direction, if it enters a one-way area, for example), should there just be one relation for the entire route from A to B to A? And, additionally, should the same relation be added to a way tw...'''
date = "2013-10-16T00:37:00Z"
lastmod = "2013-10-26T14:02:00Z"
weight = 27213
keywords = [ "ways", "bus", "route", "relations" ]
aliases = [ "/questions/27213" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bus routes that travel back and forth](/questions/27213/bus-routes-that-travel-back-and-forth)

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
<span id="post-27213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27213-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If a bus route travels back and forth between two places (sometimes taking a different route slightly in one direction, if it enters a one-way area, for example), should there just be one relation for the entire route from A to B to A? And, additionally, should the same relation be added to a way twice, for each direction, on the ways in which the route is travelled on in both directions (or for every individual time the route goes through a particular way)?</p>
<p>Also, here's an example of where a bus route might go: <a href="https://www.google.com/maps/preview#!data=!4m30!3m29!1m4!3m2!3d51.218923!4d-0.171564!6e2!1m4!3m2!3d51.2166314!4d-0.1708344!6e2!2e0!3m8!1m3!1d3016!2d-0.1685492!3d51.2185836!3m2!1i944!2i927!4f13.1!6m2!1m1!1e4!9m5!2m2!3d51.2188785!4d-0.1646564!3s0x4875fadfb3cda86b%3A0x386d1543a2c1e773!4f0.6890935&amp;fid=0">Example route</a></p>
<p>In this case, the bus travels south on the A23, turns left on to Three Arch Road, and travels to East Surrey Hospital (Canada Avenue), where it makes a small loop, where it travels back along Three Arch Road, and then continues further south in the direction of Gatwick Airport. If the bus is to then return back and again, enter the hospital, i.e. if it stops at the hospital from either direction, it will mean Three Arch Road is used by the route 4 times, therefore, should there be 4 entries of the same relation?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '13, 00:37</strong></p>
<img src="https://secure.gravatar.com/avatar/6035647123b433de9d9aaa4259d07e8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheUltimateKoopa&#39;s gravatar image" />
<p><span>TheUltimateK...</span><br />
<span class="score" title="161 reputation points">161</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheUltimateKoopa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Oct '13, 01:00</strong> </span></p>
</div>
</div>
<div id="comments-container-27213" class="comments-container">
<span id="27510"></span>
<div id="comment-27510" class="comment">
<div id="post-27510-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I tried your example, but just got a Google Maps map of N America. If this is a truly circular route (unlikely these days), then show it as one relation. Otherwise, you should have different relations for "northbound" and "southbound". Yes, (most of) the ways in the route will occur twice: once in the NB relation and once in the SB. You should make sure that the "forward"/"backward" and "forward:stop"/"backward:stop" roles are set correctly.</p>
</div>
<div id="comment-27510-info" class="comment-info">
<span class="comment-age">(26 Oct '13, 14:02)</span> <span class="comment-user userinfo">mwbg</span>
</div>
</div>
</div>
<div id="comment-tools-27213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27213-form-container" class="comment-form-container">
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

<span id="27217"></span>

<div id="answer-container-27217" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27217-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please make one relation per direction.</p>
<p>The order of the way members should be in the order the bus goes. In particular, if the bus passes the same way twice due to a loop, please add it twice.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '13, 06:39</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-27217" class="comments-container">
<span id="27245"></span>
<div id="comment-27245" class="comment">
<div id="post-27245-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just a further question, for bus routes which basically run a loop (either by going between two places in both directions, or, in some cases, just running a single one-way loop, only passing through each area once), where it ends up at the start of the route, should the last member of the relation simply be the last part of the way that's connected to the part, which has the first relation?</p>
</div>
<div id="comment-27245-info" class="comment-info">
<span class="comment-age">(16 Oct '13, 22:02)</span> <span class="comment-user userinfo">TheUltimateK...</span>
</div>
</div>
<span id="27257"></span>
<div id="comment-27257" class="comment">
<div id="post-27257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The between-two-places case with distinct directions shown on the bus display is quite clearly a case for two relations. However, if the entire bus line forms a loop served only in one direction, it should be one relation forming a closed loop, i.e. having the same stop as firat and last stop and making the last way matching the first way.</p>
</div>
<div id="comment-27257-info" class="comment-info">
<span class="comment-age">(17 Oct '13, 07:03)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-27217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27217-form-container" class="comment-form-container">
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

