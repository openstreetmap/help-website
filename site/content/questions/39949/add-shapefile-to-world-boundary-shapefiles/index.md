+++
type = "question"
title = "Add shapefile to world boundary shapefiles"
description = '''I want to display the Ordnance Survey National Grid as a tile layer in my android application. I&#x27;ve downloaded the grid data as various shapefiles from here: https://github.com/charlesroper/OSGB_Grids My options are to display the grid using the MapsForge library locally on the android device or to ...'''
date = "2015-01-01T10:22:00Z"
lastmod = "2015-01-04T10:07:00Z"
weight = 39949
keywords = [ "shapefile", "import" ]
aliases = [ "/questions/39949" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Add shapefile to world boundary shapefiles](/questions/39949/add-shapefile-to-world-boundary-shapefiles)

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
<span id="post-39949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39949-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to display the Ordnance Survey National Grid as a tile layer in my android application. I've downloaded the grid data as various shapefiles from here: <a href="https://github.com/charlesroper/OSGB_Grids">https://github.com/charlesroper/OSGB_Grids</a></p>
<p>My options are to display the grid using the MapsForge library locally on the android device or to import the grid data into my tileserver (setup using the Switch2OSM tutorial). I've decided to use my tileserver.</p>
<p>So far i've tried:</p>
<ul>
<li><p>Converting the shapefile grid data to osm (xml) format using JOSM and then importing the osm data to my tileserver using osm2pgsql. This fails to import anything, i suspect the osm tags are not recognised by osm2pgsql.</p></li>
<li><p>Converting the shapefile grid data to osm (xml) format using Merkaator and then importing the osm data to my tileserver using osm2pgsql. This fails with osm2pgswl reporting many 'BoundingBox' tag not recognised errors.</p></li>
</ul>
<p>I've also tried using shp2pgsql but my skills are not sufficient to understand the instructions :(.</p>
<p>Anyway i had an idea - can't i simply add my grid shapefile to the tileserver's existing shapefiles and then let mapnik/tile_mod render the shapefile data along with the existing shapefile data? That is render the shapefile directly without importing it into PostgreSQL.</p>
<p>So i uploaded my grid shapefiles to my server, uploading them to the directory /usr/local/share/world_boundaries. I restarted the tileserver and looked at the slippymap.html map - no sign of my os grid on the rendered tiles.</p>
<p>Can anyone suggest how i'd add my os grid shapefile to my tileserver so that it's rendered along with the existing world boundary shapefile data?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jan '15, 10:22</strong></p>
<img src="https://secure.gravatar.com/avatar/fc25b1c88a406013979438b60ab69e2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="warwound&#39;s gravatar image" />
<p><span>warwound</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="warwound has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39949" class="comments-container">
<span id="39950"></span>
<div id="comment-39950" class="comment">
<div id="post-39950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The shapefiles are in OSGB36 projection, ESPG:27700, for osm2pgsql they need to be in WGS84 (ESPG:43260). However JOSM should manage the conversion, so you need to tell us what tags you have on the grid data. Even then you need some kind of rendering rules to pull them into a your tiles.</p>
</div>
<div id="comment-39950-info" class="comment-info">
<span class="comment-age">(01 Jan '15, 11:23)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="40008"></span>
<div id="comment-40008" class="comment">
<div id="post-40008-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My goal is for my tileserver to serve semi transparent tiles which contain <em>nothing but the grid data</em>. I'll display these tiles as a tile overlay in my android application on top of the existing map tiles. So i'd display say Google's road map or satellite map tiles with my grid tiles on top.</p>
<p>For this project i don't want to display any OSM data rendered from PostgresSQL and i don't want to display the existing world boundary shapefile data. I just want a transparent tile with the grid data rendered onto it.</p>
<p>Is that possible?</p>
<p>How can i reconfigure my tileserver so that it renders just the grid shapefile and nothing else?</p>
</div>
<div id="comment-40008-info" class="comment-info">
<span class="comment-age">(04 Jan '15, 07:46)</span> <span class="comment-user userinfo">warwound</span>
</div>
</div>
</div>
<div id="comment-tools-39949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39949-form-container" class="comment-form-container">
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

<span id="39951"></span>

<div id="answer-container-39951" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39951-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-39951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>shp2pgsql is pretty simple. You'd usually run it like this:</p>
<pre><code>shp2pgsql -s 4326 -I myshapefile.shp table_name | psql -d database_name -q</code></pre>
<p>That will import myshapefile.shp into database <code>database_name</code>, creating a new table called <code>table_name</code>.</p>
<p>The number after -s is the EPSG code for the projection. 4326 is raw latitude and longitude, i.e. not really projected at all. The code for OSGB (the National Grid) is 27700. So if you use <code>-s 27700</code>, that will read a shapefile in OSGB, and store it in the database like that.</p>
<p>Alternatively, you might want to reproject on import - that is, read an OSGB shapefile, but store it in 4326 (or something else). That's easy too - just separate the two projections with a colon:</p>
<pre><code>shp2pgsql -s 27700:4326 -I myshapefile.shp table_name | psql -d database_name -q</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jan '15, 12:28</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-39951" class="comments-container">
&#10;</div>
<div id="comment-tools-39951" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39951-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40010"></span>

<div id="answer-container-40010" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40010-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've now found the various .xml.inc files located in the mapnik-styles/inc directory.</p>
<p>I updated layers.xml.inc adding a new entry:</p>
<p>&lt;!ENTITY layer-osgrid SYSTEM "layer-osgrid.xml.inc"&gt;</p>
<p>Then i created the file layer-osgrid.xml.inc:</p>
<p>&lt;Style name="osgrid"&gt; &lt;Rule&gt; &amp;maxscale_zoom4; &amp;minscale_zoom16; &lt;LineSymbolizer stroke-linejoin="round" stroke="grey" stroke-width="4" stroke-opacity="0.8"/&gt; &lt;/Rule&gt; &lt;/Style&gt; &lt;Layer name="osgrid" status="on" srs="&amp;srs27700;"&gt; &lt;StyleName&gt;osgrid&lt;/StyleName&gt; &lt;Datasource&gt; &lt;Parameter name="type"&gt;shape&lt;/Parameter&gt; &lt;Parameter name="file"&gt;&amp;world_boundaries;/OSGB_Grid_1km&lt;/Parameter&gt; &lt;/Datasource&gt; &lt;/Layer&gt;</p>
<p>In my world_boundaries directory i uploaded the OSGB_Grid_1km.shp grid shapefile. I also used shapeindex to create an index file for OSGB_Grid_1km.shp.</p>
<p>Lastly i ran this command:</p>
<p>python generate_xml.py --dbname gis --world_boundaries "/usr/local/share/world_boundaries" --accept-none</p>
<p>I deleted all cached tiles and restarted my tileserver hoping to see some grids rendered on the tiles but nothing gets rendered.</p>
<p>I'll experiment more later...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '15, 10:07</strong></p>
<img src="https://secure.gravatar.com/avatar/fc25b1c88a406013979438b60ab69e2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="warwound&#39;s gravatar image" />
<p><span>warwound</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="warwound has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40010" class="comments-container">
&#10;</div>
<div id="comment-tools-40010" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40010-form-container" class="comment-form-container">
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

