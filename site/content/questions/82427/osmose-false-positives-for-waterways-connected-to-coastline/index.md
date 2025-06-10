+++
type = "question"
title = "Osmose false positives for waterways connected to coastline"
description = '''In Osmose, almost all rivers and streams in the Philippines connected to the coastline are erroneously tagged as Unconnected river or wrong way flow and Unconnected stream or wrong way flow. I already reported the bug in Osmose backend, and got a fairly vague response. Upon inspecting other countrie...'''
date = "2021-10-31T09:51:00Z"
lastmod = "2021-10-31T21:27:00Z"
weight = 82427
keywords = [ "osmose", "multipolygons" ]
aliases = [ "/questions/82427" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmose false positives for waterways connected to coastline](/questions/82427/osmose-false-positives-for-waterways-connected-to-coastline)

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
<span id="post-82427-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82427-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82427-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Osmose, <a href="https://osmose.openstreetmap.fr/en/map/#item=1220&amp;zoom=9&amp;lat=7.666&amp;lon=122.774&amp;level=1%2C2%2C3&amp;tags=">almost all rivers and streams</a> in the Philippines connected to the coastline are erroneously tagged as <code>Unconnected river or wrong way flow</code> and <code>Unconnected stream or wrong way flow</code>.</p>
<p>I already <a href="https://github.com/osm-fr/osmose-backend/issues/1348">reported the bug</a> in Osmose backend, and got a fairly vague response. Upon inspecting other countries' coastlines, there are no similar reported issues in Osmose. Is there something wrong with the multipolygons/relations of the islands that show these false positives? Can someone check what causes this in the Philippine coastlines but not in any other country?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmose" rel="tag" title="see questions tagged &#39;osmose&#39;">osmose</span> <span class="post-tag tag-link-multipolygons" rel="tag" title="see questions tagged &#39;multipolygons&#39;">multipolygons</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '21, 09:51</strong></p>
<img src="https://secure.gravatar.com/avatar/fb34d7bed35464f64bba89dba8f34f95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JAT86&#39;s gravatar image" />
<p><span>JAT86</span><br />
<span class="score" title="240 reputation points">240</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JAT86 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82427" class="comments-container">
&#10;</div>
<div id="comment-tools-82427" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82427-form-container" class="comment-form-container">
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

<span id="82436"></span>

<div id="answer-container-82436" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82436-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess the "vague answer" hints that it's indeed a problem with osmose-backend.</p>
<p>I think that, as in other application consuming OSM data, coastlines are updated separately, because it's a really resource hungry operation. The coastline of the island I've checked was updated in June, the river days ago, maybe osmose doesn't compare objects from the same date...</p>
<p>Hope this will get resolved soon, but I'm sure you don't have to worry about it.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '21, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-82436" class="comments-container">
&#10;</div>
<div id="comment-tools-82436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82436-form-container" class="comment-form-container">
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

