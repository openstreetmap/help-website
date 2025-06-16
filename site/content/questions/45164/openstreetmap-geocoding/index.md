+++
type = "question"
title = "openstreetmap geocoding"
description = '''we created a application which is collecting latitude and longitude locations from gps devices(100). People will be able to see this through a webpage, I&#x27;m intending to use OpenStreetMap api to display the pin points. However if a user will register multiple devices which he want&#x27;s to view on the ma...'''
date = "2015-09-10T12:32:00Z"
lastmod = "2015-09-10T14:47:00Z"
weight = 45164
keywords = [ "geocoding" ]
aliases = [ "/questions/45164" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [openstreetmap geocoding](/questions/45164/openstreetmap-geocoding)

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
<span id="post-45164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45164-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>we created a application which is collecting latitude and longitude locations from gps devices(100). People will be able to see this through a webpage, I'm intending to use OpenStreetMap api to display the pin points. However if a user will register multiple devices which he want's to view on the map he will have to pay for the usage. Now to be very clear, I'm not intending to modify any map data, I'm only storing latitude and longitude in my database and addresses, and I'm displaying it on the OpenStreetMap through the API.presently we are using google api but there is some limitations(they provide only 2500 requests/day). Can I use OpenStreetMap in this case or do I need a separate license, or I cannot include it in my product if I'm charging money to display data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '15, 12:32</strong></p>
<img src="https://secure.gravatar.com/avatar/80d17e532e63ace99e22d60b3d9e62cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RajkumarP&#39;s gravatar image" />
<p><span>RajkumarP</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RajkumarP has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Sep '15, 12:33</strong> </span></p>
</div>
</div>
<div id="comments-container-45164" class="comments-container">
&#10;</div>
<div id="comment-tools-45164" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45164-form-container" class="comment-form-container">
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

<span id="45166"></span>

<div id="answer-container-45166" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45166-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-45166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unlike Google Maps (at least their free version) you can use OpenStreetMap data behind firewalls, in private projects and charge your users/customers money for usage. We ask for attribution, e.g. the text/link "© OpenStreetMap contributors" either on the map or other part of the page. See <a href="https://www.openstreetmap.org/copyright">https://www.openstreetmap.org/copyright</a></p>
<p>OpenStreetMaps' geocoding API has usage limits as well: <a href="https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy">https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy</a> With dozens of GPS devices sending data every minute you can easily reach the limits of 1 request/sec. The page also lists third-party alternatives. They cost money but you'll see they're much cheaper that Google Maps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Sep '15, 13:40</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-45166" class="comments-container">
<span id="45167"></span>
<div id="comment-45167" class="comment">
<div id="post-45167-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Another way is the local installation of a <a href="https://wiki.openstreetmap.org/wiki/Search_engines">geocoding service</a> such as <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">Nominatim</a> possibly combined with the local installation of a <a href="http://switch2osm.org/serving-tiles/">tile server</a>.</p>
</div>
<div id="comment-45167-info" class="comment-info">
<span class="comment-age">(10 Sep '15, 13:48)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45168"></span>
<div id="comment-45168" class="comment">
<div id="post-45168-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>OpenStreetMap is not offering services for commercial use. So you cannot buy a license to get access to more resources. There are a number of providers that have a geocoding service based upon OpenStreetMap data, or you can setup your own server as scai mentioned.</p>
</div>
<div id="comment-45168-info" class="comment-info">
<span class="comment-age">(10 Sep '15, 14:47)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-45166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45166-form-container" class="comment-form-container">
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

