+++
type = "question"
title = "unable to upgrade to wireshark 1.6"
description = '''I&#x27;ve downloaded(http://www.wireshark.org/download/src/all-versions/wireshark-1.6.0rc2.tar.bz2) and performed the following steps, I still see version 1.2 instead of 1.6. Please advise if any step is missing to upgrade my wireshark to 1.6 version.  ./configure make make install  I didn&#x27;t find any iss...'''
date = "2011-06-10T07:43:00Z"
lastmod = "2011-06-10T09:07:00Z"
weight = 4502
keywords = [ "upgrade" ]
aliases = [ "/questions/4502" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [unable to upgrade to wireshark 1.6](/questions/4502/unable-to-upgrade-to-wireshark-16)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4502-score" class="post-score" title="current number of votes">0</div><span id="post-4502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've downloaded(http://www.wireshark.org/download/src/all-versions/wireshark-1.6.0rc2.tar.bz2) and performed the following steps, I still see version 1.2 instead of 1.6. Please advise if any step is missing to upgrade my wireshark to 1.6 version.</p><ol><li>./configure</li><li>make</li><li>make install</li></ol><p>I didn't find any issues running above three steps. I still see version as 1.2.</p><p>tshark -version TShark 1.2.10 (RVBD_208)</p><p>Copyright 1998-2010 Gerald Combs <span><span class="__cf_email__" data-cfemail="aacdcfd8cbc6ceeaddc3d8cfd9c2cbd8c184c5d8cd">[email protected]</span></span> and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (32-bit) with GLib 2.12.3, with libpcap 0.9.4, with libz 1.2.3, with POSIX capabilities (Linux), with libpcre 6.6, without SMI, without c-ares, without ADNS, without Lua, with GnuTLS 1.4.1, with Gcrypt 1.4.4, with MIT Kerberos, without GeoIP.</p><p>Running on Linux 2.6.18-194.el5, with libpcap version 0.9.4, GnuTLS 1.4.1, Gcrypt 1.4.4.</p><p>Built using gcc 4.1.2 20080704 (Red Hat 4.1.2-48).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-upgrade" rel="tag" title="see questions tagged &#39;upgrade&#39;">upgrade</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '11, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/009622f35eab24cfbde3547b04a5bbea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asif&#39;s gravatar image" /><p><span>asif</span><br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asif has no accepted answers">0%</span></p></div></div><div id="comments-container-4502" class="comments-container"></div><div id="comment-tools-4502" class="comment-tools"></div><div class="clear"></div><div id="comment-4502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4503"></span>

<div id="answer-container-4503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4503-score" class="post-score" title="current number of votes">1</div><span id="post-4503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If Wireshark compiles without error (completes <code>./configure</code> and <code>make</code> without problems), it could be that the files simply weren't copied. If your user account does not have the proper credentials (as may well be the case), you may need to run the third step, <code>make install</code> with elevated privileges. This can be accomplished using <code>sudo</code> if your platform supports it or by first becoming root with <code>su</code>.</p><p>Try running <code>make install</code> with elevated privilege by either</p><ol><li><code>sudo make install</code></li></ol><p>or</p><ol><li><code>su root</code></li><li><code>make install</code></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '11, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-4503" class="comments-container"></div><div id="comment-tools-4503" class="comment-tools"></div><div class="clear"></div><div id="comment-4503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4509"></span>

<div id="answer-container-4509" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4509-score" class="post-score" title="current number of votes">1</div><span id="post-4509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Also, it's quite possible you now have two copies of tshark installed. It looks like you're running Redhat so chances are you've got a (Redhat-supplied) tshark in /usr/bin and the new (1.6) copy is in /usr/local/bin .</p><p>If you're running bash do:</p><p>type -a tshark</p><p>to find out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '11, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-4509" class="comments-container"></div><div id="comment-tools-4509" class="comment-tools"></div><div class="clear"></div><div id="comment-4509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

