+++
type = "question"
title = "Copy operation timed out while rendering vector tiles"
description = '''Hi, Got below error while rendering vector tiles for 6th or above zoom levels. Error: Copy operation timed out  at Timeout.&amp;lt;anonymous&amp;gt; (/usr/local/lib/node_modules/tilelive/lib/tilelive.js:390.22)  at Timeout.wrapper (timer.js:408:11) at tryOnTimeOut (timer.js:224:11)  at Timer.listOnTimeout (...'''
date = "2017-06-29T11:23:00Z"
lastmod = "2017-07-04T08:48:00Z"
weight = 56799
keywords = [ "mbtiles", "rendering", "tiles", "vector", "tileserver" ]
aliases = [ "/questions/56799" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Copy operation timed out while rendering vector tiles](/questions/56799/copy-operation-timed-out-while-rendering-vector-tiles)

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
<span id="post-56799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56799-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Got below error while rendering vector tiles for 6th or above zoom levels.</p>
<p><strong>Error: Copy operation timed out<br />
at Timeout.&lt;anonymous&gt; (/usr/local/lib/node_modules/tilelive/lib/tilelive.js:390.22)<br />
at Timeout.wrapper (timer.js:408:11) at tryOnTimeOut (timer.js:224:11)<br />
at Timer.listOnTimeout (timer.js:198:5)</strong></p>
<p>Command executing that time:</p>
<p><strong>/usr/local/bin/tilelive-copy —scheme=pyramid —bounds=-180, -85, 180, 85 —timeout=1800000 —minzoom=4 —maxzoom=6 <span>tmsource://tmp/project</span> mbtiles:///data/export/tiles.mbtiles</strong></p>
<p>Kindly help us to solve this issue.</p>
<p>Note: Searched in google &amp; got this unanswered issue from git:<br />
<a href="https://github.com/mapbox/tilelive/issues/158">https://github.com/mapbox/tilelive/issues/158</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mbtiles" rel="tag" title="see questions tagged &#39;mbtiles&#39;">mbtiles</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jun '17, 11:23</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '17, 11:27</strong> </span></p>
</div>
</div>
<div id="comments-container-56799" class="comments-container">
&#10;</div>
<div id="comment-tools-56799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56799-form-container" class="comment-form-container">
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

<span id="56800"></span>

<div id="answer-container-56800" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56800-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rajavelu_M has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I believe you have already found the answer: you need to either ask or potentially pay MapBox to fix the issue or fix it yourself <a href="https://github.com/mapbox/tilelive/issues">https://github.com/mapbox/tilelive/issues</a> You are using OSS that the authors and maintainers don't seem to be willing to maintain outside of their own needs and don't want to provide free support for, but given that it is OSS you can either investigate and fix the issue yourself or pay somebody to do so, completely without involving MapBox at all.</p>
<p><a href="https://en.wikipedia.org/wiki/There_ain%27t_no_such_thing_as_a_free_lunch">TANSTAAFL</a>.</p>
<p>Now if this was community developed and/or maintained software the situation would be slightly different.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '17, 11:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '17, 14:50</strong> </span></p>
</div>
</div>
<div id="comments-container-56800" class="comments-container">
&#10;</div>
<div id="comment-tools-56800" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56800-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56854"></span>

<div id="answer-container-56854" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56854-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your command has a <code>timeout</code> of 30 minutes, which should be very long for one tile, however maybe you have a really really complicated &amp; slow to render project/style. Does the timeout happen after ~ 30 minutes or does it happen after less than 30 minutes? One approach could be to increase the timeout ever more. Or you can improve your style. Maybe you're missing some database indexes which might make it go faster.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '17, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-56854" class="comments-container">
<span id="56870"></span>
<div id="comment-56870" class="comment">
<div id="post-56870-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/30/rorym">@rorym</a>: This timeout happening after 5 minutes.</p>
</div>
<div id="comment-56870-info" class="comment-info">
<span class="comment-age">(04 Jul '17, 06:02)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="56874"></span>
<div id="comment-56874" class="comment">
<div id="post-56874-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh that doesn't sound right then. Sorry I don't know how to help, unless you dive into the javascript source code.</p>
</div>
<div id="comment-56874-info" class="comment-info">
<span class="comment-age">(04 Jul '17, 08:48)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
</div>
<div id="comment-tools-56854" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56854-form-container" class="comment-form-container">
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

