+++
type = "question"
title = "Best way to get coordinates of each node of a way?"
description = '''I&#x27;m am on a project that would like to obtain the GPS boundaries of objects/locations of interest in JSON format. We have found it possible to make a single API call to http://overpass-api.de/api/interpreter? to get a list of ways with node ID&#x27;s. We then found that we could traverse the list and mak...'''
date = "2021-01-27T01:34:00Z"
lastmod = "2021-02-19T07:00:00Z"
weight = 78529
keywords = [ "overpassapi", "json" ]
aliases = [ "/questions/78529" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Best way to get coordinates of each node of a way?](/questions/78529/best-way-to-get-coordinates-of-each-node-of-a-way)

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
<span id="post-78529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78529-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm am on a project that would like to obtain the GPS boundaries of objects/locations of interest in JSON format. We have found it possible to make a single API call to <a href="http://overpass-api.de/api/interpreter?">http://overpass-api.de/api/interpreter?</a> to get a list of ways with node ID's. We then found that we could traverse the list and make another API call to <a href="https://api.openstreetmap.org/api/0.6/node/%7BnodeID%7D.json">https://api.openstreetmap.org/api/0.6/node/{nodeID}.json</a> to obtain the individual node coordinates. Is there a more efficient process in retrieving this information as some ways could have up to 2000 nodes? Thanks for the information in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '21, 01:34</strong></p>
<img src="https://secure.gravatar.com/avatar/6852f410a2e019b46c2819a40e852ca9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nonProfitDeveloper&#39;s gravatar image" />
<p><span>nonProfitDev...</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nonProfitDeveloper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78529" class="comments-container">
&#10;</div>
<div id="comment-tools-78529" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78529-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="78530"></span>

<div id="answer-container-78530" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78530-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nonProfitDeveloper has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass-API has functionality to retrieve the nodes: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_down_.28.3E.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_down_.28.3E.29</a></p>
<p>Typically you'd do something like</p>
<pre><code>(way[...];
&gt;;
);
out;</code></pre>
<p>where the <code>way[...];</code> is what you are doing to find the ways, and then <code>&gt;;</code> adds the results to the union.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '21, 02:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-78530" class="comments-container">
<span id="78933"></span>
<div id="comment-78933" class="comment">
<div id="post-78933-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, I was not aware of the recurse down feature.</p>
</div>
<div id="comment-78933-info" class="comment-info">
<span class="comment-age">(19 Feb '21, 02:57)</span> <span class="comment-user userinfo">nonProfitDev...</span>
</div>
</div>
<span id="78935"></span>
<div id="comment-78935" class="comment">
<div id="post-78935-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you looked at my answer, which shows better ways to get just the coordinates, if you're not interested in the node objects?</p>
</div>
<div id="comment-78935-info" class="comment-info">
<span class="comment-age">(19 Feb '21, 07:00)</span> <span class="comment-user userinfo">ikonor</span>
</div>
</div>
</div>
<div id="comment-tools-78530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78530-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78538"></span>

<div id="answer-container-78538" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78538-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can retrieve a way and all of its nodes directly from the OSM API:</p>
<p><a href="https://www.openstreetmap.org/api/0.6/way/1010/full">https://www.openstreetmap.org/api/0.6/way/1010/full</a></p>
<p>However keep in mind that this API is primarily for editing OSM data. Don't perform bulk requests against it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '21, 08:41</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78538" class="comments-container">
&#10;</div>
<div id="comment-tools-78538" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78538-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78582"></span>

<div id="answer-container-78582" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78582-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78582-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78582-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Beside recurse down (&gt;), Overpass API offers additional options to resolve the node references of a way and to get the coordinates of the nodes:</p>
<h3 id="out-geom">out geom</h3>
<p>Using <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#out"><code>out geom</code></a> output:</p>
<pre><code>[out:json];
way(95777558);
out geom;</code></pre>
<ul>
<li><a href="https://overpass-turbo.eu/s/12Ty">https://overpass-turbo.eu/s/12Ty</a></li>
<li><a href="https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%0Away%2895777558%29%3B%0Aout%20geom%3B%0A">http://overpass-api.de/api/interpreter?data=...</a></li>
</ul>
<p>writes the node coordinates to an additional <code>geometry</code> property in the way object:</p>
<pre><code>&quot;geometry&quot;: [
  { &quot;lat&quot;: 44.4198143, &quot;lon&quot;: 38.2052864 },
  { &quot;lat&quot;: 44.4196878, &quot;lon&quot;: 38.2052733 },
  { &quot;lat&quot;: 44.4195565, &quot;lon&quot;: 38.2052576 }
],</code></pre>
<p>No need to include the full node objects in the result.</p>
<h3 id="geojson-format">GeoJSON format</h3>
<p>Using the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Geometry">Geometry operator</a> <code>geom()</code> in a <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#The_statement_convert"><code>convert</code> statement</a>:</p>
<pre><code>[out:json];
way(95777558);
convert item ::=::,::geom=geom(),_osm_type=type();
out geom;</code></pre>
<ul>
<li><a href="http://overpass-turbo.eu/s/12TN">http://overpass-turbo.eu/s/12TN</a> (GeoJSON map display not supported by Overpass Turbo)</li>
<li><a href="http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%0Away%2895777558%29%3B%0Aconvert%20item%20%3A%3A%3D%3A%3A%2C%3A%3Ageom%3Dgeom%28%29%2C_osm_type%3Dtype%28%29%3B%0Aout%20geom%3B%0A">http://overpass-api.de/api/interpreter?data=...</a></li>
</ul>
<p>converts the way object into a derived object with the given properties and writes the coordinates into the <code>geometry</code> property in the <a href="https://wikipedia.org/wiki/GeoJSON">GeoJSON</a> format:</p>
<pre><code>&quot;geometry&quot;: {
  &quot;type&quot;: &quot;LineString&quot;,
  &quot;coordinates&quot;: [
    [38.2052864, 44.4198143],
    [38.2052733, 44.4196878],
    [38.2052576, 44.4195565]
  ]
},</code></pre>
<p>See also:</p>
<ul>
<li><a href="https://dev.overpass-api.de/overpass-doc/en/targets/formats.html#json">Data Formats (Overpass API User's Manual)</a></li>
<li><a href="https://dev.overpass-api.de/blog/flat_world.html">Into a Flat World (Overpass API Blog)</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '21, 19:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f92748c8fa508a936bcf2169b30cabf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikonor&#39;s gravatar image" />
<p><span>ikonor</span><br />
<span class="score" title="1286 reputation points"><span>1.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikonor has 4 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '21, 20:05</strong> </span></p>
</div>
</div>
<div id="comments-container-78582" class="comments-container">
&#10;</div>
<div id="comment-tools-78582" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78582-form-container" class="comment-form-container">
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

