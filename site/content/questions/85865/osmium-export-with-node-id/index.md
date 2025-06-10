+++
type = "question"
title = "osmium export with node id"
description = '''Hi. I use osmium for export map.osm to map.geojson (use in mobile app). How can i add node id to geojson file? My code:  osmium export map.osm -o data.geojson '''
date = "2022-10-12T11:55:00Z"
lastmod = "2022-10-12T12:39:00Z"
weight = 85865
keywords = [ "osmium" ]
aliases = [ "/questions/85865" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmium export with node id](/questions/85865/osmium-export-with-node-id)

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
<span id="post-85865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85865-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I use osmium for export map.osm to map.geojson (use in mobile app). How can i add node id to geojson file?</p>
<p>My code:</p>
<blockquote>
<p>osmium export map.osm -o data.geojson</p>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Oct '22, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/3fc2b5a99ace097647679905940c0fdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kadi4&#39;s gravatar image" />
<p><span>kadi4</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kadi4 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-85865" class="comments-container">
&#10;</div>
<div id="comment-tools-85865" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85865-form-container" class="comment-form-container">
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

<span id="85866"></span>

<div id="answer-container-85866" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85866-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I close ticket.</p>
<p>I edit config file:</p>
<pre><code>&quot;id&quot;:        true,</code></pre>
<p>and then:</p>
<pre><code>osmium export -c config map.osm -o data.geojson</code></pre>
<p>Result:</p>
<pre><code>{&quot;type&quot;:&quot;Feature&quot;,&quot;geometry&quot;:{&quot;type&quot;:&quot;Point&quot;,&quot;coordinates&quot;:[40.5024238,55.9909894]},&quot;properties&quot;:{&quot;@id&quot;:1562589184,&quot;power&quot;:&quot;tower&quot;}}</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Oct '22, 12:39</strong></p>
<img src="https://secure.gravatar.com/avatar/3fc2b5a99ace097647679905940c0fdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kadi4&#39;s gravatar image" />
<p><span>kadi4</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kadi4 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-85866" class="comments-container">
&#10;</div>
<div id="comment-tools-85866" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85866-form-container" class="comment-form-container">
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

