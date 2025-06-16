+++
type = "question"
title = "How to query and select the polygon by postal code ?"
description = '''Hi OSM community, I am totally new to Geodata and gis, so please try to answer even if its a dumb question. My task is to find the distance between 2 given addresses using osm. What I have done so far ?  Downloaded osm.pbf file for my region Imported it to local postgresql postgis enabled database w...'''
date = "2017-02-01T15:25:00Z"
lastmod = "2017-02-02T12:04:00Z"
weight = 54399
keywords = [ "osm2pgsql", "postgis" ]
aliases = [ "/questions/54399" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to query and select the polygon by postal code ?](/questions/54399/how-to-query-and-select-the-polygon-by-postal-code)

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
<span id="post-54399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54399-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi OSM community,</p>
<p>I am totally new to Geodata and gis, so please try to answer even if its a dumb question.</p>
<p>My task is to find the distance between 2 given addresses using osm.</p>
<p>What I have done so far ?</p>
<ol>
<li>Downloaded osm.pbf file for my region</li>
<li>Imported it to local postgresql postgis enabled database with different tables (planet_osm_line, planet_osm_nodes, planet_osm_point, planet_osm_polygon.. etc)</li>
</ol>
<p>Approach for my task:</p>
<p>So to calculate the distance between 2 points I thought of gecoding the addresses first and then use st_distance() to find the distance between the 2 points. (Please correct me if my approach is not advisable)</p>
<p>Where I am stuck ?</p>
<p>To select the polygon using the postal code, I thought of filtering it through postal_code. Unfortunately it does not have a column named postal_code. So how could I achieve this using the above mentioned tables and geocode the address.</p>
<p>EDIT 1: Or is it possible to just extract "addr:city", "addr:country", "addr:housenumber", "addr:housename", "addr:postcode", "addr:street", "lat", "lon"fields from osm file using osmconvert and then query against it to get the lat/lon ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '17, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/2a95229b87eba17c63a633a8fe609aa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="3yK&#39;s gravatar image" />
<p><span>3yK</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="3yK has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Feb '17, 15:54</strong> </span></p>
</div>
</div>
<div id="comments-container-54399" class="comments-container">
&#10;</div>
<div id="comment-tools-54399" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54399-form-container" class="comment-form-container">
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

<span id="54400"></span>

<div id="answer-container-54400" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54400-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is of course possible to extract the addresses. Take a look at <a href="https://wiki.openstreetmap.org/wiki/Nominatim">https://wiki.openstreetmap.org/wiki/Nominatim</a></p>
<p>It depends on where you are located, but there is a good chance that there won't be polygon features associated with postal codes, or perhaps even much address data at all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '17, 16:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-54400" class="comments-container">
<span id="54406"></span>
<div id="comment-54406" class="comment">
<div id="post-54406-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But the installation of nominatim seems a little bit complicated. My query looks simple.</p>
<p>Is it possible to geocode using the question I asked in the section EDIT 1 ? will it miss some data ?</p>
<p>What are the advantages of using nominatim over manual querying ?</p>
</div>
<div id="comment-54406-info" class="comment-info">
<span class="comment-age">(01 Feb '17, 16:42)</span> <span class="comment-user userinfo">3yK</span>
</div>
</div>
<span id="54409"></span>
<div id="comment-54409" class="comment">
<div id="post-54409-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can investigate the results nominatim returns using the public server:</p>
<p><a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a></p>
<p>nominatim builds on the osm2pgsql schema that you have used above, adding indexes and associations that are not necessarily explicitly given in any of the osm2gpsql tables. So what you are doing is starting to implement pieces of what nominatim does.</p>
</div>
<div id="comment-54409-info" class="comment-info">
<span class="comment-age">(01 Feb '17, 17:01)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="54427"></span>
<div id="comment-54427" class="comment">
<div id="post-54427-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nominatim takes the same data as you did but processes and stores it in such a way that geocoding is fast. This includes combining information from different types of relations and objects.</p>
<p>Postal code boundaries as mapped as separate relations in some countries (e.g. Germany, part of Belgium). This technique is not possible in e.g. the USA and the UK where zip codes are not areas.</p>
</div>
<div id="comment-54427-info" class="comment-info">
<span class="comment-age">(02 Feb '17, 12:04)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-54400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54400-form-container" class="comment-form-container">
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

