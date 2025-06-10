+++
type = "question"
title = "Getting roads only for Myanmar"
description = '''Hello, I would like to extract all roads in the Myanmar OSM data using osmosis in the window&#x27;s command prompt. The following is my code: osmosis --read-xml myanmar-latest (2).osm --tf accept-ways highway=* --used-node --write-xml myanmar-roads.osm I got the following error: Nov 16, 2017 5:45:15 PM o...'''
date = "2017-11-16T10:02:00Z"
lastmod = "2017-11-17T19:52:00Z"
weight = 60641
keywords = [ "filter", "myanmar", "road", "osmosis", "highway" ]
aliases = [ "/questions/60641" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Getting roads only for Myanmar](/questions/60641/getting-roads-only-for-myanmar)

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
<span id="post-60641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60641-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Hello,</strong></p>
<p><strong>I would like to extract all roads in the Myanmar OSM data using osmosis in the window's command prompt. The following is my code:</strong></p>
<p>osmosis --read-xml myanmar-latest (2).osm --tf accept-ways highway=* --used-node --write-xml myanmar-roads.osm</p>
<p><strong>I got the following error:</strong></p>
<p>Nov 16, 2017 5:45:15 PM org.openstreetmap.osmosis.core.Osmosis main</p>
<p>SEVERE: Execution aborted.</p>
<p>org.openstreetmap.osmosis.core.OsmosisRuntimeException: Only one default (un-named) argument can exist per task. Arguments 3 and 2 have no name.</p>
<p><strong>Any idea where I went wrong and how to fix this? Thanks in advance!</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-myanmar" rel="tag" title="see questions tagged &#39;myanmar&#39;">myanmar</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '17, 10:02</strong></p>
<img src="https://secure.gravatar.com/avatar/cd0567ad1b62cbdabbc2f74b9a1ffd91?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nrsbrn&#39;s gravatar image" />
<p><span>nrsbrn</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nrsbrn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60641" class="comments-container">
&#10;</div>
<div id="comment-tools-60641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60641-form-container" class="comment-form-container">
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

<span id="60656"></span>

<div id="answer-container-60656" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60656-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nrsbrn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If your file name contains spaces, you probably need to use quotes around it. Try replacing</p>
<pre><code>--read-xml myanmar-latest (2).osm</code></pre>
<p>with</p>
<pre><code>--read-xml &quot;myanmar-latest (2).osm&quot;</code></pre>
<p>or rename the file to something without spaces.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '17, 18:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-60656" class="comments-container">
<span id="60660"></span>
<div id="comment-60660" class="comment">
<div id="post-60660-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Oh wow! I'm new to using this tool. I've added the quote and managed to get the data I need. Thank you for your help, really appreciate it!</p>
</div>
<div id="comment-60660-info" class="comment-info">
<span class="comment-age">(17 Nov '17, 02:47)</span> <span class="comment-user userinfo">nrsbrn</span>
</div>
</div>
<span id="60670"></span>
<div id="comment-60670" class="comment">
<div id="post-60670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Glad to help! :) If your problem is solved, you can mark the question as answered by clicking the checkmark icon next to an answer.</p>
</div>
<div id="comment-60670-info" class="comment-info">
<span class="comment-age">(17 Nov '17, 19:52)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-60656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60656-form-container" class="comment-form-container">
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

