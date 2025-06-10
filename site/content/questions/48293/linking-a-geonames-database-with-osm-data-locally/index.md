+++
type = "question"
title = "Linking a Geonames database, with OSM data locally"
description = '''Till now, we used the free Geonames database as a location database to our project. But now, we want to implement area based search for our users, which isn&#x27;t supported by Geonames, as each and every city, county, country etc. is marked geographically by a single latitude and longitude. Is it possib...'''
date = "2016-02-22T16:31:00Z"
lastmod = "2016-02-24T14:50:00Z"
weight = 48293
keywords = [ "overpass", "nominatim", "geonames" ]
aliases = [ "/questions/48293" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Linking a Geonames database, with OSM data locally](/questions/48293/linking-a-geonames-database-with-osm-data-locally)

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
<span id="post-48293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48293-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Till now, we used the free Geonames database as a location database to our project. But now, we want to implement area based search for our users, which isn't supported by Geonames, as each and every city, county, country etc. is marked geographically by a single latitude and longitude.</p>
<p>Is it possible somehow, to link the data from Geonames, to ways and relations (where available) from OSM?</p>
<p>We have a Nominatim server locally installed, and also have access locally to the Overpass api. I've searched for hours, but can't find anything that would help me in this matter:|</p>
<p>Basically, what I would like to do is either one of the following two:</p>
<ol>
<li>Keep the Geonames data about cities, counties, countries, etc. and link an OSM way, or relation id to them which marks their boundary, where available</li>
<li>Leave out Geonames all together from the equation, and build a hierarchical location database with cities, counties, countries etc. from the OSM data (this would mean, a way to start from countries, and somehow list every other place that is hierarchicaly under the respective country, and store it in a database)</li>
</ol>
<p>EDIT: I would prefer to go with the first option, if it is possible, but if it's not possible, I would be happy to get some guidance on how to achieve the second option, as the data is present hierarchicaly in the OSM data (it can be seen when searching with Nominatim), but I just can't find out how to obtain it easily.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geonames" rel="tag" title="see questions tagged &#39;geonames&#39;">geonames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '16, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/8d611d043d7267073e41089a5283fbe1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adam%20Baranyai&#39;s gravatar image" />
<p><span>Adam Baranyai</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adam Baranyai has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Feb '16, 20:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-48293" class="comments-container">
<span id="48295"></span>
<div id="comment-48295" class="comment">
<div id="post-48295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As a clarification could you indicate what exactly you want to use from Geonames? Ancillary data, population etc?</p>
</div>
<div id="comment-48295-info" class="comment-info">
<span class="comment-age">(22 Feb '16, 22:25)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="48300"></span>
<div id="comment-48300" class="comment">
<div id="post-48300-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Only the names of populated locations and administrative regions, together with their hierarchy. So, basically everything which has an fcode like PPL% or ADM%.</p>
</div>
<div id="comment-48300-info" class="comment-info">
<span class="comment-age">(22 Feb '16, 23:43)</span> <span class="comment-user userinfo">Adam Baranyai</span>
</div>
</div>
</div>
<div id="comment-tools-48293" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48293-form-container" class="comment-form-container">
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

<span id="48314"></span>

<div id="answer-container-48314" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48314-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Adam Baranyai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From you comment I would be surprised if taking the 2nd route would not be superior given that you don't need any of the extra data GeoNames provides. Naturally the quality of OSM data varies by region, but in January I counted for GeoNames 8'712 vs. OSM 12'699 inhabited places in Switzerland .</p>
<p>It might be possible to extract the hierarchies from Nominatim but we will need somebody with the specific knowledge to way in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '16, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Feb '16, 21:58</strong> </span></p>
</div>
</div>
<div id="comments-container-48314" class="comments-container">
<span id="48324"></span>
<div id="comment-48324" class="comment">
<div id="post-48324-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was thinking about this problem, right now, I am experimenting with route 1, doing the following:</p>
<p>Fetching the needed records from the GeoNames database, reverse geocoding them by their latitude, longitude, with an ever decreasing zoom(starting from 15) until either I find an exact match to their name in the results, a very simmilar match to their name in the results or I reach zoom level 2. (of course, I am not looking for only exact matches, sometimes I delete some special phrases from the name, or add it, because there are some locations which are marked as "Something CP" in OSM data, and only "Something" in GeoNames, or vice-versa.)</p>
<p>As I've only installed Nominatim recently, I have only uploaded the data of Great Brittain, and I am experimenting with that. To process 100 such records from GeoNames in this way, it takes around 80 seconds(yes, it is rather slow, because to get the full information I need to reverse geocode, then geocode, then lookup the results, as I said, I am still experimenting, and trying to make this faster).</p>
</div>
<div id="comment-48324-info" class="comment-info">
<span class="comment-age">(24 Feb '16, 09:26)</span> <span class="comment-user userinfo">Adam Baranyai</span>
</div>
</div>
<span id="48325"></span>
<div id="comment-48325" class="comment">
<div id="post-48325-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As for the second route, I was thinking about something like the following: - show me each entity with admin level 3 from specific country - for each entity shown, show me each entity with admin level 4 - for each entity shown, show me each entity with admin level 5 - etc...</p>
<p>But this would still be incomplete, if for example, in a country, there is something that is a direct descendant which is not admin level 3, but 4,5,6...</p>
</div>
<div id="comment-48325-info" class="comment-info">
<span class="comment-age">(24 Feb '16, 09:28)</span> <span class="comment-user userinfo">Adam Baranyai</span>
</div>
</div>
<span id="48329"></span>
<div id="comment-48329" class="comment">
<div id="post-48329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Some update on this situation: Since then, I've managed to fasten the script, by using the two php classes Nominatim uses, and leaving out the web-api from the calculation. This way, I can process 1000 records from GeoNames in ~92 seconds(almost 10x faster then the original version), and I get the following results for 1000 random rows: approximatly 607 records can be matched to an osm entity(node, way, relation), approximatly 100 records are tagged with an incorrect country_id in the geonames database (for example: some cities are tagged to be in GB, but when reverse-geocoding their lat-lon coordinates, it seems that they are in CY, additionally they're name also suggest that they are greek locations), and there are no name matches for the rest 293 records. With additional naming tweeks, I may obtain an even better result, but as for the time being, this seems okay to me(at least for GB, we will see how it fares on other regions of the world).</p>
<p>But if what you say is true, that OSM has better "coverage" regarding populated places around the world, it seems that the second route would be superior, and I should find a way to utilize that route.</p>
</div>
<div id="comment-48329-info" class="comment-info">
<span class="comment-age">(24 Feb '16, 14:50)</span> <span class="comment-user userinfo">Adam Baranyai</span>
</div>
</div>
</div>
<div id="comment-tools-48314" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48314-form-container" class="comment-form-container">
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

