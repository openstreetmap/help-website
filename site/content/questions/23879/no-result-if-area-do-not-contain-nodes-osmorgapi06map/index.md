+++
type = "question"
title = "No result if area do not contain nodes (osm.org/api/0.6/map)"
description = '''I use http://api.openstreetmap.org/api/0.6/map?bbox=-118.28183448540011,34.02306804799843,-118.28091502587874,34.023833568382074 to ask for buildings or streets within the area that I provide. But I get nothing if my area do not contain Nodes coordinates which make of way(building or polygon). While...'''
date = "2013-07-01T21:25:00Z"
lastmod = "2013-07-02T08:47:00Z"
weight = 23879
keywords = [ "nodes", "api", "tagging" ]
aliases = [ "/questions/23879" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No result if area do not contain nodes (osm.org/api/0.6/map)](/questions/23879/no-result-if-area-do-not-contain-nodes-osmorgapi06map)

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
<span id="post-23879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23879-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use <a href="http://api.openstreetmap.org/api/0.6/map?bbox=-118.28183448540011,34.02306804799843,-118.28091502587874,34.023833568382074">http://api.openstreetmap.org/api/0.6/map?bbox=-118.28183448540011,34.02306804799843,-118.28091502587874,34.023833568382074</a> to ask for buildings or streets within the area that I provide. But I get nothing if my area do not contain Nodes coordinates which make of way(building or polygon). While, my area is within the way. How can I handle with it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '13, 21:25</strong></p>
<img src="https://secure.gravatar.com/avatar/27e2ceed483806d9bb9da1b9d153ae12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dong%20han6&#39;s gravatar image" />
<p><span>dong han6</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dong han6 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jul '13, 01:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-23879" class="comments-container">
&#10;</div>
<div id="comment-tools-23879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23879-form-container" class="comment-form-container">
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

<span id="23891"></span>

<div id="answer-container-23891" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23891-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-23891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The map call on the main API searches for nodes within the bounding box only and not for intersecting way segments.</p>
<p>You can use Overpass API instead, for example via <a href="http://overpass-turbo.eu/s/rm">Overpass Turbo</a>:</p>
<pre><code>(way(34.02306804799843,-118.28183448540011,34.023833568382074,-118.28091502587874);&gt;;);out meta;</code></pre>
<p>This finds all ways that intersect the given bounding box. For more details, please read about some map call variants in the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Sample_map_calls">Overpass API documentation</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '13, 08:47</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-23891" class="comments-container">
&#10;</div>
<div id="comment-tools-23891" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23891-form-container" class="comment-form-container">
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

