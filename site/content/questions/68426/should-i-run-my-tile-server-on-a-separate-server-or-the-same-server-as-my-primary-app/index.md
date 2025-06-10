+++
type = "question"
title = "Should I run my tile server on a separate server or the same server as my primary app?"
description = '''I am switching to OSM and will be hosting my own tile server. Some information about my tile server:  Covering only the southern part of Ontario. Bottom left position = {lat: 41.9, lng: -83.2}. Top right position = {lat: 47, lng: -74.2} Retina tiles (512 x 512) One style only (slightly modified vers...'''
date = "2019-03-19T19:24:00Z"
lastmod = "2019-03-20T02:01:00Z"
weight = 68426
keywords = [ "tiles", "tileserver" ]
aliases = [ "/questions/68426" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Should I run my tile server on a separate server or the same server as my primary app?](/questions/68426/should-i-run-my-tile-server-on-a-separate-server-or-the-same-server-as-my-primary-app)

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
<span id="post-68426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68426-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am switching to OSM and will be hosting my own tile server. Some information about my tile server:</p>
<ul>
<li>Covering only the southern part of Ontario. Bottom left position = {lat: 41.9, lng: -83.2}. Top right position = {lat: 47, lng: -74.2}</li>
<li>Retina tiles (512 x 512)</li>
<li>One style only (slightly modified version of OSM Bright)</li>
<li>Max zoom 18. Minimum zoom 10. All tiles from zoom 10 - 18 will be pre-rendered</li>
</ul>
<hr />
<p>The last design decision I need to make is where I should set up my tile server:</p>
<ol>
<li>On the same server as my primary application</li>
<li>On a separate server</li>
</ol>
<p>There are advantages and disadvantages to both. What is the conventional wisdom on this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '19, 19:24</strong></p>
<img src="https://secure.gravatar.com/avatar/b1e3fbb6f31c5e0144e7b18fcd7d5d33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valachio&#39;s gravatar image" />
<p><span>valachio</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valachio has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '19, 19:25</strong> </span></p>
</div>
</div>
<div id="comments-container-68426" class="comments-container">
&#10;</div>
<div id="comment-tools-68426" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68426-form-container" class="comment-form-container">
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

<span id="68427"></span>

<div id="answer-container-68427" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68427-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68427-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68427-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="valachio has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Pre-render your tiles on some cloud machine that you boot up just for the purpose, and then kill again. Transfer rendered tiles to your primary server and have them served by the local web server. This is provided you can do with something like weekly updates.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Mar '19, 20:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68427" class="comments-container">
<span id="68429"></span>
<div id="comment-68429" class="comment">
<div id="post-68429-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I need the tile server to be up for real-time rendering as well, for the extreme case that a user needs to render tiles outside my pre-defined area.</p>
</div>
<div id="comment-68429-info" class="comment-info">
<span class="comment-age">(19 Mar '19, 23:13)</span> <span class="comment-user userinfo">valachio</span>
</div>
</div>
<span id="68433"></span>
<div id="comment-68433" class="comment">
<div id="post-68433-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does that mean you want to have a world-wide database ready? Or just "all of Ontario" or "all of Canada" or...?</p>
</div>
<div id="comment-68433-info" class="comment-info">
<span class="comment-age">(19 Mar '19, 23:58)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="68434"></span>
<div id="comment-68434" class="comment">
<div id="post-68434-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>All of Ontario. I will be pre-rendering the southern part of Ontario (satisfies 99.9% of users). But some users may want to check out areas in Northern Ontario. I want the server to be ready to render those tiles if necessary.</p>
</div>
<div id="comment-68434-info" class="comment-info">
<span class="comment-age">(20 Mar '19, 00:09)</span> <span class="comment-user userinfo">valachio</span>
</div>
</div>
<span id="68435"></span>
<div id="comment-68435" class="comment">
<div id="post-68435-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In that case, if your primary server has (or can be made to have) the necessary SSD capacity for the database and the other tasks running there do not compete too much with updates and pre-rendering, I'd install everything on one server for simplicity.</p>
</div>
<div id="comment-68435-info" class="comment-info">
<span class="comment-age">(20 Mar '19, 00:18)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="68437"></span>
<div id="comment-68437" class="comment">
<div id="post-68437-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your advice</p>
</div>
<div id="comment-68437-info" class="comment-info">
<span class="comment-age">(20 Mar '19, 02:01)</span> <span class="comment-user userinfo">valachio</span>
</div>
</div>
</div>
<div id="comment-tools-68427" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68427-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

