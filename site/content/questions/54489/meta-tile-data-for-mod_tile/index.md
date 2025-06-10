+++
type = "question"
title = "Meta tile data for mod_tile"
description = '''Do the meta files that are stored on disk, contain the XML style sheet applied too? Or is it just the OSM data from the postgis database? I am looking at adding an additional path for retina support to my tile servers and was hoping that the same cache could be used. If so what commands do I need to...'''
date = "2017-02-05T23:34:00Z"
lastmod = "2017-02-06T00:20:00Z"
weight = 54489
keywords = [ "renderd", "mod_tile" ]
aliases = [ "/questions/54489" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Meta tile data for mod_tile](/questions/54489/meta-tile-data-for-mod_tile)

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
<span id="post-54489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54489-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Do the meta files that are stored on disk, contain the XML style sheet applied too? Or is it just the OSM data from the postgis database? I am looking at adding an additional path for retina support to my tile servers and was hoping that the same cache could be used. If so what commands do I need to add to rendered.conf to make sure they share the default style?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '17, 23:34</strong></p>
<img src="https://secure.gravatar.com/avatar/226f7b2fa9f2bcff48e73585ae31522c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhawkins&#39;s gravatar image" />
<p><span>bhawkins</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhawkins has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54489" class="comments-container">
&#10;</div>
<div id="comment-tools-54489" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54489-form-container" class="comment-form-container">
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

<span id="54490"></span>

<div id="answer-container-54490" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54490-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-54490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bhawkins has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot use the same cache. The meta tiles contain ready-made PNG images (64 of them per meta tile) and if you want double-resolution images you need a second cache directory. You can use the same database and the same style file for both normal and retina tiles, but not the same cache directory.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '17, 23:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54490" class="comments-container">
<span id="54491"></span>
<div id="comment-54491" class="comment">
<div id="post-54491-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I was confused by reading the docs if it was PNG data or raw OSM data.</p>
</div>
<div id="comment-54491-info" class="comment-info">
<span class="comment-age">(06 Feb '17, 00:20)</span> <span class="comment-user userinfo">bhawkins</span>
</div>
</div>
</div>
<div id="comment-tools-54490" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54490-form-container" class="comment-form-container">
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

