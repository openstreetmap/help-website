+++
type = "question"
title = "What is a good practice to make icons visible on osms?"
description = '''I am adding features by using var feature = new OpenLayers.Feature.Vector( new OpenLayers.Geometry.Point( lng ,lat ).transform(epsg4326, projectTo), {description:&#x27;some description&#x27;} , {externalGraphic: &#x27;mypicture.png&#x27;, graphicHeight: 32, graphicWidth: 32, graphicXOffset:-16, graphicYOffset:-16} );  ...'''
date = "2013-11-25T13:41:00Z"
lastmod = "2013-11-25T16:21:00Z"
weight = 28450
keywords = [ "icon", "openlayers", "features", "slippymap", "icons" ]
aliases = [ "/questions/28450" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is a good practice to make icons visible on osms?](/questions/28450/what-is-a-good-practice-to-make-icons-visible-on-osms)

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
<span id="post-28450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28450-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am adding features by using</p>
<pre><code>var feature = new OpenLayers.Feature.Vector( new OpenLayers.Geometry.Point( lng ,lat  ).transform(epsg4326, projectTo),  {description:&#39;some description&#39;} , {externalGraphic: &#39;mypicture.png&#39;, graphicHeight: 32, graphicWidth: 32, graphicXOffset:-16, graphicYOffset:-16} );</code></pre>
<p>But they are barely visible given that almost all colors are being used in osms.</p>
<p>What is a good practice to make icons visible on osms?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-features" rel="tag" title="see questions tagged &#39;features&#39;">features</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span> <span class="post-tag tag-link-icons" rel="tag" title="see questions tagged &#39;icons&#39;">icons</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Nov '13, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c00bc3f79a2483942c6cbe24e89069f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zurechtweiser&#39;s gravatar image" />
<p><span>Zurechtweiser</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zurechtweiser has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '13, 14:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-28450" class="comments-container">
<span id="28452"></span>
<div id="comment-28452" class="comment">
<div id="post-28452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I assume you mean that you are using an OSM-based map (I guess our standard "mapnik" style) in a slippy map as background to display other objects/markers on top, right?</p>
</div>
<div id="comment-28452-info" class="comment-info">
<span class="comment-age">(25 Nov '13, 14:21)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="28461"></span>
<div id="comment-28461" class="comment">
<div id="post-28461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Zurechtweiser</span> What do you mean by "osms"? Could you explain a little?</p>
</div>
<div id="comment-28461-info" class="comment-info">
<span class="comment-age">(25 Nov '13, 16:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28450-form-container" class="comment-form-container">
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

<span id="28451"></span>

<div id="answer-container-28451" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28451-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ul>
<li>OSM-related:
<ul>
<li>Use another map rendering style as background (see <span>Tiles</span> and <span>Rendering</span>). <a href="http://mc.bbbike.org/mc/?lon=13.17694&amp;lat=52.09467&amp;zoom=13&amp;num=4&amp;mt0=cloudmade-paledawn&amp;mt1=mapnik-bw&amp;mt2=mapquest-eu&amp;mt3=mapbox">Examples</a>. Remember: OSM is just data - and many different maps (and services) are made of it.</li>
<li>… But please respect the individual tile usage policies. Example: <span>policy for osm.org's tiles</span></li>
</ul></li>
<li>(not-OSM-related:) Use an "<code>externalGraphic: 'mypicture.png'</code>" which has a big border/shadow around it - so it sticks out of the map. Or use the <a href="http://www.ithacaweb.org/media/mapfish/mfbase/openlayers/examples/marker-shadow.html">shadow feature of OpenLayers</a>. (I did not try this myself)</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '13, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '13, 14:33</strong> </span></p>
</div>
</div>
<div id="comments-container-28451" class="comments-container">
&#10;</div>
<div id="comment-tools-28451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28451-form-container" class="comment-form-container">
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

