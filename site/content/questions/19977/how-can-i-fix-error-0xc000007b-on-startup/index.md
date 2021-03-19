+++
type = "question"
title = "How can I fix error 0xc000007b on startup?"
description = '''When I open the program, I get this error: 0xc000007b. I have windows 7 home premium x64. How I can resolve?'''
date = "2013-03-31T16:02:00Z"
lastmod = "2017-01-30T23:36:00Z"
weight = 19977
keywords = [ "windows", "crash" ]
aliases = [ "/questions/19977" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How can I fix error 0xc000007b on startup?](/questions/19977/how-can-i-fix-error-0xc000007b-on-startup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19977-score" class="post-score" title="current number of votes">0</div><span id="post-19977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I open the program, I get this error: 0xc000007b.</p><p>I have windows 7 home premium x64.</p><p>How I can resolve?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '13, 16:02</strong></p><img src="https://secure.gravatar.com/avatar/664f7eb44cb3816daa5f3f82c2ef397b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asdflol&#39;s gravatar image" /><p><span>asdflol</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asdflol has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Apr '13, 07:17</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-19977" class="comments-container"></div><div id="comment-tools-19977" class="comment-tools"></div><div class="clear"></div><div id="comment-19977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="19978"></span>

<div id="answer-container-19978" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19978-score" class="post-score" title="current number of votes">1</div><span id="post-19978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm assuming that you are getting this error when you try to start Wireshark.</p><p>Googling a bit on error 0xc000007b finds the following:</p><p><a href="http://social.msdn.microsoft.com/Forums/en-US/vssetup/thread/96035692-9a50-40d4-a7d3-48bda87d11ec/">http://social.msdn.microsoft.com/Forums/en-US/vssetup/thread/96035692-9a50-40d4-a7d3-48bda87d11ec/</a></p><p>The error apparently means: "STATUS_INVALID_IMAGE_FORMAT"</p><p>and apparently can be caused by things as a corrupted Wireshark exec file, trying to exec a 32 bit image on a 64 bit system, etc.</p><p>If the above doesn't help try looking at some of the other results from a search for 0xc000007b (not 0cx....)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '13, 16:41</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-19978" class="comments-container"><span id="19986"></span><div id="comment-19986" class="comment"><div id="post-19986-score" class="comment-score"></div><div class="comment-text"><p>I tryed but i ha ve the esame problem.</p></div><div id="comment-19986-info" class="comment-info"><span class="comment-age">(01 Apr '13, 04:12)</span> <span class="comment-user userinfo">asdflol</span></div></div><span id="26855"></span><div id="comment-26855" class="comment"><div id="post-26855-score" class="comment-score"></div><div class="comment-text"><p>The install package was downloaded directly from Wireshark. All anti-malware software was disabled during the installation. The 64-bit program would still not start (gave error). However, if the 32-bit is installed it operates perfectly, even if the anti-malware software is active during the install. This appears to indicate a needed 64-bit dll is not being installed or referenced correctly.</p></div><div id="comment-26855-info" class="comment-info"><span class="comment-age">(11 Nov '13, 12:52)</span> <span class="comment-user userinfo">ff2emtvol</span></div></div></div><div id="comment-tools-19978" class="comment-tools"></div><div class="clear"></div><div id="comment-19978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20022"></span>

<div id="answer-container-20022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20022-score" class="post-score" title="current number of votes">0</div><span id="post-20022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As <span>@Bill Meier</span> said, 0xc000007b means a corrupted image file.</p><p>See also here:</p><blockquote><p><a href="http://msdn.microsoft.com/en-us/library/cc704588.aspx">http://msdn.microsoft.com/en-us/library/cc704588.aspx</a></p></blockquote><p>If reinstalling Whireshark does not solve the problem, there is <strong>something</strong> on your system the modifies either the Wireshark binary (wireshark.exe) or some of the libraries. Good candidates are Anti Virus software, Endpoint Security Software (Symantec), or any other security software, as it might think to have found malware in those files and tried to 'clean' the files. If you downloaded the wireshark installer from wireshark.org, there will be <strong>no malware</strong> in those files and your security software needs to be adjusted to allow installing and running wireshark (please ask your security software vendor). If did <strong>not</strong> download the installer from wireshark.org, you might be in "trouble", as that installer (or the content) could be infected with malware. In that case your security software saved your butt ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '13, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20022" class="comments-container"></div><div id="comment-tools-20022" class="comment-tools"></div><div class="clear"></div><div id="comment-20022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28197"></span>

<div id="answer-container-28197" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28197-score" class="post-score" title="current number of votes">0</div><span id="post-28197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>I too face same error and this is coming due to : msvcr100.dll and msvcr80.dll mismatch. copied these dlls from : <a href="http://helpx.adobe.com/lightroom/kb/error-unable-start-correctly-0xc00007b.html">http://helpx.adobe.com/lightroom/kb/error-unable-start-correctly-0xc00007b.html</a></p><p>and this solved my problem</p><p>Thanks Sridhar P</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '13, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/164377bf1b3dc9d82b5a50d56b525b0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pinisetti&#39;s gravatar image" /><p><span>pinisetti</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pinisetti has no accepted answers">0%</span></p></div></div><div id="comments-container-28197" class="comments-container"></div><div id="comment-tools-28197" class="comment-tools"></div><div class="clear"></div><div id="comment-28197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59172"></span>

<div id="answer-container-59172" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59172-score" class="post-score" title="current number of votes">0</div><span id="post-59172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>It occurs when you try to run a app on 64-bit system which is compatible with 32-bit system. you can resolve this issue by following some simple steps. 1. Reinstall the Application 2. Run as An Administrator 3. Fix Compatibility between Application and System 4. Check Your Hard Disk For detailed solution visit here: <a href="http://errorcodespro.com/fix-error-code-0xc000007b-windows-7-10/">http://errorcodespro.com/fix-error-code-0xc000007b-windows-7-10/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '17, 23:36</strong></p><img src="https://secure.gravatar.com/avatar/c6dd459b157ab6cd878408d6761954c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="christinegrant98&#39;s gravatar image" /><p><span>christinegra...</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="christinegrant98 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jan '17, 23:37</strong> </span></p></div></div><div id="comments-container-59172" class="comments-container"></div><div id="comment-tools-59172" class="comment-tools"></div><div class="clear"></div><div id="comment-59172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

