+++
type = "question"
title = "Routing through swing gates"
description = '''There are two swing gates on a particular road: https://www.openstreetmap.org/node/8637280777 https://www.openstreetmap.org/node/8637280778 They don&#x27;t allow routing through them even though in the Feature Editor they have Allowed Access, All set to &quot;yes&quot;. Why don&#x27;t they allow routing? (This is my fi...'''
date = "2021-09-22T16:13:00Z"
lastmod = "2021-09-24T06:58:00Z"
weight = 81857
keywords = [ "swing-gate", "routing" ]
aliases = [ "/questions/81857" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Routing through swing gates](/questions/81857/routing-through-swing-gates)

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
<span id="post-81857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81857-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are two swing gates on a particular road:</p>
<p><a href="https://www.openstreetmap.org/node/8637280777">https://www.openstreetmap.org/node/8637280777</a></p>
<p><a href="https://www.openstreetmap.org/node/8637280778">https://www.openstreetmap.org/node/8637280778</a></p>
<p>They don't allow routing through them even though in the Feature Editor they have Allowed Access, All set to "yes". Why don't they allow routing?</p>
<p>(This is my first exposure to the behind-the-scenes of OSM. I am trying to figure out why my navigation app, Kurviger, won't allow me to plot a course through this road.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-swing-gate" rel="tag" title="see questions tagged &#39;swing-gate&#39;">swing-gate</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '21, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/5662d1262516ccbd70249e7aeaf58901?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dan000&#39;s gravatar image" />
<p><span>dan000</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dan000 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81857" class="comments-container">
<span id="81858"></span>
<div id="comment-81858" class="comment">
<div id="post-81858-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Different routers have different rules about what they think is navigable and what is not. You can try various combinations on the OpenStreetMap site at <a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=-27.26300%2C152.95739%3B-27.26384%2C152.95687#map=19/-27.26343/152.95714">https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=-27.26300%2C152.95739%3B-27.26384%2C152.95687#map=19/-27.26343/152.95714</a> .</p>
<p>Do you know how often Kurviger updates their routing data from OSM? It won;t be instant, and might be a longer time than you're expecting.</p>
</div>
<div id="comment-81858-info" class="comment-info">
<span class="comment-age">(22 Sep '21, 16:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="81866"></span>
<div id="comment-81866" class="comment">
<div id="post-81866-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You were probably mistaken about the allowed access for all to be set to "yes". What you were seeing in the editor was an implicit assumption made by the editor. Note that the "yes" was written in a light grey font. Only when it appears as black font is it explicitly tagged. You see that also in the tags listed on the node pages that you linked above where the <code>access</code> key is not present.</p>
</div>
<div id="comment-81866-info" class="comment-info">
<span class="comment-age">(22 Sep '21, 21:07)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-81857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81857-form-container" class="comment-form-container">
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

<span id="81859"></span>

<div id="answer-container-81859" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81859-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-81859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dan000 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These gates don't actually have the allowed access set to "yes". Rather, they've both been tagged with <code>opening_hours=24/7</code>, which is a tag that routers may not look at for barriers. OSRM is treating these gates as closed and routing via other roads, though Graphhopper is routing through them.</p>
<p>Routers are more likely to look at the legal access tags. If these gates are always open, I would recommend tagging them with <code>access=yes</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '21, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-81859" class="comments-container">
&#10;</div>
<div id="comment-tools-81859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81859-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81912"></span>

<div id="answer-container-81912" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81912-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As we have not heard back from <a href="https://help.openstreetmap.org/users/20806/dan000">@dan000</a> as yet, I have added access=yes to both lift gates as they are only in use during very uncommon flooding events at the river crossing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '21, 00:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-81912" class="comments-container">
<span id="81913"></span>
<div id="comment-81913" class="comment">
<div id="post-81913-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for that.</p>
</div>
<div id="comment-81913-info" class="comment-info">
<span class="comment-age">(24 Sep '21, 06:58)</span> <span class="comment-user userinfo">dan000</span>
</div>
</div>
</div>
<div id="comment-tools-81912" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81912-form-container" class="comment-form-container">
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

