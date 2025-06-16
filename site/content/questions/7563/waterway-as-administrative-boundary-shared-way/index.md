+++
type = "question"
title = "Waterway as administrative boundary - shared way?"
description = '''If an administrative boundary is going along a river in its centre (the river is effectively the boundary). Yet the administrative boundary is likely defined independently (intentionaly along the river, but if the river changed the boundary would not move automatically).   should they share the same...'''
date = "2011-09-02T20:59:00Z"
lastmod = "2015-07-15T16:45:00Z"
weight = 7563
keywords = [ "waterway", "admin_boundary" ]
aliases = [ "/questions/7563" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Waterway as administrative boundary - shared way?](/questions/7563/waterway-as-administrative-boundary-shared-way)

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
<span id="post-7563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7563-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-7563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If an administrative boundary is going along a river in its centre (the river is effectively the boundary). Yet the administrative boundary is likely defined independently (intentionaly along the river, but if the river changed the boundary would not move automatically).</p>
<ul>
<li>should they share the same way together (minimum redundancy, more complicated relations)?<br />
</li>
<li>should they share nodes only (easy to do)?</li>
<li>should they be completely independent?</li>
</ul>
<p>How should it be mapped?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '11, 20:59</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-7563" class="comments-container">
&#10;</div>
<div id="comment-tools-7563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7563-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="7564"></span>

<div id="answer-container-7564" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7564-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LM_1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sharing nodes is not recommended and should only be used if the shared segment is rather short. This may look as if it were "easy to do" but it is actually difficult to edit - try refining the geometry of such a multi-way in JOSM and you'll find that you can only refine one way at a time.</p>
<p>If you do not have exact data for the administrative boundary, but all you have is your assumption that it is "likely defined independently" then I would use the river as part of my boundary relation (and the relation is not more difficult just because one of its ways is a river rather than a specially drawn admin boundary).</p>
<p>If on the other hand you have exact data for the administrative boundary and you know it to be not only independent, but in fact different from the river centreline, then draw both as their own ways, and maybe even add a <code>note</code> tag to tell other mappers that you've drawn two lines on purpose and that they should please refrain from merging both lines.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '11, 21:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-7564" class="comments-container">
<span id="7566"></span>
<div id="comment-7566" class="comment">
<div id="post-7566-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In fact I have very precise data for the administrative boundary and it is intentionally put in the river centerline.<br />
I meant independent in the sense of being defined by set of geographically coded lines rather than wherever the river is. Currently they ar exactly in the river's centerline.<br />
The question was whether this should play any role (defined by coordinates in the river/by the river itself).</p>
</div>
<div id="comment-7566-info" class="comment-info">
<span class="comment-age">(02 Sep '11, 21:45)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
<span id="7568"></span>
<div id="comment-7568" class="comment">
<div id="post-7568-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My recommendation would be to not try to be too clever. Use the same geometry for both. If someone later moves the river then they will - wrongly - move the admin boundary also but I suggest to cross that bridge when we come to it. Even if you make two totally independent geometries now, it is not unlikely that someone moving the river will also move the boundary, assuming they are meant to run together.</p>
</div>
<div id="comment-7568-info" class="comment-info">
<span class="comment-age">(02 Sep '11, 22:07)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7564-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44206"></span>

<div id="answer-container-44206" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44206-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The river way should always be tagged as a river, and never be an untagged line that just so happens to be part of a waterway relation.</p>
<p>It may be part of an administrative boundary relation, and may be tagged boundary=administrative in addition to having a waterway tag, but I'd consider that optional.</p>
<p>As I said above, use the same way if the boundary is defined by the river, and use a separate geometry if the boundary is defined independently of the river (i.e. ask yourself "what happens if the river moves?").</p>
<p>I'd still advise against having several ways share nodes for anything but a short stretch. JOSM may have become more sophisticated but at the same time there are now other editors for whom we do not wish to make life harder.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '15, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-44206" class="comments-container">
&#10;</div>
<div id="comment-tools-44206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44206-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44203"></span>

<div id="answer-container-44203" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44203-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(Edit after receiving answers, see above, consolidate view for future users): The question is quite old, but still relevant. Assume the following situation: Border is defined by the river, hence runs along its "centreline". This is quite a realistic scenario as rivers usually do not move (very much), especially in mountainous or sparsely populated areas.</p>
<p>(Old) Example from the Iran-Turkmenistan border, meanwhile changed: <img src="/upfiles/Clipboard01.jpg" alt="alt text" /></p>
<p>Clearly, the resulting picture should look like in the area to the right. There, the boundary and the river match visibly (like in reality); in the database however, they are different ways, but share the same nodes (two ways glued togehter). This cannot be seen from the picture, but can be found out by looking at the data directly.</p>
<p>Although in JOSM, you could nowadays easily refine the geometry of two ways that are "glued" together (using the w shortcut e. g.), there might be other editors that do not allow this. Furthermore, the JOSM validator detects an error "overlapping ways".</p>
<p>Furthermore: "glueing" ways together might be a bad practice from a logical point of view ("data hygiene"): after all, you actually have <em>one</em> element in the database that describes <em>one</em> physical shape (the geometrical line), and this shape has two meanings: 1. river and 2. boundary. Now logically, this would imply you should draw <em>one</em> line and tag it appropriately to represent several functions.</p>
<p>To illustrate it, the desired result should look like this:</p>
<ol>
<li>Draw a way along the waterway (that defines the border) and tag is as a an appropriate waterway, may be assign it additionally to a waterway relation(s).</li>
<li>Tag the the drawn way (now with waterway=river e. g.) additionally with boundary keys and include it in the necessary boundary type relations (there are most likely several ones like nation, province, county etc. depending on the country-specific hierarchy and admin levels).</li>
</ol>
<p>(May be this description can be added to an appropriate wiki page, as I see a lot of "ugly" borders around the world..... I might do it one day...)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '15, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/fd1035a2bbd533c4ec6fbd22fc705a5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sakudo&#39;s gravatar image" />
<p><span>sakudo</span><br />
<span class="score" title="131 reputation points">131</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sakudo has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '15, 10:41</strong> </span></p>
</div>
</div>
<div id="comments-container-44203" class="comments-container">
&#10;</div>
<div id="comment-tools-44203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44203-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24051"></span>

<div id="answer-container-24051" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24051-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Even old question, would like to share one answer here, without open same discussion again. What about having one relation for the administrative boundary and one for the waterway? In that case we should have one way included in both relations. My question now is what tags to remain on that way: waterway, boundary or both?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '13, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/d1495190e346c0c530fd7205883b55c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Plamen&#39;s gravatar image" />
<p><span>Plamen</span><br />
<span class="score" title="151 reputation points">151</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Plamen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24051" class="comments-container">
&#10;</div>
<div id="comment-tools-24051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24051-form-container" class="comment-form-container">
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

