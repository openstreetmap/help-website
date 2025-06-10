+++
type = "question"
title = "change theme of map"
description = '''Hi guys , I am flutter developer and new on osm and map stuff. On my application I am using osm like this: FlutterMap(  options: MapOptions(  controller: controller,  center: model!.userLocation,  zoom: 16.0,  onTap: (point) {  model.setSelectedLatLngMarker(point);  },  plugins: [  DragMarkerPlugin(...'''
date = "2021-03-26T17:01:00Z"
lastmod = "2021-03-26T17:01:00Z"
weight = 79403
keywords = [ "osm", "flutter" ]
aliases = [ "/questions/79403" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [change theme of map](/questions/79403/change-theme-of-map)

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
<span id="post-79403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79403-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys , I am flutter developer and new on osm and map stuff. On my application I am using osm like this:</p>
<pre><code>FlutterMap(
                    options: MapOptions(
                        controller: controller,
                        center: model!.userLocation,
                        zoom: 16.0,
                        onTap: (point) {
                          model.setSelectedLatLngMarker(point);
                        },
                        plugins: [
                          DragMarkerPlugin(),
                        ]),
                    layers: [
                      TileLayerOptions(
                        urlTemplate:
                            &#39;https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png&#39;,
                        subdomains: [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;],
                        tileProvider: NonCachingNetworkTileProvider(),
                      )</code></pre>
<p>I want to use dark map but <a href="https://cartodb-basemaps">https://cartodb-basemaps</a>-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png', is very dark : <a href="https://pasteboard.co/JUque4J.png">https://pasteboard.co/JUque4J.png</a></p>
<p>Is it possible to change street line and title colors ?</p>
<p>After googleing I found <a href="https://openmaptiles.org/docs/style/maputnik/">This guide</a> . Now with <strong>maputnik</strong> I made my custom style. After exporting json style how can I use this style ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-flutter" rel="tag" title="see questions tagged &#39;flutter&#39;">flutter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Mar '21, 17:01</strong></p>
<img src="https://secure.gravatar.com/avatar/3016a8114f68eb431594ee9ec890c246?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alt2020&#39;s gravatar image" />
<p><span>alt2020</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alt2020 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Mar '21, 18:27</strong> </span></p>
</div>
</div>
<div id="comments-container-79403" class="comments-container">
&#10;</div>
<div id="comment-tools-79403" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79403-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

