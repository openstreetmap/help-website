+++
type = "question"
title = "[SOLVED] Wrong routing computation"
description = '''Hi all, I&#x27;m having trouble with this simple route (car routing by graphhopper engine): https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;amp;route=38.92776%2C-1.74088%3B38.92781%2C-1.74031 Just zoom in until you get closer to the start/end points and you&#x27;ll see that the routing engine ...'''
date = "2018-08-11T15:31:00Z"
lastmod = "2018-08-12T06:50:00Z"
weight = 65274
keywords = [ "routing" ]
aliases = [ "/questions/65274" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[SOLVED\] Wrong routing computation](/questions/65274/solved-wrong-routing-computation)

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
<span id="post-65274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65274-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I'm having trouble with this simple route (car routing by graphhopper engine):</p>
<p><a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=38.92776%2C-1.74088%3B38.92781%2C-1.74031">https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=38.92776%2C-1.74088%3B38.92781%2C-1.74031</a></p>
<p>Just zoom in until you get closer to the start/end points and you'll see that the routing engine decides to skip the roundabout exit instead of taking it to get to the end point.</p>
<p>Any insights about what could possibly be happening?</p>
<p>Thank you.</p>
<p>PD: I'm new in OSM editing so I don't know the exact procedure to fix it, I'll be glad if some of you could give me a tip on this.</p>
<p><strong>UPDATE</strong>: I removed a one-way restriction which definitely could cause problems, but the routing engine keeps doing the same wrong computation.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '18, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/9412f421fb20ee41fe185a32cd99f16c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jjgcc&#39;s gravatar image" />
<p><span>jjgcc</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jjgcc has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Aug '18, 12:28</strong> </span></p>
</div>
</div>
<div id="comments-container-65274" class="comments-container">
<span id="65276"></span>
<div id="comment-65276" class="comment">
<div id="post-65276-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><strong>SOLVED</strong>: The OSRM routing engine works properly.</p>
</div>
<div id="comment-65276-info" class="comment-info">
<span class="comment-age">(11 Aug '18, 16:11)</span> <span class="comment-user userinfo">jjgcc</span>
</div>
</div>
</div>
<div id="comment-tools-65274" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65274-form-container" class="comment-form-container">
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

<span id="65283"></span>

<div id="answer-container-65283" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65283-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>the database behind the routing engines is not updated instantanously. It can take a few days before the new route will be calculated. So try Graphopper again in a few days.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '18, 06:50</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-65283" class="comments-container">
&#10;</div>
<div id="comment-tools-65283" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65283-form-container" class="comment-form-container">
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

