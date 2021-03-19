+++
type = "question"
title = "Qt4 GUI build fails"
description = '''Hi, I&#x27;m trying to compile the Qt4 version of Wireshark on Ubuntu 12.04 (--with-qt). Unfortunately the build process fails at several places (latest SVN trunk). And: yes, I did install libqt4-dev ;-) Is it my system, or is the Qt4 build not yet finished? Regards Kurt'''
date = "2012-05-25T11:27:00Z"
lastmod = "2012-05-29T06:07:00Z"
weight = 11347
keywords = [ "qt4" ]
aliases = [ "/questions/11347" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Qt4 GUI build fails](/questions/11347/qt4-gui-build-fails)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11347-score" class="post-score" title="current number of votes">1</div><span id="post-11347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to compile the Qt4 version of Wireshark on Ubuntu 12.04 (--with-qt). Unfortunately the build process fails at several places (latest SVN trunk). And: yes, I did install libqt4-dev ;-)</p><p>Is it my system, or is the Qt4 build not yet finished?</p><p>Regards<br />
Kurt</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-qt4" rel="tag" title="see questions tagged &#39;qt4&#39;">qt4</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '12, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 May '12, 11:32</strong> </span></p></div></div><div id="comments-container-11347" class="comments-container"></div><div id="comment-tools-11347" class="comment-tools"></div><div class="clear"></div><div id="comment-11347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11348"></span>

<div id="answer-container-11348" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11348-score" class="post-score" title="current number of votes">1</div><span id="post-11348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kurt Knochner has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I can't speak to failures in the build process with SVN trunk since I haven't done a build of Qt Wireshark in a while.</p><p>However, I can say that Qt Wireshark is very much a work in progress (quite early development).</p><p>Have you reviewed <code>doc/README.qt</code> ??</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '12, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-11348" class="comments-container"><span id="11350"></span><div id="comment-11350" class="comment"><div id="post-11350-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Have you reviewed doc/README.qt ??</p></blockquote><p>No, thanks for the hint. I will read that now.</p></div><div id="comment-11350-info" class="comment-info"><span class="comment-age">(25 May '12, 13:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11436"></span><div id="comment-11436" class="comment"><div id="post-11436-score" class="comment-score"></div><div class="comment-text"><p>I should have read doc/README.qt :-) It's all described therein...</p></div><div id="comment-11436-info" class="comment-info"><span class="comment-age">(29 May '12, 05:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11348" class="comment-tools"></div><div class="clear"></div><div id="comment-11348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11357"></span>

<div id="answer-container-11357" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11357-score" class="post-score" title="current number of votes">2</div><span id="post-11357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Using CMake the qt build compiled OK for me on Kubuntu 12.04, Wireshark trunk r42854:</p><pre><code>xx:~/Software/Wireshark/build$./qtshark --version
wireshark 1.7.2 (SVN Rev 42854 from /trunk)

Copyright 1998-2012 Gerald Combs &lt;[email protected]wireshark.org&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (32-bit) with Qt 4.8.1 with GLib 2.32.1, with libpcap, with libz
1.2.3.4, with POSIX capabilities (Linux), with SMI 0.4.8, with c-ares 1.7.5,
with Lua 5.1, without Python, with GnuTLS 2.12.14, with Gcrypt 1.5.0, with MIT
Kerberos, with GeoIP, with PortAudio V19-devel (built Dec 10 2011 11:43:21),
without AirPcap.

Running on Linux 3.2.0-24-generic, with locale en_GB.UTF-8, with libpcap version
1.1.1, with libz 1.2.3.4, GnuTLS 2.12.14, Gcrypt 1.5.0.

Built using gcc 4.6.3.

xx:~/Software/Wireshark/build$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 12.04 LTS
Release:        12.04
Codename:       precise</code></pre><p>Oddly enough I can't get the gtk build to complete, CMake can't find glibconfig.h even though it does exist, probably a path issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '12, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 May '12, 15:27</strong> </span></p></div></div><div id="comments-container-11357" class="comments-container"><span id="11437"></span><div id="comment-11437" class="comment"><div id="post-11437-score" class="comment-score"></div><div class="comment-text"><p>cmake is the way to go (or qtcreator) - doc/README.qt. Unfortunately I was not able to build the latest trunk with cmake on Ubuntu 12.04 (Gnome). There are a some errors in <a href="http://CMakeLists.txt">CMakeLists.txt</a></p><blockquote><p><code>QT4_ADD_TRANSLATION - Unknown CMake command ..</code><br />
<code>No cmake_minimum_required command is present</code> (while it's there)</p></blockquote><p>.</p><blockquote><p>Using CMake the qt build compiled OK for me on Kubuntu 12.04, Wireshark trunk r42854</p></blockquote><p>I wonder what's the difference between Kubuntu 12.04 and Ubuntu 12.04 in terms of building wireshark with cmake. I blieve I have installed all required Qt (dev) libs and tools. Maybe not....</p></div><div id="comment-11437-info" class="comment-info"><span class="comment-age">(29 May '12, 05:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11439"></span><div id="comment-11439" class="comment"><div id="post-11439-score" class="comment-score"></div><div class="comment-text"><p>As I mentioned, on Kubuntu I can't get cmake to do a gtk build. Like you I believe I have all the required libs, I think the paths are tripping up cmake though. I should post on the dev mailing list about that.</p></div><div id="comment-11439-info" class="comment-info"><span class="comment-age">(29 May '12, 06:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-11357" class="comment-tools"></div><div class="clear"></div><div id="comment-11357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

