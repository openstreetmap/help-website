+++
type = "question"
title = "Geocoding correction"
description = '''I am from India.In my Company We are developing a Web Interface which is able to do Forward and Reverse Geocoding Process Simultaneously .For this we used OSM MAP of India where the centroid point is placed in each polygon .then this Point is sent to GOOGLE API where the equivalent address for the p...'''
date = "2013-12-14T03:50:00Z"
lastmod = "2013-12-14T07:34:00Z"
weight = 29050
keywords = [ "geocoding" ]
aliases = [ "/questions/29050" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Geocoding correction](/questions/29050/geocoding-correction)

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
<span id="post-29050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29050-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am from India.In my Company We are developing a Web Interface which is able to do Forward and Reverse Geocoding Process Simultaneously .For this we used OSM MAP of India where the centroid point is placed in each polygon .then this Point is sent to GOOGLE API where the equivalent address for the point is generated.We Then structured the address based on address returned as Country,State,District,Locality,Sub-Locality and neighbourhood. The Problem is now :Multipart polygons for eg: some of the neighbourhood polygons is present in multiple sub localities .Why this occurs how can I resolve it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '13, 03:50</strong></p>
<img src="https://secure.gravatar.com/avatar/2683b12218e08a59d45fa2e5a0fbd2f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun&#39;s gravatar image" />
<p><span>Arun</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29050" class="comments-container">
&#10;</div>
<div id="comment-tools-29050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29050-form-container" class="comment-form-container">
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

<span id="29051"></span>

<div id="answer-container-29051" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29051-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-29051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Without a concrete example it is diffcult to see where the problem is. However your application should be able to handle multipolygons with multiple outer and inner rings in lieu of simple polygons in any case (use an appropriate algorithm to generate the centroid).</p>
<p>Note: your usage of the google api may not be in line with googles terms of service and that under no circumstances are you allowed to enter results from google in to the OSM database.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '13, 07:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Dec '13, 10:18</strong> </span></p>
</div>
</div>
<div id="comments-container-29051" class="comments-container">
&#10;</div>
<div id="comment-tools-29051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29051-form-container" class="comment-form-container">
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

