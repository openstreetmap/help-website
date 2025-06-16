+++
type = "question"
title = "Complex routes of nested ways"
description = '''Several abandoned railways in our area have been converted to multi-use trails. Many third party users of OSM data do not support semicolon separated values. So my question is; how to map these complex scenarios where trails have multiple uses and trails do not form a simple hierarchy: Gordon Glaves...'''
date = "2014-04-18T15:06:00Z"
lastmod = "2016-07-07T23:34:00Z"
weight = 32432
keywords = [ "multi-use", "railway", "route", "relation", "abandoned" ]
aliases = [ "/questions/32432" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Complex routes of nested ways](/questions/32432/complex-routes-of-nested-ways)

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
<span id="post-32432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32432-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Several abandoned railways in our area have been converted to multi-use trails. Many third party users of OSM data do not support semicolon separated values. So my question is; how to map these complex scenarios where trails have multiple uses and trails do not form a simple hierarchy:</p>
<p>Gordon Glaves Memorial Parkway in Brantford is a multi-use trail through parks and along riverbanks. Sites like waymarkedtrails.org expect a separate relations for each use (bicycle, hiking, inline_skating). This in itself; is not so difficult to code.</p>
<p>Some sections of the Gordon Glaves Memorial Parkway (GGMP) are part of Trans-Canada Trail (TCT); a cross-Canada multi-use trail that sometimes uses the shoulder of rural roads.</p>
<p>How is it best to map relations for GGMP and TCT? A) Should GGMP be a collection of two routes (one that is part of TCT and the other is not)? B) Since third party sites want multi relations for multi use; is it best to create a "hiking" route; then create a parent for "bicycle" and "inline_skates"; or should the base relation be "unknown" with 3 parents (hiking, bicycle, inline_skates)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-multi-use" rel="tag" title="see questions tagged &#39;multi-use&#39;">multi-use</span> <span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-abandoned" rel="tag" title="see questions tagged &#39;abandoned&#39;">abandoned</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '14, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c1a722148c903e45bc99a8dcbba4577e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fbax&#39;s gravatar image" />
<p><span>fbax</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fbax has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32432" class="comments-container">
&#10;</div>
<div id="comment-tools-32432" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32432-form-container" class="comment-form-container">
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

<span id="32440"></span>

<div id="answer-container-32440" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32440-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi each section of a trail using a way should be part of a relation. Please read this section of the WIKI complicated yes, <a href="https://wiki.openstreetmap.org/wiki/Route#Bus_routes_.28also_trolley_bus.29">https://wiki.openstreetmap.org/wiki/Route#Bus_routes_.28also_trolley_bus.29</a> There is even a specific section for bicycle routes as well. If you follow these guidelines the renderer can read your contributions correctly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '14, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-32440" class="comments-container">
&#10;</div>
<div id="comment-tools-32440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32440-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50714"></span>

<div id="answer-container-50714" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50714-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a new user, I would like to know why this is a problem. Can you not add multiple attributes in multiple categories for a single way? Can I have surface = gravel as well as surface = dirt, plus width = 5 m as well as other sizes?</p>
<p>Or (I'm looking for fundamental best practices here), should every section of a way with a unique combination of attributes be separate from the others?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '16, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/bd47a2c66ca4f2bbc7994c7805a2359c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robinottawa&#39;s gravatar image" />
<p><span>robinottawa</span><br />
<span class="score" title="105 reputation points">105</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robinottawa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50714" class="comments-container">
<span id="50716"></span>
<div id="comment-50716" class="comment">
<div id="post-50716-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>robinottawa:</p>
<p>My original question was about ways within relations; not tags (attributes) on ways.</p>
<p>As a follow-up; I'll mention that waymarkedtrails.org site modified their code such that multi-purpose routes are now supported. When I raised my question the site did not support "route=hiking;bicycle" (with a semicolon). Now tag values with semicolon is supported.</p>
<p>If you have your own question; then you should likely start a new thread.</p>
</div>
<div id="comment-50716-info" class="comment-info">
<span class="comment-age">(07 Jul '16, 17:48)</span> <span class="comment-user userinfo">fbax</span>
</div>
</div>
<span id="50724"></span>
<div id="comment-50724" class="comment">
<div id="post-50724-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/12525/robinottawa">@robinottawa</a> Generally speaking, you'd split a way into sections for which the tagging is unique. For example, this bit of road <a href="https://www.openstreetmap.org/way/31559293">https://www.openstreetmap.org/way/31559293</a> has mostly the same tags as an adjacent bit <a href="https://www.openstreetmap.org/way/283948074">https://www.openstreetmap.org/way/283948074</a> , but the speed limits are different. If you tried to add "speed_limit=40 mph;50 mph" you wouldn't know which bit had which speed limit.</p>
</div>
<div id="comment-50724-info" class="comment-info">
<span class="comment-age">(07 Jul '16, 23:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50714-form-container" class="comment-form-container">
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

