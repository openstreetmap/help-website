+++
type = "question"
title = "what are nodes in nearest endpoint results"
description = '''I&#x27;m new to OSRM and I need to clarify the following output. Given the following &quot;nearest/v1/driving/79.862839,6.916330?number=5&quot;&quot; Please explain why 2 nodeIDs are given? If so how can a nodeID be 0 in the second array element below.  {  &quot;distance&quot;: 16.449379,  &quot;hint&quot;: &quot;hVIAgP___38IAAAAWgAAAAcAAAAAAA...'''
date = "2018-02-09T15:46:00Z"
lastmod = "2018-02-09T15:46:00Z"
weight = 62030
keywords = [ "osrm", "nodes" ]
aliases = [ "/questions/62030" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [what are nodes in nearest endpoint results](/questions/62030/what-are-nodes-in-nearest-endpoint-results)

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
<span id="post-62030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62030-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSRM and I need to clarify the following output. Given the following "nearest/v1/driving/79.862839,6.916330?number=5"" Please explain why 2 nodeIDs are given? If so how can a nodeID be 0 in the second array element below.</p>
<pre><code> {
    &quot;distance&quot;: 16.449379,
    &quot;hint&quot;: &quot;hVIAgP___38IAAAAWgAAAAcAAAAAAAAACAAAAFoAAAAHAAAAAAAAADAAAADpm8IEaIlpADecwgTqiGkAAQCvA_-mldo=&quot;,
    &quot;location&quot;: [
        79.862761,
        6.916456
    ],
    &quot;name&quot;: &quot; &quot;,
    &quot;nodes&quot;: [
        1346377747,
        4009185293
    ]
},
{
    &quot;distance&quot;: 20.219594,
    &quot;hint&quot;: &quot;hVIAgP___38HAAAABwAAAAAAAABaAAAABwAAAAcAAAAAAAAAWgAAADAAAACOm8IEMIlpADecwgTqiGkAAACvA_-mldo=&quot;,
    &quot;location&quot;: [
        79.86267,
        6.9164
    ],
    &quot;name&quot;: &quot;Srimath Anagarika Dharmapala Mawatha&quot;,
    &quot;nodes&quot;: [
        0,
        1346377747
    ]
},</code></pre>
<p>Also is there any possibility to get the distance between two nodes if NodeIDs are provided?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '18, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/8e69eee546779bbb2c813e4faa58d231?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KlausD94&#39;s gravatar image" />
<p><span>KlausD94</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KlausD94 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Feb '18, 16:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-62030" class="comments-container">
&#10;</div>
<div id="comment-tools-62030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62030-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

