+++
type = "question"
title = "1.8.4 doesn&#x27;t install on new computers"
description = '''You guys know you missed something in 1.8.4 right? New install of 1.8.3 a couple days ago, no problem New install of 1.8.4 (two different laptops) today... &quot;missing msvrc100.dll&quot;'''
date = "2012-11-29T09:47:00Z"
lastmod = "2012-11-29T10:35:00Z"
weight = 16434
keywords = [ "installation" ]
aliases = [ "/questions/16434" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [1.8.4 doesn't install on new computers](/questions/16434/184-doesnt-install-on-new-computers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16434-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>You guys know you missed something in 1.8.4 right?</p><p>New install of 1.8.3 a couple days ago, no problem</p><p>New install of 1.8.4 (two different laptops) today... "missing msvrc100.dll"</p></div><div id="question-tags" class="tags-container tags">installation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '12, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/4236f30a4fa840a16a367eb6364c022b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="uncleboarder&#39;s gravatar image" /><p>uncleboarder<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="uncleboarder has no accepted answers">0%</span></p></div></div><div id="comments-container-16434" class="comments-container"><span id="16435"></span><div id="comment-16435" class="comment"><div id="post-16435-score" class="comment-score"></div><div class="comment-text"><p>Can you provide a little more detail? Which version(s) of Windows? 32-bit or 64-bit?</p></div><div id="comment-16435-info" class="comment-info"><span class="comment-age">(29 Nov '12, 10:11)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-16434" class="comment-tools"></div><div class="clear"></div><div id="comment-16434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16436"></span>

<div id="answer-container-16436" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16436-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is msvcr100.dll (note the spelling) present in <code>c:\Program Files\Wireshark</code> (or <code>c:\Program Files (x86)\Wireshark</code> if you installed the 32-bit executable on a 64-bit system)? Are you running any AV software that might have quarantined this file?</p><p>If I run the 32-bit installer (Wireshark-win32-1.8.4.exe) on a Windows XP 32-bit system here the installer log has the line</p><pre><code> Extract: msvcr100.dll</code></pre><p>about a tenth of the way from the top. Msvcr100.dll is present in <code>c:\Program\Files\Wireshark</code> and running Dependency Walker on wireshark.exe shows that msvcr100.dll is loaded successfully from that directory. Finally, running wireshark.exe works as expected.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '12, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-16436" class="comments-container"><span id="16437"></span><div id="comment-16437" class="comment"><div id="post-16437-score" class="comment-score"></div><div class="comment-text"><p>I installed the 64bit version of 1.8.4... it failed. I installed it again... it failed. I installed the 64bit version of 1.6.12... it worked fine.</p><p>I'm not really looking for an answer as 1.6.12 is ok for my needs. But I wanted to let you know what I experienced.</p><p>Thanks for a great product!</p></div><div id="comment-16437-info" class="comment-info"><span class="comment-age">(29 Nov '12, 11:57)</span> uncleboarder</div></div><span id="16438"></span><div id="comment-16438" class="comment"><div id="post-16438-score" class="comment-score"></div><div class="comment-text"><p>Can you try installing 1.8.4 again? About a tenth of the way down in the installer log (the last screen of the installer) you <em>should</em> see the following:</p><pre><code>Extract: vcredist_x64.exe... 100%
Execute: &quot;C:\Program Files\Wireshark\vcredist_x64.exe&quot; /q /norestart
vcredist_x64 returned 0</code></pre><p>After the installation you should also have "Microsoft Visual C++ 2010 x86 Redistributable - 10.0.40219" listed in the Programs and Features control panel.</p></div><div id="comment-16438-info" class="comment-info"><span class="comment-age">(29 Nov '12, 12:24)</span> Gerald Combs ♦♦</div></div><span id="16444"></span><div id="comment-16444" class="comment"><div id="post-16444-score" class="comment-score"></div><div class="comment-text"><p>Installing 1.8.4 after having installed 1.6.12... I no longer have the problem. (all 64 bit versions)</p><p>I can only assume the uninstallation of 1.6.12, did not uninstall the .dll. I actually did the install 4 times on two different computers before reverting to 1.6.12.</p><p>The laptops are now deployed at a remote location to solve a problem.</p></div><div id="comment-16444-info" class="comment-info"><span class="comment-age">(29 Nov '12, 17:51)</span> uncleboarder</div></div></div><div id="comment-tools-16436" class="comment-tools"></div><div class="clear"></div><div id="comment-16436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

