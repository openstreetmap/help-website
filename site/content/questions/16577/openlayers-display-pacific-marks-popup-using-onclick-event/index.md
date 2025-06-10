+++
type = "question"
title = "Openlayers: display pacific marks popup using onclick event"
description = '''I have the following code which addes 3 markers to the map a long with there popup boxes what i want to do is have a list of location at bottom of page and using the id of the marker when click a place on the list just make that places popup appear on the map. &amp;lt;html&amp;gt;  &amp;lt;head&amp;gt;  &amp;lt;meta ht...'''
date = "2012-10-01T15:35:00Z"
lastmod = "2012-10-01T16:05:00Z"
weight = 16577
keywords = [ "openstreetmap", "javascript", "openlayers" ]
aliases = [ "/questions/16577" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Openlayers: display pacific marks popup using onclick event](/questions/16577/openlayers-display-pacific-marks-popup-using-onclick-event)

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
<span id="post-16577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16577-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-16577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the following code which addes 3 markers to the map a long with there popup boxes what i want to do is have a list of location at bottom of page and using the id of the marker when click a place on the list just make that places popup appear on the map.</p>
<pre><code>&lt;html&gt;
    &lt;head&gt;
        &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=utf-8&quot;/&gt;
        &lt;title&gt;Open Street Map&lt;/title&gt;
        &lt;style type=&quot;text/css&quot;&gt;
            body { font: normal 10pt Helvetica, Arial; }
            #map { width: 100%; height: 100%; border: 0px; padding: 0px; }
        &lt;/style&gt;
        &lt;script src=&quot;lib/OpenLayers.js&quot; type=&quot;text/javascript&quot;&gt;&lt;/script&gt;
        &lt;script type=&quot;text/javascript&quot;&gt;
            var iconSize = new OpenLayers.Size(21, 25);
            var iconOffset = new OpenLayers.Pixel(-(iconSize.w / 2), -iconSize.h);
            var icon = new OpenLayers.Icon(&quot;img/fourmarker.png&quot;,
                           iconSize, iconOffset);
&#10;            var zoom, center, currentPopup, map, lyrMarkers;
            var popupClass = OpenLayers.Class(OpenLayers.Popup.FramedCloud, {
                &quot;autoSize&quot;: true,
                &quot;minSize&quot;: new OpenLayers.Size(300, 50),
                &quot;maxSize&quot;: new OpenLayers.Size(500, 300),
                &quot;keepInMap&quot;: true
            });
&#10;            var bounds = new OpenLayers.Bounds();
            function addMarker(id, lng, lat, info) {
                var pt = new OpenLayers.LonLat(lng, lat)
                                       .transform(new OpenLayers.Projection(&quot;EPSG:4326&quot;), 
                                       map.getProjectionObject());
                bounds.extend(pt);
                var feature = new OpenLayers.Feature(lyrMarkers, pt);
                feature.closeBox = true;
                feature.popupClass = popupClass;
                feature.data.popupContentHTML = info ;
                feature.data.overflow = &quot;auto&quot;;
                var marker = new OpenLayers.Marker(pt, icon.clone());
&#10;                var markerClick = function(evt) {
                    if (currentPopup != null &amp;&amp; currentPopup.visible()) {
                        currentPopup.hide();
                    }
&#10;                    if (this.popup == null) {
                        this.popup = this.createPopup(this.closeBox);
                        map.addPopup(this.popup);
                        this.popup.show();
                    } else {
                        this.popup.toggle();
                    }
                    currentPopup = this.popup;
                    OpenLayers.Event.stop(evt);
                };
                marker.events.register(&quot;mousedown&quot;, feature, markerClick);
                lyrMarkers.addMarker(marker);
            }
&#10;            function initMap() {
                var options = {
                    projection: new OpenLayers.Projection(&quot;EPSG:900913&quot;),
                    displayProjection: new OpenLayers.Projection(&quot;EPSG:4326&quot;),
                    units: &quot;m&quot;,
                    numZoomLevels: 19,
                    maxResolution: 156543.0339,
                    maxExtent: new OpenLayers.Bounds(-0.13011, -0.13011, 51.51039, 51.51039)
                };
&#10;                map = new OpenLayers.Map(&quot;map&quot;, options);
                map.addControl(new OpenLayers.Control.DragPan());
                var lyrOsm = new OpenLayers.Layer.OSM();
                map.addLayer(lyrOsm);
                lyrMarkers = new OpenLayers.Layer.Markers(&quot;Markers&quot;);
                map.addLayer(lyrMarkers);
&#10;                 //add marker on given coordinates
                addMarker(&#39;1&#39;,-0.12519,51.51112 , &#39;&lt;b&gt;Tescos&lt;/b&gt;&lt;br/&gt;Covent garden&#39;);
                addMarker(&#39;2&#39;,-0.13264,51.50918 , &#39;&lt;b&gt;Spar&lt;/b&gt;&lt;br/&gt;Leicester Square&#39;);
                addMarker(&#39;3&#39;, -0.12498,51.50807 , &#39;&lt;b&gt;M &amp; S&lt;/b&gt;&lt;br/&gt;Embankment&#39;);
                center = bounds.getCenterLonLat();
                map.setCenter(center, map.getZoomForExtent(bounds) - 1);
                zoom = map.getZoom();
            }
&#10;        &lt;/script&gt;
    &lt;/head&gt;
    &lt;body onload=&quot;initMap()&quot; style=&quot;margin:0; border:0; padding:0; width:1000px; height:500px;&quot;&gt;
        &lt;div id=&quot;map&quot;&gt;&lt;/div&gt;
&#10;&lt;a href=&quot;popup()&quot;id=&quot;1&quot;&gt;1&lt;/a&gt; &lt;br/&gt;
&lt;a href=&quot;popup()&quot;&gt;1&lt;/a&gt;
    &lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Oct '12, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/79efeaa26d0275a0004a660c330cb2cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zaratj&#39;s gravatar image" />
<p><span>zaratj</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zaratj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Oct '12, 16:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-16577" class="comments-container">
<span id="16579"></span>
<div id="comment-16579" class="comment">
<div id="post-16579-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That's really an OpenLayers question rather than an OSM one.</p>
<p>There are a bunch of OpenLayers mailing lists described <a href="http://trac.osgeo.org/openlayers/wiki/MailingLists">here</a>, and other useful resources, including an OpenLayers IRC channel, <a href="http://trac.osgeo.org/openlayers/">here</a>.</p>
</div>
<div id="comment-16579-info" class="comment-info">
<span class="comment-age">(01 Oct '12, 16:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-16577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16577-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

