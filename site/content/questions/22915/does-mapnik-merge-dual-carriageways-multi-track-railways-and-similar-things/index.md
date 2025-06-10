+++
type = "question"
title = "Does mapnik merge dual carriageways, multi-track railways and similar things?"
description = '''When mapnik renders e.g. a dual carriageway in a scale that is zoomed out far enough that it does not make sense to render the ways separately, does it &quot;merge&quot; the ways before rendering, or does it just render them on top of each other, hoping that the result won&#x27;t be too ugly? (I could probably fig...'''
date = "2013-05-31T13:44:00Z"
lastmod = "2013-05-31T16:49:00Z"
weight = 22915
keywords = [ "railway", "carriageway", "mapnik", "dual" ]
aliases = [ "/questions/22915" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Does mapnik merge dual carriageways, multi-track railways and similar things?](/questions/22915/does-mapnik-merge-dual-carriageways-multi-track-railways-and-similar-things)

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
<span id="post-22915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22915-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When mapnik renders e.g. a dual carriageway in a scale that is zoomed out far enough that it does not make sense to render the ways separately, does it "merge" the ways before rendering, or does it just render them on top of each other, hoping that the result won't be too ugly?</p>
<p>(I could probably figure this out by expermimenting and/or reading code, but I am hoping that somebody can give a quick "it does/doesn't merge" off the top of his or her head. :-) )</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-carriageway" rel="tag" title="see questions tagged &#39;carriageway&#39;">carriageway</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-dual" rel="tag" title="see questions tagged &#39;dual&#39;">dual</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '13, 13:44</strong></p>
<img src="https://secure.gravatar.com/avatar/80abc4597de5aeb507c5a7ccd4ccee7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="turepalsson&#39;s gravatar image" />
<p><span>turepalsson</span><br />
<span class="score" title="836 reputation points">836</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="turepalsson has 3 accepted answers">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 May '13, 21:10</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-22915" class="comments-container">
&#10;</div>
<div id="comment-tools-22915" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22915-form-container" class="comment-form-container">
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

<span id="22922"></span>

<div id="answer-container-22922" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22922-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="turepalsson has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It does not merge the roads. In fact merging the roads would be computationally quite expensive and unlikely to be possible "on the fly". There's existing work in preprocessing data to find and merge such lines, but not for rendering - just for labelling. See <a href="https://github.com/migurski/Skeletron">https://github.com/migurski/Skeletron</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '13, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-22922" class="comments-container">
<span id="22925"></span>
<div id="comment-22925" class="comment">
<div id="post-22925-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer, and for the link; some interesting references there!</p>
</div>
<div id="comment-22925-info" class="comment-info">
<span class="comment-age">(31 May '13, 16:49)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
</div>
<div id="comment-tools-22922" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22922-form-container" class="comment-form-container">
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

