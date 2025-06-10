+++
type = "question"
title = "Is a vector map layer planned for openstreetmap.org?"
description = '''Is there a vector map layer planned for openstreetmap.org? Since such layer would move map rendering from server to client I think there may be a lot of potential to lower both rendering and traffic load of OSM servers. Are there any plans for this? Maybe something like Mapbox GL JS could be used as...'''
date = "2016-05-14T22:00:00Z"
lastmod = "2017-11-06T13:41:00Z"
weight = 49697
keywords = [ "osm.org", "rendering", "vector" ]
aliases = [ "/questions/49697" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Is a vector map layer planned for openstreetmap.org?](/questions/49697/is-a-vector-map-layer-planned-for-openstreetmaporg)

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
<span id="post-49697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49697-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-49697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a vector map layer planned for openstreetmap.org? Since such layer would move map rendering from server to client I think there may be a lot of potential to lower both rendering and traffic load of OSM servers. Are there any plans for this? Maybe something like <a href="https://www.mapbox.com/mapbox-gl-js/api/">Mapbox GL JS</a> could be used as technical solution.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '16, 22:00</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 May '16, 22:04</strong> </span></p>
</div>
</div>
<div id="comments-container-49697" class="comments-container">
&#10;</div>
<div id="comment-tools-49697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49697-form-container" class="comment-form-container">
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

<span id="49785"></span>

<div id="answer-container-49785" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49785-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-49785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think there are a couple of reasons why a vector map of, what I assume you refer too, is the Standard or OpenStreetMap-Carto styled layer is not planned or realistic anywhere in the near future:</p>
<ul>
<li><p>As someone already pointed out, developer resources is one aspect. Knowing what I know from developing an OSM renderer from scratch for ArcGIS, it is an absolute huge undertaking to develop and maintain a style as complex as Carto / Standard, and the infrastructure to support it all. Converting the existing raster based style and infrastructure to a vector based one, would be a pretty massive task.</p></li>
<li><p>There is a second, much underappreciated aspect though. Despite all the flashy promotion of vector based maps as being "light-weight" and "fast" compared to raster tile services, this is only so for very basic simple maps with just a few vector layers (maybe 5-10 max). As soon as you start converting a style as complex as Carto, which would probably require a couple of hundreds of vector layers, things start to look <strong><em>entirely</em></strong> different...</p></li>
<li><p>Also, Carto currently displays buildings from a scale of about 1:50k. That would mean literally (tens of) thousands of vector building objects needing to be transferred and rendered on mobile devices with big screens if a 1:1 vector style conversion would need to be implemented with the same level of detail as Carto at each Z zoomlevel...</p></li>
</ul>
<p>Honestly, <em>have you ever seen a style even nearly as complex as Carto being served as pure vector tiles</em>?</p>
<p>I haven't, I think that says enough. I think current mobile hardware simply is not yet up to the task to deal with such complex vector services. Maybe in another 10 years...</p>
<p>Just testing of some vector services on my Samsung Tab S (first version), which is pretty high end as regards mobile with an octo-core processor, shows map rendering in the mobile browser to be very sluggish compared to opening the same vector service in a browser on my Core i5 desktop. And that is with a very basic style. Opening the Google Maps App, which does offer acceptable performance, and zooming all the way in, I only get to see any buildings when there are no more than maybe 50-500 buildings max in the viewport...</p>
<p>Also, in this respect, I recently read an article where the author concluded that with the apparent switch to vector based services, a style like Google's was considerably simplified compared to the styling before the switch. Less objects were shown at each zoom level. So you can have vector on your mobile device now, but at the huge cost of great simplification of the styling and the number of features shown at each zoom level.</p>
<p>Is that the price you want to pay for having vector?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 May '16, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 May '16, 11:10</strong> </span></p>
</div>
</div>
<div id="comments-container-49785" class="comments-container">
<span id="49786"></span>
<div id="comment-49786" class="comment">
<div id="post-49786-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Re "have you ever seen a style even nearly as complex as Carto being served as pure vector tiles", OsmAnd's style isn't a million miles away, either in the data used to display it and the complexity of the style itself. You can't compare "lines of code" since the styling language is so different, but it's not that dissimilar.</p>
<p>See for example:</p>
<p><a href="https://github.com/osmandapp/OsmAnd-resources/blob/master/obf_creation/rendering_types.xml">https://github.com/osmandapp/OsmAnd-resources/blob/master/obf_creation/rendering_types.xml</a></p>
</div>
<div id="comment-49786-info" class="comment-info">
<span class="comment-age">(22 May '16, 11:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="49791"></span>
<div id="comment-49791" class="comment">
<div id="post-49791-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>A 1:1 conversion is definitely unrealistic but maybe we don't need this. When zooming out OsmAnd stops pretty soon to display things like buildings due to the high complexity already mentioned by you. Yet instead of this black and white approach it is possible to do something in-between, like drawing only important buildings (hospitals, schools, churches, train stations, ...). An efficient, performant vector style will definitely need some additional brain power but it's not impossible as shown by various applications already using vector maps.</p>
</div>
<div id="comment-49791-info" class="comment-info">
<span class="comment-age">(22 May '16, 17:17)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="49794"></span>
<div id="comment-49794" class="comment">
<div id="post-49794-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not saying you can't have vector maps. Yes, MapOut looks impressive with its "3D" hillshading. But almost all vector maps I have seen do away with two things much valued by OSM users: 1) Layered rendering of highways and railways based on the OSM layer=x tag. Most only render connected lines, or show layering only at the very highest zoom levels (e.g. Google Maps App for Android). 2) High detail at lower zoom levels, e.g. buildings and (small) natural and landuse features. Despite what all of you are saying, many of the requests I have seen on the Carto Github in the past few years, actually are from people asking for more to be shown, even in zoom levels that seem hardly feasible. So I am pretty sure there are other opinions out there as well.</p>
</div>
<div id="comment-49794-info" class="comment-info">
<span class="comment-age">(22 May '16, 23:56)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="49795"></span>
<div id="comment-49795" class="comment">
<div id="post-49795-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>" If getting that quality of cartography onto osm.org is a "price" I can "pay", show me where to enter my credit card details."</p>
<p>You may find this interesting: <a href="http://forum.openstreetmap.org/viewtopic.php?pid=578345#p578345">http://forum.openstreetmap.org/viewtopic.php?pid=578345#p578345</a></p>
<p>And considerably outdated in terms of the cartography, but still some impression: <a href="http://forum.openstreetmap.org/viewtopic.php?id=26451">http://forum.openstreetmap.org/viewtopic.php?id=26451</a></p>
</div>
<div id="comment-49795-info" class="comment-info">
<span class="comment-age">(23 May '16, 00:04)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="55925"></span>
<div id="comment-55925" class="comment not_top_scorer">
<div id="post-55925-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>FIY these guys have a working solution for global vector tiles: <a href="https://openmaptiles.org/.">https://openmaptiles.org/.</a> So it is doable and is working quite nicely. Works well on mobile too.</p>
</div>
<div id="comment-55925-info" class="comment-info">
<span class="comment-age">(27 Apr '17, 22:05)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
<span id="55929"></span>
<div id="comment-55929" class="comment">
<div id="post-55929-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/237/kozuch">@Kozuch</a> none of the styles suggested by openmaptiles.org is a general purpose (with POIs etc) map style a la the OSM "standard" style. Actually if you look at all the major vector tile providers MB, MZ and WMF, you will notice that they all provide basic, typically very bland, map styles that at best are usable as a background for a small bit of custom data. The only exception would seem to be maps produced by Andy Allan, but even those tend to be "topical".</p>
</div>
<div id="comment-55929-info" class="comment-info">
<span class="comment-age">(28 Apr '17, 10:47)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="55931"></span>
<div id="comment-55931" class="comment not_top_scorer">
<div id="post-55931-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My ArcGIS Renderer in development, needs a staggering 350+(!) layers to create a rendering as rich, and in some areas clearly surpassing Carto, like the ability to show area:highway and man_made=bridge respecting OSM layer=x tag. I would love to see vector tile services able to handle a complexity like that, but at the current state of affairs, I think we are a long way off.</p>
</div>
<div id="comment-55931-info" class="comment-info">
<span class="comment-age">(28 Apr '17, 11:34)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="57225"></span>
<div id="comment-57225" class="comment not_top_scorer">
<div id="post-57225-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is a new website that features freely accessible OSM-based worldwide vector map - <a href="https://www.mapcat.com">https://www.mapcat.com</a>. You can search for POIs (example: "restaurant") in the top left corner and they show the result directly on the map which is very nice.</p>
</div>
<div id="comment-57225-info" class="comment-info">
<span class="comment-age">(21 Jul '17, 13:52)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
</div>
<div id="comment-tools-49785" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-49785-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49799"></span>

<div id="answer-container-49799" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49799-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just to chime in here. I've been working on porting the openstreetmap-carto style to vector tiles. But to render it server side with mapnik, producing images at the end, not to use client side rendering. It took a bit of work, but it can be done. I am not sure if it's sensible to have that rendered client side.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '16, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-49799" class="comments-container">
<span id="49802"></span>
<div id="comment-49802" class="comment">
<div id="post-49802-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>could you insert a link to some repo or documentation?</p>
</div>
<div id="comment-49802-info" class="comment-info">
<span class="comment-age">(23 May '16, 11:27)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49806"></span>
<div id="comment-49806" class="comment">
<div id="post-49806-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not yet, but hopefully soon.</p>
</div>
<div id="comment-49806-info" class="comment-info">
<span class="comment-age">(23 May '16, 12:37)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="60478"></span>
<div id="comment-60478" class="comment">
<div id="post-60478-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's probably this repo:</p>
<p><a href="https://github.com/geofabrik/openstreetmap-carto-vector-tiles">https://github.com/geofabrik/openstreetmap-carto-vector-tiles</a></p>
</div>
<div id="comment-60478-info" class="comment-info">
<span class="comment-age">(06 Nov '17, 13:41)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
</div>
<div id="comment-tools-49799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49799-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55932"></span>

<div id="answer-container-55932" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55932-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, oh my oh my, <em>what was I wrong</em>!!</p>
<p>I am taking back my words about not being able to publish a 350+ layer Vector Tiles service...</p>
<p>I knew ESRI was working on Vector Tiles, but hadn't yet found the time to explore the new addition in Pro 1.4. I am not used to ESRI getting it right the first time, it usually takes a second round.</p>
<p>But I just published an Amsterdam OpenStreetMap extract to a Vector Tile service created with ArcGIS Pro, with all freaking 350+ thematic layers!</p>
<p>There are some caveats though: - (Open cross) hatch polygon symbols are not yet supported in Vector Tiles, they end up being solid fills, which covers up stuff below it, which it really shouldn't. - Also hatched line symbols fail, and draw as a simple line feature - Random stipple pattern symbols seem replaced with equally spaced ones, meaning lesser cartography. - Symbols that use a reference scale for their size (e.g. 1:10k), and should be scaled in size / made bigger or smaller at other scales, don't. This doesn't work with Vector Tiles and the current client rendering. - Labelling is not as good as ESRI's Maplex label engine, there is quite a lot of labels missing.!But all in all, I am surprised to see this output so easily! I even published in a custom UTM zone 31N projection, instead of default Web Mercator.</p>
<p>The attached image shows both the Vector Tile (Right) and a PDF of the same data as comparison (Left). Notice the solid fill instead of cross hatch near Amsterdam Central Station, and a lot of missing labels.</p>
<p>Lastly, my first generation Tab S was able to handle opening this smaller extract as well. <img src="https://help.openstreetmap.org/upfiles/ArcGIS_Renderer_Vector_Tiles.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '17, 13:40</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Apr '17, 13:48</strong> </span></p>
</div>
</div>
<div id="comments-container-55932" class="comments-container">
<span id="55933"></span>
<div id="comment-55933" class="comment">
<div id="post-55933-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm sure we good get this done with proprietary software and/or a horde of paid developers :-) (not to mention an essentially 100% stranglehold on the commercial GIS market).</p>
<p>The question is just what does it have to do with OpenStreetMap?</p>
</div>
<div id="comment-55933-info" class="comment-info">
<span class="comment-age">(28 Apr '17, 14:22)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="55934"></span>
<div id="comment-55934" class="comment">
<div id="post-55934-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"The question is just what does it have to do with OpenStreetMap?"</p>
<p>That client side rendering and server side publishing of a Vector Tile service as complex as Carto's is at least theoretically possible.</p>
<p>Whether this all holds up at the scale of current global OSM data, and whether the OpenStreetMap site should serve VT for styles like Carto, or has the developers sources to explore it, are other questions indeed.</p>
<p>By the way, the "horde" in this case just has a single member, I developed my own renderer and style...</p>
</div>
<div id="comment-55934-info" class="comment-info">
<span class="comment-age">(28 Apr '17, 14:41)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="55948"></span>
<div id="comment-55948" class="comment">
<div id="post-55948-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The "hordes" referred to ESRIs developer staff. There is a, at least short term, difference between OSM and companies that can spend a billion or two, three ... on something they consider strategic (ESRI, google, etc) and what we can do in a short time (given time lots of things are possible without funds).</p>
</div>
<div id="comment-55948-info" class="comment-info">
<span class="comment-age">(28 Apr '17, 19:02)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55932-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49779"></span>

<div id="answer-container-49779" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49779-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, there is no such planning.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '16, 22:04</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-49779" class="comments-container">
<span id="49780"></span>
<div id="comment-49780" class="comment">
<div id="post-49780-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is the reason for a "no" just a lack of (developer) resources or is there something else behind?</p>
</div>
<div id="comment-49780-info" class="comment-info">
<span class="comment-age">(21 May '16, 23:12)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
<span id="49781"></span>
<div id="comment-49781" class="comment">
<div id="post-49781-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/99/stephan75">@stephan75</a> no plans even for the long run? I doubt that.</p>
</div>
<div id="comment-49781-info" class="comment-info">
<span class="comment-age">(22 May '16, 07:54)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="49782"></span>
<div id="comment-49782" class="comment">
<div id="post-49782-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>FWIW: on the dev mailing list I only found this partly relevant entry (searching for vector) <a href="https://lists.openstreetmap.org/pipermail/dev/2015-December/028970.html">https://lists.openstreetmap.org/pipermail/dev/2015-December/028970.html</a> which has no follow ups.</p>
</div>
<div id="comment-49782-info" class="comment-info">
<span class="comment-age">(22 May '16, 09:39)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49783"></span>
<div id="comment-49783" class="comment">
<div id="post-49783-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>and of course there is <a href="https://wiki.openstreetmap.org/wiki/Vector_tiles">https://wiki.openstreetmap.org/wiki/Vector_tiles</a></p>
</div>
<div id="comment-49783-info" class="comment-info">
<span class="comment-age">(22 May '16, 09:40)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49779-form-container" class="comment-form-container">
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

