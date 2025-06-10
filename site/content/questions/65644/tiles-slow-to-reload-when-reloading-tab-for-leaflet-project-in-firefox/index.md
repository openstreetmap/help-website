+++
type = "question"
title = "Tiles slow to reload when reloading tab for Leaflet project in Firefox"
description = '''I&#x27;m unsure this is a direct Leaflet problem, but hope some can help. I&#x27;m developing a webpage. The file are stored on my local drive. I click on the .html file &amp;amp; it loads into Firefox &amp;amp; displays in the expected amount of time. When I amend the html file I reload the Firefox tab by right clic...'''
date = "2018-08-30T15:00:00Z"
lastmod = "2018-08-30T15:00:00Z"
weight = 65644
keywords = [ "leaflet", "firefox", "tileserver" ]
aliases = [ "/questions/65644" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tiles slow to reload when reloading tab for Leaflet project in Firefox](/questions/65644/tiles-slow-to-reload-when-reloading-tab-for-leaflet-project-in-firefox)

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
<span id="post-65644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65644-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm unsure this is a direct Leaflet problem, but hope some can help.</p>
<p>I'm developing a webpage. The file are stored on my local drive. I click on the .html file &amp; it loads into Firefox &amp; displays in the expected amount of time. When I amend the html file I reload the Firefox tab by right clicking on it. The tiles (http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png) take seconds, even minutes to load. There's a message in the bottom left Transferring data form (a or b.or c).tile.openstreemap.org.</p>
<p>This occurred using different versions of leaflet &amp; Firefox over many months. It doesn't occur in IE 11.</p>
<p>I've tried other tilelayer (https://{s}.tile.openstreetmap.se/hydda/full/{z}/{x}/{y}.png) &amp; it works fine. There are no delays on the main OSM site when zooming/panning.</p>
<p>Base Code I used (badly formatted by this help site)</p>
<p>&lt;head&gt; &lt;title&gt;Base 1_34&lt;/title&gt; &lt;meta charset="utf-8"/&gt; &lt;link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.4/dist/leaflet.css"/&gt; &lt;script src="https://unpkg.com/leaflet@1.3.4/dist/leaflet.js"&gt;&lt;/script&gt; &lt;style&gt; body {padding: 0;margin: 0;} html, body, #map {height: 100%;width: 100%;} &lt;/style&gt; &lt;/head&gt; &lt;body&gt;</p>
<div>
&#10;</div>
&lt;script&gt; var osm = new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {opacity: 0.7}); var map = new L.Map('map').addLayer(osm).setView(new L.LatLng(51.4769,0.0), 13.5); &lt;/script&gt; &lt;/body&gt;
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-firefox" rel="tag" title="see questions tagged &#39;firefox&#39;">firefox</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Aug '18, 15:00</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Aug '18, 15:06</strong> </span></p>
</div>
</div>
<div id="comments-container-65644" class="comments-container">
&#10;</div>
<div id="comment-tools-65644" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65644-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

