+++
type = "question"
title = "How can I download user edit history for specific users?"
description = '''Hello, I am trying to research a few aspects and then hopefully build a useful tool for OSM. I was wondering if it is possible to obtain the user edit histories for a specific set of users (around 1700, I have their UIDs). I know about the API, but the wiki states that it is recommended only for edi...'''
date = "2014-03-10T14:11:00Z"
lastmod = "2014-03-10T14:20:00Z"
weight = 31423
keywords = [ "api", "users", "history" ]
aliases = [ "/questions/31423" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I download user edit history for specific users?](/questions/31423/how-can-i-download-user-edit-history-for-specific-users)

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
<span id="post-31423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31423-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am trying to research a few aspects and then hopefully build a useful tool for OSM. I was wondering if it is possible to obtain the user edit histories for a specific set of users (around 1700, I have their UIDs).</p>
<p>I know about the API, but the wiki states that it is recommended only for editing operations. I wasn't able to find any queries for such an operation using the Overpass API.</p>
<p>Is the planet.osm dump the best method?</p>
<p>Also, are their any privacy implications? All I am trying to understand is how these users contribute.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-users" rel="tag" title="see questions tagged &#39;users&#39;">users</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '14, 14:11</strong></p>
<img src="https://secure.gravatar.com/avatar/ce2105c628f0492c916ba08fab8455d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vr3690&#39;s gravatar image" />
<p><span>vr3690</span><br />
<span class="score" title="66 reputation points">66</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vr3690 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Mar '14, 18:14</strong> </span></p>
</div>
</div>
<div id="comments-container-31423" class="comments-container">
&#10;</div>
<div id="comment-tools-31423" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31423-form-container" class="comment-form-container">
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

<span id="31424"></span>

<div id="answer-container-31424" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31424-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-31424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vr3690 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can extract this information from the <a href="http://wiki.openstreetmap.org/wiki/Planet.osm/full">Full History Planet dump</a>, but it will be a time- and resource-intensive exercise. Even then these dumps do not contain edits prior to October 2007 or redacted objects.</p>
<p>You should also be aware that some aspects of how people edit OSM can depend on the editor they're using.</p>
<p>It may be worth investigating the various user-related tools <a href="http://neis-one.org/">Pascal Neis</a> has developed (for example) before committing time and energy to building your own.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '14, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-31424" class="comments-container">
&#10;</div>
<div id="comment-tools-31424" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31424-form-container" class="comment-form-container">
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

