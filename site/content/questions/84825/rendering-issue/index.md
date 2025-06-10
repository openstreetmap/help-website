+++
type = "question"
title = "Rendering Issue"
description = '''I just edited the features in a school. When I look at it on the standard map, it looks fine as long as I am zoomed out. But when I zoom in to the maximum zoom level or even one level above the maximum zoom level, most of the features I added disappear and some of appear distorted or clipped. I was ...'''
date = "2022-06-19T20:00:00Z"
lastmod = "2022-06-19T20:21:00Z"
weight = 84825
keywords = [ "rendering", "clipping", "rendering_error", "features" ]
aliases = [ "/questions/84825" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Rendering Issue](/questions/84825/rendering-issue)

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
<span id="post-84825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84825-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just edited the features in a school. When I look at it on the standard map, it looks fine as long as I am zoomed out. But when I zoom in to the maximum zoom level or even one level above the maximum zoom level, most of the features I added disappear and some of appear distorted or clipped. I was wondering what the cause of the issue was and if there was some way to fix it. The location of the school is 37.85775,-122.26273. I have attached an image of the issue below. This is what it looks like zoomed out:</p>
<p><img src="https://media.discordapp.net/attachments/867875954318639164/988139895170166834/unknown.png" alt="alt text" /></p>
<p>This is what it looks like zoomed to the maximum level: <img src="https://media.discordapp.net/attachments/867875954318639164/988140236309676062/unknown.png?width=1229&amp;height=609" alt="alt text" /></p>
<p>This is what is looks like in edit mode: <img src="https://media.discordapp.net/attachments/867875954318639164/988155654873157662/unknown.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-clipping" rel="tag" title="see questions tagged &#39;clipping&#39;">clipping</span> <span class="post-tag tag-link-rendering_error" rel="tag" title="see questions tagged &#39;rendering_error&#39;">rendering_error</span> <span class="post-tag tag-link-features" rel="tag" title="see questions tagged &#39;features&#39;">features</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '22, 20:00</strong></p>
<img src="https://secure.gravatar.com/avatar/8c1d94ee91ebf9f6a93ecf416c22bafb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PoultryPants&#39;s gravatar image" />
<p><span>PoultryPants</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PoultryPants has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '22, 20:00</strong> </span></p>
</div>
</div>
<div id="comments-container-84825" class="comments-container">
&#10;</div>
<div id="comment-tools-84825" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84825-form-container" class="comment-form-container">
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

<span id="84827"></span>

<div id="answer-container-84827" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84827-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-84827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PoultryPants has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tiles for the different zoom levels don't always get regenerated at exactly the same rate. So it's quite common to see odd things happening when you zoom in and out a short time after making a change. (It's also worth checking that you don't have old tiles in your local cache, but I think in this example that's probably not the issue). A little bit of patience should see everything sorted out.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '22, 20:21</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</img>
</div>
</div>
<div id="comments-container-84827" class="comments-container">
&#10;</div>
<div id="comment-tools-84827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84827-form-container" class="comment-form-container">
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

