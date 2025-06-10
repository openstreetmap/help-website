+++
type = "question"
title = "Multipolygon Issue"
description = '''I have been trying to use a multipolygon to render the public access areas of Windsor Great Park (UK). I have used a role=outer, leisure=park for the outer boundary and for the inner non-access areas I have used role=inner. The relationship is 2195597. The inner polygons are not being &quot;subtracted&quot; f...'''
date = "2012-06-26T12:50:00Z"
lastmod = "2012-06-26T17:05:00Z"
weight = 13796
keywords = [ "rendering", "park", "multipolygon" ]
aliases = [ "/questions/13796" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Multipolygon Issue](/questions/13796/multipolygon-issue)

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
<span id="post-13796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13796-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been trying to use a multipolygon to render the public access areas of Windsor Great Park (UK). I have used a role=outer, leisure=park for the outer boundary and for the inner non-access areas I have used role=inner. The relationship is <a href="http://www.openstreetmap.org/browse/relation/2195597">2195597</a>. The inner polygons are not being "subtracted" from the park render. Can anyone identify the issue / help please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '12, 12:50</strong></p>
<img src="https://secure.gravatar.com/avatar/e4bb669a2ceb84f0aa71e466e1bfd7b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trubshaw&#39;s gravatar image" />
<p><span>Trubshaw</span><br />
<span class="score" title="80 reputation points">80</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trubshaw has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '12, 15:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-13796" class="comments-container">
&#10;</div>
<div id="comment-tools-13796" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13796-form-container" class="comment-form-container">
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

<span id="13807"></span>

<div id="answer-container-13807" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13807-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Trubshaw has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just a hunch, but you might want to move the leisure=park tag from the outer way to the relation. Otherwise the tools don't know that is what you want the holes to appear in (the relation itself might have different landuse tags to put holes in, but at the moment has none).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '12, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-13807" class="comments-container">
<span id="13808"></span>
<div id="comment-13808" class="comment">
<div id="post-13808-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ed, I use Potlatch (mainly). If the leisure=park is removed from the outer then where does it go? How do I add a landuse tag to the relationship?</p>
</div>
<div id="comment-13808-info" class="comment-info">
<span class="comment-age">(26 Jun '12, 17:01)</span> <span class="comment-user userinfo">Trubshaw</span>
</div>
</div>
<span id="13809"></span>
<div id="comment-13809" class="comment">
<div id="post-13809-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Oops - I have now found the advanced properties for the relationship, scroll down was required.</p>
</div>
<div id="comment-13809-info" class="comment-info">
<span class="comment-age">(26 Jun '12, 17:05)</span> <span class="comment-user userinfo">Trubshaw</span>
</div>
</div>
</div>
<div id="comment-tools-13807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13807-form-container" class="comment-form-container">
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

