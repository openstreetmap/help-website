+++
type = "question"
title = "Show My Location is very approximate"
description = '''I use a Samsung S21 phone. If I open the web page OpenStreetMap.org in Chrome and select Show My Location, the position shown is roughly 1000 m away from where I actually am. The marked position is surrounded by a blue circle and when I touch the centre it says &#x27;You are within 2000 m of this point&#x27;....'''
date = "2022-11-02T00:15:00Z"
lastmod = "2022-11-03T07:08:00Z"
weight = 86054
keywords = [ "location", "gps" ]
aliases = [ "/questions/86054" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Show My Location is very approximate](/questions/86054/show-my-location-is-very-approximate)

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
<span id="post-86054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86054-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use a Samsung S21 phone. If I open the web page OpenStreetMap.org in Chrome and select Show My Location, the position shown is roughly 1000 m away from where I actually am. The marked position is surrounded by a blue circle and when I touch the centre it says 'You are within 2000 m of this point'. Presumably this blue circle is 4000m in diameter and indicates that my position can't be accurately located.</p>
<p>My Location Service is turned on and GPS works fine in Google Maps and other similar mapping apps. To add insult to injury, my wife has a Samsung S8 and OpenStreetMaps.org positions her accurately within a few metres. Is there a setting somewhere that I'm missing?</p>
<p>When I use my desktop computer, the Show My Location position is a bit more accurate (within 750 m) and my desktop has no GPS!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '22, 00:15</strong></p>
<img src="https://secure.gravatar.com/avatar/43ea419946de5e356c9628aace45d869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WG50&#39;s gravatar image" />
<p><span>WG50</span><br />
<span class="score" title="81 reputation points">81</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WG50 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-86054" class="comments-container">
<span id="86057"></span>
<div id="comment-86057" class="comment">
<div id="post-86057-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Are you just using the website? This sounds like it's probably more of a phone issue than an OSM issue.</p>
</div>
<div id="comment-86057-info" class="comment-info">
<span class="comment-age">(02 Nov '22, 07:46)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="86059"></span>
<div id="comment-86059" class="comment">
<div id="post-86059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you sure that your GPS is working correctly? You can't check that with Google Maps since it also uses various network services to locate you. Check the GPS functionality of your device with other apps such as GPSTest or SatStat.</p>
</div>
<div id="comment-86059-info" class="comment-info">
<span class="comment-age">(02 Nov '22, 08:17)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86054" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86054-form-container" class="comment-form-container">
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

<span id="86067"></span>

<div id="answer-container-86067" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86067-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-86067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've stumbled on the answer! As noted by InsertUser it was a phone (and specifically Android 12) issue and not an OSM issue. I had previously checked that Chrome had permission to use my geolocation and that 'Use Precise Location' was enabled. As an experiment, I disabled 'Use Precise Location' then re-enabled it and the problem was solved!</p>
<p>The reason my wife's phone didn't have the same problem is that it uses Android 9 which doesn't have an option to turn precise location on and off for each app. In Android 9 geolocation in Chrome (and presumably in all apps) is either enabled or disabled with no option for selecting precise or approximate positioning.</p>
<p>I have no idea why disabling then re-enabling 'Use Precise Location' kicked it into action but it did.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '22, 20:40</strong></p>
<img src="https://secure.gravatar.com/avatar/43ea419946de5e356c9628aace45d869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WG50&#39;s gravatar image" />
<p><span>WG50</span><br />
<span class="score" title="81 reputation points">81</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WG50 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-86067" class="comments-container">
<span id="86068"></span>
<div id="comment-86068" class="comment">
<div id="post-86068-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've accepted your answer for you - hope you don't mind.</p>
</div>
<div id="comment-86068-info" class="comment-info">
<span class="comment-age">(02 Nov '22, 21:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="86069"></span>
<div id="comment-86069" class="comment">
<div id="post-86069-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No problem. I'm new to this and didn't realise I had to accept the answer. Actually I can't see where to do that either?</p>
</div>
<div id="comment-86069-info" class="comment-info">
<span class="comment-age">(02 Nov '22, 21:38)</span> <span class="comment-user userinfo">WG50</span>
</div>
</div>
<span id="86070"></span>
<div id="comment-86070" class="comment">
<div id="post-86070-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can't accept your own answer; that's why I did it.</p>
</div>
<div id="comment-86070-info" class="comment-info">
<span class="comment-age">(02 Nov '22, 21:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86067" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86067-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86073"></span>

<div id="answer-container-86073" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86073-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think much like if you opened up your maps app straight away, location services will give you an approximate initial location based on wifi location, bluetooth, cell triangulation, before gps kicks in and gives you a much more accurate location.</p>
<p>The first location you are getting is probably one of the more initial location methods. Which has the parking lot as that location.</p>
<p>It takes GPS some time to get a fix, so at least to cover this delay apple use other methods to get a near instant coarse location.</p>
<p>In fact if you say your friend is in the building they may not even get a GPS fix depending on how the building is constructed and how well the GPS signals will get into the buildi</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '22, 06:11</strong></p>
<img src="https://secure.gravatar.com/avatar/486a902de208f08f3eb976595c9a3b3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nakaru87&#39;s gravatar image" />
<p><span>nakaru87</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nakaru87 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86073" class="comments-container">
<span id="86074"></span>
<div id="comment-86074" class="comment">
<div id="post-86074-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry nakaru87, your answer makes no sense to me. The geolocation that was indicated on the openstreetmap.org web page didn't change with time - it remained a 'coarse' or approximate location even though 'Use Precise Location' (an Android setting) appeared to be enabled for Chrome. Turning 'Use Precise Location' off then on again fixed my problem and my geolocation now shows correctly on openstreetmap.org</p>
</div>
<div id="comment-86074-info" class="comment-info">
<span class="comment-age">(03 Nov '22, 07:08)</span> <span class="comment-user userinfo">WG50</span>
</div>
</div>
</div>
<div id="comment-tools-86073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86073-form-container" class="comment-form-container">
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

