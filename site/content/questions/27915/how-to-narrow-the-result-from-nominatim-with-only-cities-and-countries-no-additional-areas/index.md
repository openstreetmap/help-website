+++
type = "question"
title = "How to narrow the result from Nominatim with only cities and countries, no additional areas?"
description = '''I&#x27;m trying to get WKT polygons of cities and countries from Nominatim (for example, Paris and France). I send a GET request but it returns me several results named &quot;Paris&quot;. How may I narrow results only to the capital. Here&#x27;s my request url: http://nominatim.openstreetmap.org/search/fr/paris?format=...'''
date = "2013-11-08T16:10:00Z"
lastmod = "2022-09-16T05:22:00Z"
weight = 27915
keywords = [ "nominatim" ]
aliases = [ "/questions/27915" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to narrow the result from Nominatim with only cities and countries, no additional areas?](/questions/27915/how-to-narrow-the-result-from-nominatim-with-only-cities-and-countries-no-additional-areas)

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
<span id="post-27915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27915-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to get WKT polygons of cities and countries from Nominatim (for example, Paris and France). I send a GET request but it returns me several results named "Paris". How may I narrow results only to the capital. Here's my request url:</p>
<p><strong><a href="http://nominatim.openstreetmap.org/search/fr/paris?format=json&amp;polygon_geojson=1">http://nominatim.openstreetmap.org/search/fr/paris?format=json&amp;polygon_geojson=1</a></strong></p>
<p>And I get an array of 10 objects, only one is the capital,</p>
<pre><code>class: &quot;boundary&quot;, type: &quot;administrative&quot;.</code></pre>
<p>The rest are:</p>
<pre><code>class: &quot;place&quot;, type: &quot;isolated_dwelling&quot;
class: &quot;place&quot;, type: &quot;hamlet&quot;,
class: &quot;place&quot;, type: &quot;neighbourhood&quot;
and so on...</code></pre>
<p>How to select only the desired city and only the desired country ignoring rest of results?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '13, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/94e9da2e1e68f09a40814281943f9ebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="green10701&#39;s gravatar image" />
<p><span>green10701</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="green10701 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27915" class="comments-container">
&#10;</div>
<div id="comment-tools-27915" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27915-form-container" class="comment-form-container">
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

<span id="27938"></span>

<div id="answer-container-27938" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27938-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's probably no guaranteed way to do this but several things that can help:</p>
<ul>
<li>Limit the number of results to one by adding &amp;limit=1 <a href="http://nominatim.openstreetmap.org/search/fr/paris?format=json&amp;limit=1">(example)</a></li>
<li>Request only certain feature types by adding &amp;featuretype=city <a href="http://nominatim.openstreetmap.org/search/fr/paris?format=json&amp;featuretype=city">(example)</a></li>
<li>Request only cities named "Paris" in a country named "France" by using as structured query: search?city=Paris <a href="http://nominatim.openstreetmap.org/search?format=json&amp;city=Paris&amp;country=France">(example)</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Nov '13, 15:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Nov '13, 15:03</strong> </span></p>
</div>
</div>
<div id="comments-container-27938" class="comments-container">
<span id="85635"></span>
<div id="comment-85635" class="comment">
<div id="post-85635-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Apparently the <code>featuretype</code> parameter was removed <a href="https://github.com/osm-search/Nominatim/issues/1938">https://github.com/osm-search/Nominatim/issues/1938</a></p>
</div>
<div id="comment-85635-info" class="comment-info">
<span class="comment-age">(16 Sep '22, 05:22)</span> <span class="comment-user userinfo">cyberixae</span>
</div>
</div>
</div>
<div id="comment-tools-27938" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27938-form-container" class="comment-form-container">
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

