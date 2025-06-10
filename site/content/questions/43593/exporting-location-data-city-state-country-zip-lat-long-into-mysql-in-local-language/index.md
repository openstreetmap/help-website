+++
type = "question"
title = "Exporting location data (city, state, country, zip, lat, long) into mysql in local language"
description = '''Hi Guys, I have been trying to use http://download.geonames.org/export/dump/ to get a data set where I can extract   City  County State Region Country Latitude Longitude Postal code/zip code  The requirement is to be able to lookup places by zip code/postal code or by place name. Now the place name ...'''
date = "2015-06-17T02:06:00Z"
lastmod = "2015-06-17T17:23:00Z"
weight = 43593
keywords = [ "localization", "export", "location", "language", "mysql" ]
aliases = [ "/questions/43593" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting location data (city, state, country, zip, lat, long) into mysql in local language](/questions/43593/exporting-location-data-city-state-country-zip-lat-long-into-mysql-in-local-language)

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
<span id="post-43593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43593-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Guys,</p>
<p>I have been trying to use <a href="http://download.geonames.org/export/dump/">http://download.geonames.org/export/dump/</a> to get a data set where I can extract</p>
<ul>
<li>City</li>
<li>County</li>
<li>State</li>
<li>Region</li>
<li>Country</li>
<li>Latitude</li>
<li>Longitude</li>
<li>Postal code/zip code</li>
</ul>
<p>The requirement is to be able to lookup places by zip code/postal code or by place name. Now the place name etc needs to be available in english as well as local language.</p>
<p>e.x for Taipei, capital or Taiwan where the main language is Chinese, we want:</p>
<ul>
<li>Place name (English): Taipei</li>
<li>Place name (Chinese): 台北市</li>
<li>All other information as above</li>
</ul>
<p>Is this possible to get this info from <a href="http://planet.openstreetmap.org/">http://planet.openstreetmap.org/</a>?</p>
<p>I just downloaded a sample data xml for a region and I can see that it has lot of information. I did find a wiki for a script to import data to mysql - <a href="http://forum.openstreetmap.org/viewtopic.php?pid=152695">http://forum.openstreetmap.org/viewtopic.php?pid=152695</a> but I don't think I can use it as it is because the data I want is not per geo boundary but more like per city/state/country. So can anyone guide me how I can use this data for my usage? I don't want to run a script to export the data per geolocation or by specifying certain area.</p>
<p>Thanks a ton!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-localization" rel="tag" title="see questions tagged &#39;localization&#39;">localization</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '15, 02:06</strong></p>
<img src="https://secure.gravatar.com/avatar/2e571ab1226e822cbced32144d3b456d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sumitk&#39;s gravatar image" />
<p><span>sumitk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sumitk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jun '15, 02:09</strong> </span></p>
</div>
</div>
<div id="comments-container-43593" class="comments-container">
&#10;</div>
<div id="comment-tools-43593" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43593-form-container" class="comment-form-container">
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

<span id="43600"></span>

<div id="answer-container-43600" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43600-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your aim should be possible, but I fear there is no ready made how to.</p>
<p>At least two keywords can be used for a search ion this FAQ site, namely "export" and "CSV".</p>
<p>There have been already some questions similar to yours here, but it can be some work to transfer other howtos to your aim.</p>
<p>You should make three steps:</p>
<p>1) find the OSM elements in general that contain your special needed information. 2) Filter those elements for your needs, via overpass-api, osmosis or osmfilter. 3) find a good export format and a way to import the result in your database schema.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '15, 17:23</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-43600" class="comments-container">
&#10;</div>
<div id="comment-tools-43600" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43600-form-container" class="comment-form-container">
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

