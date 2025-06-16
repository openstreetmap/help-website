+++
type = "question"
title = "Overpass turbo: Query ran out of memory"
description = ''' I don&#x27;t know how to handle this error'''
date = "2019-01-11T13:59:00Z"
lastmod = "2019-01-12T13:38:00Z"
weight = 67551
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/67551" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass turbo: Query ran out of memory](/questions/67551/overpass-turbo-query-ran-out-of-memory)

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
<span id="post-67551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67551-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><img src="/upfiles/Overpas_turbo_Sr8eilu.png" alt="alt text" /></p>
<p>I don't know how to handle this error</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '19, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/1e0a3ed4d83599fbc07f5f73fd186824?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leanderleza&#39;s gravatar image" />
<p><span>leanderleza</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leanderleza has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-67551" class="comments-container">
<span id="67554"></span>
<div id="comment-67554" class="comment">
<div id="post-67554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you paste the actual text of your query in to the question, the screenshot is not legible.</p>
</div>
<div id="comment-67554-info" class="comment-info">
<span class="comment-age">(11 Jan '19, 14:49)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="67555"></span>
<div id="comment-67555" class="comment">
<div id="post-67555-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is legible in the RSS notification I got:</p>
<p>&lt;osm-script timeout="180" element-limit="20000000"&gt; &lt;union&gt; &lt;area-query ref="3600034719"/&gt; &lt;recurse type="node-relation" into="rels"/&gt; &lt;recurse type="node-way"/&gt; &lt;recurse type="way-relation"/&gt; &lt;/union&gt; &lt;union&gt; &lt;item/&gt; &lt;recurse type="way-node"/&gt; &lt;/union&gt; &lt;print mode="body"/&gt; &lt;/osm-script&gt;</p>
<p>As far as I can tell this will return all relations (and ways and nodes) in Graz which appears to be too much information.</p>
</div>
<div id="comment-67555-info" class="comment-info">
<span class="comment-age">(11 Jan '19, 15:25)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67551-form-container" class="comment-form-container">
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

<span id="67560"></span>

<div id="answer-container-67560" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67560-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found out how to fix it! Just needed to use a higher number at element limit, as it limits the ram use to that amount</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '19, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/1e0a3ed4d83599fbc07f5f73fd186824?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leanderleza&#39;s gravatar image" />
<p><span>leanderleza</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leanderleza has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67560" class="comments-container">
&#10;</div>
<div id="comment-tools-67560" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67560-form-container" class="comment-form-container">
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

