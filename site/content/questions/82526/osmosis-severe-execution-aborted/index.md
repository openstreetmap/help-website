+++
type = "question"
title = "osmosis: SEVERE: Execution aborted."
description = '''Hello, I&#x27;m trying to filter basic OSM data with Osmosis. I can&#x27;t seem to get osmosis running though. I&#x27;ve now cut down the command-code to:  osmosis &#92; --read-pbf file=~/desktop/BA/Modell/SciGRID/data/01_osm_raw_data/germany-24.10.21.osm.pbf  --write-null  and I still get the same Error:  SEVERE: Exe...'''
date = "2021-11-08T19:21:00Z"
lastmod = "2021-11-09T13:48:00Z"
weight = 82526
keywords = [ "mac", "osm", "osmosis" ]
aliases = [ "/questions/82526" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmosis: SEVERE: Execution aborted.](/questions/82526/osmosis-severe-execution-aborted)

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
<span id="post-82526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82526-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I'm trying to filter basic OSM data with Osmosis. I can't seem to get osmosis running though. I've now cut down the command-code to:</p>
<p><code> osmosis \ --read-pbf file=~/desktop/BA/Modell/SciGRID/data/01_osm_raw_data/germany-24.10.21.osm.pbf --write-null </code></p>
<p>and I still get the same Error:</p>
<p><code> SEVERE: Execution aborted. org.openstreetmap.osmosis.core.OsmosisRuntimeException: The following named pipes () and 1 default pipes have not been terminated with appropriate output sinks. </code></p>
<p>I really don't know what I'm doing wrong.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '21, 19:21</strong></p>
<img src="https://secure.gravatar.com/avatar/3a250fe9d89941f54efc48c2dd62c7ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thiblo&#39;s gravatar image" />
<p><span>thiblo</span><br />
<span class="score" title="-11 reputation points">-11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thiblo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82526" class="comments-container">
&#10;</div>
<div id="comment-tools-82526" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82526-form-container" class="comment-form-container">
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

<span id="82527"></span>

<div id="answer-container-82527" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82527-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This error message appears when I run your command without the "--write-null". Make sure that everything is actually on one line. Drop the backslash behind osmosis, and write both the --read-pbf and the --write-null into the same line as "osmosis". Make sure that whatever shell script is called when you run "osmosis" doesn't accidentally remove some of the arguments.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '21, 23:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-82527" class="comments-container">
<span id="82529"></span>
<div id="comment-82529" class="comment">
<div id="post-82529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your help. That actually works, I thought everything will be read in one line as long as I don't use any backslash. How do you run multiple commands though? I've just have a space block between every command but that doesn't seem like the best option.</p>
</div>
<div id="comment-82529-info" class="comment-info">
<span class="comment-age">(09 Nov '21, 12:12)</span> <span class="comment-user userinfo">thiblo</span>
</div>
</div>
<span id="82530"></span>
<div id="comment-82530" class="comment">
<div id="post-82530-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can use backslashes to improve readability, but then you have to make sure to put one at the end of each line. I just advised you to get rid of that above in order to minimize the potential for errors ;)</p>
</div>
<div id="comment-82530-info" class="comment-info">
<span class="comment-age">(09 Nov '21, 13:48)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82527" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82527-form-container" class="comment-form-container">
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

