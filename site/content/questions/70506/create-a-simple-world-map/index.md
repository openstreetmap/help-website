+++
type = "question"
title = "Create a simple world map"
description = '''Hi everyone... since more than 3 weeks I am trying to create a simple world map (in osm.pbf or o5m format) which contains borders, major cities and rivers (including their names) and countries (including their names). I don´t need buildings, streets etc. I have downloaded planet-latest.osm.pbf from ...'''
date = "2019-08-24T16:13:00Z"
lastmod = "2019-09-01T12:20:00Z"
weight = 70506
keywords = [ "simple", "world", "create", "o5m", "map" ]
aliases = [ "/questions/70506" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Create a simple world map](/questions/70506/create-a-simple-world-map)

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
<span id="post-70506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70506-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone... since more than 3 weeks I am trying to create a simple world map (in osm.pbf or o5m format) which contains borders, major cities and rivers (including their names) and countries (including their names). I don´t need buildings, streets etc.</p>
<p>I have downloaded planet-latest.osm.pbf from <a href="https://planet.osm.org">https://planet.osm.org</a> and used osmfilter to filter out the things I need. But this is where I am failing. There are hundreds of tags with "name" "city" "waterway" etc. Some in capital letters, some not.</p>
<p>I am using Linux. Doing "osmfilter planet-latest.o5m --keep="cities names waterway" -o=planet-filtered.o5m" creates a huge file with I think unnecessary data and in now way looking like it should be.</p>
<p>Anybody able providing the steps necessary to create a simple world map in o5m format? The map should pretty much look like this: <a href="https://www.openstreetmap.org/#map=5/49.167/8.745">https://www.openstreetmap.org/#map=5/49.167/8.745</a> except for that all names should either be in English or German.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-simple" rel="tag" title="see questions tagged &#39;simple&#39;">simple</span> <span class="post-tag tag-link-world" rel="tag" title="see questions tagged &#39;world&#39;">world</span> <span class="post-tag tag-link-create" rel="tag" title="see questions tagged &#39;create&#39;">create</span> <span class="post-tag tag-link-o5m" rel="tag" title="see questions tagged &#39;o5m&#39;">o5m</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '19, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/acd93c84995906b20a3b26c47378a669?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Likonaus&#39;s gravatar image" />
<p><span>Likonaus</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Likonaus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '19, 18:44</strong> </span></p>
</div>
</div>
<div id="comments-container-70506" class="comments-container">
&#10;</div>
<div id="comment-tools-70506" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70506-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="70507"></span>

<div id="answer-container-70507" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70507-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap is the wrong data set for that because our data is so detailed. For a map like the one you want, you do not need the coastline of Norway in all its beautiful detail, nor the detailed boundary between any two countries.</p>
<p>It would be much easier for you if you could find a way to use, say, the naturalearthdata.com data set (which comes in the form of shape files, not osm or o5m. What is your use case?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '19, 17:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70507" class="comments-container">
<span id="70508"></span>
<div id="comment-70508" class="comment">
<div id="post-70508-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to run an offline map server and want to be able to feed my GPS position into it. Then I want to add a hundreds of custom markers which will be placed at major airports. These markers contain custom information about this airport which need to be quickly accessible in case of an inflight emergency. There are market solutions for that, unfortunately I am not able to modify the displayed data. I found a script on Github which sets up a tileserver (using o5m or osm.pbf files). Adding the markers is no problem.I am not an expert my knowledge is pretty restricted and that seems momentarily the only way for me to make that happen. I don´t know if I will be able to use GPS data using only files from naturalearthdata.com, which by the way I haven´t been able to load into tile server as the server accepts only the previous mentioned formats. The server script I am using can be found here: <a href="https://github.com/AcuGIS/OpenTileServer">https://github.com/AcuGIS/OpenTileServer</a> There is another server which I am experimenting with (<a href="https://openmaptiles.com/server/#install)">https://openmaptiles.com/server/#install)</a> but it runs in a docker and I am not able to feed my GPS position into it and to add markers. So I am pretty much stuck to the OSM approach...</p>
</div>
<div id="comment-70508-info" class="comment-info">
<span class="comment-age">(24 Aug '19, 18:43)</span> <span class="comment-user userinfo">Likonaus</span>
</div>
</div>
<span id="70510"></span>
<div id="comment-70510" class="comment">
<div id="post-70510-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>All the solutions you are looking at are geared towards working with OSM data, but your application is not something that calls for OSM data in the first place. You could use a simple map server powered by MapServer or Geoserver; it is quite possible that the whole concept of using a tile server isn't even right for your use case and a simple WMS would be good enough. Adding markers can be done server-side or client-side. If client-side, then you'd deal with it through the Leaflet or OpenLayers libraries which use your tile or WMS server, and the adding-markers-and-using-your-GPS-position question is totally independent of what map backend you use.</p>
<p>If you <em>do</em> want to continue down the OSM route, which I would not recommend, then you should use pre-processed coastline data from <a href="https://osmdata.openstreetmap.de/">https://osmdata.openstreetmap.de/</a> and use the osmium (recommended) or osmosis or osmfilter tools to extract boundary relations (<code>boundary=administrative</code>), rivers (<code>waterway=river</code>), and large place nodes (<code>place=city</code>) - but even these reduced data sets will be much larger than what you get from naturalearthdata.com where everything is already boiled down to what you need for a map of your scale.</p>
</div>
<div id="comment-70510-info" class="comment-info">
<span class="comment-age">(25 Aug '19, 09:16)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70507" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70507-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70584"></span>

<div id="answer-container-70584" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70584-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I wrote a diary entry around doing this sort of thing <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/47027">here</a>. The requirement there was very much to use modified boundaries created from OSM data. If that's not a requirement (and it sounds like it isn't in your case) then as Frederik says, something based on Natural Earth data might be the best way to go.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '19, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-70584" class="comments-container">
&#10;</div>
<div id="comment-tools-70584" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70584-form-container" class="comment-form-container">
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

