+++
type = "question"
title = "Download all countries with regions and cities"
description = '''Hello,  I would like to know, what is the best way to download all countries from around the world. Each country should have related regions and regions should have cities (cities with latitude and longitude). It seems to be impossible to do it using overpass turbo (too much data). Thanks for your a...'''
date = "2020-03-06T09:43:00Z"
lastmod = "2020-03-11T21:51:00Z"
weight = 73419
keywords = [ "country", "region" ]
aliases = [ "/questions/73419" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Download all countries with regions and cities](/questions/73419/download-all-countries-with-regions-and-cities)

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
<span id="post-73419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73419-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I would like to know, what is the best way to download all countries from around the world. Each country should have related regions and regions should have cities (cities with latitude and longitude). It seems to be impossible to do it using overpass turbo (too much data). Thanks for your answers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-region" rel="tag" title="see questions tagged &#39;region&#39;">region</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '20, 09:43</strong></p>
<img src="https://secure.gravatar.com/avatar/ac3861e87bbff3bbd8b1c2add0d9f96c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="avenh2&#39;s gravatar image" />
<p><span>avenh2</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="avenh2 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73419" class="comments-container">
<span id="73436"></span>
<div id="comment-73436" class="comment">
<div id="post-73436-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you just want country boundaries and cities, or do you want more map data? Not all countries structure their internal divisions the same way.</p>
</div>
<div id="comment-73436-info" class="comment-info">
<span class="comment-age">(07 Mar '20, 13:29)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="73441"></span>
<div id="comment-73441" class="comment">
<div id="post-73441-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I need country, region, city names. Cities should have gps coordinates.</p>
</div>
<div id="comment-73441-info" class="comment-info">
<span class="comment-age">(09 Mar '20, 05:56)</span> <span class="comment-user userinfo">avenh2</span>
</div>
</div>
</div>
<div id="comment-tools-73419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73419-form-container" class="comment-form-container">
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

<span id="73484"></span>

<div id="answer-container-73484" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73484-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For countries and regions, the best source I know of is <a href="https://wambachers-osm.website/boundaries/.">https://wambachers-osm.website/boundaries/.</a> It’s a third party service (run by a volunteer) which offers preprocessed administrative boundaries per country and their subdivisions.</p>
<p>For cities one source is the <a href="http://download.geofabrik.de/">Geofabrik Download service</a>. For each country/region it offers a zip file with preprocessed layers in ESRI Shape format – look for the <code>.shp.zip</code> downloads. Inside you will find files <code>gis_osm_places_free_1.*</code> which contain points with <a href="https://wiki.openstreetmap.org/wiki/Key:place">“places”</a>. These can be everything from cities, suburbs, towns, down to villages, hamlets and farms. So depending on your definition of “city” you may want to filter them.</p>
<p>If you combine these two sources, cities will not be directly connected to countries, but you should be able to link them by performing a point-in-polygon test.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '20, 21:51</strong></p>
<img src="https://secure.gravatar.com/avatar/97f754e0356a74acc666550948b48bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hfs&#39;s gravatar image" />
<p><span>hfs</span><br />
<span class="score" title="851 reputation points">851</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hfs has 3 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-73484" class="comments-container">
&#10;</div>
<div id="comment-tools-73484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73484-form-container" class="comment-form-container">
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

