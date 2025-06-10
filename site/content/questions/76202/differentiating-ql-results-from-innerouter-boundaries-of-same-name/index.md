+++
type = "question"
title = "Differentiating QL results from inner/outer boundaries of same name"
description = '''The two examples below illustrate the issue Query1: [out:csv(&quot;name&quot;;false)] [bbox:-33.9480172,151.1107534,-33.8594833,151.2207935]; area[name=&quot;Sydney&quot;]; way(area)[highway][name]; out; One of the many results (after obtaining lat-lon and distance) is: Airport Drive, Sydney, 2000, -33.9272726, 151.169...'''
date = "2020-08-19T03:35:00Z"
lastmod = "2020-08-20T02:54:00Z"
weight = 76202
keywords = [ "suburb", "admin_boundary", "inner", "outer" ]
aliases = [ "/questions/76202" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Differentiating QL results from inner/outer boundaries of same name](/questions/76202/differentiating-ql-results-from-innerouter-boundaries-of-same-name)

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
<span id="post-76202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76202-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The two examples below illustrate the issue Query1:</p>
<p>[out:csv("name";false)] [bbox:-33.9480172,151.1107534,-33.8594833,151.2207935]; area[name="Sydney"]; way(area)[highway][name]; out;</p>
<p>One of the many results (after obtaining lat-lon and distance) is: Airport Drive, Sydney, 2000, -33.9272726, 151.1694315, 2.637km</p>
<p>Query 2:</p>
<p>[out:csv("name";false)] [bbox:-33.9480172,151.1107534,-33.8594833,151.2207935]; area[name="Mascot"]; way(area)[highway][name]; out;</p>
<p>One of the many results (after obtaining lat-lon and distance) is:</p>
<p>Airport Drive, Mascot, 2020, -33.9272726, 151.1694315, 2.637km</p>
<p>The two results are essentially identical (eg lat-lons) except for the name of the suburb. The problem appears to be due to there being an Administrative Area called Sydney which embraces all suburbs. Also, within the all-embracing Sydney, there is a relatively small suburb area also with the name Sydney (Both of admin level=10).</p>
<p>If one is looking for streets in suburbs within a largish BBox well inside the larger Sydney (which includes by design, the smaller Sydney), a large number of 'duplicate' (spurious) streets are generated with a suburb name of Sydney, it would seem, due to the outer Sydney boundary.</p>
<p>How can such a situation be avoided?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-suburb" rel="tag" title="see questions tagged &#39;suburb&#39;">suburb</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-inner" rel="tag" title="see questions tagged &#39;inner&#39;">inner</span> <span class="post-tag tag-link-outer" rel="tag" title="see questions tagged &#39;outer&#39;">outer</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '20, 03:35</strong></p>
<img src="https://secure.gravatar.com/avatar/c5e89b8b037b23165056f8722eb83dd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorylila&#39;s gravatar image" />
<p><span>rorylila</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorylila has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76202" class="comments-container">
&#10;</div>
<div id="comment-tools-76202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76202-form-container" class="comment-form-container">
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

<span id="76226"></span>

<div id="answer-container-76226" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76226-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My bad! I had checked the admin_levels of both the inner and outer Sydneys and concluded they were both 10. However, re-checking, the admin_level of the outer Sydney is 7. Changing the definition of 'area'in the query corrected the problem:</p>
<p>area["boundary"="administrative"] ["admin_level"="10"] ["name"="Sydney"]; way(area)[highway][name]; out ;</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '20, 02:54</strong></p>
<img src="https://secure.gravatar.com/avatar/c5e89b8b037b23165056f8722eb83dd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorylila&#39;s gravatar image" />
<p><span>rorylila</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorylila has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76226" class="comments-container">
&#10;</div>
<div id="comment-tools-76226" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76226-form-container" class="comment-form-container">
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

