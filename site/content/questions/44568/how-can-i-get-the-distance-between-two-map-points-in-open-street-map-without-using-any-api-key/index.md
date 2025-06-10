+++
type = "question"
title = "How can i get the distance between two map points in open street map without using any api key"
description = '''I wish to get the distance and the travel time from one map point to another in open street map in json format for my laravel based website. How can i do this? Since i am new to open street map, i am not aware of the steps to follow. Please help me. Thanks in advance'''
date = "2015-07-31T10:56:00Z"
lastmod = "2015-07-31T11:10:00Z"
weight = 44568
keywords = [ "openstreetmap", "distance" ]
aliases = [ "/questions/44568" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can i get the distance between two map points in open street map without using any api key](/questions/44568/how-can-i-get-the-distance-between-two-map-points-in-open-street-map-without-using-any-api-key)

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
<span id="post-44568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44568-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I wish to get the distance and the travel time from one map point to another in open street map in json format for my laravel based website. How can i do this? Since i am new to open street map, i am not aware of the steps to follow. Please help me. Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '15, 10:56</strong></p>
<img src="https://secure.gravatar.com/avatar/b7c3d7f33bf049e6236ef4e9a4ea6f92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sujitha&#39;s gravatar image" />
<p><span>sujitha</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sujitha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44568" class="comments-container">
&#10;</div>
<div id="comment-tools-44568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44568-form-container" class="comment-form-container">
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

<span id="44569"></span>

<div id="answer-container-44569" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44569-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Computing the travel distance between two points requires a routing engine. A routing engine needs to be run on a server. There are a couple of people who operate such servers and who will let you use them for free, for example the server at <a href="http://map.project-osrm.org">http://map.project-osrm.org</a>. That site also contains documentation about how to call the server and get a JSON response (or just switch on your browser's net debugger and see what requests it sends).</p>
<p>Be aware however that if you should set up a web site that makes many such routing requests, or even a commercial site of which such routing is an integral part, then you should not use these volunteer run resources, but instead set up your own routing server. The software and the data are free for the taking - but the computing resources need to be paid for by someone!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '15, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-44569" class="comments-container">
&#10;</div>
<div id="comment-tools-44569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44569-form-container" class="comment-form-container">
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

