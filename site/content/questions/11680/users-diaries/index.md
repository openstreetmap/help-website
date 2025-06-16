+++
type = "question"
title = "Users&#x27; diaries"
description = '''Why does &#x27;Users&#x27; Diaries&#x27; no longer appear as a heading alongside &#x27;View&#x27;, &#x27;Edit&#x27;, &#x27;History&#x27;, &#x27;Export&#x27; and &#x27;GPS Traces&#x27; at https://www.openstreetmap.org/index.html?'''
date = "2012-04-01T15:43:00Z"
lastmod = "2012-04-01T17:02:00Z"
weight = 11680
keywords = [ "map", "main", "osm", "online" ]
aliases = [ "/questions/11680" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Users' diaries](/questions/11680/users-diaries)

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
<span id="post-11680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11680-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Why does 'Users' Diaries' no longer appear as a heading alongside 'View', 'Edit', 'History', 'Export' and 'GPS Traces' at <a href="https://www.openstreetmap.org/index.html?">https://www.openstreetmap.org/index.html?</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-main" rel="tag" title="see questions tagged &#39;main&#39;">main</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-online" rel="tag" title="see questions tagged &#39;online&#39;">online</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '12, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/ffcc41f13929627742b4936ec178c6f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silver%20mapper&#39;s gravatar image" />
<p><span>silver mapper</span><br />
<span class="score" title="256 reputation points">256</span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silver mapper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11680" class="comments-container">
&#10;</div>
<div id="comment-tools-11680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11680-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="11681"></span>

<div id="answer-container-11681" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11681-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can view a change log of the web site source code here:</p>
<p><a href="https://github.com/openstreetmap/openstreetmap-website/commits/master">https://github.com/openstreetmap/openstreetmap-website/commits/master</a></p>
<p>You will find that the change in question has been coded by Tom MacWright here:</p>
<p><a href="https://github.com/openstreetmap/openstreetmap-website/commit/ae8cc604a1b7477a79f505592942c2d754825bc1">https://github.com/openstreetmap/openstreetmap-website/commit/ae8cc604a1b7477a79f505592942c2d754825bc1</a></p>
<p>His reason (taken from an earlier commit that was intended to remove the tab) was:</p>
<pre><code>This eliminates the user diaries tab. I&#39;ve never understood
why it was there, and think it is of limited utility
given that it displays diary entries in all languages
at once, and user diaries aren&#39;t the centerpiece of the site.</code></pre>
<p>Such changes are usually discussed on the <a href="http://lists.openstreetmap.org/listinfo/rails-dev">rails-dev list</a> so if you want to suggest an alternative, that would be a good place for that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '12, 16:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-11681" class="comments-container">
&#10;</div>
<div id="comment-tools-11681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11681-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11683"></span>

<div id="answer-container-11683" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11683-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Note there is now a link to 'User Diaries' in the left-hand sidebar, under the section for 'Community'.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '12, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-11683" class="comments-container">
<span id="11684"></span>
<div id="comment-11684" class="comment">
<div id="post-11684-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which is somewhat redundant, because the 'Blogs' page linked in the same section also includes all user diary posts.</p>
</div>
<div id="comment-11684-info" class="comment-info">
<span class="comment-age">(01 Apr '12, 17:02)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-11683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11683-form-container" class="comment-form-container">
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

