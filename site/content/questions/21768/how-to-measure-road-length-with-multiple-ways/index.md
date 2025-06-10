+++
type = "question"
title = "How to measure road length with multiple ways"
description = '''Some trunk roads have multiple ways (oneway=true), how would you go about measure the length of such a road without counting those portions twice ?'''
date = "2013-04-23T17:45:00Z"
lastmod = "2013-04-25T07:43:00Z"
weight = 21768
keywords = [ "roads" ]
aliases = [ "/questions/21768" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to measure road length with multiple ways](/questions/21768/how-to-measure-road-length-with-multiple-ways)

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
<span id="post-21768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21768-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Some trunk roads have multiple ways (oneway=true), how would you go about measure the length of such a road without counting those portions twice ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '13, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/d52bb695795c59fc3c5ef38b7d59b415?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pgirolami76&#39;s gravatar image" />
<p><span>pgirolami76</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pgirolami76 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Apr '13, 19:35</strong> </span></p>
</div>
</div>
<div id="comments-container-21768" class="comments-container">
&#10;</div>
<div id="comment-tools-21768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21768-form-container" class="comment-form-container">
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

<span id="21769"></span>

<div id="answer-container-21769" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21769-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps the easiest option is to use a routing engine (such as OSRM); route from the start to the end of the road (which will probably prefer trunk roads on its default profile); and measure the length of the result. The <a href="http://map.project-osrm.org/">OSRM demo site</a> will tell you the distance, or you could analyse the GPX export. You could, of course, use your own OSRM instance or the <a href="https://github.com/DennisOSRM/Project-OSRM/wiki/Server-api">public API</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '13, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-21769" class="comments-container">
&#10;</div>
<div id="comment-tools-21769" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21769-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21772"></span>

<div id="answer-container-21772" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21772-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you load the data into a PostGIS database (e.g. with osm2pgsql) then you can conceivably run an operation like "draw an area of 50 metres around each bit of a trunk road; if another bit of trunk road falls within that area, delete it". (The relevant PostGIS functions to look up are <code>ST_BUFFER</code> and <code>ST_CONTAINS</code> or <code>ST_INTERSECTS</code>.) This will never give a perfect result since you would wrongly keep those lanes that are more than 50 metres apart, and you would wrongly drop bits that run really close to another trunk road, but you'd probably arrive at a relatively good measure.</p>
<p>(Btw. if you have the stuff in PostGIS anyway, it is dead easy to compute the length by using <code>ST_LENGTH</code> on a <code>GEOGRAPHY</code> data type.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '13, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-21772" class="comments-container">
<span id="21774"></span>
<div id="comment-21774" class="comment">
<div id="post-21774-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes everything is in postgis and we're working with a treillis. What I want is to know the length of the roads inside each treillis square. The issue here is that for 2-way roads, I'll count twice the length and that's incorrect.</p>
</div>
<div id="comment-21774-info" class="comment-info">
<span class="comment-age">(23 Apr '13, 19:32)</span> <span class="comment-user userinfo">pgirolami76</span>
</div>
</div>
<span id="21781"></span>
<div id="comment-21781" class="comment">
<div id="post-21781-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As I said - compute a buffer around each road and delete others inside that buffer, that should get rid of the 2-way roads.</p>
</div>
<div id="comment-21781-info" class="comment-info">
<span class="comment-age">(24 Apr '13, 07:18)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="21791"></span>
<div id="comment-21791" class="comment">
<div id="post-21791-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain a little more ? How would I create the shape for that road to buffer around if I can't distinguish the ways ?</p>
</div>
<div id="comment-21791-info" class="comment-info">
<span class="comment-age">(24 Apr '13, 17:20)</span> <span class="comment-user userinfo">pgirolami76</span>
</div>
</div>
<span id="21818"></span>
<div id="comment-21818" class="comment">
<div id="post-21818-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I understand better : you're saying eliminate <em>all</em> the other roads and that will get rid of the other way. But I'm interested in computing the intersected length of all road segments per category (primary, secondary, tertiary) so that wouldn't work. It would however help if I precomputed each road and if I kept in each square only the longest segment per road (=per ref). Is that your idea or was it something else ?</p>
</div>
<div id="comment-21818-info" class="comment-info">
<span class="comment-age">(25 Apr '13, 07:43)</span> <span class="comment-user userinfo">pgirolami76</span>
</div>
</div>
</div>
<div id="comment-tools-21772" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21772-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21770"></span>

<div id="answer-container-21770" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21770-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There was a proposal to join the two carriageways into a dual_carriageway relation. This would assist with your question (if in a DC relation only measure one way or the average of the two). It would also assist with the application of maxspeed=national to know difference between a single or dual carriage road without the kludge of adding maxspeed=70 mph / 60 mph when the sign says national speed limit not 60 or 70 mph.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '13, 18:32</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-21770" class="comments-container">
<span id="21775"></span>
<div id="comment-21775" class="comment">
<div id="post-21775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes it would. As would assigning a direction to the ways. Did that ever make any progress ? What was blocking it ?</p>
</div>
<div id="comment-21775-info" class="comment-info">
<span class="comment-age">(23 Apr '13, 19:33)</span> <span class="comment-user userinfo">pgirolami76</span>
</div>
</div>
<span id="21776"></span>
<div id="comment-21776" class="comment">
<div id="post-21776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Everything in OSM is voluntary, including tagging. I used the relation a little but it didn't catch on so it is not used now AFAIK.</p>
</div>
<div id="comment-21776-info" class="comment-info">
<span class="comment-age">(23 Apr '13, 19:45)</span> <span class="comment-user userinfo">ChrisH</span>
</div>
</div>
</div>
<div id="comment-tools-21770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21770-form-container" class="comment-form-container">
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

