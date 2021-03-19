+++
type = "question"
title = "How does Wireshark populate the general command section of man pages?"
description = '''output of &#x27;wireshark -v&#x27;: Wireshark 2.0.5 (v2.0.5-0-ga3be9c6 from master-2.0) Copyright 1998-2016 Gerald Combs gerald@wireshark.org and contributors. License GPLv2+: GNU GPL version 2 or later http://www.gnu.org/licenses/old-licenses/gpl-2.0.html This is free software; see the source for copying con...'''
date = "2016-08-26T18:39:00Z"
lastmod = "2016-08-26T19:21:00Z"
weight = 55138
keywords = [ "osx", "mac", "dmg", "wireshark" ]
aliases = [ "/questions/55138" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How does Wireshark populate the general command section of man pages?](/questions/55138/how-does-wireshark-populate-the-general-command-section-of-man-pages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55138-score" class="post-score" title="current number of votes">0</div><span id="post-55138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>output of 'wireshark -v':<br />
Wireshark 2.0.5 (v2.0.5-0-ga3be9c6 from master-2.0)</p><p>Copyright 1998-2016 Gerald Combs <span><span class="__cf_email__" data-cfemail="10777562717c745067796275637871627b3e7f6277">[email protected]</span></span> and contributors. License GPLv2+: GNU GPL version 2 or later <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">http://www.gnu.org/licenses/old-licenses/gpl-2.0.html</a> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with Qt 5.3.2, with libpcap, without POSIX capabilities, with libz 1.2.5, with GLib 2.36.0, with SMI 0.4.8, with c-ares 1.10.0, with Lua 5.2, with GnuTLS 2.12.19, with Gcrypt 1.5.0, with MIT Kerberos, with GeoIP, with QtMultimedia, without AirPcap.</p><p>Running on Mac OS X 10.11.6, build 15G31 (Darwin 15.6.0), with locale en_US.UTF-8, with libpcap version 1.5.3 - Apple version 54, with libz 1.2.5, with GnuTLS 2.12.19, with Gcrypt 1.5.0. Intel(R) Core(TM) i5-5250U CPU @ 1.60GHz (with SSE4.2)</p><p>Built using llvm-gcc 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.9.00).<br />
</p><p>When installing Wireshark from a .dmg file, the man pages are not populated. /usr/share/man/man1 does not contain a man page for Wireshark, nor can I use 'man wireshark'. I have confirmed that this is also an issue for other Mac users as it has been submitted as a bug found <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12746">here</a>.</p><p>Considering that man pages worked for me on the Linux version of Wireshark, and not on the Mac version, and since it is occurring on other's Macs, I can confirm this as a minor bug.</p><p>I made the assumption that the file is populated during Make, but I want to get more information here.</p><p>How does Wireshark populate the man pages, and how could I fix this for Mac builds?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-dmg" rel="tag" title="see questions tagged &#39;dmg&#39;">dmg</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '16, 18:39</strong></p><img src="https://secure.gravatar.com/avatar/beed9ebfd7efaf125b56d9938d5a6365?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xeno&#39;s gravatar image" /><p><span>xeno</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xeno has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-55138" class="comments-container"></div><div id="comment-tools-55138" class="comment-tools"></div><div class="clear"></div><div id="comment-55138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55139"></span>

<div id="answer-container-55139" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55139-score" class="post-score" title="current number of votes">1</div><span id="post-55139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How does Wireshark populate the man pages</p></blockquote><p>It depends. "make install" will typically install them in <code>/usr/local</code>, but the app bundles distributed by wireshark.org are built differently. There <em>are</em> man pages in the app bundle - they're in subdirectories of the app bundle's <code>Contents/Resources/share/man</code> directory - but the installer doesn't copy them to <code>/usr/local/share/man</code> or link them from <code>/usr/local/share/man</code>.</p><blockquote><p>and how could I fix this for Mac builds?</p></blockquote><p>Have the post-install script for the CLI, in the Wireshark install package for OS X, copy the man pages to <code>/usr/local/share/man</code>. (<code>/usr/local/man</code> is off-limits to anything not from Apple - and System Integrity Protection enforces that in El Capitan and later - so we will not ever install stuff there.)</p><p>That script is in the Wireshark source; it's <code>packaging/macosx/Scripts/cli-postinstall.sh</code>.</p><p>The default <code>MANPATH</code> appears to include <code>/usr/local/share/man</code>; if you're setting <code>MANPATH</code> yourself, for example in your <code>.profile</code> or <code>.login</code> script, you will need to make sure it includes <code>/usr/local/share/man</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '16, 19:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-55139" class="comments-container"></div><div id="comment-tools-55139" class="comment-tools"></div><div class="clear"></div><div id="comment-55139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

