+++
type = "question"
title = "Please Help me to find proper libraries for my android(and iOS after that) app"
description = '''Hi guys, Here is what I have in my mind:  I have a ~40GB compressed XML file on the host of OSM, I want to have separate downloadable files on my website for each city, so one shouldn&#x27;t download whole country&#x27;s database. However I guess I should include freeways and outskirts of a city, and it will ...'''
date = "2015-07-19T12:18:00Z"
lastmod = "2015-07-24T08:47:00Z"
weight = 44270
keywords = [ "openstreetmap" ]
aliases = [ "/questions/44270" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Please Help me to find proper libraries for my android(and iOS after that) app](/questions/44270/please-help-me-to-find-proper-libraries-for-my-androidand-ios-after-that-app)

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
<span id="post-44270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44270-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys, Here is what I have in my mind:</p>
<ul>
<li>I have a ~40GB compressed XML file on the host of OSM, I want to have separate downloadable files on my website for each city, so one shouldn't download whole country's database. However I guess I should include freeways and outskirts of a city, and it will probably have common areas if one wants to download two nearby cities, so it should understand and won't download what is already available.</li>
<li>No need to download further information for routing. The routing information should be included</li>
<li>I want to add extra information about a point on the map (either text or image), and they should be dynamic, so it shows metro schedule and the next train, or current problems on route or certain location online.</li>
<li>I want to add traffic information, and include it in routing.</li>
<li>If it is possible I want to add multiple condition for routing, e.g. one can say how can I go to X and have a Gas station, bank and... in my way with minimum traffic base on the hour.</li>
</ul>
<p>I haven't worked with OSM APIs, so I don't know what they can do... which would work together better, and where should I implement my own codes. I read wiki.openstreetmap.org, but there where little information about each APIs and it would be nice to see a lot of sample codes so I can get ideas from them, there are only a simple project with each API, not a compilation of them.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '15, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0f14e93f9694860b5e7619e7ea826d57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="youyeg&#39;s gravatar image" />
<p><span>youyeg</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="youyeg has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jul '15, 12:19</strong> </span></p>
</div>
</div>
<div id="comments-container-44270" class="comments-container">
<span id="44273"></span>
<div id="comment-44273" class="comment">
<div id="post-44273-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>This is way too ambitious for a simple help.openstreetmap.org answer. Essentially you want a complete mapping stack customised to your own requirements. Your requirements would take an OSM specialist days, even weeks to build (and several parts, such as train schedules and traffic levels, are not included in OSM at any rate). I think the nearest you'll get is checking out Mapbox's paid-for plans (<a href="http://mapbox.com">http://mapbox.com</a>), which are substantially OSM-based, and seeing if any of them come close to your requirements.</p>
</div>
<div id="comment-44273-info" class="comment-info">
<span class="comment-age">(19 Jul '15, 16:14)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="44277"></span>
<div id="comment-44277" class="comment">
<div id="post-44277-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know where to began and choose which APIs. I need to know where I should began to implement my own parts, and where I can use others' work. I explained, so you know where I am to go. Thanks..</p>
</div>
<div id="comment-44277-info" class="comment-info">
<span class="comment-age">(19 Jul '15, 21:25)</span> <span class="comment-user userinfo">youyeg</span>
</div>
</div>
<span id="44285"></span>
<div id="comment-44285" class="comment">
<div id="post-44285-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>First of all, <a href="https://wiki.openstreetmap.org/wiki/API">openstreetmap.org's API</a> is for editing. You're not building a map editor, so it's not relevant to you. You will need to use third-party components based on OSM data. As it happens, since you want offline use, online "APIs" per se probably aren't much use.</p>
<p>As SomeoneElse said, you need to break the question into parts - you have asked for simply too much. But at a very rough stab, look at GraphHopper for routing, and the Mapbox SDKs for map display. Traffic information is not included in OSM, nor are public transport timetables. I don't know of any modern, common library that uses the same info for map display and for routing.</p>
</div>
<div id="comment-44285-info" class="comment-info">
<span class="comment-age">(20 Jul '15, 08:31)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="44286"></span>
<div id="comment-44286" class="comment not_top_scorer">
<div id="post-44286-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You know, the reason why I explain my work as a whole was that the reader know what I need. Surely if I wanted to ask separately I should have give explanation for each API I think I might need, and I thought it would cause further confusion. Anyway, I looked into Mapbox, and began to read its documents. About the traffic, I was thinking if it is possible to give the routes a weight, like a graph, so the nearest destination calculate base on the sum of weights. I don't expect that I have all I want at once, I want a library to access to map, a library for routing, and a library to display the map, and I know I should develop rest of it on my own. Could you please recommend those library which work best together? Reading map, Displaying map, and Routing. Thanks :)</p>
</div>
<div id="comment-44286-info" class="comment-info">
<span class="comment-age">(20 Jul '15, 08:53)</span> <span class="comment-user userinfo">youyeg</span>
</div>
</div>
<span id="44288"></span>
<div id="comment-44288" class="comment">
<div id="post-44288-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Well, the general expectation is that you try and find some stuff out yourself, and then come here when you're stuck.</p>
<p>Yes, you can give segments in a routing graph a weight, using OSRM or GraphHopper or any similar library. I'd suggest you download one, play with it, and then ask again here if you're having troubles.</p>
<p>Bear in mind that OSRM (aka Mapbox Directions) will not run comfortably on-device, whereas GraphHopper can.</p>
</div>
<div id="comment-44288-info" class="comment-info">
<span class="comment-age">(20 Jul '15, 09:05)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="44289"></span>
<div id="comment-44289" class="comment not_top_scorer">
<div id="post-44289-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Richard.</p>
</div>
<div id="comment-44289-info" class="comment-info">
<span class="comment-age">(20 Jul '15, 09:09)</span> <span class="comment-user userinfo">youyeg</span>
</div>
</div>
<span id="44330"></span>
<div id="comment-44330" class="comment">
<div id="post-44330-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The main OSM API is only for editing so you won't be using that. Then there's a Nominatim API operated by the project which allows you to find places on the map of which you only know a name. Then there's project-osrm.org which is a third-party OSM based routing engine that finds you the fastest route from A to B. Then there's overpass-api.de which is a third-party search service for the OSM database that can do more "programmer like" queries than Nominatim can. All of these services require an online connection and have strict usage limits. If you want to go offline then you might want to look into "libosmscout". But if you hope that there are ready-made components that you just have to mix and match then you will be disappointed; existing libraries will only do a small part of what you are looking for.</p>
</div>
<div id="comment-44330-info" class="comment-info">
<span class="comment-age">(21 Jul '15, 19:10)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="44336"></span>
<div id="comment-44336" class="comment not_top_scorer">
<div id="post-44336-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your answer was very helpful Frederik, I wish I know more about OSM-based free offline APIs so I could combine and develop what I need. I looked into wiki.openstreetmap.org, but there were no comprehensive list of OSM-based projects, it would be great if there were a list with features of each one. Anyway, I should thank you a lot. :)</p>
</div>
<div id="comment-44336-info" class="comment-info">
<span class="comment-age">(22 Jul '15, 08:46)</span> <span class="comment-user userinfo">youyeg</span>
</div>
</div>
</div>
<div id="comment-tools-44270" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-44270-form-container" class="comment-form-container">
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

<span id="44279"></span>

<div id="answer-container-44279" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44279-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As Richard has said, public libraries to do what you want in its entirety do not exist (on any platform). As you've found, there are solutions to some parts of the problems that you're posing yourself, but not others, and certainly not all together.</p>
<p>Where you go next is likely to depend on what it is that you're actually trying to do and how much money you've got - are you trying to develop a commercial app, or is this just a college project? If the former, then paying someone someone else to help you with what's possible, what's not and how much it'll all cost is surely the way forward. There are some possibilities listed <a href="https://switch2osm.org/providers/">here</a>, and I'm sure there will be suggestions in the wiki too. If the latter, then obviously you have to develop something yourself. I'd suggest breaking the problem down into parts and seeing what bits OSM data can help with and what parts it can't. The essence of OSM is that 40Gb of data that you've downloaded - what you do with it after that is up to you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '15, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-44279" class="comments-container">
&#10;</div>
<div id="comment-tools-44279" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44279-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44388"></span>

<div id="answer-container-44388" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44388-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For Android you can try mapsforge and GraphHopper which both are running offline on the device. GraphHopper includes a simple Android demo including some maps to download. GraphHopper also runs <a href="https://github.com/graphhopper/graphhopper-ios">on iOS</a> too, but I do not know much about offline libs for maps there. (note: I'm the author of GraphHopper)</p>
<p>But traffic data and offline is not fitting well together :). Though you can integrate traffic in the routing but your devices need online access - see <a href="https://karussell.wordpress.com/2015/04/08/visualize-and-handle-traffic-information-with-graphhopper-in-real-time-for-cologne-germany-koln/">this blog post</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '15, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/fec61c70a4cc98b1e84a5dfbde1e9a6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peatar&#39;s gravatar image" />
<p><span>peatar</span><br />
<span class="score" title="351 reputation points">351</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peatar has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-44388" class="comments-container">
<span id="44402"></span>
<div id="comment-44402" class="comment">
<div id="post-44402-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I began to work of GraphHopper, and I will ask if there were anything to ask. I thought I could have something like MAMPS.ME (MapsWithMe) so routing data and maps data could be together. Would it be possible? With GraphHopper? :) Thanks.</p>
</div>
<div id="comment-44402-info" class="comment-info">
<span class="comment-age">(24 Jul '15, 08:47)</span> <span class="comment-user userinfo">youyeg</span>
</div>
</div>
</div>
<div id="comment-tools-44388" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44388-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44272"></span>

<div id="answer-container-44272" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44272-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi youyeg, two rules for this forum; its specific for OSM troubles, not for developers and theyre troubleshooting. ask one question at the time, so that you end up whith an clear answer to your question. Greetz Ps Try to ask or take a look here <a href="https://wiki.openstreetmap.org/wiki/Develop">https://wiki.openstreetmap.org/wiki/Develop</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '15, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-44272" class="comments-container">
<span id="44282"></span>
<div id="comment-44282" class="comment">
<div id="post-44282-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, could you please link me to the proper section? Thanks. :)</p>
</div>
<div id="comment-44282-info" class="comment-info">
<span class="comment-age">(20 Jul '15, 05:30)</span> <span class="comment-user userinfo">youyeg</span>
</div>
</div>
</div>
<div id="comment-tools-44272" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44272-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44281"></span>

<div id="answer-container-44281" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44281-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK. But, what I was looking for was what the existing APIs can do, and where should I try to fill the gap. It would be very appreciated if someone could say: A can do this, but has this limitation, and B can do that part for you and... I couldn't even find collection of examples in OSM, just API and an example only for that API. I wish I could find a slightly similar project and look into it and then finally figure out what should I do!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '15, 03:10</strong></p>
<img src="https://secure.gravatar.com/avatar/0f14e93f9694860b5e7619e7ea826d57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="youyeg&#39;s gravatar image" />
<p><span>youyeg</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="youyeg has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jul '15, 05:34</strong> </span></p>
</div>
</div>
<div id="comments-container-44281" class="comments-container">
&#10;</div>
<div id="comment-tools-44281" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44281-form-container" class="comment-form-container">
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

