+++
type = "question"
title = "JOSM filter &#x27;untagged&#x27;. Is there a way to get it to filter out &#x27;meta&#x27; tags?"
description = '''By default JOSM&#x27;s filter &#x27;untagged&#x27; option ignores meta tags such as note, source &amp;amp; created_by etc. This is useful &amp;amp; annoying in equal measure. Is there a way to turn this behavior off? (toggle?) Is there a list of all these meta tags?'''
date = "2019-01-09T22:49:00Z"
lastmod = "2019-01-10T07:39:00Z"
weight = 67531
keywords = [ "filter", "josm", "untagged" ]
aliases = [ "/questions/67531" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM filter 'untagged'. Is there a way to get it to filter out 'meta' tags?](/questions/67531/josm-filter-untagged-is-there-a-way-to-get-it-to-filter-out-meta-tags)

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
<span id="post-67531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67531-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>By default JOSM's filter 'untagged' option ignores meta tags such as note, source &amp; created_by etc.</p>
<p>This is useful &amp; annoying in equal measure. Is there a way to turn this behavior off? (toggle?)</p>
<p>Is there a list of all these meta tags?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-untagged" rel="tag" title="see questions tagged &#39;untagged&#39;">untagged</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '19, 22:49</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-67531" class="comments-container">
&#10;</div>
<div id="comment-tools-67531" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67531-form-container" class="comment-form-container">
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

<span id="67533"></span>

<div id="answer-container-67533" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67533-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-67533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tags to ignore when looking for untagged nodes seem to be defined in <a href="https://josm.openstreetmap.de/browser/josm/trunk/src/org/openstreetmap/josm/data/validation/tests/UntaggedNode.java#L62">UntaggedNode.java function visitKeyValue()</a>. Currently they are:</p>
<ul>
<li>tag fixme=*</li>
<li>tags starting with
<ul>
<li>note, comment or description</li>
<li>created_by or converted_by</li>
<li>watch</li>
<li>source</li>
</ul></li>
</ul>
<p>I'm not sure if you can disable this behavior. However you can explicitly add tags you are searching for, for example by using "untagged or fixme or note".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jan '19, 07:39</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '19, 08:06</strong> </span></p>
</div>
</div>
<div id="comments-container-67533" class="comments-container">
&#10;</div>
<div id="comment-tools-67533" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67533-form-container" class="comment-form-container">
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

