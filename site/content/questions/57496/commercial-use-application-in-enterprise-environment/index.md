+++
type = "question"
title = "Commercial use Application in Enterprise Environment"
description = '''I am currently writing an application in VB.net using the Gmap.Net framework. I have read several posts on commercial use and OpenStreetMap data. However, I am still unsure and would like to hear from someone who may be able to provide an expert answer.  I am not an expert on the framework itself, b...'''
date = "2017-08-07T20:03:00Z"
lastmod = "2017-08-08T09:50:00Z"
weight = 57496
keywords = [ "commercial", "visualbasic", "gmap" ]
aliases = [ "/questions/57496" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Commercial use Application in Enterprise Environment](/questions/57496/commercial-use-application-in-enterprise-environment)

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
<span id="post-57496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57496-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently writing an application in VB.net using the Gmap.Net framework. I have read several posts on commercial use and OpenStreetMap data. However, I am still unsure and would like to hear from someone who may be able to provide an expert answer.</p>
<p>I am not an expert on the framework itself, but in short the application is simply providing a map to the users using the Gmap Control. The user is then able to place markers based on their own points of interest.</p>
<p>I want to potentially put the application on the marker. It would not be for the public but be sold to enterprise companies revolving around Public Safety. It is almost as if they were accessing OpenStreetMap from a browser and entering in the data to add points of interest markers, however the database of POI would be stored locally on their computer.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-commercial" rel="tag" title="see questions tagged &#39;commercial&#39;">commercial</span> <span class="post-tag tag-link-visualbasic" rel="tag" title="see questions tagged &#39;visualbasic&#39;">visualbasic</span> <span class="post-tag tag-link-gmap" rel="tag" title="see questions tagged &#39;gmap&#39;">gmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '17, 20:03</strong></p>
<img src="https://secure.gravatar.com/avatar/02fc17b7fef3d87157c21fe97d7a4a43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MatthewJones&#39;s gravatar image" />
<p><span>MatthewJones</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MatthewJones has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57496" class="comments-container">
&#10;</div>
<div id="comment-tools-57496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57496-form-container" class="comment-form-container">
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

<span id="57497"></span>

<div id="answer-container-57497" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57497-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-57497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two sides to this. One is that if you want to display OSM maps on the device, the maps need to come from somewhere. If you are planning to use a public tile server like tile.openstreetmap.org to show maps to users of your application, make sure to observe the <a href="https://operations.osmfoundation.org/policies/tiles/">tile usage policy</a>. This is not relevant if you create your own tiles or have someone create them for you, of course.</p>
<p>The other is the licensing side. If your users place markers on the OSM map then these markers might constitute a "derived database" in the sense of OSM's open license, meaning that if (!) the markers were publicly used they would have to be shared under the ODbL license (i.e. no publishing of images with a byline of "this data is intended for XY use only, copying prohibited" or so). As long as the data is only used internally by the user of your application, however, nothing like that will happen. For details on the license ssee <a href="http://wiki.osmfoundation.org/wiki/Licence">http://wiki.osmfoundation.org/wiki/Licence</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '17, 21:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-57497" class="comments-container">
<span id="57498"></span>
<div id="comment-57498" class="comment">
<div id="post-57498-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Let me give you a better description of the application;</p>
<p>The application only lets the user put the markers as an overlay on the map, there is not changing of the data to the map. I would be like holding a picture up to a glass and then the user writing on the glass that is visible with the map as a background.</p>
<p>Of course coordinates are being used, and routing, but only at a small scale. As far as tiles go, I am not sure what constitutes as heavy tile useage. The max zoom is set at 17 to help with that. So say you are using the application and you work for a company that purchased my application. You are a in public safety and you see that there is an emergency at a certain address, you would then add a marker at that point or Lat/Long but as an overlay.</p>
<p>I wish I knew more on how the tiles are fetched, they are obviously fetched from the server, but I don't fully understand how every piece of the framework, works.</p>
<p>Your answer has helped, but I hope my explanation helped for future answers.</p>
</div>
<div id="comment-57498-info" class="comment-info">
<span class="comment-age">(07 Aug '17, 22:12)</span> <span class="comment-user userinfo">MatthewJones</span>
</div>
</div>
<span id="57502"></span>
<div id="comment-57502" class="comment">
<div id="post-57502-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>License-wise, the "user writing on glass" doesn't absolve you from the consequences of share-alike, since your users might use the OSM map to place their markers; example: the user knows they want to place a marker "right in front of XY church on ZZ street", and only through OSM do they know where that is. The the marker is derived from OSM.</p>
<p>Regarding the tiles - read www.switch2osm.org and you will know how to set up your own tile server. OSM tile servers are financed by donations and kept running by volunteers; even though their performance and reliability outclasses many commercial offerings, you shouldn't rely on them for a commercial application. If you don't want to set up your own tile server, then you can look into commercial offerings on <a href="http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services</a> (disclosure: I work for one such company).</p>
</div>
<div id="comment-57502-info" class="comment-info">
<span class="comment-age">(08 Aug '17, 09:50)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57497-form-container" class="comment-form-container">
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

