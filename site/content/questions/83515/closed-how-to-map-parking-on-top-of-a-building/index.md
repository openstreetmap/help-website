+++
type = "question"
title = "[Closed] How to map parking on top of a building?"
description = '''There is a parking on top of a building (id:94574722). How should this parking be mapped? I get errors for highway crossing building.'''
date = "2022-02-18T08:26:00Z"
lastmod = "2022-02-18T17:10:00Z"
weight = 83515
keywords = [ "parking" ]
aliases = [ "/questions/83515" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [\[Closed\] How to map parking on top of a building?](/questions/83515/closed-how-to-map-parking-on-top-of-a-building)

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
<span id="post-83515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83515-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a parking on top of a building (id:94574722). How should this parking be mapped? I get errors for highway crossing building.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '22, 08:26</strong></p>
<img src="https://secure.gravatar.com/avatar/7fbbe44e24bdb695025fddb0879817a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Msiipola&#39;s gravatar image" />
<p><span>Msiipola</span><br />
<span class="score" title="227 reputation points">227</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Msiipola has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Feb '22, 10:52</strong> </span></p>
</div>
</div>
<div id="comments-container-83515" class="comments-container">
&#10;</div>
<div id="comment-tools-83515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83515-form-container" class="comment-form-container">
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

<span id="83517"></span>

<div id="answer-container-83517" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83517-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Msiipola has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You map them just normally. But additionally, you need to add appropriate <a href="https://wiki.openstreetmap.org/wiki/Key:layer"><code>layer</code></a> tags to all overlapping objects to determin the right stacking order. E.g. the building could get <code>layer=0</code> (0 could be omitted as default, but it does not hurt tagging for clarity) and the parking <code>layer=1</code>. Same applies to the ramps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '22, 10:05</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Feb '22, 10:41</strong> </span></p>
</div>
</div>
<div id="comments-container-83517" class="comments-container">
<span id="83518"></span>
<div id="comment-83518" class="comment">
<div id="post-83518-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for answer. I missed the fact the ramp should also have layer=1. And now I don't get errors on the crossing highway and building.</p>
</div>
<div id="comment-83518-info" class="comment-info">
<span class="comment-age">(18 Feb '22, 10:51)</span> <span class="comment-user userinfo">Msiipola</span>
</div>
</div>
<span id="83519"></span>
<div id="comment-83519" class="comment">
<div id="post-83519-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is for road rendering. Technically <code>layer=</code> doesn't work well with <code>building=</code>. For 3D info, you want <code>level=</code>. <code>location=rooftop</code> is another possible addition.</p>
</div>
<div id="comment-83519-info" class="comment-info">
<span class="comment-age">(18 Feb '22, 11:48)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-83517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83517-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83520"></span>

<div id="answer-container-83520" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83520-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The wiki page for <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking">parking</a> allows for <a href="https://wiki.openstreetmap.org/wiki/Key:parking"><code>parking=rooftop</code></a>. I think the parking area should be outlined as for a <code>surface</code> lot and the appropriate <code>rooftop</code> and <code>layer</code> tag also defined in addition to the main parking amenity.</p>
<p>A <a href="https://wiki.openstreetmap.org/wiki/Key:level"><code>level</code></a> tag may also be appropriate if it is understood to coincide with a particular level of the building (it looks in the image like part of the building may be higher?).</p>
<p>Warnings from the validator are not always correct. In this case I think it is simply saying that "roads do not normally cross buildings" this is true in general, but in this specific case the road really does cross the building and after double checking that there are no other accidental crossings it can probably be safely ignored.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '22, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-83520" class="comments-container">
<span id="83521"></span>
<div id="comment-83521" class="comment">
<div id="post-83521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems my "form resubmission" was an answer that is now redundant. oops.</p>
</div>
<div id="comment-83521-info" class="comment-info">
<span class="comment-age">(18 Feb '22, 14:02)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="83524"></span>
<div id="comment-83524" class="comment">
<div id="post-83524-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wasn't aware of the keys parking=rooftop and location=rooftop. Maybe I have to reconsider how I shall map the parking, after I have read the wiki about "rooftop".</p>
</div>
<div id="comment-83524-info" class="comment-info">
<span class="comment-age">(18 Feb '22, 17:10)</span> <span class="comment-user userinfo">Msiipola</span>
</div>
</div>
</div>
<div id="comment-tools-83520" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83520-form-container" class="comment-form-container">
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

