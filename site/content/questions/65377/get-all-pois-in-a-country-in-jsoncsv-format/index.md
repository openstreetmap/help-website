+++
type = "question"
title = "Get all POIs in a country in json/csv format"
description = '''Hi, I would need all the available points of interest from a country in json/csv format, with the following fields: POI name, POI address, POI city, POI county, POI postcode. Something like what Nominatim returns. I&#x27;ve downloaded the country .osm.pbf file from geofabrik, but the data is not even clo...'''
date = "2018-08-16T00:46:00Z"
lastmod = "2018-08-18T19:06:00Z"
weight = 65377
keywords = [ "json", "csv", "osm", "poi" ]
aliases = [ "/questions/65377" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get all POIs in a country in json/csv format](/questions/65377/get-all-pois-in-a-country-in-jsoncsv-format)

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
<span id="post-65377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65377-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I would need all the available points of interest from a country in json/csv format, with the following fields: POI name, POI address, POI city, POI county, POI postcode. Something like what Nominatim returns. I've downloaded the country .osm.pbf file from geofabrik, but the data is not even close to the format I need. What would be the way to go ?</p>
<p>Thanks for your time!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '18, 00:46</strong></p>
<img src="https://secure.gravatar.com/avatar/2607d9c98bfa068899d5b1a0d609f260?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RollyPeres&#39;s gravatar image" />
<p><span>RollyPeres</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RollyPeres has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65377" class="comments-container">
&#10;</div>
<div id="comment-tools-65377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65377-form-container" class="comment-form-container">
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

<span id="65386"></span>

<div id="answer-container-65386" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65386-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In principle you could do this with the overpass-api however that will only work for very small countries.</p>
<p>Your best bet is likely a combination of <a href="https://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a> (as you will probably want polygon centroids for POIs that are not mapped as nodes) and one of the filter applications for example osmfilter or the <a href="https://osmcode.org/osmium-tool/">osmium command line tool</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '18, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Aug '18, 13:19</strong> </span></p>
</div>
</div>
<div id="comments-container-65386" class="comments-container">
<span id="65396"></span>
<div id="comment-65396" class="comment">
<div id="post-65396-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>but Overpass will only show the county, city and postcode if they are mapped on the POI. In some countries this information is mapped as separate relations. I think this is also a problem for osmfilter and osmium (but I'm not familiar with them). You will need to process those boundaries somewhere in the workflow to get the CSV you want.</p>
</div>
<div id="comment-65396-info" class="comment-info">
<span class="comment-age">(17 Aug '18, 06:40)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="65424"></span>
<div id="comment-65424" class="comment">
<div id="post-65424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Simon for the suggestion. I've taken a look at those tool, however I couldn't find a way to get the data in the needed format. What I managed to do is run the osm.pbf file through osmconvert and get it back in osm format. This file contains a bunch of nodes, ways, relations that I'm not familiar with. Are you aware of a command which would extract me the data in the format that I need ?</p>
</div>
<div id="comment-65424-info" class="comment-info">
<span class="comment-age">(18 Aug '18, 18:12)</span> <span class="comment-user userinfo">RollyPeres</span>
</div>
</div>
<span id="65425"></span>
<div id="comment-65425" class="comment">
<div id="post-65425-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Exactly what escada commented. In the osm file, some POIs do have a street/postcode/city/county attached to it, but that's rare. For the rest they should probably be calculated somehow from relations or something, but it's not intuitive whatsoever.</p>
</div>
<div id="comment-65425-info" class="comment-info">
<span class="comment-age">(18 Aug '18, 18:16)</span> <span class="comment-user userinfo">RollyPeres</span>
</div>
</div>
<span id="65426"></span>
<div id="comment-65426" class="comment">
<div id="post-65426-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For POIs without addresses you really need to have the data in a spatially enabled database to be able to determine the address.</p>
<p>There are essentially these cases you have to consider</p>
<ul>
<li>POI is in a (building-)polygon with address tags</li>
<li>POI is in a (building-)polygon which doesn't have address tags but encloses a node (or multiple nodes) with address tags, or has a node (or multiple nodes) with address tags on the outline itself</li>
<li>there is a nearby node or other element with address tags</li>
<li>there is no nearby element with address tags</li>
</ul>
<p>Note: the only tags you can expect to find explicitly tagged with a high likelihood are house number and street (addr:housenumber and addr:street), enclosing administrative or postal entities need to be either deduced from enclosing polygons or from other nearby elements.</p>
</div>
<div id="comment-65426-info" class="comment-info">
<span class="comment-age">(18 Aug '18, 19:06)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65386-form-container" class="comment-form-container">
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

