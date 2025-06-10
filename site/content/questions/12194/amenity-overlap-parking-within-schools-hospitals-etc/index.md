+++
type = "question"
title = "Amenity overlap - parking within schools, hospitals etc"
description = '''Is it OK to have an amenity=parking inside, say an amenity=hospital area (where the outer area represents the hospital site, not just a single building)? It feels wrong to have overlapping keys of the same type. But so does a multipolygon - the parking area IS part of the hospital. I&#x27;ve come across ...'''
date = "2012-04-20T11:24:00Z"
lastmod = "2012-04-20T15:58:00Z"
weight = 12194
keywords = [ "amenity", "leisure", "overlap" ]
aliases = [ "/questions/12194" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Amenity overlap - parking within schools, hospitals etc](/questions/12194/amenity-overlap-parking-within-schools-hospitals-etc)

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
<span id="post-12194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12194-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it OK to have an amenity=parking inside, say an amenity=hospital area (where the outer area represents the hospital site, not just a single building)?</p>
<p>It feels wrong to have overlapping keys of the same type. But so does a multipolygon - the parking area IS part of the hospital.</p>
<p>I've come across this dialemma a few times (e.g. leisure=playground inside a leisure=park). Overlapping the areas seems to render OK but is it good practice?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-leisure" rel="tag" title="see questions tagged &#39;leisure&#39;">leisure</span> <span class="post-tag tag-link-overlap" rel="tag" title="see questions tagged &#39;overlap&#39;">overlap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Apr '12, 11:24</strong></p>
<img src="https://secure.gravatar.com/avatar/f4df1119bfdf1e97bac7fb18996160ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pete&#39;s gravatar image" />
<p><span>Pete</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pete has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12194" class="comments-container">
&#10;</div>
<div id="comment-tools-12194" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12194-form-container" class="comment-form-container">
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

<span id="12205"></span>

<div id="answer-container-12205" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12205-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are instances where it's perfectly correct to have multiple overlapping areas, I think you've identified a couple of them. Carry on!</p>
<p>Where there comes a problem is if you try to have multiple values of the same key on the same node/way/area (aka "overload the key"). For example, if you put amenity=parking;hospital, what displayed would depend on how the renderer interprets that (would it display as parking? as hospital? as both? as neither?)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '12, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-12205" class="comments-container">
&#10;</div>
<div id="comment-tools-12205" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12205-form-container" class="comment-form-container">
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

