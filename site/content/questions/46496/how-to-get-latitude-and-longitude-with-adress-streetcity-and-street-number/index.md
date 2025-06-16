+++
type = "question"
title = "how to get latitude and longitude with adress street,city and street number"
description = '''hello i am new to issues of maps and I doubt I could import a map to Postgres with PostGIS and I would like to query the database to give me the latitude and longitude having the address and numbering their respective city'''
date = "2015-11-10T15:56:00Z"
lastmod = "2015-11-13T22:47:00Z"
weight = 46496
keywords = [ "latitude", "city", "street", "postgresql", "longitude" ]
aliases = [ "/questions/46496" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to get latitude and longitude with adress street,city and street number](/questions/46496/how-to-get-latitude-and-longitude-with-adress-streetcity-and-street-number)

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
<span id="post-46496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46496-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello i am new to issues of maps and I doubt I could import a map to Postgres with PostGIS and I would like to query the database to give me the latitude and longitude having the address and numbering their respective city</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '15, 15:56</strong></p>
<img src="https://secure.gravatar.com/avatar/b778b8327dcf016ac62981bc2bd7719a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malg001&#39;s gravatar image" />
<p><span>malg001</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malg001 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46496" class="comments-container">
&#10;</div>
<div id="comment-tools-46496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46496-form-container" class="comment-form-container">
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

<span id="46504"></span>

<div id="answer-container-46504" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46504-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems that you are looking for an OSM based geocoder engine, so you enter an address with street and city, and you want to have target coordinates, right?</p>
<p>See the OSM wiki about <a href="https://wiki.openstreetmap.org/wiki/Search_engines">Search Engines</a> to get a list of all OSM based or related services.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '15, 17:37</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-46504" class="comments-container">
<span id="46507"></span>
<div id="comment-46507" class="comment">
<div id="post-46507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, that's what I need and these search engines can connect to local mode using a map, and imported Geofabrik Postgres?</p>
</div>
<div id="comment-46507-info" class="comment-info">
<span class="comment-age">(10 Nov '15, 17:40)</span> <span class="comment-user userinfo">malg001</span>
</div>
</div>
<span id="46577"></span>
<div id="comment-46577" class="comment">
<div id="post-46577-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your question does not make sense. If you want to install a local search engine, you need to install one of the software packages listed on the wiki page, and you can then use any OSM data file, from Geofabrik or elsewhere, to load data into your geocoder. However, if you have already imported data into PostgreSQL, that will not help you; every search engine uses their own data format and you have to follow the import procedure for the search engine that you choose.</p>
</div>
<div id="comment-46577-info" class="comment-info">
<span class="comment-age">(13 Nov '15, 22:47)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46504-form-container" class="comment-form-container">
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

