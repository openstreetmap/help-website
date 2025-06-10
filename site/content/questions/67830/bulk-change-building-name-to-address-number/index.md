+++
type = "question"
title = "Bulk change building name to address number?"
description = '''I am mapping a community in Peru, where addresses are listed by block letter and number (ie. Block A Lot 5). because OSM isn&#x27;t designed to present this type of address, I thought the best option was to put this information in the buliding name space. However, I&#x27;m realizng it may make more sense to p...'''
date = "2019-01-31T17:30:00Z"
lastmod = "2019-02-01T18:19:00Z"
weight = 67830
keywords = [ "addressing", "bulk_editing", "address" ]
aliases = [ "/questions/67830" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bulk change building name to address number?](/questions/67830/bulk-change-building-name-to-address-number)

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
<span id="post-67830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67830-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am mapping a community in Peru, where addresses are listed by block letter and number (ie. Block A Lot 5). because OSM isn't designed to present this type of address, I thought the best option was to put this information in the buliding name space. However, I'm realizng it may make more sense to put block and lot information in the address number area. Is there a way to make bulk changes to adjust the addresses of all of the houses I've done so far in this area?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span> <span class="post-tag tag-link-bulk_editing" rel="tag" title="see questions tagged &#39;bulk_editing&#39;">bulk_editing</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jan '19, 17:30</strong></p>
<img src="https://secure.gravatar.com/avatar/6a11d51836984dc2f8ae62eea932a5c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amitchell18&#39;s gravatar image" />
<p><span>amitchell18</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amitchell18 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67830" class="comments-container">
<span id="67831"></span>
<div id="comment-67831" class="comment">
<div id="post-67831-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You should probably use separate tags for the two elements: addr:block perhaps and addr:housenumber (or conscription number if the lot numbering is assigned as each lot is created). If you are still not sure addr:full is always the best fallback.</p>
</div>
<div id="comment-67831-info" class="comment-info">
<span class="comment-age">(31 Jan '19, 19:30)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67830-form-container" class="comment-form-container">
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

<span id="67839"></span>

<div id="answer-container-67839" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67839-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If it is dozens or hundreds of addresses, JOSM should work fine. I would use the search to find the buildings you are interested in and then you can just rename the key. It should be possible to come up with a search that only matches the buildings with addresses in the name, something like <code>building name:Block</code> would match buildings with "Block" in the name field.</p>
<p>As SK53 mentions, better to use <code>addr:full</code> than to put data into a field where it doesn't quite fit.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '19, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-67839" class="comments-container">
&#10;</div>
<div id="comment-tools-67839" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67839-form-container" class="comment-form-container">
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

