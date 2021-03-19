+++
type = "question"
title = "Slackware 64bit  Segmentation fault with wireshark-1.10.0"
description = '''I just built and installed wireshark-1.10.0 (as root) It compiled normally with a few typical warnings. When I run it (as root) I get a Segmentation fault When I debug with gdb I get the following backtrace Program received signal SIGSEGV, Segmentation fault. 0x00007ffff14839fe in genl_register () f...'''
date = "2013-06-14T15:24:00Z"
lastmod = "2013-07-29T12:03:00Z"
weight = 22075
keywords = [ "64bit", "slackware" ]
aliases = [ "/questions/22075" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slackware 64bit Segmentation fault with wireshark-1.10.0](/questions/22075/slackware-64bit-segmentation-fault-with-wireshark-1100)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22075-score" class="post-score" title="current number of votes">0</div><span id="post-22075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just built and installed wireshark-1.10.0 (as root) It compiled normally with a few typical warnings.</p><p>When I run it (as root) I get a Segmentation fault</p><p>When I debug with gdb I get the following backtrace</p><pre><code>Program received signal SIGSEGV, Segmentation fault.
0x00007ffff14839fe in genl_register () from /usr/lib64/libnl-genl-3.so.200
(gdb) bt 10
#0 0x00007ffff14839fe in genl_register () from /usr/lib64/libnl-genl-3.so.200
#1 0x00007fffefdda716 in ?? () from /usr/lib64/libnl.so.1
#2 0x0000000000000000 in ?? ()
(gdb)</code></pre><p>I updated libnl to 3.2.22 (the latest I could find) no change</p><p>Any ideas???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-64bit" rel="tag" title="see questions tagged &#39;64bit&#39;">64bit</span> <span class="post-tag tag-link-slackware" rel="tag" title="see questions tagged &#39;slackware&#39;">slackware</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '13, 15:24</strong></p><img src="https://secure.gravatar.com/avatar/485a88133be8366f8ed700251fa2b9ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tolip&#39;s gravatar image" /><p><span>tolip</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tolip has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '13, 18:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-22075" class="comments-container"></div><div id="comment-tools-22075" class="comment-tools"></div><div class="clear"></div><div id="comment-22075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23428"></span>

<div id="answer-container-23428" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23428-score" class="post-score" title="current number of votes">0</div><span id="post-23428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is, apparently, a problem between libpcap linking to one version of libnl and Wireshark linking against a different version.</p><p>./configure --without-libnl</p><p>will make the problem go away. I'm not sure if there's a better fix.</p><p>See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7808">bug 7808</a> for details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '13, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-23428" class="comments-container"></div><div id="comment-tools-23428" class="comment-tools"></div><div class="clear"></div><div id="comment-23428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

