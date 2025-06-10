+++
type = "question"
title = "[closed] How to show KML in OSM with automatically refresh ?"
description = '''I&#x27;ve got a complexion with this JavaScript. I&#x27;ve done several research but yet to succeed. Anyone? &amp;lt;script type=&quot;text/javascript&quot;&amp;gt; var map;  function init() { // Create the map object map = new OpenLayers.Map({  allOverlays: true,  controls: [  new OpenLayers.Control.Navigation(),  new OpenLay...'''
date = "2011-08-05T08:46:00Z"
lastmod = "2011-08-05T09:45:00Z"
weight = 6899
keywords = [ "openstreetmap", "kml", "javascript" ]
aliases = [ "/questions/6899" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to show KML in OSM with automatically refresh ?](/questions/6899/how-to-show-kml-in-osm-with-automatically-refresh)

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
<span id="post-6899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6899-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've got a complexion with this JavaScript. I've done several research but yet to succeed. Anyone?</p>
<pre><code>&lt;script type=&quot;text/javascript&quot;&gt;
var map;
&#10;function init() {
// Create the map object
map = new OpenLayers.Map({
        allOverlays: true,
        controls: [
            new OpenLayers.Control.Navigation(),
            new OpenLayers.Control.PanZoom(),
        ]
    });
    var osm_layer = new OpenLayers.Layer.OSM();
    map.addLayer(osm_layer);
&#10;map.setCenter(
            new OpenLayers.LonLat(mylon,mylat).transform(
                new OpenLayers.Projection(&quot;EPSG:4326&quot;),
                map.getProjectionObject()
            ), 12
        ); */        
}
&#10;var KMLURL = &#39;myfile.kml?&#39; + Math.random();
&#10;var MyKmlLayer= new OpenLayers.Layer.Vector(&quot;This Is My KML Layer&quot;, {
        //Set your projection and strategies//
        projection: new OpenLayers.Projection(&quot;EPSG:4326&quot;),
        strategies: [new OpenLayers.Strategy.Fixed()],
        //set the protocol with a url//
        protocol: new OpenLayers.Protocol.HTTP({
            //set the url to your variable//
            url: KMLURL,
            //format this layer as KML//
            format: new OpenLayers.Format.KML({
                //maxDepth is how deep it will follow network links//
                maxDepth: 1,
                //extract styles from the KML Layer//
                extractStyles: true,
                //extract attributes from the KML Layer//
                extractAttributes: true
            })
        })
    });
&#10;window.setInterval(UpdateKmlLayer, 5000, MyKmlLayer);
&#10;function UpdateKmlLayer(layer) {
        //setting loaded to false unloads the layer//
        layer.loaded = false;
        //setting visibility to true forces a reload of the layer//
        layer.setVisibility(true);
        //the refresh will force it to get the new KML data//
        layer.refresh({ force: true, params: { &#39;key&#39;: Math.random()} });
    }
}
&lt;/script&gt;</code></pre>
<p>Thank you in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Aug '11, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/96b4bf504743155d2eef7efd49cea622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zearth&#39;s gravatar image" />
<p><span>zearth</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zearth has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>05 Aug '11, 09:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-6899" class="comments-container">
<span id="6903"></span>
<div id="comment-6903" class="comment">
<div id="post-6903-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>First, this isn't really an OpenStreetMap question, but an OpenLayers one (or even just a JavaScript one) -- you may get an answer by asking in a forum for OpenLayers.</p>
<p>Even then you should try to come up with a better worded question, rather than simply dumping your code and expecting everyone to find the problem. State what you've tried that didn't work, and what results you got instead.</p>
</div>
<div id="comment-6903-info" class="comment-info">
<span class="comment-age">(05 Aug '11, 09:45)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
</div>
<div id="comment-tools-6899" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6899-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Jonathan Bennett 05 Aug '11, 09:41

</div>

</div>

</div>

