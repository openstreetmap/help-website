+++
type = "question"
title = "Overpass API: Fetch country regions where no subarea relation"
description = '''I have written a query to get a countries sub regions by first querying for the country relation, then recursing down, then filtering the relations by role=subarea, query: [out:json]; rel[&#x27;ISO3166-1&#x27;=&#x27;{countryCode}&#x27;]-&amp;gt;.c; .c &amp;gt;&amp;gt;; (rel(r:&#x27;subarea&#x27;);.c;)-&amp;gt;.a; .a out meta bb;  This query wor...'''
date = "2018-05-24T09:49:00Z"
lastmod = "2018-08-02T17:11:00Z"
weight = 63677
keywords = [ "overpass", "overpass-ql", "relations", "overpass-api", "country" ]
aliases = [ "/questions/63677" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: Fetch country regions where no subarea relation](/questions/63677/overpass-api-fetch-country-regions-where-no-subarea-relation)

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
<span id="post-63677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63677-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have written a query to get a countries sub regions by first querying for the country relation, then recursing down, then filtering the relations by <code>role=subarea</code>, query:</p>
<pre><code>[out:json];
rel[&#39;ISO3166-1&#39;=&#39;{countryCode}&#39;]-&gt;.c;
.c &gt;&gt;;
(rel(r:&#39;subarea&#39;);.c;)-&gt;.a;
.a out meta bb;</code></pre>
<p>This query works well for countries such as Spain (<code>{countryCode}=ES</code>) and Portugal (PT) and it is very easy to extract a hierarchy from output as relations have an id and members have a relation to the same id.</p>
<p>However, countries such as Croatia (HR) only return the country relation .c when this query is executed, inspection of the result shows that the Croatia relation has no member relations with the subarea role, and thus the recursion returns an empty set.</p>
<p>It is important to me that I am able to build a hierarchy from the results and I have not been able to create a query which returns a nations regions for a country such as Croatia where the country relation has no subareas.</p>
<p>I do not mind executing another query or going to another openstreetmap source if the first query should return only the country relation.</p>
<p>Do you know of any way to query Overpass to get a heirarchy of a countries sub regions when the relations members have no subarea role? Or another source for the information? Or some other way of achieving the same result?</p>
<p>Any help is greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '18, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/4145617372f958be0d7c4d5a5cea16e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dreggers&#39;s gravatar image" />
<p><span>dreggers</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dreggers has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63677" class="comments-container">
<span id="63720"></span>
<div id="comment-63720" class="comment">
<div id="post-63720-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crossposting: <a href="https://gis.stackexchange.com/questions/283925/overpass-api-fetch-country-regions-where-no-subarea-relation">https://gis.stackexchange.com/questions/283925/overpass-api-fetch-country-regions-where-no-subarea-relation</a></p>
</div>
<div id="comment-63720-info" class="comment-info">
<span class="comment-age">(24 May '18, 21:32)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-63677" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63677-form-container" class="comment-form-container">
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

<span id="63747"></span>

<div id="answer-container-63747" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63747-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://overpass-turbo.eu/s/z6n">Here's a query that fetches objects tagged with admin_level from a given country</a>:</p>
<pre><code>area[admin_level=2][int_name=Croatia]-&gt;.search;
(way(area.search)[admin_level=4];
 rel(area.search)[admin_level=4];
);
out center;</code></pre>
<p>Overpass-API creates the <code>area</code> features for use in queries by processing OpenStreetMap objects with tags that indicate they should be treated as an interesting area. There should be one for every administrative region in OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '18, 23:22</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-63747" class="comments-container">
<span id="65082"></span>
<div id="comment-65082" class="comment">
<div id="post-65082-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That was very helpful. Thank you very much!</p>
</div>
<div id="comment-65082-info" class="comment-info">
<span class="comment-age">(02 Aug '18, 17:11)</span> <span class="comment-user userinfo">rene78</span>
</div>
</div>
</div>
<div id="comment-tools-63747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63747-form-container" class="comment-form-container">
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

