+++
type = "question"
title = "OpenLayers - limit the number of zoom levels"
description = '''Hello, I&#x27;m trying to limit the zoom levels of my OpenLayers application. I want to make max zoom level to be 14 using standard zoom levels (nothing fancy like fractional zooms and resolutions) and that is all. I&#x27;ve read this article: http://trac.osgeo.org/openlayers/wiki/SettingZoomLevels I&#x27;ve tried...'''
date = "2012-06-20T18:52:00Z"
lastmod = "2016-06-09T11:48:00Z"
weight = 13666
keywords = [ "openlayers", "zoom" ]
aliases = [ "/questions/13666" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [OpenLayers - limit the number of zoom levels](/questions/13666/openlayers-limit-the-number-of-zoom-levels)

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
<span id="post-13666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13666-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-13666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm trying to limit the zoom levels of my OpenLayers application. I want to make max zoom level to be 14 using standard zoom levels (nothing fancy like fractional zooms and resolutions) and that is all. I've read this article: <a href="http://trac.osgeo.org/openlayers/wiki/SettingZoomLevels">http://trac.osgeo.org/openlayers/wiki/SettingZoomLevels</a> I've tried tons of combinations of maxExtent, minExtent, maxResolution, minResolution, numZoomLevels and so on... the user is always able to go beyond ZL 14 :(</p>
<p>Here is my map definition:</p>
<pre><code>var options = {
        projection: new OpenLayers.Projection(&quot;EPSG:900913&quot;),
        units: &quot;m&quot;,
        controls: [
            new OpenLayers.Control.PanZoomBar(),
            new OpenLayers.Control.LayerSwitcher(),
            new OpenLayers.Control.Permalink(),
            new OpenLayers.Control.Attribution(),
            new OpenLayers.Control.Navigation(),
            new OpenLayers.Control.ScaleLine()
        ],
        displayProjection: new OpenLayers.Projection(&quot;EPSG:4326&quot;)
    }
    map = new OpenLayers.Map(&quot;mapdiv&quot;,options);
    map.addLayer(new OpenLayers.Layer.OSM());</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '12, 18:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>21 Jun '12, 23:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f92748c8fa508a936bcf2169b30cabf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikonor&#39;s gravatar image" />
<p><span>ikonor</span><br />
<span class="score" title="1286 reputation points"><span>1.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span></p>
</div>
</div>
<div id="comments-container-13666" class="comments-container">
&#10;</div>
<div id="comment-tools-13666" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13666-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="13713"></span>

<div id="answer-container-13713" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13713-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-13713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For tile based layers you can set zoomOffset and resolutions. See Wiki <a href="https://wiki.openstreetmap.org/wiki/OpenLayers_Simple_Example#Restricting_the_bounds_.26_zoom_levels">Restricting the bounds &amp; zoom levels</a> and example <a href="http://www.wightpaths.co.uk/">Isle of Wight Paths</a>. Setting maxResolution and numZoomLevels along with serverResolutions should also work, see <a href="http://openlayers.org/dev/examples/bing-tiles-restrictedzoom.html">Bing Tiles with a Subset of Resolutions Example</a>.</p>
<p>For convenience, I use the serverResolutions array defined in the Bing layer, which corresponds to OSM resolutions (apart from extending to level 21):</p>
<pre><code>var resolutions = OpenLayers.Layer.Bing.prototype.serverResolutions.slice(14, 19);
map.addLayer(new OpenLayers.Layer.OSM(null, null, {zoomOffset: 14, resolutions: resolutions}));
&#10;// zoom level relative to zoomOffset
map.setCenter(new OpenLayers.LonLat(-0.1265, 51.5034).transform(
   new OpenLayers.Projection(&quot;EPSG:4326&quot;), map.getProjectionObject()), 0);</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '12, 23:16</strong></p>
<img src="https://secure.gravatar.com/avatar/f92748c8fa508a936bcf2169b30cabf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikonor&#39;s gravatar image" />
<p><span>ikonor</span><br />
<span class="score" title="1286 reputation points"><span>1.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikonor has 4 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-13713" class="comments-container">
&#10;</div>
<div id="comment-tools-13713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13713-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13676"></span>

<div id="answer-container-13676" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13676-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd register an event on movestart (which includes zooming) and prevent zooming if the map's zoomlevel is higher than a certain value</p>
<pre><code>function handleZoom(event) {
    var map = event.object;
    if (map.getZoom() &gt; 14) {
       event.stop(event);
    }
}
var map = new OpenLayers.Map();¨
map.events.register(&#39;zoomstart&#39;, map, handleZoom)</code></pre>
<p>I didn't test this, so you propably need to enhance the event handling function</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '12, 09:07</strong></p>
<img src="https://secure.gravatar.com/avatar/30b87850d86c99d1c4f1f72c9abaeb52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frabron&#39;s gravatar image" />
<p><span>frabron</span><br />
<span class="score" title="361 reputation points">361</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frabron has 2 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-13676" class="comments-container">
<span id="13806"></span>
<div id="comment-13806" class="comment">
<div id="post-13806-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, the first issue was that the event name is 'movestart', not 'zoomstart'. I've changed that and the handler is firing, but I can't stop the event propagation. I keep getting event.stop is not a function. I tried OpenLayers.Event.stop(e) but that seems to do nothing at all. How to get the event from the handler function? The callback argument seem to contain 2 properties - dom element and object (that is not OpenLayers.Event object) and that is all.</p>
</div>
<div id="comment-13806-info" class="comment-info">
<span class="comment-age">(26 Jun '12, 14:49)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
</div>
<div id="comment-tools-13676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13676-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50104"></span>

<div id="answer-container-50104" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50104-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>I found the simplest way to restrict the maxZoom levels for a XYZ layer was to override the getNumZoomLevels method:</strong></p>
<pre><code>  function zoomChanged()
    {
        var coor_from = new OpenLayers.Projection(&quot;EPSG:4326&quot;);
        var coor_to   = new OpenLayers.Projection(&quot;EPSG:900913&quot;);
        var level = map.getZoom();
        var center =   map.getCenter()
        center.transform(coor_to,coor_from);
        var zoomLevel = level;
        var valid =false;
        map.getNumZoomLevels = function(){ return 16; };
        map.isValidZoomLevel = function(zoomLevel) {
            valid = ( (zoomLevel != null) &amp;&amp;
            (zoomLevel &gt;= minzoom) &amp;&amp;
            (zoomLevel &lt;= maxzoom) );
            console.log(valid);
            console.log(map.getZoom());
            if(!valid &amp;&amp; map.getZoom() == 0){
                map.zoomTo(maxzoom - (maxzoom - minzoom)/2);
&#10;            }
            return valid;
        }
        if(valid)
        {
            SetCenterPoint(center.lat, center.lon, map.getZoom());
        }
        return valid;
    }</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '16, 11:48</strong></p>
<img src="https://secure.gravatar.com/avatar/f397095f89218f9edf95c98923d5cbe6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Rajbhar&#39;s gravatar image" />
<p><span>Vijay Rajbhar</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Rajbhar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50104" class="comments-container">
&#10;</div>
<div id="comment-tools-50104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50104-form-container" class="comment-form-container">
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

