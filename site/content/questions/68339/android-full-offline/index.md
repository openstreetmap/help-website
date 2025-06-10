+++
type = "question"
title = "android full-offline"
description = '''Hey guys... I want to develop a full offline app, where the map data is included in the apk, for android (java). First I started using the mapbox sdk but unfortunately I noticed that they have a tile limitation of 6k Tiles and I couldn&#x27;t figure out how to load OpenStreetMap data... Now I used the os...'''
date = "2019-03-09T15:42:00Z"
lastmod = "2022-04-16T09:18:00Z"
weight = 68339
keywords = [ "map", "android", "osmand", "offlinemaps" ]
aliases = [ "/questions/68339" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [android full-offline](/questions/68339/android-full-offline)

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
<span id="post-68339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68339-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys...</p>
<p>I want to develop a full offline app, where the map data is included in the apk, for android (java). First I started using the mapbox sdk but unfortunately I noticed that they have a tile limitation of 6k Tiles and I couldn't figure out how to load OpenStreetMap data...</p>
<p>Now I used the osmand sdk to make the map show up with the markers and stuff... I didn't find a clear solution for my <strong>problem</strong>:</p>
<p>Say I have downloaded the data from <a href="https://openmaptiles.com/downloads/planet/">https://openmaptiles.com/downloads/planet/</a> in .mbtiles how can I load the data from the asset folder to my device and show the map, so that someone can install the .apk and will have a full offline Map.</p>
<p>Or is there any "how to" tutorial for building a full offline map-app...</p>
<p>I also checked mapsforge but how I figured out, they focus more on rendering than on pre-loaded data or do I miss something there?</p>
<p>SO: 1. Tutorial to include .mbtiles or 2. Any Tutorial / tips to build full offline map...</p>
<p>Thanks a lot.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osmand" rel="tag" title="see questions tagged &#39;osmand&#39;">osmand</span> <span class="post-tag tag-link-offlinemaps" rel="tag" title="see questions tagged &#39;offlinemaps&#39;">offlinemaps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '19, 15:42</strong></p>
<img src="https://secure.gravatar.com/avatar/d8a8bd0f93cd544c77b9192ec5d759e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mathmike&#39;s gravatar image" />
<p><span>mathmike</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mathmike has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '19, 21:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-68339" class="comments-container">
&#10;</div>
<div id="comment-tools-68339" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68339-form-container" class="comment-form-container">
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

<span id="68344"></span>

<div id="answer-container-68344" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68344-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mathmike has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The correct answer really depends on what functionality you want to provide (which in turn tends to impact the offline data format).</p>
<p>For simply providing an offline map, <a href="https://github.com/mapsforge/mapsforge">mapsforge</a> is a tried solution.</p>
<p>For completeness sake, <a href="https://wiki.openstreetmap.org/wiki/Frameworks#Displaying_interactive_maps">https://wiki.openstreetmap.org/wiki/Frameworks#Displaying_interactive_maps</a> is a list of relevant frameworks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '19, 19:50</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '19, 21:08</strong> </span></p>
</div>
</div>
<div id="comments-container-68344" class="comments-container">
<span id="68348"></span>
<div id="comment-68348" class="comment">
<div id="post-68348-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, so I definitely will work on mapsforge in that case.</p>
<p>Right now the needed functions are: -providing offlinemap -adding markers and user location (and some marker.OnClickListener) -reverse geocoding -would be nice to provide a full street directory</p>
<p>Is this possible with mapsforge?</p>
</div>
<div id="comment-68348-info" class="comment-info">
<span class="comment-age">(09 Mar '19, 20:41)</span> <span class="comment-user userinfo">mathmike</span>
</div>
</div>
<span id="68349"></span>
<div id="comment-68349" class="comment">
<div id="post-68349-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know how well it works but here is an example <a href="https://github.com/mapsforge/mapsforge/blob/c8294c7ae27b2ce4a6af56516216af8c6d7cb0b3/mapsforge-samples-android/src/main/java/org/mapsforge/samples/android/ReverseGeocodeViewer.java">https://github.com/mapsforge/mapsforge/blob/c8294c7ae27b2ce4a6af56516216af8c6d7cb0b3/mapsforge-samples-android/src/main/java/org/mapsforge/samples/android/ReverseGeocodeViewer.java</a></p>
</div>
<div id="comment-68349-info" class="comment-info">
<span class="comment-age">(09 Mar '19, 21:06)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68344" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68344-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68342"></span>

<div id="answer-container-68342" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68342-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My knowledge here is as a user of OsmAnd not as a developer, but with that caveat in mind:</p>
<p>While OsmAnd can show tiles it primarily stores map data as *.obf files (it's own format) and renders the map from these files. If there is no file for the area you are interested in you can create one yourself with <a href="https://wiki.openstreetmap.org/wiki/OsmAndMapCreator">OsmAndMapCreator</a>. There are then different styles within the application for how these should be displayed, for custom styles see links in <a href="https://wiki.openstreetmap.org/wiki/OsmAnd#Custom_rendering_style">this section</a> of the OsmAnd wiki page.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '19, 16:21</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-68342" class="comments-container">
&#10;</div>
<div id="comment-tools-68342" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68342-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84191"></span>

<div id="answer-container-84191" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84191-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I wrote about this very problem last year. You can read about the whole solution here</p>
<p><a href="https://medium.com/@ty2/how-to-display-offline-maps-using-maplibre-mapbox-39ad0f3c7543">https://medium.com/@ty2/how-to-display-offline-maps-using-maplibre-mapbox-39ad0f3c7543</a></p>
<p>and the code for the same is here</p>
<p><a href="https://github.com/kuwapa/OfflineMapExample/tree/83c7e81391a5f0946ab1fcb3155966c4997d44d3">https://github.com/kuwapa/OfflineMapExample/tree/83c7e81391a5f0946ab1fcb3155966c4997d44d3</a></p>
<p>Essentially, solution is</p>
<ol>
<li>Use MapLibre SDK</li>
<li>Generate MBTILES using tilemaker or downloaded tiles from Maptiler (the important thing here is that the vector tiles in the MBTILES file are built using the openmaptiles styles)</li>
<li>Load MBTILES file in the assets folder on the Android app</li>
<li>Create a local style file json for vector tiles with a placeholder for a local MBTILES file.</li>
<li>In app code, load local style file, replaced placeholder with MBTILES file uri and add "mbtiles://" before the uri</li>
<li>Save new style file in some location</li>
<li>Open map, load the new style</li>
<li>View MBTILES file locally</li>
<li>For future for loading multiple MBTILES files together, create a local server and point the style file to local server and using local server, serve vector files to the map.</li>
</ol>
<p>I hope this helps. Please comment any questions you might have. Happy to help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '22, 09:18</strong></p>
<img src="https://secure.gravatar.com/avatar/79e65eed0a4d543a7229550d59f0e309?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="protos29&#39;s gravatar image" />
<p><span>protos29</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="protos29 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '22, 09:18</strong> </span></p>
</div>
</div>
<div id="comments-container-84191" class="comments-container">
&#10;</div>
<div id="comment-tools-84191" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84191-form-container" class="comment-form-container">
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

