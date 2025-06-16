+++
type = "question"
title = "Road Length Africa Data by Country &amp; by City in OSM?"
description = '''I would like to get the road network length in OSM for the Africa and a dataset by Country. And for each country the length within the boundaries of the selected key urban areas like the capital, largest cities, or major port cities. In addition to length I would like to get data on road class (prim...'''
date = "2015-09-18T17:31:00Z"
lastmod = "2018-06-14T08:46:00Z"
weight = 45378
keywords = [ "data", "length", "africa", "road" ]
aliases = [ "/questions/45378" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Road Length Africa Data by Country & by City in OSM?](/questions/45378/road-length-africa-data-by-country-by-city-in-osm)

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
<span id="post-45378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45378-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to get the road network length in OSM for the Africa and a dataset by Country. And for each country the length within the boundaries of the selected key urban areas like the capital, largest cities, or major port cities.</p>
<p>In addition to length I would like to get data on road class (primary, secondary, tertiary), road surface type (paved, unpaved); road condition (good, fair, poor); and if possible an estimate of the traffic level in average number of vehicles per day (0-30, 30-100, 100-300, 300-1000, 1000-3000, more than 3000 veh/day).</p>
<p>Assuming many countries have limited data in OSM, has some already done an estimate of network length using alternative sources?. Thanks, Alberto</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-africa" rel="tag" title="see questions tagged &#39;africa&#39;">africa</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '15, 17:31</strong></p>
<img src="https://secure.gravatar.com/avatar/8d078e2e6407686e4e0507f24d9c1198?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alberto%20Nogales&#39;s gravatar image" />
<p><span>Alberto Nogales</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alberto Nogales has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Sep '15, 13:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45378" class="comments-container">
&#10;</div>
<div id="comment-tools-45378" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45378-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="45399"></span>

<div id="answer-container-45399" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45399-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-45399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Network length is easy to calculate: download OSM Africa data, select only highways (eg with osmfilter), upload to PostGIS and perform appropriate queries. You will also need a country boundary data set, for which Natural Earth will probably be adequately accurate (at least for a first iteration: it will probably lose many residential roads adjacent to the coast, so finer scale polygons will be needed eventually).</p>
<p>OSM does not hold any information on traffic frequency or road condition. Most roads in Africa will not have the surface type mapped.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '15, 12:44</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-45399" class="comments-container">
<span id="45400"></span>
<div id="comment-45400" class="comment">
<div id="post-45400-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I zoomed to a random location somewhere in the centre of Africa, and <a href="http://overpass-turbo.eu/s/bxQ">there are</a> many surface tags on highways. So, OSM supplies <span>road condition information</span> at least in some parts of Africa. "OSM does not hold any information on […] road condition" is not true.</p>
</div>
<div id="comment-45400-info" class="comment-info">
<span class="comment-age">(19 Sep '15, 13:13)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="45488"></span>
<div id="comment-45488" class="comment">
<div id="post-45488-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> The OP explicitly asked about road condition separately from surface, and it was in that sense that I answered them.</p>
</div>
<div id="comment-45488-info" class="comment-info">
<span class="comment-age">(21 Sep '15, 20:59)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="45489"></span>
<div id="comment-45489" class="comment">
<div id="post-45489-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a>, oh, right, reading helps ("road surface type (paved, unpaved); road condition (good, fair, poor)"). okay … yes, "condition" may be less popular. We could count our "smoothness" tag as condition, can't we? Yes, seems to me much less popular than "surface".</p>
</div>
<div id="comment-45489-info" class="comment-info">
<span class="comment-age">(21 Sep '15, 21:10)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="47879"></span>
<div id="comment-47879" class="comment">
<div id="post-47879-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The potential loss of "residential roads the coast" should not be significant compared with the total in the country. With regard to road condition I can provide definitions of Good, Fair, Poor using the International Roughness Index (IRI) by a given Road surface (paved or unpaved)to provide a consistent measurement of "smoothness".</p>
</div>
<div id="comment-47879-info" class="comment-info">
<span class="comment-age">(03 Feb '16, 19:05)</span> <span class="comment-user userinfo">Alberto Nogales</span>
</div>
</div>
</div>
<div id="comment-tools-45399" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45399-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45505"></span>

<div id="answer-container-45505" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45505-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-45505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The osm2pgsql documentation includes <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/docs/analysis.md">an example of how to get road statistics for a city</a>, which could be adapted to get road data for all countries in an extract.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '15, 10:31</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-45505" class="comments-container">
<span id="47882"></span>
<div id="comment-47882" class="comment">
<div id="post-47882-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there any recent example of applying osm2psgsl to any city that I could take a look at? Preferably in the Africa Region or a developing country in Latin America or Eastern Europe.</p>
</div>
<div id="comment-47882-info" class="comment-info">
<span class="comment-age">(03 Feb '16, 19:25)</span> <span class="comment-user userinfo">Alberto Nogales</span>
</div>
</div>
</div>
<div id="comment-tools-45505" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45505-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45413"></span>

<div id="answer-container-45413" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45413-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-45413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm working on a dataset that does (amongst others) just that, for all regions and countries in the world. But also with a time dimension: how much is mapped now, and what was the road length on january first of all the years since OSM started. That can give you a good idea of how complete the road network is. I could prioiritize Africa you give me a deadline.</p>
<p>It might be good to compare the results to <a href="https://www.cia.gov/library/publications/the-world-factbook/rankorder/2085rank.html#gh">CIA Factbook basic statistics on road network</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '15, 09:11</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-45413" class="comments-container">
<span id="47881"></span>
<div id="comment-47881" class="comment">
<div id="post-47881-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please share the status on the world data set that you have worked. I also have worldwide data and been recently involved mostly in the Africa Region. Maybe we could test a few countries to start comparing results. I suggest Tanzania, Uganda, Ghana and Mozambique for which I have some detailed data. I also have some estimates for the entire Africa Region that could be useful.</p>
</div>
<div id="comment-47881-info" class="comment-info">
<span class="comment-age">(03 Feb '16, 19:11)</span> <span class="comment-user userinfo">Alberto Nogales</span>
</div>
</div>
<span id="47886"></span>
<div id="comment-47886" class="comment">
<div id="post-47886-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Mapbox has a website where the total mapped road length per country is compared with CIA data: <a href="https://www.mapbox.com/data-platform/country/#uganda">https://www.mapbox.com/data-platform/country/#uganda</a></p>
</div>
<div id="comment-47886-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 05:59)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-45413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45413-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64212"></span>

<div id="answer-container-64212" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64212-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>Download an OSM Extract in .osm.pbf <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts</a></li>
<li>Find an OSM relation with the city boundary you want then <code>wget -O boundary.osm </code><a href="https://www.openstreetmap.org/api/0.6/relations/RELATION_ID/full"><code>https://www.openstreetmap.org/api/0.6/relations/RELATION_ID/full</code></a></li>
<li><code>osmium extract -p region.osm extract.osm.pbf -o region.osm.pbf</code></li>
<li><code>osmium tags-filter extract.osm.pbf w/highway=motorway,trunk,primary,secondary,tertiary,unclassified,residential -o roads.osm.pbf</code></li>
<li><code>osmium export roads.osm.pbf -o roads.geojson</code></li>
<li><code>geojson-stats roads.geojson</code></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jun '18, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/7284ad488e18a2b052a9c7b8fe1e3922?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aharvey&#39;s gravatar image" />
<p><span>aharvey</span><br />
<span class="score" title="523 reputation points">523</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aharvey has 4 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-64212" class="comments-container">
&#10;</div>
<div id="comment-tools-64212" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64212-form-container" class="comment-form-container">
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

