+++
type = "question"
title = "Add several xml (osm relations) to one layer at OpenLayers"
description = '''I&#x27;m using OpenLayers to display some OSM relations and then add some tags to them. I&#x27;m using this code to add xml files to my map. osm_layer = new OpenLayers.Layer.GML(&quot;Polygon&quot;, relation.xml, { format: OpenLayers.Format.OSM, style: {strokeColor: &quot;blue&quot;}, projection: new OpenLayers.Projection(&quot;EPSG:...'''
date = "2012-05-03T17:40:00Z"
lastmod = "2012-05-05T10:10:00Z"
weight = 12531
keywords = [ "osm", "openlayers", "relations" ]
aliases = [ "/questions/12531" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Add several xml (osm relations) to one layer at OpenLayers](/questions/12531/add-several-xml-osm-relations-to-one-layer-at-openlayers)

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
<span id="post-12531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12531-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using OpenLayers to display some OSM relations and then add some tags to them. I'm using this code to add xml files to my map.</p>
<pre><code>osm_layer = new OpenLayers.Layer.GML(&quot;Polygon&quot;, relation.xml, {
format: OpenLayers.Format.OSM,
style: {strokeColor: &quot;blue&quot;},
projection: new OpenLayers.Projection(&quot;EPSG:4326&quot;)
});</code></pre>
<p>But what I need is to add more than one relation.xml per layer, as relation1.xml, relation2.xml in the SAME layer. Until know I can only show multiple xml if they go in multiple layers.</p>
<p>When using vectors I just created the layer and then added the vectors by something like</p>
<pre><code>polygonFeature = new OpenLayers.Feature.Vector(
                 new OpenLayers.Geometry.Polygon(linearRing), style);</code></pre>
<p>And then</p>
<pre><code>Layer.addFeatures(polygonFeature);</code></pre>
<p>However, I can't make it work with xml / OSM relation format... It should be something like</p>
<pre><code>        i=1;
        while(i&lt;relations_list.length)
        { 
            osm_layer = new OpenLayers.Layer.GML(&quot;GML&quot;) 
            map.addLayer(osm_layer);
&#10;            xml_feature = new Openlayers.Feature.Vector(relation[i], {
                    format: OpenLayers.Format.OSM,
                    style: {strokeWidth: 3},
                    projection: new OpenLayers.Projection(&quot;EPSG:4326&quot;)
                });
&#10;            osm_layer.addFeatures(xml_feature);
&#10;            i=i+1;
&#10;            if(relations_list[i]==&quot;&quot;) {i=relations_list.length;}
        }</code></pre>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '12, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/40d0052a4cd080ec949c64c2ae62bd82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JorgePM&#39;s gravatar image" />
<p><span>JorgePM</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JorgePM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12531" class="comments-container">
&#10;</div>
<div id="comment-tools-12531" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12531-form-container" class="comment-form-container">
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

<span id="12555"></span>

<div id="answer-container-12555" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12555-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe a look at the source of <a href="http://wiki.openstreetmap.org/wiki/WIWOSM">WIWOSM</a> can help you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '12, 10:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-12555" class="comments-container">
&#10;</div>
<div id="comment-tools-12555" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12555-form-container" class="comment-form-container">
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

