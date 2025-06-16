+++
type = "question"
title = "Filtering open street data by certain fields"
description = '''I want to filter the data for a particular .osm file by highway, name, tiger:county, tiger:zip_left and tiger:zip_right. I&#x27;ve tried osmfilter,but it doesn&#x27;t quite seem to work the way I want it to. I used it to just filter highway=residential, but when I look at the data it brings back data where hi...'''
date = "2012-09-18T04:08:00Z"
lastmod = "2012-09-18T08:14:00Z"
weight = 16197
keywords = [ "osmfilter" ]
aliases = [ "/questions/16197" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering open street data by certain fields](/questions/16197/filtering-open-street-data-by-certain-fields)

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
<span id="post-16197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16197-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to filter the data for a particular .osm file by highway, name, tiger:county, tiger:zip_left and tiger:zip_right. I've tried osmfilter,but it doesn't quite seem to work the way I want it to. I used it to just filter highway=residential, but when I look at the data it brings back data where highway is not residential. Also, I want to filter where the fields for highway, name, and tiger:county are absolutely populated and either one of zip_left must be populated. Any thoughts on how to do this with osmfilter?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '12, 04:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a45de846d76d68849c0e70b6fd21f256?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JMB5&#39;s gravatar image" />
<p><span>JMB5</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JMB5 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16197" class="comments-container">
<span id="16199"></span>
<div id="comment-16199" class="comment">
<div id="post-16199-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It is always helpful to show us the osmfilter call(s) you have tried so far.</p>
</div>
<div id="comment-16199-info" class="comment-info">
<span class="comment-age">(18 Sep '12, 06:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-16197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16197-form-container" class="comment-form-container">
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

<span id="16203"></span>

<div id="answer-container-16203" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16203-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can try with <a href="https://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a>. You should get the residential highways wich such a command:</p>
<p><code>osmosis --rx input.osm --tf accept-ways highway=residential --used-node --wx highway.residential.osm</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '12, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-16203" class="comments-container">
&#10;</div>
<div id="comment-tools-16203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16203-form-container" class="comment-form-container">
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

