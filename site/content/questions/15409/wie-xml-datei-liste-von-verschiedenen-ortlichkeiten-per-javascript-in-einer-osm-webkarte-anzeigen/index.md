+++
type = "question"
title = "Wie xml-Datei (Liste von verschiedenen Örtlichkeiten) per JavaScript in einer OSM-Webkarte anzeigen?"
description = '''Moin, wie muss man vorgehen,um eine xml-Datei(Liste von verschiedenen Örtlichkeiten) in einer Openstreetmap-Karte angezeigt zu bekommen? Beispiel für eine Gestaltung einer Grundkarte in einer Html mittels CSS und Javascript ist hier: http://wiki.openstreetmap.org/wiki/DE:Karte_in_Webseite_einbinden ...'''
date = "2012-08-22T21:20:00Z"
lastmod = "2012-08-25T08:56:00Z"
weight = 15409
keywords = [ "xml-datei", "openlayers", "webseite", "lang-de" ]
aliases = [ "/questions/15409" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wie xml-Datei (Liste von verschiedenen Örtlichkeiten) per JavaScript in einer OSM-Webkarte anzeigen?](/questions/15409/wie-xml-datei-liste-von-verschiedenen-ortlichkeiten-per-javascript-in-einer-osm-webkarte-anzeigen)

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
<span id="post-15409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15409-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Moin,</p>
<p>wie muss man vorgehen,um eine xml-Datei(Liste von verschiedenen Örtlichkeiten) in einer Openstreetmap-Karte angezeigt zu bekommen?</p>
<p>Beispiel für eine Gestaltung einer Grundkarte in einer Html mittels CSS und Javascript ist hier: <a href="http://wiki.openstreetmap.org/wiki/DE:Karte_in_Webseite_einbinden">http://wiki.openstreetmap.org/wiki/DE:Karte_in_Webseite_einbinden</a></p>
<p>Aber wie muss ich dann weiter gehen?</p>
<p>Gruß</p>
<p>Thal</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml-datei" rel="tag" title="see questions tagged &#39;xml-datei&#39;">xml-datei</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-webseite" rel="tag" title="see questions tagged &#39;webseite&#39;">webseite</span> <span class="post-tag tag-link-lang-de" rel="tag" title="see questions tagged &#39;lang-de&#39;">lang-de</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '12, 21:20</strong></p>
<img src="https://secure.gravatar.com/avatar/26e99a9029da21c580b1624b782cca47?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thal1982&#39;s gravatar image" />
<p><span>thal1982</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thal1982 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '13, 00:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-15409" class="comments-container">
<span id="15412"></span>
<div id="comment-15412" class="comment">
<div id="post-15412-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As far as I understand, the question is about displaying data stored in xml on OSM map.</p>
<p>Do you know if a parser still exist for your XML format? What is the structure of your format.</p>
<p>The example given use Openlayers, but Leaflet can also be used if it is easier for your data.</p>
</div>
<div id="comment-15412-info" class="comment-info">
<span class="comment-age">(22 Aug '12, 21:38)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="15498"></span>
<div id="comment-15498" class="comment">
<div id="post-15498-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Moin,</p>
<p>bislang bin ich kein Schritt weiter gekommen.</p>
<p>in welcher Zeile muss ich den Code einfügen?</p>
<p>Folgende Dateien sind vorhanden:</p>
<pre><code>function jumpTo(lon, lat, zoom) {
    var x = Lon2Merc(lon);
    var y = Lat2Merc(lat);
    map.setCenter(new OpenLayers.LonLat(x, y), zoom);
    return false;
}
&#10;function Lon2Merc(lon) {
    return 20037508.34 * lon / 180;
}
&#10;function Lat2Merc(lat) {
    var PI = 3.14159265358979323846;
    lat = Math.log(Math.tan( (90 + lat) * PI / 360)) / (PI / 180);
    return 20037508.34 * lat / 180;
}
&#10;function addMarker(layer, lon, lat, popupContentHTML) {
&#10;    var ll = new OpenLayers.LonLat(Lon2Merc(lon), Lat2Merc(lat));
    var feature = new OpenLayers.Feature(layer, ll); 
    feature.closeBox = true;
    feature.popupClass = OpenLayers.Class(OpenLayers.Popup.FramedCloud, {minSize: new OpenLayers.Size(300, 180) } );
    feature.data.popupContentHTML = popupContentHTML;
    feature.data.overflow = &quot;hidden&quot;;
&#10;    var marker = new OpenLayers.Marker(ll);
    marker.feature = feature;
&#10;    var markerClick = function(evt) {
        if (this.popup == null) {
            this.popup = this.createPopup(this.closeBox);
            map.addPopup(this.popup);
            this.popup.show();
        } else {
            this.popup.toggle();
        }
        OpenLayers.Event.stop(evt);
    };
    marker.events.register(&quot;mousedown&quot;, feature, markerClick);
&#10;    layer.addMarker(marker);
    map.addPopup(feature.createPopup(feature.closeBox));
}
&#10;function getCycleTileURL(bounds) {
   var res = this.map.getResolution();
   var x = Math.round((bounds.left - this.maxExtent.left) / (res * this.tileSize.w));
   var y = Math.round((this.maxExtent.top - bounds.top) / (res * this.tileSize.h));
   var z = this.map.getZoom();
   var limit = Math.pow(2, z);
&#10;   if (y &lt; 0 || y &gt;= limit)
   {
     return null;
   }
   else
   {
     x = ((x % limit) + limit) % limit;
&#10;     return this.url + z + &quot;/&quot; + x + &quot;/&quot; + y + &quot;.&quot; + this.type;
   }
}</code></pre>
<p>Dies ist die tom.js(-Datei).</p>
<p>Und dies ist die Index.html(-Datei):</p>
<pre><code>&lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD XHTML 1.1//EN&quot; &quot;http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd&quot;&gt;
&lt;html xmlns=&quot;http://www.w3.org/1999/xhtml&quot; xml:lang=&quot;de&quot; lang=&quot;de-de&quot;&gt;
&lt;head&gt;
&lt;title&gt;Map | Testanwendung&lt;/title&gt;
&lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;
&lt;meta http-equiv=&quot;content-script-type&quot; content=&quot;text/javascript&quot; /&gt;
&lt;meta http-equiv=&quot;content-style-type&quot; content=&quot;text/css&quot; /&gt;
&lt;meta http-equiv=&quot;content-language&quot; content=&quot;de&quot; /&gt;
&lt;meta name=&quot;author&quot; content=&quot;Thomas Heiles&quot; /&gt;
&lt;link rel=&quot;stylesheet&quot; type=&quot;text/css&quot; href=&quot;map.css&quot;&gt;&lt;/link&gt;
&lt;!--[if IE]&gt;
&lt;link rel=&quot;stylesheet&quot; type=&quot;text/css&quot; href=&quot;ie_map.css&quot;&gt;&lt;/link&gt;
&lt;![endif]--&gt;
&lt;script type=&quot;text/javascript&quot; src=&quot;http://www.openlayers.org/api/OpenLayers.js&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot; src=&quot;http://www.openstreetmap.org/openlayers/OpenStreetMap.js&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot; src=&quot;tom.js&quot;&gt;&lt;/script&gt;
&#10;&lt;script type=&quot;text/javascript&quot;&gt;
//&lt;![CDATA[
&#10;var map;
var layer_mapnik;
var layer_tah;
var layer_markers;
&#10;function drawmap() {
    // Popup und Popuptext mit evtl. Grafik
    var popuptext=&quot;&lt;font color=\&quot;black\&quot;&gt;&lt;b&gt;Thomas Heiles&lt;br&gt;Stra&amp;szlig;e 123&lt;br&gt;54290 Trier&lt;/b&gt;&lt;p&gt;&lt;img src=\&quot;test.jpg\&quot; width=\&quot;180\&quot; height=\&quot;113\&quot;&gt;&lt;/p&gt;&lt;/font&gt;&quot;;
&#10;    OpenLayers.Lang.setCode(&#39;de&#39;);
&#10;    // Position und Zoomstufe der Karte
    var lon = 6.641389;
    var lat = 49.756667;
    var zoom = 7;
&#10;    map = new OpenLayers.Map(&#39;map&#39;, {
        projection: new OpenLayers.Projection(&quot;EPSG:900913&quot;),
        displayProjection: new OpenLayers.Projection(&quot;EPSG:4326&quot;),
        controls: [
            new OpenLayers.Control.Navigation(),
            new OpenLayers.Control.LayerSwitcher(),
            new OpenLayers.Control.PanZoomBar()],
        maxExtent:
            new OpenLayers.Bounds(-20037508.34,-20037508.34,
                                    20037508.34, 20037508.34),
        numZoomLevels: 18,
        maxResolution: 156543,
        units: &#39;meters&#39;
    });
&#10;    layer_mapnik = new OpenLayers.Layer.OSM.Mapnik(&quot;Mapnik&quot;);
    layer_markers = new OpenLayers.Layer.Markers(&quot;adress&quot;, { projection: new OpenLayers.Projection(&quot;EPSG:4326&quot;), 
                                                  visibility: true, displayInLayerSwitcher: false });
&#10;    map.addLayers([layer_mapnik, layer_markers]);
    jumpTo(lon, lat, zoom);
&#10;    // Position des Markers
    addMarker(layer_markers, 6.641389, 49.756667, popuptext);
&#10;}
&#10;//]]&gt;
    &lt;/script&gt;
&#10;  &lt;/head&gt;
  &lt;body onload=&quot;drawmap();&quot;&gt;
&#10;  &lt;div id=&quot;header&quot;&gt;
   &lt;div id=&quot;content&quot;&gt;Karte (Testversion)&lt;/div&gt;
   &lt;div id=&quot;osm&quot;&gt;© &lt;a href=&quot;http://www.openstreetmap.org&quot;&gt;OpenStreetMap&lt;/a&gt;
     und &lt;a href=&quot;http://www.openstreetmap.org/copyright&quot;&gt;Mitwirkende&lt;/a&gt;,
     &lt;a href=&quot;http://creativecommons.org/licenses/by-sa/2.0/deed.de&quot;&gt;CC-BY-SA&lt;/a&gt;
   &lt;/div&gt;
  &lt;/div&gt;
  &lt;div id=&quot;map&quot;&gt;
  &lt;/div&gt;
&#10;&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>In welcher Datei muss man dann den xml-Link zur Datei hinzufügen. Natürlich sollen mittels der XML-Datei die Marker aus dem Code heraus ausgelagert werden.</p>
<p>Dieser oben genannte Code stammt von hier: <a href="http://wiki.openstreetmap.org/wiki/DE:Karte_in_Webseite_einbinden">http://wiki.openstreetmap.org/wiki/DE:Karte_in_Webseite_einbinden</a></p>
<p>Ich hoffe ich habe dabei nichts übersehen,wie man zu einer Lösung kommt.</p>
<p>Gruß</p>
<p>Thal</p>
</div>
<div id="comment-15498-info" class="comment-info">
<span class="comment-age">(25 Aug '12, 07:14)</span> <span class="comment-user userinfo">thal1982</span>
</div>
</div>
<span id="15504"></span>
<div id="comment-15504" class="comment">
<div id="post-15504-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey thal, dein Openlayers-Ploblem scheint alles andere als eine FAQ zu sein.</p>
<p>Ich halte es daher für besser und aussichtsreicher, wenn du die Fragestellung im deutschen Unterforum auf <a href="http://forum.osm.org">http://forum.osm.org</a> nochmal stellst. Da lesen wohl mehr OL-Experten mit.</p>
</div>
<div id="comment-15504-info" class="comment-info">
<span class="comment-age">(25 Aug '12, 08:56)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-15409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15409-form-container" class="comment-form-container">
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

<span id="15433"></span>

<div id="answer-container-15433" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15433-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Some hints are listed at the website of <a href="http://openlayers.org">OpenLayers.org</a> ... they have a collection of <a href="http://openlayers.org/dev/examples/">examples</a> there.</p>
<p>About the Leaflet framework, have a look at their <a href="http://leaflet.cloudmade.com">website</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '12, 09:39</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Aug '12, 09:39</strong> </span></p>
</div>
</div>
<div id="comments-container-15433" class="comments-container">
&#10;</div>
<div id="comment-tools-15433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15433-form-container" class="comment-form-container">
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

