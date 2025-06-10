+++
type = "question"
title = "Usage Policy"
description = '''I&#x27;ve read the usage policy and various documents but do not see explicit usage numbers on what&#x27;s allowed like I&#x27;ve seen with Google maps. We have a travel guide that we would like to use OpenStreetMap. It&#x27;s possible we could see 50k map views per day. Would that be considered excessive?'''
date = "2012-04-16T22:56:00Z"
lastmod = "2012-04-17T19:08:00Z"
weight = 12070
keywords = [ "usage", "policy" ]
aliases = [ "/questions/12070" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Usage Policy](/questions/12070/usage-policy)

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
<span id="post-12070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12070-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-12070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've read the usage policy and various documents but do not see explicit usage numbers on what's allowed like I've seen with Google maps.</p>
<p>We have a travel guide that we would like to use OpenStreetMap. It's possible we could see 50k map views per day. Would that be considered excessive?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-policy" rel="tag" title="see questions tagged &#39;policy&#39;">policy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '12, 22:56</strong></p>
<img src="https://secure.gravatar.com/avatar/10be05fdd39bf97c4c781dc19eb42529?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="travelr&#39;s gravatar image" />
<p><span>travelr</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="travelr has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '12, 23:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-12070" class="comments-container">
&#10;</div>
<div id="comment-tools-12070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12070-form-container" class="comment-form-container">
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

<span id="12071"></span>

<div id="answer-container-12071" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12071-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-12071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The reason we chose not to give exact numbers is that people would then assume that if N is excessive, N-1 must be allowed (and if we ban them they'd say "but I counted the requests!!!!").</p>
<p>OSM is serving roughly 150 million tiles per day (for a current number, take the figure in the "total" row and the "Avg:" column and multiply by 86,400):</p>
<p><img src="http://munin.openstreetmap.org/openstreetmap/tile.openstreetmap/squid_requests-day.png" alt="tile.openstreetmap.org munin graph" /></p>
<p>One map view, on a standard map size, might perhaps use 20 or so tiles, so when you say 50k map views per day then that's one million tiles per day; in other words, you would be using about 1/150th of what OSM delivers.</p>
<p>I'd say that is a calibre in which you should look at running your own tile server, or paying someone to provide tiles for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '12, 23:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-12071" class="comments-container">
<span id="12093"></span>
<div id="comment-12093" class="comment">
<div id="post-12093-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the clarification.</p>
</div>
<div id="comment-12093-info" class="comment-info">
<span class="comment-age">(17 Apr '12, 19:08)</span> <span class="comment-user userinfo">travelr</span>
</div>
</div>
</div>
<div id="comment-tools-12071" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12071-form-container" class="comment-form-container">
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

