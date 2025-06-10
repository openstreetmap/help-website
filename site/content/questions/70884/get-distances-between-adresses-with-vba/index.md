+++
type = "question"
title = "Get distances between adresses with VBA"
description = '''Hello, How can I query OSM to give me travel distances between adresses from access VBA? regards'''
date = "2019-09-22T14:28:00Z"
lastmod = "2019-09-22T14:35:00Z"
weight = 70884
keywords = [ "access", "vba" ]
aliases = [ "/questions/70884" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get distances between adresses with VBA](/questions/70884/get-distances-between-adresses-with-vba)

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
<span id="post-70884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70884-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>How can I query OSM to give me travel distances between adresses from access VBA?</p>
<p>regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-vba" rel="tag" title="see questions tagged &#39;vba&#39;">vba</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '19, 14:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c41a6f853a125347923503a050e42fdf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thedan85&#39;s gravatar image" />
<p><span>thedan85</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thedan85 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70884" class="comments-container">
&#10;</div>
<div id="comment-tools-70884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70884-form-container" class="comment-form-container">
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

<span id="70886"></span>

<div id="answer-container-70886" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70886-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-70886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="thedan85 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot query OSM to do this, you need to query a routing engine. You can either install a routing engine yourself - open source software includes OSRM, Graphhopper, Valhalla - or you can use a routing engine run (and paid for) by someone else, for example the free offers on graphhopper.com (running Graphhopper) or routing.openstreetmap.de (running OSRM). These servers have usage policies and limits - it's ok to make a couple hundred queries for yourself but if you want to use it intensively or commercially, double-check what you are allowed to do.</p>
<p>Generally these servers will expect you to make a HTTP request and reply with a JSON message that you can then process in VBA. The precise formatting of the request and response depend on which routing engine you are using.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '19, 14:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '19, 14:37</strong> </span></p>
</div>
</div>
<div id="comments-container-70886" class="comments-container">
&#10;</div>
<div id="comment-tools-70886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70886-form-container" class="comment-form-container">
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

