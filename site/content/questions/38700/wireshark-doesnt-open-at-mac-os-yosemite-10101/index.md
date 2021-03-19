+++
type = "question"
title = "Wireshark doesn&#x27;t open at MAC OS Yosemite 10.10.1"
description = '''Hello, I can&#x27;t open Wireshark at my Mac OS Yosemite 10.10.1 I get following error messages at CLI: *macbook-pro-5:~ user$ sudo wireshark Password: 2014-12-24 18:41:57.438 defaults[2540:92985] The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist 2014-12-24 1...'''
date = "2014-12-24T09:53:00Z"
lastmod = "2015-01-04T03:15:00Z"
weight = 38700
keywords = [ "mac", "yosemite", "open", "message", "error" ]
aliases = [ "/questions/38700" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark doesn't open at MAC OS Yosemite 10.10.1](/questions/38700/wireshark-doesnt-open-at-mac-os-yosemite-10101)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38700-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I can't open Wireshark at my Mac OS Yosemite 10.10.1</p><p>I get following error messages at CLI:</p><pre><code>*macbook-pro-5:~ user$ sudo wireshark
Password:
2014-12-24 18:41:57.438 defaults[2540:92985] The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist
2014-12-24 18:41:57.450 defaults[2541:92991] The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist
dyld: Library not loaded: /usr/X11/lib/libcairo.2.dylib
  Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin
  Reason: image not found
macbook-pro-5:~ reneschiller$ sudo ln -s /opt/X11 /usr/X11
macbook-pro-5:~ reneschiller$ sudo wireshark
2014-12-24 18:43:13.614 defaults[2579:93502] The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist
2014-12-24 18:43:13.625 defaults[2580:93508] The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist
(process:2569): Gtk-WARNING **: Locale not supported by C library.
    Using the fallback &#39;C&#39; locale.
(wireshark-bin:2569): Gtk-WARNING **: cannot open display: /private/tmp/com.apple.launchd.JDIYCkEIov/org.macosforge.xquartz:0*</code></pre><p>Hopefully you have an idea. Many thanks</p></div><div id="question-tags" class="tags-container tags">mac yosemite open message error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '14, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/0a6e9607e4d3edda816af15879f86201?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiresniff&#39;s gravatar image" /><p>wiresniff<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiresniff has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Dec '14, 15:27</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-38700" class="comments-container"><span id="38701"></span><div id="comment-38701" class="comment"><div id="post-38701-score" class="comment-score">1</div><div class="comment-text"><p>Do you have X11 installed? What does <code>ls -ld /opt/X11</code> print?</p></div><div id="comment-38701-info" class="comment-info"><span class="comment-age">(24 Dec '14, 15:28)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-38700" class="comment-tools"></div><div class="clear"></div><div id="comment-38700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38876"></span>

<div id="answer-container-38876" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38876-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello, thank you for this tip. I had an old version of X11 running. I installed the latest release 2.7.7. Now Wireshark opens.</p><p>Best Regards</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '15, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/0a6e9607e4d3edda816af15879f86201?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiresniff&#39;s gravatar image" /><p>wiresniff<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiresniff has no accepted answers">0%</span></p></div></div><div id="comments-container-38876" class="comments-container"></div><div id="comment-tools-38876" class="comment-tools"></div><div class="clear"></div><div id="comment-38876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

