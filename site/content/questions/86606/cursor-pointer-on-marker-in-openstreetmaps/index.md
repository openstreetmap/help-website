+++
type = "question"
title = "cursor pointer on marker in #openstreetmaps"
description = '''I have this code with openstreetmaps (is a cicle, then I have more marker named marker1, marker2 ,marker3 and so on), but property curosor: pointer dont workk (I tried with a lot of browser of course). // Create a marker feature 1  var marker1 = new ol.Feature({  geometry: new ol.geom.Point(ol.proj....'''
date = "2023-02-01T16:25:00Z"
lastmod = "2023-02-01T16:25:00Z"
weight = 86606
keywords = [ "#pointer", "#cursor", "#marke" ]
aliases = [ "/questions/86606" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [cursor pointer on marker in \#openstreetmaps](/questions/86606/cursor-pointer-on-marker-in-openstreetmaps)

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
<span id="post-86606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86606-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have this code with openstreetmaps (is a cicle, then I have more marker named marker1, marker2 ,marker3 and so on), but property curosor: pointer dont workk (I tried with a lot of browser of course).</p>
<pre><code>// Create a marker feature 1    
var marker1 = new ol.Feature({
    geometry: new ol.geom.Point(ol.proj.fromLonLat([14.3619382, 46.0649361])),
    name: &#39;some text&#39;,
    description: &#39;other some text&#39;
});
&#10;// Create a marker style 1  
var markerStyle1 = new ol.style.Style({
    image: new ol.style.Icon({
    src: &#39;/assets/images/ico.png&#39;,
    scale: 1            }),
    cursor: &#39;pointer&#39;
});
&#10;// Set style to marker feature 1    
marker1.setStyle(markerStyle1);
&#10;// Add the marker feature 1 to the vector source
vectorSource.addFeature(marker1);</code></pre>
<p>Also tried with css:</p>
<pre><code>.ol-marker .ol-icon {
  cursor: pointer;
}</code></pre>
<p>the same, dont work :( Someone can help me plese? Thanks in advanced</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-#pointer" rel="tag" title="see questions tagged &#39;#pointer&#39;">#pointer</span> <span class="post-tag tag-link-#cursor" rel="tag" title="see questions tagged &#39;#cursor&#39;">#cursor</span> <span class="post-tag tag-link-#marke" rel="tag" title="see questions tagged &#39;#marke&#39;">#marke</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '23, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/ab7c2b7c000b677ff3eac2da1c98d650?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LucaFrass&#39;s gravatar image" />
<p><span>LucaFrass</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LucaFrass has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Feb '23, 14:11</strong> </span></p>
</div>
</div>
<div id="comments-container-86606" class="comments-container">
&#10;</div>
<div id="comment-tools-86606" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86606-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

