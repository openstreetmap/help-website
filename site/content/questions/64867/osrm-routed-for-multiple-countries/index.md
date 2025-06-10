+++
type = "question"
title = "OSRM routed for multiple countries"
description = '''Hi,  Right now, we run osrm-routed for a single region by running something like /usr/local/bin/osrm-routed -i 127.0.0.1 -p 5000 --algorithm=MLD great-britain-latest.osrm  Now, if we were to add another region (say, the Middle East), do I need to run another instance of osrm-routed and use nginx or ...'''
date = "2018-07-23T08:21:00Z"
lastmod = "2018-07-23T10:19:00Z"
weight = 64867
keywords = [ "osrm", "routing" ]
aliases = [ "/questions/64867" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OSRM routed for multiple countries](/questions/64867/osrm-routed-for-multiple-countries)

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
<span id="post-64867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64867-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Right now, we run osrm-routed for a single region by running something like</p>
<pre><code>/usr/local/bin/osrm-routed -i 127.0.0.1 -p 5000 --algorithm=MLD great-britain-latest.osrm</code></pre>
<p>Now, if we were to add another region (say, the Middle East), do I need to run another instance of osrm-routed and use nginx or something to send the requests to one of these servers? Or is it possible to merge the two results. Googling for this gave me answers like osmosis to convert, but they were working on pbf but the osrm-routed seems to work on .osrm files.</p>
<p>Can you please suggest if the only way is to run multiple osrm-routed servers?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '18, 08:21</strong></p>
<img src="https://secure.gravatar.com/avatar/fb83976abd4d2d2f5f4c4f086a3b09f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raja&#39;s gravatar image" />
<p><span>Raja</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raja has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64867" class="comments-container">
&#10;</div>
<div id="comment-tools-64867" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64867-form-container" class="comment-form-container">
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

<span id="64868"></span>

<div id="answer-container-64868" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64868-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Raja has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot merge two OSRM files, you have to merge the .osm.pbf before you process them into a routing graph.</p>
<p>The alternative is, as you say, running multiple OSRM daemons. It is possible to hide them behind an Apache or nginx web server and, if the bounding boxes are disjunct like e.g. routing for the US and the Middle East, you could even have the server look at the coordinates and "guess" which backend to send the request to.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '18, 09:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-64868" class="comments-container">
<span id="64869"></span>
<div id="comment-64869" class="comment">
<div id="post-64869-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the quick response. If we have disjunct areas like US and MiddleEast, would merging the osm.pbf file work, as there are areas in between that are left out. I am going to give it a try anyway.</p>
</div>
<div id="comment-64869-info" class="comment-info">
<span class="comment-age">(23 Jul '18, 09:10)</span> <span class="comment-user userinfo">Raja</span>
</div>
</div>
<span id="64870"></span>
<div id="comment-64870" class="comment">
<div id="post-64870-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sure it will work, you won't be able to compute routes between the areas but that's all.</p>
</div>
<div id="comment-64870-info" class="comment-info">
<span class="comment-age">(23 Jul '18, 10:19)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64868" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64868-form-container" class="comment-form-container">
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

