+++
type = "question"
title = "Possibility of download public GPS trace by user"
description = '''Hi all,  I&#x27;m trying to do some data analysis and would like to know the historical data of each individual. I understand OSM now provides API to download GPS traces in a specific area by using GET /api/0.6/trackpoints?bbox=left,bottom,right,top&amp;amp;page=pageNumber  I wonder if there is any similar f...'''
date = "2019-07-03T15:47:00Z"
lastmod = "2019-07-10T22:20:00Z"
weight = 69864
keywords = [ "download", "gps-traces", "api" ]
aliases = [ "/questions/69864" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Possibility of download public GPS trace by user](/questions/69864/possibility-of-download-public-gps-trace-by-user)

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
<span id="post-69864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69864-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I'm trying to do some data analysis and would like to know the historical data of each individual. I understand OSM now provides API to download GPS traces in a specific area by using</p>
<pre><code>GET /api/0.6/trackpoints?bbox=left,bottom,right,top&amp;page=pageNumber</code></pre>
<p>I wonder if there is any similar function to download GPS trace of a specific user ID? Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-gps-traces" rel="tag" title="see questions tagged &#39;gps-traces&#39;">gps-traces</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '19, 15:47</strong></p>
<img src="https://secure.gravatar.com/avatar/75a49dc51b0dfc8d3a6150ddb9879043?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stormzhou&#39;s gravatar image" />
<p><span>stormzhou</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stormzhou has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69864" class="comments-container">
&#10;</div>
<div id="comment-tools-69864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69864-form-container" class="comment-form-container">
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

<span id="69865"></span>

<div id="answer-container-69865" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69865-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, this is not possible, for privacy reasons. You will notice that the "trackpoints" API does not give you user names or user IDs either.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '19, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-69865" class="comments-container">
<span id="69867"></span>
<div id="comment-69867" class="comment">
<div id="post-69867-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer. That's what confuses me because in the raw data I downloaded each trace started with a string like <code>&lt;url&gt;</code><a href="https://api.openstreetmap.org/user/ABCD/traces/3026889%3C/url%3E"><code>https://api.openstreetmap.org/user/ABCD/traces/3026889&lt;/url&gt;</code></a> , which gives the user name of each GPS trace. But if there is no such API call existing, I'll just try to parse the URL in the raw data instead.</p>
</div>
<div id="comment-69867-info" class="comment-info">
<span class="comment-age">(03 Jul '19, 16:27)</span> <span class="comment-user userinfo">stormzhou</span>
</div>
</div>
<span id="69868"></span>
<div id="comment-69868" class="comment">
<div id="post-69868-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Users have the option of making their traces public so that they can be associated with the user ID but this is true only for a fraction of traces.</p>
</div>
<div id="comment-69868-info" class="comment-info">
<span class="comment-age">(03 Jul '19, 16:39)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="69980"></span>
<div id="comment-69980" class="comment">
<div id="post-69980-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, that explains a lot. I'll download all data to see how I can clean and categorize them.</p>
</div>
<div id="comment-69980-info" class="comment-info">
<span class="comment-age">(10 Jul '19, 22:20)</span> <span class="comment-user userinfo">stormzhou</span>
</div>
</div>
</div>
<div id="comment-tools-69865" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69865-form-container" class="comment-form-container">
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

