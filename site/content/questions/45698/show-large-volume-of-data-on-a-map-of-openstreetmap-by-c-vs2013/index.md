+++
type = "question"
title = "[closed] show large volume of data on a map of OpenStreetMap by C# VS2013"
description = '''I am very new to Open Street Map. I have some data that need to be shown on a map by Open Street Map from C# VS2013. The application can be WPF or windows forms. The data is about some statistics results by location. For example, location, latitude, longitude, address, population, household, income ...'''
date = "2015-10-04T04:49:00Z"
lastmod = "2015-10-04T10:44:00Z"
weight = 45698
keywords = [ "c#", "visualization", "wpf", "c#.net" ]
aliases = [ "/questions/45698" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] show large volume of data on a map of OpenStreetMap by C# VS2013](/questions/45698/show-large-volume-of-data-on-a-map-of-openstreetmap-by-c-vs2013)

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
<span id="post-45698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45698-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-45698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am very new to Open Street Map. I have some data that need to be shown on a map by Open Street Map from C# VS2013. The application can be WPF or windows forms.</p>
<p>The data is about some statistics results by location.</p>
<p>For example,</p>
<p>location, latitude, longitude, address, population, household, income of household, tax of household</p>
<p>The data was got from a database by running SQL query from C# code. The data volume may have 1 million rows. I need to do some aggregation so that they can be displayed on the map clearly. For example, aggregate all houshold (located in zip code 10080) information in a circle displayed on the map.</p>
<p>Moreover, I need to provide the following functions the on map so that the users can do:</p>
<p>(1) when zoom in to a location, more detailed data (from zip code to street level) will be shown.</p>
<p>(2) when zoom out, only the aggregated data was shown. For example, from street level to zip code level.</p>
<p>(3) users can get detailed data by selecting any location on the map as long as the location has data to show. For example, if a location in zip code = 10080 was selected, all household information in the selected location can be shown.</p>
<p>(4) users can hold control and click any location so that multiple locations household information can be show.</p>
<p>I have checked OSM wiki website and API, but I still have no idea how to add the data to a OSM map and edit the map to show it clearly.</p>
<p>Any help would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-visualization" rel="tag" title="see questions tagged &#39;visualization&#39;">visualization</span> <span class="post-tag tag-link-wpf" rel="tag" title="see questions tagged &#39;wpf&#39;">wpf</span> <span class="post-tag tag-link-c#.net" rel="tag" title="see questions tagged &#39;c#.net&#39;">c#.net</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '15, 04:49</strong></p>
<img src="https://secure.gravatar.com/avatar/b9c47170c54a4fa58922f981df8a54b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="usact&#39;s gravatar image" />
<p><span>usact</span><br />
<span class="score" title="19 reputation points">19</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="usact has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '16, 12:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45698" class="comments-container">
<span id="45700"></span>
<div id="comment-45700" class="comment">
<div id="post-45700-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Duplicate post on GIS stackexchange: <a href="http://gis.stackexchange.com/questions/165227/show-some-data-on-a-map-by-openstreetmap-from-c-vs2013">http://gis.stackexchange.com/questions/165227/show-some-data-on-a-map-by-openstreetmap-from-c-vs2013</a></p>
<p>Another duplicate post on StackOverflow: <a href="http://stackoverflow.com/questions/32929453/show-large-volume-of-data-on-a-map-of-openstreetmap-by-c-sharp-vs2013">http://stackoverflow.com/questions/32929453/show-large-volume-of-data-on-a-map-of-openstreetmap-by-c-sharp-vs2013</a></p>
<p>Please follow up there. Thanks.</p>
</div>
<div id="comment-45700-info" class="comment-info">
<span class="comment-age">(04 Oct '15, 08:58)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="45702"></span>
<div id="comment-45702" class="comment">
<div id="post-45702-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note that your question is not OSM specific. You do not really want to "add your data to OSM" (which would make your data public), you just want to display your data on top of a map - whether this is OpenStreetMap or something else doesn't change what you have to do.</p>
</div>
<div id="comment-45702-info" class="comment-info">
<span class="comment-age">(04 Oct '15, 10:44)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45698" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45698-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Quoting PolyGeo: "Here are my requirements, can you help me design my solution?". Question is not suitable for Q&A site." by mmd 04 Oct '15, 09:00

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45699"></span>

<div id="answer-container-45699" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45699-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This should be handy enough to do, for the most part. You may want to do all your aggregating first and work with the finished data</p>
<p>1 &amp; 2 - Leaflet + Cluster plugin will do that nicely for you</p>
<p>3 - Depends on if the post code boundaries are available</p>
<p>4 - I dont know if that is currently possible without</p>
<p>Have a look at <a href="http://umap.openstreetmap.fr/en/">http://umap.openstreetmap.fr/en/</a></p>
<p>If that doesnt suit your needs, you may want to look at something like CartoDB or building it all from scratch in Tilemill / QGIS</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '15, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/9f0faef4659de616c82f448ff3f4e8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaCor&#39;s gravatar image" />
<p><span>DaCor</span><br />
<span class="score" title="1339 reputation points"><span>1.3k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaCor has one accepted answer">2%</span></p>
</div>
</div>
<div id="comments-container-45699" class="comments-container">
&#10;</div>
<div id="comment-tools-45699" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45699-form-container" class="comment-form-container">
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

