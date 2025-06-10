+++
type = "question"
title = "Shared Space Tagging Conventions"
description = '''Hi there,  I am trying to change the tagging of some city centre pedestrian shared use paths so they can be better consumed by providers such as Cycle OSM, and properly marked as such on these services. I am in the UK, and I was wondering what the tagging convention would be for such a path - shared...'''
date = "2021-10-29T11:17:00Z"
lastmod = "2021-10-30T09:57:00Z"
weight = 82406
keywords = [ "shared", "pedestrians" ]
aliases = [ "/questions/82406" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Shared Space Tagging Conventions](/questions/82406/shared-space-tagging-conventions)

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
<span id="post-82406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82406-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I am trying to change the tagging of some city centre pedestrian shared use paths so they can be better consumed by providers such as Cycle OSM, and properly marked as such on these services.</p>
<p>I am in the UK, and I was wondering what the tagging convention would be for such a path - shared by pedestrians and cyclists, no marked delineation between the two and no usual access for cars.</p>
<p>Regards,</p>
<p>Harvey</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shared" rel="tag" title="see questions tagged &#39;shared&#39;">shared</span> <span class="post-tag tag-link-pedestrians" rel="tag" title="see questions tagged &#39;pedestrians&#39;">pedestrians</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Oct '21, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/f70df2a55314d25a2ac294a519837641?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hblu&#39;s gravatar image" />
<p><span>hblu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hblu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82406" class="comments-container">
<span id="82422"></span>
<div id="comment-82422" class="comment">
<div id="post-82422-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Please ask on the talk-gb mailing list. The developers of cycle.travel , Cyclestreets and OpenCycleMap are all active on that list. As both services have been in use for some considerable time I would expect they will have picked up any significant routing issues some time ago. It is also advisable to stick to current (UK) local conventions, and please avoid tagging for one specific renderer (CycleOSM)</p>
<p>Note the recommendation of highway=path on the wiki, does not necessarily accord with consensus tagging in the UK for cycle infra.</p>
</div>
<div id="comment-82422-info" class="comment-info">
<span class="comment-age">(30 Oct '21, 09:57)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82406-form-container" class="comment-form-container">
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

<span id="82421"></span>

<div id="answer-container-82421" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82421-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mainly you are looking for <code>segregated=no</code>. <code> highway=path foot=designated bicycle=designated segregated=no surface=paved </code> or <code> highway=cycleway foot=designated segregated=no surface=paved </code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '21, 08:09</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Oct '21, 10:27</strong> </span></p>
</div>
</div>
<div id="comments-container-82421" class="comments-container">
&#10;</div>
<div id="comment-tools-82421" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82421-form-container" class="comment-form-container">
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

