+++
type = "question"
title = "API or tool to match a GPS track to existing roads"
description = '''I need to identify the road (or, more precisely, the sequence of road segments) that a GPS track is following.  I can see how to implement this through low-level methods - find closest segments for each point on the track, then clean up the results - but maybe this is already implemented somewhere?'''
date = "2014-11-08T06:46:00Z"
lastmod = "2014-11-11T18:22:00Z"
weight = 38372
keywords = [ "track", "api", "matching", "road" ]
aliases = [ "/questions/38372" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [API or tool to match a GPS track to existing roads](/questions/38372/api-or-tool-to-match-a-gps-track-to-existing-roads)

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
<span id="post-38372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38372-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-38372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to identify the road (or, more precisely, the sequence of road segments) that a GPS track is following.</p>
<p>I can see how to implement this through low-level methods - find closest segments for each point on the track, then clean up the results - but maybe this is already implemented somewhere?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-matching" rel="tag" title="see questions tagged &#39;matching&#39;">matching</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '14, 06:46</strong></p>
<img src="https://secure.gravatar.com/avatar/777894ea5153122bfa6b83f5bbf23622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leonid&#39;s gravatar image" />
<p><span>leonid</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leonid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Nov '14, 06:56</strong> </span></p>
</div>
</div>
<div id="comments-container-38372" class="comments-container">
&#10;</div>
<div id="comment-tools-38372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38372-form-container" class="comment-form-container">
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

<span id="38448"></span>

<div id="answer-container-38448" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38448-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-38448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One simple possibility is to use routing software, such as OSRM, to find a route between a series of via points taken from your GPS track.</p>
<p>You could take a point from your track every 2km, and add a via point at that location. Then call OSRM's viaroute function to get a route back which will follow OSM data between those points.</p>
<p>To make the route more faithful, you could replace "every 2km" with a shorter interval, or add some logic to add a via point whenever the track goes round a sharp corner.</p>
<p>OSRM will return turn-by-turn directions for the route, plus a polyline. If you want the exact OSM IDs, you can run your own instance of OSRM and adapt the car.lua profile code to return OSM IDs as part of the road name.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '14, 10:08</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-38448" class="comments-container">
&#10;</div>
<div id="comment-tools-38448" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38448-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38376"></span>

<div id="answer-container-38376" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38376-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-38376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This kind of problem is called "matching" and is adressed by various approaches:<br />
<a href="http://lmgtfy.com/?q=match+gps+track+road+network">http://lmgtfy.com/?q=match+gps+track+road+network</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '14, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-38376" class="comments-container">
<span id="38378"></span>
<div id="comment-38378" class="comment">
<div id="post-38378-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I suspect that the OP was perfectly capable of doing a web search and was rather hoping for personal recommendations of what works and what doesn't in particular circumstances...</p>
</div>
<div id="comment-38378-info" class="comment-info">
<span class="comment-age">(08 Nov '14, 13:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="38447"></span>
<div id="comment-38447" class="comment">
<div id="post-38447-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please don't reply with lmgtfy-type sites. This is help.osm.org, not snarky.osm.org.</p>
</div>
<div id="comment-38447-info" class="comment-info">
<span class="comment-age">(11 Nov '14, 10:05)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="38460"></span>
<div id="comment-38460" class="comment">
<div id="post-38460-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm sorry, my intention wasn't to blame anybody. I just thought that <a href="https://help.openstreetmap.org/users/9965/leonid">@leonid</a> didn't had an idea on what he is looking in detail (as he didn't provided further infos about his usecase).</p>
</div>
<div id="comment-38460-info" class="comment-info">
<span class="comment-age">(11 Nov '14, 18:22)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-38376" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38376-form-container" class="comment-form-container">
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

