+++
type = "question"
title = "Local Nominatim Server - Bulk support?"
description = '''Has anyone implemented Bulk Geocoding with Nominatim? I have my own, local instance of Nominatim running but I am not sure how to best proceed when I want to geocode several 100k of addresses.'''
date = "2012-04-27T13:48:00Z"
lastmod = "2012-04-28T20:47:00Z"
weight = 12392
keywords = [ "bulk", "nominatim" ]
aliases = [ "/questions/12392" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Local Nominatim Server - Bulk support?](/questions/12392/local-nominatim-server-bulk-support)

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
<span id="post-12392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12392-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Has anyone implemented Bulk Geocoding with Nominatim? I have my own, local instance of Nominatim running but I am not sure how to best proceed when I want to geocode several 100k of addresses.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bulk" rel="tag" title="see questions tagged &#39;bulk&#39;">bulk</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '12, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/e17c2bfaed82349f7a355866ff24e4cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Norm1&#39;s gravatar image" />
<p><span>Norm1</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Norm1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Apr '12, 20:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-12392" class="comments-container">
&#10;</div>
<div id="comment-tools-12392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12392-form-container" class="comment-form-container">
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

<span id="12411"></span>

<div id="answer-container-12411" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12411-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simply write 10 lines of code in a scripting language of your choice that fire off the required HTTP requests to your locally running Nominatim. I don't think a ready-made script exists but it should really just be a few lines of code, and those lines would heavily depend on what format your data is in and what output you want.</p>
<p>(I removed a previous answer after it became clear that this question is about a locally running instance.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '12, 20:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12411" class="comments-container">
&#10;</div>
<div id="comment-tools-12411" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12411-form-container" class="comment-form-container">
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

