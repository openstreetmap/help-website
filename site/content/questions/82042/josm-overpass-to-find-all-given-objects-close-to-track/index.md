+++
type = "question"
title = "JOSM + Overpass to find all given objects close to track?"
description = '''Hello, I was wondering if JOSM can be fed a track, and query OSM through Overpass to find all objects of a given type that lie within x kilometers from the track? Thank you.'''
date = "2021-10-06T15:56:00Z"
lastmod = "2021-10-08T14:51:00Z"
weight = 82042
keywords = [ "overpass", "josm" ]
aliases = [ "/questions/82042" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM + Overpass to find all given objects close to track?](/questions/82042/josm-overpass-to-find-all-given-objects-close-to-track)

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
<span id="post-82042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82042-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I was wondering if JOSM can be fed a track, and query OSM through Overpass to find all objects of a given type that lie within x kilometers from the track?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '21, 15:56</strong></p>
<img src="https://secure.gravatar.com/avatar/222fc1ad4f1993620a21cb57fa816f16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shohreh&#39;s gravatar image" />
<p><span>Shohreh</span><br />
<span class="score" title="85 reputation points">85</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shohreh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82042" class="comments-container">
&#10;</div>
<div id="comment-tools-82042" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82042-form-container" class="comment-form-container">
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

<span id="82048"></span>

<div id="answer-container-82048" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82048-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Shohreh has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Look at the <code>around</code> command:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '21, 00:18</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-82048" class="comments-container">
<span id="82087"></span>
<div id="comment-82087" class="comment">
<div id="post-82087-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I'll experiment with OT and its around().</p>
</div>
<div id="comment-82087-info" class="comment-info">
<span class="comment-age">(08 Oct '21, 14:51)</span> <span class="comment-user userinfo">Shohreh</span>
</div>
</div>
</div>
<div id="comment-tools-82048" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82048-form-container" class="comment-form-container">
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

