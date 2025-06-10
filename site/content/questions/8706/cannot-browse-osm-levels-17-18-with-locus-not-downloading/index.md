+++
type = "question"
title = "Cannot browse OSM levels 17-18 with Locus (NOT downloading)"
description = '''Hello, I found recently that I cannot access the upper levels of OSM using Locus for browsing the maps. I am aware that no downloading of these levels is allowed and Locus AFAIK would not allow it in the current version; but why OSM server bans usual normal browsing with Locus, showing &quot;app is block...'''
date = "2011-10-30T21:32:00Z"
lastmod = "2011-11-03T14:53:00Z"
weight = 8706
keywords = [ "locus" ]
aliases = [ "/questions/8706" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot browse OSM levels 17-18 with Locus (NOT downloading)](/questions/8706/cannot-browse-osm-levels-17-18-with-locus-not-downloading)

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
<span id="post-8706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8706-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I found recently that I cannot access the upper levels of OSM using Locus for <strong>browsing</strong> the maps. I am aware that no downloading of these levels is allowed and Locus AFAIK would not allow it in the current version; but why OSM server bans <strong>usual normal browsing</strong> with Locus, showing "app is blocked" tiles instead of normal tiles? The app is actually nice browser which caches everything once seen, and I use this feature a lot, without any need for preemptive mass-downloading.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-locus" rel="tag" title="see questions tagged &#39;locus&#39;">locus</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '11, 21:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c7090ee680c9d288f1e78b2572de9729?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Denmes&#39;s gravatar image" />
<p><span>Denmes</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Denmes has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8706" class="comments-container">
<span id="8707"></span>
<div id="comment-8707" class="comment">
<div id="post-8707-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>How would you suggest that OSM finds out if you are just viewing the tiles or downloading them?</p>
</div>
<div id="comment-8707-info" class="comment-info">
<span class="comment-age">(30 Oct '11, 21:37)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="8708"></span>
<div id="comment-8708" class="comment">
<div id="post-8708-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Probably, it would be right when server would just reasonably limit the downloading rate or the number of high-resolution tiles downloaded from certain IP address in any given hour (or minute, or day, or whatever). It isn't fair to plainly ban Locus as browser because some dumbheads overload servers abusing the download feature of the generally very useful app.</p>
</div>
<div id="comment-8708-info" class="comment-info">
<span class="comment-age">(30 Oct '11, 21:52)</span> <span class="comment-user userinfo">Denmes</span>
</div>
</div>
</div>
<div id="comment-tools-8706" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8706-form-container" class="comment-form-container">
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

<span id="8709"></span>

<div id="answer-container-8709" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8709-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is nothing the openstreetmap administrators should do about this. There is no way to detect if a user uses Locus for mass download or browsing. A filter on IP have been tryed and it gives many false positives or fails to stop abusers. It is realy hard for a computer to see the difference betwean valid users with NAT and abusers.</p>
<p>As far as I see Locus does most things right like limiting download rate and providing a vector map. However it seems that it is possible to download tiles for offline use (if this is not correct ask the developers to contact OSM).</p>
<p>If the creators of Locus would add a speccial User-Agent when the user browses the map, or disallowes download from <a href="http://tile.openstreetmap.org">tile.openstreetmap.org</a> Locus will be allowed to browse all zoom levels. There are many other maps based on OSM out there and it is easy to set up your own tile server.</p>
<p>It is nice to see that the two most used OSM applications have moved to vector maps. Offline maps is a good selling point that others can't provide.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '11, 00:24</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-8709" class="comments-container">
<span id="8724"></span>
<div id="comment-8724" class="comment">
<div id="post-8724-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is it entirely forbidden to download tiles preemptively? Locus currently allows to load up to 10000 tiles per day (sized from 25 000 in previous version).</p>
<p>By the way, I have tried vector maps with Locus and they are quite ok, but they are lacking building numbers and other descriptions in contrast to the maps from OSM servers. Are vector maps distributed this way or the problem is caused by Locus?</p>
<p>And a question out of curiosity. Did administration of OSM ever think to distribute map data (tiles) by torrent? This would allow people to download what they want without overloading tile servers.</p>
</div>
<div id="comment-8724-info" class="comment-info">
<span class="comment-age">(31 Oct '11, 18:37)</span> <span class="comment-user userinfo">Denmes</span>
</div>
</div>
<span id="8727"></span>
<div id="comment-8727" class="comment">
<div id="post-8727-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The <a href="http://wiki.openstreetmap.org/wiki/Tile_Usage_Policy">Tile Usage Policy</a> says that all "bulk downloading is strongly discouraged" and that permission must be obtained in advance by the app author.</p>
<p>The vector data distributed by OSM contains everything we have. If Locus choose not to render all of it that's their choice.</p>
</div>
<div id="comment-8727-info" class="comment-info">
<span class="comment-age">(31 Oct '11, 21:55)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="8736"></span>
<div id="comment-8736" class="comment">
<div id="post-8736-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Have you worked out the implications of what you are asking? There are thousands of Locus users, if they each downloaded 10,000 tiles that is tens of millions of tiles, each day!</p>
<p>The answer lies in the hands of the authors of Locus. If they set up a tile server for their product then they could scale their tile server to support their customers. They would impose no load on OSM tile servers and they could provide different styles for different customers and even charge money for that. Instead they choose to free-load from the OSM tile servers and their customers are now being penalised.</p>
</div>
<div id="comment-8736-info" class="comment-info">
<span class="comment-age">(01 Nov '11, 12:05)</span> <span class="comment-user userinfo">ChrisH</span>
</div>
</div>
</div>
<div id="comment-tools-8709" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8709-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8743"></span>

<div id="answer-container-8743" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8743-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a new blog post from the OpenStreetMap Foundation describing the challenges of serving tiles to popular applications. <a href="http://blog.osmfoundation.org/2011/11/01/tile-usage-policy/">http://blog.osmfoundation.org/2011/11/01/tile-usage-policy/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '11, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Weait has 8 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-8743" class="comments-container">
<span id="8744"></span>
<div id="comment-8744" class="comment">
<div id="post-8744-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understand the point of OSM admins pretty well, but the idea of the blocking is generally wrong, even if there's no other way for now. There should be some reasonable way to let end user download what he wants. The downloading is also a kind of use. Map caching and preemtive downloads are extremely useful when cellular internet isn't available while travelling, and even when it is - map download on-the-go may be slow and always very energy-consuming.</p>
</div>
<div id="comment-8744-info" class="comment-info">
<span class="comment-age">(01 Nov '11, 15:05)</span> <span class="comment-user userinfo">Denmes</span>
</div>
</div>
<span id="8745"></span>
<div id="comment-8745" class="comment">
<div id="post-8745-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Look, the situation is quite simple. OSMf does not have the recorces to allow every request to go thrugh. They are prioritizing requests from users causualy browsing the map. The alternative is to shut down the server.</p>
<p>If Locus wants their paying customers to mass download free maps OSMf is not the right place. They should take some of the income they make from the service and set up their own tile server. This can be done within the hour.</p>
<p>If OSMf had have more recorces they could accept more requests. However it is not the job of OSMf to run tile generators for software companies.</p>
</div>
<div id="comment-8745-info" class="comment-info">
<span class="comment-age">(01 Nov '11, 15:39)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
<span id="8751"></span>
<div id="comment-8751" class="comment">
<div id="post-8751-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>"There should be some reasonable way to let end user download what he wants."</p>
<p>I would like some free beer every day. There should be some reasonable way to let me have what I want.</p>
<p>Come on!</p>
</div>
<div id="comment-8751-info" class="comment-info">
<span class="comment-age">(01 Nov '11, 18:14)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="8754"></span>
<div id="comment-8754" class="comment">
<div id="post-8754-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>However it is not the job of OSMf to run tile generators for software companies.</p>
</blockquote>
<p>No, there is something wrong with the logic. The access should be then also blocked for any user running Windows/MacOS, because they use paid software to access OSM and download tiles.</p>
</div>
<div id="comment-8754-info" class="comment-info">
<span class="comment-age">(01 Nov '11, 20:20)</span> <span class="comment-user userinfo">Denmes</span>
</div>
</div>
<span id="8755"></span>
<div id="comment-8755" class="comment">
<div id="post-8755-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"I would like some free beer every day."</p>
<p>No, I didn't mean it this way. The OSM foundation is giving away its stuff for free, it just don't have enough resources to service all requests. And its going to be worse in the future. At certain point the foundation may not be able to service even browsing-only users when they are numerous enough. Unfortunately, I am not educated enough in all the technical stuff to say or to do the right thing, so I'm just speculating/discussing. I am very grateful to all people who created and maintain the amazing OSM service. I just wish it to be even better.</p>
</div>
<div id="comment-8755-info" class="comment-info">
<span class="comment-age">(01 Nov '11, 20:35)</span> <span class="comment-user userinfo">Denmes</span>
</div>
</div>
</div>
<div id="comment-tools-8743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8743-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8782"></span>

<div id="answer-container-8782" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8782-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi guys, tile server is in preparation now. Did you read this post? <a href="http://www.openstreetmap.org/user/!i!/diary/15190.">http://www.openstreetmap.org/user/!i!/diary/15190.</a> There is nice graph that show current stat. I completely! disable downloading of tiles from your server during October. So since version 1.14.0 and up, Locus is not allowed to directly download map tiles from your server, so it works only as a viewer. Is there now any chance to unblock access to tiles level 17 and higher for app with user agent Locus/1.14.0 and higher?</p>
<p>I hope that server will be ready till end of November so then I hope that most of current users will use this server that will serve only for Locus.</p>
<p>Just one think (to comment previous posts), access to maps is exactly same for Free and Pro version of app. So I don't want money from users for maps! Pro version is payed for extra functionality that offer, not for maps! And also, Free version is fully functional, not just some time limited demo, so I'm really trying to offer people fully working app and if they want some extra ...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '11, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/d2aebf074a0667a95d09bf5c48baa12e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="menion&#39;s gravatar image" />
<p><span>menion</span><br />
<span class="score" title="88 reputation points">88</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="menion has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Nov '11, 05:53</strong> </span></p>
</div>
</div>
<div id="comments-container-8782" class="comments-container">
&#10;</div>
<div id="comment-tools-8782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8782-form-container" class="comment-form-container">
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

