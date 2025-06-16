+++
type = "question"
title = "OpenStreetMap Nominatim API limit parameter behaving erratically, returns inconsistent numbers of results"
description = '''I am trying to use the Nominatim API to geocode cities, with simple HTTP GET requests. I want to receive a specific number of possible matches, when available. The documentation indicates this is possible by using the &quot;limit&quot; parameter: limit=integer Limit the number of returned results.  This works...'''
date = "2016-09-28T06:03:00Z"
lastmod = "2016-10-06T18:48:00Z"
weight = 52260
keywords = [ "api", "url", "openstreetmap", "nominatim", "osm" ]
aliases = [ "/questions/52260" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OpenStreetMap Nominatim API limit parameter behaving erratically, returns inconsistent numbers of results](/questions/52260/openstreetmap-nominatim-api-limit-parameter-behaving-erratically-returns-inconsistent-numbers-of-results)

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
<span id="post-52260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52260-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to use the Nominatim API to geocode cities, with simple HTTP GET requests. I want to receive a specific number of possible matches, when available. The <a href="https://wiki.openstreetmap.org/wiki/Nominatim">documentation</a> indicates this is possible by using the "limit" parameter:</p>
<pre><code>limit=integer
Limit the number of returned results.</code></pre>
<p>This works as expected for most queries. For example, if I request <a href="https://nominatim.openstreetmap.org/search?format=json&amp;limit=2&amp;polygon_geojson=1&amp;country=Mexico&amp;city=Mexico">limit=2</a>, I get the top 2 results and if I request <a href="https://nominatim.openstreetmap.org/search?format=json&amp;limit=3&amp;polygon_geojson=1&amp;country=Mexico&amp;city=Mexico">limit=3</a>, I get the top 3 results. But the limit parameter behaves erratically for some queries. For example, with Sonoma California:</p>
<ul>
<li>If I request <a href="https://nominatim.openstreetmap.org/search?format=json&amp;limit=1&amp;polygon_geojson=1&amp;country=USA&amp;state=California&amp;city=Sonoma">limit=1</a>, I get 1 result</li>
<li>But if I request <a href="https://nominatim.openstreetmap.org/search?format=json&amp;limit=2&amp;polygon_geojson=1&amp;country=USA&amp;state=California&amp;city=Sonoma">limit=2</a>, I still get just 1 result</li>
<li>And if I request <a href="https://nominatim.openstreetmap.org/search?format=json&amp;limit=3&amp;polygon_geojson=1&amp;country=USA&amp;state=California&amp;city=Sonoma">limit=3</a>, I suddenly get 2 results</li>
</ul>
<p><strong>If 2 results are available when I request limit=3, why didn't I get 2 results when I requested limit=2?</strong></p>
<p>As another example, with Petaluma California:</p>
<ul>
<li>If I request <a href="https://nominatim.openstreetmap.org/search?format=json&amp;limit=1&amp;polygon_geojson=1&amp;country=USA&amp;state=California&amp;city=Petaluma">limit=1</a>, I get 1 result</li>
<li>But if I request <a href="https://nominatim.openstreetmap.org/search?format=json&amp;limit=2&amp;polygon_geojson=1&amp;country=USA&amp;state=California&amp;city=Petaluma">limit=2</a>, I still get just 1 result</li>
<li>And if I request <a href="https://nominatim.openstreetmap.org/search?format=json&amp;limit=3&amp;polygon_geojson=1&amp;country=USA&amp;state=California&amp;city=Petaluma">limit=3</a>, I get 3 results this time</li>
</ul>
<p><strong>Why am I inconsistently not receiving as many results as I am requesting, and how can I make sure to receive the exact number I request?</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Sep '16, 06:03</strong></p>
<img src="https://secure.gravatar.com/avatar/8eb28ad933ae655db57b6c6b8563eb67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gboeing&#39;s gravatar image" />
<p><span>gboeing</span><br />
<span class="score" title="136 reputation points">136</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gboeing has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52260" class="comments-container">
<span id="52288"></span>
<div id="comment-52288" class="comment">
<div id="post-52288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>cross-posted: <a href="https://gis.stackexchange.com/questions/212307/openstreetmap-nominatim-api-limit-parameter-behaving-erratically-returns-incons">https://gis.stackexchange.com/questions/212307/openstreetmap-nominatim-api-limit-parameter-behaving-erratically-returns-incons</a></p>
</div>
<div id="comment-52288-info" class="comment-info">
<span class="comment-age">(28 Sep '16, 19:04)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52260-form-container" class="comment-form-container">
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

<span id="52261"></span>

<div id="answer-container-52261" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52261-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gboeing has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sometimes you have several objects in OSM identifying the same place or object in reality. The simplest case is a street being split in many different OSM ways due to different characteristics. Nominatim will attempt to detect such duplicates and only return one match; this is controlled by the <code>dedupe</code> parameter which defaults to 1. Since the <code>limit</code> is, for reasons of efficiency, enforced before and not after de-duplicating, it is possible that de-duplicating leaves you with less results than requested.</p>
<p>In your "Sonoma" case, when limit=2 and dedupe=0 are set, Nominatim returns the ways 33162431 and 33162426 (it should return <a href="https://www.openstreetmap.org/relation/113172">https://www.openstreetmap.org/relation/113172</a> instead and I don't know why it doesn't).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '16, 07:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52261" class="comments-container">
<span id="52381"></span>
<div id="comment-52381" class="comment">
<div id="post-52381-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. Yes the dedupe parameter used in conjunction with the limit parameter does appear to give me the number of results I request, each time. However, like you mentioned in the last sentence that is an odd result.</p>
</div>
<div id="comment-52381-info" class="comment-info">
<span class="comment-age">(06 Oct '16, 18:48)</span> <span class="comment-user userinfo">gboeing</span>
</div>
</div>
</div>
<div id="comment-tools-52261" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52261-form-container" class="comment-form-container">
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

