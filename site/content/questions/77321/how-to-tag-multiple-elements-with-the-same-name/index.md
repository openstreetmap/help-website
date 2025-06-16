+++
type = "question"
title = "How to tag multiple elements with the same name?"
description = '''I&#x27;m mapping a natural area where some of the ponds are named in pairs or more, like (translated) &quot;The Beaver Ponds&quot; which refers to two nearby but separate ponds. I can make the ponds as a single multipolygon where each separate pond is an outer, and name that multipolygon &quot;The Beaver Ponds&quot;. To me ...'''
date = "2020-10-30T12:07:00Z"
lastmod = "2020-10-31T11:45:00Z"
weight = 77321
keywords = [ "naming", "multipolygon" ]
aliases = [ "/questions/77321" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag multiple elements with the same name?](/questions/77321/how-to-tag-multiple-elements-with-the-same-name)

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
<span id="post-77321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77321-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-77321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm mapping a natural area where some of the ponds are named in pairs or more, like (translated) "The Beaver Ponds" which refers to two nearby but separate ponds. I can make the ponds as a single multipolygon where each separate pond is an outer, and name that multipolygon "The Beaver Ponds". To me that feels logical from a database perspective. However, the the OSM renderer seems to put the name only in the biggest pond, instead of placing the name somewhere inbetween all the ponds, like it's done in the official maps.</p>
<p>Is that possible to achieve?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-naming" rel="tag" title="see questions tagged &#39;naming&#39;">naming</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '20, 12:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d04f4c51fab1e216224e5a7ae978b311?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="torger&#39;s gravatar image" />
<p><span>torger</span><br />
<span class="score" title="220 reputation points">220</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="torger has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77321" class="comments-container">
&#10;</div>
<div id="comment-tools-77321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77321-form-container" class="comment-form-container">
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

<span id="77324"></span>

<div id="answer-container-77324" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77324-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could map the individual ponds and then put them into a relation of types <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Group_Relation">group</a> or <a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Cluster">cluster</a>.</p>
<p>Have a look at a <a href="/questions/72769/is-there-a-relationsite-variant-to-use-for-natural-objects">related question</a> from earlier this year on the usage of these.</p>
<p>I have no idea how names would be rendered using these relations but <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">you shouldn't worry about that</a> as every map provider can do that differently anyway. Just make sure the data is entered correctly within our data model.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '20, 14:35</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-77324" class="comments-container">
<span id="77337"></span>
<div id="comment-77337" class="comment">
<div id="post-77337-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks, I went for the group tagging. Unfortunately names doesn't seem to be rendered at all. I know I shouldn't tag for the renderer, but unfortunately the often stated "don't worry how it renders" is like saying "don't worry if you make a useful map or not". I think it's a major problem when the default renderer, which does end up being used as a "end user map" in several ocassions, can't render features that is standard on any official map. It's frustrating when all hard work tagging ends up just invisible. And sometimes it's the other way around, like visible river names inside lakes... <strong><em>aaaarrgghhh</em></strong>. Well, sorry, I just got a minor outburst of frustration.</p>
</div>
<div id="comment-77337-info" class="comment-info">
<span class="comment-age">(31 Oct '20, 11:45)</span> <span class="comment-user userinfo">torger</span>
</div>
</div>
</div>
<div id="comment-tools-77324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77324-form-container" class="comment-form-container">
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

