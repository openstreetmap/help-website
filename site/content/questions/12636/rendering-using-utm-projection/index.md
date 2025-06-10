+++
type = "question"
title = "Rendering using UTM-Projection"
description = '''Heyho! I want to render a map.png in UTM-Projection. But I didn&#x27;t find anything useful on the internet.. :( Can anyone tell me, what I have to do to simply render in UTM-Projection?? I only want to render small maps so the different zones should not be a problem, I think. I imported my schleswig-hol...'''
date = "2012-05-09T09:14:00Z"
lastmod = "2012-08-17T10:11:00Z"
weight = 12636
keywords = [ "rendering", "projection", "mapnik", "utm" ]
aliases = [ "/questions/12636" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering using UTM-Projection](/questions/12636/rendering-using-utm-projection)

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
<span id="post-12636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12636-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Heyho!</p>
<p>I want to render a map.png in UTM-Projection. But I didn't find anything useful on the internet.. :(</p>
<p>Can anyone tell me, what I have to do to simply render in UTM-Projection??</p>
<p>I only want to render small maps so the different zones should not be a problem, I think.</p>
<p>I imported my schleswig-holstein.osm via osm2pgsql to my PostgreSQL/PostGIS database and now I want to render using Python/Mapnik.</p>
<p>I'm very thankful for any little hint or idea! Please help me!</p>
<p>Greetz Matze</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-projection" rel="tag" title="see questions tagged &#39;projection&#39;">projection</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-utm" rel="tag" title="see questions tagged &#39;utm&#39;">utm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '12, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0198a02af3c41ad04b61e028c3b126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHein&#39;s gravatar image" />
<p><span>MHein</span><br />
<span class="score" title="141 reputation points">141</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHein has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12636" class="comments-container">
&#10;</div>
<div id="comment-tools-12636" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12636-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="12834"></span>

<div id="answer-container-12834" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12834-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just to make this a little bit clearer and to give you an "answer":<br />
If you define an UTM projection in your XML, you simply need to (for mapnik2)</p>
<pre><code>bounds = (000000, -8100000, 3700000 , 8100000)
mapfile = &#39;/your/path/to/osm.xml&#39;
map_ = mapnik.Map(500, 500)
mapnik.load_map(map_, mapfile)
bbox = mapnik.Envelope(*bounds)
map_.zoom_to_box(bbox)
image = mapnik.Image(width, height)
mapnik.render(map_, image)
image.save(image_name, &#39;png&#39;)</code></pre>
<p>and that should give you an image in UTM. You may verify this by printing some metadata</p>
<pre><code>print map_.srs
print map_.scale_denominator()</code></pre>
<p>HTH Frank</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '12, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/30b87850d86c99d1c4f1f72c9abaeb52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frabron&#39;s gravatar image" />
<p><span>frabron</span><br />
<span class="score" title="361 reputation points">361</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frabron has 2 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-12834" class="comments-container">
<span id="12710"></span>
<div id="comment-12710" class="comment">
<div id="post-12710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Heyho!</p>
<p>I tried rendering in UTM but when I had eliminated all errors and saw the map, I recognized that the map was still rendered in standard (google?)-projection (where Greenland is as big as Africa).</p>
<p>I changed the -- Map background-color="#fff" srs="+init=epsg:3857" -- into -- Map background-color="#b5d0d0" srs="&amp;srs_UTM;" --</p>
<p>and defined srs_UTM in entities.xml.inc this way:</p>
<p><code>&lt;!ENTITY srs_UTM "+proj=utm +zone=32 +ellps=WGS84 +datum=WGS84 +units=m +no_defs"&gt;</code></p>
<p>In my generate_imgage.py I used:</p>
<pre><code>bounds = (000000, -8100000, 3700000 , 8100000)
# utm in meters 
    utm = mapnik.Projection(&#39;+proj=utm +zone=32 +ellps=WGS84 +datum=WGS84 +units=m +no_defs&#39;)
transform = mapnik.ProjTransform(utm,merc)</code></pre>
<p>I don't know what I did wrong or maybe what I forgot to change.. e.g. I found</p>
<pre><code># ensure the target map projection is mercator
m.srs = merc.params()</code></pre>
<p>and I don't know If I should change it or anything else..</p>
<p>this is my entities.xcl.inc: <a href="http://dpaste.org/cuJW3/">http://dpaste.org/cuJW3/</a></p>
<p>this is my osm.xml: <a href="http://dpaste.org/xLqJA/">http://dpaste.org/xLqJA/</a></p>
<p>this is my generate_image.py: <a href="http://dpaste.org/0WEQw/">http://dpaste.org/0WEQw/</a></p>
<p>I hope that anyone can help me.. please!!!</p>
<p>Greetings Matze</p>
</div>
<div id="comment-12710-info" class="comment-info">
<span class="comment-age">(14 May '12, 07:48)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
<span id="12833"></span>
<div id="comment-12833" class="comment">
<div id="post-12833-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well, apparently you are transforming your desired UTM to Mercator in your Python script. Just skip the transformation steps and you should be fine</p>
</div>
<div id="comment-12833-info" class="comment-info">
<span class="comment-age">(21 May '12, 08:43)</span> <span class="comment-user userinfo">frabron</span>
</div>
</div>
<span id="12894"></span>
<div id="comment-12894" class="comment">
<div id="post-12894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately it doesn't work.. I will describe the problems in another answer.</p>
</div>
<div id="comment-12894-info" class="comment-info">
<span class="comment-age">(23 May '12, 11:39)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
<span id="12897"></span>
<div id="comment-12897" class="comment">
<div id="post-12897-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>First of all, thank you, Frank!</p>
<p>I deleted all the transformation-things etc. und put the things as you wrote it.</p>
<p>The rendering doesn't produce any errors but the maps I get are not like I want them.</p>
<p>This happens, when I try to render my hometown Kiel in Schleswig-Holstein, Germany: <a href="http://imgur.com/CIPJ5">http://imgur.com/CIPJ5</a><br />
( <code>bounds = (565124, 6014024, 579888 , 6026499) #Kiel UTM</code> )</p>
<p>This looks as if just the coastlines are used to create this image. Why is the osm-content of my schleswig-holstein.osm.pbf not displayed? I imported it like this: <code>osm2pgsql --slim -d gis -C 1024 -E 32632 ~/schleswig-holstein.osm.pbf</code></p>
<p>When I try to render the whole world, the image looks like this: <a href="http://imgur.com/f2gNa">http://imgur.com/f2gNa</a></p>
<p>( <code>bounds = (000000, -8100000, 3700000 , 8100000)</code> )</p>
<p>This looks as if the coastlines have not been used.. Is it because of the fact that the coastlines are not in the right projection?</p>
<p>I'll post my <code>new_generate_image.py</code>: <a href="http://dpaste.org/RScJO/">http://dpaste.org/RScJO/</a></p>
<p>Maybe you, Frank or anybody else can can give me some useful advice, info or hint! That would make me really glad!</p>
<p>Thank you in advance! Greetings, Matze</p>
</div>
<div id="comment-12897-info" class="comment-info">
<span class="comment-age">(23 May '12, 12:08)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
<span id="12908"></span>
<div id="comment-12908" class="comment">
<div id="post-12908-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I know Kiel, there's definetely more to see there ;-)<br />
I guess that there's a problem with your data from the database. Did you configure your datasource and settings files correctly, e.g. paths to shapefiles and EPSG codes? Look in the "inc" Folder for those ...</p>
</div>
<div id="comment-12908-info" class="comment-info">
<span class="comment-age">(23 May '12, 15:11)</span> <span class="comment-user userinfo">frabron</span>
</div>
</div>
<span id="12923"></span>
<div id="comment-12923" class="comment not_top_scorer">
<div id="post-12923-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, much more!</p>
<p>As a test, I imported (by osm2pgsql) my schleswig-holstein.osm.pbf with standard projection and rendered with the standard generate_image.py and it all worked out fine.. and I was using the same "inc"-files.</p>
<p>Anyway, it's surprising that Kiel has the coastline and for the whole world they seem to be missing..</p>
<p>any other idea?</p>
</div>
<div id="comment-12923-info" class="comment-info">
<span class="comment-age">(24 May '12, 08:45)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
</div>
<div id="comment-tools-12834" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-12834-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12637"></span>

<div id="answer-container-12637" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12637-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well you should have an XML style file that gives the desired map projection at the top, like this:</p>
<pre><code>&lt;Map background-color=&quot;#fff&quot; srs=&quot;+init=epsg:3857&quot;&gt;</code></pre>
<p>If you change that to the EPSG code for the UTM projection you want to use (or even, instead of using one of the existing definitions, just write your own projection definition there in proj4 style) then the map is generated in that projection. Be careful when specifying the render extent; you'll have to give that in UTM coordinates then as well.</p>
<p>If you use nik2img.py (recommended), you can even specify the projection on the command line.</p>
<p>In the <code>&lt;Layer&gt;</code> defintions that reference your database, make sure to stick to the projection you imported your data in; so if you ran osm2pgsql without <code>-E</code> or <code>-l</code> (ell), the <code>&lt;Layer&gt;</code> bits will continue to have to use EPSG:3857 no matter what your output projection.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '12, 09:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 May '12, 09:26</strong> </span></p>
</div>
</div>
<div id="comments-container-12637" class="comments-container">
&#10;</div>
<div id="comment-tools-12637" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12637-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12928"></span>

<div id="answer-container-12928" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12928-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-12928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>the map's srs is the dest srs, while your datasource's srs are the source srs. since you use osm data, so the datasource's is under wgs84(i.e.lat/long). To project to utm, you should set your map's srs to the desired utm zone.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '12, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/25ac0534e5b4a6769cd9f07f95cc7463?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feverzsj&#39;s gravatar image" />
<p><span>feverzsj</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feverzsj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12928" class="comments-container">
<span id="12929"></span>
<div id="comment-12929" class="comment">
<div id="post-12929-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, this is not correct, since he used<br />
: osm2pgsql --slim -d gis -C 1024 -E 32632<br />
to import the data. Pay attention to the -E switch. So his data in PostGIS is actually UTM 32N</p>
</div>
<div id="comment-12929-info" class="comment-info">
<span class="comment-age">(24 May '12, 13:42)</span> <span class="comment-user userinfo">frabron</span>
</div>
</div>
<span id="12931"></span>
<div id="comment-12931" class="comment">
<div id="post-12931-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>then no projection is needed for mapnik, just set all to same srs</p>
</div>
<div id="comment-12931-info" class="comment-info">
<span class="comment-age">(24 May '12, 13:50)</span> <span class="comment-user userinfo">feverzsj</span>
</div>
</div>
<span id="13117"></span>
<div id="comment-13117" class="comment">
<div id="post-13117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>as far as I know, I set all the srs..</p>
<p>In which files do I have to set the srs?</p>
</div>
<div id="comment-13117-info" class="comment-info">
<span class="comment-age">(30 May '12, 10:02)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
<span id="13149"></span>
<div id="comment-13149" class="comment">
<div id="post-13149-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The possibly quickest way would be to add a new projection definition to inc/entities.xml.inc<br />
</p>
<pre><code>&lt;!ENTITY utm32 &quot;+proj=utm +zone=32 +ellps=WGS84 +datum=WGS84 +units=m +no_defs&quot;&gt;</code></pre>
<p>just below the other two (srs900913 and srs4326) and in inc/settings.xml.inc set</p>
<pre><code>&lt;!ENTITY osm2pgsql_projection &quot;&amp;srs900913;&quot;&gt;</code></pre>
<p>to</p>
<pre><code>&lt;!ENTITY osm2pgsql_projection &quot;&amp;utm32;&quot;&gt;</code></pre>
<p>There's probably no need to adjust the dwithin parameters, I'd give it a try like I described it.</p>
<p>HTH Frank</p>
</div>
<div id="comment-13149-info" class="comment-info">
<span class="comment-age">(31 May '12, 13:27)</span> <span class="comment-user userinfo">frabron</span>
</div>
</div>
<span id="13156"></span>
<div id="comment-13156" class="comment not_top_scorer">
<div id="post-13156-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! I had added the projection in entities yet. But the change in settings was not made yet. now it looks this way:</p>
<pre><code>&lt;!-- use the &#39;&amp;srs900913;&#39; entity if you have called osm2pgsql without special flags (or with -m); use &#39;&amp;srs4326;&#39; if you have used -l --&gt;
&lt;!-- &lt;!ENTITY osm2pgsql_projection &quot;&amp;srs900913;&quot;&gt; --&gt;
&lt;!ENTITY osm2pgsql_projection &quot;&amp;srs_UTM;&quot;&gt;</code></pre>
<p>I will try the next few days if it works ;)</p>
</div>
<div id="comment-13156-info" class="comment-info">
<span class="comment-age">(31 May '12, 15:40)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
<span id="15203"></span>
<div id="comment-15203" class="comment">
<div id="post-15203-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>it doesn't work :(</p>
</div>
<div id="comment-15203-info" class="comment-info">
<span class="comment-age">(17 Aug '12, 10:11)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
</div>
<div id="comment-tools-12928" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-12928-form-container" class="comment-form-container">
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

