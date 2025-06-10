+++
type = "question"
title = "How can I show elevation &quot;ele=..&quot; in the map"
description = '''Hi to all The elevation &quot;ele=xyz&quot; in meters are shown directly in the map for the tags &quot;Natural=peck&quot; &quot;Natural=saddle&quot;. I tried in a lot of way but I cannot show in the map the elevation for others tags, for example of &quot;Place=hamlet&quot;. The purpose is to supply the information of the elevation directl...'''
date = "2016-11-01T17:17:00Z"
lastmod = "2016-11-02T22:45:00Z"
weight = 52775
keywords = [ "elevation", "ele" ]
aliases = [ "/questions/52775" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How can I show elevation "ele=.." in the map](/questions/52775/how-can-i-show-elevation-ele-in-the-map)

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
<span id="post-52775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52775-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all The elevation "ele=xyz" in meters are shown directly in the map for the tags "Natural=peck" "Natural=saddle". I tried in a lot of way but I cannot show in the map the elevation for others tags, for example of "Place=hamlet". The purpose is to supply the information of the elevation directly in the map without activate the layers and check the box Data in the map and select the tag and .... all annoying thinks when you use a smartphone in the mountains. Someone can help me ? Best regards Danilo PS I don't want insert estensively the elevation, from example from GPS data, because these are not reliable. I want take the elevation from the topo maps for some important tags (hamlet, path intersections, springs ...etc) if the GPS is not working well (it supplies wrong coordinates, sometimes happens) it is important to know the elevation of the place around to met it in the old way....</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span> <span class="post-tag tag-link-ele" rel="tag" title="see questions tagged &#39;ele&#39;">ele</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '16, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/443ca47def2516be9306b3419b80d789?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danbag&#39;s gravatar image" />
<p><span>danbag</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danbag has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52775" class="comments-container">
<span id="52778"></span>
<div id="comment-52778" class="comment">
<div id="post-52778-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When you say "shown directly in the map" what do you mean by "the map"?</p>
</div>
<div id="comment-52778-info" class="comment-info">
<span class="comment-age">(01 Nov '16, 20:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52794"></span>
<div id="comment-52794" class="comment">
<div id="post-52794-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sorry I have not explained that my notes are referred at mountains. Walking in that steep situation the elevation of a point sometime is much more important that the GPS coordinates.... it is so... beleave me ! Said that I think the situation is more clear... At the moment I have avoided the problem using a bug of OSM: the tag "place=locality" does not show nothing in the map (this is a bug) so I use that with "name=q.1740" and on the map we can see only the name and the name is the elevation (q. means quota,elevation). For another common situation I use to add to the name the elevation, example: place=hamlet ele=700 name=Intragna q.700</p>
<p>on the map we can see "Intragna q.700" with the simbol of hamlet.</p>
<p>I explain onother bug of OSM: the situation is: an old small village in mountain is now only ruins, its name is la Trecciura and its elevation is 1335 mt. The OSM code is:</p>
<p>name=la Trecciura q.1335 place=locality ele=1335</p>
<p>the ruins are coded in this way:</p>
<p>abandoned:building=ruins</p>
<p>On the map is shown ONLY the name "la Trecciura q.1335" there is no ruins, there is no icon of the locality ......</p>
<p>I have no words.....about the bugs and about the impossibilty to show the elevations, but I agree your suggestions.</p>
<p>Best regards Danilo (danbag)</p>
<p>PS you can see in the OSM map but is better in JOSM: q.1740 46°01.793'N 8°32.221'E la Trecciura q.1335 46°00.586'N 8°33.463'E and around that places a lot of examples tagged by me (danbag)</p>
</div>
<div id="comment-52794-info" class="comment-info">
<span class="comment-age">(02 Nov '16, 09:01)</span> <span class="comment-user userinfo">danbag</span>
</div>
</div>
<span id="52797"></span>
<div id="comment-52797" class="comment">
<div id="post-52797-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi danbag, please don’t use OSM and an editors bug as if it were your "own". Please read these pages <a href="https://wiki.openstreetmap.org/wiki/Names">https://wiki.openstreetmap.org/wiki/Names</a> (sorry not in Italian) and act accordingly by deleting your own "false" tags. And start reading these Italian <a href="https://wiki.openstreetmap.org/wiki/IT:Beginners%27_guide">https://wiki.openstreetmap.org/wiki/IT:Beginners%27_guide</a> as well ;-)</p>
</div>
<div id="comment-52797-info" class="comment-info">
<span class="comment-age">(02 Nov '16, 09:55)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="52803"></span>
<div id="comment-52803" class="comment">
<div id="post-52803-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the clarifications. I will delete the quote inserted erroneusly in the name, but the problem of elevation remain in "toto".... the bug used are clearly not a good solution but they solved the problem ! In any case I will delete.. and I stop to work with OSM in the same way I stopped with opensea for the same problem with the depths ... I answered to a opensea specialist in this way: in Italy we say that "il meglio uccide il bene" i.e. if someone want to reach the best it is possible he doesn't reach not even the good. In the sea the depth are important like in mountain the elevation, and if it is impossible to put both, the map in the sea and the map in mountain are useless. I am speaking with knowledgement both for mountain and for sea; I was alpinist and I reached the summit of 65 mountain over 4000 mt and in the sea I was with my boat in Greenland and at Cape Horn (detail in www.shaulatre.blogspot.it). Good luck !</p>
</div>
<div id="comment-52803-info" class="comment-info">
<span class="comment-age">(02 Nov '16, 22:31)</span> <span class="comment-user userinfo">danbag</span>
</div>
</div>
</div>
<div id="comment-tools-52775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52775-form-container" class="comment-form-container">
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

<span id="52804"></span>

<div id="answer-container-52804" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52804-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The map you see on openstreetmap.org is only one of <a href="http://wiki.openstreetmap.org/wiki/List_of_OSM-based_services">many different maps</a> based on the OSM database. While this one doesn't render the "ele" tag for most objects, there may be another map out there that does.</p>
<p>Very importantly, please do not <a href="http://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tag for the renderer</a>. The OSM data is used for many different purposes, not just for rendering images on a map. By adding the elevation to the name tag of an object, you make the name tag less useful for other data consumers. Please add the information in the intended tags and leave it up to each map renderer to decide what to show. Don't mix additional information into the name tag or use an inappropriate place=* tag just so an object will show up the way you want on one particular map rendering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '16, 22:33</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-52804" class="comments-container">
&#10;</div>
<div id="comment-tools-52804" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52804-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52805"></span>

<div id="answer-container-52805" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52805-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are currently 4 map styles on OpenStreetMap.org. the "standard" map style (which I presume you are talking about) is only one of those 4. It does not show the elevantion for "place=locality", but it does for "natural=peak". The "standard" map style is maintained <a href="https://github.com/gravitystorm/openstreetmap-carto/">here</a>. With a github account you can log bugs there and suggest improvements. It isn't possible to show absolutely everything in OSM data though - it would just look a mess. However, iIf you want to show elevation data against things like localities, then you can create your own map using OSM data to show that. Various "how to set up a server for my own map style" sites have been set up, including <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">this one</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '16, 22:45</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-52805" class="comments-container">
&#10;</div>
<div id="comment-tools-52805" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52805-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52777"></span>

<div id="answer-container-52777" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52777-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi danbag, there some hiccups in your plan. What do you want to do with the knowledge ? Here are a few points; A saddle and peak have a pin point height, A hamlet like Castelmezzano is pin pointed by its size, but looking at the widely spread buildings over some distance, it is clearly a village on a hillside. The height won’t be a pin pointed spot but a moving one (downhill) with every new building added to the hamlet or village. Copying form any map won’t do, because the copyright and agreements as stated here, <a href="https://wiki.openstreetmap.org/wiki/Open_Database_License">https://wiki.openstreetmap.org/wiki/Open_Database_License</a><br />
Use your own not reliable GPS together with a lot of other people to get a reliable outcome, but it’s not ready quick. But in the end you ve got to talk about it at the tagging and other OSM Fora to do so.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '16, 20:18</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Nov '16, 20:21</strong> </span></p>
</div>
</div>
<div id="comments-container-52777" class="comments-container">
&#10;</div>
<div id="comment-tools-52777" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52777-form-container" class="comment-form-container">
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

