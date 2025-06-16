+++
type = "question"
title = "Jumping to a specific set of coordinates on the map"
description = '''I have the coordinates (latitude and longitude) for a location. How can I make the map on www.openstreetmap.org display the area in question?'''
date = "2011-12-29T00:57:00Z"
lastmod = "2017-10-12T18:38:00Z"
weight = 9669
keywords = [ "osm.org", "entering", "coordinates" ]
aliases = [ "/questions/9669" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Jumping to a specific set of coordinates on the map](/questions/9669/jumping-to-a-specific-set-of-coordinates-on-the-map)

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
<span id="post-9669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9669-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-9669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the coordinates (latitude and longitude) for a location. How can I make the map on www.openstreetmap.org display the area in question?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-entering" rel="tag" title="see questions tagged &#39;entering&#39;">entering</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '11, 00:57</strong></p>
<img src="https://secure.gravatar.com/avatar/68674d3986e8e974ff3ab159a91b29be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allan%20J&#39;s gravatar image" />
<p><span>Allan J</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allan J has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jul '16, 20:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-9669" class="comments-container">
&#10;</div>
<div id="comment-tools-9669" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9669-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="9673"></span>

<div id="answer-container-9673" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9673-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-9673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The web site on <a href="http://www.openstreetmap.org">www.openstreetmap.org</a> does not have a dedicated coordinate input field, but you can easily construct an URL that gets you to a set of coordinates by writing</p>
<p><a href="https://www.openstreetmap.org/?mlat=">https://www.openstreetmap.org/?mlat=</a><em>latitude</em>&amp;mlon=<em>longitude</em>&amp;zoom=12</p>
<p>You can also enter <em>latitude</em>,<em>longitude</em> in the search box which will then present you with a pseudo "search result" consisting of exactly such a link.</p>
<p>It would be trivial to set up your own OpenLayers web site that has a dedicated latitude/longitude input box if that is important to you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '11, 07:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9673" class="comments-container">
<span id="13252"></span>
<div id="comment-13252" class="comment">
<div id="post-13252-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And this make another example why osm is useless.</p>
<p>a friend give me this location. i will use google, because there is no other variant that i can use without installing a server !!!!!!~!! Are you kidding me ?</p>
<p>45°31’49.28″N, 25°59’18.94″E</p>
<p>this is basic, not even basic, but elementary.</p>
<p>happy complaining that people prefer to use gm instead of osm.</p>
<p>Don`t make a google maps competition, but make the site usable at least.</p>
</div>
<div id="comment-13252-info" class="comment-info">
<span class="comment-age">(04 Jun '12, 18:24)</span> <span class="comment-user userinfo">Badita Florin</span>
</div>
</div>
<span id="13253"></span>
<div id="comment-13253" class="comment">
<div id="post-13253-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Yes. You need coordinates with decimal degrees, not the ones with degrees, minutes, and decimal seconds that you have used. Convert a DD°MM'SS.FF coordinate to decimal degrees by computing the value of DD+(MM/60)+(SS.FF/3600), use a negative sign for West or South. In your case this yields 49.530355 and 25.98859. Of course you could easily make a Javascript page that does this computation if you wanted. You could also ask people to add this code to the main OSM web site but opening your request with the line "OSM is useless" will not get you the desired response.</p>
</div>
<div id="comment-13253-info" class="comment-info">
<span class="comment-age">(04 Jun '12, 18:24)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="15807"></span>
<div id="comment-15807" class="comment">
<div id="post-15807-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Frederik I understand you, but I think that altough he is not polite he represents very big userbase. I think OSM community should start seriously investigate what are the blockers for these users, because by not giving them what need we potentially loose many users and later on contributors. I think we should learn from reactions like that.</p>
</div>
<div id="comment-15807-info" class="comment-info">
<span class="comment-age">(05 Sep '12, 09:04)</span> <span class="comment-user userinfo">gorn</span>
</div>
</div>
<span id="15828"></span>
<div id="comment-15828" class="comment">
<div id="post-15828-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Fully agree with Gorn, the feature of being able to enter coordinates in some different formats both in the viewer and Potlatch editor is absolutely essential!</p>
</div>
<div id="comment-15828-info" class="comment-info">
<span class="comment-age">(05 Sep '12, 18:41)</span> <span class="comment-user userinfo">tobiasra</span>
</div>
</div>
<span id="16083"></span>
<div id="comment-16083" class="comment">
<div id="post-16083-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am glad for all the answers, and i know that osm.org is not a website, it`s a database.</p>
<p><span>@Frederik</span> i am saying strong statements because i`m sick of seeing people contributing to the wrong project (by wrong i reffer to closed sourced ) instead of osm because they will not use 10 different websites when they could use only one.</p>
<p>I do workshops and presentations where i present osm and the advantages, asked the romanian users of google map maker why they contribute,etc. As i posted in my diary, a osm website 2.0 it`s useful. <a href="https://www.openstreetmap.org/user/baditaflorin/diary/16914">https://www.openstreetmap.org/user/baditaflorin/diary/16914</a></p>
</div>
<div id="comment-16083-info" class="comment-info">
<span class="comment-age">(14 Sep '12, 14:05)</span> <span class="comment-user userinfo">Badita Florin</span>
</div>
</div>
</div>
<div id="comment-tools-9673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9673-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36095"></span>

<div id="answer-container-36095" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36095-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On the map page you will have something like this <a href="https://www.openstreetmap.org/#map=9/-38.3266/144.8781">https://www.openstreetmap.org/#map=9/-38.3266/144.8781</a></p>
<p>just edit the latitude and longitude. and the map can jump to the new location.</p>
<p>note negative is used for west and south and positive for north and east. If you wish convert Degrees Minutes and seconds to decimal degrees then you can use this site <a href="http://transition.fcc.gov/mb/audio/bickel/DDDMMSS-decimal.html">http://transition.fcc.gov/mb/audio/bickel/DDDMMSS-decimal.html</a> (note link not working now) minutes are 1/60 of a degree and seconds are 1/60 of a minute.... you'll need to do the maths. So 52 : 25 : 46 would become 52 + 25/60 + 46/3600 decimal degrees for example.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '14, 22:21</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jul '16, 20:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-36095" class="comments-container">
&#10;</div>
<div id="comment-tools-36095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36095-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51173"></span>

<div id="answer-container-51173" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51173-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>another option: just enter some coordinates into the search box (e.g. 52.51834,13.37568 ) and Go/Enter. Then click on the one "Results from Internal" link. It will jump to this location.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '16, 20:37</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-51173" class="comments-container">
<span id="51175"></span>
<div id="comment-51175" class="comment">
<div id="post-51175-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This works 52.51834,13.37568.... but 52 N 13 E did not so format is important. This fails 52.5, -.3 but 52.5, -0.3 is ok</p>
</div>
<div id="comment-51175-info" class="comment-info">
<span class="comment-age">(29 Jul '16, 23:08)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-51173" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51173-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36092"></span>

<div id="answer-container-36092" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36092-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First to thank you for a great resource in OSM, it is much appreciated.</p>
<p>Wakening an old thread but first result from a Google search. Gorn speaks directly to the point when he says "because by not giving them what need we potentially loose many users and later on contributors. I think we should learn from reactions like that."</p>
<p>My scenario that may or may not prove useful to this regard and is more related to user actions. The conversion appears succesful but the interaction beyond this is not expected.</p>
<ol>
<li>using Garmin gps and then Basecamp during my travels I mark waypoints for the specific use of my own maps and updating OSM.</li>
<li>reviewing my gps logs/waypoints I download to Basecamp which gives me the location as such "N41° 13.734' W75° 03.450'"</li>
<li>login to OSM to post a 'closed road' or whatever by searching by that exact coordinate returns with the following url and a red dropoint in the middle of the map, looking at the east coast of the USA.</li>
<li>Zoom is far out so I mouse over and mouse click on the zoom adjustment more and more. The red dropoint disappears every time I mouse over the map to zoom in, so adjust, click on search link, zoom, adjust, zoom, adjust, click on search link, etc.</li>
<li>Finally get to reasonable visible level and this is the result url: <a href="https://www.openstreetmap.org/search?query=N41%C2%B0%2013.734%27%20W75%C2%B0%2003.450%27#map=13/41.2290/-75.0576">https://www.openstreetmap.org/search?query=N41%C2%B0%2013.734%27%20W75%C2%B0%2003.450%27#map=13/41.2290/-75.0576</a></li>
<li>Desired Resolution: keep red dropoint and maintain during click-zoom interaction.</li>
</ol>
<p>May or not be useful, just some points. Thank you for a great resource and all the work that is provided. Marcus</p>
<p>ps - autolist numbering is odd.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '14, 21:41</strong></p>
<img src="https://secure.gravatar.com/avatar/4066be0d674d379d88460be8df5f9ff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="econwatch&#39;s gravatar image" />
<p><span>econwatch</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="econwatch has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36092" class="comments-container">
<span id="51169"></span>
<div id="comment-51169" class="comment">
<div id="post-51169-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's easy to change the lat/lon format in Basecamp to one in decimal degrees. There are numerous tools online such as GeoHack, nearby.org which will convert between various formats and provide links to major map engines (including</p>
</div>
<div id="comment-51169-info" class="comment-info">
<span class="comment-age">(29 Jul '16, 16:31)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="51176"></span>
<div id="comment-51176" class="comment">
<div id="post-51176-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>On many Garmin Gpses lat/lon format as options. so:- Position Format: choose hdddd.dddd and your device will diplay decimal degrees format as used by OSM but note west is represented by negative sign. this may be easier for you.</p>
</div>
<div id="comment-51176-info" class="comment-info">
<span class="comment-age">(30 Jul '16, 07:40)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="51177"></span>
<div id="comment-51177" class="comment">
<div id="post-51177-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Works on Oregon 450, Vista HCX and NUVI 1310</p>
</div>
<div id="comment-51177-info" class="comment-info">
<span class="comment-age">(30 Jul '16, 07:44)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-36092" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36092-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60073"></span>

<div id="answer-container-60073" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60073-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>But what about simply putting a marker on the map, without adding anything to the database? By way of example: I would like to be able to pop up OCM from a QR'd URL (for example: <a href="https://www.opencyclemap.org/?mlat=61.2">https://www.opencyclemap.org/?mlat=61.2</a> … 5&amp;zoom=18) and have an actual marker at that point. I suppose I could add points in the DB for every instance I placed a QR code maker on a trail, but that seems a bit of extra work for nought.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '17, 23:40</strong></p>
<img src="https://secure.gravatar.com/avatar/e4cadcf9f86d306510a1e19319359877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net-buoy&#39;s gravatar image" />
<p><span>net-buoy</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net-buoy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60073" class="comments-container">
<span id="60076"></span>
<div id="comment-60076" class="comment">
<div id="post-60076-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://www.openstreetmap.org/?mlat=53.9027&amp;mlon=-1.2717&amp;layers=C">https://www.openstreetmap.org/?mlat=53.9027&amp;mlon=-1.2717&amp;layers=C</a> ?</p>
</div>
<div id="comment-60076-info" class="comment-info">
<span class="comment-age">(12 Oct '17, 07:04)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="60088"></span>
<div id="comment-60088" class="comment">
<div id="post-60088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, Frederik</p>
<p>It looks like the pointer is provided via the permalink feature (#map), while the (layers=) provides the opencyclemap layer, the zoom can be set by "zoom=" OR it can be set as the first portion of the permalink, appended to the mlon= ( e.g. #map=18/61.20605/-149.78565) Is that all accurate, and if so, is there one part of the wiki that provides the specifics on using URLs to reference OSM?</p>
</div>
<div id="comment-60088-info" class="comment-info">
<span class="comment-age">(12 Oct '17, 17:49)</span> <span class="comment-user userinfo">net-buoy</span>
</div>
</div>
<span id="60089"></span>
<div id="comment-60089" class="comment">
<div id="post-60089-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Probably several :)</p>
<p><a href="https://wiki.openstreetmap.org/wiki/FAQ">https://wiki.openstreetmap.org/wiki/FAQ</a> and <a href="https://wiki.openstreetmap.org/wiki/Browsing">https://wiki.openstreetmap.org/wiki/Browsing</a> among others mention it.</p>
</div>
<div id="comment-60089-info" class="comment-info">
<span class="comment-age">(12 Oct '17, 17:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60090"></span>
<div id="comment-60090" class="comment">
<div id="post-60090-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>AHA! The link on browsing ( <a href="https://wiki.openstreetmap.org/wiki/Browsing">https://wiki.openstreetmap.org/wiki/Browsing</a> ) was just what I needed! The full explanation on the share panel was excellent, and the details on the composition on a URL was comprehensive.</p>
<p>THANKS!</p>
</div>
<div id="comment-60090-info" class="comment-info">
<span class="comment-age">(12 Oct '17, 18:38)</span> <span class="comment-user userinfo">net-buoy</span>
</div>
</div>
</div>
<div id="comment-tools-60073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60073-form-container" class="comment-form-container">
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

