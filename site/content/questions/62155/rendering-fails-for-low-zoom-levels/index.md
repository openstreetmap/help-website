+++
type = "question"
title = "Rendering fails for low zoom levels"
description = '''Hi all, I uploaded full database in to the RDS instance and it works good for zoom levels greater than 5. But it is not rendering tiles for low zoom levels (eg: example.com/0/0/0.png). The screenshot attached here shows the output I get when I run  renderd -f -c /usr/local/etc/renderd.conf.  Please ...'''
date = "2018-02-16T20:05:00Z"
lastmod = "2018-03-08T10:52:00Z"
weight = 62155
keywords = [ "openstreetmap-carto", "rendering", "aws", "mapnik", "zoomlevel" ]
aliases = [ "/questions/62155" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering fails for low zoom levels](/questions/62155/rendering-fails-for-low-zoom-levels)

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
<span id="post-62155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62155-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I uploaded full database in to the RDS instance and it works good for zoom levels greater than 5. But it is not rendering tiles for low zoom levels (eg: example.com/0/0/0.png). The screenshot attached here shows the output I get when I run</p>
<pre><code>renderd -f -c /usr/local/etc/renderd.conf.</code></pre>
<p>Please help me to find the reason behind this?</p>
<p><a href="https://help.openstreetmap.org/upfiles/tiles000_dqG5LyD.PNG"><img src="https://help.openstreetmap.org/upfiles/tiles000_dqG5LyD.PNG" alt="screenshot" /></a></p>
<p>Thanks Subin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-aws" rel="tag" title="see questions tagged &#39;aws&#39;">aws</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '18, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/95e9674b7a67d58ada813e0c6bc38d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subinjp7&#39;s gravatar image" />
<p><span>subinjp7</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subinjp7 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '18, 20:44</strong> </span></p>
</div>
</div>
<div id="comments-container-62155" class="comments-container">
&#10;</div>
<div id="comment-tools-62155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62155-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="62162"></span>

<div id="answer-container-62162" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62162-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps it's worth explaining what typically happens when you ask for a tile to be rendered.</p>
<p>The user makes a request for a tile. It doesn't exist, so Apache asks mod_tile for it (that "START TILE" above). If the tile can't be created fast enough the client will time out - that's normal. Creation of the tile continues. Some time (perhaps many minutes on a very slow system at low zooms) the tile will be created.</p>
<p>The next time the the user requests the same time, the previously rendered tile will be returned, while in the background the new tile is created.</p>
<p>So what happens in the syslog after the snippet that you posted? It could be one of a number of things - maybe the tile gets rendered after a minute or so, or maybe something gets killed because you run out of memory, or maybe "disk access" is so slow on your system that it's still trying to render that tile after many minutes (which was the diagnosis at <a href="https://help.openstreetmap.org/questions/62113/not-getting-output-from-tileserver-when-i-reduce-the-aws-rds-memory-size-to-16gb">https://help.openstreetmap.org/questions/62113/not-getting-output-from-tileserver-when-i-reduce-the-aws-rds-memory-size-to-16gb</a> ).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '18, 22:55</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-62162" class="comments-container">
&#10;</div>
<div id="comment-tools-62162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62162-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62576"></span>

<div id="answer-container-62576" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62576-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This appears to be essentially a duplicate of <a href="https://help.openstreetmap.org/questions/62113/not-getting-output-from-tileserver-when-i-reduce-the-aws-rds-memory-size-to-16gb">this question</a>. You're trying to use a cloud service for something it's not really designed for.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '18, 10:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-62576" class="comments-container">
&#10;</div>
<div id="comment-tools-62576" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62576-form-container" class="comment-form-container">
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

