+++
type = "question"
title = "routing - automatic cities &amp; city district indexing (not for navigation - don&#x27;t need turns, road numbers...)"
description = '''Hello comunity, I&#x27;m develpoing kinda &quot;hitchike&quot; app (feel like hitchike but phone instead of table) where I need some &quot;chekpoints&quot; - not road turns, but maybe road number change cities (~center), or some city districts. Is there some library, github repo for this? cause on wiki- routing https://wiki...'''
date = "2015-10-20T10:46:00Z"
lastmod = "2015-10-21T08:38:00Z"
weight = 46014
keywords = [ "directions", "routing" ]
aliases = [ "/questions/46014" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [routing - automatic cities & city district indexing (not for navigation - don't need turns, road numbers...)](/questions/46014/routing-automatic-cities-city-district-indexing-not-for-navigation-dont-need-turns-road-numbers)

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
<span id="post-46014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46014-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello comunity, I'm develpoing kinda "hitchike" app (feel like hitchike but phone instead of table) where I need some "chekpoints" - not road turns, but maybe road number change cities (~center), or some city districts. Is there some library, github repo for this? cause on wiki- routing <a href="https://wiki.openstreetmap.org/wiki/Routing">https://wiki.openstreetmap.org/wiki/Routing</a> I've not found anything satisfactory for this task. Or what's th closest existing solution for my problem.</p>
<p>Thanks Robert.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '15, 10:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f23db16638eb2c204d3e51f5d18528fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="roberto68&#39;s gravatar image" />
<p><span>roberto68</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="roberto68 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '15, 13:45</strong> </span></p>
</div>
</div>
<div id="comments-container-46014" class="comments-container">
<span id="46015"></span>
<div id="comment-46015" class="comment">
<div id="post-46015-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What are "road number change cities"? Why can't you just insert checkpoints every x kilometers? Can you give us more details about your problem and your goal?</p>
</div>
<div id="comment-46015-info" class="comment-info">
<span class="comment-age">(20 Oct '15, 11:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="46024"></span>
<div id="comment-46024" class="comment">
<div id="post-46024-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well and do not care about kilometers - there can be no city/town for e.g 20km or also 3 towns. I need to automaticaly pair the the Hhiker with the driver: the hiker eneters where is his destination (or opt point) and it can be only part of the driver routes. 90% want actually get to some town or city. I need route to consist of "chekcpoints" whether town/city or maybe road crossing. and server'd go thorough that JSON array and automatically pair dirver - hiker when that route is matching. note I'm doing this in NodeJS (javascript)</p>
</div>
<div id="comment-46024-info" class="comment-info">
<span class="comment-age">(20 Oct '15, 13:53)</span> <span class="comment-user userinfo">roberto68</span>
</div>
</div>
<span id="46033"></span>
<div id="comment-46033" class="comment">
<div id="post-46033-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so the hiker specifies a town, you translate that to lat/lon. Around this lan/lon you create a circle (of e.g. 3 km) and see whether that circle intersects with the route of the driver ? A bit similar to POIs along the route ?</p>
</div>
<div id="comment-46033-info" class="comment-info">
<span class="comment-age">(21 Oct '15, 06:38)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="46036"></span>
<div id="comment-46036" class="comment">
<div id="post-46036-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks understand. how can I check if that hiker location intersects with driver the route - do you know some good source code example for that?</p>
</div>
<div id="comment-46036-info" class="comment-info">
<span class="comment-age">(21 Oct '15, 08:38)</span> <span class="comment-user userinfo">roberto68</span>
</div>
</div>
</div>
<div id="comment-tools-46014" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46014-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

