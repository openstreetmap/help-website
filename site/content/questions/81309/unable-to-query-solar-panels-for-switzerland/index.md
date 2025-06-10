+++
type = "question"
title = "Unable to query solar panels for switzerland."
description = '''Hi everyone :)  I am having trouble making specific queries for Switzerland. Below is the query that I am using that works for cities i.e. Bern and other countries i.e. United Kingdom, however for some reason whenever I change the name to Switzerland it does not work. Any advice on what I am doing w...'''
date = "2021-08-15T10:42:00Z"
lastmod = "2021-08-15T20:20:00Z"
weight = 81309
keywords = [ "python", "switzerland", "overpass-api", "error" ]
aliases = [ "/questions/81309" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to query solar panels for switzerland.](/questions/81309/unable-to-query-solar-panels-for-switzerland)

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
<span id="post-81309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81309-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone :) I am having trouble making specific queries for Switzerland. Below is the query that I am using that works for cities i.e. Bern and other countries i.e. United Kingdom, however for some reason whenever I change the name to Switzerland it does not work. Any advice on what I am doing wrong??<br />
<code>solar_query = """ [out:json]; area["name"="Switzerland"]-&gt;.searchArea; ( node(area.searchArea)["generator:source"="solar"]['generator:output:electricity'='yes']; way(area.searchArea)["generator:source"="solar"]['generator:output:electricity'='yes']; relation(area.searchArea)["generator:source"="solar"]['generator:output:electricity'='yes']; ); out body; &gt;; out skel qt; """</code> Thanks so much :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-switzerland" rel="tag" title="see questions tagged &#39;switzerland&#39;">switzerland</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Aug '21, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/df7276b9b119854e6ce531c7f6acfebe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dylan_johnson123&#39;s gravatar image" />
<p><span>dylan_johnso...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dylan_johnson123 has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-81309" class="comments-container">
&#10;</div>
<div id="comment-tools-81309" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81309-form-container" class="comment-form-container">
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

<span id="81310"></span>

<div id="answer-container-81310" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81310-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Should it be name:en rather than name, to match the English language name "Switzerland"?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '21, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-81310" class="comments-container">
<span id="81311"></span>
<div id="comment-81311" class="comment">
<div id="post-81311-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes it worked :)! Thanks so much, must have missed that on the docs !</p>
</div>
<div id="comment-81311-info" class="comment-info">
<span class="comment-age">(15 Aug '21, 20:20)</span> <span class="comment-user userinfo">dylan_johnso...</span>
</div>
</div>
</div>
<div id="comment-tools-81310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81310-form-container" class="comment-form-container">
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

