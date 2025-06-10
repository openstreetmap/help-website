+++
type = "question"
title = "Get all POI&#x27;s for a city"
description = '''Hey, I want to get all existing points of interest in a city like e.g. New York. Is there a simple way to do that and get it as an XML file? I already tried this search:  &quot;http://nominatim.openstreetmap.org/search?q=new+york[hospital]&amp;amp;format=xml&amp;amp;polygon=0&amp;amp;addressdetails=1&quot; But I don&#x27;t kn...'''
date = "2015-06-24T21:43:00Z"
lastmod = "2015-06-30T01:14:00Z"
weight = 43759
keywords = [ "city", "poi" ]
aliases = [ "/questions/43759" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Get all POI's for a city](/questions/43759/get-all-pois-for-a-city)

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
<span id="post-43759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43759-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey, I want to get all existing points of interest in a city like e.g. New York. Is there a simple way to do that and get it as an XML file?</p>
<p>I already tried this search: "http://nominatim.openstreetmap.org/search?q=new+york[hospital]&amp;format=xml&amp;polygon=0&amp;addressdetails=1" But I don't know how to eliminate the term "hospital" so that I get all the POI in new york. Is there a way to do that with this tool or do I need a completely another way?</p>
<p>Thanks in advance :) Sebastian</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '15, 21:43</strong></p>
<img src="https://secure.gravatar.com/avatar/5d5e2ac590aea7ca22a3430f2dea074d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="conansc&#39;s gravatar image" />
<p><span>conansc</span><br />
<span class="score" title="35 reputation points">35</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="conansc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43759" class="comments-container">
<span id="43760"></span>
<div id="comment-43760" class="comment">
<div id="post-43760-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Did you checked out already <a href="http://overpass-turbo.eu">http://overpass-turbo.eu</a> ?</p>
</div>
<div id="comment-43760-info" class="comment-info">
<span class="comment-age">(24 Jun '15, 22:12)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-43759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43759-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="43802"></span>

<div id="answer-container-43802" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43802-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-43802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="conansc has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For a similar task, I have used a combination of Osmosis and Osmfilter:</p>
<ol>
<li>download an extract for the desired area (e.g. <a href="http://download.geofabrik.de/north-america/us/new-york.html">http://download.geofabrik.de/north-america/us/new-york.html</a> )</li>
<li>find out the coordinate box you're interested in (the above gives you the entire Empire State :))</li>
<li>extract a .osm file (substitute the box values from step 2, the below ones are obviously nowhere near NYC):</li>
</ol>
<p><code>osmosis --read-pbf file=inputfile.pbf --dataset-bounding-box bottom=49.75 top=50.35 left=14.05 right=14.87 --write-xml file=nyc.osm</code></p>
<p>4 . filter the resulting XML using osmfilter:</p>
<p><code>osmfilter nyc.osm --keep="amenity=" --keep-ways="amenity=" --keep-relations="amenity=" &gt; amenities.xml</code></p>
<p>The above will give you everything tagged "amenity" - this should cover many POIs; check the OSM wiki for other tags which you may want to see.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '15, 08:42</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '15, 08:43</strong> </span></p>
</div>
</div>
<div id="comments-container-43802" class="comments-container">
<span id="43804"></span>
<div id="comment-43804" class="comment">
<div id="post-43804-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can probably replace the bounding box with a poly file to cut just the city you want. A good source for polyfiles straight from OSM boundaries is <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a></p>
</div>
<div id="comment-43804-info" class="comment-info">
<span class="comment-age">(26 Jun '15, 09:27)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="43815"></span>
<div id="comment-43815" class="comment">
<div id="post-43815-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good point - wanted to keep the answer simple.</p>
</div>
<div id="comment-43815-info" class="comment-info">
<span class="comment-age">(26 Jun '15, 15:04)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-43802" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43802-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43781"></span>

<div id="answer-container-43781" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43781-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please try the search feature of this FAQ site und use keywords like "export POI" or similar ...</p>
<p>there have been already several questions like yours ... and good answers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '15, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-43781" class="comments-container">
&#10;</div>
<div id="comment-tools-43781" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43781-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43850"></span>

<div id="answer-container-43850" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43850-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for your answers :)</p>
<p>I have decided to use the .osm files and write my own parser for them, because I need to automatize the whole step with JAVA EE.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '15, 01:14</strong></p>
<img src="https://secure.gravatar.com/avatar/5d5e2ac590aea7ca22a3430f2dea074d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="conansc&#39;s gravatar image" />
<p><span>conansc</span><br />
<span class="score" title="35 reputation points">35</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="conansc has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '15, 01:18</strong> </span></p>
</div>
</div>
<div id="comments-container-43850" class="comments-container">
&#10;</div>
<div id="comment-tools-43850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43850-form-container" class="comment-form-container">
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

