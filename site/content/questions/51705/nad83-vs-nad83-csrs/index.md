+++
type = "question"
title = "nad83 vs nad83 (CSRS)"
description = '''I am new to mapping and not familiar with the acronyms and standards. With that said I am trying to answer the following question: Geographic point locations used in the Solution should be displayed in an industry acceptable G.I.S format; does OpenStreetMap maps use geographic coordinate system (Lat...'''
date = "2016-08-24T20:35:00Z"
lastmod = "2016-08-25T11:40:00Z"
weight = 51705
keywords = [ "nad83" ]
aliases = [ "/questions/51705" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nad83 vs nad83 (CSRS)](/questions/51705/nad83-vs-nad83-csrs)

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
<span id="post-51705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51705-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to mapping and not familiar with the acronyms and standards. With that said I am trying to answer the following question:</p>
<p>Geographic point locations used in the Solution should be displayed in an industry acceptable G.I.S format; does OpenStreetMap maps use geographic coordinate system (Latitude, Longitude) with a North American Datum 1983 (NAD 83) and not NAD 83 (CSRS).</p>
<p>Any help is much appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nad83" rel="tag" title="see questions tagged &#39;nad83&#39;">nad83</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '16, 20:35</strong></p>
<img src="https://secure.gravatar.com/avatar/85787b34459da87ec89eeabd181e6b8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ARG1964&#39;s gravatar image" />
<p><span>ARG1964</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ARG1964 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51705" class="comments-container">
&#10;</div>
<div id="comment-tools-51705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51705-form-container" class="comment-form-container">
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

<span id="51707"></span>

<div id="answer-container-51707" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51707-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap data is stored is stored and distributed with unprojected WGS84 coordinates EPSG:4326. Typical maps displayed on the web use googles web mercator EPSG:3857, the maps displayed on openstreetmap.org are no exception to that (see <span>EPSG:3857</span>).</p>
<p>But naturally you can project OSM data to whatever you want for display purposes, however I'm not aware of a tool that does it directly (typically you would convert to shapefiles and reproject those).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '16, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '16, 22:52</strong> </span></p>
</div>
</div>
<div id="comments-container-51707" class="comments-container">
<span id="51717"></span>
<div id="comment-51717" class="comment">
<div id="post-51717-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can actually reproject OSM data when uploading it to PostGIS with osm2pgsq, which is a suitable way of consuming OSM data for a wide range of uses.</p>
</div>
<div id="comment-51717-info" class="comment-info">
<span class="comment-age">(25 Aug '16, 11:40)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51707" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51707-form-container" class="comment-form-container">
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

