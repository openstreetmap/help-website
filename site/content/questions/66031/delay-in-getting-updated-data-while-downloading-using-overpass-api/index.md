+++
type = "question"
title = "delay in getting updated data while downloading using overpass API"
description = '''I do a query in JOSM to get ways (with different tags) that share a same node. Then I unglue ways at these nodes and move the one of the new nodes and put it close to the other one. Then I upload changes and delete current data layer. Now if I download using the same query the previously changed dat...'''
date = "2018-09-24T09:53:00Z"
lastmod = "2018-09-24T11:16:00Z"
weight = 66031
keywords = [ "overpassapi", "josm", "download" ]
aliases = [ "/questions/66031" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [delay in getting updated data while downloading using overpass API](/questions/66031/delay-in-getting-updated-data-while-downloading-using-overpass-api)

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
<span id="post-66031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I do a query in JOSM to get ways (with different tags) that share a same node.</p>
<p>Then I unglue ways at these nodes and move the one of the new nodes and put it close to the other one. Then I upload changes and delete current data layer.</p>
<p>Now if I download using the same query the previously changed data are retrieved again (unchanged), while if I wait for 1-2 minutes before new download, data is updated.</p>
<p>But using the normal "Download from OSM" dialog I get the updated data, even a few seconds after upload.</p>
<p>Is this normal or I need to do something with my query?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '18, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/5b2d680cd0c22a32517db07ed16eeaf2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iriman&#39;s gravatar image" />
<p><span>iriman</span><br />
<span class="score" title="297 reputation points">297</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iriman has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Sep '18, 10:32</strong> </span></p>
</div>
</div>
<div id="comments-container-66031" class="comments-container">
&#10;</div>
<div id="comment-tools-66031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66031-form-container" class="comment-form-container">
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

<span id="66033"></span>

<div id="answer-container-66033" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66033-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="iriman has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is normal. Overpass is a secondary service that feeds from minutely diffs, and hence the replication will always take a few minutes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '18, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-66033" class="comments-container">
&#10;</div>
<div id="comment-tools-66033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66033-form-container" class="comment-form-container">
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

