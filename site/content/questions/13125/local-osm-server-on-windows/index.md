+++
type = "question"
title = "Local OSM server on windows"
description = '''Hello all! Is there a way to make all these possible:  - users want to view the map using desktop Java appliation with some moving markers on it - markers can report their positions in real time and desktop application can handle it;  - users want an application to have routing functionality;  - use...'''
date = "2012-05-30T16:00:00Z"
lastmod = "2017-01-28T22:53:00Z"
weight = 13125
keywords = [ "windows", "jmapviewer", "offline", "java", "server" ]
aliases = [ "/questions/13125" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Local OSM server on windows](/questions/13125/local-osm-server-on-windows)

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
<span id="post-13125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13125-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all!<br />
Is there a way to make all these possible:<br />
- users want to view the map using desktop Java appliation with some moving markers on it - markers can report their positions in real time and desktop application can handle it;<br />
- users want an application to have routing functionality;<br />
- users also want to edit the map - add/delete some specific information;<br />
- users <em>does not have a possibility to download the map from the internet every time</em>.<br />
</p>
<p>As far as I understood, fisrt I need to do is to set up a local map server:<br />
- download the area users interested in from <a href="http://planet.openstreetmap.org">planet.openstreetmap.org</a> into local <strong>.osm</strong> file;<br />
- edit downloaded <strong>.osm</strong> file in <a href="http://josm.openstreetmap.de">JOSM</a> editor;<br />
- set up <a href="http://www.postgresql.org">PostreSQL</a>;<br />
- set up <a href="http://www.postgis.org">PostGIS</a> extension to PostgreSQL;<br />
- import local (edited) <strong>.osm</strong> file into PostgreSQL using <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a>;<br />
- set up <a href="www.mapnik.org">Mapnik</a> to generate tiles from PostgreSQL/PostGIS;<br />
- set up <a href="http://httpd.apache.org">Apache Web Server</a> with <a href="https://wiki.openstreetmap.org/wiki/Mod_tile">mod_tile</a>;<br />
- create Java desktop (Swing) application with <a href="https://wiki.openstreetmap.org/wiki/JMapViewer">JMapViewer</a> component.<br />
</p>
<p>If I put down everything correctly <strong>:)</strong>, I want to ask some questions:<br />
- is described way correct? or there is some other (simpler) ways to do that - may be to use <strong>Shapefiles</strong> and <a href="http://geotools.org">geotools</a> instead of Mapnik?<br />
- how to set up Apache+Mapnik+PostGIS on <strong>Windows</strong> to make it a tile server for JMapViewer like <a href="http://tile.openstreetmap.org">tile.openstreetmap.org</a> - I could not find any tutorial?<br />
</p>
<p>Thank you all in advance for answers!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-jmapviewer" rel="tag" title="see questions tagged &#39;jmapviewer&#39;">jmapviewer</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '12, 16:00</strong></p>
<img src="https://secure.gravatar.com/avatar/9c1fedf457d99dba83a94061550ab814?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pau-osm&#39;s gravatar image" />
<p><span>pau-osm</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pau-osm has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-13125" class="comments-container">
<span id="16495"></span>
<div id="comment-16495" class="comment">
<div id="post-16495-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you get this working? I am looking to do something similar but without the routing/map editing. Most important to me is getting a real time marker representing a users location, the data will be pushed/pulled into the application from a smartphone</p>
</div>
<div id="comment-16495-info" class="comment-info">
<span class="comment-age">(27 Sep '12, 14:00)</span> <span class="comment-user userinfo">jamescross91</span>
</div>
</div>
<span id="16503"></span>
<div id="comment-16503" class="comment">
<div id="post-16503-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, unfortunately not. I only can store tiles localy using maperitive.net and then make JMapViewer to read them instead of reading openstreetmap.org ... But JMapViewer has MapMarker interface which you can use to draw everything you need</p>
</div>
<div id="comment-16503-info" class="comment-info">
<span class="comment-age">(27 Sep '12, 19:16)</span> <span class="comment-user userinfo">pau-osm</span>
</div>
</div>
</div>
<div id="comment-tools-13125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13125-form-container" class="comment-form-container">
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

<span id="13126"></span>

<div id="answer-container-13126" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13126-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pau-osm has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To generate map tiles on Windows you can use <a href="http://maperitive.net/">Maperative</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '12, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span> </br></br></p>
</div>
</div>
<div id="comments-container-13126" class="comments-container">
<span id="13127"></span>
<div id="comment-13127" class="comment">
<div id="post-13127-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>but tiles themselves does not provide me with the routing functionality (am I right?), the only help me to view the map in a fast way; and users can not add some specific info on the map (tile), genereated by Maperative ... so, this is unfortunatelly not the way for me to use OSM ...</p>
</div>
<div id="comment-13127-info" class="comment-info">
<span class="comment-age">(30 May '12, 17:08)</span> <span class="comment-user userinfo">pau-osm</span>
</div>
</div>
<span id="13128"></span>
<div id="comment-13128" class="comment">
<div id="post-13128-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Routing is a very different problem from displaying a map and not one that is tackled very often. There is more information here: <a href="https://wiki.openstreetmap.org/wiki/Routing">https://wiki.openstreetmap.org/wiki/Routing</a> A tool to create maps or map tiles will usually be separate from the tool that displays the maps tiles and a different tool will handle routing, probably providing an overlay drawn over the map tiles. Using Maperative or Mapnik (or anything else) to render the map is not going to provide routing, just the place to display the calculated route.</p>
<p>Of course, you might create a wonderful app that does everything.</p>
</div>
<div id="comment-13128-info" class="comment-info">
<span class="comment-age">(30 May '12, 17:28)</span> <span class="comment-user userinfo">ChrisH</span>
</div>
</div>
<span id="13164"></span>
<div id="comment-13164" class="comment">
<div id="post-13164-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried Maperitive to render the map tiles and JMapViewer to view them - everithing is fine, I liked it. So, thank you very much to make me thinking that way :) Now, it is time to find routing solution ...</p>
</div>
<div id="comment-13164-info" class="comment-info">
<span class="comment-age">(31 May '12, 16:45)</span> <span class="comment-user userinfo">pau-osm</span>
</div>
</div>
<span id="54341"></span>
<div id="comment-54341" class="comment">
<div id="post-54341-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I have Geoserver for my web map service, and I need serve map tiles generated by Maperitive. Did you use any tileserver for them or serve them directly from Geoserver or other map server?</p>
</div>
<div id="comment-54341-info" class="comment-info">
<span class="comment-age">(28 Jan '17, 22:53)</span> <span class="comment-user userinfo">mathew95</span>
</div>
</div>
</div>
<div id="comment-tools-13126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13126-form-container" class="comment-form-container">
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

