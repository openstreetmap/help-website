+++
type = "question"
title = "Server spec"
description = '''I&#x27;m looking to run a server that should expect pretty heavy traffic (in bursts) for a small area. I&#x27;m thinking about 6k-12k requests per minute. It will only cover one state in the US. My understanding is that I can get away with a pretty small SSD using an extract, say 250GB or so (is that right?),...'''
date = "2016-09-23T17:51:00Z"
lastmod = "2016-09-23T18:28:00Z"
weight = 52202
keywords = [ "mapserver" ]
aliases = [ "/questions/52202" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Server spec](/questions/52202/server-spec)

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
<span id="post-52202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52202-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking to run a server that should expect pretty heavy traffic (in bursts) for a small area. I'm thinking about 6k-12k requests per minute. It will only cover one state in the US. My understanding is that I can get away with a pretty small SSD using an extract, say 250GB or so (is that right?), but can I get away with 16GB RAM for that amount of traffic?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapserver" rel="tag" title="see questions tagged &#39;mapserver&#39;">mapserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '16, 17:51</strong></p>
<img src="https://secure.gravatar.com/avatar/9e9be16c7a847f68655ac16c1b1291e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gratheni&#39;s gravatar image" />
<p><span>gratheni</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gratheni has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Sep '16, 17:52</strong> </span></p>
</div>
</div>
<div id="comments-container-52202" class="comments-container">
<span id="52204"></span>
<div id="comment-52204" class="comment">
<div id="post-52204-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ul>
<li>What zoom levels?</li>
<li>What stylesheet?</li>
<li>What infrastructure (mod_tile / renderd, or something else)?</li>
<li>Which State (e.g. Rhode Island or California)?</li>
</ul>
<p>... are only the first questions that someone would want to ask.</p>
</div>
<div id="comment-52204-info" class="comment-info">
<span class="comment-age">(23 Sep '16, 18:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52202-form-container" class="comment-form-container">
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

<span id="52203"></span>

<div id="answer-container-52203" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52203-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This should be fairly easy to bench yourself, so do that. It will give you a much better answers than relying on somebody else's experience, which differs in hardware, dataset, and usage pattern. You'll need to set up your server anyway, and benching it is just a small amount of extra work. Use rented hardware so that you can change it easily if it is too slow or overkill.</p>
<p>How often do you intend to update the data (which will invalidate the tiles) ? Will your users concentrate on specific areas, or spread randomly ? These two questions will determine how big a tile cache you need, and wether your SSD/RAM is big enough. At 200 rq/s, you should also make sure that you have a decent number of cores.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '16, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-52203" class="comments-container">
&#10;</div>
<div id="comment-tools-52203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52203-form-container" class="comment-form-container">
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

