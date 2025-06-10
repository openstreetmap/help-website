+++
type = "question"
title = "How to edit a local pbf and update the source"
description = '''Hello all, I have a local OSRM server where I do some traffic simulations for studies, and I need to change some maxspeeds on the map. What I am trying to do:  Download a pbf from geofrabrik use osmosis to cut a small chunk where I want to edit.  -  edit the chunk with JOSM And now I am stucked on h...'''
date = "2021-04-27T19:52:00Z"
lastmod = "2021-04-28T18:18:00Z"
weight = 79884
keywords = [ "josm", "editing", "pbf", "osmosis" ]
aliases = [ "/questions/79884" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to edit a local pbf and update the source](/questions/79884/how-to-edit-a-local-pbf-and-update-the-source)

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
<span id="post-79884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79884-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,</p>
<p>I have a local OSRM server where I do some traffic simulations for studies, and I need to change some maxspeeds on the map.</p>
<p>What I am trying to do:</p>
<ul>
<li>Download a pbf from geofrabrik</li>
<li>use osmosis to cut a small chunk where I want to edit. -</li>
<li><p>edit the chunk with JOSM And now I am stucked on how I merge the edits with the original pbf. I tried use osmosis to calculate diff, but if I use:</p>
<p>osmosis --read-xml file="sudeste-latest-osm_02.osm" --read-pbf file="sudeste-latest.osm.pbf" --derive-change --write-xml-change file="changeset.osc"</p></li>
</ul>
<p>When I apply the diffs to the original "sudeste-latest" with:</p>
<pre><code>osmosis --read-xml-change file=&quot;changeset.osc&quot; --read-pbf file=&quot;sudeste-latest.osm.pbf&quot; --apply-change --write-pbf file=&quot;sudeste-new.osm.pbf&quot;</code></pre>
<p>The output file contains only the chunk that I updated.</p>
<p>If I calculated the diffs with:</p>
<pre><code>osmosis --read-pbf file=&quot;sudeste-latest.osm.pbf&quot; --read-xml file=&quot;sudeste-latest-osm_02.osm&quot; --derive-change --write-xml-change file=&quot;changeset.osc&quot;</code></pre>
<p>When I apply the osc, none of my changes was applied. What I'm doing wrong?</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '21, 19:52</strong></p>
<img src="https://secure.gravatar.com/avatar/885f4de5adc4d79a25587b89ec81f43e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rafaelricco&#39;s gravatar image" />
<p><span>rafaelricco</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rafaelricco has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Apr '21, 19:54</strong> </span></p>
</div>
</div>
<div id="comments-container-79884" class="comments-container">
&#10;</div>
<div id="comment-tools-79884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79884-form-container" class="comment-form-container">
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

<span id="79885"></span>

<div id="answer-container-79885" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79885-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Osmosis doesn't understand the JOSM xml file.</p>
<p>Osmium might work (I'm not sure): <a href="https://docs.osmcode.org/osmium/latest/osmium-apply-changes.html">https://docs.osmcode.org/osmium/latest/osmium-apply-changes.html</a></p>
<p>If you create objects, you might also have to synthesize positive ids for them to satisfy the OSRM importer (I don't know if it supports negative ids or not).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '21, 03:08</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-79885" class="comments-container">
<span id="79910"></span>
<div id="comment-79910" class="comment">
<div id="post-79910-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nice! I will give a try using Osmium!</p>
<p>Apparently, if instead of derive changes from the bigger pbf, I use the edited chunk against the non-edited chunk:</p>
<p>osmosis --read-xml file="sudeste-latest-osm_02_new.osm" --read-pbf file="sudeste-latest-osm_02_old.osm" --derive-change --write-xml-change file="changeset.osc"</p>
<p>Them the changeset was applied to the original pbf, but Osmium seems to me to be more cleaner, let see!</p>
<p>Thank you!</p>
</div>
<div id="comment-79910-info" class="comment-info">
<span class="comment-age">(28 Apr '21, 18:18)</span> <span class="comment-user userinfo">rafaelricco</span>
</div>
</div>
</div>
<div id="comment-tools-79885" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79885-form-container" class="comment-form-container">
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

