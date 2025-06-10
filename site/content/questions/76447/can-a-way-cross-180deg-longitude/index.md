+++
type = "question"
title = "can a way cross 180deg longitude"
description = '''I would like to know if it is specifically forbidden for an OSM way to cross the 180th meridian in either direction. And as a corollary to that, when I export data from OpenStreetMap.org is it guaranteed that no way contained in the exported datafile will contain such a crossing? I have discovered v...'''
date = "2020-09-05T02:03:00Z"
lastmod = "2020-09-05T19:51:00Z"
weight = 76447
keywords = [ "180º" ]
aliases = [ "/questions/76447" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can a way cross 180deg longitude](/questions/76447/can-a-way-cross-180deg-longitude)

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
<span id="post-76447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76447-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to know if it is specifically forbidden for an OSM way to cross the 180th meridian in either direction. And as a corollary to that, when I export data from OpenStreetMap.org is it guaranteed that no way contained in the exported datafile will contain such a crossing?</p>
<p>I have discovered various comments and hints in the documentation and forum that indicate problems in different pieces of software with regard to this point, but I have yet to see any authoritative-looking statement that declares whether this is a specifically forbidden condition or not.</p>
<p>The docs do seem clear that only values within [-180, +180] are legal node longitudes, but you could certainly have a way containing the legal longitude sequence ... +179.9, +180.0, -179.9, -179.8. Would this be interpreted to cross the 180th meridian in an easterly direction by 0.1 degrees or to span the gap between +180.0 and -179.9 by traveling almost 360 degrees to the west?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-180º" rel="tag" title="see questions tagged &#39;180º&#39;">180º</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '20, 02:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ea41a4b8367e5ea75d4b2416cb361c03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rbd808&#39;s gravatar image" />
<p><span>rbd808</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rbd808 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76447" class="comments-container">
&#10;</div>
<div id="comment-tools-76447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76447-form-container" class="comment-form-container">
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

<span id="76453"></span>

<div id="answer-container-76453" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76453-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is not technically forbidden. But most software cannot interpret such ways correctly - e.g. if you draw a building that sits across the dateline, the renderer will instead make your building go around the whole globe. Therefore the community will ask you to refrain from doing it.</p>
<p>When processing OSM data it is possible to encounter ways that cross the dateline but you wouldn't know from the data alone that it does (someone might <em>want</em> to draw a globe-spanning building); you can only use heuristics to guess what makes sense. Any dateline-crossing ways will likely be removed quickly by the community.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '20, 08:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-76453" class="comments-container">
<span id="76461"></span>
<div id="comment-76461" class="comment">
<div id="post-76461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, Frederik! I will extrapolate from your response that if I export regional data from the openstreetmap.org database the exported file's ways will not contain 180 crossings. If this is incorrect please advise.</p>
</div>
<div id="comment-76461-info" class="comment-info">
<span class="comment-age">(05 Sep '20, 17:08)</span> <span class="comment-user userinfo">rbd808</span>
</div>
</div>
<span id="76463"></span>
<div id="comment-76463" class="comment">
<div id="post-76463-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is unlikely for the file to contain such ways, but not impossible; if the file does contain such ways, they are likely to be removed in the next update.</p>
</div>
<div id="comment-76463-info" class="comment-info">
<span class="comment-age">(05 Sep '20, 18:30)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="76465"></span>
<div id="comment-76465" class="comment">
<div id="post-76465-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the clarification, Frederik!</p>
</div>
<div id="comment-76465-info" class="comment-info">
<span class="comment-age">(05 Sep '20, 19:51)</span> <span class="comment-user userinfo">rbd808</span>
</div>
</div>
</div>
<div id="comment-tools-76453" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76453-form-container" class="comment-form-container">
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

