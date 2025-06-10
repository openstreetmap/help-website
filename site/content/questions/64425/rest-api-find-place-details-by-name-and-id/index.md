+++
type = "question"
title = "[REST API] Find place details by name and id"
description = '''Hi :), I hope I don&#x27;t duplicate any of the previous questions. I am creating a webpage, on which I would like to display a map with all districts of the city of Gdansk and some additional information for each of them. I am trying to find some way to draw all this stuff on the map. As an initial idea...'''
date = "2018-06-28T21:51:00Z"
lastmod = "2018-07-02T09:28:00Z"
weight = 64425
keywords = [ "boundaries", "query", "api", "rest" ]
aliases = [ "/questions/64425" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[REST API\] Find place details by name and id](/questions/64425/rest-api-find-place-details-by-name-and-id)

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
<span id="post-64425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64425-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi :),</p>
<p>I hope I don't duplicate any of the previous questions.</p>
<p>I am creating a webpage, on which I would like to display a map with all districts of the city of Gdansk and some additional information for each of them. I am trying to find some way to draw all this stuff on the map.</p>
<p>As an initial idea (which may not be the best one, in the first place) am looking for a solution to send a request (REST API most preferable) to get information about a place (city, Gdansk to be exact) by its name. The information I need, are: location, boundaries, subareas (districts).</p>
<p>I will also need to be able to get the same data using an Id for each given subarea (district): location, boundaries and possibility to check if given address is a part of this subarea.</p>
<p>I will be grateful for help and can provide all required details to have the issue sorted out.</p>
<p>Thanks in advance :), Bulczi.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-rest" rel="tag" title="see questions tagged &#39;rest&#39;">rest</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '18, 21:51</strong></p>
<img src="https://secure.gravatar.com/avatar/e3db18bd716bca09c67c3ecdb8bae35f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bulczi&#39;s gravatar image" />
<p><span>Bulczi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bulczi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64425" class="comments-container">
&#10;</div>
<div id="comment-tools-64425" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64425-form-container" class="comment-form-container">
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

<span id="64433"></span>

<div id="answer-container-64433" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64433-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you want is probably the <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim API</a> or maybe <a href="http://photon.komoot.de/">Photon</a> (which is an ElasticSearch based search engine for Nominatim data).</p>
<p>Depending onwhat exactly you want to do, utilizing the <a href="http://overpass-api.de/">Overpass-API</a> may work too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '18, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '18, 07:58</strong> </span></p>
</div>
</div>
<div id="comments-container-64433" class="comments-container">
<span id="64471"></span>
<div id="comment-64471" class="comment">
<div id="post-64471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi SimonPoole :)</p>
<p>Thank you for your answer.</p>
<p>I actually took a shot with Nominatim API, but I got some issues there. <a href="https://nominatim.openstreetmap.org/details.php?place_id=223605623">Here</a> are Gdansk city information found on Nominatim. The things I am looking for are:</p>
<ol>
<li>The Gdansk city area (which is shown on the map in blue)</li>
<li>All the references, that can be found at the bottom of the page in Administrative section</li>
<li>Possibility to navigate to this references</li>
<li>Access to the area of this references (so the same as in point 1, but for the administrative reference)</li>
</ol>
<p>I need all of this, to be able, to draw it on the map divided on districts having just a city name.</p>
<p>For now I have only managed to find the some places in Gdansk using the following Nominatim request:</p>
<p><a href="https://nominatim.openstreetmap.org/search/Gdansk?format=json&amp;polygon=1&amp;polygon_geojson=1&amp;limit=9999">https://nominatim.openstreetmap.org/search/Gdansk?format=json&amp;polygon=1&amp;polygon_geojson=1&amp;limit=9999</a></p>
<p>, but I can find no results, that are stated in the Administrative reference on the Nominatim page.</p>
</div>
<div id="comment-64471-info" class="comment-info">
<span class="comment-age">(01 Jul '18, 11:56)</span> <span class="comment-user userinfo">Bulczi</span>
</div>
</div>
<span id="64478"></span>
<div id="comment-64478" class="comment">
<div id="post-64478-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You may want to have a look at <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a> to see what boundaries are actually available in OSM for Gdansk (potentially you could simply extract these directly without using Nominatim).</p>
</div>
<div id="comment-64478-info" class="comment-info">
<span class="comment-age">(02 Jul '18, 09:28)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64433-form-container" class="comment-form-container">
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

