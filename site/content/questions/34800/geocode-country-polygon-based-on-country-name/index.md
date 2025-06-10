+++
type = "question"
title = "Geocode country polygon based on country name"
description = '''Hello, I have developed an application where I have saved in a database some country names, and through a geocoding function of MapQuest I am showing a map with the markers. What I want to do now is create a kind of choropleth map, where each of the countries that exist in my database will be drawn ...'''
date = "2014-07-10T15:22:00Z"
lastmod = "2014-07-11T07:57:00Z"
weight = 34800
keywords = [ "geocoding", "polygons" ]
aliases = [ "/questions/34800" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Geocode country polygon based on country name](/questions/34800/geocode-country-polygon-based-on-country-name)

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
<span id="post-34800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34800-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have developed an application where I have saved in a database some country names, and through a geocoding function of MapQuest I am showing a map with the markers. What I want to do now is create a kind of choropleth map, where each of the countries that exist in my database will be drawn as polygons in the map, and then filled with specific colors based on the corresponding value for each country.</p>
<p>Is there a way for me to geocode my geographic data and get/draw the polygon for each of my countries?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '14, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/53a3c46c23eea233454d90c22e073171?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mariagr&#39;s gravatar image" />
<p><span>mariagr</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mariagr has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34800" class="comments-container">
<span id="34821"></span>
<div id="comment-34821" class="comment">
<div id="post-34821-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your replies. I did see the leafletjs example along with the geofabrik country shapes, but my issue is that in the first example, the countries file is "handmade" for the specific example, while the second provides very large files per country. But because I dont have fixed countries, I want to dynamically get the boundaries for each country depending on what my user chooses.</p>
</div>
<div id="comment-34821-info" class="comment-info">
<span class="comment-age">(11 Jul '14, 07:57)</span> <span class="comment-user userinfo">mariagr</span>
</div>
</div>
</div>
<div id="comment-tools-34800" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34800-form-container" class="comment-form-container">
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

<span id="34813"></span>

<div id="answer-container-34813" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34813-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using an internet search engine with "choropleth map openstreetmap" gives several hints e.g. to <a href="http://leafletjs.com/examples/choropleth.html">leafletjs</a>.</p>
<p>Success?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '14, 20:12</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-34813" class="comments-container">
&#10;</div>
<div id="comment-tools-34813" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34813-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34810"></span>

<div id="answer-container-34810" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34810-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might want to get the country shapes at <a href="http://download.geofabrik.de">http://download.geofabrik.de</a>, simplify the geometries and use OpenLayer/Leaflet JS libs to realize a cloured highlightning.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '14, 19:58</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-34810" class="comments-container">
&#10;</div>
<div id="comment-tools-34810" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34810-form-container" class="comment-form-container">
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

