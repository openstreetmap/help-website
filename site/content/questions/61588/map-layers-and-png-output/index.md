+++
type = "question"
title = "Map layers and .png output"
description = '''I&#x27;m having trouble with two things. The first is that I want 2 maps, one without roads or highway shields and a second with only roads and highway shields in order to insert a traffic layer between them. The second is that I would like to download, using C#, a .png file of each map described above. ...'''
date = "2018-01-11T18:19:00Z"
lastmod = "2018-01-19T14:36:00Z"
weight = 61588
keywords = [ "layers", "usage", "png" ]
aliases = [ "/questions/61588" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Map layers and .png output](/questions/61588/map-layers-and-png-output)

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
<span id="post-61588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61588-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm having trouble with two things.</p>
<p>The first is that I want 2 maps, one without roads or highway shields and a second with only roads and highway shields in order to insert a traffic layer between them.</p>
<p>The second is that I would like to download, using C#, a .png file of each map described above.</p>
<p>In javascript using leaflet, this seems to support this download, but it seems to derived from the leaflet.js.</p>
<p>new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');</p>
<p>Any help with these would be welcome and appreciated.</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-png" rel="tag" title="see questions tagged &#39;png&#39;">png</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '18, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/1e84593f7ccde651358522a82e90b3dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chascallaway&#39;s gravatar image" />
<p><span>chascallaway</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chascallaway has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jan '18, 20:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-61588" class="comments-container">
<span id="61589"></span>
<div id="comment-61589" class="comment">
<div id="post-61589-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>At the risk of stating the obvious, if you want to download a .png map tile layer with only certain data on it (say, no roads) then you're going to need to create a map style that shows the information you want and render the tiles for the area that you're interested in.</p>
<p>Or, alternatively, look for a "non-png" based approach - there are various ways of creating "vector tiles" out there, not all documented very well unfortunately, but this may be a more suitable approach for you.</p>
</div>
<div id="comment-61589-info" class="comment-info">
<span class="comment-age">(12 Jan '18, 00:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61590"></span>
<div id="comment-61590" class="comment">
<div id="post-61590-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I admit I'm a newbie, but I'm aware that I need to create a map style that shows the information I want but all I find at openstreetmap.org is a selection of styles - all without specific layer (badges, road, water, etc.) settings. For instance, I can choose a background but what if I don't want one at all?</p>
<p>If I need to create a stylesheet specifically disabling the hundred or so layers exposed by MapBox, I can, but what are they called?</p>
<p>And a C# sample I could find to download a (styled) .png file from a url???</p>
<p>Thanks</p>
</div>
<div id="comment-61590-info" class="comment-info">
<span class="comment-age">(12 Jan '18, 01:40)</span> <span class="comment-user userinfo">chascallaway</span>
</div>
</div>
<span id="61591"></span>
<div id="comment-61591" class="comment">
<div id="post-61591-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So this is a question about OpenStreetMap in the Mapbox UI ?</p>
</div>
<div id="comment-61591-info" class="comment-info">
<span class="comment-age">(12 Jan '18, 04:26)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="61592"></span>
<div id="comment-61592" class="comment">
<div id="post-61592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No. I wish not to use MapBox if possible.</p>
</div>
<div id="comment-61592-info" class="comment-info">
<span class="comment-age">(12 Jan '18, 06:58)</span> <span class="comment-user userinfo">chascallaway</span>
</div>
</div>
<span id="61693"></span>
<div id="comment-61693" class="comment">
<div id="post-61693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK. No answers yet.<br />
So, is it possible to turn off the roads or background layers in open source openstreetmap? Can an openstreetmap map be saved as a .png file?</p>
</div>
<div id="comment-61693-info" class="comment-info">
<span class="comment-age">(17 Jan '18, 23:44)</span> <span class="comment-user userinfo">chascallaway</span>
</div>
</div>
</div>
<div id="comment-tools-61588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61588-form-container" class="comment-form-container">
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

<span id="61694"></span>

<div id="answer-container-61694" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61694-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61694-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61694-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>So, is it possible to turn off the roads or background layers in open source openstreetmap? Can an openstreetmap map be saved as a .png file?</code></pre>
<p>The answer is "yes", but the problem is there are many different sorts of "OpenStreetMap map". You're going to have to find one that suits your needs.</p>
<p>OpenStreetMap is basically just a big lump of data. The process of turning that into a map is called <a href="https://wiki.openstreetmap.org/wiki/Rendering">rendering</a>. As can be seen from that page, you have a huge number of options. Looking at one example, the "standard" map style that's the default at osm.org is described <a href="https://github.com/gravitystorm/openstreetmap-carto/">here</a>. The map is composed of lots of smaller .png files joined together. These .pngs are sent from the map server to the client and knitted together there. The layers in that map are described in <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/project.mml">this file</a>. Each of those layers is described by something like <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/landcover.mss">this</a>. There are many more carto-based styles that work in the same basic way as this one, but there are many many more using different technologies altogether. <a href="http://paulnorman.ca/blog/2016/11/serving-vector-tiles/">Here</a>, for example, is an in-depth discussion of some of the various vector tile technologies available for use with OpenStreetMap data. With vector tiles, instead of .pngs being sent from server to client data is, and the client then renders it.</p>
<p>You won't be able to start with an existing example and "turn off a layer" to create something that works for you; you'll need to start with something very simple that contains minimal information in the three layers that you're interested in and work up from there. You'll need to decide whether something based on raster tiles, vector tiles or a combination (data drawn on top of raster tiles) is best for you, and that'll depend on things like what is going to be the client and server in your example, available bandwidth, available storage space, the amount of the world you want to be able to process and many more variables.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '18, 00:13</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-61694" class="comments-container">
<span id="61727"></span>
<div id="comment-61727" class="comment">
<div id="post-61727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. It reflects a knowledge of OpenStreetMap maps far beyond mine. I'll gladly award points, but how many points are a lot? I would like to reflect the level of my appreciation. I naively thought this would be easy.</p>
<p>That said, at this time, I need to get static maps of about 2 dozen locations defined by bounding boxes but need two maps for each - a background, which I can get, but also a second map having only the road badges plus road and city names (.png - I'm adding an additional layer between them). I can get the first one without issue. Both maps will be saved as .png in a C# app. I like MapBox and Google maps, but the recurring cost is prohibitive.</p>
<p>Whom would you suggest I approach to get this done?</p>
</div>
<div id="comment-61727-info" class="comment-info">
<span class="comment-age">(19 Jan '18, 14:36)</span> <span class="comment-user userinfo">chascallaway</span>
</div>
</div>
</div>
<div id="comment-tools-61694" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61694-form-container" class="comment-form-container">
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

