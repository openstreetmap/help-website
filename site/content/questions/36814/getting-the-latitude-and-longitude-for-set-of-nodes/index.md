+++
type = "question"
title = "Getting the latitude and longitude for Set of nodes"
description = '''in my android application when i take a picture the GPS read info of my position (lat/long)  , I need to get the lat/long for my town and insert it to my database , I download my region file by mean of JSOM the file was in osm extention , my mind tell me that i need to write a program to parse this ...'''
date = "2014-09-14T17:37:00Z"
lastmod = "2014-09-22T18:51:00Z"
weight = 36814
keywords = [ "openstreetmap", "latitude", "longitude", "gps" ]
aliases = [ "/questions/36814" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Getting the latitude and longitude for Set of nodes](/questions/36814/getting-the-latitude-and-longitude-for-set-of-nodes)

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
<span id="post-36814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36814-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>in my <strong>android application</strong> when i take a picture the <strong>GPS</strong> read info of my position <strong>(lat/long)</strong> , I need to get the lat/long for my town and insert it to my database , I download my region file by mean of <strong>JSOM</strong> the file was in <strong>osm</strong> extention , my mind tell me that i need to write a program to parse this file (raw data) and insert the whole <strong>node's</strong> (id + lat +long + other info ) to my database is that the best solution ,becasue time killing me ! .</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '14, 17:37</strong></p>
<img src="https://secure.gravatar.com/avatar/26ceead6052b5d3807baaa723b9fa7a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abogaseem&#39;s gravatar image" />
<p><span>abogaseem</span><br />
<span class="score" title="25 reputation points">25</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abogaseem has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36814" class="comments-container">
<span id="36828"></span>
<div id="comment-36828" class="comment">
<div id="post-36828-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>if the gps as a fix when the picture is taken it should be in the jpeg's exif info.</p>
</div>
<div id="comment-36828-info" class="comment-info">
<span class="comment-age">(15 Sep '14, 08:24)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-36814" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36814-form-container" class="comment-form-container">
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

<span id="36821"></span>

<div id="answer-container-36821" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36821-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's not quite clear what your actual problem is. Your smartphone should already be capable of obtaining lat and lon via the integrated GPS device.</p>
<p>Do you need the name of the town for the current position? In that case you can use <a href="http://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a> and run a simple <em>reverse</em> geocoding query.</p>
<p>Do you need the position of a specific town? In that case use <a href="http://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a> with a regular geocoding query.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '14, 20:42</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-36821" class="comments-container">
&#10;</div>
<div id="comment-tools-36821" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36821-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36815"></span>

<div id="answer-container-36815" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36815-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See this previous answer to adding geo-tagged photos in Josm.<br />
<a href="https://help.openstreetmap.org/questions/26416/open-jpg-in-josm">photos</a> (Not relevant to this question)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '14, 18:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Sep '14, 19:28</strong> </span></p>
</div>
</div>
<div id="comments-container-36815" class="comments-container">
<span id="36816"></span>
<div id="comment-36816" class="comment">
<div id="post-36816-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>that's not my question ! , my is how to extract the raw data in file.osm into my database</p>
</div>
<div id="comment-36816-info" class="comment-info">
<span class="comment-age">(14 Sep '14, 19:03)</span> <span class="comment-user userinfo">abogaseem</span>
</div>
</div>
<span id="36977"></span>
<div id="comment-36977" class="comment">
<div id="post-36977-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you are telling us about two kinds of raw data:</p>
<p>1) photos with or without a GPS position that should be contained in the mentioned EXIF information field of each photo.</p>
<p>2) you have downloaded OSM data in raw XML OSM format via the JOSM editor.</p>
<p>But we cannot give you more solutions about your "database" unlesss you tell us IN DETAIL what database you mean.</p>
<p>Tell us more about your aim!</p>
</div>
<div id="comment-36977-info" class="comment-info">
<span class="comment-age">(22 Sep '14, 18:51)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-36815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36815-form-container" class="comment-form-container">
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

