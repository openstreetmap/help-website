+++
type = "question"
title = "iOS - Android SDK ?"
description = '''Hi, I&#x27;m a complete newbie here. Please bear with me. I&#x27;m trying to find a way to include offline mapping in my iOS and Android app which effectively plots a GPS position (or many positions/trail) on a map background. I can do this live/on line (if a data connection is available) with, say, Google Ma...'''
date = "2011-09-21T14:38:00Z"
lastmod = "2011-09-23T12:23:00Z"
weight = 8066
keywords = [ "sdk", "ios", "amdroid" ]
aliases = [ "/questions/8066" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [iOS - Android SDK ?](/questions/8066/ios-android-sdk)

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
<span id="post-8066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8066-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm a complete newbie here. Please bear with me. I'm trying to find a way to include offline mapping in my iOS and Android app which effectively plots a GPS position (or many positions/trail) on a map background. I can do this live/on line (if a data connection is available) with, say, Google Maps, but now want to add offline capability.</p>
<p>I have the GPS/positioning (getting and manipulating Lat/Lon data) side of things pretty much sussed but have no idea how to simply/easily offer the capability to plot positions on a pre-downloaded map within my app. I can currently load in, say, an image, and display it but have no idea as to how to then scale said image correctly and pass in a position (Lat/Lon) for display on said 'image'...</p>
<p>Is there an SDK for Android / iOS ? Am I missing something really obvious ? Am I in the right place ? Maybe this has already been done and is now a little passee but I'm really keen to do soemthing with OSM as the map source. Sorry, completely lost !</p>
<p>Can anyone point me in the right direction please ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sdk" rel="tag" title="see questions tagged &#39;sdk&#39;">sdk</span> <span class="post-tag tag-link-ios" rel="tag" title="see questions tagged &#39;ios&#39;">ios</span> <span class="post-tag tag-link-amdroid" rel="tag" title="see questions tagged &#39;amdroid&#39;">amdroid</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '11, 14:38</strong></p>
<img src="https://secure.gravatar.com/avatar/e97550047f470639a8ac81615c36b87d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JanCol&#39;s gravatar image" />
<p><span>JanCol</span><br />
<span class="score" title="44 reputation points">44</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JanCol has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8066" class="comments-container">
&#10;</div>
<div id="comment-tools-8066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8066-form-container" class="comment-form-container">
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

<span id="8068"></span>

<div id="answer-container-8068" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8068-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-8068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap doesn't provide a formal SDK. We focus on creating the map data; we don't provide an end-user product or developer tools. We leave that to other people!</p>
<p>For iOS, the most popular map library is <a href="https://github.com/route-me/route-me">RouteMe</a>, which is open source. Bear in mind, however, that if your app uses map images from <a href="http://openstreetmap.org">openstreetmap.org</a>, you absolutely must adhere to the <a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy">Tile Usage Policy</a>, and that pretty much means using your own server or a third-party one unless you're expecting only miniscule amounts of usage.</p>
<p>You may also find <a href="http://developers.cloudmade.com/projects">CloudMade's SDKs</a> of interest.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '11, 16:03</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-8068" class="comments-container">
<span id="8072"></span>
<div id="comment-8072" class="comment">
<div id="post-8072-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi. Thanks for the answers. Appreciated. I'm still confused though - sorry... like i say, i'm new to this. So, I understand that OSM 'provides' the map data. And <code>others</code> provide the ability to view such data... I guess I'd like /need to find a suitable SDK -or- create my own but, how would i download a particular area/map tile? If i did download one, am i able to use it offline? Would i be able to zoom in/out or is the tile of a fixed zoom level once downloaded ? Would i need to download the same tile at various zoom levels to be able to zoom in/out or....is the map image/tile scaled? I mean how is the map bounds and scale data incorporated? Within the map 'tile' or as a separate 'data' file... I'm really keen to provide off-line mapping but am looking for some pointers as to the established 'norms' so i can decide if i need to create something myself and how simple it is to download the map tiles themselves and then scale them/set the lat/lon bounds etc Like i say, I'm keen to use OSM as my data source but am confused as to how to/where to start... as you'll have gathered from the above...</p>
<p>If you've gotten this far then thanks. I hope you can help point me in the right direction TIA, Jane.</p>
</div>
<div id="comment-8072-info" class="comment-info">
<span class="comment-age">(21 Sep '11, 22:28)</span> <span class="comment-user userinfo">JanCol</span>
</div>
</div>
<span id="8092"></span>
<div id="comment-8092" class="comment">
<div id="post-8092-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>First of all you need to decide whether you want map tiles (pre-rendered vector images, usually .pngs of 256x256 pixels each) or to draw your own map from vector data. Map tiles are easier to work with for simple map display - the Route-Me library, for example, uses map tiles - but you'll need to identify a server from where you can get them.</p>
<p>Once you've decided that, come back and ask us more - right now your question is a bit too open-ended for us to advise more.</p>
</div>
<div id="comment-8092-info" class="comment-info">
<span class="comment-age">(23 Sep '11, 11:40)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="8096"></span>
<div id="comment-8096" class="comment">
<div id="post-8096-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Saying more about that : map tiles are simple pre-rendered image files (png or jpg) you can store on your device for the offline mode. But be aware that this requires a lot of storage memory, depending the amount of zooms and the area you want to cover. Storing the vector data is surely an alternative that offers other possibilities like off-line routing but you will have to render the images yourself.</p>
</div>
<div id="comment-8096-info" class="comment-info">
<span class="comment-age">(23 Sep '11, 12:23)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-8068" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8068-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8079"></span>

<div id="answer-container-8079" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8079-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The map data is provided as whole planet dumps or extracts. See <a href="http://wiki.openstreetmap.org/wiki/Planet.osm">Planet.osm</a> on the wiki for more details. These are quite large files and contain every (current) bit of data is the osm database. For a mobile app you would probably run the data through filters beforehand possibly changing the format as well as discarding unwanted elements. Then you application would have to read the vector data and render it on the mobile device.</p>
<p>This is fairly complex to program, you might find open source programs which can do this already and try to use them.</p>
<p>The other way is to use map tiles which are rendered on a server and sent as pictures (usually png). This is what you see on the main site. You can use the tiles rendered by the openstreetmap servers but there is the <a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy">Tile Usage Policy</a> mentioned by Richard which doesn't allow mass downloading of tiles for offline use. The solution is to set up your own server to render the tiles (or find another source of tiles with a compatible usage policy).</p>
<p>A disadvantage of this is that the tiles take up quite a lot more storage than the vector data so the offline area would be more restricted. Making a program to display map tiles is much easier and uses less processing power on the device, again you might find an already existing open source program which would help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '11, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb4d30bb6d40cf9b3644ff4f453e5bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quantumstate&#39;s gravatar image" />
<p><span>quantumstate</span><br />
<span class="score" title="455 reputation points">455</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quantumstate has 3 accepted answers">30%</span></p>
</div>
</div>
<div id="comments-container-8079" class="comments-container">
&#10;</div>
<div id="comment-tools-8079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8079-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8071"></span>

<div id="answer-container-8071" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8071-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at the OSM wiki about <a href="http://wiki.openstreetmap.org/wiki/Apple_iOS">Apple iOS</a> and <a href="http://wiki.openstreetmap.org/wiki/Android">Android</a> ... there are some apps that are opensource.</p>
<p>Have a look how they get theit OSM derived data and how they display it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '11, 18:34</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-8071" class="comments-container">
<span id="8089"></span>
<div id="comment-8089" class="comment">
<div id="post-8089-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks... a lot to be thinking about. Thanks for the clear and concise answers to my somewhat vague questions. Back to the wiki.again - thanks</p>
</div>
<div id="comment-8089-info" class="comment-info">
<span class="comment-age">(22 Sep '11, 22:26)</span> <span class="comment-user userinfo">JanCol</span>
</div>
</div>
<span id="8090"></span>
<div id="comment-8090" class="comment">
<div id="post-8090-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks... like i say a lot to be thinking about. Need to decide first i guess on vector or png-style (raster, i guess) mapping... again, back to the wiki...</p>
</div>
<div id="comment-8090-info" class="comment-info">
<span class="comment-age">(22 Sep '11, 22:28)</span> <span class="comment-user userinfo">JanCol</span>
</div>
</div>
</div>
<div id="comment-tools-8071" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8071-form-container" class="comment-form-container">
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

