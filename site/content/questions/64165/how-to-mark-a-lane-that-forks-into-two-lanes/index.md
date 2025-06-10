+++
type = "question"
title = "How to mark a lane that forks into two lanes?"
description = '''In the link below is an example of the scenario (pretend that the cars are going in the opposite direction). I have seen proposed documentation about transit:lanes=fork, but that was rejected when I checked today. Thank you! https://www.rsc.wa.gov.au/RSC/media/SiteImages/Videos/merging-video-teaser....'''
date = "2018-06-11T23:51:00Z"
lastmod = "2018-06-12T09:03:00Z"
weight = 64165
keywords = [ "fork", "lane", "split", "road" ]
aliases = [ "/questions/64165" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to mark a lane that forks into two lanes?](/questions/64165/how-to-mark-a-lane-that-forks-into-two-lanes)

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
<span id="post-64165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64165-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the link below is an example of the scenario (pretend that the cars are going in the opposite direction). I have seen proposed documentation about transit:lanes=fork, but that was rejected when I checked today. Thank you!</p>
<p><a href="https://www.rsc.wa.gov.au/RSC/media/SiteImages/Videos/merging-video-teaser.jpg">https://www.rsc.wa.gov.au/RSC/media/SiteImages/Videos/merging-video-teaser.jpg</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-fork" rel="tag" title="see questions tagged &#39;fork&#39;">fork</span> <span class="post-tag tag-link-lane" rel="tag" title="see questions tagged &#39;lane&#39;">lane</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jun '18, 23:51</strong></p>
<img src="https://secure.gravatar.com/avatar/74ace9f12d8a8354d511ea87b04f4bba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MeghanKNg&#39;s gravatar image" />
<p><span>MeghanKNg</span><br />
<span class="score" title="171 reputation points">171</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MeghanKNg has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jun '18, 23:53</strong> </span></p>
</div>
</div>
<div id="comments-container-64165" class="comments-container">
&#10;</div>
<div id="comment-tools-64165" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64165-form-container" class="comment-form-container">
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

<span id="64168"></span>

<div id="answer-container-64168" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64168-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-64168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MeghanKNg has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is sufficient to just map the <a href="https://wiki.openstreetmap.org/wiki/Lanes"><code>lanes</code></a> of the road. Mapped lanes implicitly contain forks.</p>
<p>Example using your picture (I've reversed the car's driving direction with my incredible paint skills ;)):</p>
<p><img src="https://help.openstreetmap.org/upfiles/merging-video-teaser_PtUPgPZ.jpg" alt="example image" /></p>
<p>Also consider mapping <code>turn:lanes</code>. The wiki page about <a href="https://wiki.openstreetmap.org/wiki/Lanes"><code>lanes</code></a> is really helpful and has nice examples.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '18, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jun '18, 12:27</strong> </span></p>
</div>
</div>
<div id="comments-container-64168" class="comments-container">
<span id="64169"></span>
<div id="comment-64169" class="comment">
<div id="post-64169-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've deleted my answer, as I seem to have got lanes:forward and lanes:backward swapped (I blame my driving on the left).</p>
</div>
<div id="comment-64169-info" class="comment-info">
<span class="comment-age">(12 Jun '18, 09:03)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64168-form-container" class="comment-form-container">
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

