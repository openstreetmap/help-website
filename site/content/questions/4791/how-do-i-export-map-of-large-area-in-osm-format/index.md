+++
type = "question"
title = "How do I export map of large area in .osm format?"
description = '''I want to download a map of large area (like a city) for some researches, in the .osm format. Methods in https://help.openstreetmap.org/questions/22/how-do-i-export-map-images-of-larger-areas seems useless for my problem because it can capture the small area in .osm format only. How can I do that?'''
date = "2011-04-25T14:04:00Z"
lastmod = "2020-02-25T15:43:00Z"
weight = 4791
keywords = [ "large", ".osm", "area" ]
aliases = [ "/questions/4791" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I export map of large area in .osm format?](/questions/4791/how-do-i-export-map-of-large-area-in-osm-format)

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
<span id="post-4791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4791-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to download a map of large area (like a city) for some researches, in the .osm format. Methods in <a href="/questions/22/how-do-i-export-map-images-of-larger-areas">https://help.openstreetmap.org/questions/22/how-do-i-export-map-images-of-larger-areas</a> seems useless for my problem because it can capture the small area in .osm format only. How can I do that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-large" rel="tag" title="see questions tagged &#39;large&#39;">large</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '11, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/812e5d5946cdd3c66a718d4685ac703f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="crisp22140&#39;s gravatar image" />
<p><span>crisp22140</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="crisp22140 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4791" class="comments-container">
&#10;</div>
<div id="comment-tools-4791" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4791-form-container" class="comment-form-container">
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

<span id="4793"></span>

<div id="answer-container-4793" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4793-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-4793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="crisp22140 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Export tab on the main OSM site is not the appropriate way to export large areas: it uses too many resources from the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6">API</a>. I also think it is limited by constraints in the API interface itself: there is a maximum area and maximum amount of data which can be downloaded through the API <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Retrieving_map_data_by_bounding_box:_GET_.2Fapi.2F0.6.2Fmap">map</a> call.</p>
<p>Therefore you will need to use the available alternatives:</p>
<ul>
<li><strong>One of the <a href="https://wiki.openstreetmap.org/wiki/Xapi">XAPI</a> instances</strong>. These are designed for providing read-only access to very recent snapshots of OSM data. Unfortunately, they are often overwhelmed by requests. The <a href="http://open.mapquestapi.com/xapi/">JAXPI</a> instance run by MapQuest is probably the best one to use: it should certainly cope with downloading a city.</li>
<li><strong>Using an already available download</strong>, such as those of <a href="http://www.geofabrik.de/data/download.html">Geofabrik</a> and <a href="http://downloads.cloudmade.com/">Cloudmade</a>. These cover many (but not all) countries and most regions of the world. For places which are very actively mapped there may be extracts of smaller areas. In most cases you will still want to reduce the amount of data you use. To do this you should use <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> to read the extract file and extract a bounding box from it (<code>osmosis --rx file="bla.osm" --bbox left=##.## right=##.## top=##.## bottom=##.## --wx file="extracted_city.osm"</code>, where the numeric values are the lat and lon of a bounding box)</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '11, 14:34</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-4793" class="comments-container">
&#10;</div>
<div id="comment-tools-4793" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4793-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53602"></span>

<div id="answer-container-53602" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53602-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use QGis to download large data. Vector-&gt;OpenStreetMap-&gt; download data</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '16, 05:47</strong></p>
<img src="https://secure.gravatar.com/avatar/6c7e605d14fb58b948cf721f9506f1b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Man&#39;s gravatar image" />
<p><span>Man</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Man has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53602" class="comments-container">
<span id="68377"></span>
<div id="comment-68377" class="comment">
<div id="post-68377-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This solution is very simple. Thank you Man for your answer.</p>
</div>
<div id="comment-68377-info" class="comment-info">
<span class="comment-age">(14 Mar '19, 23:35)</span> <span class="comment-user userinfo">BanAnanas</span>
</div>
</div>
<span id="73231"></span>
<div id="comment-73231" class="comment">
<div id="post-73231-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is that still up to date? Was just searching for a solution, to download larger areas from OSM and found your answer. But when I go for Vector - there is not OpenStreetMap. Is there another way today or just not possible anymore?</p>
</div>
<div id="comment-73231-info" class="comment-info">
<span class="comment-age">(25 Feb '20, 12:50)</span> <span class="comment-user userinfo">sant0s_</span>
</div>
</div>
<span id="73232"></span>
<div id="comment-73232" class="comment">
<div id="post-73232-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes there is still a download option in QGIS, the QuickOSM plugin, which is an interface to Overpass which these days is the de facto answer to the question. In general it's probably better in this case to ask a new question as this one is rather old: it's rather easier to provide an up-to-date answer without having to explain why the accepted answers are no longer applicable.</p>
</div>
<div id="comment-73232-info" class="comment-info">
<span class="comment-age">(25 Feb '20, 15:43)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53602-form-container" class="comment-form-container">
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

