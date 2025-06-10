+++
type = "question"
title = "Compare values with Overpass"
description = '''I&#x27;d like to find Objects where certain Keys have the same value. Irish streets normally have two names, one in Irish and one in English. In osm the have three tags for that, name, name:en and name:ga. I&#x27;d like to find all objects having all three tags where name doesn&#x27;t match with name:en or name:ga...'''
date = "2015-05-29T08:17:00Z"
lastmod = "2019-01-04T21:39:00Z"
weight = 43298
keywords = [ "overpass", "comparison" ]
aliases = [ "/questions/43298" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [Compare values with Overpass](/questions/43298/compare-values-with-overpass)

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
<span id="post-43298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43298-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to find Objects where certain Keys have the same value. Irish streets normally have two names, one in Irish and one in English. In osm the have three tags for that, name, name:en and name:ga. I'd like to find all objects having all three tags where name doesn't match with name:en or name:ga.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-comparison" rel="tag" title="see questions tagged &#39;comparison&#39;">comparison</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 May '15, 08:17</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-43298" class="comments-container">
&#10;</div>
<div id="comment-tools-43298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43298-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="43316"></span>

<div id="answer-container-43316" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43316-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ogmios has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's not possible with Overpass API today, but with a bit of post-processing you can get the results in a few minutes.</p>
<p>The Overpass QL query below returns relevant nodes/way/rel having a name, name:en and name:ga tag in CSV output format (tab separator character).</p>
<p>To get the data, just click on the following overpass turbo link: <a href="http://overpass-turbo.eu/s/9FN">http://overpass-turbo.eu/s/9FN</a> and then hit "Export" -&gt; "raw data directly from Overpass API". This should automatically open LibreOffice or Excel, depending on your local machine. When importing the CSV file, make sure to specify "tab" as separator character.</p>
<p>There are only 11120 rows returned by the query, about 300 of them match your search criterion. Just add a formula to all rows to compare different names and you're probably all set.</p>
<pre><code>[timeout:1800]
[bbox:51.08282186160976,-12.8759765625,55.986091533808384,-1.86767578125]
[out:csv(::id, ::type, name, &quot;name:en&quot;, &quot;name:ga&quot;)];
&#10;( node[name][&quot;name:en&quot;][&quot;name:ga&quot;];
  way[name][&quot;name:en&quot;][&quot;name:ga&quot;];
  rel[name][&quot;name:en&quot;][&quot;name:ga&quot;];
);
out;</code></pre>
<p>Overpass QL result in CSV format, as returned by Overpass API:</p>
<pre><code>@id @type   name    name:en name:ga
661291  node    Sutton  Sutton  Cill Fhionntain
661448  node    Killester   Killester   Cill Easra
661999  node    Glenageary  Glenageary  Gleann na Caorach
662088  node    Booterstown Booterstown Baile an Bhóthair
664528  node    Shankill    Shankill    Seanchill
665844  node    Cowper  Cowper  Cúipéar
666663  node    Milltown    Milltown    Baile An Mhuilinn
12646992    node    Carrickmines    Carrickmines    Carraig Mhaighin
12647002    node    Carrickmines    Carrickmines    Carraig Mhaighin
12647038    node    Cherrywood  Cherrywood  Coill na Silíní
19223931    node    Windy Arbour    Windy Arbour    Na Glasáin
26608599    node    Cork Airport    Cork Airport    Aerfort Chorcaí
26608601    node    Shannon Airport Shannon Airport Aerfort na Sionainne
28650950    node    Cooanmore Point Cooanmore Point Gob an Chuain Mhóir
28652693    node    Killaspug Point Killaspug Point Rinn Chill Easpaig
&#10;[...]</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '15, 16:53</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 May '15, 17:15</strong> </span></p>
</div>
</div>
<div id="comments-container-43316" class="comments-container">
&#10;</div>
<div id="comment-tools-43316" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43316-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43321"></span>

<div id="answer-container-43321" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43321-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-43321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass isn't the only tool out there. Here's an alternative :</p>
<ul>
<li>Install <a href="http://www.gaia-gis.it/gaia-sins/">spatialite</a> using your platform's prefered install method</li>
<li>download a <a href="http://download.geofabrik.de/europe/ireland-and-northern-ireland.html">country extract from geofabrik</a></li>
<li>import the extract into an sqlite db using spatialite "spatialite_osm_raw -o input.pbf -d output.sqlite -jo"</li>
<li>enter the database: "sqlite3 output.sqlite"</li>
<li>run this query: "select t1.way_id,t1.v,t2.v,t3.v from osm_way_tags t1 left join osm_way_tags t2 on (t1.way_id=t2.way_id) left join osm_way_tags t3 on (t1.way_id=t3.way_id) where t1.k='name' and t2.k='name:ga' and t3.k='name:en' and t1.v &lt;&gt; t2.v and t1.v &lt;&gt; t3.v;"</li>
</ul>
<p>This give a result like this:</p>
<pre><code>4934506|Suir Road Bridge|Bóthar na Siúire|Suir Road
4934592|Macartney Bridge|Sráid Bhagóid Íochtarach|Baggot Street Lower
4934663|Rialto Bridge|Cuarbóthar Theas|South Circular Road
13769663|School Lane|Ascaill Na gCrann|Trees Avenue
16315628|Trimleston Gardens|Gairdíní Baile Trimble|Trimbleston Garde</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '15, 18:21</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 May '15, 18:22</strong> </span></p>
</div>
</div>
<div id="comments-container-43321" class="comments-container">
<span id="43322"></span>
<div id="comment-43322" class="comment">
<div id="post-43322-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That looks good. I will definately try it. Thanks.</p>
</div>
<div id="comment-43322-info" class="comment-info">
<span class="comment-age">(29 May '15, 18:23)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
<span id="43338"></span>
<div id="comment-43338" class="comment">
<div id="post-43338-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Downloading an extract (100MB) and creating an sqlite db from it (= 2,x GB(!)) seems a bit heavy to me for 11000 relevant objects.</p>
<p>As an alternative to using a Geofabrik country extract, I'd really recommend to start with a small Overpass extract instead: <a href="http://overpass-turbo.eu/s/9FQ">http://overpass-turbo.eu/s/9FQ</a> -&gt; Export -&gt; raw data directly from Overpass API. The download will be around 12MB uncompressed OSM data (query takes about 1 minute), the resulting sqlite DB file size will be just 19MB.</p>
<p>Also, it would be good to have some sql statements for nodes and relations as well to make the example complete.</p>
</div>
<div id="comment-43338-info" class="comment-info">
<span class="comment-age">(31 May '15, 17:23)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="43340"></span>
<div id="comment-43340" class="comment">
<div id="post-43340-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Didn't have an estimate of the number of matches until you wrote your answer. Overpass and spatialite are both great tools with strenghts and weaknesses, it's good to know them both.</p>
</div>
<div id="comment-43340-info" class="comment-info">
<span class="comment-age">(31 May '15, 21:39)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="59356"></span>
<div id="comment-59356" class="comment">
<div id="post-59356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You don't have to install it now - just use the Wikidata+OSM sparql query - answer below :)</p>
</div>
<div id="comment-59356-info" class="comment-info">
<span class="comment-age">(06 Sep '17, 08:35)</span> <span class="comment-user userinfo">nyuriks</span>
</div>
</div>
</div>
<div id="comment-tools-43321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43321-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67452"></span>

<div id="answer-container-67452" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67452-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For those searching for a solution via internet search:</p>
<p>It's now possible within Overpass:</p>
<p><a href="http://overpass-turbo.eu/s/EYC">http://overpass-turbo.eu/s/EYC</a></p>
<pre><code>// return keys that don&#39;t have same values
[bbox:{{bbox}}];
nwr[highway=footway][name][&quot;name:en&quot;][&quot;name:ga&quot;]
(if: t[&quot;name&quot;] != t[&quot;name:en&quot;] &amp;&amp; t[&quot;name&quot;] != t[&quot;name:ga&quot;]); 
out geom;</code></pre>
<p>I'm sure it can be developed further.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '19, 21:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jan '19, 21:41</strong> </span></p>
</div>
</div>
<div id="comments-container-67452" class="comments-container">
&#10;</div>
<div id="comment-tools-67452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67452-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43310"></span>

<div id="answer-container-43310" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43310-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can't answer your query but are you aware that we have our own instance of overpass at <a href="http://overpass-turbo.openstreetmap.ie/">http://overpass-turbo.openstreetmap.ie/</a></p>
<p>There are some folks in the Irish chatroom who might be able to assist also</p>
<p><a href="http://wiki.openstreetmap.org/wiki/WikiProject_Ireland#Contacting_Irish_Mappers">http://wiki.openstreetmap.org/wiki/WikiProject_Ireland#Contacting_Irish_Mappers</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '15, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/9f0faef4659de616c82f448ff3f4e8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaCor&#39;s gravatar image" />
<p><span>DaCor</span><br />
<span class="score" title="1339 reputation points"><span>1.3k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaCor has one accepted answer">2%</span></p>
</div>
</div>
<div id="comments-container-43310" class="comments-container">
<span id="43317"></span>
<div id="comment-43317" class="comment">
<div id="post-43317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thats neat but it throws an error with my query: "Error: runtime error: open64: 111 Connection refused /home/roles/overpass/db//osm3s_v0.7.52_osm_base Dispatcher_Client::3"</p>
</div>
<div id="comment-43317-info" class="comment-info">
<span class="comment-age">(29 May '15, 17:06)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
</div>
<div id="comment-tools-43310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43310-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="59309"></span>

<div id="answer-container-59309" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59309-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use <a href="https://wiki.openstreetmap.org/wiki/Wikidata%2BOSM_SPARQL_query_service">OSM+Wikidata service</a> to find it.</p>
<pre><code>#defaultView:Map
SELECT ?osmid ?name ?nameen ?namega ?loc {
  # subjects must have all 3 tags: name, name:en, name:ga
  ?osmid osmt:name ?name ;
         osmt:name:en ?nameen ;
         osmt:name:ga ?namega .
&#10;  # &quot;name&quot; is not the same as &quot;name:ga&quot; or &quot;name:en&quot;
  FILTER (?name != ?nameen &amp;&amp; ?name != ?namega)
&#10;  # Limit to those that are within 500km around Ireland &quot;center&quot;
  # The center is taken from Wikidata Q27 (Ireland), P625 (location)
  wd:Q27 wdt:P625 ?irelandCenter .
  SERVICE wikibase:around {
    ?osmid osmm:loc ?loc .
    bd:serviceParam wikibase:center ?irelandCenter .
    bd:serviceParam wikibase:radius &quot;500&quot; .
  }
} LIMIT 100</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '17, 08:08</strong></p>
<img src="https://secure.gravatar.com/avatar/d46d9a8875ccdaa0b3b39bf485df3ead?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nyuriks&#39;s gravatar image" />
<p><span>nyuriks</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nyuriks has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '17, 08:34</strong> </span></p>
</div>
</div>
<div id="comments-container-59309" class="comments-container">
&#10;</div>
<div id="comment-tools-59309" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59309-form-container" class="comment-form-container">
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

