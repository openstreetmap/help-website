+++
type = "question"
title = "How to map Center Turn Lanes?"
description = '''Specifically, what are the lanes, turn:lanes, and change:lanes tags for the following example? https://www.branson.com/wp/wp-content/uploads/2017/03/170323-Center-Lane-1024x683.jpg This is what I have so far: lanes = 3 lanes:forward = 1 lanes:backward = 1 lanes:both_ways = 1 turn:lanes:both_ways = l...'''
date = "2018-07-09T21:41:00Z"
lastmod = "2018-12-06T17:21:00Z"
weight = 64617
keywords = [ "centre_turn_lane", "lanes", "turnlanes" ]
aliases = [ "/questions/64617" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to map Center Turn Lanes?](/questions/64617/how-to-map-center-turn-lanes)

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
<span id="post-64617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64617-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-64617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Specifically, what are the <strong>lanes</strong>, <strong>turn:lanes</strong>, and <strong>change:lanes</strong> tags for the following example?</p>
<p><a href="https://www.branson.com/wp/wp-content/uploads/2017/03/170323-Center-Lane-1024x683.jpg">https://www.branson.com/wp/wp-content/uploads/2017/03/170323-Center-Lane-1024x683.jpg</a></p>
<p>This is what I have so far:</p>
<p>lanes = 3</p>
<p>lanes:forward = 1</p>
<p>lanes:backward = 1</p>
<p>lanes:both_ways = 1</p>
<p>turn:lanes:both_ways = left</p>
<p>change:lanes = ??</p>
<p>I was also wondering if the <a href="https://wiki.openstreetmap.org/wiki/Key:centre_turn_lane">centre_ turn_lane</a> tag would be applicable in this scenario?</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-centre_turn_lane" rel="tag" title="see questions tagged &#39;centre_turn_lane&#39;">centre_turn_lane</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-turnlanes" rel="tag" title="see questions tagged &#39;turnlanes&#39;">turnlanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '18, 21:41</strong></p>
<img src="https://secure.gravatar.com/avatar/74ace9f12d8a8354d511ea87b04f4bba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MeghanKNg&#39;s gravatar image" />
<p><span>MeghanKNg</span><br />
<span class="score" title="171 reputation points">171</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MeghanKNg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64617" class="comments-container">
&#10;</div>
<div id="comment-tools-64617" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64617-form-container" class="comment-form-container">
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

<span id="64619"></span>

<div id="answer-container-64619" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64619-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-64619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MeghanKNg has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tags you have so far (<code>lanes</code>, <code>lanes:forward</code>, <code>lanes:backward</code>, <code>lanes:both_ways</code>, and <code>turn:lanes:both_ways</code>) is all you need.</p>
<p><code>change:lanes</code> is not needed in this case as you can change into or out of that lane at any place which is the default assumption for where you can change lanes.</p>
<p><code>centre_turn_lane</code> is, I think, an earlier attempt to tag the situation but I don't think it is current tagging practice.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '18, 23:20</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-64619" class="comments-container">
<span id="67085"></span>
<div id="comment-67085" class="comment">
<div id="post-67085-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi stf, can you further explain why you wouldn't need the change:lanes tag for center turn lanes with lanes:both_ways?? Does this only apply to the above example or would it be the same for say: lanes = 5, lanes:forward = 2, lanes:backward = 2, lanes:both_ways = 1</p>
<p>On overpass turbo, for the 5 lanes tag I have found people use these tags:</p>
<p>change:lanes:backward = not_left|yes, change:lanes:both_ways = yes, change:lanes:forward = not_left|yes,</p>
<p>On overpass turbo, for the 3 lanes (above example) tag I have found people use these tags:</p>
<p>change:lanes:backward = not_left, change:lanes:both_ways = yes, change:lanes:forward = not_left,</p>
<p>Thanks</p>
</div>
<div id="comment-67085-info" class="comment-info">
<span class="comment-age">(06 Dec '18, 17:21)</span> <span class="comment-user userinfo">ragingtoro</span>
</div>
</div>
</div>
<div id="comment-tools-64619" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64619-form-container" class="comment-form-container">
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

