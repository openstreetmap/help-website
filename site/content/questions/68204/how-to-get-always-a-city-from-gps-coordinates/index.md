+++
type = "question"
title = "How to get ALWAYS a city from GPS coordinates?"
description = '''Hello, I have a GPS coordinates list and I want to retrieve the corrisponding cities. I&#x27;m making calls to Nominatim service, like this: https://nominatim.openstreetmap.org/reverse?format=json&amp;amp;lat=30.4573699&amp;amp;lon=-97.8247654 The response in this case is: {&quot;place_id&quot;:&quot;32590342&quot;,&quot;licence&quot;:&quot;Data ...'''
date = "2019-03-01T16:24:00Z"
lastmod = "2019-03-03T20:09:00Z"
weight = 68204
keywords = [ "nominatim", "city", "reversegeocoding", "coordinates", "address" ]
aliases = [ "/questions/68204" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get ALWAYS a city from GPS coordinates?](/questions/68204/how-to-get-always-a-city-from-gps-coordinates)

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
<span id="post-68204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68204-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have a GPS coordinates list and I want to retrieve the corrisponding cities.</p>
<p>I'm making calls to Nominatim service, like this: <a href="https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=30.4573699&amp;lon=-97.8247654">https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=30.4573699&amp;lon=-97.8247654</a></p>
<p>The response in this case is:</p>
<pre><code>{&quot;place_id&quot;:&quot;32590342&quot;,&quot;licence&quot;:&quot;Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright&quot;,&quot;osm_type&quot;:&quot;node&quot;,&quot;osm_id&quot;:&quot;2785042716&quot;,&quot;lat&quot;:&quot;30.4573699&quot;,&quot;lon&quot;:&quot;-97.8247654&quot;,&quot;display_name&quot;:&quot;Nagoya Steak &amp; Sushi, 11630, RM 620, Anderson Mill, Austin, Williamson County, Texas, 78713, USA&quot;,&quot;address&quot;:{&quot;restaurant&quot;:&quot;Nagoya Steak &amp; Sushi&quot;,&quot;house_number&quot;:&quot;11630&quot;,&quot;road&quot;:&quot;RM 620&quot;,&quot;neighbourhood&quot;:&quot;Anderson Mill&quot;,&quot;city&quot;:&quot;Austin&quot;,&quot;county&quot;:&quot;Williamson County&quot;,&quot;state&quot;:&quot;Texas&quot;,&quot;postcode&quot;:&quot;78713&quot;,&quot;country&quot;:&quot;USA&quot;,&quot;country_code&quot;:&quot;us&quot;},&quot;boundingbox&quot;:[&quot;30.4572699&quot;,&quot;30.4574699&quot;,&quot;-97.8248654&quot;,&quot;-97.8246654&quot;]}</code></pre>
<p>So I can just get the value of <code>city</code> property and obtain the city. What about getting the city when the response doesn't have <code>city</code> property?</p>
<p>According to <a href="https://help.openstreetmap.org/questions/61683/all-possible-fields-of-address-object">this answer</a>, I see that I can get other properties, such as <code>town</code>, <code>village</code>, <code>suburb</code>, <code>locality</code>, <code>hamlet</code> and so on... but what is the best? If Nominatim response doesn't have <code>city</code> what property should I look for? And if even that property doesn't appear what should be the next property to try to get the value from?</p>
<p>Can you make a list of these properties, ordered by frequency or relevance?</p>
<p>In addition, what about places that doesn't have any address property? Here is some examples:</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=19.2954697&amp;lon=-99.1545323">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=19.2954697&amp;lon=-99.1545323</a> <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=28.7146224&amp;lon=77.1577398">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=28.7146224&amp;lon=77.1577398</a> <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=33.2038405&amp;lon=-96.7436876">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=33.2038405&amp;lon=-96.7436876</a> <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=28.7131567&amp;lon=77.1466021">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=28.7131567&amp;lon=77.1466021</a> <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=32.2327348&amp;lon=-81.4502764">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=32.2327348&amp;lon=-81.4502764</a> <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=35.851869&amp;lon=-79.0196451">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=35.851869&amp;lon=-79.0196451</a> <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=19.3709484&amp;lon=-99.1666932">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=19.3709484&amp;lon=-99.1666932</a> <a href="https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=51.6185115&amp;lon=-0.7130883">https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=51.6185115&amp;lon=-0.7130883</a></p>
<p>How to deal with them?</p>
<p>Generally speaking, what is the best strategy to ALWAYS get a city from GPS coordinates?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Mar '19, 16:24</strong></p>
<img src="https://secure.gravatar.com/avatar/50334ab2e351e4f5af1917f7f6ef8dc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andreanovenove&#39;s gravatar image" />
<p><span>Andreanovenove</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andreanovenove has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '19, 14:10</strong> </span></p>
</div>
</div>
<div id="comments-container-68204" class="comments-container">
&#10;</div>
<div id="comment-tools-68204" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68204-form-container" class="comment-form-container">
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

<span id="68206"></span>

<div id="answer-container-68206" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68206-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Andreanovenove has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The ALWAYS isn't possible. You might get close, but unless you change the definition of city you have to deal with empty data in your data model.</p>
<ul>
<li><p>Not every place (or address) in the world is assigned to a city. People living on small islands will use the name of the island as logical administrative label in their address, it doesn't make it a city.</p></li>
<li><p>A city can be multiple types of place. Especially large metropolitan areas are often both city and county, sometimes city and state (Berlin), sometimes city and country (Monaco). OSM data only allows setting one type. In rare cases two places exist in OSM data overlapping each other (same exact boundaries).</p></li>
<li><p>OSM data might be missing (explicit) assignments of streets to their city (e.g. with address tagging) or OSM data doesn't contain boundaries of a city. Other than guessing by distance it's unclear where some houses belong to.</p></li>
<li><p>Nominatim might not return the city field correctly. When a place exists as node tagged a city, but also relation (same name and/or linked) tagged a village it might return it as village. There's open issues e.g. with London boroughs, Paris Arrondissements and quarters.</p></li>
</ul>
<p><a href="https://wiki.openstreetmap.org/wiki/Key:place">https://wiki.openstreetmap.org/wiki/Key:place</a> lists the place types and the right columns of the table have global counts. <a href="https://github.com/OpenCageData/address-formatting/blob/master/conf/components.yaml">https://github.com/OpenCageData/address-formatting/blob/master/conf/components.yaml</a> has a hierarchy of fields relevant for an address. <a href="https://github.com/openstreetmap/Nominatim/blob/master/lib/ClassTypes.php">https://github.com/openstreetmap/Nominatim/blob/master/lib/ClassTypes.php</a> is Nominatim's internal logic to assign field names.</p>
<p>I would use the components.yaml, look for city aliases and if empty in the Nominatim response move up the hierarchy (county, state...).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '19, 17:04</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-68206" class="comments-container">
<span id="68219"></span>
<div id="comment-68219" class="comment">
<div id="post-68219-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your reply, I really appreciated it. Can you tell me what is wrong with places like this <a href="https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=51.6185115&amp;lon=-0.7130883">https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=51.6185115&amp;lon=-0.7130883</a> ? As you can see the only reference for place is country! Why?</p>
</div>
<div id="comment-68219-info" class="comment-info">
<span class="comment-age">(02 Mar '19, 14:13)</span> <span class="comment-user userinfo">Andreanovenove</span>
</div>
</div>
<span id="68220"></span>
<div id="comment-68220" class="comment">
<div id="post-68220-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That might be an issue with the Nominatim logic. Can happen in remote areas (no addresses in 20+ km radius or such) but shouldn't happen in dense populated areas. Add &amp;zoom=16 to the URL since you said you don't need housenumber level data. Even zoom=10 might work for you. The parameter is explained here <a href="http://nominatim.org/release-docs/latest/api/Reverse/">http://nominatim.org/release-docs/latest/api/Reverse/</a></p>
</div>
<div id="comment-68220-info" class="comment-info">
<span class="comment-age">(02 Mar '19, 22:44)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="68232"></span>
<div id="comment-68232" class="comment">
<div id="post-68232-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It doesn't do the trick. I get "city" with default zoom (18) from here <a href="https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=52.5332647&amp;lon=13.2065231,">https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=52.5332647&amp;lon=13.2065231,</a> but not with zoom 10. Besides, I get no city, at any zoom level, with other GPS coordinates, like this <a href="https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=-1.8292911&amp;lon=99.2568908">https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=-1.8292911&amp;lon=99.2568908</a></p>
</div>
<div id="comment-68232-info" class="comment-info">
<span class="comment-age">(03 Mar '19, 16:40)</span> <span class="comment-user userinfo">Andreanovenove</span>
</div>
</div>
<span id="68234"></span>
<div id="comment-68234" class="comment">
<div id="post-68234-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OpenStreetMap doesn't have enough data for that area. There isn't even a street mapped yet. <a href="https://nominatim.openstreetmap.org/reverse?format=html&amp;lat=-1.8292911&amp;lon=99.2568908">https://nominatim.openstreetmap.org/reverse?format=html&amp;lat=-1.8292911&amp;lon=99.2568908</a></p>
</div>
<div id="comment-68234-info" class="comment-info">
<span class="comment-age">(03 Mar '19, 17:12)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="68235"></span>
<div id="comment-68235" class="comment">
<div id="post-68235-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I see. What do you think about the first link? Giving different zoom level doesn't always do the trick. Sometimes is convenient to use default zoom because level 10 doesn't return any city field, other times is better to use other zoom level, like 10, to get the city because default level doesn't contains any city field. So, there isn't a rule that I can follow to retrieve always an address field that is city or similar (similar administrative level).</p>
</div>
<div id="comment-68235-info" class="comment-info">
<span class="comment-age">(03 Mar '19, 19:10)</span> <span class="comment-user userinfo">Andreanovenove</span>
</div>
</div>
<span id="68236"></span>
<div id="comment-68236" class="comment not_top_scorer">
<div id="post-68236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Berlin is one of cases with conflicting information. <a href="https://www.openstreetmap.org/node/240109189">https://www.openstreetmap.org/node/240109189</a> is tagged as both admin_level=2 (state) and place=city and that confused the reverse geocoding.</p>
</div>
<div id="comment-68236-info" class="comment-info">
<span class="comment-age">(03 Mar '19, 20:09)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-68206" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-68206-form-container" class="comment-form-container">
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

