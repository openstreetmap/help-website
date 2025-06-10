+++
type = "question"
title = "source:maxspeed for 2 directions"
description = '''I would like to tag source:maxspeed for 2 directions (forward and backward) on the same road and same part. The tags are:  one direction (forward) source:maxspeed=country_code:urban opposite direction (backward) source:maxspeed=country_code:rural  Do I have to tag it &quot;source:maxspeed:forward/backwar...'''
date = "2017-09-15T16:52:00Z"
lastmod = "2017-09-17T19:41:00Z"
weight = 59642
keywords = [ "source", "maxspeed" ]
aliases = [ "/questions/59642" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [source:maxspeed for 2 directions](/questions/59642/sourcemaxspeed-for-2-directions)

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
<span id="post-59642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to tag <em>source:maxspeed</em> for 2 directions (forward and backward) on the same road and same part. The tags are:</p>
<ul>
<li>one direction (forward) <em>source:maxspeed=country_code:urban</em></li>
<li>opposite direction (backward) <em>source:maxspeed=country_code:rural</em></li>
</ul>
<p>Do I have to tag it "source:maxspeed:forward/backward"? The information is missing in the wiki (<a href="https://wiki.openstreetmap.org/wiki/Key:source:maxspeed)">https://wiki.openstreetmap.org/wiki/Key:source:maxspeed)</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '17, 16:52</strong></p>
<img src="https://secure.gravatar.com/avatar/fd25f3f852898d7266f2233aeec47808?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="istefanos&#39;s gravatar image" />
<p><span>istefanos</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="istefanos has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59642" class="comments-container">
<span id="59643"></span>
<div id="comment-59643" class="comment">
<div id="post-59643-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Is it really true that one side of a road is rural and one side urban? Does the place boundary go down the middle of the road?</p>
<p>If this isn't the case, then presumably you shouldn't be using "source:maxspeed" (where you can derive a maxspeed purely from road location - common in some places, not in others) but some other tag - perhaps "maxspeed:type"?</p>
</div>
<div id="comment-59643-info" class="comment-info">
<span class="comment-age">(15 Sep '17, 17:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="59644"></span>
<div id="comment-59644" class="comment">
<div id="post-59644-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have almost entirely stopped using source:<em>=</em> tags as it really should duplicate the information found in the change set comments.</p>
<p>That being said, there are some sections of roads with different speed limits on on each side. I'd tag those maxspeed:forward= <em>and maxspeed:backward=</em>. If one really wanted to put source tags on that, then I'd use source:maxspeed:forward= <em>and source:maxspeed:backward=</em>.</p>
</div>
<div id="comment-59644-info" class="comment-info">
<span class="comment-age">(15 Sep '17, 23:15)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="59645"></span>
<div id="comment-59645" class="comment">
<div id="post-59645-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think source tags are very important and, especially in certain cases, can be invaluable. For example, I just used a source:maxspeed tag to locate a Mapillary image that was used to set the maxspeed incorrectly. Fortunately, the original mapper had used the source:maxspeed tag containing a Mapillary URL.</p>
<p>Putting such information in the changeset comment is fine as long as the changeset is small but often they contain too many additions or edits to make that a practical solution in all situations.</p>
</div>
<div id="comment-59645-info" class="comment-info">
<span class="comment-age">(16 Sep '17, 02:06)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="59652"></span>
<div id="comment-59652" class="comment">
<div id="post-59652-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>SomeoneElse, yes, it is true. In slovakia and hungary I know some places, e.g. "47.8484, 18.1719" (forward) and "47.84275, 18.17141" (backward) by mapillary captures.</p>
<p>stf, I did it the same way, but I did not find any documentation.</p>
</div>
<div id="comment-59652-info" class="comment-info">
<span class="comment-age">(16 Sep '17, 23:05)</span> <span class="comment-user userinfo">istefanos</span>
</div>
</div>
</div>
<div id="comment-tools-59642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59642-form-container" class="comment-form-container">
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

<span id="59658"></span>

<div id="answer-container-59658" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59658-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-59658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The :forward and :backward suffixes can be used for many traffic-related keys, even if that possibility is not always mentioned explicitly in the wiki. In this case, there's also more than ten thousand instances of each the two keys already in the database.</p>
<p>So yes, use <strong><code>source:maxspeed:forward/backward</code></strong> for this. (Assuming this actually represents the on-the-ground situation correctly, of course.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '17, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-59658" class="comments-container">
&#10;</div>
<div id="comment-tools-59658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59658-form-container" class="comment-form-container">
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

