+++
type = "question"
title = "How to block tiles for some users?"
description = '''For past two days some user started bulk downloading tiles from my server. The tile cache quickly eaten up all the disk space. I&#x27;ve blocked that user with iptables, but now wondering if that can be done a) automatically, b) not by physically blocking them, but by replacing tiles with an error tile &quot;...'''
date = "2015-01-23T13:31:00Z"
lastmod = "2015-01-23T13:50:00Z"
weight = 40563
keywords = [ "apache", "tileserver", "blocking", "mod_tile" ]
aliases = [ "/questions/40563" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to block tiles for some users?](/questions/40563/how-to-block-tiles-for-some-users)

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
<span id="post-40563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40563-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-40563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For past two days some user started bulk downloading tiles from my server. The tile cache quickly eaten up all the disk space. I've blocked that user with iptables, but now wondering if that can be done a) automatically, b) not by physically blocking them, but by replacing tiles with an error tile "you're doing it wrong, contact admin". Is there such option in mod_tile? How it is done on osm.org?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-blocking" rel="tag" title="see questions tagged &#39;blocking&#39;">blocking</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jan '15, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/5cbbf1cf884c2145026c237aaed80dde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zverik&#39;s gravatar image" />
<p><span>Zverik</span><br />
<span class="score" title="613 reputation points">613</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zverik has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-40563" class="comments-container">
&#10;</div>
<div id="comment-tools-40563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40563-form-container" class="comment-form-container">
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

<span id="40564"></span>

<div id="answer-container-40564" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40564-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-40564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Zverik has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>mod_tile has a built-in throttling capability (see demo config file which explains things) where you can slow down tile delivery for IP numbers that ask for too much. The general approach is usingh buckets and top-up rates, i.e. any IP gets an allowance of X tiles initially but then their "bucket" is empty and only fills up again at a predefined rate. You can can even differentiate between tiles that are already there (allow more of those) and tiles that have to be freshly computed (make them reeeealllyy slow). There's no way to switch to an error tile automatically though, I believe.</p>
<p>You an also use fail2ban which would by default simply kill the IP with iptables, but can also be made to re-route the requests to port 81 or so, where you'd have a simple web server that only ever hands out an error tile.</p>
<p>As far as I know, osm.org uses a technique similar to that mod_tile offers, but it runs on the proxy level i.e. before the requests even reach mod_tile.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '15, 13:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jan '15, 13:50</strong> </span></p>
</div>
</div>
<div id="comments-container-40564" class="comments-container">
&#10;</div>
<div id="comment-tools-40564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40564-form-container" class="comment-form-container">
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

