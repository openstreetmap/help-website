+++
type = "question"
title = "overpass - get way direction"
description = '''Thinking about how to visualize the direction of a way in mapcontrib or umap instance using an Overpass query: it might be done by querying the second node of a way. If you overlay that node on the way itself, it can show you where it begins. Maybe again for the second-last. (Not the first and last ...'''
date = "2017-02-10T07:49:00Z"
lastmod = "2017-02-24T07:48:00Z"
weight = 54584
keywords = [ "ways", "overpass", "direction", "mapcontrib", "umap" ]
aliases = [ "/questions/54584" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [overpass - get way direction](/questions/54584/overpass-get-way-direction)

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
<span id="post-54584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54584-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Thinking about how to visualize the direction of a way in mapcontrib or umap instance using an Overpass query: it might be done by querying the second node of a way. If you overlay that node on the way itself, it can show you where it begins. Maybe again for the second-last. (Not the first and last nodes, because they would often overlap with the nodes of an adjacent way)</p>
<p>Say I want to show the direction of highways that don't have a oneway tag in this way, how would I go from this basic query?</p>
<pre><code>[out:json][timeout:25];
(
  way[&quot;highway&quot;][!&quot;oneway&quot;]({{bbox}});
);
out body;
&gt;;
out skel qt;</code></pre>
<p>If you have a better idea to approach the problem, do go ahead.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-direction" rel="tag" title="see questions tagged &#39;direction&#39;">direction</span> <span class="post-tag tag-link-mapcontrib" rel="tag" title="see questions tagged &#39;mapcontrib&#39;">mapcontrib</span> <span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '17, 07:49</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-54584" class="comments-container">
&#10;</div>
<div id="comment-tools-54584" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54584-form-container" class="comment-form-container">
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

<span id="54782"></span>

<div id="answer-container-54782" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54782-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joost schouppe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>visualize the direction of a way</p>
</blockquote>
<p>The optimal solution for this would be to make the displaying software (here: umap) render the direction of the lines for one.</p>
<blockquote>
<p>[…] by querying the second node of a way.</p>
</blockquote>
<p>The Overpass API doesn't (yet?) support nth-child queries for way-nodes (or relation members).</p>
<p>But you could do this in post-processing: After converting the Overpass result to GeoJSON, run something like the following (in nodejs):</p>
<p><code>var geojson = … geojson.features.forEach(f =&gt; { if (f.geometry.type !== "LineString") return; var newcoords = [0,0], coords = f.geometry.coordinates; newcoords[0] = coords[0][0]*0.75+coords[1][0]*0.25; newcoords[1] = coords[0][1]*0.75+coords[1][1]*0.25; geojson.features.push({type:'Feature', properties:{}, geometry:{type:'Point', coordinates:newcoords}}); });</code></p>
<p>After that, there are additional point features in the <code>geojson</code> which are placed near the start point of each LineString (1 quarter distance towards the second vertex).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '17, 16:24</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-54782" class="comments-container">
<span id="54791"></span>
<div id="comment-54791" class="comment">
<div id="post-54791-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the help!</p>
</div>
<div id="comment-54791-info" class="comment-info">
<span class="comment-age">(24 Feb '17, 07:48)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-54782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54782-form-container" class="comment-form-container">
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

