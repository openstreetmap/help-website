+++
type = "question"
title = "Translate JOSM Filter to Osmosis/Osmfilter"
description = '''Hello Everyone, I am really new to OSM and I am trying to extract all public transportation Data. I am currently using a JOSM Filter that basically gives me what I want. (child(type:relation (route= bus or route=trolleybus or route=ferry or route=detour or route=train or route=tram or route=railway ...'''
date = "2020-10-15T09:11:00Z"
lastmod = "2020-10-22T08:20:00Z"
weight = 77109
keywords = [ "filter", "josm", "extract", "osmfilter", "osmosis" ]
aliases = [ "/questions/77109" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Translate JOSM Filter to Osmosis/Osmfilter](/questions/77109/translate-josm-filter-to-osmosisosmfilter)

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
<span id="post-77109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77109-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Everyone, I am really new to OSM and I am trying to extract all public transportation Data. I am currently using a JOSM Filter that basically gives me what I want.</p>
<p><code>(child(type:relation (route= bus or route=trolleybus or route=ferry or route=detour or route=train or route=tram or route=railway or route=subway or route=light_rail or route=tracks)))</code></p>
<p>I use this filter by inverting the results.</p>
<p>By copying my filtered content into a new layer and then saving it to *.osm.pbf I can even use the filtered content somewhere else. Their are three problems with that approach because of the Rendering Aspect of JOSM this approach is really slow, consumes a lot of resources and I can’t really automate it.<br />
I tried to “translate” my JOSM Filter to use it in Osmosis are Osmfilter, but I couldn’t get it right. Does anyone have a solution for my Problem with a better performance and a way to automate it with a script?I am also flexibel with the tools, I used Osmfilter and Osmosis because it seemed that they were the go to Tools for the task at hand.</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '20, 09:11</strong></p>
<img src="https://secure.gravatar.com/avatar/bb0fe2070a2b3e4c6a5b09d4b7b7ec99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ale_fhw&#39;s gravatar image" />
<p><span>ale_fhw</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ale_fhw has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-77109" class="comments-container">
&#10;</div>
<div id="comment-tools-77109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77109-form-container" class="comment-form-container">
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

<span id="77194"></span>

<div id="answer-container-77194" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77194-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If anyone is curious how i solved my problem. I just queried the data already "filtered" from Overpass-API.</p>
<p>The Query I used was:</p>
<pre><code>  http://overpass-api.de/api/interpreter?data=[out:xml];
  (rel(55.78,10.58,51.89,12.73) 
  [&quot;route&quot;~&quot;bus|light_rail|trolleybus|ferry|detour|train|tram|railway|subway|tracks&quot;];); 
  out meta;
  &gt;; 
  out skel meta;</code></pre>
<p>If anyone is looking at a similar Problem I strongly recommend the <em>Overpass API</em> since the QL is really powerful in contrast to the rather elementary possibilities of <em>osmfilter</em>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '20, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/bb0fe2070a2b3e4c6a5b09d4b7b7ec99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ale_fhw&#39;s gravatar image" />
<p><span>ale_fhw</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ale_fhw has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '20, 08:26</strong> </span></p>
</div>
</div>
<div id="comments-container-77194" class="comments-container">
&#10;</div>
<div id="comment-tools-77194" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77194-form-container" class="comment-form-container">
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

