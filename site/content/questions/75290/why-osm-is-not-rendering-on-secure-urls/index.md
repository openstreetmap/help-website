+++
type = "question"
title = "Why OSM is not rendering on secure URLs?"
description = '''Hello Everyone! I am a beginner in using openstreet maps. I have encountered an issue with my website i.e. when I am loading my website with secure https then the maps have stopped loading. While it was working fine with http. This is my code: &amp;lt;script&amp;gt;  // initialize Leaflet  var greenIcon = L...'''
date = "2020-06-11T11:14:00Z"
lastmod = "2020-06-11T11:55:00Z"
weight = 75290
keywords = [ "ssl", "https" ]
aliases = [ "/questions/75290" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why OSM is not rendering on secure URLs?](/questions/75290/why-osm-is-not-rendering-on-secure-urls)

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
<span id="post-75290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75290-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Everyone!</p>
<p>I am a beginner in using openstreet maps. I have encountered an issue with my website i.e. when I am loading my website with secure https then the maps have stopped loading. While it was working fine with http.</p>
<p>This is my code: &lt;script&gt; // initialize Leaflet var greenIcon = L.icon({ iconUrl: 'cloud.png', iconSize: [30, 20] }); var map = L.map('map').setView({ lon: 67.022095, lat: 24.926294 }, 10);</p>
<pre><code>            // add the OpenStreetMap tiles
            L.tileLayer(&#39;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&#39;, {
                maxZoom: 19,
                attribution: &#39;&amp;copy; &lt;a href=&quot;https://openstreetmap.org/copyright&quot;&gt;OpenStreetMap contributors&lt;/a&gt;&#39;
            }).addTo(map);
&#10;            // show the scale bar on the lower left corner
            L.control.scale().addTo(map);
&#10;            var data = &lt;?php echo JSON_encode($donnees); ?&gt;;
&#10;            console.log(data[0].lat);
            for (var i = 0; i &lt; data.length; i++) {
                //data[i].name
                L.marker({
                    lon: data[i].lng,
                    lat: data[i].lat
                }, {
                    icon: greenIcon
                }).bindPopup(&quot;&lt;b&gt;Location Name: &lt;/b&gt;&quot; + data[i].name + &quot;&lt;br&gt; &lt;b&gt;Number of Fans: &lt;/b&gt;&quot;+ data[i].count_fan&quot;).addTo(map);
            }
        &lt;/script&gt;</code></pre>
<p>This is the error: Mixed Content: The page at 'https://...' was loaded over HTTPS, but requested an insecure stylesheet 'http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css'. This request has been blocked; the content must be served over HTTPS.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jun '20, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/9667d3d17221e7c3ee3de480ee747b16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mahnoor%20Atiq&#39;s gravatar image" />
<p><span>Mahnoor Atiq</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mahnoor Atiq has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75290" class="comments-container">
&#10;</div>
<div id="comment-tools-75290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75290-form-container" class="comment-form-container">
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

<span id="75291"></span>

<div id="answer-container-75291" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75291-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Somewhere in your html (not in the snippet in your question) you have a reference to <a href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css">http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css</a> , which is http not https (and is a <em>very</em> old version of leaflet).</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jun '20, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-75291" class="comments-container">
&#10;</div>
<div id="comment-tools-75291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75291-form-container" class="comment-form-container">
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

