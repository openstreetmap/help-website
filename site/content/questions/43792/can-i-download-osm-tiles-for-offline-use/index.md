+++
type = "question"
title = "Can i download osm tiles for offline use?"
description = '''Hi, I&#x27;m trying to create an application using map which will work on intranet and requires no internet connectivity. Is there a legal option to download the tiles (very few) for my offline implementation ? Or should i have to contact any System administrators for getting licence for it ? If so kindl...'''
date = "2015-06-26T05:45:00Z"
lastmod = "2018-10-11T19:05:00Z"
weight = 43792
keywords = [ "offline", "local-tile-server", "tiles", "offlinemaps" ]
aliases = [ "/questions/43792" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Can i download osm tiles for offline use?](/questions/43792/can-i-download-osm-tiles-for-offline-use)

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
<span id="post-43792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43792-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to create an application using map which will work on intranet and requires no internet connectivity.</p>
<p>Is there a legal option to download the tiles (very few) for my offline implementation ?</p>
<p>Or should i have to contact any System administrators for getting licence for it ?</p>
<p>If so kindly provide me any contact like emailid to get clarified.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-local-tile-server" rel="tag" title="see questions tagged &#39;local-tile-server&#39;">local-tile-server</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-offlinemaps" rel="tag" title="see questions tagged &#39;offlinemaps&#39;">offlinemaps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '15, 05:45</strong></p>
<img src="https://secure.gravatar.com/avatar/c6f76b29e7070eba5f36b050f89f7fc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rramprakash1&#39;s gravatar image" />
<p><span>rramprakash1</span><br />
<span class="score" title="55 reputation points">55</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rramprakash1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43792" class="comments-container">
<span id="43798"></span>
<div id="comment-43798" class="comment">
<div id="post-43798-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you tell us about how many tiles you are talking? Which zoom level(s) and which area size?</p>
</div>
<div id="comment-43798-info" class="comment-info">
<span class="comment-age">(26 Jun '15, 07:48)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="43807"></span>
<div id="comment-43807" class="comment">
<div id="post-43807-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure about the number of tiles. But as far as zoom levels as concern it will be from 17 to 19 so that the markers added to the tile will give good visibility to user. Also the site range will not exceed more than 2 kilometers (Eg: a foot ball court, airport or college campus).</p>
</div>
<div id="comment-43807-info" class="comment-info">
<span class="comment-age">(26 Jun '15, 10:09)</span> <span class="comment-user userinfo">rramprakash1</span>
</div>
</div>
<span id="43811"></span>
<div id="comment-43811" class="comment">
<div id="post-43811-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I also wonder how often you will download the tiles. Depending on the region the downloaded tiles might be out-of-date sooner than later.</p>
</div>
<div id="comment-43811-info" class="comment-info">
<span class="comment-age">(26 Jun '15, 12:28)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="43812"></span>
<div id="comment-43812" class="comment">
<div id="post-43812-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The download is done only during the initial setup of application only once. As of now we are not concerned about updating the tiles</p>
</div>
<div id="comment-43812-info" class="comment-info">
<span class="comment-age">(26 Jun '15, 12:31)</span> <span class="comment-user userinfo">rramprakash1</span>
</div>
</div>
<span id="43813"></span>
<div id="comment-43813" class="comment">
<div id="post-43813-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There seems to be something of a communications failure here - the answers below ("no, you can't download lots of tiles directly from OSM" and "you don't need to - just stick a tile server on your intranet") are both correct, yet you still seem to be waiting for someone to say "yes, download all the tiles that you want". Unfortunately, that isn't going to happen - but as listed below, you have at least 3 other options.</p>
</div>
<div id="comment-43813-info" class="comment-info">
<span class="comment-age">(26 Jun '15, 12:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="66301"></span>
<div id="comment-66301" class="comment not_top_scorer">
<div id="post-66301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello friends,</p>
<p>Which one of you could do that service to get tile render png osm?</p>
</div>
<div id="comment-66301-info" class="comment-info">
<span class="comment-age">(11 Oct '18, 19:05)</span> <span class="comment-user userinfo">CLAGOS</span>
</div>
</div>
</div>
<div id="comment-tools-43792" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-43792-form-container" class="comment-form-container">
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

<span id="43793"></span>

<div id="answer-container-43793" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43793-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-43793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes you can download (very few!) tiles, but need to respect the tile usage policy to avoid stressing our servers <a href="https://wiki.openstreetmap.org/wiki/Category:Tile_downloading">https://wiki.openstreetmap.org/wiki/Category:Tile_downloading</a><br />
You need also to respect the legal aspects if you ship it with your application <a href="https://wiki.openstreetmap.org/wiki/Legal_FAQ">https://wiki.openstreetmap.org/wiki/Legal_FAQ</a></p>
<p>Another alternative is to render your own tiles using an desktop renderer as Tilemill, maperitive, ...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '15, 06:11</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-43793" class="comments-container">
<span id="43794"></span>
<div id="comment-43794" class="comment">
<div id="post-43794-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But i came across in a wiki stating : "These tiles are generally not available (cached) on the server in advance, and have to be rendered specifically for those requests, putting an unjustified burden on the available resources." Are you still sure of downloading tiles to server for offline use ?</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">https://wiki.openstreetmap.org/wiki/Tile_usage_policy</a></p>
</div>
<div id="comment-43794-info" class="comment-info">
<span class="comment-age">(26 Jun '15, 06:33)</span> <span class="comment-user userinfo">rramprakash1</span>
</div>
</div>
<span id="43795"></span>
<div id="comment-43795" class="comment">
<div id="post-43795-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As the text says, this is for high zoom tiles as they would take to much space. You might also use existing 3rd party tile services as mapquest, ...</p>
</div>
<div id="comment-43795-info" class="comment-info">
<span class="comment-age">(26 Jun '15, 06:38)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="43796"></span>
<div id="comment-43796" class="comment">
<div id="post-43796-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But for my application, I had to download tiles with higher zoom levels so that the user can be able to view the markers not in a congested manner. Kindly mention me if i have to contact anybody for it if i have to pay for any licencing option.</p>
<p>Referred MapQuest few days back, but the service is changed and not consistant also the Leaflet APIs are also not accessible now.</p>
<p><a href="https://developer.mapquest.com/documentation/documentation/leaflet-plugins/maps">https://developer.mapquest.com/documentation/documentation/leaflet-plugins/maps</a></p>
<p>Also raised for clarification in their forum too and there is no response yet :</p>
<p><a href="https://developer.mapquest.com/forum/downloading-map-tile-offline-use">https://developer.mapquest.com/forum/downloading-map-tile-offline-use</a></p>
<p>I'm also in the middle of developement. Any help regarding offline map is appreciated.</p>
</div>
<div id="comment-43796-info" class="comment-info">
<span class="comment-age">(26 Jun '15, 07:16)</span> <span class="comment-user userinfo">rramprakash1</span>
</div>
</div>
<span id="43806"></span>
<div id="comment-43806" class="comment">
<div id="post-43806-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>try mapbox</p>
</div>
<div id="comment-43806-info" class="comment-info">
<span class="comment-age">(26 Jun '15, 09:58)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43793" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43793-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43799"></span>

<div id="answer-container-43799" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43799-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A better alternative would be downloading the OSM <em>data</em> instead and running your own intranet tile server. There's a wide choice of tools for this; I had a great time processing the data into my own tiles with Tilemill - see e.g. this: <a href="https://www.mapbox.com/blog/create-a-custom-map-of-your-city-in-30-minutes-with-tilemill-and-openstreetmap/">https://www.mapbox.com/blog/create-a-custom-map-of-your-city-in-30-minutes-with-tilemill-and-openstreetmap/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '15, 08:25</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-43799" class="comments-container">
<span id="43805"></span>
<div id="comment-43805" class="comment">
<div id="post-43805-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>See also:</p>
<p><a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a></p>
<p>If you're only interested in tiles for a region that's "small" in OSM terms (such as India), then the infrastructure you need for a tile server isn't large - it's well within "off the shelf desktop PC" territory.</p>
</div>
<div id="comment-43805-info" class="comment-info">
<span class="comment-age">(26 Jun '15, 09:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43799-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49521"></span>

<div id="answer-container-49521" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49521-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, you can do that now thanks to vector tiles: See <a href="http://osm2vectortiles.org/">http://osm2vectortiles.org/</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '16, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/019a45dc05eab7273c5b5a662b899848?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Geonick&#39;s gravatar image" />
<p><span>Geonick</span><br />
<span class="score" title="106 reputation points">106</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Geonick has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49521" class="comments-container">
&#10;</div>
<div id="comment-tools-49521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49521-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53178"></span>

<div id="answer-container-53178" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53178-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am working on similar requirement, may be helpful for such requirement.</p>
<p><a href="https://github.com/gagan-bansal/osm-for-my-country">osm-for-my-country</a> install all osm dependent packages and libs through scripts. With this you can download your country data and create all map tiles on your server.</p>
<p>It's small effort to make OSM map usage simple.</p>
<p><a href="https://github.com/gagan-bansal/osm-for-my-country">https://github.com/gagan-bansal/osm-for-my-country</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '16, 05:02</strong></p>
<img src="https://secure.gravatar.com/avatar/39d75f04e1a21ba653b41ac75ec1b026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gagan&#39;s gravatar image" />
<p><span>Gagan</span><br />
<span class="score" title="305 reputation points">305</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gagan has 2 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '17, 09:20</strong> </span></p>
</div>
</div>
<div id="comments-container-53178" class="comments-container">
<span id="53184"></span>
<div id="comment-53184" class="comment">
<div id="post-53184-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just to clarify the technologies used: This is based on raster tiles and server-side CartoCSS styling language whereas OSM2VectorTiles.org (and OpenMapTiles) are based on vector tiles and client-side MB JS styling language.</p>
</div>
<div id="comment-53184-info" class="comment-info">
<span class="comment-age">(30 Nov '16, 19:20)</span> <span class="comment-user userinfo">Geonick</span>
</div>
</div>
<span id="53187"></span>
<div id="comment-53187" class="comment">
<div id="post-53187-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/1667/geonick">@geonick</a> Thanks for adding input.</p>
</div>
<div id="comment-53187-info" class="comment-info">
<span class="comment-age">(01 Dec '16, 03:35)</span> <span class="comment-user userinfo">Gagan</span>
</div>
</div>
</div>
<div id="comment-tools-53178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53178-form-container" class="comment-form-container">
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

