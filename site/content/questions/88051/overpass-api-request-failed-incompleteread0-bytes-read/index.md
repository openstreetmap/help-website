+++
type = "question"
title = "Overpass API request failed: IncompleteRead(0 bytes read)"
description = '''Hello everyone! Could anyone help me with this issue:  Overpass API request failed: IncompleteRead(0 bytes read) The query code is: [out:json] [timeout:9000]; ( way[&quot;highway&quot;=motorway](bbox:{x_min},{y_min},{x_max},{y_max}); way[&quot;highway&quot;=trunk](bbox:{x_min},{y_min},{x_max},{y_max}); way[&quot;highway&quot;=pr...'''
date = "2023-12-14T12:41:00Z"
lastmod = "2023-12-14T12:41:00Z"
weight = 88051
keywords = [ "failed", "bbox", "incomplete" ]
aliases = [ "/questions/88051" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API request failed: IncompleteRead(0 bytes read)](/questions/88051/overpass-api-request-failed-incompleteread0-bytes-read)

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
<span id="post-88051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88051-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone! Could anyone help me with this issue: Overpass API request failed: IncompleteRead(0 bytes read)</p>
<p>The query code is:</p>
<pre><code>[out:json] [timeout:9000];
(
way[&quot;highway&quot;=motorway](bbox:{x_min},{y_min},{x_max},{y_max});
way[&quot;highway&quot;=trunk](bbox:{x_min},{y_min},{x_max},{y_max});
way[&quot;highway&quot;=primary](bbox:{x_min},{y_min},{x_max},{y_max});
...
way[&quot;highway&quot;=tertiary_link](bbox:{x_min},{y_min},{x_max},{y_max});
);
(._;&gt;;);
out body;</code></pre>
<p>Where bbox is: 41.207270630721524, 1.597245844790248, 41.77753602675901, 2.427776294121272 There are 11 values for this key so far, but this query will be supplied by other ones, so I would like to manage these issues. I've been trying to change the timeout randomly or even remove its definition, but to no avail.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span> <span class="post-tag tag-link-incomplete" rel="tag" title="see questions tagged &#39;incomplete&#39;">incomplete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '23, 12:41</strong></p>
<img src="https://secure.gravatar.com/avatar/7426f3a1e92cbadd1fb13a11c35a7712?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vwvbrand&#39;s gravatar image" />
<p><span>vwvbrand</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vwvbrand has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Dec '23, 12:47</strong> </span></p>
</div>
</div>
<div id="comments-container-88051" class="comments-container">
&#10;</div>
<div id="comment-tools-88051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88051-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

