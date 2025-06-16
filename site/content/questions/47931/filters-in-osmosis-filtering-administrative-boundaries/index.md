+++
type = "question"
title = "Filters in Osmosis; filtering administrative boundaries"
description = '''I am trying to filter administrative boundaries of admin_level 4. I carefully read the Osmosis reference and some examples, and composed the following query (the chevrons allow to feed multiple lines into the Windows Command Prompt): osmosis ^  --read-pbf-fast workers=2 &quot;D:/GIS Data/Data/netherlands...'''
date = "2016-02-05T02:43:00Z"
lastmod = "2016-02-06T10:49:00Z"
weight = 47931
keywords = [ "extract", "osmosis" ]
aliases = [ "/questions/47931" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filters in Osmosis; filtering administrative boundaries](/questions/47931/filters-in-osmosis-filtering-administrative-boundaries)

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
<span id="post-47931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47931-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to filter administrative boundaries of admin_level 4. I carefully read the Osmosis reference and some examples, and composed the following query (the chevrons allow to feed multiple lines into the Windows Command Prompt):</p>
<pre><code>osmosis ^
  --read-pbf-fast workers=2 &quot;D:/GIS Data/Data/netherlands-latest.osm.pbf&quot; ^
  --tf accept-relations boundary=administrative ^
  --tf accept-relations admin_level=4 ^
  --tf reject-ways ^
  --tf reject-nodes ^
  --used-way ^
  --used-node ^
  --write-pbf omitmetadata=true file=&quot;D:/GIS Data/Tijdelijk/provinciestestosmosis.osm.pbf&quot;</code></pre>
<p>This works fine in the sense that it yields all the required relations (checked the OSM file manually). However, no ways of nodes are included, which is not what I wanted as I need them to plot the administrative boundaries. It seemed an obvious error to me as I first accept the required relations, then reject all ways and nodes, leaving Osmosis unable to resolve the used ways and nodes in the relations.</p>
<p>Then did the following, however this yields the same result:</p>
<pre><code>osmosis ^
  --read-pbf-fast workers=2 &quot;D:/GIS Data/Data/netherlands-latest.osm.pbf&quot; ^
  --tf accept-relations boundary=administrative ^
  --tf accept-relations admin_level=4 ^
  --used-node ^
  --tf reject-ways ^
  --tf reject-nodes ^
  --write-pbf omitmetadata=true file=&quot;D:/GIS Data/Tijdelijk/provinciestestosmosis.osm.pbf&quot;</code></pre>
<p>Then did the following:</p>
<pre><code>osmosis ^
  --read-pbf-fast workers=2 &quot;D:/GIS Data/Data/netherlands-latest.osm.pbf&quot; ^
  --tf accept-relations boundary=administrative ^
  --tf accept-relations admin_level=4 ^
  --tf accept-ways ^
  --tf accept-nodes ^
  --used-ways ^
  --used-node ^
  --write-pbf omitmetadata=true file=&quot;D:/GIS Data/Tijdelijk/provinciestestosmosis.osm.pbf&quot;</code></pre>
<p>However this yields an enormous result (700 MB PBF file), including far more data then is neccessary for the selected relations. Can someone please elaborate on how to exactly read the Osmosis queries and show an example of what is the correct query (relations:admin_level=4 including depending sub-relations, ways and nods)?</p>
<p>BTW: This question is related to my question about <a href="/questions/47932/filters-in-osmfilter-a-lot-of-unwanted-data">Osmfilter</a>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '16, 02:43</strong></p>
<img src="https://secure.gravatar.com/avatar/b7a71ee7c9bc8c574ea76486008dea16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steijn&#39;s gravatar image" />
<p><span>Steijn</span><br />
<span class="score" title="61 reputation points">61</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steijn has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '16, 03:40</strong> </span></p>
</div>
</div>
<div id="comments-container-47931" class="comments-container">
<span id="47965"></span>
<div id="comment-47965" class="comment">
<div id="post-47965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did run another query:</p>
<pre><code>osmosis ^
  --read-pbf-fast workers=2 &quot;D:/GIS Data/Data/netherlands-latest.osm.pbf&quot; ^
  --tf accept-relations boundary=administrative ^
  --tf accept-relations admin_level=4 ^
  --used-way ^
  --used-node ^
  --write-pbf omitmetadata=true file=&quot;D:/GIS Data/Tijdelijk/provinciestestosmosis.osm.pbf&quot;</code></pre>
<p>This again results in a very large PBF file (700 MB PBF file), clearly contains far more data than needed. :(</p>
</div>
<div id="comment-47965-info" class="comment-info">
<span class="comment-age">(05 Feb '16, 21:52)</span> <span class="comment-user userinfo">Steijn</span>
</div>
</div>
<span id="47972"></span>
<div id="comment-47972" class="comment">
<div id="post-47972-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: please could you add this as a "new comment" instead if it is no "answer" to the original question? :-) Or edit your original question text and add it there.</p>
</div>
<div id="comment-47972-info" class="comment-info">
<span class="comment-age">(06 Feb '16, 10:21)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="47973"></span>
<div id="comment-47973" class="comment">
<div id="post-47973-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Conversion from answer to comment done.</p>
<p>@Stejin: we are happy when you pay attention to this hint from aseerel4c26.</p>
</div>
<div id="comment-47973-info" class="comment-info">
<span class="comment-age">(06 Feb '16, 10:49)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-47931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47931-form-container" class="comment-form-container">
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

<span id="47969"></span>

<div id="answer-container-47969" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47969-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The following works correct. First filter the relations (step 1), then filter the ways (step 2) en then filter the nodes (step 3). I must say, Osmosis is not a very straight forward tool to use.</p>
<p>Step 1:</p>
<pre><code>osmosis ^
  --read-pbf-fast workers=2 &quot;D:/GIS Data/Tijdelijk/netherlands-latest.osm.pbf&quot; ^
  --tf accept-relations boundary=administrative ^
  --tf accept-relations admin_level=4 ^
  --write-pbf file=&quot;D:/GIS Data/Tijdelijk/step1.osm.pbf&quot;</code></pre>
<p>Step 2:</p>
<pre><code>osmosis ^
  --read-pbf-fast workers=2 &quot;D:/GIS Data/Tijdelijk/step1.osm.pbf&quot; ^
  --used-way ^
  --write-pbf file=&quot;D:/GIS Data/Tijdelijk/step2.osm.pbf&quot;</code></pre>
<p>Step 3:</p>
<pre><code>osmosis ^
  --read-pbf-fast workers=2 &quot;D:/GIS Data/Tijdelijk/step2.osm.pbf&quot; ^
  --used-node ^
  --write-pbf file=&quot;D:/GIS Data/Tijdelijk/step3.osm.pbf&quot;</code></pre>
<p>Are there any suggestions on how to improve the rather tedious method? :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '16, 00:21</strong></p>
<img src="https://secure.gravatar.com/avatar/b7a71ee7c9bc8c574ea76486008dea16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steijn&#39;s gravatar image" />
<p><span>Steijn</span><br />
<span class="score" title="61 reputation points">61</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steijn has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '16, 00:22</strong> </span></p>
</div>
</div>
<div id="comments-container-47969" class="comments-container">
&#10;</div>
<div id="comment-tools-47969" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47969-form-container" class="comment-form-container">
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

