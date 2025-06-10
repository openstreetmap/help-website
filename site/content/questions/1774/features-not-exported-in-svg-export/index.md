+++
type = "question"
title = "Features not exported in SVG export"
description = '''When I export a region to svg with mapnik, areas that are not rendered in mapnik are not exported as well. This sounds silly, but fell, cliff and scree currently aren&#x27;t rendered in mapnik and show up as grey area everywhere. But they aren&#x27;t exported as grey areas altogether, they simply aren&#x27;t there...'''
date = "2010-12-12T00:40:00Z"
lastmod = "2010-12-12T17:36:00Z"
weight = 1774
keywords = [ "export", "renderer", "mapnik" ]
aliases = [ "/questions/1774" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Features not exported in SVG export](/questions/1774/features-not-exported-in-svg-export)

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
<span id="post-1774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1774-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I export a region to svg with mapnik, areas that are not rendered in mapnik are not exported as well. This sounds silly, but fell, cliff and scree currently aren't rendered in mapnik and show up as grey area everywhere. But they aren't exported as grey areas altogether, they simply aren't there, the only thing there is the grey background.</p>
<p>Is there a way (apart from setting up an own mapnik instance with custom rendering rules etc.) to export everything in a svg for some experiments and tweaks on the image. I was wondering if coloring fell in a greyish green, scree in light grey and cliff in darker grey would yield to a better display without having the put the areas in there all by myself on the exported image...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-renderer" rel="tag" title="see questions tagged &#39;renderer&#39;">renderer</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '10, 00:40</strong></p>
<img src="https://secure.gravatar.com/avatar/720ecc66aa0d49f61a12c4d9e526e66f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexander%20Roalter&#39;s gravatar image" />
<p><span>Alexander Ro...</span><br />
<span class="score" title="276 reputation points">276</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexander Roalter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1774" class="comments-container">
<span id="1776"></span>
<div id="comment-1776" class="comment">
<div id="post-1776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What areas are you talking about?</p>
<p>Are you complaining that an export of the map looks exactly like the map you are exporting?</p>
</div>
<div id="comment-1776-info" class="comment-info">
<span class="comment-age">(12 Dec '10, 06:38)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
<span id="1777"></span>
<div id="comment-1777" class="comment">
<div id="post-1777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have an area consisting of forest, scrub, scree, fell and cliff. Upon export, I get only a polygon for the forest and scrub, but no polygon (albeit transparent) for fell, scree and cliff. In Data view mode.</p>
</div>
<div id="comment-1777-info" class="comment-info">
<span class="comment-age">(12 Dec '10, 10:44)</span> <span class="comment-user userinfo">Alexander Ro...</span>
</div>
</div>
</div>
<div id="comment-tools-1774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1774-form-container" class="comment-form-container">
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

<span id="1784"></span>

<div id="answer-container-1784" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1784-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, you can't do this using the image export alone. Check out <a href="http://maperitive.net/">Maperitive</a>, a desktop-based renderer that can use your own style rules and talks SVG happily.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '10, 17:36</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '13, 00:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-1784" class="comments-container">
&#10;</div>
<div id="comment-tools-1784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1784-form-container" class="comment-form-container">
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

