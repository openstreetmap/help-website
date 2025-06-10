+++
type = "question"
title = "Marker Pop-up and line between two marker"
description = '''Here is my code:  &amp;lt;html lang=&quot;en&quot;&amp;gt; &amp;lt;head&amp;gt;  &amp;lt;meta charset=&quot;utf-8&quot;&amp;gt;  &amp;lt;title&amp;gt;Etü &amp;amp; Proje - Staj&amp;lt;/title&amp;gt;  &amp;lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=UTF-8&quot;/&amp;gt;  &amp;lt;link rel=&quot;stylesheet&quot; href=&quot;https://openlayers.org/en/v4.6.5/css/ol.css&quot; type=&quot;text/...'''
date = "2020-07-01T10:31:00Z"
lastmod = "2020-07-01T10:31:00Z"
weight = 75491
keywords = [ "up-line-marker", "pop" ]
aliases = [ "/questions/75491" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Marker Pop-up and line between two marker](/questions/75491/marker-pop-up-and-line-between-two-marker)

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
<span id="post-75491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75491-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Here is my code:</p>
&lt;html lang="en"&gt; &lt;head&gt; &lt;meta charset="utf-8"&gt; &lt;title&gt;Etü &amp; Proje - Staj&lt;/title&gt; &lt;meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/&gt; &lt;link rel="stylesheet" href="https://openlayers.org/en/v4.6.5/css/ol.css" type="text/css"&gt; &lt;script src="https://openlayers.org/en/v4.6.5/build/ol.js" type="text/javascript"&gt;&lt;/script&gt;
<p>&lt;script&gt; var map; var mapLat = 39.8588; var mapLng = 32.64402; var mapDefaultZoom = 10;</p>
<pre><code>function initialize_map() {
  map = new ol.Map({
    target: &quot;map&quot;,
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM({
                  url: &quot;https://a.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;
            })
        })
    ],
    view: new ol.View({
        center: ol.proj.fromLonLat([mapLng, mapLat]),
        zoom: mapDefaultZoom
    })
  });
}
&#10;function add_map_point(lat, lng) {
  var vectorLayer = new ol.layer.Vector({
    source:new ol.source.Vector({
      features: [new ol.Feature({
            geometry: new ol.geom.Point(ol.proj.transform([parseFloat(lng), parseFloat(lat)], &#39;EPSG:4326&#39;, &#39;EPSG:3857&#39;)),
        })]
    }),
    style: new ol.style.Style({
      image: new ol.style.Icon({
        anchor: [0.5, 0.5],
        anchorXUnits: &quot;fraction&quot;,
        anchorYUnits: &quot;fraction&quot;,
        src: &quot;https://upload.wikimedia.org/wikipedia/commons/e/ec/RedDot.svg&quot;
      })
    })
  });
&#10;  map.addLayer(vectorLayer);
}</code></pre>
&lt;/script&gt;
<p>&lt;/head&gt; &lt;body onload="initialize_map(); add_map_point(39.8588, 32.64402);add_map_point(39.921295, 32.852267);"&gt;</p>
<div>
&#10;</div>
&lt;/body&gt; &lt;/html&gt;
<p>My question is how can i add a marker pop up and draw a line between these two markers?</p>
<p>Thanks alot.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-up-line-marker" rel="tag" title="see questions tagged &#39;up-line-marker&#39;">up-line-marker</span> <span class="post-tag tag-link-pop" rel="tag" title="see questions tagged &#39;pop&#39;">pop</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '20, 10:31</strong></p>
<img src="https://secure.gravatar.com/avatar/9009b4a89ac18e5ab303ab46fcfff22b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="serkan991&#39;s gravatar image" />
<p><span>serkan991</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="serkan991 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75491" class="comments-container">
&#10;</div>
<div id="comment-tools-75491" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75491-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

