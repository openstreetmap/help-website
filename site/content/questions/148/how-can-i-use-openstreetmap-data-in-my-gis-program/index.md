+++
type = "question"
title = "How can I use OpenStreetMap data in my GIS program?"
description = '''OpenStreetMap has a lot of great data which I&#x27;d like to be able to use in my GIS program. How would I go about downloading the data in shapefile format or another common GIS data file format?'''
date = "2010-07-12T20:24:00Z"
lastmod = "2013-11-16T19:23:00Z"
weight = 148
keywords = [ "shapefile", "data", "download", "gis" ]
aliases = [ "/questions/148" ]
osqa_answers = 6
osqa_accepted = false
+++

<div class="headNormal">

# [How can I use OpenStreetMap data in my GIS program?](/questions/148/how-can-i-use-openstreetmap-data-in-my-gis-program)

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
<span id="post-148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-148-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OpenStreetMap has a lot of great data which I'd like to be able to use in my GIS program. How would I go about downloading the data in shapefile format or another common GIS data file format?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '10, 20:24</strong></p>
<img src="https://secure.gravatar.com/avatar/f0051830201ed06e6023fe692c49a2eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dankarran&#39;s gravatar image" />
<p><span>dankarran</span><br />
<span class="score" title="121 reputation points">121</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dankarran has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-148" class="comments-container">
<span id="23291"></span>
<div id="comment-23291" class="comment">
<div id="post-23291-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A fair few of the points made in answers to this question are outdated and need revision (particularly with respect to Quantum GIS).</p>
</div>
<div id="comment-23291-info" class="comment-info">
<span class="comment-age">(12 Jun '13, 22:09)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-148" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-148-form-container" class="comment-form-container">
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

6 Answers:

</div>

</div>

<span id="149"></span>

<div id="answer-container-149" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-149-score" class="post-score" title="current number of votes">
15
</div>
<span id="post-149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can download prepared shapefiles of OpenStreetMap data from <a href="http://downloads.cloudmade.com/">Cloudmade</a> or <a href="http://download.geofabrik.de/osm/">Geofabrik</a>, two companies providing specialist OSM-based services. Shape files for small areas can be extracted directly on the <a href="http://extract.bbbike.org/">BBBike</a> site, but please don't abuse this facility when suitable extracts are available elsewhere.</p>
<p>It's also possible to create PostGIS databases of OpenStreetMap data using either <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a> or <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>, which will give you greater control over the types of features included, but is a more complicated procedure.</p>
<p>Some GIS are starting to provide native support for OpenStreetMap XML data, including <a href="https://wiki.openstreetmap.org/wiki/ArcGIS">ArcGIS</a> and <a href="https://wiki.openstreetmap.org/wiki/QGIS">Quantum GIS</a>, but these are at an early stage of development and may not work as reliably as importing shapefiles yet. At present (June 2012) the QGIS OSM plugin is no longer supported, and requires workarounds in order to use OSM Data (see answers to <a href="/questions/21078/my-lines-and-polygons-have-turned-to-nodes-when-exported-as-osm-xml-data-and-imported-into-qgis">this question</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '10, 20:40</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jun '13, 23:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-149" class="comments-container">
&#10;</div>
<div id="comment-tools-149" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-149-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="151"></span>

<div id="answer-container-151" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-151-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>ESRI have an open source extension for ArcGIS that will read and edit OSM data.</p>
<p>More information: <a href="http://www.esri.com/news/releases/10_3qtr/openstreetmap.html">ArcGIS extension</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '10, 22:10</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-151" class="comments-container">
&#10;</div>
<div id="comment-tools-151" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-151-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="150"></span>

<div id="answer-container-150" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-150-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can also download OSM data straight into <a href="http://www.qgis.org/" title="QGIS">QGIS</a>, either via the api or by opening .osm files. This <a href="http://mapperz.blogspot.com/2009/11/openstreetmap-data-on-demand-with.html">guide</a> is a little old, but you get the idea.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '10, 22:06</strong></p>
<img src="https://secure.gravatar.com/avatar/50ac30a0553308fb00e6ac3126224239?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IknowJoseph&#39;s gravatar image" />
<p><span>IknowJoseph</span><br />
<span class="score" title="226 reputation points">226</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IknowJoseph has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-150" class="comments-container">
<span id="15911"></span>
<div id="comment-15911" class="comment">
<div id="post-15911-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've just been setting up more info on the QGIS plugin: <a href="https://wiki.openstreetmap.org/wiki/QGIS_OSM_Plugin">https://wiki.openstreetmap.org/wiki/QGIS_OSM_Plugin</a> For some reason it took me a while to find this: <a href="http://docs.qgis.org/user_guide/html/en/plugins/plugins_openstreetmap.html">http://docs.qgis.org/user_guide/html/en/plugins/plugins_openstreetmap.html</a></p>
</div>
<div id="comment-15911-info" class="comment-info">
<span class="comment-age">(09 Sep '12, 04:35)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
</div>
<div id="comment-tools-150" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-150-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7611"></span>

<div id="answer-container-7611" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7611-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A complete solution for using OpenStreetMap data in QGIS is described here:</p>
<p><a href="http://www.qgis.org/wiki/OpenStreetMap_data_rendered_with_QGIS">http://www.qgis.org/wiki/OpenStreetMap_data_rendered_with_QGIS</a> <a href="http://www.qgis.org/wiki/Using_OpenStreetMap_data">http://www.qgis.org/wiki/Using_OpenStreetMap_data</a> <a href="https://wiki.openstreetmap.org/wiki/Osm2postgresql">https://wiki.openstreetmap.org/wiki/Osm2postgresql</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '11, 15:56</strong></p>
<img src="https://secure.gravatar.com/avatar/6d2cc30e4deb919dc2493457f2491d32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mayeul&#39;s gravatar image" />
<p><span>Mayeul</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mayeul has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Sep '11, 18:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span></p>
</div>
</div>
<div id="comments-container-7611" class="comments-container">
&#10;</div>
<div id="comment-tools-7611" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7611-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28155"></span>

<div id="answer-container-28155" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28155-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The GIS software <a href="https://wiki.openstreetmap.org/wiki/OpenJUMP">OpenJUMP</a> has a feature to import OSM data directly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '13, 19:23</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-28155" class="comments-container">
&#10;</div>
<div id="comment-tools-28155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28155-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27107"></span>

<div id="answer-container-27107" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27107-score" class="post-score" title="current number of votes">
-7
</div>
<span id="post-27107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can try to use (software name removed) from (URL removed) to downlaod Openstreet Maps to disk and create ESRI world file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Oct '13, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/d3e5b3415d5beb0d6eeda4a77b88f05a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mark_879&#39;s gravatar image" />
<p><span>Mark_879</span><br />
<span class="score" title="-5 reputation points">-5</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mark_879 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '13, 11:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-27107" class="comments-container">
<span id="27108"></span>
<div id="comment-27108" class="comment">
<div id="post-27108-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This will get you blocked from using the tile servers pretty quickly for breaking the usage policy. Don't do this.</p>
</div>
<div id="comment-27108-info" class="comment-info">
<span class="comment-age">(12 Oct '13, 14:48)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
<span id="27111"></span>
<div id="comment-27111" class="comment">
<div id="post-27111-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But it says: You are free to copy, distribute, transmit and adapt our data, as long as you credit OpenStreetMap and its contributors. If you alter or build upon our data, you may distribute the result only under the same licence....</p>
</div>
<div id="comment-27111-info" class="comment-info">
<span class="comment-age">(12 Oct '13, 15:09)</span> <span class="comment-user userinfo">Mark_879</span>
</div>
</div>
<span id="27112"></span>
<div id="comment-27112" class="comment">
<div id="post-27112-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Downloading (ripping or scraping) tiles is not the same as using the data. The tile server is there to support people editing the map and is easily swamped by scraping tiles. You can freely download the data or parts of it; more info here: <a href="http://planet.openstreetmap.org/">http://planet.openstreetmap.org/</a></p>
</div>
<div id="comment-27112-info" class="comment-info">
<span class="comment-age">(12 Oct '13, 15:23)</span> <span class="comment-user userinfo">ChrisH</span>
</div>
</div>
<span id="27121"></span>
<div id="comment-27121" class="comment">
<div id="post-27121-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As <a href="http://wiki.osm.org/wiki/Tile_Usage_Policy">http://wiki.osm.org/wiki/Tile_Usage_Policy</a> explains: "OpenStreetMap data is free for everyone to use. Our tile servers are not."</p>
</div>
<div id="comment-27121-info" class="comment-info">
<span class="comment-age">(13 Oct '13, 11:51)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27107" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27107-form-container" class="comment-form-container">
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

