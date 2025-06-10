+++
type = "question"
title = "easy and quick way to add POIs from OSM to uMap"
description = '''what is the quickest and easiest way to add a single POI from OSM to uMap? I would also like to include things like opening hours, address and other tags. what I currently do is, I create a new marker (the POI entry) on uMap. Then I go to OSM, search for my POI, copy the tags and paste it in the des...'''
date = "2015-01-29T09:40:00Z"
lastmod = "2019-09-22T11:01:00Z"
weight = 40689
keywords = [ "clickable", "poi", "osm24", "osm", "umap" ]
aliases = [ "/questions/40689" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [easy and quick way to add POIs from OSM to uMap](/questions/40689/easy-and-quick-way-to-add-pois-from-osm-to-umap)

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
<span id="post-40689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40689-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>what is the quickest and easiest way to add a single POI from OSM to uMap? I would also like to include things like opening hours, address and other tags.</p>
<p>what I currently do is, I create a new marker (the POI entry) on uMap. Then I go to OSM, search for my POI, copy the tags and paste it in the description of the POI in uMap. Then I have to edit the text I just pasted and remove all of the unnecessary stuff. <strong>Is there a better way to do this?</strong></p>
<p>In Google Maps one can simply click on a POI (e.g. a Restaurant) and add it to a map. In uMap (and OSM) POI's are unfortunately not clickable. In osm24.eu POI's are clickable, but unfortunately osm24.eu is not integrated with uMap as of now.</p>
<p>I've just discoverd that one can export a POI from OSM into XML format and import in uMap this file (selecting OSM file format). But import in uMaps doesn't work with all POIs, specifically those which have lot's of additional tags. Also things like opening hours are not automatically put in the descriptions of the POI in uMap.</p>
<p>Another possible solution is <a href="http://www.mappa-mercia.org/2014/09/creating-an-always-up-to-date-map.html">described here</a> from this <a href="https://bitbucket.org/yohanboniface/umap/issue/112/ease-osm-objects-integration-through">uMap thread</a>. It is based on overpass and probalbly exactly what I need, but it is way too complicated for a regular user. The uMap developer says they want to work on a more simple solution, but no one knows when (or if) that will be ready to use</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-clickable" rel="tag" title="see questions tagged &#39;clickable&#39;">clickable</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span> <span class="post-tag tag-link-osm24" rel="tag" title="see questions tagged &#39;osm24&#39;">osm24</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '15, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/6becf19b4f69018510c55b228a327771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Urml&#39;s gravatar image" />
<p><span>Urml</span><br />
<span class="score" title="76 reputation points">76</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Urml has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jan '15, 10:45</strong> </span></p>
</div>
</div>
<div id="comments-container-40689" class="comments-container">
<span id="70880"></span>
<div id="comment-70880" class="comment">
<div id="post-70880-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>uMap issue has been created recently to make this easier: <a href="https://github.com/umap-project/umap/issues/710">https://github.com/umap-project/umap/issues/710</a> .</p>
</div>
<div id="comment-70880-info" class="comment-info">
<span class="comment-age">(22 Sep '19, 11:01)</span> <span class="comment-user userinfo">Richlv</span>
</div>
</div>
</div>
<div id="comment-tools-40689" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40689-form-container" class="comment-form-container">
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

<span id="41320"></span>

<div id="answer-container-41320" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41320-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Urml has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What do you think of this <a href="http://umap.openstreetmap.fr/fr/map/carte-sans-nom_30247#19/48.85339/2.33946">uMap</a>. I've configured my data layer with remote data, checked "dynamic" option and given this data url:</p>
<pre><code>http://overpass-api.de/api/interpreter?data=[out:json][timeout:25];(node[&quot;opening_hours&quot;][&quot;amenity&quot;=&quot;restaurant&quot;]({south},{west},{north},{east}););out body;&gt;;out skel qt;</code></pre>
<p>Then I've putted in "popup options" content:</p>
<pre><code>{name}
Opening hours: {opening_hours}
[[https://www.openstreetmap.org/{id}|data]]</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '15, 15:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-41320" class="comments-container">
<span id="41643"></span>
<div id="comment-41643" class="comment">
<div id="post-41643-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nicolas, it looks interesting, thanks. But these are apparently <strong>all</strong> restaurant POIs that have opening hours in OSM, right?. My goal is select only a few POIs that I want to see. Not all POI's. Fetching opening hours from OSM is of course nice to have. In any case, I've tried to setup a layer with the data url's you've provided, but it doesn't seem to work for me. No POI's appear on the map dynamically. <a href="http://imagizer.imageshack.com/img911/7312/wS3D5n.png">Here</a> is a screenshot of what I configured. Anything else I have to change from the default default options? Or if you don't mind, I would be grateful if you would export your map to kml or gpx and post the file to sendspace.com or alike. It might be faster than troubleshooting. Thanks.</p>
</div>
<div id="comment-41643-info" class="comment-info">
<span class="comment-age">(11 Mar '15, 14:00)</span> <span class="comment-user userinfo">Urml</span>
</div>
</div>
<span id="41650"></span>
<div id="comment-41650" class="comment">
<div id="post-41650-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ok. 1. You can export the displayed data on my map, filter or modify them in josm (or any other tool) and create another map on umap with your new data set. 2. I don't see the entire URL and try to select the "osm" format.</p>
</div>
<div id="comment-41650-info" class="comment-info">
<span class="comment-age">(12 Mar '15, 08:45)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="41651"></span>
<div id="comment-41651" class="comment">
<div id="post-41651-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>for downloading data: click on "more" on the left, then on the button "share and export" and then select the desired format and it's done.</p>
</div>
<div id="comment-41651-info" class="comment-info">
<span class="comment-age">(12 Mar '15, 08:47)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="41653"></span>
<div id="comment-41653" class="comment">
<div id="post-41653-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the hints. Overpass seems to be very flexible and powerfull, but nothing for the regular, non tech user. In any case, now it seems to work for me and maybe I can build something usefull with it. Thanks again.</p>
</div>
<div id="comment-41653-info" class="comment-info">
<span class="comment-age">(12 Mar '15, 10:44)</span> <span class="comment-user userinfo">Urml</span>
</div>
</div>
</div>
<div id="comment-tools-41320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41320-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40720"></span>

<div id="answer-container-40720" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40720-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The mappa mercia page you linked to is the best way of doing this, although, as you mention, not very user friendly</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '15, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/9f0faef4659de616c82f448ff3f4e8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaCor&#39;s gravatar image" />
<p><span>DaCor</span><br />
<span class="score" title="1339 reputation points"><span>1.3k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaCor has one accepted answer">2%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jan '15, 17:56</strong> </span></p>
</div>
</div>
<div id="comments-container-40720" class="comments-container">
&#10;</div>
<div id="comment-tools-40720" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40720-form-container" class="comment-form-container">
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

