+++
type = "question"
title = "what&#x27;s the primary reason windows can&#x27;t capture usb packets yet linux can"
description = '''http://wiki.wireshark.org/CaptureSetup/USB is it because windows just doesn&#x27;t have the software to do so?'''
date = "2012-05-16T01:15:00Z"
lastmod = "2013-04-11T18:30:00Z"
weight = 11025
keywords = [ "wireshark" ]
aliases = [ "/questions/11025" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [what's the primary reason windows can't capture usb packets yet linux can](/questions/11025/whats-the-primary-reason-windows-cant-capture-usb-packets-yet-linux-can)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11025-score" class="post-score" title="current number of votes">0</div><span id="post-11025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="http://wiki.wireshark.org/CaptureSetup/USB">http://wiki.wireshark.org/CaptureSetup/USB</a><br />
is it because windows just doesn't have the software to do so?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '12, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/b2a4006b4a0252f8be292c57acde97ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiresharkhelpers&#39;s gravatar image" /><p><span>wiresharkhel...</span><br />
<span class="score" title="30 reputation points">30</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiresharkhelpers has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-11025" class="comments-container"></div><div id="comment-tools-11025" class="comment-tools"></div><div class="clear"></div><div id="comment-11025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11026"></span>

<div id="answer-container-11026" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11026-score" class="post-score" title="current number of votes">1</div><span id="post-11026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wiresharkhelpers has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Microsoft :-)</p><p>Just kidding.... Linux offers a subsystem (usbmon) that enables libpcap to sniff USB traffic. There is nothing comparable under windows, as nobody has implemented it yet. You'll find some hints in the wiki how to create such a subsystem ("Hints for developing something like a Windows native "USBPcap":). However some of the links are outdated.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '12, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 May '12, 01:22</strong> </span></p></div></div><div id="comments-container-11026" class="comments-container"><span id="11029"></span><div id="comment-11029" class="comment"><div id="post-11029-score" class="comment-score"></div><div class="comment-text"><p>ok so windows doesn't have the software</p></div><div id="comment-11029-info" class="comment-info"><span class="comment-age">(16 May '12, 01:24)</span> <span class="comment-user userinfo">wiresharkhel...</span></div></div><span id="11033"></span><div id="comment-11033" class="comment"><div id="post-11033-score" class="comment-score"></div><div class="comment-text"><p>well, it's not yet possible with wireshark.</p><p>If you need to sniff USB traffic on windows 7, check this link:</p><blockquote><p><code>http://blogs.msdn.com/b/usbcoreblog/archive/2009/12/04/etw-in-the-windows-7-usb-core-stack.aspx</code></p></blockquote></div><div id="comment-11033-info" class="comment-info"><span class="comment-age">(16 May '12, 01:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="20347"></span><div id="comment-20347" class="comment"><div id="post-20347-score" class="comment-score"></div><div class="comment-text"><p>Microsoft:) boy,that is spot on(SteveJ will shower his blessings)</p></div><div id="comment-20347-info" class="comment-info"><span class="comment-age">(11 Apr '13, 12:49)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="20360"></span><div id="comment-20360" class="comment"><div id="post-20360-score" class="comment-score"></div><div class="comment-text"><p>The company that the first SteveJ who comes to mind formerly headed doesn't have a published and documented mechanism for doing USB sniffing. There are debug versions of the IOUSBFamily kext ("kext" is to OS X as "lkm" is to Linux or ".sys file", I guess, is to Windows) that provide information that some Apple tools can read; the debug versions are OS-version-dependent. <a href="http://developer.apple.com/library/mac/#qa/qa1370/_index.html">Apple Technical Q&amp;A QA1370</a>, which is a bit out of date (<code>/Developer</code> is obsolete; that stuff is now under <code>/Applications/Xcode.app/Contents</code>) says</p><blockquote><p>The logging version of the IOUSBFamily Kernel Extension does not provide packet data information that is available under Windows. Even under Windows, a USB Analyzer is required to analyze problems resulting from STALL, DATA TOGGLE, and other protocol error conditions.</p></blockquote><p>so it sounds as if, even <em>with</em> that kext, you can't do as much sniffing on OS X as you can on Windows. Linux FTW here....</p></div><div id="comment-20360-info" class="comment-info"><span class="comment-age">(11 Apr '13, 18:30)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-11026" class="comment-tools"></div><div class="clear"></div><div id="comment-11026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20345"></span>

<div id="answer-container-20345" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20345-score" class="post-score" title="current number of votes">1</div><span id="post-20345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <a href="http://desowin.org/usbpcap">USBPcap</a> to capture USB traffic on Windows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '13, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/96637248dab9a269e98fbf0344e26a93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="desowin&#39;s gravatar image" /><p><span>desowin</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="desowin has no accepted answers">0%</span></p></div></div><div id="comments-container-20345" class="comments-container"><span id="20353"></span><div id="comment-20353" class="comment"><div id="post-20353-score" class="comment-score"></div><div class="comment-text"><p>nice one. Thank you!</p></div><div id="comment-20353-info" class="comment-info"><span class="comment-age">(11 Apr '13, 14:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20345" class="comment-tools"></div><div class="clear"></div><div id="comment-20345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

