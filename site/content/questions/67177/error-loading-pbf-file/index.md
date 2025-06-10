+++
type = "question"
title = "Error loading pbf file"
description = '''I&#x27;m loading data into a Postgresql 9.5 over Ubuntu 16.04 but I having some issue with some pbf files, like &quot;argentina-latest.osm.pbf&quot; or &quot;south-america-latest.osm.pbf&quot;, but no problem with &quot;uruguay-latest.osm.pbf&quot; or &quot;venezuela-latest.osm.pbf&quot; Server: 12GB RAM 16 cores I have tried with different va...'''
date = "2018-12-13T21:29:00Z"
lastmod = "2018-12-14T08:47:00Z"
weight = 67177
keywords = [ "load", "pbf", "error" ]
aliases = [ "/questions/67177" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error loading pbf file](/questions/67177/error-loading-pbf-file)

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
<span id="post-67177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67177-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm loading data into a Postgresql 9.5 over Ubuntu 16.04 but I having some issue with some pbf files, like "argentina-latest.osm.pbf" or "south-america-latest.osm.pbf", but no problem with "uruguay-latest.osm.pbf" or "venezuela-latest.osm.pbf"</p>
<p>Server: 12GB RAM 16 cores</p>
<p>I have tried with different values for -C osm2pgsql parameter but the result is always the same.</p>
<p>Into line 4390 of /home/platform/src/SomeoneElse-style/style.lua file we can see: keyvalues["name"] = keyvalues["name"] .. " (" .. keyvalues["iata"] .. ")"</p>
<p>May be invalid content of some pbf files ?</p>
<p>How I can avoid the "contatenate nil value" in such setence ?</p>
<p>osm2pgsql -d gis --create --slim -C 3500 --number-processes 12 -S ~/src/openstreetmap-carto-AJT/openstreetmap-carto.style --multi-geometry --tag-transform-script ~/src/SomeoneElse-style/style.lua ~/data/south-america-latest.osm.pbf</p>
<p>but some minutes after:</p>
<p>Using PBF parser. Processing: Node(10320k 94.7k/s) Way(0k 0.00k/s) Relation(0 0.00/s)node cache: stored: 10434925(100.00%), storage efficiency: 50.81% (dense blocks: 148, sparse nodes: 9661361), hit rate: -nan%</p>
<p>Osm2pgsql failed due to ERROR: Failed to execute lua function for basic tag processing: /home/platform/src/SomeoneElse-style/style.lua:4390: attempt to concatenate field 'name' (a nil value)</p>
<p>Could you give me any clue? Thanks, Alberto Butrico</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-load" rel="tag" title="see questions tagged &#39;load&#39;">load</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '18, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/e8ae33b5c6317603b844713fc3d8cf79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abutrico&#39;s gravatar image" />
<p><span>abutrico</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abutrico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67177" class="comments-container">
<span id="67178"></span>
<div id="comment-67178" class="comment">
<div id="post-67178-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unlikely to be a problem with the data, more likely to be a bug in the map style. Maybe it is assuming that all airports with iata codes have names and there is one in your data that does not?</p>
</div>
<div id="comment-67178-info" class="comment-info">
<span class="comment-age">(13 Dec '18, 21:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67177-form-container" class="comment-form-container">
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

<span id="67183"></span>

<div id="answer-container-67183" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67183-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try it again. I've fixed it <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/commit/cf99c4eaa9f509d607d4440e392d47ff93caeae7">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '18, 08:47</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-67183" class="comments-container">
&#10;</div>
<div id="comment-tools-67183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67183-form-container" class="comment-form-container">
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

