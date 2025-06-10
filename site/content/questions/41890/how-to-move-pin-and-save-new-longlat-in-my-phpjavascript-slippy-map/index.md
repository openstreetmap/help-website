+++
type = "question"
title = "How to move &quot;pin&quot; and save new Long/Lat in my php/javascript slippy map?"
description = '''I have been looking into getting GPS info from devices and simply displaying a map pin and all - quite simple stuff really. However, I can&#x27;t help but notice that the &quot;pin&quot; is too often quite a distance from the actual location. I&#x27;d therefore like to be able to move the &quot;pin&quot; and retrieve the new lon...'''
date = "2015-03-24T19:45:00Z"
lastmod = "2022-10-20T06:47:00Z"
weight = 41890
keywords = [ "marker", "development", "javascript", "map" ]
aliases = [ "/questions/41890" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to move "pin" and save new Long/Lat in my php/javascript slippy map?](/questions/41890/how-to-move-pin-and-save-new-longlat-in-my-phpjavascript-slippy-map)

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
<span id="post-41890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41890-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been looking into getting GPS info from devices and simply displaying a map pin and all - quite simple stuff really. However, I can't help but notice that the "pin" is too often quite a distance from the actual location. I'd therefore like to be able to move the "pin" and retrieve the new longitude/latitude (saved in MySQL for example) for later use.</p>
<p>Could somebody please example how this can be achieved (assuming its feasible of course).</p>
<p>More details: I'm using a little javascript and PHP to create a simple web page to show "saved locations". The initial location is being captured from a phone or extracted from the JPG/EXIF data, where its saved to a database for future display. However, in the interests of accuracy, I'd like to be able to move this "initial" location and update the long/lat in the database accordingly. Ideally this would be by; viewing the current pined location on a map and allow it to be moved - each move could be used to update longitude and latitude stored in the database.</p>
<p>thanks in advance, Brain.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '15, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/09b5e9597ead940880976aa14db980fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brainie&#39;s gravatar image" />
<p><span>Brainie</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brainie has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '15, 21:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-41890" class="comments-container">
<span id="41892"></span>
<div id="comment-41892" class="comment">
<div id="post-41892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>about which "pin" are you talking? in a specific program/website?</p>
</div>
<div id="comment-41892-info" class="comment-info">
<span class="comment-age">(24 Mar '15, 20:22)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="41902"></span>
<div id="comment-41902" class="comment">
<div id="post-41902-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ta - by pin - I mean the image (marker.png) which shows the location on the map (is there a technical term for this?)</p>
</div>
<div id="comment-41902-info" class="comment-info">
<span class="comment-age">(25 Mar '15, 09:39)</span> <span class="comment-user userinfo">Brainie</span>
</div>
</div>
<span id="41921"></span>
<div id="comment-41921" class="comment">
<div id="post-41921-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the <a href="https://www.openstreetmap.org/?mlat=20.00&amp;mlon=75.00#map=6/17.078/75.740">red one</a> is a bit more frequently (than "pin") called "marker" (as in your image file name). I have added a bit text from your comment below to your question text to clarify it.</p>
</div>
<div id="comment-41921-info" class="comment-info">
<span class="comment-age">(25 Mar '15, 21:02)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41890-form-container" class="comment-form-container">
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

<span id="41905"></span>

<div id="answer-container-41905" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41905-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could use a JavaScript library (Leaflet, OpenLayers) to display the map and the pins. Those libraries are also capable to convert a mouse click on the map into long/lat, which can then be used to update your data via a call to your server.</p>
<p>an example: <a href="http://openlayers.org/en/v3.2.1/examples/drag-features.html">http://openlayers.org/en/v3.2.1/examples/drag-features.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '15, 10:53</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '15, 21:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-41905" class="comments-container">
<span id="41911"></span>
<div id="comment-41911" class="comment">
<div id="post-41911-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That sounds hopefuly, thank you very much.</p>
</div>
<div id="comment-41911-info" class="comment-info">
<span class="comment-age">(25 Mar '15, 13:31)</span> <span class="comment-user userinfo">Brainie</span>
</div>
</div>
</div>
<div id="comment-tools-41905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41905-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41899"></span>

<div id="answer-container-41899" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41899-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming you are talking about waypoints created on a GPS device. Most GPS devices will allow you to move the waypoint (aka pin) to a new location. My GPS allows me to move the waypoint on the map or to type in explicit coordinates.</p>
<p>I assume that software such as Basecamp (from Garmin) can do the same, once you have downloaded the files to your PC.</p>
<p>Of course this approach only works when you are talking about the GPS tracks and waypoint files generated by the GPS device.</p>
<p>You can always "move a pin", i.e. change it coordinates, because that is just data in a file or database. The actual solution depends in which file (and where) you have stored your waypoints/pins</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '15, 08:28</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '15, 08:29</strong> </span></p>
</div>
</div>
<div id="comments-container-41899" class="comments-container">
<span id="41900"></span>
<div id="comment-41900" class="comment">
<div id="post-41900-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah... OK not quite what the problem, sorry I'll try again. I'm using a little javascript and PHP to create a simple web page to show "saved locations". The initial location is being captured from a phone or extracted from the JPG/EXIF data, where its saved to a database for future display. However, in the interests of accuracy, I'd like to be able to move this "initial" location and update the long/lat in the database accordingly. Ideally this would be by; viewing the current pined location on a map and allow it to be moved - each move could be used to update longitude and latitude stored in the database.</p>
</div>
<div id="comment-41900-info" class="comment-info">
<span class="comment-age">(25 Mar '15, 09:34)</span> <span class="comment-user userinfo">Brainie</span>
</div>
</div>
</div>
<div id="comment-tools-41899" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41899-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85928"></span>

<div id="answer-container-85928" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85928-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I was looking for how to extract the coordinates from Google Maps, but now I think it's already paid... It was then that I discovered OpenStreetMap, what I don't know is if you can make this html code work:</p>
<p><a href="https://imagesearchreverse.com/get-coordinates-map.html">https://imagesearchreverse.com/get-coordinates-map.html</a></p>
<p>My idea is that the users publish their photos and have the possibility to choose where the photos were taken... If anyone has new information that can help us, I would greatly appreciate it.</p>
<p>Either way, I'll keep looking to find and share a solution around here-.</p>
<p>Thanks!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '22, 06:47</strong></p>
<img src="https://secure.gravatar.com/avatar/dab75831bfc00e22b348249c1a95040f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="torres187&#39;s gravatar image" />
<p><span>torres187</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="torres187 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85928" class="comments-container">
&#10;</div>
<div id="comment-tools-85928" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85928-form-container" class="comment-form-container">
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

