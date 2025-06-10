+++
type = "question"
title = "How to download rendered OSM maps?"
description = '''What is the best way to download the tiles, I tried to download a specific region using XAPI, for example: http://xapi.openstreetmap.org/api/0.6/map?bbox=11.54, 48.14,11.543,48.145 but I could not download. I need to download the maps rendered to load on my database for use with Open Layers.'''
date = "2010-07-16T06:42:00Z"
lastmod = "2014-11-01T10:16:00Z"
weight = 242
keywords = [ "download", "rendering", "tiles" ]
aliases = [ "/questions/242" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [How to download rendered OSM maps?](/questions/242/how-to-download-rendered-osm-maps)

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
<span id="post-242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-242-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the best way to download the tiles, I tried to download a specific region using XAPI, for example: <a href="http://xapi.openstreetmap.org/api/0.6/map?bbox=11.54">http://xapi.openstreetmap.org/api/0.6/map?bbox=11.54</a>, 48.14,11.543,48.145 but I could not download. I need to download the maps rendered to load on my database for use with Open Layers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '10, 06:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f5d1f6984463f23078c730c4e31c91b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leo2gz&#39;s gravatar image" />
<p><span>leo2gz</span><br />
<span class="score" title="59 reputation points">59</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leo2gz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>13 Nov '10, 17:02</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-242" class="comments-container">
<span id="260"></span>
<div id="comment-260" class="comment">
<div id="post-260-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This question is very confused - you ask about downloading tiles which implies that you're talking about rendered maps but then start talking about using XAPI which will give you raw data.</p>
</div>
<div id="comment-260-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 13:31)</span> <span class="comment-user userinfo">TomH ♦♦</span>
</div>
</div>
</div>
<div id="comment-tools-242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-242-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="243"></span>

<div id="answer-container-243" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-243-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="leo2gz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The XAPI can serve you the raw OSM data in XML format. That means that the data is NOT in any image format that you can easily view.</p>
<p>Rendering of rendered image tiles is possible. If you want to use the tiles from the main slippy map which are rendered with mapnik you need to read, understand and follow <a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy"></a><a href="http://wiki.openstreetmap.org"></a><a href="http://wiki.openstreetmap.org">wiki.openstreetmap.org</a>/wiki/Tile_usage_policy. The tiles from the tiles@home layer rendered with osmarender are not limited in this way as they are preprendered.</p>
<p>Other tile provider like cloudmade, cyclemap or other have their own usage policies, so if you want to use them you have to find out yourself what kind of usage is acceptable. Please understand that this is not a arbittrary restriction to annoy you, but many map, especially special topic maps, are produced on donated hardware with limited resources and simply can't produce the tiles fast enough to feed large batch downloads.</p>
<p>Note that rendered images are (normally) not stored in a database but directly in a set of folders on your harddisk. A database is only used if you want fast access to raw OSM data. In that case you can load the OpenStreetMap data obtained in XML format into a database with a suitable structure.</p>
<p>And a last remark: If you only want to create a website with openlayers you don't necessarily need to host the image tiles yourself. You can point your openlayers installation at the regular tiles servers. As long as the visitor of your website dont create hundreds of requests per second to the tile servers, nobody will object to this usage.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '10, 06:58</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-243" class="comments-container">
<span id="245"></span>
<div id="comment-245" class="comment">
<div id="post-245-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So if i want to load the OSM data (xml format) in my Database. then i have to render with mapnik or osmarender?</p>
</div>
<div id="comment-245-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 07:12)</span> <span class="comment-user userinfo">leo2gz</span>
</div>
</div>
<span id="246"></span>
<div id="comment-246" class="comment">
<div id="post-246-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you want to render the data yourself using Mapnik you should probably load the data into a database, yes. Mapnik can render the data straight from a file too, but the standard OSM stylesheet doesn't handle the case. So unless you want to write your own stylesheet from scratch loading the data into a DB using osm2pgsql.</p>
<p>Osmarender renders OSM data straight from the OSM data in XML format. However you should not feed it the whole world in one big file.</p>
<p>As I don't know how large a region you want to render and how often you want to update it, it's hard to give precise advice.</p>
</div>
<div id="comment-246-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 07:44)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="267"></span>
<div id="comment-267" class="comment">
<div id="post-267-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would only be needed on a city map to trace the routes of transport. How could I do that.</p>
</div>
<div id="comment-267-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 17:26)</span> <span class="comment-user userinfo">leo2gz</span>
</div>
</div>
<span id="269"></span>
<div id="comment-269" class="comment">
<div id="post-269-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you only need a single map of the whole city or do you need tiles (portions of the city at different zoomlevel) so you can pan and zoom on your website?</p>
</div>
<div id="comment-269-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 18:04)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="271"></span>
<div id="comment-271" class="comment">
<div id="post-271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I need a map of a city but with Different zoomlevel (tiles), pan and zoom on my website. for example OSM transport. How could I work with the maps?</p>
</div>
<div id="comment-271-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 18:48)</span> <span class="comment-user userinfo">leo2gz</span>
</div>
</div>
<span id="272"></span>
<div id="comment-272" class="comment not_top_scorer">
<div id="post-272-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In that case you want to make the mapdisplay using openlayers. Either feed it with the standard tiles and overlay a vector layer, or render you own tiles. For that you can use mapnik or osmarender. Osmarender will be more fiddling with small programms and tool, mapnik will need a database filled with the data for that city. Read up on both in the wiki and then ask more specific questions.</p>
<p>I probably wont answer with more details as we are drifting away from the orginal question.</p>
</div>
<div id="comment-272-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 19:11)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-243" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-243-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="244"></span>

<div id="answer-container-244" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-244-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>the xapi is AFAIK only for the data... so it doesn't serve the tiles... if you want to hav the tiles you have to render the data.</p>
<p>if you mean: how can I download the regional data: maybe that helps: <a href="http://download.geofabrik.de/osm/">http://download.geofabrik.de/osm/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '10, 06:58</strong></p>
<img src="https://secure.gravatar.com/avatar/db9d4c9ffd75f95f97122bbc97b90a64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="josias&#39;s gravatar image" />
<p><span>josias</span><br />
<span class="score" title="598 reputation points">598</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="josias has 3 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-244" class="comments-container">
&#10;</div>
<div id="comment-tools-244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-244-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1539"></span>

<div id="answer-container-1539" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1539-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One way is to use <a href="http://maperitive.net">Maperitive</a>. Steps:</p>
<ol>
<li>Download OSM data from XAPI (using the <code>download-osm</code> command). Or, if you already have an OSM XML file, load it using the <a href="http://maperitive.net/docs/manual/Commands/LoadSource.html"><code>load-source</code> command</a>.</li>
<li>Turn off the existing Web map layer (click on the yellow star in the bottom right corner).</li>
<li>Generate tiles using the <a href="http://maperitive.net/docs/manual/Commands/GenerateTiles.html"><code>generate-tiles</code> command</a>.</li>
</ol>
<p>The generated tiles are OpenLayers-compatible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '10, 17:08</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-1539" class="comments-container">
<span id="1542"></span>
<div id="comment-1542" class="comment">
<div id="post-1542-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@Vclaw: if you vote down answers, at least provide a reason for doing so.</p>
</div>
<div id="comment-1542-info" class="comment-info">
<span class="comment-age">(14 Nov '10, 07:07)</span> <span class="comment-user userinfo">Breki</span>
</div>
</div>
</div>
<div id="comment-tools-1539" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1539-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1522"></span>

<div id="answer-container-1522" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1522-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-1522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello this is shushak.....</p>
<p>Thanks for your great answers.....</p>
<p>but my problem is something different... i am able to generate tiles from .osm files.... but i want to generate tiles of my own country because world tiles generation takes very long time..... bu when i try to generate tiles of my country using coordinates(bbox) &amp; my country .osm file.... it generate empty tiles for rest of the world which takes same time as planet.osm takes....</p>
<p>Is there any way to generate tiles of my own country with leaving empty tiles....</p>
<p>I am also found another way to download tiles but due to slow net connection this method also fails....</p>
<p>I there any way to do that plz tell me i want to learn this....</p>
<p>sorry for any grammatical or spelling mistake i am a new baby... thanks to you for showing interest<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '10, 08:25</strong></p>
<img src="https://secure.gravatar.com/avatar/3b475b3db92f5a6f627ffbdf8672de6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shushank%20Sharma&#39;s gravatar image" />
<p><span>Shushank Sharma</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shushank Sharma has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-1522" class="comments-container">
<span id="1524"></span>
<div id="comment-1524" class="comment">
<div id="post-1524-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is a separate question and you should post it as such, rather than piggybacking onto the end of someone else's question.</p>
</div>
<div id="comment-1524-info" class="comment-info">
<span class="comment-age">(11 Nov '10, 12:06)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="1527"></span>
<div id="comment-1527" class="comment">
<div id="post-1527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Shushank, you can ask your new questions maybe better at <a href="http://forum.openstreetmap.org">http://forum.openstreetmap.org</a></p>
</div>
<div id="comment-1527-info" class="comment-info">
<span class="comment-age">(11 Nov '10, 16:56)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-1522" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1522-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38222"></span>

<div id="answer-container-38222" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38222-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-38222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Why downloading tiles, if you can easily render your map from original osm data with <a href="http://sourceforge.net/projects/topomapcreator/">TopoMapCreator</a>?</p>
<p><a href="http://sourceforge.net/p/topomapcreator/wiki/ExtendedMapCreator">ExtendedMapCreator</a> is a Desktop-Program, that creates "Topographic Maps" from OSM, NASA and ESA. You simply define a map extent by dragging over a browsable word map, click on start and wait till the GeoTIFF, ECW, GALILEO, ORUXMAPS or NAVIMAP files got created. ExtendedMapCreator is based on the Mapnik-Renderer, nevertheless all data downloading and processing is fully automatic.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '14, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/6c696b469aba99282f03a4a1f33528b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kaki007&#39;s gravatar image" />
<p><span class="suspended-user">kaki007</span><br />
(suspended)<br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kaki007 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38222" class="comments-container">
&#10;</div>
<div id="comment-tools-38222" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38222-form-container" class="comment-form-container">
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

