+++
type = "question"
title = "Download certain POIs for a whole country and transfer to Postgres-database"
description = '''Hello, I&#x27;d like to extract certain data from OSM for a whole country (Germany). The data I&#x27;d like to obtain are POI&#x27;s, but oviously not all of them.  I&#x27;d like to filter only the supermarkets for example and transfer them directly into a postgres database. So far I understood that I can archieve that...'''
date = "2019-11-08T15:11:00Z"
lastmod = "2019-11-14T19:01:00Z"
weight = 71541
keywords = [ "query", "overpass-turbo", "osm2pgsql", "osmosis", "postgres" ]
aliases = [ "/questions/71541" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Download certain POIs for a whole country and transfer to Postgres-database](/questions/71541/download-certain-pois-for-a-whole-country-and-transfer-to-postgres-database)

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
<span id="post-71541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71541-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'd like to extract certain data from OSM for a whole country (Germany). The data I'd like to obtain are POI's, but oviously not all of them. I'd like to filter only the supermarkets for example and transfer them directly into a postgres database.</p>
<p>So far I understood that I can archieve that for example with the Overpass api (via Overpass turbo). I already tried two options:</p>
<ul>
<li><strong>Overpass-Turbo (browser-based)</strong></li>
<li><strong>QuickOSM-Plugin for QGIS</strong></li>
</ul>
<p>In Overpass Turbo I filtered through the query-wizard I the POIs (shop=supermarket) and set a bounding box fitting germany inside. It worked only once though (when i chosed only nodes and due to access limitations...), but I got also POIS around Germany (as the bbox doesn't match with the country border). Therfore I tried to use the area-tags (<strong>addr:country=DE</strong>) to filter only supermarkets in Germany. But then some Points where left out because missing country-tags... anyways when chosing nodes, relations and ways, the query collapses after timeout.</p>
<p>The I tried the QuickOSM-Plugin for QGIS using the area-code (<strong>3600051477</strong>) to filter only the supermarkets inside Germany. Same thing – the area seems too big to rum the query successfully. After 180 seconds (max. timeout I guess…) the query aborts. Therefore I tried the same query with sub-regions (like German provinces, for e.g. Berlin, Bayern, etc.) and it worked.</p>
<p>I mean I could do several queries for each province in a row to fetch the data and merge it after all together, but there should be a more convinient way.</p>
<p>I downloaded the <strong>germany osm.pbf</strong> file from <strong>Geofrabrik</strong> and transfered it with <strong>osm2pgsql</strong> into my postgres database. Its a huge file (3 GB- takes a lot of disk-space!) and needed several hours to transfer (even with cached 16 GB ram…) and I have now loads of data in my database, which I actually dont need. Alltogether not the most satifiying solution as well.</p>
<p>I heard that I could prefilter the .osm data with <strong>osmosis</strong> before transfering it with osm2pgsql right?</p>
<p>But my question is:</p>
<p>Do I really have to download the whole dataset .osm.pbf, filter it with <strong>osmosis</strong> and transfer it with <strong>osm2pgsql</strong>?</p>
<p>Or is there any other solution regarding <strong>overpass</strong> that I dont know about?</p>
<p>It would be so much more efficient to download only the data I actually need!</p>
<p>Thanks in advance for any suggestions!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '19, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/79075c02f75a547c7bee9dc19f57d9a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pippo87&#39;s gravatar image" />
<p><span>Pippo87</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pippo87 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Nov '19, 15:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span></p>
</div>
</div>
<div id="comments-container-71541" class="comments-container">
&#10;</div>
<div id="comment-tools-71541" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71541-form-container" class="comment-form-container">
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

<span id="71622"></span>

<div id="answer-container-71622" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71622-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Do I really have to download the whole dataset .osm.pbf, filter it with osmosis and transfer it with osm2pgsql?</p>
</blockquote>
<p>No. For example you could pay somebody or a company to extract the data that you need for you (given that we are only talking about Germany I don't quite see where the pain is supposed to be, but OK). If it makes sense to import the data with osm2pgsql depends on what you actually want to do with the resulting data, which is what you don't mention. In any case you should think about if you actually need the original data, which will include polygons for those POIs that are mapped as areas, or if gettign everything as points would be better.</p>
<blockquote>
<p>Or is there any other solution regarding overpass that I dont know about?</p>
</blockquote>
<p>Probably not, the overpass servers are a shared, volunteer run resource that can't simply cater for everything people would like to do.</p>
<blockquote>
<p>It would be so much more efficient to download only the data I actually need!</p>
</blockquote>
<p>TANSTAAFL</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '19, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '19, 23:14</strong> </span></p>
</div>
</div>
<div id="comments-container-71622" class="comments-container">
<span id="71631"></span>
<div id="comment-71631" class="comment">
<div id="post-71631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Points would be better. Polygons are not needed, as I would use the locations in the database for further map productions later on.</p>
</div>
<div id="comment-71631-info" class="comment-info">
<span class="comment-age">(14 Nov '19, 13:56)</span> <span class="comment-user userinfo">Pippo87</span>
</div>
</div>
</div>
<div id="comment-tools-71622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71622-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71626"></span>

<div id="answer-container-71626" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71626-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please set a manual timeout. An example:</p>
<pre><code>[timeout:900];
area[name=&quot;Deutschland&quot;];
nwr[shop=supermarket](area);
out center;</code></pre>
<p>Please do not download through Overpass Turbo, because displaying in the browser is not designed for large queries. Use <a href="https://dev.overpass-api.de/overpass-doc/en/full_data/area.html#full">wget or curl</a> instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '19, 04:24</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-71626" class="comments-container">
<span id="71632"></span>
<div id="comment-71632" class="comment">
<div id="post-71632-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thx! I will try that. But as a newbie in that field, as far as I understood, to use overpass-api I'd have to download a clone of the overpass database (the whole planet-file?) and start queries from there? (As it is described here: <a href="https://dev.overpass-api.de/no_frills.html#startup)">https://dev.overpass-api.de/no_frills.html#startup)</a> Then again, I'd download mostly unneccessary data then...</p>
</div>
<div id="comment-71632-info" class="comment-info">
<span class="comment-age">(14 Nov '19, 14:04)</span> <span class="comment-user userinfo">Pippo87</span>
</div>
</div>
<span id="71637"></span>
<div id="comment-71637" class="comment">
<div id="post-71637-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can just use the public instance. It is well within reasonable limits.</p>
</div>
<div id="comment-71637-info" class="comment-info">
<span class="comment-age">(14 Nov '19, 19:01)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-71626" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71626-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71629"></span>

<div id="answer-container-71629" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71629-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With the Germany pbf file you can quickly filter out supermarkets using osmfilter. Furthermore you can convert areas to centroids using osmconvert if it suits.</p>
<p>As Roland says do not use Overpass-turbo for large queries. You can export your query in a form suitable for use directly with the overpass-api through the command line.</p>
<p>In both cases you probably need to import data to PostGiS using osm2pgsql because areas are not returned from the overpass-api.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '19, 11:33</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-71629" class="comments-container">
<span id="71633"></span>
<div id="comment-71633" class="comment">
<div id="post-71633-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Whats the difference betwenn osmfilter and osmosis?</p>
</div>
<div id="comment-71633-info" class="comment-info">
<span class="comment-age">(14 Nov '19, 14:07)</span> <span class="comment-user userinfo">Pippo87</span>
</div>
</div>
<span id="71635"></span>
<div id="comment-71635" class="comment">
<div id="post-71635-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osmconvert is closer to osmosis, osmfilter is for filtering (a bit like tag-filter). They are simpler to run (single executables, no dependencies), they use a proprietary format (o5m) for some actions, and are not as flexible as osmosis. However, their greater simplicity makes them highly suitable for the type of task you describe.</p>
</div>
<div id="comment-71635-info" class="comment-info">
<span class="comment-age">(14 Nov '19, 14:26)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71629" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71629-form-container" class="comment-form-container">
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

