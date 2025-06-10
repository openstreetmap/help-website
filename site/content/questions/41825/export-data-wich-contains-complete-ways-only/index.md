+++
type = "question"
title = "Export data wich contains complete ways only"
description = '''Hello, I want to export osm data from open street map. However, the file should only contain complete ways. This means, the file should not contain ways which reference nodes outside the target area. Does somebody know how I can do this in open street map or maybe there is a tool which can eliminate...'''
date = "2015-03-20T16:16:00Z"
lastmod = "2015-03-20T22:05:00Z"
weight = 41825
keywords = [ "export", "osm" ]
aliases = [ "/questions/41825" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export data wich contains complete ways only](/questions/41825/export-data-wich-contains-complete-ways-only)

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
<span id="post-41825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41825-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I want to export osm data from open street map. However, the file should only contain complete ways. This means, the file should not contain ways which reference nodes outside the target area.</p>
<p>Does somebody know how I can do this in open street map or maybe there is a tool which can eliminate ways which are not complete in an osm file.</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Mar '15, 16:16</strong></p>
<img src="https://secure.gravatar.com/avatar/91a08b5958dcd13b5110be8da89877c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stteffen&#39;s gravatar image" />
<p><span>stteffen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stteffen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41825" class="comments-container">
&#10;</div>
<div id="comment-tools-41825" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41825-form-container" class="comment-form-container">
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

<span id="41834"></span>

<div id="answer-container-41834" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41834-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Exporting data through the web site will always yield complete ways. Extracting data with osmosis from a larger OSM file also offers a completeWays option. If you already have a file with some ways that reference missing nodes, the following trick</p>
<pre><code>osmosis --read-pbf input.osm.pbf --bb left=-180 right=180 top=90 bottom=-90 clipIncompleteEntities=true --write-pbf output.osm.pbf</code></pre>
<p>will remove all dangling references from ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '15, 22:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-41834" class="comments-container">
&#10;</div>
<div id="comment-tools-41834" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41834-form-container" class="comment-form-container">
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

