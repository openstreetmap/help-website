+++
type = "question"
title = "JMapViewer checkout problem"
description = '''Hi all. I am trying to checkout JMapViewer project, doing like this: svn co http://svn.openstreetmap.org/applications/viewer/jmapviewer jmapviewer  but I get an error: svn:Server sent unexpected return value (400 Malformed Request) in response to REPORT request for &#x27;/!svn/vcc/default&#x27;  What am I doi...'''
date = "2012-05-10T17:32:00Z"
lastmod = "2012-05-15T09:06:00Z"
weight = 12659
keywords = [ "jmapviewer", "java", "checkout" ]
aliases = [ "/questions/12659" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JMapViewer checkout problem](/questions/12659/jmapviewer-checkout-problem)

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
<span id="post-12659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12659-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all. I am trying to checkout JMapViewer project, doing like this:</p>
<pre><code>svn co http://svn.openstreetmap.org/applications/viewer/jmapviewer jmapviewer</code></pre>
<p>but I get an error:</p>
<pre><code>svn:Server sent unexpected return value (400 Malformed Request) in response to REPORT request for &#39;/!svn/vcc/default&#39;</code></pre>
<p>What am I doing wrong? Thank you very much in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-jmapviewer" rel="tag" title="see questions tagged &#39;jmapviewer&#39;">jmapviewer</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-checkout" rel="tag" title="see questions tagged &#39;checkout&#39;">checkout</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '12, 17:32</strong></p>
<img src="https://secure.gravatar.com/avatar/9c1fedf457d99dba83a94061550ab814?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pau-osm&#39;s gravatar image" />
<p><span>pau-osm</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pau-osm has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 May '12, 17:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ec2962c6ef6aab7940982ed25f2ca544?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheOddOne2&#39;s gravatar image" />
<p><span>TheOddOne2</span><br />
<span class="score" title="685 reputation points">685</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span></p>
</div>
</div>
<div id="comments-container-12659" class="comments-container">
&#10;</div>
<div id="comment-tools-12659" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12659-form-container" class="comment-form-container">
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

<span id="12665"></span>

<div id="answer-container-12665" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12665-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pau-osm has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Checkout works ok for me and I am unable to find any errors on the svn server.</p>
<p>Likely the issue is cause by a (ISP?) proxy which is unable to parse WebDAV requests.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '12, 11:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
</div>
<div id="comments-container-12665" class="comments-container">
<span id="12739"></span>
<div id="comment-12739" class="comment">
<div id="post-12739-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much and - yes, this is an ISP problem (settings)</p>
</div>
<div id="comment-12739-info" class="comment-info">
<span class="comment-age">(15 May '12, 09:06)</span> <span class="comment-user userinfo">pau-osm</span>
</div>
</div>
</div>
<div id="comment-tools-12665" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12665-form-container" class="comment-form-container">
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

