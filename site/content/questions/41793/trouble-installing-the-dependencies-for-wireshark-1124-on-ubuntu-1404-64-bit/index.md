+++
type = "question"
title = "Trouble installing the dependencies for wireshark 1.12.4 on Ubuntu 14.04 64-bit"
description = '''Hi, I&#x27;ve run apt-get build-dep wireshark several times and it errors out. here is my progress (abbreviated, of course!) sue@SuesPhoenix:~/Programs$ sudo apt-get build-dep wireshark Reading package lists... Done Building dependency tree  Reading state information... Done Note, selecting &#x27;libcap-dev&#x27; ...'''
date = "2015-04-24T10:04:00Z"
lastmod = "2015-04-28T12:19:00Z"
weight = 41793
keywords = [ "dependencies", "ubuntu" ]
aliases = [ "/questions/41793" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trouble installing the dependencies for wireshark 1.12.4 on Ubuntu 14.04 64-bit](/questions/41793/trouble-installing-the-dependencies-for-wireshark-1124-on-ubuntu-1404-64-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41793-score" class="post-score" title="current number of votes">0</div><span id="post-41793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've run apt-get build-dep wireshark several times and it errors out. here is my progress (abbreviated, of course!)</p><pre><code>[email protected]:~/Programs$ sudo apt-get build-dep wireshark
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Note, selecting &#39;libcap-dev&#39; instead of &#39;libcap2-dev&#39;
The following packages have unmet dependencies:
libgnutls-dev : Depends: libgnutls-openssl27 (= 2.12.23-12ubuntu2.2) but 3.2.16-1u1~ppa2 is to be installed
E: Build-dependencies for wireshark could not be satisfied.
[email protected]:~/Programs$ sudo apt-get build-dep libgnutls-dev
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Picking &#39;gnutls26&#39; as source package instead of &#39;libgnutls-dev&#39;
0 upgraded, 0 newly installed, 0 to remove and 110 not upgraded.
[email protected]:~/Programs$</code></pre><p>Seems to have me stuck. What do I do to get the wireshark dependencies successfully installed?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dependencies" rel="tag" title="see questions tagged &#39;dependencies&#39;">dependencies</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '15, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/33b8ab9f5cef32ec9ebc6c7df0126498?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GuruSue&#39;s gravatar image" /><p><span>GuruSue</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GuruSue has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Apr '15, 16:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-41793" class="comments-container"><span id="41799"></span><div id="comment-41799" class="comment"><div id="post-41799-score" class="comment-score"></div><div class="comment-text"><p>Oh yeah, and my customized Ubuntu installation (desktop wallpaper, launcher icons for frequently used programs, other fun stuff like that) have all be reset to plain vanilla Trusty Tahir install. YUCK!</p></div><div id="comment-41799-info" class="comment-info"><span class="comment-age">(24 Apr '15, 12:40)</span> <span class="comment-user userinfo">GuruSue</span></div></div><span id="41804"></span><div id="comment-41804" class="comment"><div id="post-41804-score" class="comment-score"></div><div class="comment-text"><p>and can no longer be edited. Here's the error when trying to reset the ability to set the settings:</p><pre><code>[email protected]:~$ gsettings set org.gnome.settings-daemon.plugins.background active true

GLib-GIO-Message: Using the &#39;memory&#39; GSettings backend.  Your settings will not be saved or shared with other applications.
[email protected]:~$</code></pre></div><div id="comment-41804-info" class="comment-info"><span class="comment-age">(24 Apr '15, 15:55)</span> <span class="comment-user userinfo">GuruSue</span></div></div></div><div id="comment-tools-41793" class="comment-tools"></div><div class="clear"></div><div id="comment-41793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41929"></span>

<div id="answer-container-41929" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41929-score" class="post-score" title="current number of votes">0</div><span id="post-41929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you try: sudo apt-get install qt4-default</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '15, 12:19</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-41929" class="comments-container"></div><div id="comment-tools-41929" class="comment-tools"></div><div class="clear"></div><div id="comment-41929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

