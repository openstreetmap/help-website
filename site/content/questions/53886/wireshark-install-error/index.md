+++
type = "question"
title = "Wireshark install error."
description = '''I&#x27;m having an issue installing any of the 2.0.X versions of Wireshark. I keep getting the error &quot;Wireshark or one of its associated programs is running. Please close it first.&quot; I&#x27;m currently installing on a Windows 7 64 bit system but I&#x27;m also running into the same issue with Windows 2012 R2.I&#x27;ve re...'''
date = "2016-07-07T02:07:00Z"
lastmod = "2016-07-07T04:49:00Z"
weight = 53886
keywords = [ "wireshark" ]
aliases = [ "/questions/53886" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark install error.](/questions/53886/wireshark-install-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53886-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm having an issue installing any of the 2.0.X versions of Wireshark. I keep getting the error "Wireshark or one of its associated programs is running. Please close it first." I'm currently installing on a Windows 7 64 bit system but I'm also running into the same issue with Windows 2012 R2.I've read the previous answer where to go in a verify that dumpcap.exe was not running, which I did. I've also checked for other running Wireshark processes. I can install any of the 1.12.X versions without any issues. I've checked the event logs with no addition information being provided. This version of Windows has had many security modifications applied to it but I went though each one and I can not come up with which one may be an issue. Any guidance would be appreciated.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '16, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/17b0cab25d8571b5fe44d3cee64641ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael2016&#39;s gravatar image" /><p>Michael2016<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael2016 has no accepted answers">0%</span></p></div></div><div id="comments-container-53886" class="comments-container"><span id="53891"></span><div id="comment-53891" class="comment"><div id="post-53891-score" class="comment-score"></div><div class="comment-text"><p>Have you tried installing to a different directory, e.g. C:\temp\Wireshark?</p></div><div id="comment-53891-info" class="comment-info"><span class="comment-age">(07 Jul '16, 03:24)</span> grahamb ♦</div></div><span id="53896"></span><div id="comment-53896" class="comment"><div id="post-53896-score" class="comment-score"></div><div class="comment-text"><p>I don't even get that far. As soon as you right click and "run as Administrator" the error pops up.</p></div><div id="comment-53896-info" class="comment-info"><span class="comment-age">(07 Jul '16, 04:16)</span> Michael2016</div></div></div><div id="comment-tools-53886" class="comment-tools"></div><div class="clear"></div><div id="comment-53886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53899"></span>

<div id="answer-container-53899" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53899-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark installer checks for an instance of the shared mutex "Wireshark-is-running-{9CA78EEA-EA4D-4490-9240-FC01FCEF464B}" both for the current user and globally on the system. This mutex is created when any applications of the Wireshark suite are running, and cause the installer to generate the error message shown.</p><p>Using <a href="https://technet.microsoft.com/en-us/sysinternals/bb896653">Process Explorer</a> from SysInternals you can search for all process using this mutex. Running Process Explorer as an administrator, use the Find -&gt; Find Handle or DLL... menu option to search for "Wireshark-is-running" and the process(es) will be listed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '16, 04:49</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53899" class="comments-container"><span id="53901"></span><div id="comment-53901" class="comment"><div id="post-53901-score" class="comment-score"></div><div class="comment-text"><p>graham, I will have to download and test in the morning. Thank you and I will update you then.</p></div><div id="comment-53901-info" class="comment-info"><span class="comment-age">(07 Jul '16, 06:21)</span> Michael2016</div></div><span id="56963"></span><div id="comment-56963" class="comment"><div id="post-56963-score" class="comment-score"></div><div class="comment-text"><p>I was finally able to install Process Explorer and it found 0 matching items. I've thought about building a new system and applying Wireshark first but each time I go to upgrade I'll run into the same problem.</p></div><div id="comment-56963-info" class="comment-info"><span class="comment-age">(04 Nov '16, 00:19)</span> Michael2016</div></div><span id="56966"></span><div id="comment-56966" class="comment"><div id="post-56966-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately there must be something in your system specifically causing this issue as with over 500, 000 downloads per month almost no other users have run into this.</p><p>Can you uninstall Wireshark, reboot and try the install again?</p></div><div id="comment-56966-info" class="comment-info"><span class="comment-age">(04 Nov '16, 02:16)</span> grahamb ♦</div></div></div><div id="comment-tools-53899" class="comment-tools"></div><div class="clear"></div><div id="comment-53899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

