+++
type = "question"
title = "What is the bandwith limit?"
description = '''Hi, I am new to the GIS world and I am working on a website that I would like to use OSM on. I have been playing around with OpenLayers and would like to know if the bandwidth limit is applicable when using OpenLayers to view the maps and if it is then also what is the limit? Thanks, Matt'''
date = "2011-03-24T11:14:00Z"
lastmod = "2011-03-24T11:37:00Z"
weight = 4037
keywords = [ "limit", "bandwidth", "openlayers" ]
aliases = [ "/questions/4037" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the bandwith limit?](/questions/4037/what-is-the-bandwith-limit)

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
<span id="post-4037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4037-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am new to the GIS world and I am working on a website that I would like to use OSM on. I have been playing around with OpenLayers and would like to know if the bandwidth limit is applicable when using OpenLayers to view the maps and if it is then also what is the limit?</p>
<p>Thanks,</p>
<p>Matt</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-limit" rel="tag" title="see questions tagged &#39;limit&#39;">limit</span> <span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '11, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/d9ff5b4974913c085bfe0bbc6e048386?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matt_H&#39;s gravatar image" />
<p><span>Matt_H</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matt_H has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '11, 11:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-4037" class="comments-container">
&#10;</div>
<div id="comment-tools-4037" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4037-form-container" class="comment-form-container">
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

<span id="4038"></span>

<div id="answer-container-4038" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4038-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-4038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two different limits:</p>
<ol>
<li>The limit of raw data that can be downloaded from the API. This API is meant for edits and thus limits the amount of data that you can download to a amount that you wont normally reach while mapping. If you need more data have a look at <a href="https://wiki.openstreetmap.org/wiki/Planet">planet dumps</a> (also available as regional extracts) or the <a href="https://wiki.openstreetmap.org/wiki/Osmxapi">XAPI</a>. If you exceed that amount you will be automatically blocked with the message "bandwidth exceeded".</li>
<li>The limit of renderd tiles that you can download. What is and isn't fair use is laid out in the <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">tile usage policy</a>. This is counted per source connection. If one user (or one application) download so many tiles that it is noticable by a server admin it will be served the yellow-black tile shown on the wiki page. If 100 of your users view your website with openlayers and openstreetmap tiles embedded, everything should be fine. If you have 100000 users viewing your website and requesting tiles we will probably notice the referrer, contact you, tell you to stop it and if you don't, we'll block you manually.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '11, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-4038" class="comments-container">
&#10;</div>
<div id="comment-tools-4038" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4038-form-container" class="comment-form-container">
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

