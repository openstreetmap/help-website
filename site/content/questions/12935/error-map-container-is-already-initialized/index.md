+++
type = "question"
title = "Error: &quot;Map container is already initialized.&quot;"
description = '''Hi All, I hope this is the right place to ask this question: I have just installed leaflet/cloudmap for the first time and while the map appears to works as it should, I get the error that “Map container is already initialized. (7 out of range 4),” Having searched on the web, some people say that th...'''
date = "2012-05-24T15:52:00Z"
lastmod = "2018-04-26T05:42:00Z"
weight = 12935
keywords = [ "initialize", "leaflet" ]
aliases = [ "/questions/12935" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error: "Map container is already initialized."](/questions/12935/error-map-container-is-already-initialized)

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
<span id="post-12935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12935-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All, I hope this is the right place to ask this question:</p>
<p>I have just installed leaflet/cloudmap for the first time and while the map appears to works as it should, I get the error that “Map container is already initialized. (7 out of range 4),”</p>
<p>Having searched on the web, some people say that the map div is being created twice (I couldn’t see this myself).</p>
<p>Does anyone know how to fix this bug? All help is much appreciated!</p>
<p>Thanks, Lee</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-initialize" rel="tag" title="see questions tagged &#39;initialize&#39;">initialize</span> <span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '12, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/d67d1b12768436896496415e81a18267?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LondonLee&#39;s gravatar image" />
<p><span>LondonLee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LondonLee has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '12, 16:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span></p>
</div>
</div>
<div id="comments-container-12935" class="comments-container">
<span id="12936"></span>
<div id="comment-12936" class="comment">
<div id="post-12936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Perhaps pastebin the code (or if it's small, add it as a comment here - Richard's example <a href="http://switch2osm.org/using-tiles/getting-started-with-leaflet/">here</a> is only 15 lines long, after all)</p>
</div>
<div id="comment-12936-info" class="comment-info">
<span class="comment-age">(24 May '12, 16:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="12937"></span>
<div id="comment-12937" class="comment">
<div id="post-12937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>The code is as follows, it is the basic code example. it does sit within a page that also does a JSON call etc.</p>
<p>Much appreciated!</p>
<pre><code>    &lt;script src=&quot;leaflet/dist/leaflet.js&quot;&gt;&lt;/script&gt;
&#10;    &lt;div id=&quot;map&quot; style=&quot;height: 200px&quot;&gt; &lt;a href=&quot;#&quot; data-role=&quot;button&quot; id=&quot;getLocation&quot;&gt;Get my location&lt;/a&gt; &lt;/div&gt;
&#10;    &lt;script&gt;
&#10;            $(&#39;#getLocation&#39;).click(function(){
&#10;            map = new L.Map(&#39;map&#39;);
&#10;            var cloudmadeUrl = &#39;http://{s}.tile.cloudmade.com/myapikey/997/256/{z}/{x}/{y}.png&#39;,
            cloudmadeAttribution = &#39;Map data &amp;copy; 2011 OpenStreetMap contributors, Imagery &amp;copy; 2011 CloudMade&#39;,
            cloudmade = new L.TileLayer(cloudmadeUrl, {maxZoom: 18, attribution: cloudmadeAttribution});
            map.setView(new L.LatLng(51.505, -0.09), 13).addLayer(cloudmade);
&#10;            var markerLocation = new L.LatLng(51.5, -0.09),
            marker = new L.Marker(markerLocation);
            map.addLayer(marker);
            marker.bindPopup(&quot;&lt;b&gt;Hello world!&lt;/b&gt;&lt;br /&gt;I am a popup.&quot;).openPopup();
&#10;            });</code></pre>
</div>
<div id="comment-12937-info" class="comment-info">
<span class="comment-age">(24 May '12, 16:31)</span> <span class="comment-user userinfo">LondonLee</span>
</div>
</div>
</div>
<div id="comment-tools-12935" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12935-form-container" class="comment-form-container">
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

<span id="63150"></span>

<div id="answer-container-63150" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63150-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Before initializing map check for is the map is already initiated or not</p>
<p>var container = L.DomUtil.get('map'); if(container != null){ container._leaflet_id = null; }</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '18, 05:42</strong></p>
<img src="https://secure.gravatar.com/avatar/235e744acd9588f7d8543431f8ae7bdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dipin%20Raj%20C&#39;s gravatar image" />
<p><span>Dipin Raj C</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dipin Raj C has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63150" class="comments-container">
&#10;</div>
<div id="comment-tools-63150" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63150-form-container" class="comment-form-container">
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

