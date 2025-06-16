+++
type = "question"
title = "Export only roads?"
description = '''Hi everyone, When I export the .osm data, I&#x27;d like it to give me only roads that cars can actually drive on if possible? At the moment it&#x27;s giving me buildings, walking paths in the middle of parks and all sorts. Is there a quick fix for this? Not all nodes have tags which state whether they are hig...'''
date = "2014-02-12T22:58:00Z"
lastmod = "2021-09-01T18:32:00Z"
weight = 30692
keywords = [ "roads", "export", "road" ]
aliases = [ "/questions/30692" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [Export only roads?](/questions/30692/export-only-roads)

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
<span id="post-30692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30692-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>When I export the .osm data, I'd like it to give me only roads that cars can actually drive on if possible? At the moment it's giving me buildings, walking paths in the middle of parks and all sorts.</p>
<p>Is there a quick fix for this? Not all nodes have tags which state whether they are highways so actually going through them one by one would be painful...</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '14, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/56d5ec9b3e908fa8e2b33e604f334284?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kyanite&#39;s gravatar image" />
<p><span>Kyanite</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kyanite has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30692" class="comments-container">
<span id="30693"></span>
<div id="comment-30693" class="comment">
<div id="post-30693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Update: I have discovered OSMFilter, however am unsure how to filter just roads and remove everything else!</p>
<p>--keep="highway=" I'm assuming I will need this, however how can I drop all other non-vehicle roads?</p>
</div>
<div id="comment-30693-info" class="comment-info">
<span class="comment-age">(12 Feb '14, 23:24)</span> <span class="comment-user userinfo">Kyanite</span>
</div>
</div>
<span id="30695"></span>
<div id="comment-30695" class="comment">
<div id="post-30695-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please ask a new question about osmfilter (if you cannot find it in the previous questions). however, I think it should be clear on the wiki page: you need to filter for tags (not only keys). Note: I did not use this tool on my own.</p>
</div>
<div id="comment-30695-info" class="comment-info">
<span class="comment-age">(12 Feb '14, 23:31)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="30696"></span>
<div id="comment-30696" class="comment">
<div id="post-30696-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>One thing to think about - what do you consider a road that cars can drive on? A "highway=footway" obviously isn't, and a "highway=primary" obviously is, but what about "highway=track"? Also you may want to think about "access" tags.</p>
</div>
<div id="comment-30696-info" class="comment-info">
<span class="comment-age">(12 Feb '14, 23:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30692-form-container" class="comment-form-container">
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

<span id="30723"></span>

<div id="answer-container-30723" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30723-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kyanite has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To know which highway tags are important for cars, have a look at these wiki pages:<br />
<a href="https://wiki.openstreetmap.org/wiki/Highway">https://wiki.openstreetmap.org/wiki/Highway</a><br />
<a href="https://wiki.openstreetmap.org/wiki/Key:access">https://wiki.openstreetmap.org/wiki/Key:access</a></p>
<p>As a start point, you should select ways (and only ways, not nodes) with:<br />
- highway=motorway or highway=motorway_link<br />
- highway=trunk or highway=trunk_link<br />
- highway=primary or highway=primary_link<br />
- highway=secondary or highway=secondary_link<br />
- highway=tertiary or highway=tertiary_link<br />
- highway=unclassified or highway=unclassified_link<br />
- highway=residential or highway=residential_link<br />
- highway=service or highway=service_link<br />
- highway=living_street<br />
- highway=track (possibly combined with a <a href="https://wiki.openstreetmap.org/wiki/Key:tracktype">graduation</a> tag)<br />
- highway=path (only if combined with "motor_vehicle=yes" or "motorcar=yes")<br />
- highway=road (might be ignored since the highway class is unknown and might be impassable for cars)<br />
</p>
<p>The tag "access" is important (the legal status). Absence of access tags means "allowed". Otherwise, look if "motor_vehicle=yes|no" or "motorcar=yes|no" is present. Otherwise, look for a general access definition like "access=yes|permissive" for "allowed" or "access=private|delivery|emergency|forestry|no" for "disallowed".</p>
<p>If you care about direction, check the tag <a href="https://wiki.openstreetmap.org/wiki/Oneway">oneway=yes|-1|no</a> or <a href="https://wiki.openstreetmap.org/wiki/Tag:junction%3Droundabout">junction=roundabout</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '14, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
</div>
<div id="comments-container-30723" class="comments-container">
<span id="30727"></span>
<div id="comment-30727" class="comment">
<div id="post-30727-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'd add one caveat to that, where it says 'Absence of access tags means "allowed"':<br />
</p>
<p>The meaning of the absense of an access tag is very dependant on context. If it's in an area in which it's clear that all of the access rights have clearly been surveyed by people on the ground, then it might well mean that.<br />
</p>
<p>However, if it's a rural area where data has come from aerial imagery, it actually means "not yet known". For example in England I wouldn't assume that I had legal motor vehicle access to a highway=track unless it had an approriate access tag.</p>
</div>
<div id="comment-30727-info" class="comment-info">
<span class="comment-age">(13 Feb '14, 13:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30728"></span>
<div id="comment-30728" class="comment">
<div id="post-30728-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There are also <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">implicit default access values</a> which <em>should</em> be used whenever there are no access tags present.</p>
<p>But as already explained by SomeoneElse a missing access tag doesn't always mean that the default access restrictions apply. It could also indicate that nobody has checked the legal access status yet.</p>
</div>
<div id="comment-30728-info" class="comment-info">
<span class="comment-age">(13 Feb '14, 14:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="30729"></span>
<div id="comment-30729" class="comment">
<div id="post-30729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Even with surveyed roads, nobody is adding an explicite "access=yes" tag to all created highways. Probably because the access tag reflects a road sign most of the time. And in absence of road signs, "what is not forbidden is allowed".</p>
</div>
<div id="comment-30729-info" class="comment-info">
<span class="comment-age">(13 Feb '14, 14:26)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="30730"></span>
<div id="comment-30730" class="comment">
<div id="post-30730-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"what is not forbidden is allowed". In some countries perhaps; most certainly not in others. :)</p>
<p>The point about implicit access rules saying things like "you are allowed to drive on a highway=primary" is well made; no-one is suggesting tagging them all with "motorcar=yes".</p>
<p>However, the point that I was trying to make was that anyone extracting highway data from OSM has to think about how it got there, and how much information is missing (because it's just never been surveyed) from what they've extracted.</p>
</div>
<div id="comment-30730-info" class="comment-info">
<span class="comment-age">(13 Feb '14, 14:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30731"></span>
<div id="comment-30731" class="comment">
<div id="post-30731-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is true but not only for access tags, for all attributs in OSM in general.</p>
</div>
<div id="comment-30731-info" class="comment-info">
<span class="comment-age">(13 Feb '14, 15:48)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="60299"></span>
<div id="comment-60299" class="comment not_top_scorer">
<div id="post-60299-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/87/pieren">@Pieren</a> Could you direct me to the syntax...i understand the logic but am struggling with proper syntax</p>
</div>
<div id="comment-60299-info" class="comment-info">
<span class="comment-age">(25 Oct '17, 13:27)</span> <span class="comment-user userinfo">amishra</span>
</div>
</div>
</div>
<div id="comment-tools-30723" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-30723-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30732"></span>

<div id="answer-container-30732" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30732-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-30732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>An easy way to get predefined data is the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> with its user friendly tool <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">Overpass Turbo</a>.<br />
I created a query for all highways except footway, path and pedestrian which you can find (and enhance) here: <a href="http://overpass-turbo.eu/s/2vM">http://overpass-turbo.eu/s/2vM</a></p>
<p>hth<br />
malenki</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '14, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span> </br></br></p>
</div>
</div>
<div id="comments-container-30732" class="comments-container">
<span id="30733"></span>
<div id="comment-30733" class="comment">
<div id="post-30733-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You forgot to exclude <em>highway=steps</em> :) And depending on the use-case one could exclude <em>highway=construction</em>, too. And nodes which have a highway tag but aren't part of a way with a highway tag, such as <em>highway=bus_stop</em>.</p>
</div>
<div id="comment-30733-info" class="comment-info">
<span class="comment-age">(13 Feb '14, 18:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="30734"></span>
<div id="comment-30734" class="comment">
<div id="post-30734-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes - thanks for the addition</p>
</div>
<div id="comment-30734-info" class="comment-info">
<span class="comment-age">(13 Feb '14, 18:45)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
</div>
<div id="comment-tools-30732" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30732-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30697"></span>

<div id="answer-container-30697" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30697-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't say what program you're feeding the OSM data into. Usually, any such filtering would be done by this "client" program. For example, if you were using a renderer such as Mapnik, you would write a stylesheet that only uses the highway= tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '14, 00:58</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span> </br></br></p>
</div>
</div>
<div id="comments-container-30697" class="comments-container">
&#10;</div>
<div id="comment-tools-30697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30697-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30694"></span>

<div id="answer-container-30694" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30694-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30694-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30694-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess using <span>osmfilter</span> (read the section about Object Filter) afterwards is a good option as I do not know of the osm.org export being able to filter server-side. However, thirdparty services may help too (e.g. <span>overpass turbo</span> could be an option). It depends on your usecase what is best.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '14, 23:28</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '14, 23:29</strong> </span></p>
</div>
</div>
<div id="comments-container-30694" class="comments-container">
&#10;</div>
<div id="comment-tools-30694" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30694-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81601"></span>

<div id="answer-container-81601" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81601-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems like a lot of work has gone into the Car routing profile for OSRM. It would be great if there was a way to use this as the input and get the corresponding roads that it considers drivable. <a href="https://github.com/Project-OSRM/osrm-backend/blob/master/profiles/car.lua">https://github.com/Project-OSRM/osrm-backend/blob/master/profiles/car.lua</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '21, 18:32</strong></p>
<img src="https://secure.gravatar.com/avatar/dd47cffcb48e7b856f7b14a777e552e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrowe&#39;s gravatar image" />
<p><span>chrowe</span><br />
<span class="score" title="-1 reputation points">-1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrowe has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-81601" class="comments-container">
&#10;</div>
<div id="comment-tools-81601" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81601-form-container" class="comment-form-container">
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

