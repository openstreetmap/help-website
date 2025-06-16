+++
type = "question"
title = "Shouldnt a man-made pier get layer 1 ?"
description = '''Hi a man made pier is mostly build over water. I did not find a trace, hint nor a pier with the tag 1. A bridge gets layer 1, shouldn’t a man made pier be tagged layer 1 ?'''
date = "2013-08-06T22:54:00Z"
lastmod = "2013-08-07T15:29:00Z"
weight = 25008
keywords = [ "bridge", "layer", "pier" ]
aliases = [ "/questions/25008" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Shouldnt a man-made pier get layer 1 ?](/questions/25008/shouldnt-a-man-made-pier-get-layer-1)

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
<span id="post-25008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25008-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi a man made pier is mostly build over water. I did not find a trace, hint nor a pier with the tag 1. A bridge gets layer 1, shouldn’t a man made pier be tagged layer 1 ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-pier" rel="tag" title="see questions tagged &#39;pier&#39;">pier</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '13, 22:54</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-25008" class="comments-container">
&#10;</div>
<div id="comment-tools-25008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25008-form-container" class="comment-form-container">
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

<span id="25009"></span>

<div id="answer-container-25009" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25009-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-25009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hendrikklaas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, there is some logic to what you ask. However, the general consensus is that certain features are always "background", and are to be drawn behind everything else, without the need for <code>layer</code>.</p>
<p>Examples for "background features":</p>
<ul>
<li><code>landuse</code></li>
<li><code>natural</code> (when used for areas)</li>
<li><code>highway</code> (when used for areas, though it is drawn above <code>landuse</code> or <code>natural</code>)</li>
</ul>
<p>So since the water is implicitly "background", there's no need to give the pier a layer.</p>
<p>For example, the <a href="https://wiki.openstreetmap.org/wiki/Key:layer">wiki</a> explains:</p>
<blockquote>
<p>Waterways (waterway=*) do not normally need to be tagged with a layer and are generally rendered as if they flow underneath built features. [...] Landuses, such as parks and woods should not normally be tagged with a layer.</p>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '13, 23:21</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-25009" class="comments-container">
<span id="25013"></span>
<div id="comment-25013" class="comment">
<div id="post-25013-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>… but it also does not harm to tag it explicitly, does it? I think the transition between implicit assumptions (by some more/most renderers) and trying to correct the most prevalent errors (by some/many renderers) is continuous (e.g. what is about smaller landuse areas on top of bigger landuse areas?). The comparison with a a bridge sounds reasonable.</p>
</div>
<div id="comment-25013-info" class="comment-info">
<span class="comment-age">(06 Aug '13, 23:39)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="25019"></span>
<div id="comment-25019" class="comment">
<div id="post-25019-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>A pier is similar to a bridge. But whereas bridges can have other roads beneath them, piers usually don't. Nevertheless adding the layer tag won't harm, that's true.</p>
</div>
<div id="comment-25019-info" class="comment-info">
<span class="comment-age">(07 Aug '13, 06:26)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="25034"></span>
<div id="comment-25034" class="comment">
<div id="post-25034-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm, yes. Depending on the type of support (many or just a few big poles) below the pier some small boats could pass through.</p>
</div>
<div id="comment-25034-info" class="comment-info">
<span class="comment-age">(07 Aug '13, 14:26)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="25035"></span>
<div id="comment-25035" class="comment">
<div id="post-25035-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's an interesting issue. But for tagging if and which boats can pass through additional tags are required (height, width, draught).</p>
</div>
<div id="comment-25035-info" class="comment-info">
<span class="comment-age">(07 Aug '13, 14:50)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-25009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25009-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25036"></span>

<div id="answer-container-25036" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25036-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well strictly speaking the <a href="https://wiki.openstreetmap.org/wiki/Layer">layer tag</a> is relative, so what value is used will depend on what else is mapped (or is planned to be mapped) under or over it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '13, 15:29</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-25036" class="comments-container">
&#10;</div>
<div id="comment-tools-25036" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25036-form-container" class="comment-form-container">
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

