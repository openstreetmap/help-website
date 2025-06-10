+++
type = "question"
title = "Struggling to extract country boundary from Mozambique"
description = '''I&#x27;m busy extracting the country boundaries for several southern African countries from PBF files downloaded from GeoFabrik using QGIS. I&#x27;m doing this by filtering the multipolygon layer on admin level, then running the dissolve algorithm on the filtered layer. This has worked for South Africa, Zimba...'''
date = "2020-01-10T22:40:00Z"
lastmod = "2020-01-12T20:49:00Z"
weight = 72468
keywords = [ "qgis", "boundaries", "admin_level", "multipolygon" ]
aliases = [ "/questions/72468" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Struggling to extract country boundary from Mozambique](/questions/72468/struggling-to-extract-country-boundary-from-mozambique)

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
<span id="post-72468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72468-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm busy extracting the country boundaries for several southern African countries from PBF files downloaded from GeoFabrik using QGIS.</p>
<p>I'm doing this by filtering the multipolygon layer on admin level, then running the dissolve algorithm on the filtered layer. This has worked for South Africa, Zimbabwe and Botswana, but I cannot get the correct result for Mozambique. I cannot seem to find a filter query that gets me the country's borders that I see on Open Street Maps and I'm not sure why, it's almost as if the country doesn't have any polygons to represent its provinces, but that doesn't make sense because I can see it on the Open Street Maps website.</p>
<p>Does anyone know why Mozambique is so different from its neighbors and what I can do to get the country's boundary?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jan '20, 22:40</strong></p>
<img src="https://secure.gravatar.com/avatar/62d4beafa99dc707da2a400597901681?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Walter&#39;s gravatar image" />
<p><span>Walter</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Walter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72468" class="comments-container">
&#10;</div>
<div id="comment-tools-72468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72468-form-container" class="comment-form-container">
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

<span id="72470"></span>

<div id="answer-container-72470" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72470-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Walter has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It can sometimes happen that one small part of the country boundary lies outside of the Geofabrik extract and then the boundary cannot be built. I am the maintainer of the Geofabrik service and will have a look; in the meantime, why not try out this OSM boundaries service: <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jan '20, 23:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-72470" class="comments-container">
<span id="72471"></span>
<div id="comment-72471" class="comment">
<div id="post-72471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Cool thanks for taking a look. I checked out the extract of Mozam found here: <a href="https://download.openstreetmap.fr/extracts/africa/mozambique.osm.pbf">https://download.openstreetmap.fr/extracts/africa/mozambique.osm.pbf</a> and it has similar problems, although I can get much better polygons from the admin level filter using this one (just not the polygons I need). But I'll use that boundaries service you suggested in the mean time, thanks for the help.</p>
</div>
<div id="comment-72471-info" class="comment-info">
<span class="comment-age">(11 Jan '20, 15:07)</span> <span class="comment-user userinfo">Walter</span>
</div>
</div>
</div>
<div id="comment-tools-72470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72470-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72479"></span>

<div id="answer-container-72479" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72479-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's how it can be perform with Overpass:</p>
<pre><code>area[&quot;ISO3166-1&quot;~&quot;MZ|ZW&quot;]; //Mozambique/Zimbabwe
rel(pivot)-&gt;.countries;
rel(area)[admin_level=4];
out geom;
.countries out geom;;</code></pre>
<p><a href="https://overpass-turbo.eu/s/PG4">https://overpass-turbo.eu/s/PG4</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '20, 17:30</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jan '20, 17:33</strong> </span></p>
</div>
</div>
<div id="comments-container-72479" class="comments-container">
<span id="72480"></span>
<div id="comment-72480" class="comment">
<div id="post-72480-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the query, but If I open the query the vector overlay shows that the returned geometry seems to be the maritime boundaries and not the land based coastline, so I don't get the detail of the coastline for Mozambique using this query.</p>
</div>
<div id="comment-72480-info" class="comment-info">
<span class="comment-age">(12 Jan '20, 18:18)</span> <span class="comment-user userinfo">Walter</span>
</div>
</div>
<span id="72481"></span>
<div id="comment-72481" class="comment">
<div id="post-72481-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You asked for "country boundaries" It returns them. You made mention of "provinces", It also returns those. You said you were "filtering by admin_level". It filters by admin_level. Coastlines don't usually contain admin_level tags. The ' boundaries service' recommended by Frederik returns the same boundaries as the OP routine.</p>
</div>
<div id="comment-72481-info" class="comment-info">
<span class="comment-age">(12 Jan '20, 18:47)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="72482"></span>
<div id="comment-72482" class="comment">
<div id="post-72482-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe I'm using the wrong terminology to describe what I need, but if I filter on admin level for several other countries I do get the polygons that represent the coastline for that country, it just seems to be failing for Mozambique. Using the boundaries service returned the correct coastline boundary polygons when set to "land".</p>
</div>
<div id="comment-72482-info" class="comment-info">
<span class="comment-age">(12 Jan '20, 20:49)</span> <span class="comment-user userinfo">Walter</span>
</div>
</div>
</div>
<div id="comment-tools-72479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72479-form-container" class="comment-form-container">
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

