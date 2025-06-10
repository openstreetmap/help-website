+++
type = "question"
title = "How to tag parts of a building which cross a road and are part of a multipolygon?"
description = '''I have a problem with the mall that I have fiddled with in this changeset. The problem is that the two building parts 370434881 and 370434882 cross a road. They are first-floor parts of the mall where the road passes under. You can see them in for example this picture: I suppose I could try tagging ...'''
date = "2017-10-25T12:31:00Z"
lastmod = "2017-10-27T20:14:00Z"
weight = 60298
keywords = [ "building", "covered", "layer" ]
aliases = [ "/questions/60298" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag parts of a building which cross a road and are part of a multipolygon?](/questions/60298/how-to-tag-parts-of-a-building-which-cross-a-road-and-are-part-of-a-multipolygon)

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
<span id="post-60298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60298-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a problem with the mall that I have fiddled with in <a href="https://www.openstreetmap.org/changeset/53202753#map=18/57.04728/9.92735">this changeset</a>. The problem is that the two building parts 370434881 and 370434882 cross a road. They are first-floor parts of the mall where the road passes under. You can see them in for example this picture:<img src="https://migogaalborg.dk/wp-content/uploads/2016/06/Friis-edit.jpg" alt="alt text" /></p>
<p>I suppose I could try tagging them like the nearby passage through the building part 370411677, but I think of these parts of the mall as less of a tunnel through a building than smaller building parts crossing the road.</p>
<p>I have currently tried tagging the building parts as <code>level=1</code> and the the parts of the road beneath them as <code>covered=yes</code>. This usually works for roofs over gas stations etc., but in this case here, the road parts are not rendered as covered by the building. I suspect this is because the building parts are members of the larger mall multipolygon 441887338 which is tagged as a building and is implicitly layer 0?</p>
<p>How would you suggest tagging this situation to get the road correctly rendered as covered by the buildings?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-covered" rel="tag" title="see questions tagged &#39;covered&#39;">covered</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '17, 12:31</strong></p>
<img src="https://secure.gravatar.com/avatar/299be62a6d830e72cba2f73d38fcc3f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThomasA&#39;s gravatar image" />
<p><span>ThomasA</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThomasA has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-60298" class="comments-container">
&#10;</div>
<div id="comment-tools-60298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60298-form-container" class="comment-form-container">
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

<span id="60300"></span>

<div id="answer-container-60300" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60300-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-60300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>How would you suggest tagging this situation to get the road correctly rendered as covered by the buildings?</p>
</blockquote>
<p>This is not the question you should be asking. Instead, you should be asking a question like, "How would you suggest tagging this situation to best represent the reality on-the-ground?" The rendering will vary depending on the data consumer, so don't worry about that part. Just make sure the objects are tagged as accurately as you can.</p>
<p>As for how I would tag it, I would tag the building part as layer=1 (because it physically crosses above the implicit layer=0 highway) and the highway underneath as covered=yes. At the time of my writing this, it appears that this is how these objects are already tagged, so I don't see any reason to change anything. The "Standard" rendering at osm.org renders highways differently when tagged with covered=yes, so there's already an indication that a portion of the highway is covered.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '17, 20:54</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-60300" class="comments-container">
<span id="60306"></span>
<div id="comment-60306" class="comment">
<div id="post-60306-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess my question here is then: Should the mall be represented by a multipolygon (as it is now)? The entire multipolygon is implicitly <code>layer=0</code>, but that does not accurately reflect the two building parts crossing the road which are individually tagged <code>layer=1</code>.</p>
</div>
<div id="comment-60306-info" class="comment-info">
<span class="comment-age">(26 Oct '17, 09:18)</span> <span class="comment-user userinfo">ThomasA</span>
</div>
</div>
<span id="60334"></span>
<div id="comment-60334" class="comment">
<div id="post-60334-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, the mall should be represented as a multipolygon because it has a hole.</p>
<p>The way <a href="https://www.openstreetmap.org/way/370434882">https://www.openstreetmap.org/way/370434882</a> is tagged with building:part=yes and layer=1. As far as I understand the building:part spec that's the correct tagging: the building part is a separate way that overlaps the base building (which, in this case, happens to be a multipolygon).</p>
</div>
<div id="comment-60334-info" class="comment-info">
<span class="comment-age">(27 Oct '17, 20:14)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
</div>
<div id="comment-tools-60300" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60300-form-container" class="comment-form-container">
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

