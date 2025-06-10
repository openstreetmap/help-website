+++
type = "question"
title = "Rendering maps with bounding box overlays"
description = '''Hello, I&#x27;d like to render my own maps with bounding box overlays. I do not wish to use tiles since the application will require multiple requests, therefore burdening the OSM servers, and I have enough knowledge to set Mapnik up myself. However, Mapnik seems to just be a map renderer. I&#x27;d like to re...'''
date = "2014-07-23T14:09:00Z"
lastmod = "2014-07-23T16:47:00Z"
weight = 35103
keywords = [ "rendering", "map", "overlay" ]
aliases = [ "/questions/35103" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering maps with bounding box overlays](/questions/35103/rendering-maps-with-bounding-box-overlays)

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
<span id="post-35103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35103-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'd like to render my own maps with bounding box overlays. I do not wish to use tiles since the application will require multiple requests, therefore burdening the OSM servers, and I have enough knowledge to set Mapnik up myself.</p>
<p>However, Mapnik seems to just be a map renderer. I'd like to render static map cutouts with bounding box overlays over the map region. This seems to only be possible via software like OpenLayers, which only work on webpages. (The desired output must be a static image!)</p>
<p>I guess my question is this:</p>
<p>For rendering static images of regions on a map,</p>
<ul>
<li>Is Mapnik overkill, or is it necessary?</li>
<li>Does Mapnik (or similar software) render city labels and state/county/city boundary lines? (Region is United States.)</li>
<li>What software would I use to stitch the map tiles together?</li>
<li>What software would I use to render overlays above my map?</li>
</ul>
<p>Thanks in advance!</p>
<p><strong>EDIT:</strong> Solutions in Python are preferred, but not required.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '14, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/28afe1f2109cf13de14dab893cd252c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alberth&#39;s gravatar image" />
<p><span>alberth</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alberth has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '14, 14:20</strong> </span></p>
</div>
</div>
<div id="comments-container-35103" class="comments-container">
<span id="35107"></span>
<div id="comment-35107" class="comment">
<div id="post-35107-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not a direct answer to the question but:</p>
<pre><code> I do not wish to use tiles since the application will require multiple requests, therefore burdening the OSM servers</code></pre>
<p>One option would be to <a href="http://switch2osm.org/serving-tiles/">set up your own tile server</a>.</p>
</div>
<div id="comment-35107-info" class="comment-info">
<span class="comment-age">(23 Jul '14, 16:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35103-form-container" class="comment-form-container">
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

<span id="35111"></span>

<div id="answer-container-35111" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35111-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I haven't worked with the new CartoCSS way of describing styles to Mapnik, but you certainly can do what you want with Mapnik. You can define as may layers as you want selecting which features show in what layers. Finally, you can use local or non-OSM data in layers too. I did all this to create some specialized printed paper maps for an area. If you are not worrying about printer pixels per inch and what it takes to get a 1:24000 scaled printed image at, say 600dpi, they you can even crib from the web scale factor logic.</p>
<p>I don't really know Python but all the Mapnik examples I found were in Python so that is what I used. So yes, you can do it in Python too.</p>
<p>Software I used were: Mapnik, Postgresql and the gdal library for the basic map. I also used PHP in command line mode to set a color profile on the resultant image and turn everything to a PDF. Don't know if you can do that part in Python or not but since I know PHP and had the library for it that did PDF creation I used it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '14, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-35111" class="comments-container">
&#10;</div>
<div id="comment-tools-35111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35111-form-container" class="comment-form-container">
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

