+++
type = "question"
title = "I am receiving a blank page (HTTP/1.1 400 Bad Request) after requesting a data export"
description = '''Dear Sir, Since yesterday I am receiving a blank page after requesting a data export. The web console gives me the following message:  [09:40:49.306] GET http://api.openstreetmap.org/api/0.6/map?bbox=15.181,-4.4888,15.602,-4.143 [HTTP/1.1 400 Bad Request 1010ms] '''
date = "2013-08-22T08:48:00Z"
lastmod = "2013-08-22T17:51:00Z"
weight = 25637
keywords = [ "osm", "export", "data" ]
aliases = [ "/questions/25637" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I am receiving a blank page (HTTP/1.1 400 Bad Request) after requesting a data export](/questions/25637/i-am-receiving-a-blank-page-http11-400-bad-request-after-requesting-a-data-export)

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
<span id="post-25637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25637-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear Sir,</p>
<p>Since yesterday I am receiving a blank page after requesting a data export. The web console gives me the following message:</p>
<blockquote>
<p>[09:40:49.306] GET <a href="http://api.openstreetmap.org/api/0.6/map?bbox=15.181,-4.4888,15.602,-4.143">http://api.openstreetmap.org/api/0.6/map?bbox=15.181,-4.4888,15.602,-4.143</a> [HTTP/1.1 400 Bad Request 1010ms]</p>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '13, 08:48</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2a6e9bee55de2182a0803ace7105b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paulin%20Bekambo&#39;s gravatar image" />
<p><span>Paulin Bekambo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paulin Bekambo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '13, 14:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-25637" class="comments-container">
&#10;</div>
<div id="comment-tools-25637" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25637-form-container" class="comment-form-container">
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

<span id="25660"></span>

<div id="answer-container-25660" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25660-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Likely the area you selected is too big ("bad request"; same for me). Try a smaller area, e.g: <a href="http://api.openstreetmap.org/api/0.6/map?bbox=15.55,-4.24,15.56,-4.23">http://api.openstreetmap.org/api/0.6/map?bbox=15.55,-4.24,15.56,-4.23</a> . Background: The export feature needs much processing power, which our servers are short of (just donated resources!). It could be that it works during a low load time (see <a href="http://munin.openstreetmap.org/openstreetmap/thorn-01.openstreetmap/load.html">graph</a>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '13, 14:24</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '13, 14:37</strong> </span></p>
</div>
</div>
<div id="comments-container-25660" class="comments-container">
<span id="25667"></span>
<div id="comment-25667" class="comment">
<div id="post-25667-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... or try alternatively <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">http://wiki.openstreetmap.org/wiki/Overpass_API</a></p>
</div>
<div id="comment-25667-info" class="comment-info">
<span class="comment-age">(22 Aug '13, 17:51)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-25660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25660-form-container" class="comment-form-container">
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

