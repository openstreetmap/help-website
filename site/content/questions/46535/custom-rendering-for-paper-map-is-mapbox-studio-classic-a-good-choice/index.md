+++
type = "question"
title = "Custom rendering for paper map, is Mapbox Studio Classic a good choice?"
description = '''I don&#x27;t believe this is a duplicate question, as other how to print to questions I could find were much more general. I want make a paper map, for outdoor use (Hiking and Camping). I&#x27;ve looked at the web based options on the wiki page, and none of them seem to be flexible enough. I want:   about 100...'''
date = "2015-11-11T21:10:00Z"
lastmod = "2019-12-10T15:34:00Z"
weight = 46535
keywords = [ "printing", "paper", "hiking", "mapbox" ]
aliases = [ "/questions/46535" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Custom rendering for paper map, is Mapbox Studio Classic a good choice?](/questions/46535/custom-rendering-for-paper-map-is-mapbox-studio-classic-a-good-choice)

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
<span id="post-46535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46535-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I don't believe this is a duplicate question, as other how to print to questions I could find were much more general.</p>
<p>I want make a paper map, for outdoor use (Hiking and Camping). I've looked at the web based options on the wiki page, and none of them seem to be flexible enough.</p>
<p>I want:</p>
<ul>
<li>about 100cm x 60cm overall dimension, including key, title, etc.</li>
<li>1:50,000 scale.</li>
<li>to be able to selectively emphasize certain features (trails, passes, campsites, etc), and de-emphasize others (vehicular roads). With most options I've looked at, the trails disappear when I have a large area in view.</li>
<li>must output topographic info.</li>
</ul>
<p>Mapbox's Studio Classic seems to be quite capable of what I want, but has a bit of a steep learning curve. I'm totally willing to put the energy into learning CartoCSS and Studio, but I don't want to invest a lot of time into learning to use Mapbox Studio and then find out it's not able to do what I want.</p>
<ul>
<li>Will it be able to output big enough images?</li>
<li>Will the features I want visible be rendered?</li>
<li>Is there something else that would be able to do the same, but output svg that would let me further tweak the map before printing?</li>
</ul>
<p>Thanks for any input.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-printing" rel="tag" title="see questions tagged &#39;printing&#39;">printing</span> <span class="post-tag tag-link-paper" rel="tag" title="see questions tagged &#39;paper&#39;">paper</span> <span class="post-tag tag-link-hiking" rel="tag" title="see questions tagged &#39;hiking&#39;">hiking</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Nov '15, 21:10</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Nov '15, 05:56</strong> </span></p>
</div>
</div>
<div id="comments-container-46535" class="comments-container">
&#10;</div>
<div id="comment-tools-46535" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46535-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="46536"></span>

<div id="answer-container-46536" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46536-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-46536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From what I read about Mapbox Studio Classic, it is primarily geared to making webmaps, and only secondarily for print.</p>
<p>All of your requirements (maximum flexibility in design, topographic quality map output, large dimension printing and layout, map legend), really points to a GIS (Geographical Information System) as a first and likely also final step to process and layout your data.</p>
<p><a href="http://www.qgis.org">QGIS</a> is of course an obvious choice, as it allows you to download custom sets of data (both geographically and by attribute) and insert this in a SpatialLite or other type of database, but the default option in its interface still doesn't handle multipolygons properly. Therefor, it may be better to use another tool capable of handling multipolygons to process and insert the data in a database, e.g. osm2pgsql and PostGIS, and then use this as the datasource.</p>
<p>Another option is ESRI's <a href="http://www.arcgis.com/home/item.html?id=75716d933f1c40a784243198e0dc11a1">ArcGIS Editor for OpenStreetMap</a>, which also does a pretty decent job (and handles multipolygons better than QGIS in the latest release).</p>
<p>Both QGIS and ArcGIS allow you to output your data as vector PDF, meaning you could postprocess it in another application capable of editing or using PDF vector data, and at the same time not being limited by raster output like in Mapbox Studio Classic, as I understood from their website it only outputs high resolution raster for print.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '15, 23:19</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '15, 10:35</strong> </span></p>
</div>
</div>
<div id="comments-container-46536" class="comments-container">
<span id="46552"></span>
<div id="comment-46552" class="comment">
<div id="post-46552-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your response, I'll look into QGIS. (I'm on Linux, and I'd like to support free/libre software).</p>
<p>Seems like there's a lot to learn to get functional with any GIS software, but it'd sure be cool to know how to use one.</p>
</div>
<div id="comment-46552-info" class="comment-info">
<span class="comment-age">(12 Nov '15, 19:56)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-46536" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46536-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46547"></span>

<div id="answer-container-46547" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46547-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two options I would traditionally consider. Both do, however, require a little bit of 'hacking' skill; if you're worried by Mapbox Studio's steep learning curve, you'll probably find these near-vertical!</p>
<p>The first option is to convert raw OpenStreetMap data (in .osm format) to Adobe Illustrator format, and then style the map in Illustrator. There is a Perl script called <strong>osm2ai.pl</strong> which will convert an .osm file to .ai, which I wrote many years ago. Rather than providing a direct download link, I'd actually suggest you Google it as a number of people have provided helpful tutorials.</p>
<p>The script doesn't do any styling whatsoever. However, it is capable of filtering OSM data into different Illustrator layers - say, a buildings layer, a primary roads layer, a waterway layer, and so on - to make the styling process easier.</p>
<p>I've used this approach many times to create print maps from OSM data and it works well.</p>
<p>The second option is to use Mapnik, which is the core of Mapbox Studio Classic. However, instead of asking for output in a raster format such as .png, you configure it to produce PDF maps. This is achieved by using the Cairo renderer rather than the default AGG.</p>
<p>This way, you do all your styling in CartoCSS, load your data into an OSM database, and then tell Mapnik to make the map. It requires quite a lot of hacking (most usually with Python, though I use Ruby) to get it to work: PDF is a fairly minority pursuit for Mapnik. However, the results can be surprisingly good. The PDF map export feature on <a href="http://cycle.travel">cycle.travel</a> is one place I use this approach.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '15, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '15, 16:00</strong> </span></p>
</div>
</div>
<div id="comments-container-46547" class="comments-container">
<span id="46553"></span>
<div id="comment-46553" class="comment">
<div id="post-46553-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What are the benefits of these approaches over Mapbox Studio? I'm also surprised to see you recommend output from mapnik to pdf, rather than svg. It seems that svg would be an easier format to work with, to add title, legend etc.</p>
</div>
<div id="comment-46553-info" class="comment-info">
<span class="comment-age">(12 Nov '15, 19:57)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="46556"></span>
<div id="comment-46556" class="comment">
<div id="post-46556-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I use Adobe Illustrator and its SVG import, put simply, doesn't work properly. If you generate a PDF from Mapnik, it will usually look the same in Illustrator as long as you have the same fonts. If you generate an SVG, it will look like a pile of multi-coloured spaghetti with some random letters scattered all over it.</p>
</div>
<div id="comment-46556-info" class="comment-info">
<span class="comment-age">(12 Nov '15, 22:33)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46547" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46547-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46576"></span>

<div id="answer-container-46576" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46576-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might also consider the non-open-software but free-of-charge "Maperitive", a windows program that runs fine on Linux under Mono. It has its own styling language, different from that of TileMill, and it can generate SVG output that can be post-processed with Inkscape. This is useful especially if you want to make some changes that go beyond "all features that have the attribute X should be painted like this" but where you want to style a couple of individual features differently - this is easy to do once you have the data in Inkscape.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '15, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46576" class="comments-container">
&#10;</div>
<div id="comment-tools-46576" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46576-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72064"></span>

<div id="answer-container-72064" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72064-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mapbox Studio is a good styling app for pre-visualisation. <a href="https://hebstreits.com/customizer">Hebstreits customizer</a> is a new service working with Mapbox styles and deliver clean maps as Open Vector PDFs for artistic and business use. If open SVG format is desired, this would have to be requested.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '19, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/8b7dbe317cf4f41d01d004de0b9a9cfd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="netsign&#39;s gravatar image" />
<p><span>netsign</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="netsign has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Dec '19, 15:35</strong> </span></p>
</div>
</div>
<div id="comments-container-72064" class="comments-container">
&#10;</div>
<div id="comment-tools-72064" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72064-form-container" class="comment-form-container">
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

