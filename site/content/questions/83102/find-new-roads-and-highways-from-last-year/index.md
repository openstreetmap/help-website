+++
type = "question"
title = "Find new roads and highways from last year"
description = '''Is there a good way to find new highways from one year (or month) to the next? I tried looking at the version of ways (highways) but that doesn&#x27;t seem like the way to go as version 1 of ways isn&#x27;t giving me NEW roads.'''
date = "2022-01-17T18:21:00Z"
lastmod = "2022-01-17T19:04:00Z"
weight = 83102
keywords = [ "new", "road", "highway" ]
aliases = [ "/questions/83102" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find new roads and highways from last year](/questions/83102/find-new-roads-and-highways-from-last-year)

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
<span id="post-83102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83102-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a good way to find new highways from one year (or month) to the next? I tried looking at the version of ways (highways) but that doesn't seem like the way to go as version 1 of ways isn't giving me NEW roads.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-new" rel="tag" title="see questions tagged &#39;new&#39;">new</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '22, 18:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a8f374f9e963631edb07189841ca233e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gcapilot&#39;s gravatar image" />
<p><span>gcapilot</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gcapilot has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83102" class="comments-container">
&#10;</div>
<div id="comment-tools-83102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83102-form-container" class="comment-form-container">
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

<span id="83103"></span>

<div id="answer-container-83103" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83103-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's no "zero effort" way I'm afraid, as you have already seen you cannot rely on version numbers. A relatively stable approach could be something along these lines:</p>
<ul>
<li>import area of interest (as of today) into PostGIS database with osm2pgsql</li>
<li>import same area (as of one year ago) with a different prefix (so that you e.g. get a table <code>planet_osm_line</code> with today's data and <code>old_osm_line</code> with that of a year ago)</li>
<li>delete everything from the "new" table that is in the vicinity of something from the "old" table - one approach could be creating a buffer of, say, 20 meters around every "old" road geometry and then subtracting the resulting polygons from the "new" line geometries</li>
<li>what remains in the "new" table are those bits where one year ago there was no road within 20 meters of it.</li>
</ul>
<p>The 20 meter rule is to account for small geometry changes. Of course you could fine-tune this to e.g. count a street as "new" also if the name has changed from earlier or so.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '22, 19:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-83103" class="comments-container">
&#10;</div>
<div id="comment-tools-83103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83103-form-container" class="comment-form-container">
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

