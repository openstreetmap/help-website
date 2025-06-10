+++
type = "question"
title = "How can snowshoeing access be prohibited?"
description = '''There are a number of trails that I want to correct the access of. These trails do not allow access with snowshoes (as that destroys the cross-country ski access). Is there a way to do this in OpenStreetMap?'''
date = "2021-01-28T20:04:00Z"
lastmod = "2021-01-29T00:24:00Z"
weight = 78583
keywords = [ "access", "snowshoe" ]
aliases = [ "/questions/78583" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can snowshoeing access be prohibited?](/questions/78583/how-can-snowshoeing-access-be-prohibited)

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
<span id="post-78583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78583-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are a number of trails that I want to correct the access of. These trails do not allow access with snowshoes (as that destroys the cross-country ski access). Is there a way to do this in OpenStreetMap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-snowshoe" rel="tag" title="see questions tagged &#39;snowshoe&#39;">snowshoe</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '21, 20:04</strong></p>
<img src="https://secure.gravatar.com/avatar/9284c5dbd2d102b8fead808560839269?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Patel-Schneider&#39;s gravatar image" />
<p><span>Peter Patel-...</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Patel-Schneider has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '21, 20:45</strong> </span></p>
</div>
</div>
<div id="comments-container-78583" class="comments-container">
&#10;</div>
<div id="comment-tools-78583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78583-form-container" class="comment-form-container">
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

<span id="78584"></span>

<div id="answer-container-78584" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78584-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Peter -- There's an undocumented but well-established <strong><code>"snowshoe"</code></strong> access tag. Just add <strong><code>"snowshoe=no"</code></strong> to the trails in question.</p>
<p>If all foot traffic is prohibited, regardless of the footwear, just using <strong><code>"foot=no"</code></strong> is probably easier, though you could still add <strong><code>"snowshoe=no"</code></strong> to be extra explicit.</p>
<p>If foot traffic is prohibited regardless of the footwear but <em>only</em> during snow, you could try <strong><code>"foot=yes"</code></strong> + <strong><code>"foot:conditional=no @ (snow)"</code></strong>, but in that case I'd definitely also add <strong><code>"snowshoe=no"</code></strong> because you never know if someone's actually going to read the conditional access tags.</p>
<p>By the way, if there's a sign or a published regulation that corresponds to this restriction, it would be a good idea to cite that in your change comment.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '21, 21:42</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '21, 21:43</strong> </span></p>
</div>
</div>
<div id="comments-container-78584" class="comments-container">
&#10;</div>
<div id="comment-tools-78584" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78584-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78587"></span>

<div id="answer-container-78587" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78587-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks.</p>
<p>This is the likely tagging, with one last round of discussion with the owners.</p>
<p>access=private vehicle=no agricultural=private forestry=private atv=private bicycle=no snowmobile=no foot=private foot:conditional=permissive @ ( Apr 15-Nov 30 dawn-dusk ) dog=private ski=private snowshoe=no ski:nordic:conditional=permissive @ ( dawn-dusk ) horse=no hunting=no</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '21, 00:24</strong></p>
<img src="https://secure.gravatar.com/avatar/9284c5dbd2d102b8fead808560839269?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Patel-Schneider&#39;s gravatar image" />
<p><span>Peter Patel-...</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Patel-Schneider has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jan '21, 00:25</strong> </span></p>
</div>
</div>
<div id="comments-container-78587" class="comments-container">
&#10;</div>
<div id="comment-tools-78587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78587-form-container" class="comment-form-container">
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

