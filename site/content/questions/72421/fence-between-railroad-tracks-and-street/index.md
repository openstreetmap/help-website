+++
type = "question"
title = "fence between railroad tracks and street"
description = '''Hi, I want to map a fence separating a stretch of railroad tracks from a bike road. The fence is definitely property of the railroad company. It runs below the embankment and right along the road (no distance to the road but several meters to the tracks). There are some locked gates (maintenance acc...'''
date = "2020-01-07T20:47:00Z"
lastmod = "2020-01-26T14:37:00Z"
weight = 72421
keywords = [ "gate", "railroad", "barrier", "fence" ]
aliases = [ "/questions/72421" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [fence between railroad tracks and street](/questions/72421/fence-between-railroad-tracks-and-street)

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
<span id="post-72421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72421-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-72421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to map a fence separating a stretch of railroad tracks from a bike road. The fence is definitely property of the railroad company. It runs below the embankment and right along the road (no distance to the road but several meters to the tracks). There are some locked gates (maintenance access) in the fence that I'd want to add. Can I map the fence as a barrier along the road and where would a gate show up in a router? Would it be interpreted as a gate blocking the road? Alternatively, do I need to add it as a separate line object?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gate" rel="tag" title="see questions tagged &#39;gate&#39;">gate</span> <span class="post-tag tag-link-railroad" rel="tag" title="see questions tagged &#39;railroad&#39;">railroad</span> <span class="post-tag tag-link-barrier" rel="tag" title="see questions tagged &#39;barrier&#39;">barrier</span> <span class="post-tag tag-link-fence" rel="tag" title="see questions tagged &#39;fence&#39;">fence</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jan '20, 20:47</strong></p>
<img src="https://secure.gravatar.com/avatar/8565c35b65c7735935f8238c05f1e8d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="UliFR&#39;s gravatar image" />
<p><span>UliFR</span><br />
<span class="score" title="116 reputation points">116</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="UliFR has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72421" class="comments-container">
<span id="72688"></span>
<div id="comment-72688" class="comment">
<div id="post-72688-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, separated the fence. Thanks</p>
</div>
<div id="comment-72688-info" class="comment-info">
<span class="comment-age">(26 Jan '20, 14:37)</span> <span class="comment-user userinfo">UliFR</span>
</div>
</div>
</div>
<div id="comment-tools-72421" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72421-form-container" class="comment-form-container">
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

<span id="72424"></span>

<div id="answer-container-72424" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72424-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-72424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no problem that I can think of in mapping the fence. With respect to gates, I'd probably try to map them as short ways if I could do so accurately. If I couldn't (not being able to see them clearly in imagery, lack of accurate on the ground survey, etc.) then I'd map them as points.</p>
<p>There may be renderers that incorrectly orient their gate icons if they are mapped as points near a road. I know my renderer would do this wrong. If there is any evidence of a service roads or tracks, even just a few meters long, that go through the gate(s) that could assist the rendering as well as being accurate mapping.</p>
<p>But you shouldn't worry about if they will be rendered properly, just that they are mapped accurately. Map the fence where the fence is. Map the locations of gates with ways showing the length of each gate if possible. But if not possible, just use barrier nodes/points.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '20, 22:40</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-72424" class="comments-container">
<span id="72427"></span>
<div id="comment-72427" class="comment">
<div id="post-72427-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>to be super clear: the road and the fence are 2 separate OSM-ways. Do not add the barrier=fence tag to the highway=xxx-tagged way.</p>
</div>
<div id="comment-72427-info" class="comment-info">
<span class="comment-age">(08 Jan '20, 04:00)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="72428"></span>
<div id="comment-72428" class="comment">
<div id="post-72428-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>escada is correct and my answer was unclear on this. Thank you for the update/clarification!</p>
</div>
<div id="comment-72428-info" class="comment-info">
<span class="comment-age">(08 Jan '20, 05:10)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="72429"></span>
<div id="comment-72429" class="comment">
<div id="post-72429-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, so I need the extra fence object. Is that a general rule that one should not to add barrier=fence tags to highways or is this only because of the gate problem I raised?</p>
</div>
<div id="comment-72429-info" class="comment-info">
<span class="comment-age">(08 Jan '20, 08:08)</span> <span class="comment-user userinfo">UliFR</span>
</div>
</div>
<span id="72430"></span>
<div id="comment-72430" class="comment">
<div id="post-72430-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>It is best practice to map one real life feature by one OSM object each.</p>
<p>In this specific case mapping raod and fence on the same line would be ambiguous: Is the fence on the left side of the road, on the right? Or is it a barrier on the road itself stopping traffic? Or a divider between the lanes?</p>
</div>
<div id="comment-72430-info" class="comment-info">
<span class="comment-age">(08 Jan '20, 08:18)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-72424" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72424-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72431"></span>

<div id="answer-container-72431" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72431-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-72431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Certainly do not add barrier=fence to the existing highway this is likely to cause at least some routing engines to treat the road as impassable.</p>
<p>As others have said add the fence parallel to the road. You can add the gates as ways or points, but probably only the latter get shown on the standard CartoCSS render. If the gates are on potentially routable roads (e.g. service roads) it may be better to use nodes for now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '20, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-72431" class="comments-container">
&#10;</div>
<div id="comment-tools-72431" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72431-form-container" class="comment-form-container">
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

