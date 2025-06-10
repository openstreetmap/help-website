+++
type = "question"
title = "Error: Authorization request failed"
description = '''Hello, When trying to connect to my OpenStreetMap account from Gnome Maps on Linux Mint 20.3 Una, it give me that error: &quot;Authorization request failed&quot;  I tried to close and relaunch the app and also I do tried a new account without any success. What I need to do to be able to login? Best regards,  ...'''
date = "2022-07-07T05:19:00Z"
lastmod = "2022-07-08T07:24:00Z"
weight = 84994
keywords = [ "maps", "linux" ]
aliases = [ "/questions/84994" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Error: Authorization request failed](/questions/84994/error-authorization-request-failed)

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
<span id="post-84994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84994-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>When trying to connect to my OpenStreetMap account from Gnome Maps on Linux Mint 20.3 Una, it give me that error:</p>
<p>"Authorization request failed"</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_at_2022-07-07_00-10-05.png" alt="alt text" /></p>
<p>I tried to close and relaunch the app and also I do tried a new account without any success.</p>
<p>What I need to do to be able to login?</p>
<p>Best regards,</p>
<p>Guillaume</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maps" rel="tag" title="see questions tagged &#39;maps&#39;">maps</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '22, 05:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a71b275b178c14233094da96da40e533?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guillaumesoucy&#39;s gravatar image" />
<p><span>guillaumesoucy</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guillaumesoucy has one accepted answer">100%</span></p>
</img>
</div>
</div>
<div id="comments-container-84994" class="comments-container">
<span id="85004"></span>
<div id="comment-85004" class="comment">
<div id="post-85004-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is probably a gnome maps issue, have you checked <a href="https://gitlab.gnome.org/GNOME/gnome-maps/-/issues">https://gitlab.gnome.org/GNOME/gnome-maps/-/issues</a> ?</p>
</div>
<div id="comment-85004-info" class="comment-info">
<span class="comment-age">(07 Jul '22, 19:57)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84994-form-container" class="comment-form-container">
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

<span id="85008"></span>

<div id="answer-container-85008" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85008-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>After looking at their GitLab, the issues was fixed in a update.</p>
<p>I'm running a outdated version of Gnome Maps.</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_at_2022-07-07_16-57-11.png" alt="alt text" /></p>
<p>The version from the repos that Linux Mint is using seem to be outdated:</p>
<pre><code>root@workstation-dc:/home/guillaumesoucy# apt-get install gnome-maps
Reading package lists... Done
Building dependency tree       
Reading state information... Done
gnome-maps is already the newest version (3.38.2-1).
0 upgraded, 0 newly installed, 0 to remove and 3 not upgraded.</code></pre>
<p>In that case, how I can get the latest version?</p>
<p>With regards,</p>
<p>Guillaume</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '22, 22:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a71b275b178c14233094da96da40e533?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guillaumesoucy&#39;s gravatar image" />
<p><span>guillaumesoucy</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guillaumesoucy has one accepted answer">100%</span></p>
</img>
</div>
</div>
<div id="comments-container-85008" class="comments-container">
&#10;</div>
<div id="comment-tools-85008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85008-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85009"></span>

<div id="answer-container-85009" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85009-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, Have a look here:- <a href="https://flathub.org/apps/details/org.gnome.Maps">https://flathub.org/apps/details/org.gnome.Maps</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '22, 07:24</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-85009" class="comments-container">
&#10;</div>
<div id="comment-tools-85009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85009-form-container" class="comment-form-container">
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

