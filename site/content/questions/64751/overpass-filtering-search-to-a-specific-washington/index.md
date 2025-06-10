+++
type = "question"
title = "Overpass: Filtering search to a specific Washington"
description = '''in the US, there are 88 cities named &quot;Washington&quot;. I want to search for bike lanes within a specific Washington by specifying a state and country. This works and returns bike paths for ALL areas named Washington [out:json][timeout:25]; (  area[name=&quot;Washington&quot;];  way(area)[highway=&quot;cycleway&quot;];  ); ...'''
date = "2018-07-16T18:47:00Z"
lastmod = "2018-07-18T02:03:00Z"
weight = 64751
keywords = [ "overpass", "city", "area" ]
aliases = [ "/questions/64751" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: Filtering search to a specific Washington](/questions/64751/overpass-filtering-search-to-a-specific-washington)

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
<span id="post-64751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64751-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>in the US, there are 88 cities named "Washington".</p>
<p>I want to search for bike lanes within a specific Washington by specifying a state and country.</p>
<p>This works and returns bike paths for ALL areas named Washington</p>
<pre><code>[out:json][timeout:25];
(
  area[name=&quot;Washington&quot;];
  way(area)[highway=&quot;cycleway&quot;];
 );
&#10;  (._;&gt;;);
  out;</code></pre>
<p><strong>BUT this does not . It returns BLANK.</strong></p>
<pre><code>[out:json][timeout:25];
(
  area[name=&quot;Washington, MO, USA&quot;];
  way(area)[highway=&quot;cycleway&quot;];
 );
&#10;  (._;&gt;;);</code></pre>
<p>out; why does the area [name=""] not support NOMINATUM convention?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '18, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/cbff45c3fef0138cd67bbb0a2866e11b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Varun-ARGO&#39;s gravatar image" />
<p><span>Varun-ARGO</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Varun-ARGO has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '18, 19:17</strong> </span></p>
</div>
</div>
<div id="comments-container-64751" class="comments-container">
<span id="64752"></span>
<div id="comment-64752" class="comment">
<div id="post-64752-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As far as I can tell, there isn't a town/city in Washington state called "Washington", so it makes sense that nothing is returned.</p>
</div>
<div id="comment-64752-info" class="comment-info">
<span class="comment-age">(16 Jul '18, 19:08)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="64753"></span>
<div id="comment-64753" class="comment">
<div id="post-64753-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which Nominatim convention? Querying Nominatim for "Washington, WA, USA" finds all kinds of roads, cities and counties.</p>
</div>
<div id="comment-64753-info" class="comment-info">
<span class="comment-age">(16 Jul '18, 19:15)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="64754"></span>
<div id="comment-64754" class="comment">
<div id="post-64754-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try Boulder</p>
<p>if area[name="Boulder"]; you get results/</p>
<p>area[name="Boulder, CO, USA"]; you get BLANK</p>
</div>
<div id="comment-64754-info" class="comment-info">
<span class="comment-age">(16 Jul '18, 19:18)</span> <span class="comment-user userinfo">Varun-ARGO</span>
</div>
</div>
<span id="64765"></span>
<div id="comment-64765" class="comment">
<div id="post-64765-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you try to perform that query on the OSM website, you will understand why.</p>
</div>
<div id="comment-64765-info" class="comment-info">
<span class="comment-age">(17 Jul '18, 17:26)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="64766"></span>
<div id="comment-64766" class="comment">
<div id="post-64766-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you please elaborate?</p>
</div>
<div id="comment-64766-info" class="comment-info">
<span class="comment-age">(17 Jul '18, 17:27)</span> <span class="comment-user userinfo">Varun-ARGO</span>
</div>
</div>
<span id="64770"></span>
<div id="comment-64770" class="comment not_top_scorer">
<div id="post-64770-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try <a href="https://www.openstreetmap.org/search?query=Boulder%2CCO%2CUSA">https://www.openstreetmap.org/search?query=Boulder%2CCO%2CUSA</a></p>
</div>
<div id="comment-64770-info" class="comment-info">
<span class="comment-age">(17 Jul '18, 17:56)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
</div>
<div id="comment-tools-64751" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-64751-form-container" class="comment-form-container">
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

<span id="64755"></span>

<div id="answer-container-64755" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64755-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://nominatim.openstreetmap.org/search.php?q=Washington+franklin+county+Missouri&amp;polygon_geojson=1&amp;viewbox=">Washington franklin county Missouri</a> should work.</p>
<p>The blank results are when nominatim returns something that isn't searchable as an area or returns an area that doesn't have any of what you are trying to find. I don't have an explanation for the result that it returns for <a href="https://nominatim.openstreetmap.org/search.php?q=Washington%2C+MO%2C+USA&amp;polygon_geojson=1&amp;viewbox=">Washington, MO, USA</a>, but it is clear enough why Overpass API doesn't find anything there.</p>
<p>An alternative is to <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29">query by the relation id</a>, along with an offset, like:</p>
<pre><code>area(3600141263);</code></pre>
<p>(read the whole section for the info about the 3600)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '18, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-64755" class="comments-container">
<span id="64762"></span>
<div id="comment-64762" class="comment">
<div id="post-64762-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! Is there a way to retrieve relation id by city name?</p>
</div>
<div id="comment-64762-info" class="comment-info">
<span class="comment-age">(17 Jul '18, 14:06)</span> <span class="comment-user userinfo">Varun-ARGO</span>
</div>
</div>
<span id="64777"></span>
<div id="comment-64777" class="comment">
<div id="post-64777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I actually misread your question. On the Overpass-<em>Turbo</em> website there is a shortcut for looking up areas that uses Nominatim directly, <code>{{geocodeArea: Washington franklin county Missouri}};</code> Implementing something like that where the result from Nominatim is injected into the Overpass-API script, is a decent way to do the id lookups.</p>
<p>The alternative just using the Overpass-API is to first retrieve the state (or county) area and then restrict the query for the city to that state (use admin_level and name together), and then use the map_to_area statement to get an area.</p>
<p>The Overpass-API areas have the same tags as the OSM objects they are based on, that's why the Nominatim style lookups don't work, the area query will only return an exact match.</p>
</div>
<div id="comment-64777-info" class="comment-info">
<span class="comment-age">(18 Jul '18, 02:03)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-64755" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64755-form-container" class="comment-form-container">
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

