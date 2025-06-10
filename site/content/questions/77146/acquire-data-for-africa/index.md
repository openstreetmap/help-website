+++
type = "question"
title = "Acquire data for africa"
description = '''Hi team, Hope you are doing well. I am currently a Master&#x27;s in Data Analytics student at National College of Ireland, Dublin. I want to perform research on the effects of climatic changes on malaria cases depending upon the topographical parameters of Africa. And for this research, I require the dat...'''
date = "2020-10-19T10:23:00Z"
lastmod = "2020-10-23T18:35:00Z"
weight = 77146
keywords = [ "africa_topography" ]
aliases = [ "/questions/77146" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Acquire data for africa](/questions/77146/acquire-data-for-africa)

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
<span id="post-77146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77146-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi team,</p>
<p>Hope you are doing well.</p>
<p>I am currently a Master's in Data Analytics student at National College of Ireland, Dublin. I want to perform research on the effects of climatic changes on malaria cases depending upon the topographical parameters of Africa. And for this research, I require the data of topography. Please can you provide me with the same as it would be quite helpful for my research.</p>
<p>Thanks and Regards Akanksha Thorat akankshathorat14@gmail.com</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-africa_topography" rel="tag" title="see questions tagged &#39;africa_topography&#39;">africa_topography</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '20, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/6bc7c2e2f70f33f21284063648b3caca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akankshathorat&#39;s gravatar image" />
<p><span>akankshathorat</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akankshathorat has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77146" class="comments-container">
<span id="77149"></span>
<div id="comment-77149" class="comment">
<div id="post-77149-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think you need to be a bit more specific on what it is you need. Then someone could figure out if what you are looking for is available and how you could retrieve it.</p>
<p>Are you looking for terrain types, road networks, settlements, ...? What granularity are you looking for? What kind of data formats can you handle? etc.</p>
</div>
<div id="comment-77149-info" class="comment-info">
<span class="comment-age">(19 Oct '20, 11:33)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="77202"></span>
<div id="comment-77202" class="comment">
<div id="post-77202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the input, I am specifically looking at the terrain types (plain, plateau, hill, valley) whose topography indices (TWI, TRI, TPI, Slope, Elevation, Aspect) would be available. Related image data(png,jpeg) or excel sheet(csv) data would be really helpful for my research.</p>
</div>
<div id="comment-77202-info" class="comment-info">
<span class="comment-age">(23 Oct '20, 15:14)</span> <span class="comment-user userinfo">akankshathorat</span>
</div>
</div>
</div>
<div id="comment-tools-77146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77146-form-container" class="comment-form-container">
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

<span id="77206"></span>

<div id="answer-container-77206" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77206-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are global sources of elevation data, often in the form of DEM (digital elevation model) files covering a degree or so of latitude and longitude. That can be used with tools like the gdal library to extract out slope, etc. Searching the web for SRTM (Shuttle Radar Topography Mission) and/or DEM should find you at least some of the datasets.</p>
<p>None of this has anything to do with OpenStreetMap which, in general, does not have topography information in it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '20, 18:35</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-77206" class="comments-container">
&#10;</div>
<div id="comment-tools-77206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77206-form-container" class="comment-form-container">
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

