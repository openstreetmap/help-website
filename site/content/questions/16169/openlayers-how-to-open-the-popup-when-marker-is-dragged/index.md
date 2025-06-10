+++
type = "question"
title = "OpenLayers - how to open the popup when marker is dragged"
description = '''I have created the draggable marker using vector layer. Now I have to open a popup at dragend I have tried the following code: vectors = new OpenLayers.Layer.Vector(&quot;Vector Layer&quot;,{  styleMap: new OpenLayers.StyleMap({  externalGraphic: &quot;images/red-dot.png&quot;,  graphicOpacity: 1.0,  graphicWith: 16,  ...'''
date = "2012-09-17T12:33:00Z"
lastmod = "2012-09-17T13:31:00Z"
weight = 16169
keywords = [ "marker", "drag", "popup", "openlayers" ]
aliases = [ "/questions/16169" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OpenLayers - how to open the popup when marker is dragged](/questions/16169/openlayers-how-to-open-the-popup-when-marker-is-dragged)

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
<span id="post-16169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16169-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-16169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have created the draggable marker using vector layer. Now I have to open a popup at dragend I have tried the following code:</p>
<p>vectors = new OpenLayers.Layer.Vector("Vector Layer",{ styleMap: new OpenLayers.StyleMap({ externalGraphic: "images/red-dot.png", graphicOpacity: 1.0, graphicWith: 16, graphicHeight: 26, graphicYOffset: -26 }) });</p>
<pre><code>        point = new OpenLayers.Geometry.Point(77.768553,23.402765);
        vectors.addFeatures([new OpenLayers.Feature.Vector(point)]);
        map1.addLayer(vectors);</code></pre>
<p>var drag=new OpenLayers.Control.DragFeature(vectors);</p>
<pre><code>        map1.addControl(drag);
        drag.activate();</code></pre>
<p>vectors.events.on( { 'dragend': onFeatureSelect, 'dragstart': onFeatureUnselect }</p>
<p>function onFeatureSelect(evt) { try {</p>
<pre><code>    feature = evt.feature;
    var zoom = map1.getZoom();
&#10;    popup = new OpenLayers.Popup.FramedCloud(&quot;featurePopup&quot;,
                             feature.geometry.getBounds().getCenterLonLat(),
                             new OpenLayers.Size(100,100),
                             &quot;&lt;h2&gt;&quot;+feature.attributes.title + &quot;&lt;/h2&gt;&quot; +
                             feature.attributes.description, 
                             null, true, onPopupClose);
    feature.popup = popup;
    popup.feature = feature;
    map1.addPopup(popup, true);
    }
    catch(e)
    {
        alert(e);
    }
}</code></pre>
<p>function onFeatureUnselect(evt) { feature = evt.feature; if (feature.popup) { popup.feature = null; map1.removePopup(feature.popup); feature.popup.destroy(); feature.popup = null; } }</p>
<p>function onPopupClose(evt) {</p>
<pre><code>    var feature = this.feature;
    if (feature.layer) {
        drag.unselect(feature);
    } else {
&#10;        this.destroy();
    }
}</code></pre>
<p>but it is not working. Please suggest any solution.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-drag" rel="tag" title="see questions tagged &#39;drag&#39;">drag</span> <span class="post-tag tag-link-popup" rel="tag" title="see questions tagged &#39;popup&#39;">popup</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '12, 12:33</strong></p>
<img src="https://secure.gravatar.com/avatar/4103ee989b09b034a93eac604cdbdca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Niki%20Kallurwar&#39;s gravatar image" />
<p><span>Niki Kallurwar</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Niki Kallurwar has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '12, 13:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-16169" class="comments-container">
<span id="16170"></span>
<div id="comment-16170" class="comment">
<div id="post-16170-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There are a bunch of OpenLayers mailing lists described <a href="http://trac.osgeo.org/openlayers/wiki/MailingLists">here</a>, and other useful resources, including an IRC channel, <a href="http://trac.osgeo.org/openlayers/">here</a>.</p>
</div>
<div id="comment-16170-info" class="comment-info">
<span class="comment-age">(17 Sep '12, 13:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-16169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16169-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

