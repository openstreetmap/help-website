+++
type = "question"
title = "Overpass Turbo: how to fetch an inverted or negative result within a given administrative area"
description = '''I have entered &#x27;prow_ref like &quot;Binfield Heath&quot;&#x27; into Overpass Turbo wizard that returns all results of the key &#x27;prow_ref&#x27; containing the value &#x27;Binfield Heath&#x27;, which is my local civil parish. This serves me well. However, it is of greater use if I can query those Public Rights of Way with values pu...'''
date = "2016-02-03T10:16:00Z"
lastmod = "2016-02-03T13:21:00Z"
weight = 47852
keywords = [ "boundaries", "overpass-turbo" ]
aliases = [ "/questions/47852" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass Turbo: how to fetch an inverted or negative result within a given administrative area](/questions/47852/overpass-turbo-how-to-fetch-an-inverted-or-negative-result-within-a-given-administrative-area)

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
<span id="post-47852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47852-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have entered 'prow_ref like "Binfield Heath"' into Overpass Turbo wizard that returns all results of the key 'prow_ref' containing the value 'Binfield Heath', which is my local civil parish. This serves me well. However, it is of greater use if I can query those Public Rights of Way with values public_footpath|public_bridleway|restricted_byway|byway_open_to_all_traffic|public_right_of_way that do not have the key 'prow_ref' but within a given named parish, or admin_level 10 boundary, not a bounding box.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Feb '16, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ffcc41f13929627742b4936ec178c6f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silver%20mapper&#39;s gravatar image" />
<p><span>silver mapper</span><br />
<span class="score" title="256 reputation points">256</span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silver mapper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47852" class="comments-container">
&#10;</div>
<div id="comment-tools-47852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47852-form-container" class="comment-form-container">
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

<span id="47853"></span>

<div id="answer-container-47853" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47853-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to use the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Difference">overpass difference operator</a>.</p>
<p>So first need to query the big set (with all ways in the admin area), then query the smaller set (all ways that also have 'prow_ref' in that area), and finally apply the difference and output it.</p>
<p>See the example:</p>
<pre><code>area[&quot;name&quot;=&quot;xxx&quot;][&quot;admin_level&quot;=8]-&gt;.a;
(
  way[&quot;highway&quot;](area.a);
  -way[&quot;highway&quot;][&quot;prow_ref&quot;](area.a);
);
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '16, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-47853" class="comments-container">
<span id="47864"></span>
<div id="comment-47864" class="comment">
<div id="post-47864-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thank you for your prompt reply. The result includes all way types, regrettably, not ways with with values public_footpath|public_bridleway|restricted_byway|byway_open_to_all_traffic|public_right_of_way only.</p>
</div>
<div id="comment-47864-info" class="comment-info">
<span class="comment-age">(03 Feb '16, 12:46)</span> <span class="comment-user userinfo">silver mapper</span>
</div>
</div>
<span id="47868"></span>
<div id="comment-47868" class="comment">
<div id="post-47868-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's only an example query. I don't know how ways like restricted_bridleway are tagged in your area, you should look that up, then you can change the <code>["highway']</code> selector in something else like <code>["highway"="bridleway"]</code>. But as this question seems to focus on finding the "negative" or difference, that's what I gave as answer.</p>
</div>
<div id="comment-47868-info" class="comment-info">
<span class="comment-age">(03 Feb '16, 12:52)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
<span id="47869"></span>
<div id="comment-47869" class="comment">
<div id="post-47869-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For info, a restricted byway would normally be tagged "designation=restricted_byway". It's a specific access allowance that allows non-motorised traffic, so a horse and cart is OK but e.g. a moped isn't.</p>
</div>
<div id="comment-47869-info" class="comment-info">
<span class="comment-age">(03 Feb '16, 13:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47853" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47853-form-container" class="comment-form-container">
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

