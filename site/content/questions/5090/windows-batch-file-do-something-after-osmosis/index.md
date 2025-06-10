+++
type = "question"
title = "Windows Batch-File: do something after Osmosis"
description = '''hi, I have build a Batch-file for processing OSM. i whant to call Osmosis multiple times and call an other program after that  so i do that: osmosis&#92;bin&#92;osmosis.bat --rx file=&quot;gesamtbereich-map.osm&quot; --bounding-box top=53.743 left=9.669 bottom=53.287 right=10.317 --wx file=&quot;grossberich-map.osm&quot; echo ...'''
date = "2011-05-10T14:25:00Z"
lastmod = "2011-05-10T16:01:00Z"
weight = 5090
keywords = [ "windows", "batch", "osmosis" ]
aliases = [ "/questions/5090" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Windows Batch-File: do something after Osmosis](/questions/5090/windows-batch-file-do-something-after-osmosis)

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
<span id="post-5090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5090-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi, I have build a Batch-file for processing OSM. i whant to call Osmosis multiple times and call an other program after that</p>
<p>so i do that:</p>
<pre><code>osmosis\bin\osmosis.bat --rx file=&quot;gesamtbereich-map.osm&quot; --bounding-box top=53.743 left=9.669 bottom=53.287 right=10.317 --wx file=&quot;grossberich-map.osm&quot;
echo test</code></pre>
<p>but after osmosis the "test" wouldn't be printed.</p>
<p>the only result is that:</p>
<pre><code>Der Befehl &quot;JAVACMD&quot; ist entweder falsch geschrieben oder
konnte nicht gefunden werden.
10.05.2011 15:23:05 org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.38
10.05.2011 15:23:05 org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
10.05.2011 15:23:05 org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
10.05.2011 15:23:05 org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
10.05.2011 15:23:06 org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline complete.
10.05.2011 15:23:06 org.openstreetmap.osmosis.core.Osmosis run
INFO: Total execution time: 1437 milliseconds.</code></pre>
<p>where is the "test"?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-batch" rel="tag" title="see questions tagged &#39;batch&#39;">batch</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '11, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/db9d4c9ffd75f95f97122bbc97b90a64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="josias&#39;s gravatar image" />
<p><span>josias</span><br />
<span class="score" title="598 reputation points">598</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="josias has 3 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-5090" class="comments-container">
&#10;</div>
<div id="comment-tools-5090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5090-form-container" class="comment-form-container">
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

<span id="5091"></span>

<div id="answer-container-5091" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5091-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="josias has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a couple of things you might want to try. You could for example try adding call before the osmosis line to see if that completes the osmosis line before returning to the batch file. Alternatively you could put multiple commands on a single line separated by &amp;&amp; as per the batch file I use for keeping a local .osm file synced (imagine that the following is all on a single line):</p>
<pre><code>osmosis --rri --simc --rx tendring.osm --ac --bp clipIncompleteEntities=yes file=tendring.txt --wx new.osm &amp;&amp; copy new.osm tendring.osm /y &amp;&amp; del new.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 May '11, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-5091" class="comments-container">
<span id="5092"></span>
<div id="comment-5092" class="comment">
<div id="post-5092-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Using CALL works for me in a test batch script. Very useful answer. You could also use cygwin which will run the osmosis.bat DOS batch file successfully.</p>
</div>
<div id="comment-5092-info" class="comment-info">
<span class="comment-age">(10 May '11, 15:04)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="5093"></span>
<div id="comment-5093" class="comment">
<div id="post-5093-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thanks, that works: call osmosis.bat</p>
</div>
<div id="comment-5093-info" class="comment-info">
<span class="comment-age">(10 May '11, 16:01)</span> <span class="comment-user userinfo">josias</span>
</div>
</div>
</div>
<div id="comment-tools-5091" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5091-form-container" class="comment-form-container">
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

