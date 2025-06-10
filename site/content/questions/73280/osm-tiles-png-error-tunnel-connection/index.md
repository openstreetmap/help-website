+++
type = "question"
title = "OSM / Tiles / PNG / Error Tunnel Connection"
description = '''When I go here: https://openlayers.org/en/latest/examples/canvas-tiles.html many times I receive this kind of error: https://a.tile.openstreetmap.org/2/0/3.png net::ERR_TUNNEL_CONNECTION_FAILED (Chrome) Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at htt...'''
date = "2020-02-28T13:46:00Z"
lastmod = "2020-03-04T16:29:00Z"
weight = 73280
keywords = [ "tiles", "osm", "connection", "png", "error" ]
aliases = [ "/questions/73280" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OSM / Tiles / PNG / Error Tunnel Connection](/questions/73280/osm-tiles-png-error-tunnel-connection)

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
<span id="post-73280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73280-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I go here:</p>
<p><a href="https://openlayers.org/en/latest/examples/canvas-tiles.html">https://openlayers.org/en/latest/examples/canvas-tiles.html</a></p>
<p>many times I receive this kind of error:</p>
<p><a href="https://a.tile.openstreetmap.org/2/0/3.png">https://a.tile.openstreetmap.org/2/0/3.png</a> net::ERR_TUNNEL_CONNECTION_FAILED (Chrome)</p>
<p>Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at <a href="https://a.tile.openstreetmap.org/3/0/3.png.">https://a.tile.openstreetmap.org/3/0/3.png.</a> (Reason: CORS request did not succeed). (Firefox)</p>
<p>It depends on my proxy or it is a temporary problem on the server?</p>
<p>P.S. I am doing a test with an HTML on my machine copying the code on the example</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-png" rel="tag" title="see questions tagged &#39;png&#39;">png</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '20, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/dd544fdbfcaf6906fb6cd8bf7f4eff29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gf_eu&#39;s gravatar image" />
<p><span>gf_eu</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gf_eu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73280" class="comments-container">
<span id="73306"></span>
<div id="comment-73306" class="comment">
<div id="post-73306-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually the problem is also when I load this example: <a href="https://openlayers.org/en/latest/examples/canvas-tiles.html.">https://openlayers.org/en/latest/examples/canvas-tiles.html.</a> But it doesn't happen always, just sometime.</p>
<p>Now for example I am having this ok:</p>
<p><em><a href="https://b.tile.openstreetmap.org/8/140/128.png">https://b.tile.openstreetmap.org/8/140/128.png</a> via: 1.1 trogdor.openstreetmap.org (squid/4.10) x-cache: MISS from trogdor.openstreetmap.org</em></p>
<p>and this other on error <em><a href="https://c.tile.openstreetmap.org/8/140/129.png">https://c.tile.openstreetmap.org/8/140/129.png</a></em></p>
<p>And this cause me problem in viewing the map in some point. And yes, looks I have the same problem with codesanbox, here for example:</p>
<p><em><a href="https://b.tile.openstreetmap.org/13/4590/4150.png">https://b.tile.openstreetmap.org/13/4590/4150.png</a> x-cache: MISS from necrosan.openstreetmap.org</em></p>
<p>Now I am noticing that I don't have any problem with ARCGis Tiles (either on the example, either on my local file) and I replaced this:</p>
<p><em>source: new ol.source.OSM()</em></p>
<p>with this:</p>
<p><em>source: new ol.source.XYZ({ attributions: 'Tiles © <a href="https://services.arcgisonline.com/ArcGIS/&#39;%20+%20%0A%20%20&#39;rest/services/World_Topo_Map/MapServer">ArcGIS</a>', url: 'https://server.arcgisonline.com/ArcGIS/rest/services/' + 'World_Topo_Map/MapServer/tile/{z}/{y}/{x}' })</em></p>
<p>What do you suggest? To do some investigation or keep going with ARCGis Tiles that work well for me?</p>
</div>
<div id="comment-73306-info" class="comment-info">
<span class="comment-age">(02 Mar '20, 09:16)</span> <span class="comment-user userinfo">gf_eu</span>
</div>
</div>
<span id="73357"></span>
<div id="comment-73357" class="comment">
<div id="post-73357-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I have some information more, I am going to update that ticket, maybe we can find (and give help). And It looks I have the same problem with ARCGis Tiles.</p>
<p>Basically when I open the HTML (before the map is loaded), sometime the page ask me for the proxy credentials, sometimes not (I don't know what's the logic but it's about cache). When the page ask for proxy credentials and I insert them everything works fine otherwise I have that error (Open Layer Engine seems to be "offline", piece of the map are shown sometime depending on what there is in the cache I guess).</p>
<p>But also, even when is "offline" (and not working) sometime (but rarely) doing "Zoom In" and "Zoom out" the browser (not always) ask me for proxy credentials and the Open Layer Engine come "back online" and start to work again.</p>
<p>Now...as workaround maybe I can think about do a "request on the Internet" before loading everything or I don't know "skip the cache" (I tried with the meta tag but nothing). Any idea?</p>
<p>Thanks again.</p>
</div>
<div id="comment-73357-info" class="comment-info">
<span class="comment-age">(04 Mar '20, 10:48)</span> <span class="comment-user userinfo">gf_eu</span>
</div>
</div>
<span id="73368"></span>
<div id="comment-73368" class="comment">
<div id="post-73368-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure I understand your problem.</p>
<p>When you say that a proxy ask for credentials, it's a proxy on your side ? Not the tile cache server ?</p>
<p>Maybe there a problem with chaining proxies...</p>
<p>Does openstreetmap.org work with your setup ?</p>
<p>Could you give a bit more details ?</p>
<p>Regards.</p>
</div>
<div id="comment-73368-info" class="comment-info">
<span class="comment-age">(04 Mar '20, 15:23)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-73280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73280-form-container" class="comment-form-container">
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

<span id="73292"></span>

<div id="answer-container-73292" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73292-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess the "Cross-Origin Request Blocked" error might because you're loading your HTML via http, and the tiles via https. Unfortunately the main OSM servers don't provide http anymore. The problem should only happen in the reverse situation...</p>
<p>I tried with leafletjs, it works fine. I won't install npm to try the OpenLayer code, but it should be similar.</p>
<p>Did you try with "codesanbox" ? (the Edit button at top right of your example page) It also works fine for me.</p>
<p>For the server status, you can check <a href="https://a.tile.openstreetmap.org/">https://a.tile.openstreetmap.org/</a>, to get the name of your tile server, then on <a href="https://hardware.openstreetmap.org/">https://hardware.openstreetmap.org/</a> you'll find a munin link, with all the stats.</p>
<p>You can also check the Headers (x-cache) to find the tile cache server (proxy) that served you, and check it the same way.</p>
<p>Hope this helps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '20, 22:32</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73292" class="comments-container">
&#10;</div>
<div id="comment-tools-73292" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73292-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73310"></span>

<div id="answer-container-73310" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73310-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It might be a problem with your connection, but I notice on <a href="https://uptime.openstreetmap.org/">https://uptime.openstreetmap.org/</a> that trogdor and necrosan are not the most stable tile cache servers.</p>
<p>On the other hand, there is a <a href="https://github.com/openstreetmap/operations/issues/366">ticket</a> at the OSM Operation Team that looks like your problem, maybe you could help them with more data. First try on <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> to check that you can reproduce the problem.</p>
<p>Of course if you're happy with ArcGIS license and data, please use them...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '20, 18:43</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73310" class="comments-container">
<span id="73372"></span>
<div id="comment-73372" class="comment">
<div id="post-73372-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Answer to H_mlet.</p>
<p>Yes, there is a proxy on my side. And also using ARCGis Tiles I am having ERR_TUNNEL_CONNECTION_FAILED, even I am not sure yet it's the exact same error as with OSM Tiles.</p>
<p>What I did now, my workaround, is to "force a Internet request" before everything (I chose to use the same ARCGIS Map url but I could use everything on the web):</p>
<p><em>$.ajax({<br />
   type : "GET",<br />
   url : 'https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer',<br />
   success : function(data) {<br />
   init();<br />
   }<br />
   });<br />
</em></p>
<p>Only after this request is done I initialize the map (method init):</p>
<p><em>function init(){<br />
   ...<br />
   layer = new ol.layer.Tile({<br />
   source: new ol.source.XYZ({<br />
   attributions: 'Tiles ' +<br />
'rest/services/World_Topo_Map/MapServer"&gt;ArcGIS',<br />
   url: 'https://server.arcgisonline.com/ArcGIS/rest/services/' +<br />
   'World_Topo_Map/MapServer/tile/{z}/{y}/{x}'<br />
   })<br />
   });<br />
   map = new ol.Map({<br />
      target: 'map',<br />
      layers: [layer, vector],<br />
      view: new ol.View({<br />
      center: ol.proj.fromLonLat([...]),<br />
      zoom: 5<br />
   })<br />
   });<br />
   ...<br />
   }<br />
</em></p>
<p>What happen now: when I open the HTML first thing the browser does is to ask me the proxy credentials, after the map is loaded and the map works correctly. I am not having any ERR_TUNNEL_CONNECTION_FAILED. If this is a workaround can work also with OSM Tiles and outside of proxy connection I can't say yet....If I do a test I will tell you.</p>
<p>I suppose that there is a problem in the Open Layer Javascript but It can be I will be happy with this workaround...</p>
<p>Hope this can help...and can make any sense for you.</p>
</div>
<div id="comment-73372-info" class="comment-info">
<span class="comment-age">(04 Mar '20, 16:25)</span> <span class="comment-user userinfo">gf_eu</span>
</div>
</div>
<span id="73373"></span>
<div id="comment-73373" class="comment">
<div id="post-73373-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well I don't really understand, but I'm glad you found a workaround, and thanks for sharing. :-)</p>
<p>Anyway it looks more like a bug of OpenLayers, you might want to report it to them : <a href="https://github.com/openlayers/openlayers/issues">https://github.com/openlayers/openlayers/issues</a></p>
<p>Regards</p>
</div>
<div id="comment-73373-info" class="comment-info">
<span class="comment-age">(04 Mar '20, 16:29)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-73310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73310-form-container" class="comment-form-container">
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

