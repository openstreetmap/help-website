+++
type = "question"
title = "osm2pgsql does not build geometries for objects with dateline crossing"
description = '''Hello! I am trying to load a PBF dump of Russia into a PostgreSQL database using osm2pgsql. All works almost nice, but planet_osm_polygon table does not contain rows corresponding to objects situated in partly Eastern, partly Western Hemisphere, such as Chukotka Autonomous Okrug, Far Eastern Federal...'''
date = "2019-01-10T09:32:00Z"
lastmod = "2022-05-15T17:54:00Z"
weight = 67534
keywords = [ "antimeridian", "osm2pgsql", "geofabrik" ]
aliases = [ "/questions/67534" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql does not build geometries for objects with dateline crossing](/questions/67534/osm2pgsql-does-not-build-geometries-for-objects-with-dateline-crossing)

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
<span id="post-67534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67534-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! I am trying to load a PBF dump of Russia into a PostgreSQL database using osm2pgsql. All works almost nice, but <em>planet_osm_polygon</em> table does not contain rows corresponding to objects situated in partly Eastern, partly Western Hemisphere, such as Chukotka Autonomous Okrug, Far Eastern Federal District and Russia itself. I checked this fact with the following query:</p>
<p><em>select * from planet_osm_polygon where boundary='administrative' and (admin_level='2' or admin_level='3' or admin_level='4') order by admin_level</em></p>
<p>All regions have been created successfully, but those 3 are absent. Here is my command for osm2pgsql to create the database:</p>
<p>osm2pgsql --create --database geo3 --slim -U postgres -E 4326 --style planet.style --hstore --multi-geometry -C 20000 --number-processes 2 -r pbf ru.osm.pbf</p>
<p>Could anyone please help me?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-antimeridian" rel="tag" title="see questions tagged &#39;antimeridian&#39;">antimeridian</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jan '19, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/7e8e1b07b427abdbd7ba5e9403f87e01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="molokanov&#39;s gravatar image" />
<p><span>molokanov</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="molokanov has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '19, 11:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-67534" class="comments-container">
&#10;</div>
<div id="comment-tools-67534" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67534-form-container" class="comment-form-container">
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

<span id="67539"></span>

<div id="answer-container-67539" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67539-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It isn't possible to represent objects crossing the dateline in WGS84 coordinates and OSM data does not contain any such objects (obvously).</p>
<p>All objects that "should" cross the dateline have been split. I would suggest turning on the data layer on openstreetmap.org and inspecting some of the objects near the dateline.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '19, 00:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '19, 00:48</strong> </span></p>
</div>
</div>
<div id="comments-container-67539" class="comments-container">
<span id="67540"></span>
<div id="comment-67540" class="comment">
<div id="post-67540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understand the fact that in WGS84 these objects are split by 180th meridian into two or more separate parts, some of them starting from 180W and other ending at 180E. Consider, for example, relation id 151231. OSM provides all necessary "vertical" ways along 180E and 180W longitudes that are members of this relation and which are performing this splitting and closing all resulting polygons. Apparently, a set of closed polygons can be used to create geometries for the whole relation and we can see this set of polygons if we simply request the relation in the browser: <a href="https://www.openstreetmap.org/relation/151231.">https://www.openstreetmap.org/relation/151231.</a> But my osm2pgsql doesn't build its geometry. How should I make osm2pgsql build it?</p>
</div>
<div id="comment-67540-info" class="comment-info">
<span class="comment-age">(11 Jan '19, 05:39)</span> <span class="comment-user userinfo">molokanov</span>
</div>
</div>
<span id="67541"></span>
<div id="comment-67541" class="comment">
<div id="post-67541-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just checked my database, I have six entries in planet_osm_polygon for 151231 which looks about right.</p>
<p>You are looking for the negative id I hope?</p>
<p>As in</p>
<pre><code>select osm_id from planet_osm_polygon where osm_id=-151231;</code></pre>
</div>
<div id="comment-67541-info" class="comment-info">
<span class="comment-age">(11 Jan '19, 06:33)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="67542"></span>
<div id="comment-67542" class="comment">
<div id="post-67542-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Exactly. I'm looking for osm_id=-151231 with the same query but, on the contrast, I have no entries. What can be the cause?</p>
</div>
<div id="comment-67542-info" class="comment-info">
<span class="comment-age">(11 Jan '19, 07:58)</span> <span class="comment-user userinfo">molokanov</span>
</div>
</div>
<span id="67543"></span>
<div id="comment-67543" class="comment not_top_scorer">
<div id="post-67543-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osm2pgsql version? And are the polygons in question unbroken in your input data? (I know that is difficult to determine)</p>
</div>
<div id="comment-67543-info" class="comment-info">
<span class="comment-age">(11 Jan '19, 08:18)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="67545"></span>
<div id="comment-67545" class="comment not_top_scorer">
<div id="post-67545-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osm2pgsql 0.96.0</p>
<p>To determine whether all polygons being formed with osm2pgsql are unbroken seems to be impossible. They are not saved in any database field. And members of the relation are ways which are obviously unclosed.</p>
<p>Instead, I did the following thing. I took the latest OSM dump for Russia, loaded it into PostgreSQL, the result is the same. I took all members of relation 151231 via downloadable XML file of the relation. Among the ways listed there, some of them are absent in planet_osm_line table. For example, 180th-meridian ways 239992373, 23820613 and especially border way 50752242. Does it necessarily mean that I have some polygons created by osm2pgsql unclosed?</p>
</div>
<div id="comment-67545-info" class="comment-info">
<span class="comment-age">(11 Jan '19, 08:54)</span> <span class="comment-user userinfo">molokanov</span>
</div>
</div>
<span id="67546"></span>
<div id="comment-67546" class="comment not_top_scorer">
<div id="post-67546-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Right now the suspicion is that there might be an issue with geometry building that crept in between 0.95 and 0.96 (it does seem a bit unlikely though).</p>
<p>I would like to investigate a couple of things before continuing here.</p>
</div>
<div id="comment-67546-info" class="comment-info">
<span class="comment-age">(11 Jan '19, 09:46)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="67547"></span>
<div id="comment-67547" class="comment">
<div id="post-67547-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you check if the relevant ways from the antimeridian are in your database?</p>
<p>For example way 239992380 (in planet_osm_line).</p>
<p>Sorry I didn't see that you had already answered this.</p>
<p>In any case the issue is likely that extracts from geofabrik do not contain the antimerdian ways and osm2pgsql then obviously can't build the polygons, I tested with an extract of Fiji and saw exactly this issue. My regular database contains the full planet and, naturally, doesn't have this issue.</p>
<p>I've raised the issue with geofabrik, lets see what Frederik says.</p>
</div>
<div id="comment-67547-info" class="comment-info">
<span class="comment-age">(11 Jan '19, 11:02)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="67549"></span>
<div id="comment-67549" class="comment not_top_scorer">
<div id="post-67549-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have checked required ways. Way 239992380 is present in planet_osm_line, whereas way 239992373 is absent.</p>
<p>I will try to load bz2 dump, instead of pbf, maybe this will help me. Full planet is too huge for me, my workstation has 32 GB RAM.</p>
</div>
<div id="comment-67549-info" class="comment-info">
<span class="comment-age">(11 Jan '19, 11:47)</span> <span class="comment-user userinfo">molokanov</span>
</div>
</div>
<span id="67550"></span>
<div id="comment-67550" class="comment not_top_scorer">
<div id="post-67550-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>bz2 dump also didn't solve this issue. Results are the same. Hope we will get Geofabrik's answer soon.</p>
</div>
<div id="comment-67550-info" class="comment-info">
<span class="comment-age">(11 Jan '19, 13:19)</span> <span class="comment-user userinfo">molokanov</span>
</div>
</div>
<span id="67553"></span>
<div id="comment-67553" class="comment">
<div id="post-67553-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For reasons unknown, the Geofabrik polygon files used for clipping Aaia, Russia and the Far Eastern District did not extend to 180° but only to 179.9999° (and -179.999°). With regard to Fiji, the Australia-Oceania file did not even contain the over-the-dateline part of the nation, even though the Fiji polygon itself did. I've fixed these issues now and hope that tomorrow's extracts will be good.</p>
</div>
<div id="comment-67553-info" class="comment-info">
<span class="comment-age">(11 Jan '19, 14:33)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="67577"></span>
<div id="comment-67577" class="comment not_top_scorer">
<div id="post-67577-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've checked the new extract for Russia. It is still not corrected. At least two ways with absolutely different tag sets are absent in the resulting database, but they both are needed to from the country's border correctly:</p>
<p><a href="https://www.openstreetmap.org/way/239992373">https://www.openstreetmap.org/way/239992373</a></p>
<p><a href="https://www.openstreetmap.org/way/50752242">https://www.openstreetmap.org/way/50752242</a></p>
</div>
<div id="comment-67577-info" class="comment-info">
<span class="comment-age">(14 Jan '19, 07:18)</span> <span class="comment-user userinfo">molokanov</span>
</div>
</div>
<span id="84482"></span>
<div id="comment-84482" class="comment not_top_scorer">
<div id="post-84482-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many years passed. And I faced the same problem. Just used osmosis to merge russia.pbf and us.pbf since the us extract borders the russian one. It's not necessary to download planet.pbf. It seems this kind of manipulations may help with other dateline issues.</p>
</div>
<div id="comment-84482-info" class="comment-info">
<span class="comment-age">(15 May '22, 17:54)</span> <span class="comment-user userinfo">shmeser</span>
</div>
</div>
</div>
<div id="comment-tools-67539" class="comment-tools">
<span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-67539-form-container" class="comment-form-container">
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

