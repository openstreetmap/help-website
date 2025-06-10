+++
type = "question"
title = "Why are these car parks refusing to render?"
description = '''As far as I can tell then these two parking areas should render as yellow areas on the Slippy Map. Hundreds of other similar areas have worked for me, so can anyone offer any insight into why these aren&#x27;t rendering? They are both closed ways. http://www.openstreetmap.org/browse/way/96949631 http://w...'''
date = "2011-02-06T09:54:00Z"
lastmod = "2011-02-06T20:33:00Z"
weight = 2733
keywords = [ "rendering", "parking", "bug", "area" ]
aliases = [ "/questions/2733" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why are these car parks refusing to render?](/questions/2733/why-are-these-car-parks-refusing-to-render)

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
<span id="post-2733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2733-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As far as I can tell then these two parking areas should render as yellow areas on the Slippy Map. Hundreds of other similar areas have worked for me, so can anyone offer any insight into why these aren't rendering? They are both closed ways.</p>
<p><a href="http://www.openstreetmap.org/browse/way/96949631">http://www.openstreetmap.org/browse/way/96949631</a></p>
<p><a href="http://www.openstreetmap.org/browse/way/10519366">http://www.openstreetmap.org/browse/way/10519366</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '11, 09:54</strong></p>
<img src="https://secure.gravatar.com/avatar/b0d98734d95fa6d3fed729b2a919855d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fluteflute&#39;s gravatar image" />
<p><span>fluteflute</span><br />
<span class="score" title="731 reputation points">731</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fluteflute has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '11, 09:56</strong> </span></p>
</div>
</div>
<div id="comments-container-2733" class="comments-container">
&#10;</div>
<div id="comment-tools-2733" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2733-form-container" class="comment-form-container">
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

<span id="2735"></span>

<div id="answer-container-2735" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2735-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fluteflute has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The first one probably doesn't render because mapnik renders <code>leisure=pitch</code> after and therefor over <code>amenity=parking</code>. I assume the same is true for <code>man_made=pier</code> which is defined in the layer-water_features. The first one can be solved by excluding the parking lot from the area of the pitch which is only correct in my opinion as the parking lot is associated with but not part of the pitch itself. The second one is harder as the parking lot really IS on the pier and there isn't much you can do about it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '11, 10:08</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-2735" class="comments-container">
<span id="2742"></span>
<div id="comment-2742" class="comment">
<div id="post-2742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Might a layer tag work?</p>
</div>
<div id="comment-2742-info" class="comment-info">
<span class="comment-age">(06 Feb '11, 20:22)</span> <span class="comment-user userinfo">fluteflute</span>
</div>
</div>
<span id="2744"></span>
<div id="comment-2744" class="comment">
<div id="post-2744-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As the parking lot is really build on top of the pier (if your mapping is correct) a layer might be the right thing to do there. It feels like a kludge though.</p>
</div>
<div id="comment-2744-info" class="comment-info">
<span class="comment-age">(06 Feb '11, 20:29)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="2745"></span>
<div id="comment-2745" class="comment">
<div id="post-2745-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll report a bug! :D</p>
</div>
<div id="comment-2745-info" class="comment-info">
<span class="comment-age">(06 Feb '11, 20:30)</span> <span class="comment-user userinfo">fluteflute</span>
</div>
</div>
<span id="2746"></span>
<div id="comment-2746" class="comment">
<div id="post-2746-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://trac.openstreetmap.org/ticket/3517">http://trac.openstreetmap.org/ticket/3517</a></p>
</div>
<div id="comment-2746-info" class="comment-info">
<span class="comment-age">(06 Feb '11, 20:33)</span> <span class="comment-user userinfo">fluteflute</span>
</div>
</div>
</div>
<div id="comment-tools-2735" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2735-form-container" class="comment-form-container">
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

