+++
type = "question"
title = "wireshark error installation"
description = '''Hello, Then we try to install wireshark version 2.4.2 we getting this error in the installation: [23F8:2480][2017-10-17T11:06:48]i052: Condition &#x27;VersionNT64 &amp;gt;= v6.0 OR (VersionNT64 = v5.2 AND ServicePackLevel &amp;gt;= 1)&#x27; evaluates to true. [23F8:2480][2017-10-17T11:06:48]i199: Detect complete, res...'''
date = "2017-10-17T03:33:00Z"
lastmod = "2017-10-17T04:32:00Z"
weight = 63958
keywords = [ "windows", "wix", "wireshark" ]
aliases = [ "/questions/63958" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark error installation](/questions/63958/wireshark-error-installation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63958-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Then we try to install wireshark version 2.4.2 we getting this error in the installation:</p><p><code>[23F8:2480][2017-10-17T11:06:48]i052: Condition 'VersionNT64 &gt;= v6.0 OR (VersionNT64 = v5.2 AND ServicePackLevel &gt;= 1)' evaluates to true. [23F8:2480][2017-10-17T11:06:48]i199: Detect complete, result: 0x0 [23F8:2568][2017-10-17T11:06:48]e000: Error 0x80070666: Cannot install a product when a newer version is installed. [23F8:2480][2017-10-17T11:06:48]i500: Shutting down, exit code: 0x666 [23F8:2480][2017-10-17T11:06:48]i410: Variable: ServicePackLevel = 1 [23F8:2480][2017-10-17T11:06:48]i410: Variable: SystemFolder = C:\WINDOWS\system32\ [23F8:2480][2017-10-17T11:06:48]i410: Variable: VersionNT = 6.1.0.0 [23F8:2480][2017-10-17T11:06:48]i410: Variable: VersionNT64 = 6.1.0.0 [23F8:2480][2017-10-17T11:06:48]i410: Variable: windows_uCRT_DetectKey = 10.0.10586.788 [23F8:2480][2017-10-17T11:06:48]i410: Variable: windows_uCRT_DetectKeyExists = 1 [23F8:2480][2017-10-17T11:06:48]i410: Variable: WixBundleAction = 5 [23F8:2480][2017-10-17T11:06:48]i410: Variable: WixBundleCompressed = 1 [23F8:2480][2017-10-17T11:06:48]i410: Variable: WixBundleElevated = 1 [23F8:2480][2017-10-17T11:06:48]i410: Variable: WixBundleInstalled = 0 [23F8:2480][2017-10-17T11:06:48]i410: Variable: WixBundleLog = C:\Logs\VCRedist.2015.x64.Install.log [23F8:2480][2017-10-17T11:06:48]i410: Variable: WixBundleManufacturer = Microsoft Corporation [23F8:2480][2017-10-17T11:06:48]i410: Variable: WixBundleName = Microsoft Visual C++ 2015 Redistributable (x64) - 14.0.24215 [23F8:2480][2017-10-17T11:06:48]i410: Variable: WixBundleOriginalSource = \b5592s01.d101p.bdpnet.dk\SCCM_SOFTWARE$\WIRESHARK 2.4.1 X64 ENUS R2\vcredist_x64.exe [23F8:2480][2017-10-17T11:06:48]i410: Variable: WixBundleOriginalSourceFolder = \b5592s01.d101p.bdpnet.dk\SCCM_SOFTWARE$\WIRESHARK 2.4.1 X64 ENUS R2\ [23F8:2480][2017-10-17T11:06:48]i410: Variable: WixBundleProviderKey = {d992c12e-cab2-426f-bde3-fb8c53950b0d} [23F8:2480][2017-10-17T11:06:48]i410: Variable: WixBundleTag =  [23F8:2480][2017-10-17T11:06:48]i410: Variable: WixBundleVersion = 14.0.24215.1 [23F8:2480][2017-10-17T11:06:48]i007: Exit code: 0x666, restarting: No</code></p><p>hope someone can help us. to solved the problem</p></div><div id="question-tags" class="tags-container tags">windows wix wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '17, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/623a244001d14738ed0cbef4c72831df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stoffer20&#39;s gravatar image" /><p>stoffer20<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stoffer20 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '17, 04:29</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-63958" class="comments-container"></div><div id="comment-tools-63958" class="comment-tools"></div><div class="clear"></div><div id="comment-63958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63960"></span>

<div id="answer-container-63960" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63960-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're using the msi installer which IMHO is still somewhat "experimental". The installer seems to be complaining about a previous version that is newer.</p><p>Have you tried uninstalling any existing versions first? IF that doesn't fix it then I think you'll have to raise an entry on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a> if there isn't one already.</p><p>You could also try the regular .exe installer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '17, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63960" class="comments-container"><span id="63990"></span><div id="comment-63990" class="comment"><div id="post-63990-score" class="comment-score"></div><div class="comment-text"><p>i dont think its a bug. I think its because our users have other program's install that also use visuel c++ runtime. but the other program's my users use running on a newer version of visuel c++ runtime.</p><p>So what i try to understand is why wireshark not can't work with newer version of visuel c++ runtime. and is there anyway so force wireshark to work with newer version of visuel c++ runtime</p></div><div id="comment-63990-info" class="comment-info"><span class="comment-age">(17 Oct '17, 22:30)</span> stoffer20</div></div><span id="63994"></span><div id="comment-63994" class="comment"><div id="post-63994-score" class="comment-score"></div><div class="comment-text"><p>I think the fact that it doesn't work is ample evidence of a bug.</p><p>The Wireshark installers use the MS provided redistributable files for installing the VC runtimes, so either:</p><ol><li>There's a bug in the MS provided files</li><li>The installer is using the MS provided files incorrectly.</li></ol><p>I don't think there's anything the user can do to fix this, apart from uninstalling whatever it is that's conflicting which isn't positively identified and may be difficult to achieve.</p><p>Have you tried using the regular .exe installer?</p></div><div id="comment-63994-info" class="comment-info"><span class="comment-age">(18 Oct '17, 03:08)</span> grahamb ♦</div></div></div><div id="comment-tools-63960" class="comment-tools"></div><div class="clear"></div><div id="comment-63960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

