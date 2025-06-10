+++
type = "question"
title = "Altitude attribute"
description = '''Hi, Does the altitude attribute represents a relative altitude? If I have a tunnel below a railroad, should I set altitude to -1? Thanks!'''
date = "2016-04-08T14:25:00Z"
lastmod = "2016-04-08T19:11:00Z"
weight = 49109
keywords = [ "attributes", "altitude" ]
aliases = [ "/questions/49109" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Altitude attribute](/questions/49109/altitude-attribute)

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
<span id="post-49109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49109-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Does the altitude attribute represents a relative altitude?</p>
<p>If I have a tunnel below a railroad, should I set altitude to -1?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span> <span class="post-tag tag-link-altitude" rel="tag" title="see questions tagged &#39;altitude&#39;">altitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '16, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/8b0c918db549ea2308a5fc7b4edbb2ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GranBarba&#39;s gravatar image" />
<p><span>GranBarba</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GranBarba has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>12 Apr '16, 09:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/390c3a1e9ea7b1f10deea61828ad66eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lightsider&#39;s gravatar image" />
<p><span>Lightsider</span><br />
<span class="score" title="1540 reputation points"><span>1.5k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span></p>
</div>
</div>
<div id="comments-container-49109" class="comments-container">
<span id="49110"></span>
<div id="comment-49110" class="comment">
<div id="post-49110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What altitude attribute are you talking about exactly? Can you give us the name of the tag key?</p>
</div>
<div id="comment-49110-info" class="comment-info">
<span class="comment-age">(08 Apr '16, 15:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="49119"></span>
<div id="comment-49119" class="comment">
<div id="post-49119-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The name in spanish is "altitud"</p>
</div>
<div id="comment-49119-info" class="comment-info">
<span class="comment-age">(08 Apr '16, 19:11)</span> <span class="comment-user userinfo">GranBarba</span>
</div>
</div>
</div>
<div id="comment-tools-49109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49109-form-container" class="comment-form-container">
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

<span id="49111"></span>

<div id="answer-container-49111" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49111-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-49111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GranBarba has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tunnel under the railroad should probably be marked as <a href="http://wiki.openstreetmap.org/wiki/Key:layer">layer=-1</a>. Sometimes it will be a different value for the layer, but the usual tunnel will be <code>-1</code>.</p>
<p>Altitude is usually stored in the <a href="http://wiki.openstreetmap.org/wiki/Key:ele">ele</a> key (short for elevation). It should probably only be used on a limited set of objects where the elevation is well determined (things like mountain peaks). In general combining OSM data with separate elevation data is a better approach than adding elevations of various accuracies and sources to objects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '16, 15:07</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Apr '16, 15:16</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span></p>
</div>
</div>
<div id="comments-container-49111" class="comments-container">
<span id="49118"></span>
<div id="comment-49118" class="comment">
<div id="post-49118-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, Vincent and Max!</p>
</div>
<div id="comment-49118-info" class="comment-info">
<span class="comment-age">(08 Apr '16, 19:09)</span> <span class="comment-user userinfo">GranBarba</span>
</div>
</div>
</div>
<div id="comment-tools-49111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49111-form-container" class="comment-form-container">
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

