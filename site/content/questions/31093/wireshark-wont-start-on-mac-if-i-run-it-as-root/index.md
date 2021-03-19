+++
type = "question"
title = "wireshark won&#x27;t start on mac if I run it as root"
description = '''Hi there, When I launch wireshark, it closes immediately.. I tried running through terminal.. Get this message back. (process:5464): Gtk-WARNING **: Locale not supported by C library.  Using the fallback &#x27;C&#x27; locale. (wireshark-bin:5464): Gtk-WARNING **: cannot open display:  Help please.'''
date = "2014-03-23T08:06:00Z"
lastmod = "2014-08-01T10:17:00Z"
weight = 31093
keywords = [ "mac", "root", "wireshark" ]
aliases = [ "/questions/31093" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark won't start on mac if I run it as root](/questions/31093/wireshark-wont-start-on-mac-if-i-run-it-as-root)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31093-score" class="post-score" title="current number of votes">0</div><span id="post-31093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>When I launch wireshark, it closes immediately.. I tried running through terminal.. Get this message back.</p><p>(process:5464): Gtk-WARNING **: Locale not supported by C library. Using the fallback 'C' locale.</p><p>(wireshark-bin:5464): Gtk-WARNING **: cannot open display:</p><p>Help please.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-root" rel="tag" title="see questions tagged &#39;root&#39;">root</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '14, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/677c5933e7fc246c4ae1a12a50ae46bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="klipie245&#39;s gravatar image" /><p><span>klipie245</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="klipie245 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jul '14, 09:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-31093" class="comments-container"><span id="31098"></span><div id="comment-31098" class="comment"><div id="post-31098-score" class="comment-score"></div><div class="comment-text"><p>Can you post the output of 'tshark -v'?</p></div><div id="comment-31098-info" class="comment-info"><span class="comment-age">(23 Mar '14, 10:53)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="34990"></span><div id="comment-34990" class="comment"><div id="post-34990-score" class="comment-score"></div><div class="comment-text"><p>same problem, here's tshark -v:</p><p>sh-3.2# tshark -v TShark 1.10.8 (v1.10.8-2-g52a5244 from master-1.10)</p><p>Copyright 1998-2014 Gerald Combs <span class="__cf_email__" data-cfemail="dabdbfa8bbb6be9aadb3a8bfa9b2bba8b1f4b5a8bd">[email protected]</span> and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GLib 2.36.0, with libpcap, with libz 1.2.3, without POSIX capabilities, without libnl, with SMI 0.4.8, without c-ares, without ADNS, with Lua 5.1, without Python, with GnuTLS 2.12.19, with Gcrypt 1.5.0, with MIT Kerberos, with GeoIP.</p><p>Running on Mac OS X 10.9.4, build 13E28 (Darwin 13.3.0), with locale en_US.UTF-8, with libpcap version 1.3.0 - Apple version 41, with libz 1.2.5. Intel(R) Xeon(R) CPU E5462 @ 2.80GHz</p><p>Built using llvm-gcc 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.9.00).</p></div><div id="comment-34990-info" class="comment-info"><span class="comment-age">(30 Jul '14, 01:09)</span> <span class="comment-user userinfo">shonen</span></div></div></div><div id="comment-tools-31093" class="comment-tools"></div><div class="clear"></div><div id="comment-31093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35004"></span>

<div id="answer-container-35004" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35004-score" class="post-score" title="current number of votes">2</div><span id="post-35004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>sh-3.2#</p></blockquote><p>Don't run Wireshark as root:</p><ol><li>If you installed the standard Wireshark bundle, it shouldn't be necessary in order to capture traffic.</li><li><a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=doc/README.packaging;hb=HEAD">WIRESHARK CONTAINS OVER TWO MILLION LINES OF SOURCE CODE. DO NOT RUN THEM AS ROOT.</a></li><li>Processes running as root are generally not allowed to open a connection to your X server, causing a "cannot open display" error.</li></ol><p>Don't run TShark as root, either, for much the same reason.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '14, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jul '14, 09:15</strong> </span></p></div></div><div id="comments-container-35004" class="comments-container"><span id="35020"></span><div id="comment-35020" class="comment"><div id="post-35020-score" class="comment-score"></div><div class="comment-text"><p>Oops, that was left over from some cleanup work, via su. The problem changes a little with my own user account, but still can't open the display:</p><p>Mac-Pro:bin will$ ./wireshark 2014-07-30 12:04:33.945 defaults[30092:507] The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist 2014-07-30 12:04:33.958 defaults[30093:507] The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist</p><p>(process:30082): Gtk-WARNING **: Locale not supported by C library. Using the fallback 'C' locale.</p><p>(wireshark-bin:30082): Gtk-WARNING **: cannot open display: Mac-Pro:bin will$ ./tshark -v TShark 1.10.8 (v1.10.8-2-g52a5244 from master-1.10)</p><p>Copyright 1998-2014 Gerald Combs <span><span class="__cf_email__" data-cfemail="c4a3a1b6a5a8a084b3adb6a1b7aca5b6afeaabb6a3">[email protected]</span></span> and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GLib 2.36.0, with libpcap, with libz 1.2.3, without POSIX capabilities, without libnl, with SMI 0.4.8, without c-ares, without ADNS, with Lua 5.1, without Python, with GnuTLS 2.12.19, with Gcrypt 1.5.0, with MIT Kerberos, with GeoIP.</p><p>Running on Mac OS X 10.9.4, build 13E28 (Darwin 13.3.0), with locale en_US.UTF-8, with libpcap version 1.3.0 - Apple version 41, with libz 1.2.5. Intel(R) Xeon(R) CPU E5462 @ 2.80GHz</p><p>Built using llvm-gcc 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.9.00).</p></div><div id="comment-35020-info" class="comment-info"><span class="comment-age">(30 Jul '14, 16:18)</span> <span class="comment-user userinfo">shonen</span></div></div><span id="35021"></span><div id="comment-35021" class="comment"><div id="post-35021-score" class="comment-score">1</div><div class="comment-text"><p>What gets printed if you run <code>/usr/X11/bin/xterm</code>?</p></div><div id="comment-35021-info" class="comment-info"><span class="comment-age">(30 Jul '14, 16:45)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="35074"></span><div id="comment-35074" class="comment"><div id="post-35074-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I think I missed a reboot after my Xquartz re-install. Everything is working now. Thanks for the help.</p></div><div id="comment-35074-info" class="comment-info"><span class="comment-age">(01 Aug '14, 10:17)</span> <span class="comment-user userinfo">shonen</span></div></div></div><div id="comment-tools-35004" class="comment-tools"></div><div class="clear"></div><div id="comment-35004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

