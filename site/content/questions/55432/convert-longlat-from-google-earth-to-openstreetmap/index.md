+++
type = "question"
title = "Convert Long/Lat from Google Earth to OpenStreetMap"
description = '''Hi Folks I&#x27;m trying to create a map based on a tutorial I found. The tutorial has a piece of code for the start point; // define point as a new LonLat object and transfom  point = new OpenLayers.LonLat(-4.225, 57.478);  point.transform(&quot;EPSG:4326&quot;, &quot;EPSG:3857&quot;); I can follow what this code does but ...'''
date = "2017-04-02T11:24:00Z"
lastmod = "2017-04-02T16:01:00Z"
weight = 55432
keywords = [ "openstreetmap", "coordinates", "google_maps" ]
aliases = [ "/questions/55432" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Convert Long/Lat from Google Earth to OpenStreetMap](/questions/55432/convert-longlat-from-google-earth-to-openstreetmap)

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
<span id="post-55432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55432-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Folks</p>
<p>I'm trying to create a map based on a tutorial I found. The tutorial has a piece of code for the start point;</p>
<p>// define point as a new LonLat object and transfom point = new OpenLayers.LonLat(-4.225, 57.478); point.transform("EPSG:4326", "EPSG:3857");</p>
<p>I can follow what this code does but it centers the map in Scotland. I'm looking to center it in Dublin. In Google Earth the coordinates I want are 53.285756, -6.141998. But when I put that in, OpenStreetMap sends me to somewhere near the Seychelles. Can you help with how I can convert it correctly? I'm a beginners so apologies if I've not explained it correctly. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-google_maps" rel="tag" title="see questions tagged &#39;google_maps&#39;">google_maps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Apr '17, 11:24</strong></p>
<img src="https://secure.gravatar.com/avatar/17488b314c589d0c511ccb92ab6de2be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shane_Ire&#39;s gravatar image" />
<p><span>Shane_Ire</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shane_Ire has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55432" class="comments-container">
<span id="55434"></span>
<div id="comment-55434" class="comment">
<div id="post-55434-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Perhaps you could explain a little more fully what it is you're trying to do when you say "create a map."</p>
<p>Which program or website are you plugging the coordinates into?</p>
<p>When I put 53.285756, -6.141998 into JOSM, the OSM editor program, it takes me to a golf course in Dublin, so the coordinates are reasonably accurate.</p>
<p>Cheers</p>
<p>Dave</p>
</div>
<div id="comment-55434-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 11:42)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="55435"></span>
<div id="comment-55435" class="comment">
<div id="post-55435-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Dave</p>
<p>I'm only just learning Web based GIS. So here are the details. I have GeoServer 2.8.2 hosted on a VM. It is also the webserver. I have a simple HTML page calling OpenLayers and a .js file.</p>
<p>&lt;script src="http://www.openlayers.org/api/OpenLayers.js"&gt;&lt;/script&gt; &lt;script type="text/JavaScript" src="map.js"&gt;&lt;/script&gt;</p>
<p>In the .js file I am using OpenLayer and OSM;</p>
<p>//create new map object map = new OpenLayers.Map("mymap");</p>
<pre><code>//create new OSM base layer
osmlayer = new OpenLayers.Layer.OSM(&quot;Open Street Map&quot;);
&#10;//create WMS layers</code></pre>
<p>When I enter this code and open the page via <a href="http://localhost:8080/geoserver/www/index.html.">http://localhost:8080/geoserver/www/index.html.</a> It opens off the coast of Africa.</p>
<p>// define point as a new LonLat object and transform point = new OpenLayers.LonLat(53.285756, -6.141998); //point.transform("EPSG:4326", "EPSG:3857");</p>
<p>As I say, I'm new to this so might not be explaining it well. Thanks</p>
</div>
<div id="comment-55435-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 12:08)</span> <span class="comment-user userinfo">Shane_Ire</span>
</div>
</div>
<span id="55438"></span>
<div id="comment-55438" class="comment">
<div id="post-55438-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the information. This list is watched by many smart OSM folks who can possibly help and I'm sure you'll get some answers shortly. But I'm afraid I can't be of much help because I have no expertise in the area you're addressing.</p>
<p>Best,</p>
<p>Dave</p>
</div>
<div id="comment-55438-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 12:15)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="55443"></span>
<div id="comment-55443" class="comment">
<div id="post-55443-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you mixing up latitude and longitude? <code>OpenLayers.LonLat()</code> requires longitude first, then latitude (as the name of the function already indicates).</p>
</div>
<div id="comment-55443-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 14:22)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="55444"></span>
<div id="comment-55444" class="comment">
<div id="post-55444-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Dave, sorted it. Had to clear out Internet cache.</p>
</div>
<div id="comment-55444-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 14:32)</span> <span class="comment-user userinfo">Shane_Ire</span>
</div>
</div>
<span id="55451"></span>
<div id="comment-55451" class="comment not_top_scorer">
<div id="post-55451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For Info i cut and paste your coords in OSMs search box and got this <a href="http://www.openstreetmap.org/search?query=53.285756%2C%20-6.141998#map=16/53.2858/-6.1420">http://www.openstreetmap.org/search?query=53.285756%2C%20-6.141998#map=16/53.2858/-6.1420</a></p>
</div>
<div id="comment-55451-info" class="comment-info">
<span class="comment-age">(02 Apr '17, 16:01)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-55432" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-55432-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

