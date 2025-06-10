+++
type = "question"
title = "Overpass XML - Retrieving ways which share nodes..."
description = '''Greetings! I&#x27;m working on tracing some underground pipelines, and I&#x27;m using an Overpass XML script (via overpass turbo) to bring existing map nodes, ways, and relations (man_made=pipeline) in to JOSM to build upon. Some pipelines have existing (and inaccurate) TIGER data for various segments. Unfort...'''
date = "2014-01-02T15:34:00Z"
lastmod = "2014-01-02T17:12:00Z"
weight = 29546
keywords = [ "xml", "overpass" ]
aliases = [ "/questions/29546" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass XML - Retrieving ways which share nodes...](/questions/29546/overpass-xml-retrieving-ways-which-share-nodes)

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
<span id="post-29546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29546-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings!</p>
<p>I'm working on tracing some underground pipelines, and I'm using an Overpass XML script (via overpass turbo) to bring existing map nodes, ways, and relations (man_made=pipeline) in to JOSM to build upon. Some pipelines have existing (and inaccurate) TIGER data for various segments. Unfortunately, the TIGER data frequently has nodes which are shared with other map elements such as roads, political borders, rivers, etc. etc. When I delete these TIGER pipeline ways after replacing them, the shared nodes throw conflict warnings because JOSM wasn't aware of their shared nature.</p>
<p>I need some assistance in crafting an Overpass XML script which will include not only the (man_made=pipeline) ways, but also any ways which are "shared" by the nodes I retrieve in the process. That way, when I delete the TIGER pipeline after its been replaced, any other element which may share a node is there and remains intact, causing no conflicts.</p>
<p>Are there any experts who can lead me down the right path for this? I'd appreciate it greatly!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jan '14, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/e795e6d25ba5d6b1f651ba091399c6f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="greggerm&#39;s gravatar image" />
<p><span>greggerm</span><br />
<span class="score" title="45 reputation points">45</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="greggerm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29546" class="comments-container">
&#10;</div>
<div id="comment-tools-29546" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29546-form-container" class="comment-form-container">
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

<span id="29551"></span>

<div id="answer-container-29551" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29551-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="greggerm has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After you have selected the ways, you probably have a <code>&lt;recurse type="down" /&gt;</code> (or equivalent) statement to get the nodes. You can than continue to select their parents with something like <code>&lt;recurse type="up" /&gt;</code>. I'd suggest something like the following:</p>
<pre><code>&lt;union&gt;
  … select pipeline ways …
  &lt;recurse type=&quot;down&quot;/&gt;
  &lt;recurse type=&quot;up&quot; /&gt;
  &lt;recurse type=&quot;down&quot; /&gt;
&lt;/union&gt;
&lt;print mode=&quot;meta&quot; /&gt;</code></pre>
<p>(The last recurse-down makes sure that the "shared" ways also get loaded completely.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '14, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-29551" class="comments-container">
<span id="29554"></span>
<div id="comment-29554" class="comment">
<div id="post-29554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Bingo. I had to make some adjustments to account for my poor script writing, but adding the new up/down has accomplished the goal. Thanks so much!</p>
</div>
<div id="comment-29554-info" class="comment-info">
<span class="comment-age">(02 Jan '14, 17:12)</span> <span class="comment-user userinfo">greggerm</span>
</div>
</div>
</div>
<div id="comment-tools-29551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29551-form-container" class="comment-form-container">
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

