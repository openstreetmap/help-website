+++
type = "question"
title = "Wireshark crashes on OSX 10.6.8 on startup"
description = '''Hello I found this post: http://ask.wireshark.org/questions/22081/1100-trying-to-run-on-osx1058-but-crashes-on-load where someone had a problem starting Wireshark 1.10 on Mac OSX 10.5, but I have maybe the same problem with my MacBook Pro 10.6.8 (from 2009) and Wireshark 1.8.10 Intel 64 or 1.10.2 In...'''
date = "2013-10-16T14:09:00Z"
lastmod = "2013-11-13T13:52:00Z"
weight = 26086
keywords = [ "osx", "10.6.8", "crash" ]
aliases = [ "/questions/26086" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashes on OSX 10.6.8 on startup](/questions/26086/wireshark-crashes-on-osx-1068-on-startup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26086-score" class="post-score" title="current number of votes">1</div><span id="post-26086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I found this post: <a href="http://ask.wireshark.org/questions/22081/1100-trying-to-run-on-osx1058-but-crashes-on-load">http://ask.wireshark.org/questions/22081/1100-trying-to-run-on-osx1058-but-crashes-on-load</a> where someone had a problem starting Wireshark 1.10 on Mac OSX 10.5, but I have maybe the same problem with my MacBook Pro 10.6.8 (from 2009) and Wireshark 1.8.10 Intel 64 or 1.10.2 Intel 64 or 1.11.0 Intel 64. I start it and immediately I get the crash with this error:</p><blockquote><p>Exception Type: EXC_BREAKPOINT (SIGTRAP) Exception Codes: 0x0000000000000002, 0x0000000000000000 Crashed Thread: 0</p><p>Dyld Error Message: Library not loaded: /usr/lib/libc++.1.dylib<br />
Referenced from: /Applications/Wireshark.app/Contents/MacOS/../Frameworks/QtCore.framework/Versions/5/QtCore Reason: image not found</p><p>Binary Images: 0x7fff5fc00000 - 0x7fff5fc3bdef dyld 132.1 (???) &lt;b536f2f1-9df1-3b6c-1c2c-9075ea219a06&gt; /usr/lib/dyld</p></blockquote><p>I uninstalled it, reinstalled it, rebooted, not working. I even tried Wireshark 1.11.0 Intel 32 but this crashes without any crashing window. I installed XQuartz 2.7.4 now (had X11 2.3 before), log out and on, no change.</p><p>Can somebody tell me what I should do? I had a running version of Wireshark 1.6.1 Intel 64 which was working with X11.</p><p>Thank you</p><p>frank</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-10.6.8" rel="tag" title="see questions tagged &#39;10.6.8&#39;">10.6.8</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '13, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/932f872b04b352a8f3d81288805f08be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="franc&#39;s gravatar image" /><p><span>franc</span><br />
<span class="score" title="96 reputation points">96</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="franc has 2 accepted answers">40%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Oct '13, 14:33</strong> </span></p></div></div><div id="comments-container-26086" class="comments-container"><span id="26151"></span><div id="comment-26151" class="comment"><div id="post-26151-score" class="comment-score"></div><div class="comment-text"><blockquote><p>/Applications/Wireshark.app/Contents/MacOS/../Frameworks/QtCore.framework/Versions/5/QtCore Reason: image not found</p></blockquote><p>You are not getting that error from 1.8.10 or 1.10.2, as those aren't built with Qt. What errors are you getting with those versions of Wireshark?</p></div><div id="comment-26151-info" class="comment-info"><span class="comment-age">(17 Oct '13, 17:38)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-26086" class="comment-tools"></div><div class="clear"></div><div id="comment-26086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26167"></span>

<div id="answer-container-26167" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26167-score" class="post-score" title="current number of votes">1</div><span id="post-26167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Great heavens, this hint was pure gold! I uninstalled then all wireshark rests, I did:</p><p>rm /Users/f/Library/Preferences/org.wireshark.Wireshark.plist</p><p>rm -r /Users/f/.wireshark</p><p>rm -r /Applications/Wireshark.app</p><p>rm /usr/local/bin/wireshark</p><p>rm -r /Library/StartupItems/ChmodBPF</p><p>and installed the version 1.10.2 and hush! it works!!!</p><p>Thank you very much!</p><p>I think this was the mix-up with 1.11.0 and the old version 1.6.1 maybe, which through this error.</p><p>frank</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '13, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/932f872b04b352a8f3d81288805f08be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="franc&#39;s gravatar image" /><p><span>franc</span><br />
<span class="score" title="96 reputation points">96</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="franc has 2 accepted answers">40%</span></p></div></div><div id="comments-container-26167" class="comments-container"><span id="26185"></span><div id="comment-26185" class="comment"><div id="post-26185-score" class="comment-score"></div><div class="comment-text"><blockquote><p><code>rm -r /Users/f/.wireshark</code></p></blockquote><p>That step probably wasn't necessary - it threw away whatever preference settings you had.</p></div><div id="comment-26185-info" class="comment-info"><span class="comment-age">(18 Oct '13, 10:22)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="26186"></span><div id="comment-26186" class="comment"><div id="post-26186-score" class="comment-score"></div><div class="comment-text"><p>And, yes, currently 1.11.0 doesn't work on Snow Leopard. We're looking at that.</p></div><div id="comment-26186-info" class="comment-info"><span class="comment-age">(18 Oct '13, 10:22)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="26944"></span><div id="comment-26944" class="comment"><div id="post-26944-score" class="comment-score"></div><div class="comment-text"><p>I mistakenly installed 1.10.3 on my 10.6.8 machine and ran into this issue as well, deleted all the files above except the <code>.wireshark</code> and I'm back up and running. Thanks!</p></div><div id="comment-26944-info" class="comment-info"><span class="comment-age">(13 Nov '13, 06:52)</span> <span class="comment-user userinfo">Hoss</span></div></div><span id="26967"></span><div id="comment-26967" class="comment"><div id="post-26967-score" class="comment-score"></div><div class="comment-text"><p>You would not have gotten</p><pre><code>/Applications/Wireshark.app/Contents/MacOS/../Frameworks/QtCore.framework/Versions/5/QtCore Reason: image not found</code></pre><p>with 1.10.3, as the 1.10.x (and earlier) releases aren't built with Qt.</p></div><div id="comment-26967-info" class="comment-info"><span class="comment-age">(13 Nov '13, 13:52)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-26167" class="comment-tools"></div><div class="clear"></div><div id="comment-26167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

