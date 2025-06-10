+++
type = "question"
title = "Osmosis - Updating with .OSC file - multiple versions of a single entity"
description = '''Hey folks, trying to apply a changefile on an .OSM extract I get the following problem: Thread for task 1-read-xml-change failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: **Pipeline entities are not sorted or contain multiple versions of a single entity**, previous entity type=Node, id...'''
date = "2014-11-09T17:06:00Z"
lastmod = "2014-11-14T15:05:00Z"
weight = 38409
keywords = [ "changeset", ".osc", "osmosis", "diff" ]
aliases = [ "/questions/38409" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis - Updating with .OSC file - multiple versions of a single entity](/questions/38409/osmosis-updating-with-osc-file-multiple-versions-of-a-single-entity)

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
<span id="post-38409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38409-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey folks,</p>
<p>trying to apply a changefile on an .OSM extract I get the following problem:</p>
<pre><code>Thread for task 1-read-xml-change failed org.openstreetmap.osmosis.core.OsmosisRuntimeException: **Pipeline entities are not sorted or contain multiple versions of a single entity**, previous entity type=Node, id=124287, version=11 current entity type=Node, id=124287, version=12.</code></pre>
<p>I am using the following command to update my OSM file:</p>
<pre><code>osmosis --read-xml-change file=&quot;0105-0106.osc&quot; --read-xml file=&quot;haiti-100106.osm&quot; --apply-change --write-xml file=&quot;haiti-100107.osm&quot; -v5</code></pre>
<p>My question is somehow a duplicate of this <a href="https://help.openstreetmap.org/questions/12469/osmosis-merge-issue">question</a>, where the author is able to solve his problem, but I can't figure it out to do the same. As I am not convenient in using the console commands for osmosis, I would greatly appreciate if anyone could correct my code to include the simc task and the sorting of he changefile.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-.osc" rel="tag" title="see questions tagged &#39;.osc&#39;">.osc</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '14, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/999e9ededccde512b3cbd43683233d30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kartenmalergidi&#39;s gravatar image" />
<p><span>kartenmalergidi</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kartenmalergidi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38409" class="comments-container">
&#10;</div>
<div id="comment-tools-38409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38409-form-container" class="comment-form-container">
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

<span id="38561"></span>

<div id="answer-container-38561" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38561-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK, after some trying, failing and trying again, I figured it out. I ended up with the following command that is working:</p>
<pre><code>osmosis --read-xml-change file=&quot;0105-0106.osc&quot; --simc --sc --read-xml file=&quot;haiti-100106.osm&quot; --apply-change --write-xml file=&quot;haiti-100107.osm&quot; -v5 --simc and --sc are added to the command.</code></pre>
<p>The --simc task simplifies the .OSC file. "For example, if an entity is created and modified in a single change file, this task will modify it to be a single create operation with the data of the modify operation." <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.41">Osmosis - Detailed Usage</a>.</p>
<p>The --sc task sorts the .OSC file in a way that all created nodes, ways, and relations are sorted in one &lt;create&gt;, &lt;modify&gt; or &lt;delete&gt; tag. My OSC. file had multiple tags for each category sorted by their respective timestamp. Maybe this helps other newbies ;)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '14, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/999e9ededccde512b3cbd43683233d30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kartenmalergidi&#39;s gravatar image" />
<p><span>kartenmalergidi</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kartenmalergidi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38561" class="comments-container">
&#10;</div>
<div id="comment-tools-38561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38561-form-container" class="comment-form-container">
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

