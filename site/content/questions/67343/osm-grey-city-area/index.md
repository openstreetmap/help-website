+++
type = "question"
title = "osm grey city area"
description = '''Hello, I need to get cities boundaries, I know how to do it by query the planet_osm_polygon table and get the exact result as in www.openstreetmap.org but its differ from the real city area as marked in grey e.g Towcester: https://www.openstreetmap.org/relation/1641604 As it can see the area marked ...'''
date = "2018-12-24T15:08:00Z"
lastmod = "2019-01-30T14:12:00Z"
weight = 67343
keywords = [ "boundaries", "planet_osm_polygon" ]
aliases = [ "/questions/67343" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm grey city area](/questions/67343/osm-grey-city-area)

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
<span id="post-67343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67343-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I need to get cities boundaries, I know how to do it by query the planet_osm_polygon table and get the exact result as in www.openstreetmap.org but its differ from the real city area as marked in grey</p>
<p>e.g Towcester: <a href="https://www.openstreetmap.org/relation/1641604">https://www.openstreetmap.org/relation/1641604</a></p>
<p>As it can see the area marked in orange is much bigger than the city area</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-planet_osm_polygon" rel="tag" title="see questions tagged &#39;planet_osm_polygon&#39;">planet_osm_polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Dec '18, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/53c4a40bd104f3de1bbc6ccb735e52eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="altopalo&#39;s gravatar image" />
<p><span>altopalo</span><br />
<span class="score" title="53 reputation points">53</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="altopalo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Dec '18, 15:09</strong> </span></p>
</div>
</div>
<div id="comments-container-67343" class="comments-container">
<span id="67344"></span>
<div id="comment-67344" class="comment">
<div id="post-67344-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>What do you mean by "the real city area" exactly? It looks like the "area marked as grey" is mapped as landuse=residential. It doesn't correspond to any administrative boundary and naturally a city may have other landuses such as commercial or industrial.</p>
</div>
<div id="comment-67344-info" class="comment-info">
<span class="comment-age">(24 Dec '18, 15:29)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="67346"></span>
<div id="comment-67346" class="comment not_top_scorer">
<div id="post-67346-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tn'x for the data So I looks for a way to get that 'grey area' (landuse=residential) from the osm dump DB. I assume the area I gets and also seen in the map is the administrative area of the city.</p>
</div>
<div id="comment-67346-info" class="comment-info">
<span class="comment-age">(24 Dec '18, 15:52)</span> <span class="comment-user userinfo">altopalo</span>
</div>
</div>
<span id="67347"></span>
<div id="comment-67347" class="comment">
<div id="post-67347-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Landuse=residential has nothing to do with administration, it simply marks areas of land that mappers perceive as primarily used for housing.</p>
<p>If you want adminstrative areas you will need to look at boundary relations, but that seems to be where you started as you already gave an example of such a relation.</p>
</div>
<div id="comment-67347-info" class="comment-info">
<span class="comment-age">(24 Dec '18, 18:35)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="67351"></span>
<div id="comment-67351" class="comment not_top_scorer">
<div id="post-67351-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tn'x but I know how to get the administrative area.</p>
<p>I'm looking for a way to get the Landuse=residentialstrative area of specific city by query the postgis DB.</p>
</div>
<div id="comment-67351-info" class="comment-info">
<span class="comment-age">(25 Dec '18, 07:28)</span> <span class="comment-user userinfo">altopalo</span>
</div>
</div>
<span id="67366"></span>
<div id="comment-67366" class="comment">
<div id="post-67366-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Well, you'd query the database the same way as you did for the administrative boundary, but instead query for landuse=residential objects. As has been mentioned, though, this won't give you the complete area of a settlement. There will likely also be landuse=industrial, landuse=commercial, landuse=retail, leisure=park, amenity=school, and many other types of areas that together combine to form the area of the settlement. This also assumes that the landuses and other areas have all been mapped, which isn't guaranteed.</p>
</div>
<div id="comment-67366-info" class="comment-info">
<span class="comment-age">(27 Dec '18, 16:56)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="67785"></span>
<div id="comment-67785" class="comment not_top_scorer">
<div id="post-67785-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/8189/alester"></a><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> Tried your advice and indeed I get a list of polygons inside the polygon I want to, but if i look e.g: on the landuse=residential some are really residential but some are not truly place of people (the gray areas in the map)</p>
<p>e.g this query about Buckland (village in UK)</p>
<p>select i.osm_id, i.name, i.landuse from planet_osm_polygon i join planet_osm_polygon o on ST_Contains (o.way, i.way) where o.osm_id = -4108597 and i.landuse = 'residential'</p>
<p>94353763;"";"residential" 203007994;"";"residential" 203007897;"";"residential" 195214668;"";"residential" 59825490;"Ashtree Farm";"residential" 187233334;"";"residential" 95029739;"";"residential" 94441095;"";"residential" 98217350;"";"residential" ...</p>
</div>
<div id="comment-67785-info" class="comment-info">
<span class="comment-age">(29 Jan '19, 14:41)</span> <span class="comment-user userinfo">altopalo</span>
</div>
</div>
<span id="67786"></span>
<div id="comment-67786" class="comment">
<div id="post-67786-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You say "some are really residential but some are not truly place of people". Can you give an example of one in that area that is "not truly place of people"?</p>
</div>
<div id="comment-67786-info" class="comment-info">
<span class="comment-age">(29 Jan '19, 15:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="67804"></span>
<div id="comment-67804" class="comment">
<div id="post-67804-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you mean <a href="https://www.openstreetmap.org/way/59825490#map=18/51.67190/-1.52064">Ashtree Farm</a> ? It's mapped as a residential area, it's "grey" on the map. It's probably the area around the farm house. A place where people live, hence landuse=residential is correct.</p>
<p>Maybe this does not correspond to the area's you want to extract, but I fear that your definition of "city boundaries" does not match any OSM concept, as others pointed out.</p>
</div>
<div id="comment-67804-info" class="comment-info">
<span class="comment-age">(30 Jan '19, 04:09)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="67805"></span>
<div id="comment-67805" class="comment not_top_scorer">
<div id="post-67805-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks <a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> &amp; <a href="https://help.openstreetmap.org/users/5390/escada"></a><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a></p>
<p>e.g: 94353763: <a href="https://www.openstreetmap.org/way/94353763">https://www.openstreetmap.org/way/94353763</a> - green area</p>
<p>1369487 : <a href="https://www.openstreetmap.org/relation/1369487">https://www.openstreetmap.org/relation/1369487</a> is the village and what I need.</p>
<p>What i'm tying to do is by getting a point, decide if its urban area or not.</p>
</div>
<div id="comment-67805-info" class="comment-info">
<span class="comment-age">(30 Jan '19, 06:18)</span> <span class="comment-user userinfo">altopalo</span>
</div>
</div>
<span id="67811"></span>
<div id="comment-67811" class="comment not_top_scorer">
<div id="post-67811-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure why you say 94353763 is a green area. It happens to be surrounded by a wood, but the area itself consists of houses and their gardens (visible in any aerial imagery background) so its mapping as residential is correct, and so is its display as grey in the standard map.</p>
<p>What do you see as the difference between these houses and the ones in 1369487 that qualifies one group of houses as urban and not the other?</p>
</div>
<div id="comment-67811-info" class="comment-info">
<span class="comment-age">(30 Jan '19, 11:57)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-67343" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-67343-form-container" class="comment-form-container">
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

<span id="67813"></span>

<div id="answer-container-67813" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67813-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks all for the great info, after some digging I found the way to do what I need.</p>
<p>The purpose is to find the residential boundaries of a given settlement (city, village). for my purpose a farm or few houses alone is not urban so I don't need it</p>
<p>So here are the steps I done, if someone will need it also:</p>
<p>-- 1. find the polygon of the city/village (actually I already have the osm_id of the village in my DB, but to complete the explanation ...) This returned a polygon that include the village but a lot of open areas around it.</p>
<pre><code>select name, osm_id from planet_osm_polygon where name = &#39;Buckland&#39;</code></pre>
<p>-- 2. get id of the relation(s) that are inside the polygon, need the items with negative osm_id</p>
<pre><code>select i.osm_id, i.name, i.landuse 
from planet_osm_polygon i join planet_osm_polygon o on ST_Contains (o.way, i.way) 
where o.osm_id = -4108597 and i.landuse = &#39;residential&#39; and i.osm_id &lt; 0</code></pre>
<p>-- 3. get the outer way from planet_osm_rels table</p>
<pre><code>select * from planet_osm_rels where id = 1369487;</code></pre>
<p>-- 4. get the nodes from planet_osm_ways</p>
<pre><code>select * from planet_osm_ways where id = 94437443;</code></pre>
<p>-- 5. get the way's nodes data of the from node table</p>
<pre><code>select * from planet_osm_nodes where id = 1096978061;</code></pre>
<p>I checked it on few locations and its seems to work, of course need to rewrite the queries more efficiently.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '19, 14:12</strong></p>
<img src="https://secure.gravatar.com/avatar/53c4a40bd104f3de1bbc6ccb735e52eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="altopalo&#39;s gravatar image" />
<p><span>altopalo</span><br />
<span class="score" title="53 reputation points">53</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="altopalo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Feb '19, 15:58</strong> </span></p>
</div>
</div>
<div id="comments-container-67813" class="comments-container">
&#10;</div>
<div id="comment-tools-67813" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67813-form-container" class="comment-form-container">
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

