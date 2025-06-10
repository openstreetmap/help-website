+++
type = "question"
title = "How to change JOSM imagery.generic.minimum_expires but just for one imagery?"
description = '''I can set this JOSM Advanced Preference, tag key=&quot;imagery.generic.minimum_expires&quot; value=&quot;3600000000&quot;  But I don&#x27;t want to do it for all imagery. I only want to do it for the ABC imagery from the XYZ server. How to? You see there is this horrible server that is wastefully responding  HTTP/1.1 200 OK...'''
date = "2018-02-19T07:33:00Z"
lastmod = "2018-02-22T12:19:00Z"
weight = 62203
keywords = [ "josm", "cache", "preferences", "expiry" ]
aliases = [ "/questions/62203" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to change JOSM imagery.generic.minimum_expires but just for one imagery?](/questions/62203/how-to-change-josm-imagerygenericminimum_expires-but-just-for-one-imagery)

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
<span id="post-62203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62203-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can set this JOSM Advanced Preference,</p>
<pre><code>tag key=&quot;imagery.generic.minimum_expires&quot; value=&quot;3600000000&quot;</code></pre>
<p>But I don't want to do it for all imagery. I only want to do it for the ABC imagery from the XYZ server. How to?</p>
<p>You see there is this horrible server that is wastefully responding</p>
<pre><code> HTTP/1.1 200 OK
 Cache-Control: no-cache
 Pragma: no-cache
 Expires: -1</code></pre>
<p>while everybody knows the cadastral maps it serves won't change for years and years, so I don't want JOSM to bother to attempt to refresh them every hour whenever I browse them.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-cache" rel="tag" title="see questions tagged &#39;cache&#39;">cache</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span> <span class="post-tag tag-link-expiry" rel="tag" title="see questions tagged &#39;expiry&#39;">expiry</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '18, 07:33</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62203" class="comments-container">
&#10;</div>
<div id="comment-tools-62203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62203-form-container" class="comment-form-container">
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

<span id="62208"></span>

<div id="answer-container-62208" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62208-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There doesn't seem to be an imagery configuration parameter for this (see <a href="https://josm.openstreetmap.de/wiki/Maps#Documentation">https://josm.openstreetmap.de/wiki/Maps#Documentation</a> ) so the answer is simply: you can't.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '18, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-62208" class="comments-container">
<span id="62266"></span>
<div id="comment-62266" class="comment">
<div id="post-62266-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK thanks. Submitted <a href="https://josm.openstreetmap.de/ticket/16000">https://josm.openstreetmap.de/ticket/16000</a> .</p>
</div>
<div id="comment-62266-info" class="comment-info">
<span class="comment-age">(22 Feb '18, 12:19)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
</div>
<div id="comment-tools-62208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62208-form-container" class="comment-form-container">
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

