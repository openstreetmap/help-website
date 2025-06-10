+++
type = "question"
title = "how to get the duration and distance values of many address pairs"
description = '''I am doing a research now. I have 1000 real addresses and my computational example need duration and distance values for each address pair. I know I can use the Google Maps to get them one by one. But the number is very big and I almost need to do it 1000000 times. I just know OpenStreetMap and like...'''
date = "2015-02-05T13:52:00Z"
lastmod = "2015-02-05T17:53:00Z"
weight = 40805
keywords = [ "duration", "distance", "address" ]
aliases = [ "/questions/40805" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to get the duration and distance values of many address pairs](/questions/40805/how-to-get-the-duration-and-distance-values-of-many-address-pairs)

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
<span id="post-40805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40805-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am doing a research now. I have 1000 real addresses and my computational example need duration and distance values for each address pair. I know I can use the Google Maps to get them one by one. But the number is very big and I almost need to do it 1000000 times.</p>
<p>I just know OpenStreetMap and like it very much.I am eager to get the data to finish the job now. I hope I can upload the document including all the addresses and get all the duration and distance values effectively. Who can tell me how to do using OpenStreetMap? Or I will pay you if you can help me to get the data easily. I will be highly appreciated.</p>
<p>Thanks a lot!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-duration" rel="tag" title="see questions tagged &#39;duration&#39;">duration</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '15, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/96e218babb2339954e8c821f3c886453?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PengYang&#39;s gravatar image" />
<p><span>PengYang</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PengYang has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40805" class="comments-container">
&#10;</div>
<div id="comment-tools-40805" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40805-form-container" class="comment-form-container">
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

<span id="40806"></span>

<div id="answer-container-40806" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40806-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-40806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Data is free - computing time is not. Hence, you can download the OSM data and run a routing algorithm on this on your own server (or desktop PC or notebook computer) without paying a penny, but you cannot upload a spreadsheet and have OSM compute the results for you.</p>
<p>A popular routing server is <a href="http://www.project-osrm.org">OSRM</a> and you will find download and install instructions right there on the web site. Converting from addresses to coordinates requires a geocoding service in addition to that, but this is something that you only need to do 1000 times and you can store the coordinates.</p>
<p>If you'd rather pay someone to do the work for you, check out <a href="http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">Commercial OSM Software and Services</a> on the Wiki.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '15, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-40806" class="comments-container">
&#10;</div>
<div id="comment-tools-40806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40806-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40809"></span>

<div id="answer-container-40809" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40809-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After paying attention to frederik's hints, you can also do a search on this FAQ site for "<strong>batch geocode</strong>" or batch geocoding ... you are not the first one asking in this direction.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '15, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-40809" class="comments-container">
&#10;</div>
<div id="comment-tools-40809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40809-form-container" class="comment-form-container">
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

