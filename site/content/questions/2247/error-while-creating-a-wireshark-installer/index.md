+++
type = "question"
title = "Error while creating a wireshark installer"
description = '''After having successfully compiled wireshark on windows, I tried to create a windows installer. I am getting the following error on doing a &#x27;nmake -f Makefile.nmake build wireshark installer&#x27; **File: &quot;C:Userst_sidharth1wswinwiresharkwin32vcredist_x86.exe&quot; -&amp;gt; no files found. Usage: File [/nonfatal...'''
date = "2011-02-08T22:25:00Z"
lastmod = "2011-03-23T06:19:00Z"
weight = 2247
keywords = [ "installer", "wireshark" ]
aliases = [ "/questions/2247" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Error while creating a wireshark installer](/questions/2247/error-while-creating-a-wireshark-installer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2247-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After having successfully compiled wireshark on windows, I tried to create a windows installer. I am getting the following error on doing a 'nmake -f Makefile.nmake build wireshark installer'</p><p>**File: "C:Userst_sidharth1wswinwiresharkwin32vcredist_x86.exe" -&gt; no files found.</p><p>Usage: File [/nonfatal] [/a] ([/r] [/x filespec [...]] filespec [...] | /oname=outfile one_file_only)</p><p>Error in script "wireshark.nsi" on line 423 -- aborting creation process</p><p>NMAKE : fatal error U1077: '"C:Program Files (x86)NSISmakensis.exe"' : return code '0x1'</p><p>Stop.</p><p>NMAKE : fatal error U1077: '"C:Program Files (x86)Microsoft Visual Studio 9.0 VCBINnmake.exe"' : return code '0x2'</p><p>Stop.**</p></div><div id="question-tags" class="tags-container tags">installer wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '11, 22:25</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p>sid<br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-2247" class="comments-container"><span id="2248"></span><div id="comment-2248" class="comment"><div id="post-2248-score" class="comment-score"></div><div class="comment-text"><p>Perhaps you need to install the vcredist.. ref the developers guide.</p></div><div id="comment-2248-info" class="comment-info"><span class="comment-age">(08 Feb '11, 22:55)</span> Anders ♦</div></div><span id="2250"></span><div id="comment-2250" class="comment"><div id="post-2250-score" class="comment-score"></div><div class="comment-text"><p>I have downloaded vcredist_x86.exe from microsoft.com and I have installed it. But while installation it does not ask for a path as to where I want to install that.</p><p>So where exactly do I need to install the vcredist_x86.exe? And on installation of this redistributable, what files exactly come up??</p></div><div id="comment-2250-info" class="comment-info"><span class="comment-age">(09 Feb '11, 00:40)</span> sid</div></div><span id="2251"></span><div id="comment-2251" class="comment"><div id="post-2251-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Is it possible to make an installer without installing vcredist? Because, in my case, I'm not admin on my computer so I can't install vcredist.</p></div><div id="comment-2251-info" class="comment-info"><span class="comment-age">(09 Feb '11, 00:41)</span> Alwik</div></div><span id="2252"></span><div id="comment-2252" class="comment"><div id="post-2252-score" class="comment-score"></div><div class="comment-text"><p>I don't think so..redistributable files are necessary for the runtime.</p><p>Try downloading the msvcr90.dll from the internet and using it. It might work. But I am not completely sure on it.</p><p>What is the harm in trying afterall.</p><p>sid</p></div><div id="comment-2252-info" class="comment-info"><span class="comment-age">(09 Feb '11, 02:04)</span> sid</div></div></div><div id="comment-tools-2247" class="comment-tools"></div><div class="clear"></div><div id="comment-2247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="2318"></span>

<div id="answer-container-2318" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2318-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you can't even create the installer, then it likely means that you don't have a copy of <code>vcredist_x86.exe</code> saved in your wireshark library directory. By default, this is <code>C:\wireshark-win32-libs\</code>, but it appears you have a non-standard path.</p><p>Reference: <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">Create a Wireshark Installer</a>, section 2.2.13.2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '11, 18:07</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Feb '11, 13:05</p></div></div><div id="comments-container-2318" class="comments-container"></div><div id="comment-tools-2318" class="comment-tools"></div><div class="clear"></div><div id="comment-2318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2712"></span>

<div id="answer-container-2712" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2712-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have solved my problem by installing Visual Studio but not the Express Edition. Now Wireshark is well installed, but when I'm trying to launch it, i got a pop-up telling me that i may reinstall wireshark because it's not correctly configured. Any idea?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '11, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/ba2f649bff02f743f2c105a41494c0f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alwik&#39;s gravatar image" /><p>Alwik<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alwik has one accepted answer">25%</span></p></div></div><div id="comments-container-2712" class="comments-container"></div><div id="comment-tools-2712" class="comment-tools"></div><div class="clear"></div><div id="comment-2712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3040"></span>

<div id="answer-container-3040" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3040-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The solution is to install visual C++ SP1</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '11, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/ba2f649bff02f743f2c105a41494c0f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alwik&#39;s gravatar image" /><p>Alwik<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alwik has one accepted answer">25%</span></p></div></div><div id="comments-container-3040" class="comments-container"></div><div id="comment-tools-3040" class="comment-tools"></div><div class="clear"></div><div id="comment-3040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3041"></span>

<div id="answer-container-3041" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3041-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The solution is to install the visual C++ <strong>SP1</strong></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '11, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/ba2f649bff02f743f2c105a41494c0f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alwik&#39;s gravatar image" /><p>Alwik<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alwik has one accepted answer">25%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Mar '11, 06:20</p></div></div><div id="comments-container-3041" class="comments-container"></div><div id="comment-tools-3041" class="comment-tools"></div><div class="clear"></div><div id="comment-3041-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

