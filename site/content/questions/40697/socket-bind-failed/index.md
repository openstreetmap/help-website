+++
type = "question"
title = "Socket bind Failed"
description = '''while working with tile server on ubuntu 14.04 at time of manually building the tile server at the time of rendering applying the following command   sudo -u username renderd -f -c /usr/local/etc/renderd.conf   Can anyone suggest me ? actually its working on my local server but when i run it on my e...'''
date = "2015-01-29T17:51:00Z"
lastmod = "2015-01-30T08:31:00Z"
weight = 40697
keywords = [ "openstreetmap", "rendering", "switch2osm", "socket", "mapnik" ]
aliases = [ "/questions/40697" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Socket bind Failed](/questions/40697/socket-bind-failed)

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
<span id="post-40697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40697-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>while working with tile server on ubuntu 14.04 at time of manually building the tile server at the time of rendering applying the following command sudo -u username renderd -f -c /usr/local/etc/renderd.conf <img src="/upfiles/Screenshot_from_2015-01-29_23:18:03.png" alt="alt text" /></p>
<p>Can anyone suggest me ? actually its working on my local server but when i run it on my experimental server its shows " SOCKET BIND FAIL "</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-socket" rel="tag" title="see questions tagged &#39;socket&#39;">socket</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '15, 17:51</strong></p>
<img src="https://secure.gravatar.com/avatar/5706d861b862cb83624a28e2b862937e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RAMNEEK%20PAUL%20SINGH&#39;s gravatar image" />
<p><span>RAMNEEK PAUL...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RAMNEEK PAUL SINGH has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-40697" class="comments-container">
<span id="40707"></span>
<div id="comment-40707" class="comment">
<div id="post-40707-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><del>I've never set up renderd but are you trying to bind as a regular user to a port only root can bind to?</del> (nevermind, it's an UNIX domain socket). And please don't post screenshots if you have text error messages, otherwise it makes it harder for other users to search for the same problem.</p>
</div>
<div id="comment-40707-info" class="comment-info">
<span class="comment-age">(30 Jan '15, 07:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40697-form-container" class="comment-form-container">
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

<span id="40710"></span>

<div id="answer-container-40710" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40710-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Make sure the directory <code>/var/rund/renderd</code> actually exists and is writable for the user you are running renderd under.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '15, 08:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-40710" class="comments-container">
&#10;</div>
<div id="comment-tools-40710" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40710-form-container" class="comment-form-container">
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

