+++
type = "question"
title = "Route always returns location on Antarctica?"
description = '''I&#x27;ve downloaded the 5.3.0 Windows release and followed the Running OSRM instructions. I downloaded the Florida map and ran the extract and contract tools seemingly without issue. I did run into numerous warnings during extract, but I think they&#x27;re harmless? [warn] Restriction references invalid node...'''
date = "2016-07-24T15:56:00Z"
lastmod = "2016-07-24T18:47:00Z"
weight = 51074
keywords = [ "osrm", "route" ]
aliases = [ "/questions/51074" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Route always returns location on Antarctica?](/questions/51074/route-always-returns-location-on-antarctica)

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
<span id="post-51074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51074-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've downloaded the 5.3.0 Windows release and followed the Running OSRM instructions. I downloaded the Florida map and ran the extract and contract tools seemingly without issue. I did run into numerous warnings during extract, but I think they're harmless?</p>
<p>[warn] Restriction references invalid node: 4294967295 [warn] Restriction references invalid way: 423832364</p>
<p>When I run the server and call GET <a href="http://localhost:5000/route/v1/car/28.064481,-82.045101;28.06389546595713,-82.0313286781311">http://localhost:5000/route/v1/car/28.064481,-82.045101;28.06389546595713,-82.0313286781311</a></p>
<p>The server always responds with waypoints coordinates in Antarctica -- name "Sunset Drive"</p>
<p>Any ideas? I'm currently trying again, this time with the South US map.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jul '16, 15:56</strong></p>
<img src="https://secure.gravatar.com/avatar/4df3a190bc3f4255c664ac624dcc45f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BrandonD&#39;s gravatar image" />
<p><span>BrandonD</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BrandonD has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jul '16, 17:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-51074" class="comments-container">
<span id="51076"></span>
<div id="comment-51076" class="comment">
<div id="post-51076-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm guessing you're asking about OSRM? It might be helpful (with a Windows build) to say where you got it from. Can you also explain what the "South US Map" is?</p>
</div>
<div id="comment-51076-info" class="comment-info">
<span class="comment-age">(24 Jul '16, 17:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="51077"></span>
<div id="comment-51077" class="comment">
<div id="post-51077-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. From here: <a href="http://build.project-osrm.org/">http://build.project-osrm.org/</a></p>
</div>
<div id="comment-51077-info" class="comment-info">
<span class="comment-age">(24 Jul '16, 17:05)</span> <span class="comment-user userinfo">BrandonD</span>
</div>
</div>
</div>
<div id="comment-tools-51074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51074-form-container" class="comment-form-container">
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

<span id="51078"></span>

<div id="answer-container-51078" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51078-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm a dummy -- lat long coordinates need to be reversed. It's the opposite of what Google's DistanceMatrix uses.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '16, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/4df3a190bc3f4255c664ac624dcc45f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BrandonD&#39;s gravatar image" />
<p><span>BrandonD</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BrandonD has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51078" class="comments-container">
&#10;</div>
<div id="comment-tools-51078" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51078-form-container" class="comment-form-container">
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

