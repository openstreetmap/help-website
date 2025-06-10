+++
type = "question"
title = "[closed] Unable to see whole world map by decreasing panzoom bar?"
description = '''I am seeing one weird thing in Openlayers today. I am unable to see whole map by using panzoombar, previously i used too. &amp;lt;html&amp;gt; &amp;lt;head&amp;gt;  &amp;lt;title&amp;gt;OpenLayers Example&amp;lt;/title&amp;gt;  &amp;lt;script src=&quot;http://openlayers.org/api/OpenLayers.js&quot;&amp;gt;&amp;lt;/script&amp;gt;  &amp;lt;/head&amp;gt;  &amp;lt;body&amp;gt;...'''
date = "2012-07-22T23:26:00Z"
lastmod = "2012-07-22T23:26:00Z"
weight = 14488
keywords = [ "openstreetmap", "openlayers" ]
aliases = [ "/questions/14488" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Unable to see whole world map by decreasing panzoom bar?](/questions/14488/unable-to-see-whole-world-map-by-decreasing-panzoom-bar)

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
<span id="post-14488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14488-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am seeing one weird thing in Openlayers today. I am unable to see whole map by using panzoombar, previously i used too.</p>
<pre><code>&lt;html&gt;
&lt;head&gt;
  &lt;title&gt;OpenLayers Example&lt;/title&gt;
    &lt;script src=&quot;http://openlayers.org/api/OpenLayers.js&quot;&gt;&lt;/script&gt;
    &lt;/head&gt;
    &lt;body&gt;
      &lt;div style=&quot;width:100%; height:100%&quot; id=&quot;map&quot;&gt;&lt;/div&gt;
      &lt;script defer=&quot;defer&quot; type=&quot;text/javascript&quot;&gt;
       var  Geographic  = new OpenLayers.Projection(&quot;EPSG:4326&quot;); 
       var  Mercator = new OpenLayers.Projection(&quot;EPSG:900913&quot;);
&#10;       var map = new OpenLayers.Map({
           div: &quot;map&quot;,
           projection: Mercator,
           displayProjection: Geographic,
           center: new OpenLayers.LonLat(0, 0),
           minResolution: &quot;auto&quot;,
           minExtent: new OpenLayers.Bounds(-1, -1, 1, 1),
           maxResolution: &quot;auto&quot;,
           maxExtent: new OpenLayers.Bounds(-180, -90, 180, 90),
           units : &#39;km&#39;
&#10;       });
&#10;       var layerOSM = new OpenLayers.Layer.OSM();
       map.addLayer(layerOSM);
       map.addControl(new OpenLayers.Control.LayerSwitcher());
       map.setCenter(new OpenLayers.LonLat(0, 0), 1);
       map.addControl(new OpenLayers.Control.PanZoomBar());
&#10;      &lt;/script&gt;
&#10;&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>this is the code, panzoombar is showing all the levels, but it stopped at last above two levels and not coming down.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '12, 23:26</strong></p>
<img src="https://secure.gravatar.com/avatar/04a20b9fcb9bacbfff09bcd0a4266b9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramesh%20Kotha&#39;s gravatar image" />
<p><span>Ramesh Kotha</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramesh Kotha has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>23 Jul '12, 07:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span></p>
</div>
</div>
<div id="comments-container-14488" class="comments-container">
&#10;</div>
<div id="comment-tools-14488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14488-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Asked and answered at http://gis.stackexchange.com/questions/29407/unable-to-see-whole-world-map-by-decreasing-panzoom-bar (Openlayers v2.12 feature - try older openlayers)" by EdLoach 23 Jul '12, 07:07

</div>

</div>

</div>

