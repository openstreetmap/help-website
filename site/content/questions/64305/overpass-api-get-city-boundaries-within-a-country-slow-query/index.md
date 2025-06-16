+++
type = "question"
title = "Overpass API: Get city boundaries within a country - slow query!"
description = '''I want to get the city boundaries within a specific country. The following query is fast but it&#x27;s not bound to a country so that multiple city boundaries could be returned. [out:json];(rel[name=&#x27;Herne&#x27;][type=boundary];);out geom;  I tried this query but it&#x27;s extremely slow: ( area[&quot;ISO3166-1:alpha2&quot;...'''
date = "2018-06-21T14:41:00Z"
lastmod = "2019-08-08T00:20:00Z"
weight = 64305
keywords = [ "openstreetmap", "overpass", "overpass-turbo" ]
aliases = [ "/questions/64305" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: Get city boundaries within a country - slow query!](/questions/64305/overpass-api-get-city-boundaries-within-a-country-slow-query)

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
<span id="post-64305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64305-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get the city boundaries within a specific country. The following query is fast but it's not bound to a country so that multiple city boundaries could be returned.</p>
<pre><code>[out:json];(rel[name=&#39;Herne&#39;][type=boundary];);out geom;</code></pre>
<p>I tried this query but it's extremely slow:</p>
<pre><code>( area[&quot;ISO3166-1:alpha2&quot;=&quot;DE&quot;];) -&gt;.a;
rel[name=&quot;Herne&quot;]
(area.a);
(._;&gt;;);
out geom;</code></pre>
<p>Is there a better and faster solution?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '18, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/ee7b89e8765c04ab68ce284a9efb18ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OsmStorm&#39;s gravatar image" />
<p><span>OsmStorm</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OsmStorm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64305" class="comments-container">
<span id="64319"></span>
<div id="comment-64319" class="comment">
<div id="post-64319-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>crosspost: <a href="https://stackoverflow.com/questions/50967088/osm-overpass-api-get-city-boundaries-from-country-rate-limit">https://stackoverflow.com/questions/50967088/osm-overpass-api-get-city-boundaries-from-country-rate-limit</a></p>
</div>
<div id="comment-64319-info" class="comment-info">
<span class="comment-age">(22 Jun '18, 10:15)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64305-form-container" class="comment-form-container">
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

<span id="64332"></span>

<div id="answer-container-64332" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64332-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've tried myself your slow query and it took me 90 seconds. Bear in mind that it hasn't the filter <code>[type="boundary"]</code>.</p>
<p>This one takes about 50 seconds, and does the same (it includes the <code>[type="boundary"]</code> filter):</p>
<pre><code>[out:json];
relation[name=&quot;Herne&quot;][type=&quot;boundary&quot;](area:3600051477);
out geom;</code></pre>
<p>From my experience so far with Overpass, it takes normally a similar time for queries over a country of the size of Germany. But maybe somebody has a faster solution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '18, 17:23</strong></p>
<img src="https://secure.gravatar.com/avatar/d45c161edd4b471fd947a7ec574274ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edvac&#39;s gravatar image" />
<p><span>edvac</span><br />
<span class="score" title="665 reputation points">665</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edvac has 4 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-64332" class="comments-container">
<span id="64371"></span>
<div id="comment-64371" class="comment">
<div id="post-64371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer! But why is this query so much slower than the first one? The first one takes like 1-2 seconds compared to 50/90 seconds. I guess it would be faster to take one coordinate per polygon (city) and check via another query if it's inside the given country or not. If someone finds a faster query or any other faster solution, please let me know.</p>
</div>
<div id="comment-64371-info" class="comment-info">
<span class="comment-age">(26 Jun '18, 07:06)</span> <span class="comment-user userinfo">OsmStorm</span>
</div>
</div>
</div>
<div id="comment-tools-64332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64332-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64372"></span>

<div id="answer-container-64372" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64372-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Is there maybe a way to detect which polygon belongs to which country by only going through the osm or geojson print? Maybe by help of the tags?</p>
<p>Herne Germany:</p>
<pre><code> &quot;tags&quot;: {
    &quot;TMC:cid_58:tabcd_1:Class&quot;: &quot;Area&quot;,
    &quot;TMC:cid_58:tabcd_1:LCLversion&quot;: &quot;8.00&quot;,
    &quot;TMC:cid_58:tabcd_1:LocationCode&quot;: &quot;463&quot;,
    &quot;admin_level&quot;: &quot;6&quot;,
    &quot;boundary&quot;: &quot;administrative&quot;,
    &quot;de:amtlicher_gemeindeschluessel&quot;: &quot;05916000&quot;,
    &quot;de:place&quot;: &quot;city&quot;,
    &quot;de:regionalschluessel&quot;: &quot;059160000000&quot;,
    &quot;name&quot;: &quot;Herne&quot;,
    &quot;name:prefix&quot;: &quot;Stadt&quot;,
    &quot;source&quot;: &quot;https://wiki.openstreetmap.org/wiki/Import/Catalogue/Kreisgrenzen_Deutschland_2005&quot;,
    &quot;type&quot;: &quot;boundary&quot;,
    &quot;wikidata&quot;: &quot;Q2904&quot;,
    &quot;wikipedia&quot;: &quot;de:Herne&quot;
  }</code></pre>
<p>Herne Belgium:</p>
<pre><code>&quot;tags&quot;: {
&quot;admin_level&quot;: &quot;8&quot;,
&quot;boundary&quot;: &quot;administrative&quot;,
&quot;name&quot;: &quot;Herne&quot;,
&quot;name:ru&quot;: &quot;Херне&quot;,
&quot;ref:INS&quot;: &quot;23032&quot;,
&quot;type&quot;: &quot;boundary&quot;,
&quot;website&quot;: &quot;http://www.herne.be&quot;,
&quot;wikidata&quot;: &quot;Q567808&quot;,
&quot;wikipedia&quot;: &quot;nl:Herne (België)&quot;</code></pre>
<p>}</p>
<p>But here, I could only take the wikipedia entry and decide by the prefix "de" / "nl" whereas "nl" would be wrong if I was looking for a Herne in the Netherlands.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '18, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ee7b89e8765c04ab68ce284a9efb18ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OsmStorm&#39;s gravatar image" />
<p><span>OsmStorm</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OsmStorm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64372" class="comments-container">
&#10;</div>
<div id="comment-tools-64372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64372-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70342"></span>

<div id="answer-container-70342" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70342-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This should do it:</p>
<pre><code>[out:json];
area[&#39;admin_level&#39;=&#39;2&#39;][&#39;name&#39;=&#39;Deutschland&#39;];
(relation[&#39;admin_level&#39;=&#39;8&#39;](area););
out geom;</code></pre>
<p>My understanding is that this line limits the query to just Germany:</p>
<pre><code>area[&#39;admin_level&#39;=&#39;2&#39;][&#39;name&#39;=&#39;Deutschland&#39;];</code></pre>
<p>Then this line does the actual search of all cities within that area:</p>
<pre><code>(relation[&#39;admin_level&#39;=&#39;8&#39;](area););</code></pre>
<p>If it's still too slow, you could run multiple queries - one for each State (which exist at admin level 4), based on this example for Brandenburg:</p>
<pre><code>[out:json];
area[&#39;ISO3166-2&#39;~&#39;^DE&#39;][&#39;admin_level&#39;=&#39;4&#39;][&#39;name&#39;=&#39;Brandenburg&#39;];
(relation[&#39;admin_level&#39;=&#39;8&#39;](area););
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '19, 00:20</strong></p>
<img src="https://secure.gravatar.com/avatar/0ada7b97d85873855231744286452af4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesChevalier&#39;s gravatar image" />
<p><span>JamesChevalier</span><br />
<span class="score" title="151 reputation points">151</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesChevalier has one accepted answer">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Aug '19, 00:21</strong> </span></p>
</div>
</div>
<div id="comments-container-70342" class="comments-container">
&#10;</div>
<div id="comment-tools-70342" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70342-form-container" class="comment-form-container">
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

