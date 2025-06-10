+++
type = "question"
title = "Merge layer in JOSM"
description = '''In JOSM I need to merge the changed layer with the existing data layer. My question is why I need a merge. What will happen if I upload layer without merging?'''
date = "2019-01-27T09:34:00Z"
lastmod = "2019-01-27T10:35:00Z"
weight = 67753
keywords = [ "josm", "layer", "josm_8969", "merge" ]
aliases = [ "/questions/67753" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Merge layer in JOSM](/questions/67753/merge-layer-in-josm)

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
<span id="post-67753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67753-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In JOSM I need to merge the changed layer with the existing data layer. My question is why I need a merge. What will happen if I upload layer without merging?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-josm_8969" rel="tag" title="see questions tagged &#39;josm_8969&#39;">josm_8969</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '19, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7da63bcb858ed2c1e1f25aa2d3d00106?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_partha&#39;s gravatar image" />
<p><span>_partha</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_partha has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jan '19, 11:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-67753" class="comments-container">
<span id="67756"></span>
<div id="comment-67756" class="comment">
<div id="post-67756-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>is there a special reason for the tag josm_8969?</p>
</div>
<div id="comment-67756-info" class="comment-info">
<span class="comment-age">(27 Jan '19, 10:35)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67753-form-container" class="comment-form-container">
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

<span id="67755"></span>

<div id="answer-container-67755" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67755-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="_partha has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You do not need to technically merge your new data layer to a data layer which you have downloaded from the server. All your new data in your layer will be merged to the main database on upload. Note that by "merged" I mean (in simple words) that e.g. if you draw a new street where there is already a street in the main database, then you will have two streets placed on top of each other while being not connected to each other. Since we usually want no duplicate object and want a connected street network (for routing), you usually would want to <em>avoid this</em>.</p>
<p>Usually you <em>rather want</em> to first download data from the server, then edit this layer and then upload it.</p>
<p>An option is this (which you possibly described in your question): You download the existing data, start a new data layer and do your additions, merge both layers, connect streets (and similar objects) and check that you did not create any duplicated objects, and then upload the merged layer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '19, 10:35</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-67755" class="comments-container">
&#10;</div>
<div id="comment-tools-67755" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67755-form-container" class="comment-form-container">
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

