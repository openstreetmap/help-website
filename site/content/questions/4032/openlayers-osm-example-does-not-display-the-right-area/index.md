+++
type = "question"
title = "OpenLayers OSM example does not display the right area?"
description = '''http://wiki.openstreetmap.org/wiki/OpenLayers_osm_file_example i got a problem about the example in the web pag of that link.  var layer = new OpenLayers.Layer.Vector(&quot;Polygon&quot;, {  strategies: [new OpenLayers.Strategy.Fixed()],  protocol: new OpenLayers.Protocol.HTTP({  url: &quot;myosmfile.osm&quot;, //&amp;lt;-...'''
date = "2011-03-24T06:33:00Z"
lastmod = "2011-03-24T07:57:00Z"
weight = 4032
keywords = [ "openlayers" ]
aliases = [ "/questions/4032" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OpenLayers OSM example does not display the right area?](/questions/4032/openlayers-osm-example-does-not-display-the-right-area)

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
<span id="post-4032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4032-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-4032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="http://wiki.openstreetmap.org/wiki/OpenLayers_osm_file_example">http://wiki.openstreetmap.org/wiki/OpenLayers_osm_file_example</a></p>
<p>i got a problem about the example in the web pag of that link.</p>
<pre><code>  var layer = new OpenLayers.Layer.Vector(&quot;Polygon&quot;, {
                strategies: [new OpenLayers.Strategy.Fixed()],
                protocol: new OpenLayers.Protocol.HTTP({
                    url: &quot;myosmfile.osm&quot;,   //&lt;-- relative or absolute URL to your .osm file
                    format: new OpenLayers.Format.OSM()
                }),
                projection: new OpenLayers.Projection(&quot;EPSG:4326&quot;)
            });</code></pre>
<p>this part of code seems does not work, i have put the html file alongside the osm file in an apache server, but the result did not change, it did not show the area which is included in the osm file.</p>
<p>I did not how this happened，i need your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '11, 06:33</strong></p>
<img src="https://secure.gravatar.com/avatar/af1ec8bbb972abf519b0c265336d7911?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="monument&#39;s gravatar image" />
<p><span>monument</span><br />
<span class="score" title="69 reputation points">69</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="monument has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '11, 11:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-4032" class="comments-container">
&#10;</div>
<div id="comment-tools-4032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4032-form-container" class="comment-form-container">
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

<span id="4033"></span>

<div id="answer-container-4033" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4033-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Note: This is not strictly OpenStreetMap related but rather a Openlayers question and therefore offtopic here.</p>
<p>Looking at the example in the wiki the display is always centered at latitude 51.950, longitude 7.613 rather then the center of the osm file you provide. You can either hardcode the "correct" center or center "dynamically" using the <code>getDataExtent</code> property of the vector layer. For further documentation please read the documentaion on <a href="http://dev.openlayers.org/apidocs/files/OpenLayers/Layer/Vector-js.html">vector layers</a> and <a href="http://dev.openlayers.org/apidocs/files/OpenLayers/Map-js.html#OpenLayers.Map.setCenter">setCenter</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '11, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-4033" class="comments-container">
&#10;</div>
<div id="comment-tools-4033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4033-form-container" class="comment-form-container">
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

