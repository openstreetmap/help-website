+++
type = "question"
title = "Polar coordinate grid"
description = '''Hi there. I&#x27;ve found some maps for Antarctica here: https://nga.maps.arcgis.com/home/webmap/viewer.html and my question is: How can I show polar coordinate grid for it? I&#x27;ve got the grid source code in grid_wgs.js (I use OpenSeaMap in my software that is based on OpenStreetMap), so I guess I just ne...'''
date = "2018-11-08T09:38:00Z"
lastmod = "2018-11-11T09:48:00Z"
weight = 66722
keywords = [ "grid", "polar", "antarctica", "coordicates", "osm" ]
aliases = [ "/questions/66722" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Polar coordinate grid](/questions/66722/polar-coordinate-grid)

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
<span id="post-66722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66722-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there. I've found some maps for Antarctica here: <a href="https://nga.maps.arcgis.com/home/webmap/viewer.html">https://nga.maps.arcgis.com/home/webmap/viewer.html</a> and my question is: How can I show polar coordinate grid for it? I've got the grid source code in grid_wgs.js (I use OpenSeaMap in my software that is based on OpenStreetMap), so I guess I just need to change some mathematical formulas there, but I've got no idea how to do that / what to change etc. Here's the grid_wgs.js code below. I appreciate any ideas and suggestions. Thanks.</p>
<pre><code>//--------------------------------------------------------------------------------
// $Id: grid_wgs.js,v 1.6 2011/02/02 20:37:31 wolf Exp wolf $
//--------------------------------------------------------------------------------
// Erklärung: http://www.netzwolf.info/kartografie/openlayers/wgsgrid
//--------------------------------------------------------------------------------
// Fragen, Wuensche, Bedenken, Anregungen?
// &lt;openlayers(%40)netzwolf.info&gt;
//--------------------------------------------------------------------------------
&#10;OpenLayers.Layer.GridWGS = OpenLayers.Class (OpenLayers.Layer.Vector, {
&#10;    initialize: function (name, options){
        OpenLayers.Layer.Vector.prototype.initialize.apply(this, [name, options]);
    },
&#10;    gridSizeText: null,
&#10;    gridSizeDiv: null,
&#10;    zoomUnits: null,
&#10;    //---------------------------------------------------------
    // Find matching grid unit (minutes) or return null
    //---------------------------------------------------------
&#10;    getGridUnit: function (distance) {
&#10;        if (this.zoomUnits) return this.zoomUnits[this.map.zoom];
&#10;        for (var i=0; i&lt;this.gridUnits.length; i++) {
            if (distance&lt;this.gridUnits[i])
                return this.gridUnits[i];
        }
        return null;
    },
&#10;    // in Winkelsekunden
    gridUnits: [
        //3,        // 0.05&#39;
        6, 12, 30,  // 0.1&#39;  0.2&#39;  0.5&#39;
        1*60, 2*60, 3*60, 5*60, 10*60, 20*60, 30*60,
        1*3600, 2*3600, 3*3600, 4*3600, 6*3600, 10*3600, 15*3600, 30*3600, 45*3600],
&#10;    gridPixelDistance: 100,
&#10;    //---------------------------------------------------------
    // Format gridsize
    //---------------------------------------------------------
&#10;    dd: function (n) {
        return parseInt(n)&gt;=10 ? n : &#39;0&#39;+n;
    },
&#10;    formatGridSize: function (s) {
        var h = Math.floor(s/3600);
        var m = s%3600/60;
        return (h?h+&quot;°&quot;:&quot;&quot;)+(m?m+&quot;&#39;&quot;:&quot;&quot;);
    },
&#10;    formatDegrees: function (s, unit) {
        return Math.floor(s/3600) + &quot;°&quot;
            + (unit%3600?this.dd(s%3600/60)+&quot;&#39;&quot;:&quot;&quot;)
    },
&#10;    //---------------------------------------------------------
    // Draw grid on move or zoom
    //---------------------------------------------------------
&#10;    moveTo: function (bounds, zoomChanged, dragging) {
&#10;        //---------------------------------------------------------
        // but not while dragging
        //---------------------------------------------------------
&#10;        if (dragging) return;
&#10;        //---------------------------------------------------------
        // Remove old grid
        //---------------------------------------------------------
&#10;        this.destroyFeatures();
&#10;        //---------------------------------------------------------
&#10;        //---------------------------------------------------------
&#10;        var mapBounds = bounds.clone().
            transform(this.map.getProjectionObject(), this.map.displayProjection);
&#10;        //---------------------------------------------------------
        // Grid unit
        //---------------------------------------------------------
&#10;        var seconds = 3600 * (mapBounds.top-mapBounds.bottom);
&#10;        var unit = this.getGridUnit (seconds / this.map.getSize().h * this.gridPixelDistance);
&#10;        //---------------------------------------------------------
        // Grid size display object
        // (TODO: create a OpenLayers.Control-Object)
        //---------------------------------------------------------
&#10;        if (this.gridSizeText &amp;&amp; !this.gridSizeDiv) {
            this.gridSizeDiv=OpenLayers.Util.createDiv(this.id);
            this.gridSizeDiv.className=&#39;olControlGridWGS&#39;;
            this.gridSizeDiv.style.zIndex=map.Z_INDEX_BASE[&#39;Control&#39;]+ map.controls.length;
            this.gridSizeDiv.setAttribute(&quot;unselectable&quot;,&quot;on&quot;);
            this.map.viewPortDiv.appendChild (this.gridSizeDiv);
        }
&#10;        //---------------------------------------------------------
        // Hide grid size (if configured)
        //---------------------------------------------------------
&#10;        if (this.gridSizeDiv) this.gridSizeDiv.style.display=&#39;none&#39;;
&#10;        //---------------------------------------------------------
        // Create new grid
        //---------------------------------------------------------
&#10;        if (unit) {
&#10;            //---------------------------------------------------------
            // Compute grid
            //---------------------------------------------------------
&#10;            var x1 = Math.max (-180.0*3600, Math.ceil  (3600 * mapBounds.left  / unit) * unit);
            var x2 = Math.min (+180.0*3600, Math.floor (3600 * mapBounds.right / unit) * unit);
            var y1 = Math.max ( -90.0*3600, Math.ceil  (3600 * mapBounds.bottom/ unit) * unit);
            var y2 = Math.min ( +90.0*3600, Math.floor (3600 * mapBounds.top   / unit) * unit);
&#10;            var features = [];
&#10;            //---------------------------------------------------------
            // Vertical lines
            //---------------------------------------------------------
&#10;            for (var x=x1; x&lt;=x2; x+= unit) {
                var p1 = new OpenLayers.LonLat (x/3600, Math.min(+85, mapBounds.top))
                    .transform(map.displayProjection, map.getProjectionObject());
                var p2 = new OpenLayers.LonLat (x/3600, Math.max(-85, mapBounds.bottom))
                    .transform(map.displayProjection, map.getProjectionObject());
                v1 = new OpenLayers.Feature.Vector ( new OpenLayers.Geometry.LineString( [
                    new OpenLayers.Geometry.Point (p1.lon, p1.lat),
                    new OpenLayers.Geometry.Point (p2.lon, p2.lat)
                ]));
                v1.style={
                    label: this.formatDegrees (Math.abs(x), unit),
                    labelAlign: &quot;lt&quot;,
                    strokeColor: &quot;#666666&quot;,
                    strokeWidth: 1,
                    strokeOpacity: 0.8
                };
                features.push (v1);
            }
&#10;            //---------------------------------------------------------
            // Horizontal lines
            //---------------------------------------------------------
&#10;            for (var y=y1; y&lt;=y2; y+=unit) {
                var p1 = new OpenLayers.LonLat (Math.max(-180, mapBounds.left), y/3600)
                    .transform(map.displayProjection, map.getProjectionObject());
                var p2 = new OpenLayers.LonLat (Math.min(+180, mapBounds.right), y/3600)
                    .transform(map.displayProjection, map.getProjectionObject());
                v1 = new OpenLayers.Feature.Vector ( new OpenLayers.Geometry.LineString( [
                    new OpenLayers.Geometry.Point (p1.lon, p1.lat),
                    new OpenLayers.Geometry.Point (p2.lon, p2.lat)
                ]));
                v1.style={
                    label: this.formatDegrees (Math.abs(y), unit),
                    labelAlign: &quot;lb&quot;,
                    strokeColor: &quot;#666666&quot;,
                    strokeWidth: 1,
                    strokeOpacity: 0.8
                };
                features.push (v1);
            }
&#10;            //---------------------------------------------------------
            // Add grid lines to vector layer
            //---------------------------------------------------------
&#10;            this.addFeatures(features);
&#10;            //---------------------------------------------------------
            // Display grid size
            //---------------------------------------------------------
&#10;            if (this.gridSizeDiv) {
                this.gridSizeDiv.innerHTML = OpenLayers.String.format(this.gridSizeText,
                    {grid: this.formatGridSize(unit)});
                this.gridSizeDiv.style.display=null;
            }
        }
&#10;        //---------------------------------------------------------
        // Superclass
        //---------------------------------------------------------
&#10;        OpenLayers.Layer.Vector.prototype.moveTo.apply(this,arguments);
    },
&#10;    CLASS_NAME: &quot;OpenLayers.Layer.GridWGS&quot;
});
&#10;//--------------------------------------------------------------------------------
// $Id: grid_wgs.js,v 1.6 2011/02/02 20:37:31 wolf Exp wolf $
//--------------------------------------------------------------------------------</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-grid" rel="tag" title="see questions tagged &#39;grid&#39;">grid</span> <span class="post-tag tag-link-polar" rel="tag" title="see questions tagged &#39;polar&#39;">polar</span> <span class="post-tag tag-link-antarctica" rel="tag" title="see questions tagged &#39;antarctica&#39;">antarctica</span> <span class="post-tag tag-link-coordicates" rel="tag" title="see questions tagged &#39;coordicates&#39;">coordicates</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '18, 09:38</strong></p>
<img src="https://secure.gravatar.com/avatar/85400104b152c7da0f6a890d6e00a9b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="e-Ship%20ltd&#39;s gravatar image" />
<p><span>e-Ship ltd</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="e-Ship ltd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66722" class="comments-container">
<span id="66728"></span>
<div id="comment-66728" class="comment">
<div id="post-66728-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>As far as I can tell, this doesn't seem to have anything to do with OSM. Maybe it would be better to ask this on gis.stackexchange.com?</p>
</div>
<div id="comment-66728-info" class="comment-info">
<span class="comment-age">(08 Nov '18, 16:54)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="66746"></span>
<div id="comment-66746" class="comment">
<div id="post-66746-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you <a href="https://help.openstreetmap.org/users/8189/alester">@alester</a>, I've done that: <a href="https://gis.stackexchange.com/questions/302175/polar-coordinate-grid.">https://gis.stackexchange.com/questions/302175/polar-coordinate-grid.</a></p>
</div>
<div id="comment-66746-info" class="comment-info">
<span class="comment-age">(11 Nov '18, 08:29)</span> <span class="comment-user userinfo">e-Ship ltd</span>
</div>
</div>
</div>
<div id="comment-tools-66722" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66722-form-container" class="comment-form-container">
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

<span id="66747"></span>

<div id="answer-container-66747" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66747-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to add the projection as a parameter, see <a href="https://openlayers.org/en/latest/doc/faq.html#how-do-i-change-the-projection-of-my-map-">https://openlayers.org/en/latest/doc/faq.html#how-do-i-change-the-projection-of-my-map-</a> . Southern Polar Projection is EPSG:3031.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '18, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-66747" class="comments-container">
&#10;</div>
<div id="comment-tools-66747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66747-form-container" class="comment-form-container">
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

