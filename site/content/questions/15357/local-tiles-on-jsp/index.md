+++
type = "question"
title = "local tiles on jsp"
description = '''Hi, I have set up osm2pgsql,mapnik on ubuntu server. I have also generated tiles locally. Now I want to display these tiles on map in a JSP page. I am using open layers. I have been trying it. The code works fine in html, but if same thing I do in a jsp page, it does not open map tiles. Only pink ca...'''
date = "2012-08-22T08:32:00Z"
lastmod = "2012-08-23T14:38:00Z"
weight = 15357
keywords = [ "jsp" ]
aliases = [ "/questions/15357" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [local tiles on jsp](/questions/15357/local-tiles-on-jsp)

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
<span id="post-15357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15357-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have set up osm2pgsql,mapnik on ubuntu server. I have also generated tiles locally. Now I want to display these tiles on map in a JSP page. I am using open layers. I have been trying it. The code works fine in html, but if same thing I do in a jsp page, it does not open map tiles. Only pink canvas is displayed. On rightclick, it displayes map tile path as "/LocalFolder///.png". Error screen shot is attached. And source code is given below.</p>
<p>Please let me know what is the procedure I should follow to display local map on a jsp page(Tomcat server),</p>
<p>Code:</p>
<pre><code>function init() {
&#10;        map = new OpenLayers.Map ($(&#39;map&#39;), {
            controls:[
                new OpenLayers.Control.Navigation(),
                new OpenLayers.Control.PanZoomBar(),
                new OpenLayers.Control.Permalink(),
                new OpenLayers.Control.ScaleLine({geodesic: true}),
                new OpenLayers.Control.Permalink(&#39;permalink&#39;),
                new OpenLayers.Control.MousePosition(),                    
                new OpenLayers.Control.Attribution()],
           maxExtent: new OpenLayers.Bounds(-180,-90,180,90),
            minExtent: new OpenLayers.Bounds(-1,-1,1,1),
&#10;            &#39;maxResolution&#39;: 360/512,
            numZoomLevels: 4,
            units: &#39;dd&#39;,
            projection: new OpenLayers.Projection(&quot;EPSG:900913&quot;),
          //  displayProjection: new OpenLayers.Projection(&quot;EPSG:4326&quot;)
        displayProjection: new OpenLayers.Projection(&quot;EPSG:900913&quot;)
        } );
&#10;        layerMapnik = new OpenLayers.Layer.OSM.Mapnik(&quot;Mapnik&quot;);
        layerMapnik.setOpacity(0.4);
      //  map.addLayer(layerMapnik);
&#10;        layerCycleMap = new OpenLayers.Layer.OSM.CycleMap(&quot;CycleMap&quot;);
        layerCycleMap.setOpacity(0.4);
      //  map.addLayer(layerCycleMap);
&#10;        // This is the layer that uses the locally stored tiles
       var newLayer = new OpenLayers.Layer.OSM(&quot;Localhost&quot;,
         &quot;IndiaMap/${z}/${x}/${y}.png&quot;, {numZoomLevels: 4, alpha: true,
         isBaseLayer: true});
        //var newLayer = new OpenLayers.Layer.OSM(&quot;LocalTiles&quot;,
         &quot;IndiaMap/${0}/${0}/${0}.png&quot;, {numZoomLevels: 10, alpha: true,
         isBaseLayer: true});
        //layerLocalMap = new OpenLayers.Layer.OSM.LocalMap(&quot;LocalMap&quot;);
    //  layerLocalMap.setOpacity(0.4);
    //newLayer.setOpacity(0.6);
        map.addLayer(newLayer);
        // This is the end of the layer
&#10;            var switcherControl = new OpenLayers.Control.LayerSwitcher();
            map.addControl(switcherControl);
            switcherControl.maximizeControl();
&#10;        if( ! map.getCenter() ){
            var lonLat = new OpenLayers.LonLat(lon, lat).transform(new  OpenLayers.Projection(&quot;EPSG:4326&quot;), map.getProjectionObject());
            map.setCenter (lonLat, zoom);
        }
    }</code></pre>
<p>maperror.png</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-jsp" rel="tag" title="see questions tagged &#39;jsp&#39;">jsp</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '12, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '12, 12:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span></p>
</div>
</div>
<div id="comments-container-15357" class="comments-container">
&#10;</div>
<div id="comment-tools-15357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15357-form-container" class="comment-form-container">
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

<span id="15376"></span>

<div id="answer-container-15376" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15376-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know how tomcat processes URL, but I will suggest:</p>
<ul>
<li>check which URL your browser send to the server for the tiles (with firebug or webkit network analyser)</li>
<li>look at the access log on your server to see what request your server process</li>
</ul>
<p>Maybe your server process ${x} as a variable in the URL … in this case, it should be a way to bypass that (with an escape pattern)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '12, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-15376" class="comments-container">
<span id="15449"></span>
<div id="comment-15449" class="comment">
<div id="post-15449-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the help. Putting escape character solved the problem.</p>
<p>One more query please. I have generated tiles for India map using Mapnik. I can display them on a jsp page using openlayers. Do I need to run a separate map server now for serving the tiles OR only if I copy the tiles on my main server and give the path of that folder in my jsp code will do?</p>
<p>Basically, I want to know if map tiles are stored in a local folder and accessed from there in a jsp page, why is a map server required?</p>
</div>
<div id="comment-15449-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 14:08)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="15451"></span>
<div id="comment-15451" class="comment">
<div id="post-15451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you want only serve tiles, mapserver isn't needed. You can serve tiles with any file http server.</p>
<p>Don't forget to close your question if it's ok.</p>
</div>
<div id="comment-15451-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 14:38)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
</div>
<div id="comment-tools-15376" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15376-form-container" class="comment-form-container">
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

