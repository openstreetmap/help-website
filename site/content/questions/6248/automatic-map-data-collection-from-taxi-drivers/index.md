+++
type = "question"
title = "Automatic map data collection from taxi drivers"
description = '''I am looking for a good way to contribute map data to this project. I have created taxi dispatch system which is using GPS. For now we are using our Polish map provider but would like to switch to Open Street Map. One problem is that there are missing roads and addresses. In each city, where system ...'''
date = "2011-07-09T15:47:00Z"
lastmod = "2011-07-13T20:13:00Z"
weight = 6248
keywords = [ "housenumbers", "poland", "automated" ]
aliases = [ "/questions/6248" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Automatic map data collection from taxi drivers](/questions/6248/automatic-map-data-collection-from-taxi-drivers)

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
<span id="post-6248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6248-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-6248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking for a good way to contribute map data to this project. I have created taxi dispatch system which is using GPS. For now we are using our Polish map provider but would like to switch to Open Street Map. One problem is that there are missing roads and addresses. In each city, where system is working, we have in our disposal &gt;100 taxi drivers working. The question is how to modify our system so we can automatically contribute our drivers GPS traces to Open Street Map. Also we would like to create a way for a drivers terminal to aid adding address information. All collected data will be provided for Open Street Map to be integrated and we will use this integrated data for taxi dispatch.</p>
<p>We are also looking for people willing to help in setting up Open Street Map on our own servers.</p>
<p>Thank You, for every suggestion.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-poland" rel="tag" title="see questions tagged &#39;poland&#39;">poland</span> <span class="post-tag tag-link-automated" rel="tag" title="see questions tagged &#39;automated&#39;">automated</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '11, 15:47</strong></p>
<img src="https://secure.gravatar.com/avatar/afe9bae366b74d4a90c94a746dbedb2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbapl&#39;s gravatar image" />
<p><span>dbapl</span><br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbapl has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jul '11, 16:39</strong> </span></p>
</div>
</div>
<div id="comments-container-6248" class="comments-container">
<span id="6304"></span>
<div id="comment-6304" class="comment">
<div id="post-6304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for answers. I will ask about it on mailing lists.</p>
</div>
<div id="comment-6304-info" class="comment-info">
<span class="comment-age">(13 Jul '11, 20:13)</span> <span class="comment-user userinfo">dbapl</span>
</div>
</div>
</div>
<div id="comment-tools-6248" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6248-form-container" class="comment-form-container">
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

<span id="6263"></span>

<div id="answer-container-6263" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6263-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dbapl has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For GPS traces to roads, this does indeed require some manual effort... however, once the road network is basically in place, and you're just needing to add tags, correct names, or mark the location of a previously unmarked address, business, etc., this is somewhat easier to design an editing interface for.</p>
<p>There's an existing application working, and under further development for mobile phones (in Java) that would have quite a bit of overlap with the kind of thing you're wanting to do... look up "GpsMid", and the "editing" version of this in particular (I've used it for a kind-of small scale version of what you're thinking of - going along a street and marking the name and any additional details of the building I'm just outside). Again, this is likely to need at least a little "intelligent" post-processing to reposition the POI, house number, etc. closer to where the building is - or good software and a high quality GPS receiver.</p>
<p>I'd suggest it could be worth getting "stuck in" a bit, doing it "the hard way" with a small group of keen taxi drivers or other mappers, to get a feel for how the systems work generally, so you'd better understand the requirements for the form that the data needs to be in for designing your full interface.</p>
<p>Also worth asking on the mailing lists or forums, etc. as this Q&amp;A site is really more for questions that have a single "straight" answer, and primarily for being answered by other "normal mappers"...</p>
<p>You can get the basic details of the requirements for the API for retrieving and submitting map data at <a href="https://wiki.openstreetmap.org/wiki/API_v0.6">https://wiki.openstreetmap.org/wiki/API_v0.6</a> but again, experience of actually entering data would be invaluable before considering a partially automated data entry system such as you propose... and discussing on one of the appropriate mailing lists would help to keep up to speed with changes to the API and/or standard practice for handling it.</p>
<p>I'd imagine that if the systems can be worked out right, a mechanism to have taxi drivers effectively double-check and be able to correct every address every time they pick up or drop off a passenger would be a great boost - particularly if this starts to be in a form where it can be adopted by other taxi companies across the planet..... :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '11, 01:30</strong></p>
<img src="https://secure.gravatar.com/avatar/b95e1b5cb818be577b5561688a50368c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="banoffee&#39;s gravatar image" />
<p><span>banoffee</span><br />
<span class="score" title="884 reputation points">884</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="banoffee has 3 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-6263" class="comments-container">
&#10;</div>
<div id="comment-tools-6263" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6263-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6250"></span>

<div id="answer-container-6250" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6250-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-6250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a few things you can do.</p>
<h2 id="uploading-gpx-tracks">Uploading GPX Tracks</h2>
<p>First, if the GPS units in your cars can log, you can contribute those logs to OSM via the GPX track uploads. This can be useful for roads which may not be off in OSM, or inaccurate.</p>
<p>You'll need to collect the GPSes and upload the tracks, but that won't take long.</p>
<h2 id="adding-collected-data-into-osm">Adding Collected Data into OSM</h2>
<p>That's really all you can do "automatically". But what you can do is once you have the GPX tracks, you can <a href="https://wiki.openstreetmap.org/wiki/Upload">upload them</a> and compare them to OSM and see what streets are missing. You can then add the streets You can then ask a driver for the names of the streets which you're adding. If there's <a href="https://wiki.openstreetmap.org/wiki/Aerial_imagery">imagery</a> for your area (and I'd expect some with Bing), you can combine your data with the imagery and trace the roads.</p>
<p>Of course the GPX tracks won't give you the names, and neither will the imagery. That, you'll have to figure out yourself. But if the map is somewhat complete, once you've added your GPX tracks, you may find that information is easy to figure out. And then it may be only one day to figure out what to fix.</p>
<h2 id="walking-papers">Walking Papers</h2>
<p>If your drivers are willing to help, but maybe not so technical, you could hand them <a href="http://walking-papers.org/">walking papers</a> and ask them to use a pen to write out the names of the streets that don't have names. You can then scan them in and people (or you, preferably) can add the information to the map.</p>
<h2 id="addresses">Addresses</h2>
<p>Addresses are a bit trickier. In some places the addresses are relatively uniform...</p>
<p>12... 14... 16... 18 on one side, and then</p>
<p>... 13... 15... 17... 19... on the other</p>
<p>And in that case, you can use <a href="https://wiki.openstreetmap.org/wiki/Key:addr#Using_interpolation">address interpolation</a>, where you can mark off some of the addresses, and then the rest are figured out automatically. It's not perfect, of course. But it works. You can do this by marking a few houses (eg at the end of a block) or important buildings. You could ask the drivers using Walking Papers to do this, or put the waypoints in the GPS."</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '11, 16:42</strong></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emacsen has 4 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-6250" class="comments-container">
<span id="6261"></span>
<div id="comment-6261" class="comment">
<div id="post-6261-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So we should convert traces to map data ourself or find someone willing to do this? There is no other way? That is not encouraging :(</p>
<p>In Poland address interpolation will not work, very very rarely buildings are evenly spaced and in right order. I am thinking about something like this to collect address data: - driver is send to specific address for client - when he/she is on the right spot (on the road/parking near client address) and confirms client is in the taxi we mark GPS coordinates to point to that address</p>
<p>Will data generated like that be interesting to Open Street Map?</p>
</div>
<div id="comment-6261-info" class="comment-info">
<span class="comment-age">(09 Jul '11, 23:56)</span> <span class="comment-user userinfo">dbapl</span>
</div>
</div>
<span id="6262"></span>
<div id="comment-6262" class="comment">
<div id="post-6262-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>My answer doesn't fit in this little box. The help forum is for very general, generic questions. I suggest you join one of the mailing lists at <a href="http://lists.openstreetmap.org/listinfo">http://lists.openstreetmap.org/listinfo</a> and ask your question there, where you can work more easily with the community.</p>
</div>
<div id="comment-6262-info" class="comment-info">
<span class="comment-age">(10 Jul '11, 00:07)</span> <span class="comment-user userinfo">emacsen</span>
</div>
</div>
<span id="6288"></span>
<div id="comment-6288" class="comment">
<div id="post-6288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Bonus points for having GPX waypoints containing useful details uploaded as part of that. IIRC, GPX waypoints are left in tact when uploaded to OSM.</p>
</div>
<div id="comment-6288-info" class="comment-info">
<span class="comment-age">(12 Jul '11, 16:21)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-6250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6250-form-container" class="comment-form-container">
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

