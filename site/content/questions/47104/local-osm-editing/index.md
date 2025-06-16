+++
type = "question"
title = "Local OSM editing"
description = '''Finally i want to make my own local intranet map server with my changed tiles and nominatim. I just want to make an overview of security cameras in specific area of the map with geocoding (searching addresses). In JOSM editor I downloaded the specific part of the map i want. Now i want to add new ca...'''
date = "2015-12-11T17:13:00Z"
lastmod = "2015-12-18T22:22:00Z"
weight = 47104
keywords = [ "josm", "editing", "server", "osm", "local" ]
aliases = [ "/questions/47104" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Local OSM editing](/questions/47104/local-osm-editing)

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
<span id="post-47104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47104-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Finally i want to make my own local intranet map server with my changed tiles and nominatim. I just want to make an overview of security cameras in specific area of the map with geocoding (searching addresses).</p>
<p>In JOSM editor I downloaded the specific part of the map i want. Now i want to add new camera from presets to some place (no problem) with a symbol of a camera in the map (problem 1). Then what i want to do is to draw the area, which is monitored by this camera and fill this area with some color (problem 2). Then i want to save this map in osm format – load it to maperitive and generate tiles, which could look like my picture below. I tried to import to the map some picture with importimageplugin in JOSM, but after saving to osm format, loading to maperitive and rendering tiles, the picture wasn’t on the tiles (problem 3). Is possible to add icon of a camera and draw colored area of its monitoring in JOSM or in some other software?</p>
<p>I just read tutorials about nominatim install, but now the most important thing is to make the tiles with the security cameras and areas which are monitored by these cameras, because i am not shure, that i am able to install the nominatim, so i will be satisfied with a slippy map.</p>
<p>Sorry for my bad english and knowledge of osm, i am a beginner. I appreciate every answer.</p>
<p><img src="http://i.stack.imgur.com/ywMFa.jpg" alt="Picture 1" /> <img src="http://i.stack.imgur.com/Lsy3P.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '15, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/e9c07ac347c92626f2e1a6f98a82c9b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="-Ronadlisko-&#39;s gravatar image" />
<p><span>-Ronadlisko-</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="-Ronadlisko- has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-47104" class="comments-container">
&#10;</div>
<div id="comment-tools-47104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47104-form-container" class="comment-form-container">
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

<span id="47185"></span>

<div id="answer-container-47185" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47185-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-47185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="-Ronadlisko- has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This answer supposes that you want to do a webpage with cameras on it, if you want to render/print images then there are other plugins in QGIS for that.</p>
<p><strong>Add Data and style it</strong></p>
<ul>
<li>download QGIS</li>
<li>add openstreetmap base map</li>
<li>create two new layers one for points the other for areas</li>
<li>Add point *2</li>
<li>Add area *2</li>
<li>double click on the layer names</li>
<li>go to "styles" for each layer in turn</li>
<li>change transparency for polygon and then go to the other and add an SVG marker for the point</li>
</ul>
<p><strong>Export to webmap</strong></p>
<ul>
<li>install the plugin qgis2leaflet or perhaps qgis2web</li>
<li>in menu press web -&gt; qgis2leaflet</li>
<li>in dialog box:</li>
<li>press get layers</li>
<li>check convert to json</li>
<li>choose basemap</li>
<li>ask questions on IRC/gis.stackexchange.</li>
</ul>
<p>I know it doesn't involve OSM toolchain but it works, if the data about the cameras are from OSM data you can find them by using the QuickOSM plugin, then you only have to add the polygons manually.</p>
<p><img src="/upfiles/qgis_edit_camera.png" alt="editting data in Qgis with two layers and Openstreetmap base map" /> (The polygon layer is in edit mode that's why those red crosses are there, I'm modifying the yellow polygon when this screen shot was taken)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '15, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '15, 14:14</strong> </span></p>
</div>
</div>
<div id="comments-container-47185" class="comments-container">
<span id="47198"></span>
<div id="comment-47198" class="comment">
<div id="post-47198-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much, this is exactly the solution i was looking for. Now i am going to use the qgis2web plugin. After exporting i will change the tile path in index.html (which is generated by qgis2web) to my local tiles folder. Everything is working fine. One more time, thank you very much. If i could repay you for it, just tell me, because you really helped me.</p>
</div>
<div id="comment-47198-info" class="comment-info">
<span class="comment-age">(17 Dec '15, 11:50)</span> <span class="comment-user userinfo">-Ronadlisko-</span>
</div>
</div>
<span id="47223"></span>
<div id="comment-47223" class="comment">
<div id="post-47223-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm glad, I hope it works out for you. Feel free to either pay it forward, or just donate to either OSM or QGIS. <a href="https://www.qgis.org/en/site/getinvolved/donations.html">https://www.qgis.org/en/site/getinvolved/donations.html</a> <a href="http://donate.openstreetmap.org/">http://donate.openstreetmap.org/</a></p>
</div>
<div id="comment-47223-info" class="comment-info">
<span class="comment-age">(18 Dec '15, 22:22)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-47185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47185-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47119"></span>

<div id="answer-container-47119" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47119-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect the main issue could be that when you create and save new objects in JOSM they get negative IDs (proper IDs are allocated by the API post sucessful upload). It could well be that maperitive expects positive IDs (this is just speculation on my behalf, you need to test).</p>
<p>If this is indeed the problem you could simply renumber the OSM extract in question (DON'T EVER UPLOAD SUCH DATA!). Googling "OSM renumber" gives quite a number of results for tools that you could use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '15, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</img>
</div>
</div>
<div id="comments-container-47119" class="comments-container">
<span id="47173"></span>
<div id="comment-47173" class="comment">
<div id="post-47173-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the tip, but this solution is not what i need. JOSM really gives negative ID to each object i create and there is a possibility to change the ID, but i have to replace it for some existing OSM object ID everytime. So it is very difficult to renumber each object, because i want to add lots of object. Even if i renumber all ID i want, JOSM makes each object non-transparent and grey colored. What i want is a transparent colored area of camera monitoring - picture 1 and 2. Adding some image to JOSM with importimageplugin doesn't work, because when i load the changed osm file with some picture from JOSM to Maperitive, the picture doesn't show in the map. Do you have another tip for me?</p>
</div>
<div id="comment-47173-info" class="comment-info">
<span class="comment-age">(15 Dec '15, 19:43)</span> <span class="comment-user userinfo">-Ronadlisko-</span>
</div>
</div>
</div>
<div id="comment-tools-47119" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47119-form-container" class="comment-form-container">
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

