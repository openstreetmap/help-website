+++
type = "question"
title = "How do I render my own maps for my website?"
description = '''OpenStreetMap has some wonderful data, but I don&#x27;t think the map style is appropriate for my website / application. Can I render my own maps and change the style to adapt it more for my purpose?'''
date = "2010-07-12T17:46:00Z"
lastmod = "2019-06-16T21:30:00Z"
weight = 136
keywords = [ "rendering", "server", "map" ]
aliases = [ "/questions/136" ]
osqa_answers = 9
osqa_accepted = false
+++

<div class="headNormal">

# [How do I render my own maps for my website?](/questions/136/how-do-i-render-my-own-maps-for-my-website)

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
<span id="post-136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-136-score" class="post-score" title="current number of votes">
29
</div>
<span id="post-136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
9
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OpenStreetMap has some wonderful data, but I don't think the map style is appropriate for my website / application. Can I render my own maps and change the style to adapt it more for my purpose?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '10, 17:46</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-136" class="comments-container">
&#10;</div>
<div id="comment-tools-136" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-136-form-container" class="comment-form-container">
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

9 Answers:

</div>

</div>

<span id="207"></span>

<div id="answer-container-207" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-207-score" class="post-score" title="current number of votes">
29
</div>
<span id="post-207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, I would really consider using some pre-made map tiles as there are many offered for free and it saves you sigificant effort. There are for example the:</p>
<ul>
<li><a href="http://www.openstreetmap.org/?layers=B000FTFT">main tile maps</a> (tile usage policy <a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy">here</a>), the</li>
<li><a href="http://maps.cloudmade.com/">cloudmade tiles</a> (<a href="http://www.cloudmade.com/terms_conditions">Terms &amp; Conditions</a>), the</li>
<li><a href="http://www.opencyclemap.org/">cycle map tiles</a>,</li>
</ul>
<p>and probably many more (some of them commercial), offering you different styles that you can relatively easy integrate into your website.</p>
<p>You can do a lot of customization even with those pre-made maps (see below). Rendering your own maps is always quite some effort. You need to set up a renderer, retrieve the relevant data, render the tiles, put them on a webhost (the number of files quickly adds up to the thousands and millions) and repeat all that every few weeks to keep your maps updated.</p>
<p>Just, make sure you honor the respective terms of service for the tile service you use. <em>Cloudmade</em> offers a <a href="http://maps.cloudmade.com/editor">custom style editor</a> which you might want to try out if you want to customize things.</p>
<p>The next level of customization is running your own <a href="http://openlayers.org/">openlayers</a> (OL) slippymap installation which let's you offer cool things like POI overlays, colored paths and areas (<a href="http://openlayers.org/dev/examples/behavior-fixed-http-gml.html">OL example</a>), added markers (<a href="http://openlayers.org/dev/examples/dynamic-text-layer.html">OL example</a>) and/or images on a map based on an input files or an RSS feed and many more things. <a href="http://opengastromap.org">Here is a real world example</a>, showing all smoking and non-smoking restaurants in Germany, all without installing your own renderer and mucking with cartographic stylesheets... Have a look at the openlayers and slippymap pages in the osm wiki, and also make sure to explore the <a href="http://openlayers.org/dev/examples/">openlayers example page</a> to get a glimpse of what is possible and snatch the code you want from there (you'll find the code for the above examples there too). Openlayers is the most common and in my view the most convenient solution, but the wiki page "<a href="http://wiki.openstreetmap.org/wiki/Deploying_your_own_Slippy_Map">Deploying your own Slippymap</a>" lists a couple of alternative solutions.</p>
<p>That having said there are many renderers that you can use in order to create your own maps. Which one is the right one for you depends on many things. Do you need vector graphics (.svg) or .png files? Do you need one big map or 256x256 pixel tiles? Do you need to render them on-demand or do you want pre-made images? Do you need to render it once, or do you want to rerender with updated map-data frequently? Here are the commonly used ones:</p>
<ul>
<li><strong><a href="http://wiki.openstreetmap.org/wiki/Osmarender">Osmarender</a></strong>: Converts an .osm file into an .svg file using a stylesheet in custom .xml format.</li>
<li><strong><a href="http://wiki.openstreetmap.org/wiki/Orp">Or/p</a></strong>: is an osmarender drop-in replacement that is faster (written in perl).</li>
<li><strong><a href="http://wiki.openstreetmap.org/wiki/Mapnik">Mapnik</a></strong>: Full blown mapnik install is probably NOT what you want to do when all you need is some nice maps as its set up involves pulling the .osm data in a postgis database and rendering from there. However, it is the fastest and most advanced solution out there in case you need frequent re-renderings or if you want to really do advanced things.</li>
</ul>
<p>Less commonly used, but being designed for easy setup and usage are:</p>
<ul>
<li><a href="http://wiki.openstreetmap.org/wiki/Ceyx"><strong>Ceyx</strong></a> is an osm parser and MapCSS renderer. (UPDATE: it is unmaintained since 2010 and I don't think it can be used for much beyond small scale experimentation. Feel free to remove any mention of crux from this list.)(DISCLAIMER: I am the author of Ceyx, so forgive me this shameless advertisement :-)). <a href="http://wiki.openstreetmap.org/wiki/MapCSS/0.2">MapCSS</a> is the stylesheet language used by Potlatch2 to describe the look of a map and if you ever worked with HTML, you will quickly feel at home there. MapCSS is designed to be easy to customize. All it needs is python&gt;=2.5, python-cairo and pygtk (for pango/pangocairo) installed. Please refer to <a href="http://wiki.openstreetmap.org/wiki/Ceyx">its wiki page</a> for more information (note that it works just fine but is currently in maintenance mode, looking for contributors.). Another python-based mapcss renderer that I can recommend is is <a href="http://wiki.openstreetmap.org/wiki/Kothic">Kothic</a>.</li>
<li>Something that I find personally very cool, is <a href="http://wiki.openstreetmap.org/wiki/Kothic_JS">Kothic_JS</a> which does client-side rendering of map tiles and which seems to work reasonably well, if you are not on a mobile device.</li>
<li><a href="http://wiki.openstreetmap.org/wiki/Maperitive"><strong>Maperitive</strong></a>, an application written in mono to: render and print maps, as well as for setting up a local tile map server. It is the successor of <a href="http://wiki.openstreetmap.org/wiki/Kosmos">Kosmos</a>.</li>
</ul>
<p>If that selection is not enough for you, you can see even more rendering software at the <a href="http://wiki.openstreetmap.org/wiki/Renderer">OSM 'Renderer' wiki page</a>.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '10, 19:48</strong></p>
<img src="https://secure.gravatar.com/avatar/278e1af65e82993efd0ba7bbbacf6435?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spaetz&#39;s gravatar image" />
<p><span>spaetz</span><br />
<span class="score" title="853 reputation points">853</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spaetz has 2 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Oct '17, 16:59</strong> </span></p>
</div>
</div>
<div id="comments-container-207" class="comments-container">
<span id="5896"></span>
<div id="comment-5896" class="comment">
<div id="post-5896-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wish I had discovered Ceyx earlier! It's exactly what I needed, easy to use, no need for database, reliable, easy to customise (thanks to mapcss), open source... thank you for your work on it!</p>
</div>
<div id="comment-5896-info" class="comment-info">
<span class="comment-age">(20 Jun '11, 06:15)</span> <span class="comment-user userinfo">otto</span>
</div>
</div>
<span id="5898"></span>
<div id="comment-5898" class="comment">
<div id="post-5898-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Glad you like Ceyx, it is a small and nice piece, I think. Do note however, that I don't render maps for myself anymore, and basically stopped putting effort into Ceyx at the moment. I would be glad if someone else wants to pick up the torch.</p>
</div>
<div id="comment-5898-info" class="comment-info">
<span class="comment-age">(20 Jun '11, 08:03)</span> <span class="comment-user userinfo">spaetz</span>
</div>
</div>
<span id="5913"></span>
<div id="comment-5913" class="comment">
<div id="post-5913-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can't program stuff like this, I'm afraid. But I'll post more about what I did with Ceyx, it's related to <a href="http://help.openstreetmap.org/questions/4496/how-to-create-fantasyimaginary-maps-with-openstreetmap">http://help.openstreetmap.org/questions/4496/how-to-create-fantasyimaginary-maps-with-openstreetmap</a> Maybe it could interest some fantasy cartographers to work further on Ceyx...</p>
</div>
<div id="comment-5913-info" class="comment-info">
<span class="comment-age">(21 Jun '11, 00:14)</span> <span class="comment-user userinfo">otto</span>
</div>
</div>
<span id="5935"></span>
<div id="comment-5935" class="comment">
<div id="post-5935-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Motivated by someone liking it, I just implemented limited support for street names on curved paths. I think it is an improvement, let me know if you have CSS tweaks that you would like to see in mainline.</p>
</div>
<div id="comment-5935-info" class="comment-info">
<span class="comment-age">(21 Jun '11, 21:38)</span> <span class="comment-user userinfo">spaetz</span>
</div>
</div>
</div>
<div id="comment-tools-207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-207-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="141"></span>

<div id="answer-container-141" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-141-score" class="post-score" title="current number of votes">
14
</div>
<span id="post-141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Of course you can. Actually there are many different option to do it. You can either render a static map image with one of the renderers listed below, your you can use a map where you can zoom and pan around. This option is called a slippy map. The most option to realize a slippy is map is <a href="http://www.openlayers.com/">openlayers</a>. You can find documentation on the use of openlayers to display maps derived from OpenStreetMap data at <a href="http://wiki.openstreetmap.org/wiki/Openlayers"></a><a href="http://wiki.openstreetmap.org"></a><a href="http://wiki.openstreetmap.org">wiki.openstreetmap.org</a>/wiki/Openlayers.</p>
<p>However openlayers needs rendered map images (called tiles) so lets come back to the topic of renderers. There are many different renderers available for OSM data. A (probably incomplete) list can be found at <a href="http://wiki.openstreetmap.org/wiki/Rendering#Rendering_Software"></a><a href="http://wiki.openstreetmap.org"></a><a href="http://wiki.openstreetmap.org">wiki.openstreetmap.org</a>/wiki/Rendering.</p>
<p>The most common renderer if you want to generate tiles is mapnik. Documentation can be found at <a href="http://wiki.openstreetmap.org/wiki/Mapnik"></a><a href="http://wiki.openstreetmap.org"></a><a href="http://wiki.openstreetmap.org">wiki.openstreetmap.org</a>/wiki/Mapnik. It is quite fast and produces a nice looking map. This renderer is used to feed the main slippy map at <a href="http://www.openstreetmap.org"></a><a href="http://www.openstreetmap.org"></a><a href="http://www.openstreetmap.org">www.openstreetmap.org</a>. Setting up a server running mapnik and feeding the tiles to openlayers can be quite a bit or work though.</p>
<p>Another popular renderer is osmarender. Unlike mapnik it does not directly generate PNG images but generates SVG images which need to be rasterized using inkscape or batik. This is the renderer used by the tiles@home project. It is not as fast as mapnik (and some say not as good looking) but it is somewhat easier to set up and run, especially if you want to implement a custom style or only need a single image.</p>
<p>There are many other different renderers and I would probably be good if you ask this question again with a bit more details on what you exactly want in you map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '10, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-141" class="comments-container">
&#10;</div>
<div id="comment-tools-141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-141-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="205"></span>

<div id="answer-container-205" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-205-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://maperitive.net/">Maperitive</a> can render tiles. It works on OSM files though, so if you need a world-wide map, then you need a DB-based solution like Mapnik. On the other hand, setting up Maperitive is much easier. So it's more a question of what exactly your needs are.</p>
<p>I've made a sample <a href="http://beta1234.com.sunflower.arvixe.com/maps/">hiking Web map</a> made with Maperitive (warning: the server is slow).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '10, 19:25</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jun '11, 21:54</strong> </span></p>
</div>
</div>
<div id="comments-container-205" class="comments-container">
<span id="14580"></span>
<div id="comment-14580" class="comment">
<div id="post-14580-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I´ve used the Maperitive to convert my .OSM to .SVG file and it worked fine. I edited some colors on the map (colors of highways and lands) and I placed icons and imagens to attend my need. Now, what can I do with the edited .SVG file? I want to host my map like you did in your example. I´ve seen that exists MapBox but it ask for MBTiles and I just have the .SVG file that I already mencioned. What is my next step?</p>
</div>
<div id="comment-14580-info" class="comment-info">
<span class="comment-age">(25 Jul '12, 17:17)</span> <span class="comment-user userinfo">Gilliard Lopes</span>
</div>
</div>
</div>
<div id="comment-tools-205" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-205-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10975"></span>

<div id="answer-container-10975" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10975-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-10975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since this question was asked, <a href="http://switch2osm.org/serving-tiles/">this site</a> has been created which is intended to summarise the "setting up a tile server" options, if that's the road that you want to go down. It doesn't (yet) describe style editing in detail, though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '12, 11:13</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-10975" class="comments-container">
&#10;</div>
<div id="comment-tools-10975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10975-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="140"></span>

<div id="answer-container-140" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-140-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The simplest way to do this would be to use Cloudmade's <a href="http://cloudmade.com/products/style-editor">Style Editor</a>. This provides a fair amount of flexability with the styling -- certainly enough to theme it to your website.</p>
<p>Check out some examples at the <a href="http://cloudmade.com/products/style-editor/gallery">gallery</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '10, 17:59</strong></p>
<img src="https://secure.gravatar.com/avatar/d59cb9321a7a2a3ea5e5790345279ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matt%20Williams&#39;s gravatar image" />
<p><span>Matt Williams</span><br />
<span class="score" title="379 reputation points">379</span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matt Williams has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-140" class="comments-container">
<span id="208"></span>
<div id="comment-208" class="comment">
<div id="post-208-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>When using the services offered by Cloudmade on their website, you are subject to their <a href="http://www.cloudmade.com/terms_conditions">Terms of Use</a>, which are more restrictive than the legal requirements of other, usually open-source licensed, OSM rendering solutions.</p>
</div>
<div id="comment-208-info" class="comment-info">
<span class="comment-age">(14 Jul '10, 20:41)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="3722"></span>
<div id="comment-3722" class="comment">
<div id="post-3722-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Cloudmade's style editor allows only for some changes (colours of elements that are rendered according to the cloudmade stylesheet, zoom levels when they appear (but limited to high zooms), limited selection of evaluated tags), but doesn't allow for complete unlimited control (WHAT is displayed, WHEN is it displayed, HOW (icons, line style, layer order) it is displayed).</p>
</div>
<div id="comment-3722-info" class="comment-info">
<span class="comment-age">(11 Mar '11, 13:51)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-140" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-140-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3476"></span>

<div id="answer-container-3476" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3476-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Dependent on what you intend by "maps for my website" besides the already mentioned renderers like Mapnik and Maperitive you might also have a look at mapservers. There is the</p>
<ul>
<li>OSGeo <a href="http://mapserver.org/">http://mapserver.org/</a> licensed in an MIT-style license, which runs on all major platforms (Windows, Linux, Mac OS X).</li>
<li>GeoServer also from OSGeo and Opensource: <a href="http://geoserver.org/display/GEOS/Welcome">http://geoserver.org/display/GEOS/Welcome</a></li>
</ul>
<p>Both are free and open and there are tools available to convert community stylesheets from OSM into the SLD-format to begin.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '11, 12:34</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-3476" class="comments-container">
&#10;</div>
<div id="comment-tools-3476" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3476-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15059"></span>

<div id="answer-container-15059" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15059-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can also use <a href="http://mapbox.com/tilemill/">TileMill</a> to create custom maps using OpenStreetMap data. TileMill uses the Mapnik renderer (the same one the OpenStreetMap website uses), and you can export the XML stylesheets it generates.</p>
<p>There's also a <a href="http://mapbox.com/tilemill/docs/guides/osm-bright-mac-quickstart/">Quickstart Guide</a> for creating an OSM based map available as well as an <a href="http://mapbox.com/tilemill/docs/crashcourse/introduction/">Intro course</a>.</p>
<p><em>Disclosure: I work for MapBox</em></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '12, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/e7c43066000b48ff11a1ee7cef6e7a2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kkaefer&#39;s gravatar image" />
<p><span>kkaefer</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kkaefer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15059" class="comments-container">
<span id="32153"></span>
<div id="comment-32153" class="comment">
<div id="post-32153-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>wish they had a video tutorial</p>
</div>
<div id="comment-32153-info" class="comment-info">
<span class="comment-age">(06 Apr '14, 06:19)</span> <span class="comment-user userinfo">joshua robison</span>
</div>
</div>
<span id="32155"></span>
<div id="comment-32155" class="comment">
<div id="post-32155-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>suggest googling youtube &amp; tilemill</p>
</div>
<div id="comment-32155-info" class="comment-info">
<span class="comment-age">(06 Apr '14, 08:00)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15059-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69634"></span>

<div id="answer-container-69634" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69634-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After selecting the right map tiles (Raster tiles are served as images for example, so they require less processing power and memory to render) , I'd start by making sure I'd have the following Maps SDK components - glyphs - fonts used for rendering vector maps - images - images used by widgets, POI icons, etc. - sprites - images used for rendering vector maps TomTom offers Maps SDK for Web,Android and iOS that should help you with this: <a href="https://developer.tomtom.com/products/maps-sdk">https://developer.tomtom.com/products/maps-sdk</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '19, 21:30</strong></p>
<img src="https://secure.gravatar.com/avatar/119b3df587a8c143409c1c954e45d58a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tiago&#39;s gravatar image" />
<p><span>Tiago</span><br />
<span class="score" title="12 reputation points">12</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tiago has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69634" class="comments-container">
&#10;</div>
<div id="comment-tools-69634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69634-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38220"></span>

<div id="answer-container-38220" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38220-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-38220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use <a href="http://sourceforge.net/projects/topomapcreator/">TopoMapCreator</a>:</p>
<p>ExtendedMapCreator is a Desktop-Program, that creates "Topographic Maps" from OSM, NASA and ESA. You simply define a map extent by dragging over a browsable word map, click on start and wait till the GeoTIFF, ECW, GALILEO, ORUXMAPS or NAVIMAP files got created. ExtendedMapCreator is based on the Mapnik-Renderer, nevertheless all data downloading and processing is fully automatic. Click on ExtendedMapCreator to read more about the Program!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '14, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/6c696b469aba99282f03a4a1f33528b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kaki007&#39;s gravatar image" />
<p><span class="suspended-user">kaki007</span><br />
(suspended)<br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kaki007 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38220" class="comments-container">
&#10;</div>
<div id="comment-tools-38220" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38220-form-container" class="comment-form-container">
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

