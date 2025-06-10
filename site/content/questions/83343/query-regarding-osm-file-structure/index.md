+++
type = "question"
title = "Query regarding OSM file structure"
description = '''Hi, Had a query regarding the OSM file&#x27;s tags and values. I came across files where there are inconsistencies in tag names and certain node ids/uids do not have tag names and thereby don&#x27;t allow us to identify what feature it is without opening them in any GIS software. For example, some node ids an...'''
date = "2022-02-04T14:53:00Z"
lastmod = "2022-02-04T15:17:00Z"
weight = 83343
keywords = [ "nodes", "osm", "uid", "tags" ]
aliases = [ "/questions/83343" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Query regarding OSM file structure](/questions/83343/query-regarding-osm-file-structure)

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
<span id="post-83343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83343-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, Had a query regarding the OSM file's tags and values. I came across files where there are inconsistencies in tag names and certain node ids/uids do not have tag names and thereby don't allow us to identify what feature it is without opening them in any GIS software. For example, some node ids and uids have tag names as "source bing". Is there a way to identify what they represent without opening them in GIS software? Also, How does OSM recognize these features without proper tag names and values?</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-uid" rel="tag" title="see questions tagged &#39;uid&#39;">uid</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '22, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/fe6210f88c9476bec58ecca5e107762a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wind-pioneer&#39;s gravatar image" />
<p><span>Wind-pioneer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wind-pioneer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83343" class="comments-container">
&#10;</div>
<div id="comment-tools-83343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83343-form-container" class="comment-form-container">
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

<span id="83344"></span>

<div id="answer-container-83344" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83344-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Many nodes are just there to build a way object from them. This means while a node might represent a wind turbine, a node might also just represent one of 20 points that make up the building footprint of a wind turbine. In these cases, the node will be a member of a way object and that way object will have the tags you are interested in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '22, 15:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-83344" class="comments-container">
&#10;</div>
<div id="comment-tools-83344" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83344-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83345"></span>

<div id="answer-container-83345" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83345-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This wiki article gives a lot of details about the OSM data structure : <a href="https://wiki.openstreetmap.org/wiki/Elements">https://wiki.openstreetmap.org/wiki/Elements</a></p>
<p>Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '22, 15:17</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-83345" class="comments-container">
&#10;</div>
<div id="comment-tools-83345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83345-form-container" class="comment-form-container">
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

