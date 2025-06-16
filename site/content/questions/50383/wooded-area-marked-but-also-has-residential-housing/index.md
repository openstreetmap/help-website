+++
type = "question"
title = "Wooded area marked but also has residential housing"
description = '''I am new to this. I am trying to help out with areas I know. These areas are 2 acre residential lots. The current polygons seem very sporadic and will require lots of editing. Just trying to figure out how to go about mapping these. Would what have be correct? '''
date = "2016-06-22T14:02:00Z"
lastmod = "2016-06-22T16:59:00Z"
weight = 50383
keywords = [ "residential", "woodland" ]
aliases = [ "/questions/50383" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wooded area marked but also has residential housing](/questions/50383/wooded-area-marked-but-also-has-residential-housing)

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
<span id="post-50383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50383-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to this. I am trying to help out with areas I know. These areas are 2 acre residential lots. The current polygons seem very sporadic and will require lots of editing. Just trying to figure out how to go about mapping these. Would what have be correct?</p>
<p><img src="http://i.imgur.com/yNp7ODE.png" alt="screenshot" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-residential" rel="tag" title="see questions tagged &#39;residential&#39;">residential</span> <span class="post-tag tag-link-woodland" rel="tag" title="see questions tagged &#39;woodland&#39;">woodland</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '16, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/687d4ccef19d24b7b1128eb308a25440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbinott&#39;s gravatar image" />
<p><span>dbinott</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbinott has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-50383" class="comments-container">
<span id="50384"></span>
<div id="comment-50384" class="comment">
<div id="post-50384-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For info, that's here I believe:</p>
<p><a href="https://www.openstreetmap.org/way/426571814">https://www.openstreetmap.org/way/426571814</a></p>
</div>
<div id="comment-50384-info" class="comment-info">
<span class="comment-age">(22 Jun '16, 14:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50385"></span>
<div id="comment-50385" class="comment">
<div id="post-50385-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, that is it.</p>
</div>
<div id="comment-50385-info" class="comment-info">
<span class="comment-age">(22 Jun '16, 14:11)</span> <span class="comment-user userinfo">dbinott</span>
</div>
</div>
</div>
<div id="comment-tools-50383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50383-form-container" class="comment-form-container">
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

<span id="50389"></span>

<div id="answer-container-50389" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50389-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dbinott has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>landuse=residential natural=wood on the same way doesn't make much sense here, but maybe you don't realize you can overlap different layers?</p>
<p>Way 426571814 does seem like a residential area, but is not entirely tree-covered so I would remove the natural=wood tag from this way. To indicate the area that is tree-covered, you could create a new way following the treeline that is tagged natural=wood. There might be areas (like near the road to the southernmost edge) where the residential way and the wood way overlap, but mostly in this case the wood way will be a separate way within the residential way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '16, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-50389" class="comments-container">
<span id="50391"></span>
<div id="comment-50391" class="comment">
<div id="post-50391-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>sounds good. thanks!</p>
</div>
<div id="comment-50391-info" class="comment-info">
<span class="comment-age">(22 Jun '16, 16:59)</span> <span class="comment-user userinfo">dbinott</span>
</div>
</div>
</div>
<div id="comment-tools-50389" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50389-form-container" class="comment-form-container">
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

