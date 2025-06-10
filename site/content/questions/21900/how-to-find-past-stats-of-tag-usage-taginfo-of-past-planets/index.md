+++
type = "question"
title = "How to find past stats of tag usage (Taginfo of past planets) ?"
description = '''I have 2 specific cases where I&#x27;m interested in knowing the past statistics of tag usage:  a] how many of the landuse=cemetery features in the USA were at one point tagged as amenity=grave_yard. b] How many times amenity=grave_yard was used in the USA shortly after the GNIS import.  What&#x27;s the easie...'''
date = "2013-04-26T21:01:00Z"
lastmod = "2013-04-26T22:41:00Z"
weight = 21900
keywords = [ "taginfo", "tags", "history" ]
aliases = [ "/questions/21900" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find past stats of tag usage (Taginfo of past planets) ?](/questions/21900/how-to-find-past-stats-of-tag-usage-taginfo-of-past-planets)

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
<span id="post-21900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21900-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have 2 specific cases where I'm interested in knowing the past statistics of tag usage:</p>
<p>a] how many of the landuse=cemetery features in the USA were at one point tagged as amenity=grave_yard.</p>
<p>b] How many times amenity=grave_yard was used in the USA shortly after the GNIS import.</p>
<p>What's the easiest way of finding this out ? Is there a service out there that allows this, or in case B] would I have to download old planets, extract the US, set it up into an postgis db; then make a SQL query ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-taginfo" rel="tag" title="see questions tagged &#39;taginfo&#39;">taginfo</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '13, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorasaurus has 3 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-21900" class="comments-container">
&#10;</div>
<div id="comment-tools-21900" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21900-form-container" class="comment-form-container">
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

<span id="21902"></span>

<div id="answer-container-21902" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21902-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's nobody that I know of who keeps such statistics for your perusal so you would have to work this out yourself, either by downloading and comparing two different planet files, or by downloading and analysing a full history planet file.</p>
<p>You could use the <a href="https://github.com/MaZderMind/osm-history-splitter">OSM history splitter</a> to pull out the USA from the history file, and then process that. Since the full history planet is ordered by type/id/version, it would be relatively easy to answer your question with a few lines of code.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '13, 22:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-21902" class="comments-container">
&#10;</div>
<div id="comment-tools-21902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21902-form-container" class="comment-form-container">
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

