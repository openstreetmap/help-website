+++
type = "question"
title = "tile proxy 403 since today"
description = '''Since this night around 1:30 am german time my osm tile proxy server gets 403 responses from the osm tile servers. Strangely all wgets like wget https://c.tile.openstreetmap.org/17/88152/46772.png get the same 403 response also on other unrelated servers. The response is: https://c.tile.openstreetma...'''
date = "2022-04-29T10:23:00Z"
lastmod = "2022-04-29T13:13:00Z"
weight = 84301
keywords = [ "tile", "403", "proxy" ]
aliases = [ "/questions/84301" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tile proxy 403 since today](/questions/84301/tile-proxy-403-since-today)

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
<span id="post-84301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84301-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Since this night around 1:30 am german time my osm tile proxy server gets 403 responses from the osm tile servers. Strangely all wgets like</p>
<p>wget <a href="https://c.tile.openstreetmap.org/17/88152/46772.png">https://c.tile.openstreetmap.org/17/88152/46772.png</a></p>
<p>get the same 403 response also on other unrelated servers. The response is:</p>
<p><a href="https://c.tile.openstreetmap.org/17/88152/46772.png">https://c.tile.openstreetmap.org/17/88152/46772.png</a> Resolving c.tile.openstreetmap.org (c.tile.openstreetmap.org)... 2a04:4e42:3::649, 151.101.14.137 Connecting to c.tile.openstreetmap.org (c.tile.openstreetmap.org)|2a04:4e42:3::649|:443... connected. HTTP request sent, awaiting response... 403 Forbidden 2022-04-29 08:26:11 ERROR 403: Forbidden.</p>
<p>Where there any changes I'm not aware of? Does anyone have simular issus at the moment?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-403" rel="tag" title="see questions tagged &#39;403&#39;">403</span> <span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '22, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a21b2680362f989a4c0481be2bfd2739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swstoff&#39;s gravatar image" />
<p><span>swstoff</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swstoff has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84301" class="comments-container">
<span id="84303"></span>
<div id="comment-84303" class="comment">
<div id="post-84303-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you using a distinct, identifiable User-Agent for your requests, as required by the Tile Usage Policy?</p>
</div>
<div id="comment-84303-info" class="comment-info">
<span class="comment-age">(29 Apr '22, 12:16)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="84304"></span>
<div id="comment-84304" class="comment">
<div id="post-84304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, I do ... it worked for 2 years ... is there a way to check, if you are blocked? I did'nt find any.</p>
</div>
<div id="comment-84304-info" class="comment-info">
<span class="comment-age">(29 Apr '22, 12:26)</span> <span class="comment-user userinfo">swstoff</span>
</div>
</div>
<span id="84306"></span>
<div id="comment-84306" class="comment">
<div id="post-84306-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Quote: "...get the same 403 response also on other unrelated servers..." did you mean: on servers not related to OpenStreetMap? If that's the case, you'll have the problem somewhere in your network. Otherwise it's best to post all your request headers and OSMs response headers or the output of: 'wget <a href="https://tile.openstreetmap.org/cgi-bin/debug&#39;">https://tile.openstreetmap.org/cgi-bin/debug'</a> (with the User-Agent header you are using).</p>
</div>
<div id="comment-84306-info" class="comment-info">
<span class="comment-age">(29 Apr '22, 12:44)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-84301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84301-form-container" class="comment-form-container">
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

<span id="84307"></span>

<div id="answer-container-84307" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84307-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>when I used the user agent with wget, it did work corectly ... after finding nothing unsusual in the nginx log, i just restarted nginx and it worked again ... thats a bit embarrassing ... I guess I was fixated a bit to much on the wget call ... thanks for the help!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '22, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a21b2680362f989a4c0481be2bfd2739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swstoff&#39;s gravatar image" />
<p><span>swstoff</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swstoff has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '22, 13:14</strong> </span></p>
</div>
</div>
<div id="comments-container-84307" class="comments-container">
&#10;</div>
<div id="comment-tools-84307" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84307-form-container" class="comment-form-container">
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

