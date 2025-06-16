+++
type = "question"
title = "How to serve tiles from my own server?"
description = '''Hi, I have installed OSM server on Ubuntu. Now I want to use it in my applications. I want to use my local OSM server for map and not Openstreet map server. How do I serve the tiles? Any sample HTML code? I have tried code where it is referring to Openstreet map server on openstreetmap.org. How do I...'''
date = "2011-10-09T11:49:00Z"
lastmod = "2011-11-17T15:35:00Z"
weight = 8371
keywords = [ "website", "map", "server" ]
aliases = [ "/questions/8371" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to serve tiles from my own server?](/questions/8371/how-to-serve-tiles-from-my-own-server)

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
<span id="post-8371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8371-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-8371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have installed OSM server on Ubuntu. Now I want to use it in my applications. I want to use my local OSM server for map and not Openstreet map server.</p>
<p>How do I serve the tiles? Any sample HTML code? I have tried code where it is referring to Openstreet map server on <a href="http://openstreetmap.org">openstreetmap.org</a>. How do I change it to refer to localhost server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '11, 11:49</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '11, 13:10</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/b1d217a3a6e04cf4654372068beef20d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonas_&#39;s gravatar image" />
<p><span>Jonas_</span><br />
<span class="score" title="662 reputation points">662</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span></p>
</div>
</div>
<div id="comments-container-8371" class="comments-container">
&#10;</div>
<div id="comment-tools-8371" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8371-form-container" class="comment-form-container">
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

<span id="9083"></span>

<div id="answer-container-9083" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9083-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To get your own map tile server, you want <a href="http://dev.ifs.hsr.ch/redmine/projects/osminabox/wiki">OSM in a Box</a> - it does all the hard integration work for you :</p>
<ul>
<li>Configures PostgreSQL/PostGIS server</li>
<li>Creates an empty database with geospatial features - keeps all attributes in hstore</li>
<li>Configures GeoServer and tries to keep osm2gis-configuration consistent with GeoServer styling rules</li>
<li>Loads OSM data into the database</li>
<li>Incrementally updates the database</li>
<li>Produces nice maps (tiles and cached through GeoWebCache)</li>
</ul>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '11, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/733f7ff71f57fb10d9082b0c705b788f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jean_Marc%20Liotier&#39;s gravatar image" />
<p><span>Jean_Marc Li...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jean_Marc Liotier has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Nov '11, 15:36</strong> </span></p>
</div>
</div>
<div id="comments-container-9083" class="comments-container">
&#10;</div>
<div id="comment-tools-9083" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9083-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8372"></span>

<div id="answer-container-8372" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8372-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can start with the <a href="https://wiki.openstreetmap.org/wiki/OpenLayers_Simple_Example">OpenLayers simple example</a>.</p>
<p>Note the section for "Other tile sets". You have to add this code to the layer definition section, instead of the two lines for Mapnik:</p>
<pre><code>var newLayer = new OpenLayers.Layer.OSM(&quot;New Layer&quot;, &quot;URL_TO_TILES/${z}/${x}/${y}.png&quot;, {numZoomLevels: 19});
map.addLayer(newLayer);</code></pre>
<p>Just change the URL to the directory where your tiles are, and the zoom levels to how many you have. Then open it in your browser, and it should be showing your local tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '11, 12:45</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-8372" class="comments-container">
<span id="8394"></span>
<div id="comment-8394" class="comment">
<div id="post-8394-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hi, Thanks for the input. I have tried it with a single layer world tile. It is working. Now, I want to make india map tiles. Pls tell me how can I do it? I want to use India map from my server, not thro <a href="http://Openstreetmap.org">Openstreetmap.org</a> server</p>
</div>
<div id="comment-8394-info" class="comment-info">
<span class="comment-age">(11 Oct '11, 08:08)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="8418"></span>
<div id="comment-8418" class="comment">
<div id="post-8418-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi Reshma, when you have a chain of questions that go deeper in detail with each answer, you should better ask at <a href="http://forum.osm.org">forum.osm.org</a> or one of the mailing lists ... maybe there you can get detailed answers beyond any FAQ like this site is.</p>
</div>
<div id="comment-8418-info" class="comment-info">
<span class="comment-age">(11 Oct '11, 16:38)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-8372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8372-form-container" class="comment-form-container">
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

