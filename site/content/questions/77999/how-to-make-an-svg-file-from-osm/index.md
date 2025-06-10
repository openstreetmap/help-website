+++
type = "question"
title = "How to make an SVG file from OSM?"
description = '''My aim: to obtain an Inkscape editable SVG file containing a map of Berlin with fewer features than the ones which the big map contains. For instance no venues of shops, not different colours for different kinds of streets. Trying to find an answer, I got the impression that the procedure would enta...'''
date = "2020-12-19T01:09:00Z"
lastmod = "2020-12-21T14:28:00Z"
weight = 77999
keywords = [ "svg" ]
aliases = [ "/questions/77999" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to make an SVG file from OSM?](/questions/77999/how-to-make-an-svg-file-from-osm)

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
<span id="post-77999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77999-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My aim: to obtain an Inkscape editable SVG file containing a map of Berlin with fewer features than the ones which the big map contains. For instance no venues of shops, not different colours for different kinds of streets.</p>
<p>Trying to find an answer, I got the impression that the procedure would entail several steps concernig, among others,rendering, tile servers and layers.</p>
<p>Now: could anyone tell what should I do? Or at least give me a list of the entries of the Wiki that I shoud read in order to achieve my aim?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '20, 01:09</strong></p>
<img src="https://secure.gravatar.com/avatar/026fcce2d7827f63185b73969cfe13b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juanaines&#39;s gravatar image" />
<p><span>Juanaines</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juanaines has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '20, 17:50</strong> </span></p>
</div>
</div>
<div id="comments-container-77999" class="comments-container">
&#10;</div>
<div id="comment-tools-77999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77999-form-container" class="comment-form-container">
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

<span id="78025"></span>

<div id="answer-container-78025" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78025-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>'Share' on the right hand side of the main page has a SVG option.</p>
<p>rDepending on you needs it may require a <em>lot</em> of post processing in Inkscape. It produces an image with a boundary mask, but doesn't trim the actual data to it, so it will include extensive landuse areas which you may not require. Given you want all of Berlin you could end up with a very large XML file.</p>
<p>If anyone know a neater/quicker way please let me know.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '20, 23:48</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Dec '20, 14:11</strong> </span></p>
</div>
</div>
<div id="comments-container-78025" class="comments-container">
&#10;</div>
<div id="comment-tools-78025" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78025-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78026"></span>

<div id="answer-container-78026" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78026-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://extract.bbbike.org/">bbbike extracts</a> site has a few SVG options. DaveF's caveats for the main site may also apply here though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '20, 02:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-78026" class="comments-container">
<span id="78039"></span>
<div id="comment-78039" class="comment">
<div id="post-78039-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks After a brief look: Positives:</p>
<p>Trims to boundary.</p>
<p>OSM specific ID tags, so mass editing of the XML file is possible (Why OSM main page swaps in anonymous IDs is anyone's guess).</p>
<p>Negatives:</p>
<p>Very large text/symbols.</p>
<p>Rectangular boundary selection box shape is determined by the browers window shape!</p>
</div>
<div id="comment-78039-info" class="comment-info">
<span class="comment-age">(21 Dec '20, 14:28)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-78026" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78026-form-container" class="comment-form-container">
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

