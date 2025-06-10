+++
type = "question"
title = "Any way to convert outer-way-only multipolygons into single ways?"
description = '''I&#x27;ve came to the conclusion, that my old mapping habit to map large e.g. forests als multipolygon relation with many smaller outer ways is bogus. It would have been much easier for exporting and other tasks to map them as simple, large ways. Is there any way how I can convert my own multipolygons (o...'''
date = "2018-04-24T22:39:00Z"
lastmod = "2018-04-25T10:08:00Z"
weight = 63115
keywords = [ "josm", "automatically", "multipolygon" ]
aliases = [ "/questions/63115" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Any way to convert outer-way-only multipolygons into single ways?](/questions/63115/any-way-to-convert-outer-way-only-multipolygons-into-single-ways)

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
<span id="post-63115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63115-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-63115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've came to the conclusion, that my old mapping habit to map large e.g. forests als multipolygon relation with many smaller outer ways is bogus. It would have been much easier for exporting and other tasks to map them as simple, large ways.</p>
<p>Is there any way how I can convert my <em>own</em> multipolygons (only!) semi-automatically into plain ways? It's so tedious to do this by hand so I'm looking for any JOSM or even cli tools solution.</p>
<p>Thanks for any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-automatically" rel="tag" title="see questions tagged &#39;automatically&#39;">automatically</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '18, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/bdb6a1b49c42d8be4b8d87f3096a3622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Druzhba&#39;s gravatar image" />
<p><span>Druzhba</span><br />
<span class="score" title="150 reputation points">150</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Druzhba has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63115" class="comments-container">
&#10;</div>
<div id="comment-tools-63115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63115-form-container" class="comment-form-container">
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

<span id="63125"></span>

<div id="answer-container-63125" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63125-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Druzhba has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a JOSM plugin called "relation toolbox" (reltoolbox) that lets you do this. You have to select a relation and then you can right-click on the relation in the relation toolbox panel and select "reconstruct multipolygon".</p>
<p>Don't go over board though; in areas where the forest boundary and another boundary coincide for more than a couple of nodes, using relations could still make sense!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '18, 10:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-63125" class="comments-container">
&#10;</div>
<div id="comment-tools-63125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63125-form-container" class="comment-form-container">
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

