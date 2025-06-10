+++
type = "question"
title = "Scale of data"
description = '''I downloaded a data package of the county of Essex, but how do you find out the metadata of the data package as it isn&#x27;t posted anywhere clearly, can only see when the data was last updated?'''
date = "2017-03-17T09:57:00Z"
lastmod = "2017-03-17T14:40:00Z"
weight = 55149
keywords = [ "scale" ]
aliases = [ "/questions/55149" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Scale of data](/questions/55149/scale-of-data)

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
<span id="post-55149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55149-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I downloaded a data package of the county of Essex, but how do you find out the metadata of the data package as it isn't posted anywhere clearly, can only see when the data was last updated?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-scale" rel="tag" title="see questions tagged &#39;scale&#39;">scale</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '17, 09:57</strong></p>
<img src="https://secure.gravatar.com/avatar/1acd683aceb2ed00189e52e8043c19e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BenPlummer&#39;s gravatar image" />
<p><span>BenPlummer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BenPlummer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55149" class="comments-container">
<span id="55150"></span>
<div id="comment-55150" class="comment">
<div id="post-55150-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What did you download and from where?</p>
</div>
<div id="comment-55150-info" class="comment-info">
<span class="comment-age">(17 Mar '17, 10:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="55151"></span>
<div id="comment-55151" class="comment">
<div id="post-55151-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I downloaded this •essex-latest-free.shp.zip, yields a number of ESRI compatible shape files when unzipped. (Format description PDF) This file was last modified 8 hours ago. File size: 55 MB. I got it from download.geofabrik</p>
</div>
<div id="comment-55151-info" class="comment-info">
<span class="comment-age">(17 Mar '17, 10:19)</span> <span class="comment-user userinfo">BenPlummer</span>
</div>
</div>
</div>
<div id="comment-tools-55149" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55149-form-container" class="comment-form-container">
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

<span id="55155"></span>

<div id="answer-container-55155" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55155-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-55155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM data is vector data, so it doesn't have a concept of "scale" like a printed/rendered map (aka raster data) has. You can can zoom in however much you want.</p>
<p>One thing that can be done with OSM/vector data is to simplify its geometry (to make the file smaller), by removing nodes that won't make a noticeable difference when rendered at a certain scale. But AFAIK the geofabrik files do not do this. And a simplified geometry is still not the same concept as a "1:X scale".</p>
<p>Lastly, the implementation details of how lat/long are stored in OSM mean that we do not have infinite precision. But the limit is smaller than yearly continental drift, so it's not a practical concern.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '17, 11:32</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-55155" class="comments-container">
&#10;</div>
<div id="comment-tools-55155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55155-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55152"></span>

<div id="answer-container-55152" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55152-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd expect that it would be the same "and contains all OSM data up to 2017-03-16T21:43:02Z" as higher up the page on <a href="http://download.geofabrik.de/europe/great-britain/england/essex.html">http://download.geofabrik.de/europe/great-britain/england/essex.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '17, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-55152" class="comments-container">
<span id="55153"></span>
<div id="comment-55153" class="comment">
<div id="post-55153-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I looked on the page you said but I can't see any mention of scale i.e a ratio like 1:25000 or something like that is what I'm looking for</p>
</div>
<div id="comment-55153-info" class="comment-info">
<span class="comment-age">(17 Mar '17, 10:41)</span> <span class="comment-user userinfo">BenPlummer</span>
</div>
</div>
<span id="55159"></span>
<div id="comment-55159" class="comment">
<div id="post-55159-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As mentioned by Vincent, there is no scale: Ways consist of points. Points are specified by lat/lon. When you render them you decide the projection and scale to render them at.</p>
</div>
<div id="comment-55159-info" class="comment-info">
<span class="comment-age">(17 Mar '17, 14:33)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="55161"></span>
<div id="comment-55161" class="comment">
<div id="post-55161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It looks like I completely misunderstood what the question meant by "metadata" :)</p>
</div>
<div id="comment-55161-info" class="comment-info">
<span class="comment-age">(17 Mar '17, 14:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55152-form-container" class="comment-form-container">
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

