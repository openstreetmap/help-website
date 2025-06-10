+++
type = "question"
title = "Mapnik error:  column &quot;generator:source&quot; does not exist"
description = '''Heyho! When trying to render my map from PostgreSQL/PostGIS database by generate_image.py and osm.xml I receive the following ERROR! Could somebody be so kind and try to solve my problem? If you need to see some sourcecode etc. .. just tell me and I&#x27;ll upload it here! Thanks and Greetings! Matze  Tr...'''
date = "2012-03-28T08:55:00Z"
lastmod = "2013-03-17T22:28:00Z"
weight = 11542
keywords = [ "column", "osm.xml", "osm2pgsql", "mapnik", "error" ]
aliases = [ "/questions/11542" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Mapnik error: column "generator:source" does not exist](/questions/11542/mapnik-error-column-generatorsource-does-not-exist)

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
<span id="post-11542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11542-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Heyho!</p>
<p>When trying to render my map from PostgreSQL/PostGIS database by generate_image.py and osm.xml I receive the following ERROR! Could somebody be so kind and try to solve my problem?</p>
<p>If you need to see some sourcecode etc. .. just tell me and I'll upload it here!</p>
<p>Thanks and Greetings! Matze</p>
<hr />
<pre><code>Traceback (most recent call last):
  File &quot;C:\0A\9\run_python.py&quot;, line 3, in &lt;module&gt;
    execfile(r&quot;C:\0A\9\generate_image.py&quot;)
  File &quot;C:\0A\9\generate_image.py&quot;, line 42, in &lt;module&gt;
    mapnik.load_map(m,mapfile)
RuntimeError: Postgis Plugin: PSQL error:
ERROR:  column &quot;generator:source&quot; does not exist
LINE 8:          or (power=&#39;generator&#39; and (&quot;generator:source&quot;=&#39;wind...
                                            ^
Full sql was: &#39;SELECT * FROM 
      (select *
      from planet_osm_point
      where aeroway in (&#39;airport&#39;,&#39;aerodrome&#39;,&#39;helipad&#39;)
         or barrier in (&#39;bollard&#39;,&#39;gate&#39;,&#39;lift_gate&#39;,&#39;block&#39;)
         or highway in (&#39;mini_roundabout&#39;,&#39;gate&#39;)
         or man_made in (&#39;lighthouse&#39;,&#39;power_wind&#39;,&#39;windmill&#39;,&#39;mast&#39;)
         or (power=&#39;generator&#39; and (&quot;generator:source&quot;=&#39;wind&#39; or power_source=&#39;wind&#39;))
         or &quot;natural&quot; in (&#39;peak&#39;,&#39;volcano&#39;,&#39;spring&#39;,&#39;tree&#39;,&#39;cave_entrance&#39;)
         or railway=&#39;level_crossing&#39;
      ) as symbols LIMIT 0&#39;
 (encountered during parsing of layer &#39;amenity-symbols&#39; in map &#39;osm.xml&#39;)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-column" rel="tag" title="see questions tagged &#39;column&#39;">column</span> <span class="post-tag tag-link-osm.xml" rel="tag" title="see questions tagged &#39;osm.xml&#39;">osm.xml</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Mar '12, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0198a02af3c41ad04b61e028c3b126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHein&#39;s gravatar image" />
<p><span>MHein</span><br />
<span class="score" title="141 reputation points">141</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHein has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '13, 10:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-11542" class="comments-container">
&#10;</div>
<div id="comment-tools-11542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11542-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="11544"></span>

<div id="answer-container-11544" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11544-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MHein has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is likely because your osm2pgsql version is older than the osm.xml map style. The map style assumes that osm2pgsql has imported a column named <code>generator:source</code> but in fact osm2pgsql hasn't. You can fix the problem in one of these ways:</p>
<ul>
<li>get new osm2pgsql (or just new <code>default.style</code> file) and do new import</li>
<li>get an older osm.xml map style that does not rely on <code>generator:source</code></li>
<li>insert an empty <code>generator:source</code> column into your postgres tables</li>
<li>remove the line about power generators from your osm.xml</li>
</ul>
<p>Obvoiusly, only the first option will lead to wind turbines being rendered properly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '12, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-11544" class="comments-container">
<span id="11546"></span>
<div id="comment-11546" class="comment">
<div id="post-11546-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks! I'll try the first way and if it doesn't work, i'll ask again ;)</p>
</div>
<div id="comment-11546-info" class="comment-info">
<span class="comment-age">(28 Mar '12, 09:28)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
</div>
<div id="comment-tools-11544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11544-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11545"></span>

<div id="answer-container-11545" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11545-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The software osm2pgsql, usually used to import OSM data into a rendering database, only imports a subset of the data required for rendering. What osm2pgsql deems necessary for rendering (and thus the resulting database schema) is defined in a import style-sheet. This osm2pgsql import style-sheet needs to match your mapnik rendering style-sheet, otherwise you will see errors as yours, complaining about missing columns.</p>
<p>Looking at your output, it appears you are using windows. The windows version of osm2pgsql is unfortunately very old and thus the import style-sheet going with it no longer matches the current osm mapnik style-sheet. You can find the current import style-sheet at <a href="https://trac.openstreetmap.org/browser/applications/utils/export/osm2pgsql/default.style">https://trac.openstreetmap.org/browser/applications/utils/export/osm2pgsql/default.style</a> which you will need for re-importing the data into your database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '12, 09:15</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-11545" class="comments-container">
&#10;</div>
<div id="comment-tools-11545" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11545-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20783"></span>

<div id="answer-container-20783" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20783-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Who, this is probably my solution to! I don't have much experience with linux but I got pretty far. This is my error. But my question is how can I check the versions and find the right style-sheet?</p>
<p>My Error:</p>
<pre><code>`renderd[17965]: An error occurred while loading the map layer &#39;default&#39;: :
ERROR:  column &quot;generator:source&quot; does not exist
LINE 8:          or (power=&#39;generator&#39; and (&quot;generator:source&quot;=&#39;wind...
                                            ^
Full sql was: &#39;SELECT * FROM 
      (select *
      from planet_osm_point
      where aeroway in (&#39;airport&#39;,&#39;aerodrome&#39;,&#39;helipad&#39;)
         or barrier in (&#39;bollard&#39;,&#39;gate&#39;,&#39;lift_gate&#39;,&#39;block&#39;)
         or highway in (&#39;mini_roundabout&#39;,&#39;gate&#39;)
         or man_made in (&#39;lighthouse&#39;,&#39;power_wind&#39;,&#39;windmill&#39;,&#39;mast&#39;)
         or (power=&#39;generator&#39; and (&quot;generator:source&quot;=&#39;wind&#39; or power_source=&#39;wind&#39;))
         or &quot;natural&quot; in (&#39;peak&#39;,&#39;volcano&#39;,&#39;spring&#39;,&#39;tree&#39;,&#39;cave_entrance&#39;)
         or railway=&#39;level_crossing&#39;
      ) as symbols LIMIT 0&#39;
 (encountered during parsing of layer &#39;amenity-symbols&#39; in map &#39;/home/administrator/src/mapnik-style/osm.xml&#39;)
renderd[17965]: An error occurred while loading the map layer &#39;default&#39;: :
ERROR:  column &quot;generator:source&quot; does not exist
LINE 8:          or (power=&#39;generator&#39; and (&quot;generator:source&quot;=&#39;wind...
                                            ^
Full sql was: &#39;SELECT * FROM 
      (select *
      from planet_osm_point
      where aeroway in (&#39;airport&#39;,&#39;aerodrome&#39;,&#39;helipad&#39;)
         or barrier in (&#39;bollard&#39;,&#39;gate&#39;,&#39;lift_gate&#39;,&#39;block&#39;)
         or highway in (&#39;mini_roundabout&#39;,&#39;gate&#39;)
         or man_made in (&#39;lighthouse&#39;,&#39;power_wind&#39;,&#39;windmill&#39;,&#39;mast&#39;)
         or (power=&#39;generator&#39; and (&quot;generator:source&quot;=&#39;wind&#39; or power_source=&#39;wind&#39;))
         or &quot;natural&quot; in (&#39;peak&#39;,&#39;volcano&#39;,&#39;spring&#39;,&#39;tree&#39;,&#39;cave_entrance&#39;)
         or railway=&#39;level_crossing&#39;
      ) as symbols LIMIT 0&#39;
 (encountered during parsing of layer &#39;amenity-symbols&#39; in map &#39;/home/administrator/src/mapnik-style/osm.xml&#39;)
renderd[17965]: An error occurred while loading the map layer &#39;default&#39;: :
ERROR:  column &quot;generator:source&quot; does not exist
LINE 8:          or (power=&#39;generator&#39; and (&quot;generator:source&quot;=&#39;wind...
                                            ^
Full sql was: &#39;SELECT * FROM 
      (select *
      from planet_osm_point
      where aeroway in (&#39;airport&#39;,&#39;aerodrome&#39;,&#39;helipad&#39;)
         or barrier in (&#39;bollard&#39;,&#39;gate&#39;,&#39;lift_gate&#39;,&#39;block&#39;)
         or highway in (&#39;mini_roundabout&#39;,&#39;gate&#39;)
         or man_made in (&#39;lighthouse&#39;,&#39;power_wind&#39;,&#39;windmill&#39;,&#39;mast&#39;)
         or (power=&#39;generator&#39; and (&quot;generator:source&quot;=&#39;wind&#39; or power_source=&#39;wind&#39;))
         or &quot;natural&quot; in (&#39;peak&#39;,&#39;volcano&#39;,&#39;spring&#39;,&#39;tree&#39;,&#39;cave_entrance&#39;)
         or railway=&#39;level_crossing&#39;
      ) as symbols LIMIT 0&#39;
 (encountered during parsing of layer &#39;amenity-symbols&#39; in map &#39;/home/administrator/src/mapnik-style/osm.xml&#39;)
renderd[17965]: An error occurred while loading the map layer &#39;default&#39;: :
ERROR:  column &quot;generator:source&quot; does not exist
LINE 8:          or (power=&#39;generator&#39; and (&quot;generator:source&quot;=&#39;wind...
                                            ^
Full sql was: &#39;SELECT * FROM 
      (select *
      from planet_osm_point
      where aeroway in (&#39;airport&#39;,&#39;aerodrome&#39;,&#39;helipad&#39;)
         or barrier in (&#39;bollard&#39;,&#39;gate&#39;,&#39;lift_gate&#39;,&#39;block&#39;)
         or highway in (&#39;mini_roundabout&#39;,&#39;gate&#39;)
         or man_made in (&#39;lighthouse&#39;,&#39;power_wind&#39;,&#39;windmill&#39;,&#39;mast&#39;)
         or (power=&#39;generator&#39; and (&quot;generator:source&quot;=&#39;wind&#39; or power_source=&#39;wind&#39;))
         or &quot;natural&quot; in (&#39;peak&#39;,&#39;volcano&#39;,&#39;spring&#39;,&#39;tree&#39;,&#39;cave_entrance&#39;)
         or railway=&#39;level_crossing&#39;
      ) as symbols LIMIT 0&#39;
 (encountered during parsing of layer &#39;amenity-symbols&#39; in map &#39;/home/administrator/src/mapnik-style/osm.xml&#39;)`</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '13, 22:28</strong></p>
<img src="https://secure.gravatar.com/avatar/0ef4fe07a4e5cc752899b3b798083ed7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gdonk&#39;s gravatar image" />
<p><span>gdonk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gdonk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20783" class="comments-container">
&#10;</div>
<div id="comment-tools-20783" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20783-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

