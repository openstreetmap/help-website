+++
type = "question"
title = "lookup request logging"
description = '''We set up a local instance of OSM following the Wiki instructions and are successfully using it to reverse geo-code; we would love to contribute to OSM&#x27;s data but cant tell if it is possible to log the requests for reverse lookup that fail to produce a full address on our local server.  Does such a ...'''
date = "2016-11-17T21:55:00Z"
lastmod = "2016-11-17T22:49:00Z"
weight = 53014
keywords = [ "reversegeocoding", "nominatim", "logging" ]
aliases = [ "/questions/53014" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [lookup request logging](/questions/53014/lookup-request-logging)

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
<span id="post-53014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53014-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We set up a local instance of OSM following the Wiki instructions and are successfully using it to reverse geo-code; we would love to contribute to OSM's data but cant tell if it is possible to log the requests for reverse lookup that fail to produce a full address on our local server.</p>
<p>Does such a function/log exist in Nominatim or would the only option be to develop it in our application? we intend to have an employee review such requests and update them on OSM.org so that our server will get the additions through osmosis.</p>
<p>Thanks for any help or direction that you can provide.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-logging" rel="tag" title="see questions tagged &#39;logging&#39;">logging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Nov '16, 21:55</strong></p>
<img src="https://secure.gravatar.com/avatar/e6878fab8fcd3f8025c091e99be0bc64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="artecss&#39;s gravatar image" />
<p><span>artecss</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="artecss has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53014" class="comments-container">
&#10;</div>
<div id="comment-tools-53014" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53014-form-container" class="comment-form-container">
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

<span id="53021"></span>

<div id="answer-container-53021" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53021-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="artecss has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at the <code>new_query_log</code> table. It contains date, search term and number of results. You might need to switch on logging in the <code>build/settings.php</code> files (look for <code>CONST_Log_DB</code>). You should be able to extract failed queries from that. If not we're open for pull request on github.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '16, 22:49</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-53021" class="comments-container">
&#10;</div>
<div id="comment-tools-53021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53021-form-container" class="comment-form-container">
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

