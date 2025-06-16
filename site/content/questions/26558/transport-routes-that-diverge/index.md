+++
type = "question"
title = "Transport routes that diverge"
description = '''How should I input, for example, a bus route that takes a slightly different route evenings and weekends than it does during the working day? It doesn&#x27;t seem right to enter the whole route twice as two variants just for a small variation at one point on a long route that is otherwise the same. Is it...'''
date = "2013-09-20T14:25:00Z"
lastmod = "2013-11-14T09:27:00Z"
weight = 26558
keywords = [ "route", "split", "diverge" ]
aliases = [ "/questions/26558" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Transport routes that diverge](/questions/26558/transport-routes-that-diverge)

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
<span id="post-26558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26558-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How should I input, for example, a bus route that takes a slightly different route evenings and weekends than it does during the working day? It doesn't seem right to enter the whole route twice as two variants just for a small variation at one point on a long route that is otherwise the same. Is it acceptable to have the route split into two alternatives part-way along? I can't find any suitable 'role' to indicate a split like this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span> <span class="post-tag tag-link-diverge" rel="tag" title="see questions tagged &#39;diverge&#39;">diverge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Sep '13, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/15c4d97198c98739b8c13d232e5e4ea8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JClem&#39;s gravatar image" />
<p><span>JClem</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JClem has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26558" class="comments-container">
&#10;</div>
<div id="comment-tools-26558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26558-form-container" class="comment-form-container">
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

<span id="26559"></span>

<div id="answer-container-26559" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26559-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-26559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, the correct way is to create a new, complete route for the variant used in weekends, and group all of the variants under a "route_master" relation.</p>
<p>Bus Route relations should ideally never be "branched" or "broken" - no guesses should be made by (already very complex) routing software regarding the "branch" that should be taken on a route.</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Tag:type%3Droute_master">route_master</a> documentation in the OSM wiki for more information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '13, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-26559" class="comments-container">
<span id="26582"></span>
<div id="comment-26582" class="comment">
<div id="post-26582-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Branched bus routes are seen in our neighbourhood. In fact, branched routes cause problems not only in OSM-also cause problems in the route master of the bus operator. I have not tagged that branched route, because I know they will have removed the branching in the foreseeable future.</p>
</div>
<div id="comment-26582-info" class="comment-info">
<span class="comment-age">(21 Sep '13, 08:56)</span> <span class="comment-user userinfo">erkinalp</span>
</div>
</div>
</div>
<div id="comment-tools-26559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26559-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28060"></span>

<div id="answer-container-28060" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28060-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will get lots of people telling you to create a new relation for every single variant. This is impractical, certainly on every bus route/network/company in the UK that I've ever used.</p>
<p>I would dearly like some way of including branches in a given relation.</p>
<p>The notion that it would confuse routing software is specious.</p>
<p>Do people seriously expect any routing software, however good, to accommodate all the weird anomalies that even a simple UK bus route exhibits ?</p>
<p>How on earth would routing software present to the user instuctions such as "get a 61 bus from here, except if it's between 1100 and 1300, when the 61A runs this route, in which case, you have to get it from THAT stop over THERE. Whichever one you get, make sure it stops on XXX road (some don't). If it didn't stop on XXX road, continue until YYY, where you can probably pick up a 61C going the other way, and recirculate"</p>
<p>My suggested solution is to present the "normal" route (whatever that is) with one relation per direction, along with a relation containing disjointed exceptions to that route.</p>
<p>I want to get across to potential users that "some buses come this way; some don't. Those that terminate early (unpredictable) will turn-off route, stop THERE instead, and perhaps continue as a different route.".</p>
<p>It is a fact of UK bus usage that getting TO certain specific stops is rather unpredictable, as is boarding at a specific stop. My "normal" route would, in general, contain only those stops that are reasonably predictable. However, I don't want to disenfranchise certain groups of travelers, for whom the exceptions are the very ones that they want. E.g., if a particular trip serves a particular housing estate (but most don't), I don't want any map rendering to imply that it is "never served".</p>
<p>In other words, my "exceptions" relation would do nothing for routing, but would simply overlay the "dotted" lines on any rendering of the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '13, 19:04</strong></p>
<img src="https://secure.gravatar.com/avatar/033239e6e24e8bb673c3446836a5060c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mwbg&#39;s gravatar image" />
<p><span>mwbg</span><br />
<span class="score" title="45 reputation points">45</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mwbg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28060" class="comments-container">
<span id="28086"></span>
<div id="comment-28086" class="comment">
<div id="post-28086-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe in the future someone will propose (and get approved) some kind of <em>route_variant</em> relation type, somehow relating some part of an existing route (maybe through a "via" role) with another relation that describes another variant part of the route, or some other related structure. But <strong>as of NOW</strong>, there is no "official" way to map bus route variants <strong>except</strong> mapping each variant, no matter how many there are (even if dozens).</p>
</div>
<div id="comment-28086-info" class="comment-info">
<span class="comment-age">(14 Nov '13, 09:27)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
</div>
<div id="comment-tools-28060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28060-form-container" class="comment-form-container">
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

