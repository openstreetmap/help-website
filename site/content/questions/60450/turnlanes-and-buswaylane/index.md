+++
type = "question"
title = "&quot;turn:lanes&quot; and &quot;busway:lane&quot;"
description = '''How can I tag &quot;turn:lanes&quot; when a bus lane is in the middle? See picture below &quot;turn:lanes&quot;=&quot;left;through|right&quot; or &quot;turn:lanes&quot;=&quot;left;through|none|right&quot; ...?'''
date = "2017-11-03T12:23:00Z"
lastmod = "2017-11-10T18:43:00Z"
weight = 60450
keywords = [ "turn", "lane", "lanes", "bus" ]
aliases = [ "/questions/60450" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# ["turn:lanes" and "busway:lane"](/questions/60450/turnlanes-and-buswaylane)

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
<span id="post-60450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60450-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I tag "turn:lanes" when a bus lane is in the middle?</p>
<p><a href="https://www.mapillary.com/map/im/eXia0niI2aiW2LJ3TJfYYA">See picture below</a></p>
<p>"turn:lanes"="left;through|right" or "turn:lanes"="left;through|none|right" ...?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turn" rel="tag" title="see questions tagged &#39;turn&#39;">turn</span> <span class="post-tag tag-link-lane" rel="tag" title="see questions tagged &#39;lane&#39;">lane</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '17, 12:23</strong></p>
<img src="https://secure.gravatar.com/avatar/fd25f3f852898d7266f2233aeec47808?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="istefanos&#39;s gravatar image" />
<p><span>istefanos</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="istefanos has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Nov '17, 12:30</strong> </span></p>
</div>
</div>
<div id="comments-container-60450" class="comments-container">
&#10;</div>
<div id="comment-tools-60450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60450-form-container" class="comment-form-container">
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

<span id="60453"></span>

<div id="answer-container-60453" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60453-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I haven't mapped bus lanes (yet) so this is just a first attempt at thinking this through.</p>
<p>First, it appears there are three lanes:</p>
<p>lanes=3</p>
<p>I can't see turn lane markings in the center lane but the two outer lanes have them:</p>
<p>turn:lanes=left;though|none|right</p>
<p>I assume busses may use the outside lanes:</p>
<p>psv:lanes=yes|designated|yes</p>
<p>I am not sure if non-bus access is picked up from the psv tag or not, so I might add</p>
<p>access:lanes=yes|psv|yes</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '17, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-60453" class="comments-container">
<span id="60457"></span>
<div id="comment-60457" class="comment">
<div id="post-60457-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Small correction: psv is a vehicle type, and can therefore not be used as value. The last tag should be <code>access:lanes=yes|no|yes</code> instead. (For psv, the "no" is overriden by the "designated" from the more specific <code>psv:lanes</code> tag, but everyone else is excluded.)</p>
</div>
<div id="comment-60457-info" class="comment-info">
<span class="comment-age">(03 Nov '17, 20:11)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-60453" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60453-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60503"></span>

<div id="answer-container-60503" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60503-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>stf and Tordanik, thank You for Your answers, I keep tagging it this way "turn:lanes=left;through|none|right"</p>
<p>I am not sure if tagging "psv:lanes" accepts "yes" or "no", I did not find any documentation about it. I found only "lanes:psv" with number values:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Bus_lanes">Bus lanes</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/Key:lanes:psv">lanes:psv</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '17, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/fd25f3f852898d7266f2233aeec47808?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="istefanos&#39;s gravatar image" />
<p><span>istefanos</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="istefanos has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60503" class="comments-container">
<span id="60540"></span>
<div id="comment-60540" class="comment">
<div id="post-60540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The extension :lanes can be appended to all keys to make them apply on a per-lane basis instead of the road as a whole. The values stay the same, and usually, there's no special wikipage created for the per-lane variant. So when looking for documentation on such a key, it's best to look for the base key (in this case, psv).</p>
<p>As such, documentation on the values is found at <a href="https://wiki.openstreetmap.org/wiki/Key:psv">Key:psv</a>, and especially the main <a href="https://wiki.openstreetmap.org/wiki/Key:access">Key:access</a> page that is linked from there.</p>
</div>
<div id="comment-60540-info" class="comment-info">
<span class="comment-age">(10 Nov '17, 18:43)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-60503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60503-form-container" class="comment-form-container">
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

