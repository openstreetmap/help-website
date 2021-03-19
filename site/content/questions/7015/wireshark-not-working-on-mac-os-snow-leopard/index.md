+++
type = "question"
title = "wireshark not working on Mac OS snow leopard"
description = '''Hi When I try to open wireshark, I am getting error as shown below. [Start] $ sudo wireshark Password: 2011-10-20 17:42:15.677 defaults[3179:903]  The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist 2011-10-20 17:42:15.707 defaults[3180:903]  The domain/de...'''
date = "2011-10-20T17:52:00Z"
lastmod = "2011-11-05T00:42:00Z"
weight = 7015
keywords = [ "osx", "mac", "installation", "x11" ]
aliases = [ "/questions/7015" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark not working on Mac OS snow leopard](/questions/7015/wireshark-not-working-on-mac-os-snow-leopard)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7015-score" class="post-score" title="current number of votes">0</div><span id="post-7015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi When I try to open wireshark, I am getting error as shown below.</p><p>[Start]</p><p>$ sudo wireshark Password: 2011-10-20 17:42:15.677 defaults[3179:903] The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist 2011-10-20 17:42:15.707 defaults[3180:903] The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist dyld: Library not loaded: /usr/X11/lib/libpixman-1.0.dylib Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin Reason: image not found Trace/BPT trap</p><p>[/End]</p><p>FYI.. I have XQuartz 2.6.3 (xorg-server 1.10.3) Wireshark 1.6.1</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-x11" rel="tag" title="see questions tagged &#39;x11&#39;">x11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '11, 17:52</strong></p><img src="https://secure.gravatar.com/avatar/452ec59864c27b39a34979fcb21b498a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mystick_peaks&#39;s gravatar image" /><p><span>mystick_peaks</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mystick_peaks has no accepted answers">0%</span></p></div></div><div id="comments-container-7015" class="comments-container"></div><div id="comment-tools-7015" class="comment-tools"></div><div class="clear"></div><div id="comment-7015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7033"></span>

<div id="answer-container-7033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7033-score" class="post-score" title="current number of votes">0</div><span id="post-7033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't have the Apple built-in version of X11 installed, Wireshark will not work. It is <em>NOT</em> sufficient to install Xquartz from <a href="http://xquartz.macosforge.org/">http://xquartz.macosforge.org/</a>, as XQuartz doesn't install its libraries in <code>/usr/X11/lib</code>, and Wireshark is built to work with the Apple built-in version of X11 (so users don't <em>have</em> to install XQuartz) and thus it expects the X11 libraries to be in <code>/usr/X11/lib</code>. If <code>/usr/X11/lib</code> is empty, you don't have the built-in version of X11 installed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '11, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7033" class="comments-container"><span id="7232"></span><div id="comment-7232" class="comment"><div id="post-7232-score" class="comment-score"></div><div class="comment-text"><p>I dont have build-in version of X11. I got freshly installed OS from apple store. It didnt have ant X11. How would i get one.</p><p>Thanks</p></div><div id="comment-7232-info" class="comment-info"><span class="comment-age">(04 Nov '11, 00:23)</span> <span class="comment-user userinfo">mystick_peaks</span></div></div><span id="7242"></span><div id="comment-7242" class="comment"><div id="post-7242-score" class="comment-score"></div><div class="comment-text"><p>You should have gotten an installation DVD of Snow Leopard with your system, if "freshly installed OS" means it came with a machine you bought (if you bought a Snow Leopard DVD from the Apple Store, you obviously have an installation DVD).</p><p>Insert it into your optical drive; there should be an "Optional Installs" folder. Double-click on that; there should be an "Optional Installs.mpkg" package file. Double-click on that and follow the installation steps; when it gets to the "Custom Install" screen, open up "Applications" and select "X11". Continue with the installation process.</p></div><div id="comment-7242-info" class="comment-info"><span class="comment-age">(04 Nov '11, 18:17)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="7243"></span><div id="comment-7243" class="comment"><div id="post-7243-score" class="comment-score"></div><div class="comment-text"><p>Actually its work laptop, so i dont have installation disk, is there any other way?</p></div><div id="comment-7243-info" class="comment-info"><span class="comment-age">(04 Nov '11, 21:40)</span> <span class="comment-user userinfo">mystick_peaks</span></div></div><span id="7244"></span><div id="comment-7244" class="comment"><div id="post-7244-score" class="comment-score"></div><div class="comment-text"><p>Yes.</p><p>You go to whoever in your organization supplied you with the laptop, tell them you need to have X11 installed on your laptop, and give them the instructions I gave you if they ask you how to install X11.</p></div><div id="comment-7244-info" class="comment-info"><span class="comment-age">(05 Nov '11, 00:42)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-7033" class="comment-tools"></div><div class="clear"></div><div id="comment-7033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

