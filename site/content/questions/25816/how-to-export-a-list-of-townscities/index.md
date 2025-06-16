+++
type = "question"
title = "How to export a list of towns/cities?"
description = '''Hello! I&#x27;d like to export a list of the 100 biggest towns/cities of each country. The result should be a csv-file with the columns:countrycode,townname,population,latitude,longitude How would i do that?'''
date = "2013-08-26T14:59:00Z"
lastmod = "2013-08-27T02:39:00Z"
weight = 25816
keywords = [ "town", "country", "csv", "export" ]
aliases = [ "/questions/25816" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to export a list of towns/cities?](/questions/25816/how-to-export-a-list-of-townscities)

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
<span id="post-25816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25816-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>I'd like to export a list of the 100 biggest towns/cities of each country.</p>
<p>The result should be a csv-file with the columns:countrycode,townname,population,latitude,longitude</p>
<p>How would i do that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-town" rel="tag" title="see questions tagged &#39;town&#39;">town</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Aug '13, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/7c6ca7659bc8c54bf09e2dba891f76c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mawe4585&#39;s gravatar image" />
<p><span>mawe4585</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mawe4585 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25816" class="comments-container">
&#10;</div>
<div id="comment-tools-25816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25816-form-container" class="comment-form-container">
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

<span id="25835"></span>

<div id="answer-container-25835" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25835-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You're going to have to create this export yourself, though I suspect the data isn't there. Population doesn't seem like data which would be added to OSM (whether political or practical).</p>
<p>If the data does exist, then you'll likely be using the <a href="http://www.overpass-api.de/index.html">Overpass API</a>. This is a query language for accessing/filtering the OSM data.</p>
<p>Other options may include going all the way down and using <a href="https://wiki.openstreetmap.org/wiki/Osmium">Osmium</a>.</p>
<p>I'm not well versed in the types of data requests which can be made, the choices seem slim and Overpass seems to be the most comprehensive and user friendly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '13, 02:39</strong></p>
<img src="https://secure.gravatar.com/avatar/7e77c05737bf455a5bf99c0f17ac19d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="he_the_great&#39;s gravatar image" />
<p><span>he_the_great</span><br />
<span class="score" title="1175 reputation points"><span>1.2k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="he_the_great has 3 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-25835" class="comments-container">
&#10;</div>
<div id="comment-tools-25835" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25835-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25824"></span>

<div id="answer-container-25824" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25824-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please do a search on this FAQ site about "export, data, csv, list, places" or similar keywords.</p>
<p>There are already questions like yours, and answers as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '13, 16:42</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-25824" class="comments-container">
&#10;</div>
<div id="comment-tools-25824" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25824-form-container" class="comment-form-container">
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

