+++
type = "question"
title = "Extract two countries in one pass of osmosis"
description = '''I have planet.osm.pbf, a poly file for the USA, and a poly file for Canada. Is it possible to get both countries into one output file with one pass of osmosis? Or can the poly files be merged? If so, what d I have to look out for? Regards, Jim'''
date = "2012-07-09T23:16:00Z"
lastmod = "2012-07-10T07:42:00Z"
weight = 14125
keywords = [ "extract" ]
aliases = [ "/questions/14125" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract two countries in one pass of osmosis](/questions/14125/extract-two-countries-in-one-pass-of-osmosis)

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
<span id="post-14125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14125-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have planet.osm.pbf, a poly file for the USA, and a poly file for Canada.</p>
<p>Is it possible to get both countries into one output file with one pass of osmosis?</p>
<p>Or can the poly files be merged? If so, what d I have to look out for?</p>
<p>Regards, Jim</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '12, 23:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a91c10377b432d3352bd072df1aa4633?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="obrienj&#39;s gravatar image" />
<p><span>obrienj</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="obrienj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14125" class="comments-container">
&#10;</div>
<div id="comment-tools-14125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14125-form-container" class="comment-form-container">
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

<span id="14127"></span>

<div id="answer-container-14127" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14127-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The easiest way of merging the poly files is to convert them to .osm format using poly2osm.pl from <a href="http://svn.openstreetmap.org/applications/utils/osm-extract/polygons,">http://svn.openstreetmap.org/applications/utils/osm-extract/polygons,</a> then combine them in JOSM, and convert them back with osm2poly.pl. However, if you are not too picky about the US-Mexico boundary, you could also use JOSM to quickly draw a polygon around the US and Canada by hand, save that, and convert to .poly.</p>
<p>Regarding your Osmosis question, yes it is possible, and examples for that are <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Examples">on the Wiki</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '12, 07:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-14127" class="comments-container">
&#10;</div>
<div id="comment-tools-14127" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14127-form-container" class="comment-form-container">
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

