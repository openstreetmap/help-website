+++
type = "question"
title = "Algorithm for geo/print size conversion"
description = '''Hi, I’m preparing some maps using Maperitive for projects in print, e.g. my personal travel photobook and a travel guide to be published. I got the conversion OSM-SVG-PDF working, but I need my (PDF) maps in defined sizes, e.g.  show the surroundings of some sight in 1:5000 in a picture of 5x5cm sho...'''
date = "2015-08-16T04:31:00Z"
lastmod = "2015-09-16T09:39:00Z"
weight = 44779
keywords = [ "maperitive", "projection", "algorithm" ]
aliases = [ "/questions/44779" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Algorithm for geo/print size conversion](/questions/44779/algorithm-for-geoprint-size-conversion)

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
<span id="post-44779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44779-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I’m preparing some maps using Maperitive for projects in print, e.g. my personal travel photobook and a travel guide to be published.</p>
<p>I got the conversion OSM-SVG-PDF working, but I need my (PDF) maps in defined sizes, e.g.</p>
<ul>
<li>show the surroundings of some sight in 1:5000 in a picture of 5x5cm</li>
<li>show a whole country, state or city on a book/A4 page</li>
</ul>
<p>That means, my output size is fixed, I can also set the scale, and I have either a pair of coordinates that must be included, or I have one coordinate to be the center point.</p>
<p>I don’t really care about the used projection (I wouldn’t know which one to choose anyway) and would use the default one of Maperitive.</p>
<p>But I need an algorithm to calculate the coordinates to use in Maperitive’s "set-print-bounds-geo" from output size, scale and a center point OR from output size and an included pair of coordinates. I’ll implement that in a Python script (and possibly in a spreadsheet). If some guesswork is involved, I'll just try a loop for approximation.</p>
<p>Please don’t just send me to Geoinformatics 101 ;)</p>
<p>EDIT: Trying to reword my question: As far as I understand, OSM data is in WGS84. Now, if I need a map of e.g. 5x5km around a coordinate, how much are these 2.5km plus/minus in easting/northing? Does it depend on the actual place?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span> <span class="post-tag tag-link-projection" rel="tag" title="see questions tagged &#39;projection&#39;">projection</span> <span class="post-tag tag-link-algorithm" rel="tag" title="see questions tagged &#39;algorithm&#39;">algorithm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '15, 04:31</strong></p>
<img src="https://secure.gravatar.com/avatar/5a39f1335b6eff433673ed987859fb24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hraban&#39;s gravatar image" />
<p><span>Hraban</span><br />
<span class="score" title="186 reputation points">186</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hraban has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Aug '15, 14:45</strong> </span></p>
</div>
</div>
<div id="comments-container-44779" class="comments-container">
<span id="45270"></span>
<div id="comment-45270" class="comment">
<div id="post-45270-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Another try at rewording: How do I add some length on the map to a longitude or latitude? (The length on the surface is not the same as the length in a projection, is it?) I found the formulae of Mercator projection in Wikipedia, but I don’t understand how to employ them – if they’re a solution for my problem at all.</p>
</div>
<div id="comment-45270-info" class="comment-info">
<span class="comment-age">(16 Sep '15, 09:39)</span> <span class="comment-user userinfo">Hraban</span>
</div>
</div>
</div>
<div id="comment-tools-44779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44779-form-container" class="comment-form-container">
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

<span id="44784"></span>

<div id="answer-container-44784" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44784-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not sure about Maperitive's setup but I did something similar a while back using Mapnik. In that you specify the scale per pixel as it is generally setup for output to displays. But once you decide the number of dots per inch (or cm) you are going to be printing at and the map scale you want the printed page to be you can multiply the numbers out to get the scale per pixel you need. In my case I have some scripts where I specify the center point for the map, the printed scale I want (usually 1:24000) and the size of the paper I am printing too. Here is a bit of out of context python code where I do my calculations. (Associate array v contains a definition of the map I want to print (paper size, map center in UTM grid coordinates, etc.) while things like the print dots per inch are specified as arguments on the command line). I specify my text in terms of printer points (72dpi) so I calculate what the DPI on those should be too:</p>
<pre><code>image_width = int(round(v[&#39;width&#39;] * args.dpi))
image_height = int(round(v[&#39;height&#39;] * args.dpi))
&#10;pixels_per_point = args.dpi / 72.0;
meters_per_pixel = 0.0254 * v[&#39;scale&#39;] / args.dpi
meters_per_point = meters_per_pixel * pixels_per_point
&#10;top = int(round((meters_per_pixel * (image_height / 2)) + int(v[&#39;northing&#39;])))
bottom = int(round((meters_per_pixel * (-image_height / 2)) + int(v[&#39;northing&#39;])))
left = int(round((meters_per_pixel * (-image_width / 2)) + int(v[&#39;easting&#39;])))
right = int(round((meters_per_pixel * (image_width / 2)) + int(v[&#39;easting&#39;])))
&#10;bot_left= wgs84utm(left, bottom, inverse=True);
top_right = wgs84utm(right, top, inverse=True)</code></pre>
<p>I have another hacked up script that puts my output raster image file into a PDF so I can easily force printing at the desired DPI by just telling the print dialog box to print at 100% but that is probably outside of the scope of your question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '15, 12:33</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-44784" class="comments-container">
<span id="44787"></span>
<div id="comment-44787" class="comment">
<div id="post-44787-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for trying, but you misunderstood - I'm not interested in pixels at all, since I deal with vector data. What I need is your "wgs84utm" function. Seems like it comes from <a href="http://gis.stackexchange.com/questions/78915/off-by-about-85-meters-when-converting-nad27-utm-to-wgs84-lat-lon,">http://gis.stackexchange.com/questions/78915/off-by-about-85-meters-when-converting-nad27-utm-to-wgs84-lat-lon,</a> i.e. from <code>pyproj</code>. That’s a good hint, even if I’d like to avoid external libraries. The remaining geometric calculations maybe useful, too (but those I would have been able to cook up myself).</p>
<p>EDIT: The pyproj (i.e. proj.4) docs are too much for me. :(</p>
</div>
<div id="comment-44787-info" class="comment-info">
<span class="comment-age">(16 Aug '15, 14:11)</span> <span class="comment-user userinfo">Hraban</span>
</div>
</div>
</div>
<div id="comment-tools-44784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44784-form-container" class="comment-form-container">
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

