+++
type = "question"
title = "Using osm2pgsql slim mode with schemas that import very low amount of data"
description = '''How does osm2pgsql slim mode work if I want to import the planet and my schema discards most objects? Does it still need every single node to be stored? (I think so because diffs carry no child object info, so if not all nodes of a way are modified it would need to pull the rest from somewhere - the...'''
date = "2016-09-17T01:29:00Z"
lastmod = "2016-09-17T01:41:00Z"
weight = 52073
keywords = [ "osm2pgsql", "postgis" ]
aliases = [ "/questions/52073" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Using osm2pgsql slim mode with schemas that import very low amount of data](/questions/52073/using-osm2pgsql-slim-mode-with-schemas-that-import-very-low-amount-of-data)

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
<span id="post-52073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52073-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How does osm2pgsql slim mode work if I want to import the planet and my schema discards most objects? Does it still need every single node to be stored? (I think so because diffs carry no child object info, so if not all nodes of a way are modified it would need to pull the rest from somewhere - the slim nodes table)</p>
<p>Also, is the amount of processing time during the initial import still substantial due to how it processes data sequentially, even if the resulting table is going to be small in size?</p>
<p>In other words, does osm2pgsql scale down well for schemas that would only import a low number of objects - like keeping a table of POI? Or should I use osmfilter beforehand?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '16, 01:29</strong></p>
<img src="https://secure.gravatar.com/avatar/b68bcf9f1c4a7921aeee1bb35b0e2784?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RicoElectrico&#39;s gravatar image" />
<p><span>RicoElectrico</span><br />
<span class="score" title="371 reputation points">371</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RicoElectrico has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '16, 01:40</strong> </span></p>
</div>
</div>
<div id="comments-container-52073" class="comments-container">
&#10;</div>
<div id="comment-tools-52073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52073-form-container" class="comment-form-container">
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

<span id="52075"></span>

<div id="answer-container-52075" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52075-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RicoElectrico has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are correct, even if you discard most objects, osm2pgsql in slim mode needs to store all ways and relations with their tags and connections, as well as all node coordinates. (It does not have to store all node tags.)</p>
<p>If you don't need updates, you can use <code>--slim --drop</code> to reduce resource usage somewhat but it will still take a while. Filtering data with osmosis or osmfilter before you import with osm2pgsql will certainly speed things up in this scenario.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '16, 01:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52075" class="comments-container">
&#10;</div>
<div id="comment-tools-52075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52075-form-container" class="comment-form-container">
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

