+++
type = "question"
title = "How to query for adjacent admin boundaries?"
description = '''After hours of internet sleuthing and more-error-than-trials on overpassturbo, I admit defeat and ask for help. Here&#x27;s the thing: I&#x27;d like to..  take a given coordinate as input get its corresponding administrative boundary (admin_level=6) node to (2), give me all adjacent (as in: bordering on) admi...'''
date = "2021-05-05T15:34:00Z"
lastmod = "2021-05-06T08:58:00Z"
weight = 80009
keywords = [ "overpass", "nominatim" ]
aliases = [ "/questions/80009" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to query for adjacent admin boundaries?](/questions/80009/how-to-query-for-adjacent-admin-boundaries)

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
<span id="post-80009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80009-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After hours of internet sleuthing and more-error-than-trials on overpassturbo, I admit defeat and ask for help. Here's the thing: I'd like to..</p>
<ol>
<li>take a given coordinate as input</li>
<li>get its corresponding administrative boundary (admin_level=6) node</li>
<li>to (2), give me all <strong>adjacent</strong> (as in: bordering on) admin boundaries</li>
</ol>
<p>Any idea how this could be accomplished? I found the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#.22around.22_-_finding_something_near_something_else">"around" clause</a> but couldn't get it to work either.</p>
<p>Any help is greatly appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 May '21, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7679b0922bf0f46b00874d27922b96d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="supyall&#39;s gravatar image" />
<p><span>supyall</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="supyall has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80009" class="comments-container">
<span id="80010"></span>
<div id="comment-80010" class="comment">
<div id="post-80010-score" class="comment-score">
1
</div>
<div class="comment-text">
<ol>
<li>Check out the 'is_in' command. 3. admin_level boundaries should be all relations so 'recurse' back up from your found boundary to the ways it's attached to &amp; search those ways to see if it has any other associated relations.</li>
</ol>
</div>
<div id="comment-80010-info" class="comment-info">
<span class="comment-age">(05 May '21, 16:20)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="80020"></span>
<div id="comment-80020" class="comment">
<div id="post-80020-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the tip, but I'm a bloody noob on the whole OSM thing. Would you (are anyone else watching) be willing to write some example code (overpass would be best for testing purpose) on this?</p>
</div>
<div id="comment-80020-info" class="comment-info">
<span class="comment-age">(06 May '21, 08:58)</span> <span class="comment-user userinfo">supyall</span>
</div>
</div>
</div>
<div id="comment-tools-80009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80009-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

