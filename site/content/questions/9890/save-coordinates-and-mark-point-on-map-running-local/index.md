+++
type = "question"
title = "[closed] save coordinates and mark point on map (running local)"
description = '''Hi, I try to mark points on a OSM map temporarily and store the coordinates to them locally at the same time. The site is just running locally (using Aptana). My issue is that as soon as I activate the draw.feature layer for points the local store routine stops working... The JS code below for refer...'''
date = "2012-01-10T18:49:00Z"
lastmod = "2012-01-10T18:49:00Z"
weight = 9890
keywords = [ "draw", "local", "store" ]
aliases = [ "/questions/9890" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] save coordinates and mark point on map (running local)](/questions/9890/save-coordinates-and-mark-point-on-map-running-local)

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
<span id="post-9890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9890-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I try to mark points on a OSM map temporarily and store the coordinates to them locally at the same time. The site is just running locally (using Aptana). My issue is that as soon as I activate the draw.feature layer for points the local store routine stops working... The JS code below for reference. Any idea how to do this? Currently I store to local storage, but I am open to other options for this (i.e. export to file or something like this)</p>
<hr />
<p>var lon = 13.33; var lat = 52.51; var zoom = 10;</p>
<p>var map, vectors, controls;</p>
<p>OpenLayers.Control.Click = OpenLayers.Class(OpenLayers.Control, {<br />
defaultHandlerOptions: { 'single': true, 'double': false, 'pixelTolerance': 0, 'stopSingle': false, 'stopDouble': false },</p>
<pre><code>    initialize: function(options) {
            this.handlerOptions = OpenLayers.Util.extend(
                {}, this.defaultHandlerOptions
            );
            OpenLayers.Control.prototype.initialize.apply(
                this, arguments
            ); 
            this.handler = new OpenLayers.Handler.Click(
                this, {
                    &#39;click&#39;: this.trigger
                        }, this.handlerOptions
                    );
    },   
    trigger: function(e) {
            var lonlat = new OpenLayers.LonLat(1, 1);
            lonlat = map.getLonLatFromViewPortPx(e.xy);
            var projout = new OpenLayers.Projection(&quot;EPSG:4326&quot;);
            lonlat.transform(map.getProjectionObject(), projout);
            reclat = lonlat.lat;
            reclon = lonlat.lon; 
            var blockrec= prompt(reclat + &quot; lat, &quot; +
                             + reclon + &quot; lon&quot;,&quot;&quot;);
            if (blockrec!=null &amp;&amp; blockrec!=&quot;&quot;)
            { 
                var latulon = &quot;, &quot; + reclat + &quot;, &quot; + reclon;
                alert(blockrec + latulon);
                localStorage.setItem(blockrec, latulon ); 
    }
 }
}); 
        function init(){
            map = new OpenLayers.Map(&#39;map&#39;);
            var osm = new OpenLayers.Layer.OSM(&quot;OSM&quot;);
            var newl = new OpenLayers.Layer.Text( &quot;text&quot;, {location: &quot;textfile.txt&quot;} );
            var pointLayer = new OpenLayers.Layer.Vector(&quot;Point Layer&quot;);
&#10;            map.addLayers([osm, newl, pointLayer]);
&#10;            var click = new OpenLayers.Control.Click();
            map.addControl(click);
            click.activate();
&#10;            map.addControl(new OpenLayers.Control.LayerSwitcher());
            map.addControl(new OpenLayers.Control.MousePosition());
&#10;            var reg = new OpenLayers.Control.DrawFeature(pointLayer,OpenLayers.Handler.Point);
            map.addControl(reg);
            reg.activate();
&#10;            map.setCenter(
                    new OpenLayers.LonLat(lon, lat).transform(
                    new OpenLayers.Projection(&quot;EPSG:4326&quot;),
                    map.getProjectionObject()
                    ), zoom
                );</code></pre>
<p>}</p>
<hr />
<p>Thanx!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-draw" rel="tag" title="see questions tagged &#39;draw&#39;">draw</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-store" rel="tag" title="see questions tagged &#39;store&#39;">store</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jan '12, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/4044250d5a0cbfeca80890694d876d92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dada3781&#39;s gravatar image" />
<p><span>dada3781</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dada3781 has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>11 Jan '12, 08:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-9890" class="comments-container">
&#10;</div>
<div id="comment-tools-9890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9890-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "This is a support system for OpenStreetMap contributors, not OpenLayers. See http://openlayers.org for more information on OpenLayers." by Andy Allan 11 Jan '12, 08:45

</div>

</div>

</div>

