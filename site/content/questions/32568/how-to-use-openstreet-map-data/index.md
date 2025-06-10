+++
type = "question"
title = "how to use openstreet map data"
description = '''Hey everybody. I work with GeoServer using Apache Tomcat in NetBeans. What i want is using OpenStreetMap as base map. i search in some forums and i found that i have to add this code: &amp;lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&amp;gt;  &amp;lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD XHTML 1.0 Strict//EN&quot; &quot;DTD/xhtml...'''
date = "2014-04-23T15:43:00Z"
lastmod = "2020-05-19T08:24:00Z"
weight = 32568
keywords = [ "openstreetmap", "apache-tomcat", "geoserver" ]
aliases = [ "/questions/32568" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to use openstreet map data](/questions/32568/how-to-use-openstreet-map-data)

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
<span id="post-32568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32568-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey everybody.</p>
<p>I work with GeoServer using Apache Tomcat in NetBeans. What i want is using OpenStreetMap as base map. i search in some forums and i found that i have to add this code:</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;</code></pre>
<p>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "DTD/xhtml1-strict.dtd"&gt; &lt;html xmlns="http://www.w3.org/1999/xhtml"&gt; &lt;head&gt; &lt;title&gt;OpenLayers map preview&lt;/title&gt; &lt;link rel="stylesheet" type="text/css" href="http://localhost:8080/geoserver/openlayers/theme/default/style.css"/&gt; &lt;style type="text/css"&gt; / <em>General settings</em> / body { font-family: Verdana, Geneva, Arial, Helvetica, sans-serif; font-size: small; } / <em>Toolbar styles</em> / #toolbar { position: relative; padding-bottom: 0.5em; display: none; }</p>
<pre><code>        #toolbar ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
&#10;        #toolbar ul li {
            float: left;
            padding-right: 1em;
            padding-bottom: 0.5em;
        }
&#10;        #toolbar ul li a {
            font-weight: bold;
            font-size: smaller;
            vertical-align: middle;
            color: black;
            text-decoration: none;
        }
&#10;        #toolbar ul li a:hover {
            text-decoration: underline;
        }
&#10;        #toolbar ul li * {
            vertical-align: middle;
        }
&#10;        /* The map and the location bar */
        #map {
            clear: both;
            position: relative;
            width: 512px;
            height: 365px;
            border: 1px solid black;
        }
&#10;        #wrapper {
            width: 512px;
        }
&#10;        #location {
            float: right;
        }
&#10;        #options {
            position: absolute;
            left: 13px;
            top: 7px;
            z-index: 3000;
        }
&#10;        /* Styles used by the default GetFeatureInfo output, added to make IE happy */
        table.featureInfo, table.featureInfo td, table.featureInfo th {
            border: 1px solid #ddd;
            border-collapse: collapse;
            margin: 0;
            padding: 0;
            font-size: 90%;
            padding: .2em .1em;
        }
&#10;        table.featureInfo th {
            padding: .2em .2em;
            font-weight: bold;
            background: #eee;
        }
&#10;        table.featureInfo td {
            background: #fff;
        }
&#10;        table.featureInfo tr.odd td {
            background: #eee;
        }
&#10;        table.featureInfo caption {
            text-align: left;
            font-size: 100%;
            font-weight: bold;
            padding: .2em .2em;
        }
    &lt;/style&gt;
    &lt;!-- Import OpenLayers, reduced, wms read only version --&gt;
    &lt;script src=&quot;http://www.openlayers.org/api/OpenLayers.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;http://localhost:8080/geoserver/openlayers/OpenLayers.js&quot; type=&quot;text/javascript&quot;&gt;
    &lt;/script&gt;
    &lt;script defer=&quot;defer&quot; type=&quot;text/javascript&quot;&gt;
        var map;
        var mapnik;
        var lonlat;
        var untiled;
        var tiled;
        var pureCoverage = false;
        // pink tile avoidance
        OpenLayers.IMAGE_RELOAD_ATTEMPTS = 5;
        // make OL compute scale according to WMS spec
        OpenLayers.DOTS_PER_INCH = 25.4 / 0.28;
&#10;        function init(){
            // if this is just a coverage or a group of them, disable a few items,
            // and default to jpeg format
            format = &#39;image/png&#39;;
            if(pureCoverage) {
                document.getElementById(&#39;filterType&#39;).disabled = true;
                document.getElementById(&#39;filter&#39;).disabled = true;
                document.getElementById(&#39;antialiasSelector&#39;).disabled = true;
                document.getElementById(&#39;updateFilterButton&#39;).disabled = true;
                document.getElementById(&#39;resetFilterButton&#39;).disabled = true;
                document.getElementById(&#39;jpeg&#39;).selected = true;
                format = &quot;image/jpeg&quot;;
            }
&#10;            var bounds = new OpenLayers.Bounds(
                -6.92433643341064, 33.9211540222168,
                -6.7672119140625, 34.0333366394043
            );
&#10;            var options = {
                controls: [],
                maxExtent: bounds,
                maxResolution: 0.0006137676537037,
                projection: &quot;EPSG:900913&quot;,
                units: &#39;m&#39;
            };
            map = new OpenLayers.Map(&#39;map&#39;, options);
            mapnik = new OpenLayers.Layer.OSM();
&#10;            // setup tiled layer
            tiled = new OpenLayers.Layer.WMS(
                &quot;Region_Rabat:routes - Tiled&quot;, &quot;http://localhost:8080/geoserver/Region_Rabat/wms&quot;,
                {
                    LAYERS: &#39;Region_Rabat:routes&#39;,
                    STYLES: &#39;&#39;,
                    format: format,
                    tiled: true,
                    tilesOrigin : map.maxExtent.left + &#39;,&#39; + map.maxExtent.bottom
                },
                {
                    buffer: 0,
                    displayOutsideMaxExtent: true,
                    isBaseLayer: true,
                    yx : {&#39;EPSG:900913&#39; : false}
                } 
            );
&#10;            // setup single tiled layer
            untiled = new OpenLayers.Layer.WMS(
                &quot;Region_Rabat:routes - Untiled&quot;, &quot;http://localhost:8080/geoserver/Region_Rabat/wms&quot;,
                {
                    LAYERS: &#39;Region_Rabat:routes&#39;,
                    STYLES: &#39;&#39;,
                    format: format
                },
                {
                   singleTile: true, 
                   ratio: 1, 
                   isBaseLayer: true,
                   yx : {&#39;EPSG:900913&#39; : false}
                } 
            );
&#10;          lonlat = new OpenLayers.LonLat(-6.588, 33.571).transform(
        new OpenLayers.Projection(&quot;EPSG:4326&quot;), // transform from WGS 1984
        new OpenLayers.Projection(&quot;EPSG:900913&quot;) // to Spherical Mercator
      );
            map = new OpenLayers.Map(&quot;map&quot;,{
            layers:[mapnik,tiled,untiled],
            center: cent,
            zoom: 10
        });
&#10;            // build up all controls
            map.addControl(new OpenLayers.Control.PanZoomBar({
                position: new OpenLayers.Pixel(2, 15)
            }));
            map.addControl(new OpenLayers.Control.Navigation());
            map.addControl(new OpenLayers.Control.Scale($(&#39;scale&#39;)));
            map.addControl(new OpenLayers.Control.MousePosition({element: $(&#39;location&#39;)}));
            map.zoomToExtent(bounds);
&#10;            // wire up the option button
            var options = document.getElementById(&quot;options&quot;);
            options.onclick = toggleControlPanel;
&#10;            // support GetFeatureInfo
            map.events.register(&#39;click&#39;, map, function (e) {
                document.getElementById(&#39;nodelist&#39;).innerHTML = &quot;Loading... please wait...&quot;;
                var params = {
                    REQUEST: &quot;GetFeatureInfo&quot;,
                    EXCEPTIONS: &quot;application/vnd.ogc.se_xml&quot;,
                    BBOX: map.getExtent().toBBOX(),
                    SERVICE: &quot;WMS&quot;,
                    INFO_FORMAT: &#39;text/html&#39;,
                    QUERY_LAYERS: map.layers[0].params.LAYERS,
                    FEATURE_COUNT: 50,
                    Layers: &#39;Region_Rabat:routes&#39;,
                    WIDTH: map.size.w,
                    HEIGHT: map.size.h,
                    format: format,
                    styles: map.layers[0].params.STYLES,
                    srs: map.layers[0].params.SRS};
&#10;                // handle the wms 1.3 vs wms 1.1 madness
                if(map.layers[0].params.VERSION == &quot;1.3.0&quot;) {
                    params.version = &quot;1.3.0&quot;;
                    params.j = parseInt(e.xy.x);
                    params.i = parseInt(e.xy.y);
                } else {
                    params.version = &quot;1.1.1&quot;;
                    params.x = parseInt(e.xy.x);
                    params.y = parseInt(e.xy.y);
                }
&#10;                // merge filters
                if(map.layers[0].params.CQL_FILTER != null) {
                    params.cql_filter = map.layers[0].params.CQL_FILTER;
                } 
                if(map.layers[0].params.FILTER != null) {
                    params.filter = map.layers[0].params.FILTER;
                }
                if(map.layers[0].params.FEATUREID) {
                    params.featureid = map.layers[0].params.FEATUREID;
                }
                OpenLayers.loadURL(&quot;http://localhost:8080/geoserver/Region_Rabat/wms&quot;, params, this, setHTML, setHTML);
                OpenLayers.Event.stop(e);
            });
        }
&#10;        // sets the HTML provided into the nodelist element
        function setHTML(response){
            document.getElementById(&#39;nodelist&#39;).innerHTML = response.responseText;
        };
&#10;        // shows/hide the control panel
        function toggleControlPanel(event){
            var toolbar = document.getElementById(&quot;toolbar&quot;);
            if (toolbar.style.display == &quot;none&quot;) {
                toolbar.style.display = &quot;block&quot;;
            }
            else {
                toolbar.style.display = &quot;none&quot;;
            }
            event.stopPropagation();
            map.updateSize()
        }
&#10;        // Tiling mode, can be &#39;tiled&#39; or &#39;untiled&#39;
        function setTileMode(tilingMode){
            if (tilingMode == &#39;tiled&#39;) {
                untiled.setVisibility(false);
                tiled.setVisibility(true);
                map.setBaseLayer(tiled);
            }
            else {
                untiled.setVisibility(true);
                tiled.setVisibility(false);
                map.setBaseLayer(untiled);
            }
        }
&#10;        // Transition effect, can be null or &#39;resize&#39;
        function setTransitionMode(transitionEffect){
            if (transitionEffect === &#39;resize&#39;) {
                tiled.transitionEffect = transitionEffect;
                untiled.transitionEffect = transitionEffect;
            }
            else {
                tiled.transitionEffect = null;
                untiled.transitionEffect = null;
            }
        }
&#10;        // changes the current tile format
        function setImageFormat(mime){
            // we may be switching format on setup
            if(tiled == null)
              return;
&#10;            tiled.mergeNewParams({
                format: mime
            });
            untiled.mergeNewParams({
                format: mime
            });
            /*
            var paletteSelector = document.getElementById(&#39;paletteSelector&#39;)
            if (mime == &#39;image/jpeg&#39;) {
                paletteSelector.selectedIndex = 0;
                setPalette(&#39;&#39;);
                paletteSelector.disabled = true;
            }
            else {
                paletteSelector.disabled = false;
            }
            */
        }
&#10;        // sets the chosen style
        function setStyle(style){
            // we may be switching style on setup
            if(tiled == null)
              return;
&#10;            tiled.mergeNewParams({
                styles: style
            });
            untiled.mergeNewParams({
                styles: style
            });
        }
&#10;        // sets the chosen WMS version
        function setWMSVersion(wmsVersion){
            // we may be switching style on setup
            if(wmsVersion == null)
              return;
&#10;            if(wmsVersion == &quot;1.3.0&quot;) {
               origin = map.maxExtent.bottom + &#39;,&#39; + map.maxExtent.left;
            } else {
               origin = map.maxExtent.left + &#39;,&#39; + map.maxExtent.bottom;
            }
&#10;            tiled.mergeNewParams({
                version: wmsVersion,
                tilesOrigin : origin
            });
            untiled.mergeNewParams({
                version: wmsVersion
            });
        }
&#10;        function setAntialiasMode(mode){
            tiled.mergeNewParams({
                format_options: &#39;antialias:&#39; + mode
            });
            untiled.mergeNewParams({
                format_options: &#39;antialias:&#39; + mode
            });
        }
&#10;        function setPalette(mode){
            if (mode == &#39;&#39;) {
                tiled.mergeNewParams({
                    palette: null
                });
                untiled.mergeNewParams({
                    palette: null
                });
            }
            else {
                tiled.mergeNewParams({
                    palette: mode
                });
                untiled.mergeNewParams({
                    palette: mode
                });
            }
        }
&#10;        function setWidth(size){
            var mapDiv = document.getElementById(&#39;map&#39;);
            var wrapper = document.getElementById(&#39;wrapper&#39;);
&#10;            if (size == &quot;auto&quot;) {
                // reset back to the default value
                mapDiv.style.width = null;
                wrapper.style.width = null;
            }
            else {
                mapDiv.style.width = size + &quot;px&quot;;
                wrapper.style.width = size + &quot;px&quot;;
            }
            // notify OL that we changed the size of the map div
            map.updateSize();
        }
&#10;        function setHeight(size){
            var mapDiv = document.getElementById(&#39;map&#39;);
&#10;            if (size == &quot;auto&quot;) {
                // reset back to the default value
                mapDiv.style.height = null;
            }
            else {
                mapDiv.style.height = size + &quot;px&quot;;
            }
            // notify OL that we changed the size of the map div
            map.updateSize();
        }
&#10;        function updateFilter(){
            if(pureCoverage)
              return;
&#10;            var filterType = document.getElementById(&#39;filterType&#39;).value;
            var filter = document.getElementById(&#39;filter&#39;).value;
&#10;            // by default, reset all filters
            var filterParams = {
                filter: null,
                cql_filter: null,
                featureId: null
            };
            if (OpenLayers.String.trim(filter) != &quot;&quot;) {
                if (filterType == &quot;cql&quot;) 
                    filterParams[&quot;cql_filter&quot;] = filter;
                if (filterType == &quot;ogc&quot;) 
                    filterParams[&quot;filter&quot;] = filter;
                if (filterType == &quot;fid&quot;) 
                    filterParams[&quot;featureId&quot;] = filter;
            }
            // merge the new filter definitions
            mergeNewParams(filterParams);
        }
&#10;        function resetFilter() {
            if(pureCoverage)
              return;
&#10;            document.getElementById(&#39;filter&#39;).value = &quot;&quot;;
            updateFilter();
        }
&#10;        function mergeNewParams(params){
            tiled.mergeNewParams(params);
            untiled.mergeNewParams(params);
        }
    &lt;/script&gt;
&lt;/head&gt;
&lt;body onload=&quot;init()&quot;&gt;
&#10;&lt;p&gt;My HTML page with an embedded map&lt;/p&gt;
&#10;    &lt;div id=&quot;toolbar&quot; style=&quot;display: none;&quot;&gt;
        &lt;ul&gt;
            &lt;li&gt;
                &lt;a&gt;WMS version:&lt;/a&gt;
                &lt;select id=&quot;wmsVersionSelector&quot; onchange=&quot;setWMSVersion(value)&quot;&gt;
                    &lt;option value=&quot;1.1.1&quot;&gt;1.1.1&lt;/option&gt;
                    &lt;option value=&quot;1.3.0&quot;&gt;1.3.0&lt;/option&gt;
                &lt;/select&gt;
            &lt;/li&gt;
            &lt;li&gt;
                &lt;a&gt;Tiling:&lt;/a&gt;
                &lt;select id=&quot;tilingModeSelector&quot; onchange=&quot;setTileMode(value)&quot;&gt;
                    &lt;option value=&quot;untiled&quot;&gt;Single tile&lt;/option&gt;
                    &lt;option value=&quot;tiled&quot;&gt;Tiled&lt;/option&gt;
                &lt;/select&gt;
            &lt;/li&gt;
            &lt;li&gt;
                &lt;a&gt;Transition effect:&lt;/a&gt;
                &lt;select id=&quot;transitionEffectSelector&quot; onchange=&quot;setTransitionMode(value)&quot;&gt;
                    &lt;option value=&quot;&quot;&gt;None&lt;/option&gt;
                    &lt;option value=&quot;resize&quot;&gt;Resize&lt;/option&gt;
                &lt;/select&gt;
            &lt;/li&gt;
            &lt;li&gt;
                &lt;a&gt;Antialias:&lt;/a&gt;
                &lt;select id=&quot;antialiasSelector&quot; onchange=&quot;setAntialiasMode(value)&quot;&gt;
                    &lt;option value=&quot;full&quot;&gt;Full&lt;/option&gt;
                    &lt;option value=&quot;text&quot;&gt;Text only&lt;/option&gt;
                    &lt;option value=&quot;none&quot;&gt;Disabled&lt;/option&gt;
                &lt;/select&gt;
            &lt;/li&gt;
            &lt;li&gt;
                &lt;a&gt;Format:&lt;/a&gt;
                &lt;select id=&quot;imageFormatSelector&quot; onchange=&quot;setImageFormat(value)&quot;&gt;
                    &lt;option value=&quot;image/png&quot;&gt;PNG 24bit&lt;/option&gt;
                    &lt;option value=&quot;image/png8&quot;&gt;PNG 8bit&lt;/option&gt;
                    &lt;option value=&quot;image/gif&quot;&gt;GIF&lt;/option&gt;
                    &lt;option id=&quot;jpeg&quot; value=&quot;image/jpeg&quot;&gt;JPEG&lt;/option&gt;
                &lt;/select&gt;
            &lt;/li&gt;
            &lt;li&gt;
                &lt;a&gt;Styles:&lt;/a&gt;
                &lt;select id=&quot;imageFormatSelector&quot; onchange=&quot;setStyle(value)&quot;&gt;
                    &lt;option value=&quot;&quot;&gt;Default&lt;/option&gt;
                &lt;/select&gt;
            &lt;/li&gt;
            &lt;!-- Commented out for the moment, some code needs to be extended in 
                 order to list the available palettes
            &lt;li&gt;
                &lt;a&gt;Palette:&lt;/a&gt;
                &lt;select id=&quot;paletteSelector&quot; onchange=&quot;setPalette(value)&quot;&gt;
                    &lt;option value=&quot;&quot;&gt;None&lt;/option&gt;
                    &lt;option value=&quot;safe&quot;&gt;Web safe&lt;/option&gt;
                &lt;/select&gt;
            &lt;/li&gt;
            --&gt;
            &lt;li&gt;
                &lt;a&gt;Width/Height:&lt;/a&gt;
                &lt;select id=&quot;widthSelector&quot; onchange=&quot;setWidth(value)&quot;&gt;
                    &lt;!--
                    These values come from a statistics of the viewable area given a certain screen area
                    (but have been adapted a litte, simplified numbers, added some resolutions for wide screen)
                    You can find them here: http://www.evolt.org/article/Real_World_Browser_Size_Stats_Part_II/20/2297/
                    --&gt;&lt;option value=&quot;auto&quot;&gt;Auto&lt;/option&gt;
                    &lt;option value=&quot;600&quot;&gt;600&lt;/option&gt;
                    &lt;option value=&quot;750&quot;&gt;750&lt;/option&gt;
                    &lt;option value=&quot;950&quot;&gt;950&lt;/option&gt;
                    &lt;option value=&quot;1000&quot;&gt;1000&lt;/option&gt;
                    &lt;option value=&quot;1200&quot;&gt;1200&lt;/option&gt;
                    &lt;option value=&quot;1400&quot;&gt;1400&lt;/option&gt;
                    &lt;option value=&quot;1600&quot;&gt;1600&lt;/option&gt;
                    &lt;option value=&quot;1900&quot;&gt;1900&lt;/option&gt;
                &lt;/select&gt;
                &lt;select id=&quot;heigthSelector&quot; onchange=&quot;setHeight(value)&quot;&gt;
                    &lt;option value=&quot;auto&quot;&gt;Auto&lt;/option&gt;
                    &lt;option value=&quot;300&quot;&gt;300&lt;/option&gt;
                    &lt;option value=&quot;400&quot;&gt;400&lt;/option&gt;
                    &lt;option value=&quot;500&quot;&gt;500&lt;/option&gt;
                    &lt;option value=&quot;600&quot;&gt;600&lt;/option&gt;
                    &lt;option value=&quot;700&quot;&gt;700&lt;/option&gt;
                    &lt;option value=&quot;800&quot;&gt;800&lt;/option&gt;
                    &lt;option value=&quot;900&quot;&gt;900&lt;/option&gt;
                    &lt;option value=&quot;1000&quot;&gt;1000&lt;/option&gt;
                &lt;/select&gt;
            &lt;/li&gt;
            &lt;li&gt;
                &lt;a&gt;Filter:&lt;/a&gt;
                &lt;select id=&quot;filterType&quot;&gt;
                    &lt;option value=&quot;cql&quot;&gt;CQL&lt;/option&gt;
                    &lt;option value=&quot;ogc&quot;&gt;OGC&lt;/option&gt;
                    &lt;option value=&quot;fid&quot;&gt;FeatureID&lt;/option&gt;
                &lt;/select&gt;
                &lt;input type=&quot;text&quot; size=&quot;80&quot; id=&quot;filter&quot;/&gt;
                &lt;img id=&quot;updateFilterButton&quot; src=&quot;http://localhost:8080/geoserver/openlayers/img/east-mini.png&quot; onClick=&quot;updateFilter()&quot; title=&quot;Apply filter&quot;/&gt;
                &lt;img id=&quot;resetFilterButton&quot; src=&quot;http://localhost:8080/geoserver/openlayers/img/cancel.png&quot; onClick=&quot;resetFilter()&quot; title=&quot;Reset filter&quot;/&gt;
            &lt;/li&gt;
        &lt;/ul&gt;
    &lt;/div&gt;
    &lt;div id=&quot;map&quot;&gt;
        &lt;img id=&quot;options&quot; title=&quot;Toggle options toolbar&quot; src=&quot;http://localhost:8080/geoserver/options.png&quot;/&gt;
    &lt;/div&gt;
    &lt;div id=&quot;wrapper&quot;&gt;
        &lt;div id=&quot;location&quot;&gt;location&lt;/div&gt;
        &lt;div id=&quot;scale&quot;&gt;
        &lt;/div&gt;
    &lt;/div&gt;
    &lt;div id=&quot;nodelist&quot;&gt;
        &lt;em&gt;Click on the map to get feature info&lt;/em&gt;
    &lt;/div&gt;
&lt;/body&gt;</code></pre>
<p>&lt;/html&gt;</p>
<p>Thank you for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-apache-tomcat" rel="tag" title="see questions tagged &#39;apache-tomcat&#39;">apache-tomcat</span> <span class="post-tag tag-link-geoserver" rel="tag" title="see questions tagged &#39;geoserver&#39;">geoserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '14, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/e276dd869c646f762e247187ce1f40e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yassine10&#39;s gravatar image" />
<p><span>yassine10</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yassine10 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Apr '14, 03:30</strong> </span></p>
</div>
</div>
<div id="comments-container-32568" class="comments-container">
<span id="32573"></span>
<div id="comment-32573" class="comment">
<div id="post-32573-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What's the error? What doesn't work? Are you aware that you need OpenLayers when using this code example?</p>
</div>
<div id="comment-32573-info" class="comment-info">
<span class="comment-age">(23 Apr '14, 16:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="32576"></span>
<div id="comment-32576" class="comment">
<div id="post-32576-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yeah i have a file openlayers in my project that contains a openlayers.js !! what i want is to have a base map to my layers !! when i run the project it showed just my layer without a base map...i don't know if you get what i want</p>
</div>
<div id="comment-32576-info" class="comment-info">
<span class="comment-age">(23 Apr '14, 17:00)</span> <span class="comment-user userinfo">yassine10</span>
</div>
</div>
<span id="32581"></span>
<div id="comment-32581" class="comment">
<div id="post-32581-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I download teh OpenLayers library and add it in the same directory to my project !! am i wrong in something ?</p>
</div>
<div id="comment-32581-info" class="comment-info">
<span class="comment-age">(23 Apr '14, 19:24)</span> <span class="comment-user userinfo">yassine10</span>
</div>
</div>
<span id="32584"></span>
<div id="comment-32584" class="comment">
<div id="post-32584-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you upload your project to some freehoster or share your project URL for further analysis? That would make things way easier for everyone.</p>
</div>
<div id="comment-32584-info" class="comment-info">
<span class="comment-age">(23 Apr '14, 20:59)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="32592"></span>
<div id="comment-32592" class="comment">
<div id="post-32592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>when i run the project, it shows just the layer that i have in GeoServer !! what i want now is to show it with a base map OpenStreet Maps...</p>
</div>
<div id="comment-32592-info" class="comment-info">
<span class="comment-age">(23 Apr '14, 23:11)</span> <span class="comment-user userinfo">yassine10</span>
</div>
</div>
</div>
<div id="comment-tools-32568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32568-form-container" class="comment-form-container">
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

<span id="74900"></span>

<div id="answer-container-74900" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74900-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-74900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>GeoFabrik is a company which specializes in working with OpenStreetMap. They provide a variety of free extracts in shapefile and raw OSM format on their download website. The advantage of downloading GeoFabrik data is that it is updated every day, and it’s easy and reliable. One disadvantage is that the data is extracted by country, and not all countries are available.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 May '20, 06:27</strong></p>
<img src="https://secure.gravatar.com/avatar/d65bf3b998394330195797de81ff2de4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smith%20Hennry&#39;s gravatar image" />
<p><span>Smith Hennry</span><br />
<span class="score" title="-20 reputation points">-20</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smith Hennry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74900" class="comments-container">
<span id="74901"></span>
<div id="comment-74901" class="comment">
<div id="post-74901-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>How does that answer relate to the question and are you aware you are answering to a 6 year old problem?</p>
</div>
<div id="comment-74901-info" class="comment-info">
<span class="comment-age">(19 May '20, 08:24)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-74900" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74900-form-container" class="comment-form-container">
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

