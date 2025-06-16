+++
type = "question"
title = "How to get street name from a waypoint id?"
description = '''I am new to OSM. I have a result of a map-matching algorithm on some trajectory data (GPX) and the returned results are defined as (waypoint id, start node, end node) I want to retrieve the name of the street from the waypoint id? How to do so? For example in Nominatim service the response is in the...'''
date = "2015-02-04T15:01:00Z"
lastmod = "2015-02-05T12:13:00Z"
weight = 40777
keywords = [ "xml", "waypoints", "way", "webservice" ]
aliases = [ "/questions/40777" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get street name from a waypoint id?](/questions/40777/how-to-get-street-name-from-a-waypoint-id)

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
<span id="post-40777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40777-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to OSM. I have a result of a map-matching algorithm on some trajectory data (GPX) and the returned results are defined as (waypoint id, start node, end node)</p>
<p>I want to retrieve the name of the street from the waypoint id? How to do so?</p>
<p>For example in Nominatim service the response is in the XML form. But I cannot find a suitable service for getting real names from ids in OSM. I found this:</p>
<p><a href="https://www.openstreetmap.org/way/256328760">https://www.openstreetmap.org/way/256328760</a></p>
<p>This page returns the map of way point. But I want the <strong>ref</strong> name <strong>St 2572</strong></p>
<p>And as another question How to get All this data (the data for a city) for educational and research purposes?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-webservice" rel="tag" title="see questions tagged &#39;webservice&#39;">webservice</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '15, 15:01</strong></p>
<img src="https://secure.gravatar.com/avatar/4b0ad1bb1e78f7b6a84f02f97b22505b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alamdari&#39;s gravatar image" />
<p><span>Alamdari</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alamdari has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Feb '15, 15:09</strong> </span></p>
</div>
</div>
<div id="comments-container-40777" class="comments-container">
&#10;</div>
<div id="comment-tools-40777" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40777-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="40780"></span>

<div id="answer-container-40780" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40780-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alamdari has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>use <span>an OSM API</span> to query this way's data. Do not use the main – editing – API, it is okay for very small tests though. <span>Example URL</span> for the editing API. <a href="http://overpass.osm.rambler.ru/cgi/interpreter?data=way(256328760);out;">Example URL</a> for the Overpass API. Now just process the XML as usual to get your desired tag. With Overpass API you also could get other output formats if you do not want XML.</p>
<p>For your "data for a city" question: you can use the Overpass API for quite many requests, see its wiki article. Or do you want to download the raw OSM data for a whole city? Please search our question collection for older questions about getting data extracts and ask a new one if you cannot find anything.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '15, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Feb '15, 16:15</strong> </span></p>
</div>
</div>
<div id="comments-container-40780" class="comments-container">
<span id="40782"></span>
<div id="comment-40782" class="comment">
<div id="post-40782-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you! The OSM API is what I need. Thanks a lot!</p>
</div>
<div id="comment-40782-info" class="comment-info">
<span class="comment-age">(04 Feb '15, 17:10)</span> <span class="comment-user userinfo">Alamdari</span>
</div>
</div>
<span id="40796"></span>
<div id="comment-40796" class="comment">
<div id="post-40796-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As said, you shouldn't use the API for thousands single id requests. Instead, you should download the area into your local disk, either with an editor like JoSM (and the 'save as') or using some planet file extracts (check the wiki to find web sites offering extracts at country or even major city levels). Once you have the data locally, you can find your ref's by different means (manually or by scripts).</p>
</div>
<div id="comment-40796-info" class="comment-info">
<span class="comment-age">(05 Feb '15, 11:21)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="40798"></span>
<div id="comment-40798" class="comment">
<div id="post-40798-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/87/pieren">@Pieren</a>: while getting a data extract could still be the best/most fast solution it is okay to query Overpass API with those requests, if I understand <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Introduction">its</a> service description correctly. Maybe Alamdari even means Overpass API, because I have coined my link "an OSM API" which also lists Overpass.</p>
</div>
<div id="comment-40798-info" class="comment-info">
<span class="comment-age">(05 Feb '15, 12:13)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40780" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40780-form-container" class="comment-form-container">
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

