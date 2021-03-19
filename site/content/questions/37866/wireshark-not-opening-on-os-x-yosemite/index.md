+++
type = "question"
title = "Wireshark not opening on OS X Yosemite"
description = '''I have uninstalled both wireshark and x11, restarted, and then installed both. Still does not open.'''
date = "2014-11-14T08:28:00Z"
lastmod = "2014-11-26T13:56:00Z"
weight = 37866
keywords = [ "osx", "yosemite", "x11" ]
aliases = [ "/questions/37866" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not opening on OS X Yosemite](/questions/37866/wireshark-not-opening-on-os-x-yosemite)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37866-score" class="post-score" title="current number of votes">0</div><span id="post-37866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have uninstalled both wireshark and x11, restarted, and then installed both. Still does not open.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-yosemite" rel="tag" title="see questions tagged &#39;yosemite&#39;">yosemite</span> <span class="post-tag tag-link-x11" rel="tag" title="see questions tagged &#39;x11&#39;">x11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '14, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/fa2a0f0883482e0b75a6b564636dbc0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zero%20visual&#39;s gravatar image" /><p><span>zero visual</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zero visual has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Nov '14, 16:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-37866" class="comments-container"><span id="37876"></span><div id="comment-37876" class="comment"><div id="post-37876-score" class="comment-score"></div><div class="comment-text"><p>What messages are logged in Console?</p></div><div id="comment-37876-info" class="comment-info"><span class="comment-age">(14 Nov '14, 16:22)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-37866" class="comment-tools"></div><div class="clear"></div><div id="comment-37866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38183"></span>

<div id="answer-container-38183" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38183-score" class="post-score" title="current number of votes">0</div><span id="post-38183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Mine also crashed. log below. I 'fixed' it by creating linking /usr/X11/lib to /opt/X11/lib. Non-ideal. Not sure why the build wants /usr/X11/lib for the dylib.<br />
</p><p>Process: wireshark-bin [27506] Path: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin Identifier: wireshark-bin Version: ??? Code Type: X86-64 (Native) Parent Process: Wireshark [27491] Responsible: Wireshark [27491] User ID: 501</p><p>Date/Time: 2014-11-26 15:07:46.327 -0500 OS Version: Mac OS X 10.10.1 (14B25) Report Version: 11 Anonymous UUID: 916AFB86-3665-D0D6-D61E-84E34AFA401F</p><p>Sleep/Wake UUID: 0373CED3-FFE0-4B8C-9F3A-B3CD3A2A180A</p><p>Time Awake Since Boot: 200000 seconds Time Since Wake: 20000 seconds</p><p>Crashed Thread: 0</p><p>Exception Type: EXC_BREAKPOINT (SIGTRAP) Exception Codes: 0x0000000000000002, 0x0000000000000000</p><p>Application Specific Information: dyld: launch, loading dependent libraries</p><p>Dyld Error Message: Library not loaded: /usr/X11/lib/libXext.6.dylib Referenced from: /Applications/Wireshark.app/Contents/Resources/lib/libgtk-x11-2.0.0.dylib Reason: image not found</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '14, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/920edd0b9f2ac1fb3d46dfa10065bfac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kmb&#39;s gravatar image" /><p><span>kmb</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kmb has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-38183" class="comments-container"><span id="38186"></span><div id="comment-38186" class="comment"><div id="post-38186-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Not sure why the build wants /usr/X11/lib for the dylib.</p></blockquote><p>Because that's where it <em>is</em> on those versions of Mac OS X that include X11 as a standard part of the OS.</p><p>Apple stopped shipping X11 with the OS in Mountain Lion and, instead, contributed to (and hosted) the XQuartz project, and pointed users there. That installs X11 under /opt/X11, with a symbolic link from /usr/X11 to /opt/X11.</p><p>I don't know whether the upgrade from Mountain Lion to Mavericks preserves that link. The upgrade from Mavericks (and, presumably, from Mountain Lion) to Yosemite does <strong><em>NOT</em></strong> preserve that link, unfortunately, so you have to put it back manually.</p><p>The correct long-term fix for this is to stop using X11 for Wireshark on OS X; the plan is to stop using GTK+ entirely and use Qt instead - Qt for OS X (which appears to be better supported than "native" GTK+-on-OS X) does not use X11.</p></div><div id="comment-38186-info" class="comment-info"><span class="comment-age">(26 Nov '14, 13:46)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="38187"></span><div id="comment-38187" class="comment"><div id="post-38187-score" class="comment-score"></div><div class="comment-text"><p>However, un-installing X11 and re-installing it should cause the /usr/X11 link to be planted, <strong><em>IF</em></strong> there's no /usr/X11 directory (which there shouldn't be, if you were running Mountain Lion or Mavericks, with XQuartz installed, and upgraded to Mavericks).</p><p>So it sounds as if zero visual might have a different problem; that's why I asked "What messages are logged in Console?"</p></div><div id="comment-38187-info" class="comment-info"><span class="comment-age">(26 Nov '14, 13:56)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-38183" class="comment-tools"></div><div class="clear"></div><div id="comment-38183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

