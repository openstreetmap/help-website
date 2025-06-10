+++
type = "question"
title = "in openstreemap how to make a html code that when i move the mouse over the map it will display in real time the coordinates in a small tooltip?"
description = '''I want that when i move the mouse over the map it will display like in a small tool tip balloon the coordinates in real time on the mouse cursor for example like: 35.56, 56.765 I tried this code in my wix site but it&#x27;s showing the map but the coordinate with the mouse is not working showing anything...'''
date = "2024-01-03T20:23:00Z"
lastmod = "2024-01-03T20:23:00Z"
weight = 88117
keywords = [ "openstreetmap", "html", "javascript" ]
aliases = [ "/questions/88117" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [in openstreemap how to make a html code that when i move the mouse over the map it will display in real time the coordinates in a small tooltip?](/questions/88117/in-openstreemap-how-to-make-a-html-code-that-when-i-move-the-mouse-over-the-map-it-will-display-in-real-time-the-coordinates-in-a-small-tooltip)

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
<span id="post-88117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88117-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want that when i move the mouse over the map it will display like in a small tool tip balloon the coordinates in real time on the mouse cursor for example like: 35.56, 56.765</p>
<p>I tried this code in my wix site but it's showing the map but the coordinate with the mouse is not working showing anything.</p>
<pre><code>&lt;html&gt;
&lt;head&gt;
   &lt;link rel=&quot;stylesheet&quot; href=&quot;https://unpkg.com/leaflet/dist/leaflet.css&quot; /&gt;
   &lt;script src=&quot;https://unpkg.com/leaflet/dist/leaflet.js&quot;&gt;&lt;/script&gt;
   &lt;style&gt;
      body, html, #map {
         height: 100%;
         margin: 0;
      }
   &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
   &lt;div id=&quot;map&quot;&gt;&lt;/div&gt;
&#10;   &lt;script&gt;
      var map = L.map(&#39;map&#39;).setView([32.921, 39.562], 10);
      L.tileLayer(&#39;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&#39;, {
         attribution: &#39;© OpenStreetMap contributors&#39;
      }).addTo(map);
&#10;      var marker = L.marker([32.921, 39.562]).addTo(map);
      marker.bindPopup(&quot;&lt;b&gt;Hello World!&lt;/b&gt;&lt;br&gt;This is a customizable popup.&quot;).openPopup();
&#10;      // Create a tooltip to show coordinates
      var tooltip = L.tooltip({
         permanent: true,
         direction: &#39;bottom&#39;,
         opacity: 0.7
      });
&#10;      // Add the tooltip to the map
      tooltip.addTo(map);
&#10;      // Event listener for mousemove
      map.on(&#39;mousemove&#39;, function (e) {
         var latlng = e.latlng;
         tooltip.setLatLng(latlng).setContent(&#39;Coordinates: &#39; + latlng.lat.toFixed(6) + &#39;, &#39; + latlng.lng.toFixed(6));
      });
   &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-html" rel="tag" title="see questions tagged &#39;html&#39;">html</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '24, 20:23</strong></p>
<img src="https://secure.gravatar.com/avatar/341f73e16114cc9ef077ab0c66f1a4a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chocolade72&#39;s gravatar image" />
<p><span>chocolade72</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chocolade72 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88117" class="comments-container">
&#10;</div>
<div id="comment-tools-88117" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88117-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

