+++
type = "question"
title = "Updating OSM database with Government Data Sets"
description = '''The South Australian Government provides datasets for Open Street Map The datasets are located at https://data.sa.gov.au/data/dataset/roads Is there anyway to import this data for Geocoding purposes into my nominatim/tile servers? When I am searching addresses it only shows the street in the search ...'''
date = "2018-04-24T15:33:00Z"
lastmod = "2018-04-25T01:53:00Z"
weight = 63105
keywords = [ "openstreetmap", "australia", "nominatim", "dataset" ]
aliases = [ "/questions/63105" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Updating OSM database with Government Data Sets](/questions/63105/updating-osm-database-with-government-data-sets)

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
<span id="post-63105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63105-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The South Australian Government provides datasets for Open Street Map</p>
<p>The datasets are located at <a href="https://data.sa.gov.au/data/dataset/roads">https://data.sa.gov.au/data/dataset/roads</a></p>
<p>Is there anyway to import this data for Geocoding purposes into my nominatim/tile servers?</p>
<p>When I am searching addresses it only shows the street in the search box and not the number</p>
<p>However, when I go to <a href="http://location.sa.gov.au/viewer/?map=hybrid&amp;x=138.68544&amp;y=-34.94746&amp;z=13&amp;uids=136">http://location.sa.gov.au/viewer/?map=hybrid&amp;x=138.68544&amp;y=-34.94746&amp;z=13&amp;uids=136</a> I am able to search via the full street name</p>
<p>An example would be, currently when I search for "2 Fernilee Avenue, Tea Tree Gully" it only shows "Fernilee Avenue, Tea Tree Gully". It is missing the street number.</p>
<p>But when I search on the above link it works perfectly</p>
<p>To put it in short, can any of the data files offered <a href="https://data.sa.gov.au/data/dataset/roads">https://data.sa.gov.au/data/dataset/roads</a> be added into OSM system in order to provide more complete address searches</p>
<p>Best Regards</p>
<p>Reza</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-australia" rel="tag" title="see questions tagged &#39;australia&#39;">australia</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-dataset" rel="tag" title="see questions tagged &#39;dataset&#39;">dataset</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '18, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/ca009706fa6df2b33eb931f781ff57f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khamooshi&#39;s gravatar image" />
<p><span>khamooshi</span><br />
<span class="score" title="146 reputation points">146</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khamooshi has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-63105" class="comments-container">
&#10;</div>
<div id="comment-tools-63105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63105-form-container" class="comment-form-container">
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

<span id="63116"></span>

<div id="answer-container-63116" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63116-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you need more complete address coverage than what's in OSM at the moment and you're running your own nominatim/tile servers, you could use <a href="https://www.data.gov.au/dataset/geocoded-national-address-file-g-naf">GNAF</a> via <a href="http://results.openaddresses.io/sources/au/countrywide">OpenAddresses</a> (<a href="http://results.openaddresses.io/sources/au/countrywide">http://results.openaddresses.io/sources/au/countrywide</a>) which can be transformed with <a href="https://github.com/andrewharvey/oa2osm">oa2osm</a> into an OSM XML file for easier ingestion into the OSM tool pipeline.</p>
<p>Although OpenStreetMap has many addresses mapped, in Australia it's not that complete yet.</p>
<p>Although the South Australian government has <a href="https://wiki.openstreetmap.org/wiki/File:Data.sa.gov.au_CCBYPermission_Open_Street_Map.pdf">completed the OSMF CC BY waiver</a> to make their CC BY 4.0 licensed open data from <a href="https://data.sa.gov.au">data.sa.gov.au</a> usable in OpenStreetMap, address points aren't included in this data currently, even if it was the <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">Import Guidelines</a> would need to be followed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '18, 01:53</strong></p>
<img src="https://secure.gravatar.com/avatar/7284ad488e18a2b052a9c7b8fe1e3922?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aharvey&#39;s gravatar image" />
<p><span>aharvey</span><br />
<span class="score" title="523 reputation points">523</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aharvey has 4 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-63116" class="comments-container">
&#10;</div>
<div id="comment-tools-63116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63116-form-container" class="comment-form-container">
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

