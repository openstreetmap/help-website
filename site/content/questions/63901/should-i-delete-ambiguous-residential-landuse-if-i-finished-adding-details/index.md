+++
type = "question"
title = "Should I delete ambiguous residential landuse if I finished adding details?"
description = '''Hi folks, Several times I encounter whole towns/villages ambiguously mapped as landuse=residential polygons (and sometimes with a place=* tag) at its first mapping attemps, when there are no details yet. Maybe it is to see the general extent of &quot;built-up&quot; area or the general extent of the town. But ...'''
date = "2018-05-31T06:17:00Z"
lastmod = "2018-06-04T08:06:00Z"
weight = 63901
keywords = [ "town", "residential", "landuse" ]
aliases = [ "/questions/63901" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Should I delete ambiguous residential landuse if I finished adding details?](/questions/63901/should-i-delete-ambiguous-residential-landuse-if-i-finished-adding-details)

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
<span id="post-63901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63901-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi folks,</p>
<p>Several times I encounter whole towns/villages ambiguously mapped as <code>landuse=residential</code> polygons (and sometimes with a <code>place=*</code> tag) at its first mapping attemps, when there are no details yet. Maybe it is to see the general extent of "built-up" area or the general extent of the town. But let's say later I have added all buildings and landuse's with enough detail that this residential landuse becomes ambiguous: within it there are markets, airports, parks, hospitals and any kind of landuse you would encounter in a normal town, and even real (smaller) "residential" areas.</p>
<p>So what is the best practice regarding this? Would I delete the large residential area polygon as the extent of build-up can be seen with mapped features now? Or do I simply try to fine-tune its extent (most of the time it is very general)?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-town" rel="tag" title="see questions tagged &#39;town&#39;">town</span> <span class="post-tag tag-link-residential" rel="tag" title="see questions tagged &#39;residential&#39;">residential</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '18, 06:17</strong></p>
<img src="https://secure.gravatar.com/avatar/15d45a99f101e06c9e79916af33f8336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Privatemajory&#39;s gravatar image" />
<p><span>Privatemajory</span><br />
<span class="score" title="1125 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Privatemajory has 4 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 May '18, 11:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-63901" class="comments-container">
&#10;</div>
<div id="comment-tools-63901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63901-form-container" class="comment-form-container">
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

<span id="63903"></span>

<div id="answer-container-63903" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63903-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-63903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I was going to write "yes, delete it", but then I realized that the polygon might, at least in some cases, serve as a good place to put the place=X tag on. Remove the landuse tag, though.</p>
<p>Rationale: It is pointless to have overlapping, conflicting landuses. This is typical OSM iterative refinement. Stuff gets mapped coarsely at first and then replaced by better data. Having place=X,name=Y tags on a polygon and not on a point is potentially useful, because it shows the extent of the place, for example telling renderers how much "wiggle room" they have in placing labels.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '18, 07:50</strong></p>
<img src="https://secure.gravatar.com/avatar/80abc4597de5aeb507c5a7ccd4ccee7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="turepalsson&#39;s gravatar image" />
<p><span>turepalsson</span><br />
<span class="score" title="836 reputation points">836</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="turepalsson has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-63903" class="comments-container">
<span id="63913"></span>
<div id="comment-63913" class="comment">
<div id="post-63913-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good point. Thanks 😉</p>
</div>
<div id="comment-63913-info" class="comment-info">
<span class="comment-age">(31 May '18, 14:12)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
<span id="63953"></span>
<div id="comment-63953" class="comment">
<div id="post-63953-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oftentimes I see landuse=residential being used when place=neighborhood and/or an administrative boundary is more appropriate.</p>
</div>
<div id="comment-63953-info" class="comment-info">
<span class="comment-age">(02 Jun '18, 04:45)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="63970"></span>
<div id="comment-63970" class="comment">
<div id="post-63970-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, I also think the place=* tag is best put on an administrative boundary. I don't really like the idea putting it on often vague limits of built-up / groups of buildings.</p>
</div>
<div id="comment-63970-info" class="comment-info">
<span class="comment-age">(03 Jun '18, 08:03)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
<span id="63999"></span>
<div id="comment-63999" class="comment">
<div id="post-63999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By all means, if there are appropriate admin borders to put place=tags on, do so. However, don't let the absence of admin borders stop you from putting place tags! For example, the smallest legally regognized administrative subdivision of Sweden is a kommun (admin_level=7), and some of those are... big: <a href="https://www.openstreetmap.org/relation/935541">https://www.openstreetmap.org/relation/935541</a></p>
</div>
<div id="comment-63999-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 08:06)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
</div>
<div id="comment-tools-63903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63903-form-container" class="comment-form-container">
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

