+++
type = "question"
title = "Difference between local instance of Nominatim and web public platform"
description = '''Hello,  We have installed a fresh instance of Nominatim using docker by following the installation steps from https://nominatim.org/release-docs/develop/admin/Installation/ . I doubled checked multiple times for everything to be up-to-date. TIGER data is also up to date. Unfortunately, we have obser...'''
date = "2022-05-09T08:53:00Z"
lastmod = "2023-03-29T15:44:00Z"
weight = 84415
keywords = [ "docker", "nominatim", "json", "server" ]
aliases = [ "/questions/84415" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Difference between local instance of Nominatim and web public platform](/questions/84415/difference-between-local-instance-of-nominatim-and-web-public-platform)

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
<span id="post-84415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84415-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>We have installed a fresh instance of Nominatim using docker by following the installation steps from <a href="https://nominatim.org/release-docs/develop/admin/Installation/">https://nominatim.org/release-docs/develop/admin/Installation/</a> . I doubled checked multiple times for everything to be up-to-date. TIGER data is also up to date.</p>
<p>Unfortunately, we have observed some differences between what our server returns and what the public Nominatim platform shows by using the same search parameters.</p>
<p>Here are the search parameters: street=520+Madison+Avenue&amp;city=new+york&amp;state=ny&amp;postalcode=10022</p>
<p>Local url: <a href="http://142.132.128.187:8080/search.php?street=520+Madison+Avenue&amp;city=new+york&amp;state=ny&amp;postalcode=10022&amp;format=jsonv2">http://142.132.128.187:8080/search.php?street=520+Madison+Avenue&amp;city=new+york&amp;state=ny&amp;postalcode=10022&amp;format=jsonv2</a> Public url: <a href="https://nominatim.openstreetmap.org/search.php?street=520+Madison+Avenue&amp;city=new+york&amp;state=ny&amp;postalcode=10022&amp;format=jsonv2">https://nominatim.openstreetmap.org/search.php?street=520+Madison+Avenue&amp;city=new+york&amp;state=ny&amp;postalcode=10022&amp;format=jsonv2</a></p>
<p>Our response:</p>
<pre><code>[</code></pre>
<p>{ "place_id": 136458099, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://osm.org/copyright">https://osm.org/copyright",</a> "osm_type": "way", "osm_id": 266010397, "boundingbox": [ "40.7599002", "40.760584", "-73.9748887", "-73.9740315" ], "lat": "40.76022135", "lon": "-73.97442525051773", "display_name": "520 Madison Avenue, 520, Madison Avenue, Midtown East, Manhattan Community Board 5, Manhattan, New York County, New York, 10037, United States", "place_rank": 30, "category": "place", "type": "house", "importance": 0.511 } ]</p>
<p>Web response:</p>
<p>[ { "place_id": 294697572, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://osm.org/copyright">https://osm.org/copyright",</a> "osm_type": "way", "osm_id": 420281339, "boundingbox": [ "40.760019333333", "40.760119333333", "-73.974156111111", "-73.974056111111" ], "lat": "40.76006933333333", "lon": "-73.97410611111111", "display_name": "520, Madison Avenue, Midtown East, Manhattan Community Board 5, New York County, New York, 10022, United States", "place_rank": 30, "category": "place", "type": "house", "importance": 0.621 }, { "place_id": 303958173, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://osm.org/copyright">https://osm.org/copyright",</a> "osm_type": "way", "osm_id": 669246310, "boundingbox": [ "42.654086064516", "42.654186064516", "-73.770921322581", "-73.770821322581" ], "lat": "42.65413606451613", "lon": "-73.77087132258065", "display_name": "520, Madison Avenue, Park South, Lark Street, City of Albany, Albany County, New York, 12208, United States", "place_rank": 30, "category": "place", "type": "house", "importance": 0.611 }, { "place_id": 167244054, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://osm.org/copyright">https://osm.org/copyright",</a> "osm_type": "way", "osm_id": 266010397, "boundingbox": [ "40.7599002", "40.760584", "-73.9748887", "-73.9740315" ], "lat": "40.76022135", "lon": "-73.97442525051773", "display_name": "520 Madison Avenue, 520, Madison Avenue, Midtown East, Manhattan Community Board 5, New York County, New York, 10037, United States", "place_rank": 30, "category": "building", "type": "commercial", "importance": 0.511 }, { "place_id": 290349413, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://osm.org/copyright">https://osm.org/copyright",</a> "osm_type": "way", "osm_id": 24137660, "boundingbox": [ "40.751863186047", "40.751963186047", "-73.588143813953", "-73.588043813953" ], "lat": "40.75191318604651", "lon": "-73.58809381395349", "display_name": "520, Madison Avenue, Westbury, Town of North Hempstead, Nassau County, New York, 11590, United States", "place_rank": 30, "category": "place", "type": "house", "importance": 0.511 }, { "place_id": 314875463, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://osm.org/copyright">https://osm.org/copyright",</a> "osm_type": "way", "osm_id": 13087865, "boundingbox": [ "42.338065343744", "42.338165343744", "-77.67069690835", "-77.67059690835" ], "lat": "42.33811534374404", "lon": "-77.6706469083502", "display_name": "520, Madison Avenue, Town of Hornellsville, Steuben County, New York, 14843, United States", "place_rank": 30, "category": "place", "type": "house", "importance": 0.511 }, { "place_id": 290421264, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://osm.org/copyright">https://osm.org/copyright",</a> "osm_type": "way", "osm_id": 24137656, "boundingbox": [ "40.696777416667", "40.696877416667", "-73.657202972222", "-73.657102972222" ], "lat": "40.69682741666667", "lon": "-73.65715297222222", "display_name": "520, Madison Avenue, West Hempstead, Franklin Square, Town of Hempstead, Nassau County, New York, 11552, United States", "place_rank": 30, "category": "place", "type": "house", "importance": 0.511 }, { "place_id": 290418110, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://osm.org/copyright">https://osm.org/copyright",</a> "osm_type": "way", "osm_id": 24137653, "boundingbox": [ "40.674544554217", "40.674644554217", "-73.618284759036", "-73.618184759036" ], "lat": "40.67459455421687", "lon": "-73.61823475903616", "display_name": "520, Madison Avenue, South Hempstead, Baldwin, Town of Hempstead, Nassau County, New York, 11510, United States", "place_rank": 30, "category": "place", "type": "house", "importance": 0.511 }, { "place_id": 314323208, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://osm.org/copyright">https://osm.org/copyright",</a> "osm_type": "way", "osm_id": 20255741, "boundingbox": [ "41.103991788222", "41.104091788222", "-72.366563786757", "-72.366463786757" ], "lat": "41.104041788222084", "lon": "-72.36651378675711", "display_name": "520, Madison Avenue, Greenport, Town of Southold, Suffolk County, New York, 11944, United States", "place_rank": 30, "category": "place", "type": "house", "importance": 0.511 }, { "place_id": 306011336, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://osm.org/copyright">https://osm.org/copyright",</a> "osm_type": "way", "osm_id": 12320838, "boundingbox": [ "42.626001035714", "42.626101035714", "-79.071002642857", "-79.070902642857" ], "lat": "42.62605103571429", "lon": "-79.07095264285714", "display_name": "520, Madison Avenue, Lake Erie Beach, Town of Evans, Erie County, New York, 14006, United States", "place_rank": 30, "category": "place", "type": "house", "importance": 0.511 }, { "place_id": 314388006, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="https://osm.org/copyright">https://osm.org/copyright",</a> "osm_type": "way", "osm_id": 20255732, "boundingbox": [ "40.804359755102", "40.804459755102", "-73.254504265306", "-73.254404265306" ], "lat": "40.804409755102036", "lon": "-73.25445426530612", "display_name": "520, Madison Avenue, Brentwood, Suffolk County, New York, 11717, United States", "place_rank": 30, "category": "place", "type": "house", "importance": 0.511 } ]</p>
<p>Could you please help us identify what is the root cause of this behavior?</p>
<p>Many thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-docker" rel="tag" title="see questions tagged &#39;docker&#39;">docker</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '22, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/8473e49db1905d23d9381e55719356fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="radu_ncht&#39;s gravatar image" />
<p><span>radu_ncht</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="radu_ncht has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84415" class="comments-container">
&#10;</div>
<div id="comment-tools-84415" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84415-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="84416"></span>

<div id="answer-container-84416" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84416-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are not running the same software version of Nominatim and you are using different data. Differences are to be expected.</p>
<p>The public servers at <a href="https://nominatim.openstreetmap.org">https://nominatim.openstreetmap.org</a> are on a rolling release of the latest development version of Nominatim and are updated with minutely diffs. It is not possible to set up a local instance that is in exactly the same state.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '22, 09:20</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-84416" class="comments-container">
<span id="84424"></span>
<div id="comment-84424" class="comment">
<div id="post-84424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We understand that may be a slight difference between a local environment and the public servers. The issue in hand is that the difference is way too obvious, given the large difference in the number of responses obtained using both versions.</p>
<p>As we stated earlier we are running with the latest data and software version, here are some information on that: - PBF_URL: <a href="https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/planet-latest.osm.pbf">https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/pbf/planet-latest.osm.pbf</a> - REPLICATION_URL: <a href="https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/replication/day/">https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/replication/day/</a> - PostgreSQL 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1) - ENV NOMINATIM_VERSION 4.0.1</p>
<p>We also went ahead and installed all the auxiliary data sources according to <a href="https://nominatim.org/release-docs/latest/develop/data-sources/">https://nominatim.org/release-docs/latest/develop/data-sources/</a> .</p>
<p>Is there anything left to be installed/configured to be somewhat inline with the public servers ?</p>
</div>
<div id="comment-84424-info" class="comment-info">
<span class="comment-age">(10 May '22, 09:54)</span> <span class="comment-user userinfo">radu_ncht</span>
</div>
</div>
<span id="84427"></span>
<div id="comment-84427" class="comment">
<div id="post-84427-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can try reimporting with <code>NOMINATIM_TOKENIZER=icu</code>. It may or may not help. Depends on what your exact issue with the search results is. As it stands, the result on your server seems to be the more correct one.</p>
</div>
<div id="comment-84427-info" class="comment-info">
<span class="comment-age">(10 May '22, 10:50)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="84450"></span>
<div id="comment-84450" class="comment">
<div id="post-84450-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer Ionvia, we have already imported with "ICU" tokenizer.</p>
<p>Is there any difference in the search logic between a local instance and the public servers ?</p>
</div>
<div id="comment-84450-info" class="comment-info">
<span class="comment-age">(12 May '22, 09:02)</span> <span class="comment-user userinfo">radu_ncht</span>
</div>
</div>
</div>
<div id="comment-tools-84416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84416-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87004"></span>

<div id="answer-container-87004" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87004-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, you can use debug mode of Nominatim search request. Just add debug=1 parameter to both of your queries and compare the explanation of their processing, even with SQL queries to the DB.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '23, 15:44</strong></p>
<img src="https://secure.gravatar.com/avatar/8fd0f1dd50b1b8df50bfce3cde10c438?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cepslart&#39;s gravatar image" />
<p><span>Cepslart</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cepslart has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87004" class="comments-container">
&#10;</div>
<div id="comment-tools-87004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87004-form-container" class="comment-form-container">
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

