+++
type = "question"
title = "Set speed limit in a country"
description = '''Is it possible to set the speed limit to all roads by category. Eg Morotway 100kmh, Main road 60kmh, all others 40kmh. I am looking to map speed limits in Trinidad but there is limited road speed data for the whole country. Tks.'''
date = "2022-10-20T13:24:00Z"
lastmod = "2022-10-22T22:45:00Z"
weight = 85937
keywords = [ "speedlimit", "roadtype" ]
aliases = [ "/questions/85937" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Set speed limit in a country](/questions/85937/set-speed-limit-in-a-country)

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
<span id="post-85937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85937-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to set the speed limit to all roads by category. Eg Morotway 100kmh, Main road 60kmh, all others 40kmh. I am looking to map speed limits in Trinidad but there is limited road speed data for the whole country.</p>
<p>Tks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-speedlimit" rel="tag" title="see questions tagged &#39;speedlimit&#39;">speedlimit</span> <span class="post-tag tag-link-roadtype" rel="tag" title="see questions tagged &#39;roadtype&#39;">roadtype</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '22, 13:24</strong></p>
<img src="https://secure.gravatar.com/avatar/61d844ca9a3355adc18056e38911d2b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vincentokane&#39;s gravatar image" />
<p><span>vincentokane</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vincentokane has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85937" class="comments-container">
<span id="85967"></span>
<div id="comment-85967" class="comment">
<div id="post-85967-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"Defaults" for untagged ways are often stored elsewhere such as in <a href="https://wiki.openstreetmap.org/wiki/Default_speed_limits">this table</a> in the wiki which does contain a line for T&amp;T.</p>
</div>
<div id="comment-85967-info" class="comment-info">
<span class="comment-age">(22 Oct '22, 22:45)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-85937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85937-form-container" class="comment-form-container">
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

<span id="85941"></span>

<div id="answer-container-85941" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85941-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-85941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is something that the routing engine or app would have to do. We don't usually map default speed limits (i.e. those that are not signposted) because that would mean that if there's a change in the law, we would have to update all the roads - and worse, we wouldn't even know if a "maxspeed=100" is due to there being an actual sign, or due to someone just mapping the default!</p>
<p>See <a href="https://2022.stateofthemap.org/sessions/YWH3XD/">https://2022.stateofthemap.org/sessions/YWH3XD/</a> for a talk at State of the Map 2022 that discussed this issue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '22, 14:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-85941" class="comments-container">
<span id="85946"></span>
<div id="comment-85946" class="comment">
<div id="post-85946-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Actually, we have <code>source:maxspeed=*</code> and <code>maxspeed:type=*</code> to know whether a particular speed restriction is implicit or comes from a sign. However, these tags aren't always present and have to be kept up-to-data, of course.</p>
</div>
<div id="comment-85946-info" class="comment-info">
<span class="comment-age">(21 Oct '22, 07:14)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-85941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85941-form-container" class="comment-form-container">
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

