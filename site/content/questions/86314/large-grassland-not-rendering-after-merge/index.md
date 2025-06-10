+++
type = "question"
title = "Large grassland not rendering after merge"
description = '''I was merging some grassland done in sections, and suddenly it won&#x27;t render. One of the lines is here https://www.openstreetmap.org/edit#map=17/64.62778/-21.37549 and the area expand southwards.  Is there a max size for grassland? Does forgotten lines between merged areas mess things up? '''
date = "2022-12-06T23:34:00Z"
lastmod = "2022-12-07T00:40:00Z"
weight = 86314
keywords = [ "grassland", "large_area", "area", "size" ]
aliases = [ "/questions/86314" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Large grassland not rendering after merge](/questions/86314/large-grassland-not-rendering-after-merge)

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
<span id="post-86314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86314-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was merging some grassland done in sections, and suddenly it won't render.</p>
<p>One of the lines is here <a href="https://www.openstreetmap.org/edit#map=17/64.62778/-21.37549">https://www.openstreetmap.org/edit#map=17/64.62778/-21.37549</a> and the area expand southwards.</p>
<ul>
<li>Is there a max size for grassland?</li>
<li>Does forgotten lines between merged areas mess things up?</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-grassland" rel="tag" title="see questions tagged &#39;grassland&#39;">grassland</span> <span class="post-tag tag-link-large_area" rel="tag" title="see questions tagged &#39;large_area&#39;">large_area</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '22, 23:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a340c84369e78552eb294e65cddd04c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikaeldui&#39;s gravatar image" />
<p><span>mikaeldui</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikaeldui has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86314" class="comments-container">
&#10;</div>
<div id="comment-tools-86314" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86314-form-container" class="comment-form-container">
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

<span id="86315"></span>

<div id="answer-container-86315" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86315-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mikaeldui has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The JOSM validator flags up 6 issues:</p>
<ul>
<li>1 "Intersection between outer ways" (in the vicinity of <a href="https://www.openstreetmap.org/node/10243101779">https://www.openstreetmap.org/node/10243101779</a> )</li>
<li>2 "Multipolygon outer way shares segment with other ring"</li>
<li>3 "Multipolygon outer ring contains segment twice"</li>
</ul>
<p>Regardless of what you use for editing I can wholeheartedly recommend JOSM's validator to help detect this sort of issue.</p>
<p>In answer to your specific questions:</p>
<blockquote>
<p>Is there a max size for grassland?</p>
</blockquote>
<p>There are some object size limits in OSM, but the one for "number of members of a relation" is huge and not an issue here.</p>
<blockquote>
<p>Does forgotten lines between merged areas mess things up?</p>
</blockquote>
<p>I suspect that the "forgotten lines" are causing the 2nd and 3rd problem that JOSM's validator found, so yet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '22, 23:47</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-86315" class="comments-container">
<span id="86316"></span>
<div id="comment-86316" class="comment">
<div id="post-86316-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, after cleaning up the "residual/forgotten" lines between the areas merged, it's now rendering again!</p>
</div>
<div id="comment-86316-info" class="comment-info">
<span class="comment-age">(07 Dec '22, 00:40)</span> <span class="comment-user userinfo">mikaeldui</span>
</div>
</div>
</div>
<div id="comment-tools-86315" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86315-form-container" class="comment-form-container">
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

