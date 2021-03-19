+++
type = "question"
title = "Can&#x27;t Enable SNMP Decodes in 64 bit Windows"
description = '''I&#x27;m running Wireshark 1.4.1 on Windows 7 x64. I&#x27;m trying to enable SNMP decodes, but can&#x27;t. Under Preferences - Name Resolution, I&#x27;ve got the options for Enable OID Resolution and Suppress SMI Errors, but both have the entry &quot;N/A&quot;, I can&#x27;t check / uncheck them. I also don&#x27;t have an SNMP directory un...'''
date = "2010-11-09T08:01:00Z"
lastmod = "2010-11-09T13:59:00Z"
weight = 878
keywords = [ "windows", "1.4.1", "snmp", "64-bit" ]
aliases = [ "/questions/878" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't Enable SNMP Decodes in 64 bit Windows](/questions/878/cant-enable-snmp-decodes-in-64-bit-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-878-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running Wireshark 1.4.1 on Windows 7 x64. I'm trying to enable SNMP decodes, but can't.</p><p>Under Preferences - Name Resolution, I've got the options for Enable OID Resolution and Suppress SMI Errors, but both have the entry "N/A", I can't check / uncheck them. I also don't have an SNMP directory under the Wireshark system directory.</p><p>This is a brand new install and I've tried uninstalling / reinstalling. Am I missing a module? I didn't see anything in the installer.</p><p>So, what do I need to do to enable SNMP decodes with MIBs?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">windows 1.4.1 snmp 64-bit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '10, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/846ee9e7b2fa95d07a234d40b3ae20d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlecIs&#39;s gravatar image" /><p>AlecIs<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlecIs has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jan '12, 12:30</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-878" class="comments-container"></div><div id="comment-tools-878" class="comment-tools"></div><div class="clear"></div><div id="comment-878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="887"></span>

<div id="answer-container-887" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-887-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark needs libsmi to do that. There's no 64bit version of that library yet. To make it work install 32bit Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '10, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-887" class="comments-container"><span id="8567"></span><div id="comment-8567" class="comment"><div id="post-8567-score" class="comment-score"></div><div class="comment-text"><p>FYI, libsmi supports 64-bit now.</p><pre><code>$ file /usr/lib/libsmi.so.2.0.27 
/usr/lib/libsmi.so.2.0.27: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, BuildID[sha1]=0x56bff7c8275830abed32367f5256ef8a8e432a8a, stripped</code></pre><p>I'm on Arch Linux using <a href="http://aur.archlinux.org/packages.php?ID=29078">this</a> package.</p></div><div id="comment-8567-info" class="comment-info"><span class="comment-age">(23 Jan '12, 11:01)</span> mitch_feaster</div></div><span id="8570"></span><div id="comment-8570" class="comment"><div id="post-8570-score" class="comment-score"></div><div class="comment-text"><p>The question refers to Windows, not Linux. However libsmi has now been added to Windows 64 bit, but from the <a href="http://www.wireshark.org/docs/relnotes/wireshark-1.6.5.html">1.6.5</a> release notes it would appear that it is only available in the 1.7 development releases.</p></div><div id="comment-8570-info" class="comment-info"><span class="comment-age">(23 Jan '12, 12:04)</span> grahamb ♦</div></div></div><div id="comment-tools-887" class="comment-tools"></div><div class="clear"></div><div id="comment-887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

