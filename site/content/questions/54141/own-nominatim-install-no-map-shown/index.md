+++
type = "question"
title = "Own Nominatim install, no map shown"
description = '''I just created a Nominatim server. Everything seemed to have gone OK, and I can lookup addresses. The result is the details of the address, but no map of the address gets shown. Also when you click the reverse lookup link, all you get is an empty page. Note though that reverse lookup using an xml qu...'''
date = "2017-01-18T13:42:00Z"
lastmod = "2017-01-18T15:00:00Z"
weight = 54141
keywords = [ "nominatim" ]
aliases = [ "/questions/54141" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Own Nominatim install, no map shown](/questions/54141/own-nominatim-install-no-map-shown)

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
<span id="post-54141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54141-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just created a Nominatim server. Everything seemed to have gone OK, and I can lookup addresses. The result is the details of the address, but no map of the address gets shown. Also when you click the reverse lookup link, all you get is an empty page. Note though that reverse lookup using an xml query works!)</p>
<p>Any ideas what is wrong?</p>
<p>The main Nominatim page can be found at: <a href="http://54.200.226.228/nominatim/.">http://54.200.226.228/nominatim/.</a> Sample reverse xml lookup: <a href="http://54.200.226.228/nominatim/reverse.php?format=xml&amp;lat=41.8905556&amp;lon=12.4883333&amp;zoom=18&amp;addressdetails=1">http://54.200.226.228/nominatim/reverse.php?format=xml&amp;lat=41.8905556&amp;lon=12.4883333&amp;zoom=18&amp;addressdetails=1</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '17, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/fcc569efc617a6f5dcb0ae7da98c4042?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hayo%20Baan&#39;s gravatar image" />
<p><span>Hayo Baan</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hayo Baan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '17, 13:43</strong> </span></p>
</div>
</div>
<div id="comments-container-54141" class="comments-container">
&#10;</div>
<div id="comment-tools-54141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54141-form-container" class="comment-form-container">
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

<span id="54142"></span>

<div id="answer-container-54142" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54142-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hayo Baan has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think that gets caused by the line <code>json_encode($aNominatimMapInit, JSON_PRETTY_PRINT)</code> in <code>lib/template/search-html.php</code>. It returns an empty string, at least I don't seen any output in the HTML in my browser.</p>
<p>The option JSON_PRETTY_PRINT got added in PHP version 5.4.0. Are you running a PHP version older than that?</p>
<p>Do you see any error message in the webserver (nginx) error log?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '17, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-54142" class="comments-container">
<span id="54145"></span>
<div id="comment-54145" class="comment">
<div id="post-54145-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Awesome!!! That was it! The system is was on 5.3.29 as that was the version that I got with installing php-pgsql. However, I'm now using php56-pgsql and all is working fine (after some effort in getting it configured right).</p>
<p>THANKS!</p>
</div>
<div id="comment-54145-info" class="comment-info">
<span class="comment-age">(18 Jan '17, 15:00)</span> <span class="comment-user userinfo">Hayo Baan</span>
</div>
</div>
</div>
<div id="comment-tools-54142" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54142-form-container" class="comment-form-container">
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

