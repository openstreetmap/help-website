+++
type = "question"
title = "How to decode the road name to Chinese"
description = '''I have downloaded the SHP file from the openstreetmap, and try to read the data from the shp. But when I get the attribute &quot;name&quot;, I have no idea to decode them to Chinese. Refer to the OpenstreetMap documents, it shows that all the strings are encoded by UTF-8, but the followding code didnt&#x27; work (...'''
date = "2021-06-07T10:13:00Z"
lastmod = "2021-06-10T07:56:00Z"
weight = 80446
keywords = [ "decode", "simplified-chinese" ]
aliases = [ "/questions/80446" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode the road name to Chinese](/questions/80446/how-to-decode-the-road-name-to-chinese)

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
<span id="post-80446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80446-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have downloaded the SHP file from the openstreetmap, and try to read the data from the shp. But when I get the attribute "name", I have no idea to decode them to Chinese. Refer to the OpenstreetMap documents, it shows that all the strings are encoded by UTF-8, but the followding code didnt' work (return the messy chars). new String(feature.getAttribute("name").toString().getBytes("UTF-8"), "gbk").</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-simplified-chinese" rel="tag" title="see questions tagged &#39;simplified-chinese&#39;">simplified-chinese</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '21, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/cc91d948ba8d98477191355d3fe0fdd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paradise099&#39;s gravatar image" />
<p><span>paradise099</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paradise099 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80446" class="comments-container">
<span id="80448"></span>
<div id="comment-80448" class="comment">
<div id="post-80448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain in a bit more detail what your end goal is?</p>
</div>
<div id="comment-80448-info" class="comment-info">
<span class="comment-age">(07 Jun '21, 11:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="80463"></span>
<div id="comment-80463" class="comment">
<div id="post-80463-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Where are you getting a SHP file?</p>
</div>
<div id="comment-80463-info" class="comment-info">
<span class="comment-age">(08 Jun '21, 02:40)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="80470"></span>
<div id="comment-80470" class="comment">
<div id="post-80470-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Download the SHP from the website: <a href="https://download.geofabrik.de">https://download.geofabrik.de</a></p>
</div>
<div id="comment-80470-info" class="comment-info">
<span class="comment-age">(08 Jun '21, 08:56)</span> <span class="comment-user userinfo">paradise099</span>
</div>
</div>
<span id="80471"></span>
<div id="comment-80471" class="comment">
<div id="post-80471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to compare the speed of the real road data.</p>
</div>
<div id="comment-80471-info" class="comment-info">
<span class="comment-age">(08 Jun '21, 08:57)</span> <span class="comment-user userinfo">paradise099</span>
</div>
</div>
</div>
<div id="comment-tools-80446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80446-form-container" class="comment-form-container">
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

<span id="80447"></span>

<div id="answer-container-80447" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80447-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The output when decode the name:</p>
<p><img src="/upfiles/messy.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '21, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/cc91d948ba8d98477191355d3fe0fdd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paradise099&#39;s gravatar image" />
<p><span>paradise099</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paradise099 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '21, 10:49</strong> </span></p>
</div>
</div>
<div id="comments-container-80447" class="comments-container">
&#10;</div>
<div id="comment-tools-80447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80447-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80514"></span>

<div id="answer-container-80514" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80514-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, I had faced a similar situation to yours. I tried to re-download the file and defined the encoding to UTF-8 in QGIS. Maybe this article will help you <a href="https://communities.bentley.com/products/hydraulics">https://communities.bentley.com/products/hydraulics</a><strong>_hydrology/w/hydraulics_and_hydrology</strong>wiki/37273/characters-in-a-shapefile-do-not-appear-correctly-in-the-modelbuilder-preview (or visit communities.bentley.com and find a page 'Characters in a shapefile do not appear correctly in the ModelBuilder preview')</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '21, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/499787bd754895d017e47577bb288202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zramadhanis&#39;s gravatar image" />
<p><span>zramadhanis</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zramadhanis has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jun '21, 07:59</strong> </span></p>
</div>
</div>
<div id="comments-container-80514" class="comments-container">
&#10;</div>
<div id="comment-tools-80514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80514-form-container" class="comment-form-container">
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

