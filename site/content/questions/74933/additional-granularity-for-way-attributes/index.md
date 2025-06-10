+++
type = "question"
title = "Additional granularity for &#x27;way&#x27; attributes?"
description = '''I am working on a project to provide more granular data for hiking trails to benefit users with mobility challenges (e.g. wheelchair, prosthetic, heart condition, etc.) In doing so, I&#x27;ve captured local geodata at a much more granular level than at individual Nodes along a given Way on OSM. I&#x27;ve done...'''
date = "2020-05-20T17:13:00Z"
lastmod = "2020-05-22T11:46:00Z"
weight = 74933
keywords = [ "footpath", "disability", "incline", "hiking", "granularity" ]
aliases = [ "/questions/74933" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Additional granularity for 'way' attributes?](/questions/74933/additional-granularity-for-way-attributes)

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
<span id="post-74933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74933-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am working on a project to provide more granular data for hiking trails to benefit users with mobility challenges (e.g. wheelchair, prosthetic, heart condition, etc.) In doing so, I've captured local geodata at a much more granular level than at individual Nodes along a given Way on OSM. I've done this with a few Attributes, but one good example is Incline. I believe I can use "Incline=" x in percent, but that attribute then applies to the entire way. Is there a capability to somehow assign a sequence of slope values (perhaps evenly distributed) along the way? I've seen some usage of "max=" for the Incline key, but that won't work for this project.</p>
<p>I'm new to OSM, so thank you all in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-footpath" rel="tag" title="see questions tagged &#39;footpath&#39;">footpath</span> <span class="post-tag tag-link-disability" rel="tag" title="see questions tagged &#39;disability&#39;">disability</span> <span class="post-tag tag-link-incline" rel="tag" title="see questions tagged &#39;incline&#39;">incline</span> <span class="post-tag tag-link-hiking" rel="tag" title="see questions tagged &#39;hiking&#39;">hiking</span> <span class="post-tag tag-link-granularity" rel="tag" title="see questions tagged &#39;granularity&#39;">granularity</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '20, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/168d65b5cb31c3951699a536183af790?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TrailAbilities&#39;s gravatar image" />
<p><span>TrailAbilities</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TrailAbilities has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74933" class="comments-container">
&#10;</div>
<div id="comment-tools-74933" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74933-form-container" class="comment-form-container">
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

<span id="74934"></span>

<div id="answer-container-74934" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74934-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In OSM it is pretty common to split a way where a characteristic changes. For roads that may be the type of pavement, number of lanes, speed limit, etc.</p>
<p>So there is nothing wrong in splitting a hiking trail where the grade changes (or other criteria like surface or smoothness) so that you can tag the specific sections appropriately.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '20, 19:22</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-74934" class="comments-container">
<span id="74935"></span>
<div id="comment-74935" class="comment">
<div id="post-74935-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. Would the splitting of the way need to be done anywhere any characteristic changes? For example, if tracking 5 characteristics, then a change to any one of them would lead to a new split? I think that's what you are saying, and it makes sense.</p>
<p>I'm actually hoping for a way to deal with very dense characteristic changes...such as slope on an undulating hiking trail. If each change to the slope requires a new way, it could lead to a large number of ways (probably not desirable for many other use cases).</p>
<p>Perhaps I'll look into whether hosting the (very granular) data with a third party (while keeping it open source) in a separate layer is a possibility. Thanks again, and I look forward to any other ideas from the community!</p>
</div>
<div id="comment-74935-info" class="comment-info">
<span class="comment-age">(20 May '20, 20:44)</span> <span class="comment-user userinfo">TrailAbilities</span>
</div>
</div>
<span id="74954"></span>
<div id="comment-74954" class="comment">
<div id="post-74954-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OSM doesn't store a DEM. As an end-user, I might be more interested in gradient between two particular objects, or on a segment that is already splited for its major differing propoerties. Of course, changes between up, down, and flat should be recorded, as well as stairs, edges, and any significantly sharp changes. For values varying in between, it is ultimately up to your judgement on how micro you want your micro-mapping steps to be. There should be other projects aiming to produce the most detailed, fine-grained elevation data. You can definitely contribute to both.</p>
</div>
<div id="comment-74954-info" class="comment-info">
<span class="comment-age">(22 May '20, 11:46)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-74934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74934-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74937"></span>

<div id="answer-container-74937" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74937-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think when stf says "it is pretty common" it could be better stated by saying that "the only way" to do what you wish is to split the way whenever any characteristic changes. Each change in slope won't require a "new way" as you indicate in your reply but each would require the way to be split. This makes it possible for such changes to be detected by a sufficiently intelligent rendering engine.</p>
<p>If several characteristics change in the same area, then indeed the original way could end up as many smaller pieces that are still connected but each with its own collection of attributes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '20, 01:56</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-74937" class="comments-container">
&#10;</div>
<div id="comment-tools-74937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74937-form-container" class="comment-form-container">
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

