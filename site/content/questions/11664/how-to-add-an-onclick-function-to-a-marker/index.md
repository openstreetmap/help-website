+++
type = "question"
title = "[closed] how to add an &quot;onclick&quot; function to a marker?"
description = '''I have a marker such as this var feature = new OpenLayers.Feature.Vector(  new OpenLayers.Geometry.Point( lng,lat ).transform(epsg4326, projectTo),  {description:&#x27;something&#x27;} ,  {externalGraphic: &#x27;somepic.png&#x27;, graphicHeight:34, graphicWidth: 21, graphicXOffset:0,   graphicYOffset:0 });  vectorLayer...'''
date = "2012-03-31T19:03:00Z"
lastmod = "2012-03-31T20:01:00Z"
weight = 11664
keywords = [ "clickable", "openlayers", "markers" ]
aliases = [ "/questions/11664" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] how to add an "onclick" function to a marker?](/questions/11664/how-to-add-an-onclick-function-to-a-marker)

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
<span id="post-11664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11664-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a marker such as this</p>
<pre><code>var feature = new OpenLayers.Feature.Vector(
                      new OpenLayers.Geometry.Point( lng,lat ).transform(epsg4326, projectTo),
                      {description:&#39;something&#39;} ,
                      {externalGraphic: &#39;somepic.png&#39;, graphicHeight:34, graphicWidth: 21, graphicXOffset:0,   
                                      graphicYOffset:0 }); 
vectorLayer.addFeatures(feature);
map.addLayer(vectorLayer);</code></pre>
<p>i was wondering if there is a way to add onclick function to the markers, so an example use would be something like</p>
<pre><code>feature.onClick(function (){
   alert(&quot;clicked&quot;);
});</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-clickable" rel="tag" title="see questions tagged &#39;clickable&#39;">clickable</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-markers" rel="tag" title="see questions tagged &#39;markers&#39;">markers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Mar '12, 19:03</strong></p>
<img src="https://secure.gravatar.com/avatar/3227c0aa7dd4c83f2fc7958a4f63fc99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bernabasd&#39;s gravatar image" />
<p><span>bernabasd</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bernabasd has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>31 Mar '12, 20:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-11664" class="comments-container">
&#10;</div>
<div id="comment-tools-11664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11664-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Frederik Ramm 31 Mar '12, 20:01

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11668"></span>

<div id="answer-container-11668" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11668-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is an OpenStreetMap help forum but your question is a general OpenLayers question. The OpenLayers "users" mailing list at <a href="http://lists.osgeo.org/mailman/listinfo/openlayers-users/">http://lists.osgeo.org/mailman/listinfo/openlayers-users/</a> would be a good place to ask such a question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Mar '12, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-11668" class="comments-container">
&#10;</div>
<div id="comment-tools-11668" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11668-form-container" class="comment-form-container">
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

