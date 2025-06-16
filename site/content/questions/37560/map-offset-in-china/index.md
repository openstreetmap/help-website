+++
type = "question"
title = "Map offset in China"
description = '''Hi. I&#x27;m in China. I want to use the Open Street Map Android app to grab Lat and Long point data and then drop that data into a Google Fusion table.  When I do that and then view the corresponding map in Fusion the map points are offset - meaning located on the map 100s of metres from where they shou...'''
date = "2014-10-13T04:00:00Z"
lastmod = "2015-04-08T12:32:00Z"
weight = 37560
keywords = [ "china", "offset" ]
aliases = [ "/questions/37560" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Map offset in China](/questions/37560/map-offset-in-china)

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
<span id="post-37560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37560-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I'm in China. I want to use the Open Street Map Android app to grab Lat and Long point data and then drop that data into a Google Fusion table.</p>
<p>When I do that and then view the corresponding map in Fusion the map points are offset - meaning located on the map 100s of metres from where they should be.</p>
<p>I understand a little about the offset issue in China. However, if the OSM app correctly identifies my position on the China map (I'm in Shanghai) why does the Lat and Long position not translate to the correct location when I then add that data to a Fusion table?</p>
<p>Can anyone simply describe the issue with GPS offset issues in China? For example my Android Nexus 5 GPS module must be providing the correct Lat and Long details is that correct? Then when they are added to another mapping service - such as Google they are offset, why? The Google Map app on my Android device correctly positions me on the map.</p>
<p>It's a headache, I'd love if someone can help me understand the issues and also let me know how I can correctly gather Lat and Long data on my mobile device that can be used in another mapping application - I want to create localised maps in Shanghai as part of a university initiative.</p>
<p>Thanks! Adrian</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-china" rel="tag" title="see questions tagged &#39;china&#39;">china</span> <span class="post-tag tag-link-offset" rel="tag" title="see questions tagged &#39;offset&#39;">offset</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '14, 04:00</strong></p>
<img src="https://secure.gravatar.com/avatar/17685e03496c78b3d820b825c4e621e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amhodge&#39;s gravatar image" />
<p><span>amhodge</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amhodge has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '14, 04:18</strong> </span></p>
</div>
</div>
<div id="comments-container-37560" class="comments-container">
<span id="42195"></span>
<div id="comment-42195" class="comment">
<div id="post-42195-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've created a Wikipedia page describing the <a href="https://en.wikipedia.org/wiki/Restrictions_on_geographic_data_in_China#The_China_GPS_shift_problem">China GPS offset issue</a>.</p>
</div>
<div id="comment-42195-info" class="comment-info">
<span class="comment-age">(08 Apr '15, 12:32)</span> <span class="comment-user userinfo">dandv</span>
</div>
</div>
</div>
<div id="comment-tools-37560" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37560-form-container" class="comment-form-container">
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

<span id="37567"></span>

<div id="answer-container-37567" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37567-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-37567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Due to some Chinese regulation from the Cold War, Chinese maps have an offset (i assume it used to be secret otherwise it makes little sense).</p>
<p>You can read more about it here: <a href="http://www.polastre.com/2013/02/what-the-map/" title="What The Map? Why Maps in China Are Offset">What The Map? Why Maps in China Are Offset</a></p>
<p>I don't know anything about Google Fusion tables, but since Google (and others) know about this offset, my guess is that they compensate for it when you use fusion tables.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '14, 08:59</strong></p>
<img src="https://secure.gravatar.com/avatar/b9a8b8a3b1418b4b0bb41041555b18a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dymo12&#39;s gravatar image" />
<p><span>Dymo12</span><br />
<span class="score" title="796 reputation points">796</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dymo12 has 2 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '14, 09:05</strong> </span></p>
</div>
</div>
<div id="comments-container-37567" class="comments-container">
&#10;</div>
<div id="comment-tools-37567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37567-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37582"></span>

<div id="answer-container-37582" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37582-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37582-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-37582-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Google can fake the GPS position to be in accordance to its <a href="http://mc.bbbike.org/mc/?lon=102.71079&amp;lat=25.07972&amp;zoom=16&amp;num=4&amp;mt0=mapnik&amp;mt1=google-map&amp;mt2=google-satellite&amp;mt3=bing-satellite">offset-plagued chinese map</a> when you use Google's Android map app, but not when you upload context-free GPS positions to Google Fusion. The raw GPS points you collected are likely correct, and overlaying them on Google Map will reveal the legaly-imposed forgery.</p>
<p>If you use an OSM basemap instead of a Google one, it'll look ok. Mapbox has <a href="https://www.mapbox.com/mapbox-studio/source-quickstart/">a tool that can cover many Google Fusion usecases</a>, so does <a href="http://geojson.io/">geojson.io</a> and maybe <a href="https://wiki.openstreetmap.org/wiki/GIS_software">others</a> depending on your usecase.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '14, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-37582" class="comments-container">
<span id="37606"></span>
<div id="comment-37606" class="comment">
<div id="post-37606-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for this explanation it helps me a lot.</p>
<p>If my GPS lat and long data is correct (grabbed from OSM) and the map on my phone is provided by Google (or whomever) what is it that China is doing that causes the offset? As I understand the Google map is offset - but who offsets it? The Four Sq. map using Google maps is offset. Yet my native Google Maps app reports my correct position, as does the OSM map. So, why can't Four Square use the same map as the Google native app?</p>
<p>For my work with Fusion or other mapping tool I'll test with the OSM base map.</p>
<p>Thanks again!</p>
</div>
<div id="comment-37606-info" class="comment-info">
<span class="comment-age">(14 Oct '14, 03:53)</span> <span class="comment-user userinfo">amhodge</span>
</div>
</div>
<span id="37609"></span>
<div id="comment-37609" class="comment">
<div id="post-37609-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The chinese government is asking map providers to add the random offsets. Look at yandex maps in my first link for example: the offets are different from Google's. So the offset is a legal obligation, but left as an exercise for the map provider. Because of OSM's structure, that kind of legal presure can't be used against OSM, so you get unskewed data from OSM.</p>
<p>Concerning Foursquare, they switched from GoogleMaps to OSM not too long ago, but not on all platforms. Phone apps still typically use the phone's native map, which on Android phones is Google.</p>
</div>
<div id="comment-37609-info" class="comment-info">
<span class="comment-age">(14 Oct '14, 12:35)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="37618"></span>
<div id="comment-37618" class="comment">
<div id="post-37618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you again. My mobile is a Nexus 5 from Hong Kong. The Google Map app installed on the device hasn't been vetted by China or given to China by Google I'm guessing, it's just installed on the phone via the app store. My location is reported correctly on the map. But not in the Foursquare app (and others) that are using Google Maps - and not in the new My Maps Google app?? China can't interfere with the data received from the GPS module on the phone (?) and they don't have control over the apps. At what point are they interfering with the system?</p>
</div>
<div id="comment-37618-info" class="comment-info">
<span class="comment-age">(15 Oct '14, 04:27)</span> <span class="comment-user userinfo">amhodge</span>
</div>
</div>
<span id="37620"></span>
<div id="comment-37620" class="comment">
<div id="post-37620-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Google is a company. Google wants to earn money in China. Therefore Google has to comply with Chinese government regulations. This means modifications of both their web map as well as any of their map-related apps. Your GPS module will report the correct coordinates but the location will always be wrong when displayed on a map provided by a commercial company. Use a free map instead and the problem will be gone.</p>
</div>
<div id="comment-37620-info" class="comment-info">
<span class="comment-age">(15 Oct '14, 10:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="37634"></span>
<div id="comment-37634" class="comment">
<div id="post-37634-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Whatever steps the GoogleMap app takes to offet your location so that it matches the map offets arent taken by the Foursquare app, despite using the Google Map. Do not confuse the map data with the app that displays it.</p>
<p>I guess the Google developers did just enough to not be censored by the Chinese government, so the illusion isn't perfect as you can see when using the Foursquare app.</p>
</div>
<div id="comment-37634-info" class="comment-info">
<span class="comment-age">(15 Oct '14, 18:42)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37582" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37582-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37562"></span>

<div id="answer-container-37562" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37562-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's hard to tell what goes wrong, without having more details, but here are some points to think/investigate</p>
<ol>
<li>Your conversion algorithm is wrong</li>
<li>The original points in OSM have an offset</li>
<li>The Fusion table is showing them on a map that has an offset. I vaguely remember reading something about differences between OSM and other maps in the US as well</li>
<li>A GPS always has a offset. E.g. my GPS always displays the fault tolerance. It can be as good as up the 1m, but it can also be several meters (e.g. in narrow streets between buildings, or near a cliff). Maybe some governments do not allow accurate GPS reporting.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '14, 04:29</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-37562" class="comments-container">
<span id="37565"></span>
<div id="comment-37565" class="comment">
<div id="post-37565-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I agree with escada, especially concerning the unavoidable offset from your Android-Nexus GPS points. There is always some offset and the amount of it depends on many things: buildings, tree cover, etc. The only way to insure your area of interest in OSM is accurately positioned is to manually offset the underlying imagery using several GPS traces, the more the better. Even then, the imagery only a few meters away might be aligned differently because of problems with "stitching" the image tiles together.</p>
</div>
<div id="comment-37565-info" class="comment-info">
<span class="comment-age">(13 Oct '14, 08:24)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-37562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37562-form-container" class="comment-form-container">
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

