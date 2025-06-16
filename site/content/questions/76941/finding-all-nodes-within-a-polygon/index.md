+++
type = "question"
title = "Finding all nodes within a polygon"
description = '''I am trying to extract all nodes (e.g. shop, restaurant, cafe, etc.) from a way (e.g. a shopping mall). Using this http://overpass-turbo.eu/s/YFG, there are some nodes (such as IKEA and Swarovski) that didn&#x27;t get selected by this script. What did I do wrongly?'''
date = "2020-10-04T12:51:00Z"
lastmod = "2020-10-06T00:10:00Z"
weight = 76941
keywords = [ "nodes", "within", "polygon" ]
aliases = [ "/questions/76941" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Finding all nodes within a polygon](/questions/76941/finding-all-nodes-within-a-polygon)

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
<span id="post-76941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76941-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to extract all nodes (e.g. shop, restaurant, cafe, etc.) from a way (e.g. a shopping mall). Using this <a href="http://overpass-turbo.eu/s/YFG">http://overpass-turbo.eu/s/YFG</a>, there are some nodes (such as IKEA and Swarovski) that didn't get selected by this script. What did I do wrongly?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-within" rel="tag" title="see questions tagged &#39;within&#39;">within</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '20, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/d8242cadd7e274a8abb1fabb96be736e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hosei&#39;s gravatar image" />
<p><span>hosei</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hosei has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '20, 12:51</strong> </span></p>
</div>
</div>
<div id="comments-container-76941" class="comments-container">
&#10;</div>
<div id="comment-tools-76941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76941-form-container" class="comment-form-container">
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

<span id="76964"></span>

<div id="answer-container-76964" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76964-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect there may be an error in your polygon. This <a href="http://overpass-turbo.eu/s/YI4">query</a> which uses the retail area for JEM returns both Ikea &amp; Swarvski (although I'm at a bit of a loss about why the latter gets missed).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '20, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-76964" class="comments-container">
<span id="76970"></span>
<div id="comment-76970" class="comment">
<div id="post-76970-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The polygon was based on the nodes of the way (JEM) which should include everything in it. I will try again with other polygon of other way and report back.</p>
</div>
<div id="comment-76970-info" class="comment-info">
<span class="comment-age">(06 Oct '20, 00:10)</span> <span class="comment-user userinfo">hosei</span>
</div>
</div>
</div>
<div id="comment-tools-76964" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76964-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76949"></span>

<div id="answer-container-76949" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76949-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-76949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Both IKEA and Swarovski have their names &amp; brands locked. Probably it may restrict the scripts somehow <img src="/upfiles/Screenshot_2020-10-04_at_20.25.29.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '20, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/be20d26db9045491e65f24686822e4e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="laechoppe&#39;s gravatar image" />
<p><span>laechoppe</span><br />
<span class="score" title="14 reputation points">14</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="laechoppe has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-76949" class="comments-container">
<span id="76950"></span>
<div id="comment-76950" class="comment">
<div id="post-76950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's a feature in the editor, it wouldn't impact the Overpass-API search (which does not consider wikidata tags unless you specify them in the query).</p>
</div>
<div id="comment-76950-info" class="comment-info">
<span class="comment-age">(04 Oct '20, 20:45)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="76958"></span>
<div id="comment-76958" class="comment">
<div id="post-76958-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think the name being locked is the cause. The name is locked because there is a linked Wikidata. If you look at my overpass turbo link, the node "Monster Curry" (7127656165) which its name is not locked, yet it doesn't show up in my query.</p>
</div>
<div id="comment-76958-info" class="comment-info">
<span class="comment-age">(05 Oct '20, 06:47)</span> <span class="comment-user userinfo">hosei</span>
</div>
</div>
</div>
<div id="comment-tools-76949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76949-form-container" class="comment-form-container">
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

