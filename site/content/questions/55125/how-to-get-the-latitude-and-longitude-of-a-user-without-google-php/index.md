+++
type = "question"
title = "how to get the latitude and longitude of a user without google, PHP ?"
description = '''Hello everyone,  I would like to know how to get the lat and long of users using OSM map, and Nomatim or something else, without using google services, because It wont work in China and few other countries. My goal is to let users find people in specific location, so when they make a research via El...'''
date = "2017-03-16T11:47:00Z"
lastmod = "2017-03-16T17:58:00Z"
weight = 55125
keywords = [ "geolocation", "nominatim", "php" ]
aliases = [ "/questions/55125" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to get the latitude and longitude of a user without google, PHP ?](/questions/55125/how-to-get-the-latitude-and-longitude-of-a-user-without-google-php)

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
<span id="post-55125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55125-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>I would like to know how to get the lat and long of users using OSM map, and Nomatim or something else, <strong>without using google services</strong>, because It wont work in China and few other countries.</p>
<p>My goal is to let users find people in specific location, so when they make a research via Elasticsearch, it will show them choosen located users with a radius range.</p>
<p>Our website is running under <strong>symfony3 , Php</strong>.</p>
<p>hope someone can help us, Thank's by advance</p>
<p>Best regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geolocation" rel="tag" title="see questions tagged &#39;geolocation&#39;">geolocation</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '17, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/b2fd5b892dbad273367e163f0723896c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aladib&#39;s gravatar image" />
<p><span>aladib</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aladib has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '17, 09:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-55125" class="comments-container">
<span id="55126"></span>
<div id="comment-55126" class="comment">
<div id="post-55126-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The question isn't clear. What is your actual input and desired output ? So far this question seems unrelated to OSM, and a quick duckduck search points towards <a href="https://www.elastic.co/guide/en/elasticsearch/reference/1.4/query-dsl-geo-shape-query.html">https://www.elastic.co/guide/en/elasticsearch/reference/1.4/query-dsl-geo-shape-query.html</a></p>
</div>
<div id="comment-55126-info" class="comment-info">
<span class="comment-age">(16 Mar '17, 12:30)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55125-form-container" class="comment-form-container">
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

<span id="55129"></span>

<div id="answer-container-55129" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55129-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM and other OSM-related software can't tell you where a user is. It would be the location services in the user's device/browser that would do that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '17, 17:58</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-55129" class="comments-container">
&#10;</div>
<div id="comment-tools-55129" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55129-form-container" class="comment-form-container">
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

