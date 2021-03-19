+++
type = "question"
title = "Uninstalling wireshark 1.6.4"
description = '''I am currently testing wireshark 1.6.4 within an Army environment and have discovered that I can not uninstall this version using the Programs and Features module. Any suggestions on why this is so?'''
date = "2011-12-14T11:21:00Z"
lastmod = "2011-12-16T13:24:00Z"
weight = 7978
keywords = [ "windows", "error", "uninstall" ]
aliases = [ "/questions/7978" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Uninstalling wireshark 1.6.4](/questions/7978/uninstalling-wireshark-164)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7978-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am currently testing wireshark 1.6.4 within an Army environment and have discovered that I can not uninstall this version using the Programs and Features module. Any suggestions on why this is so?</p></div><div id="question-tags" class="tags-container tags">windows error uninstall</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '11, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/a331eac212eb6fb9b90853d2bec4234d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbhunee&#39;s gravatar image" /><p>dbhunee<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbhunee has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Dec '11, 15:39</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-7978" class="comments-container"><span id="8002"></span><div id="comment-8002" class="comment"><div id="post-8002-score" class="comment-score"></div><div class="comment-text"><p>I'm assuming you get an error when you try to uninstall. What is the error message?</p></div><div id="comment-8002-info" class="comment-info"><span class="comment-age">(15 Dec '11, 15:37)</span> helloworld</div></div><span id="8006"></span><div id="comment-8006" class="comment"><div id="post-8006-score" class="comment-score"></div><div class="comment-text"><p>I don't even get the option to uninstall so there is no error message. Wireshark does not show up in Add/Remove programs and there is no uninstall option under the start menu either.</p></div><div id="comment-8006-info" class="comment-info"><span class="comment-age">(16 Dec '11, 05:18)</span> dbhunee</div></div></div><div id="comment-tools-7978" class="comment-tools"></div><div class="clear"></div><div id="comment-7978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8019"></span>

<div id="answer-container-8019" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8019-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure Wireshark is installed? Does <code>C:\Program Files\Wireshark</code> or <code>C:\Program Files (x86)\Wireshark</code> exist? Do the registry keys <code>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Wireshark</code> or <code>HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Wireshark</code> (if you're running 64-bit Windows) exist as described in <a href="http://support.microsoft.com/kb/314481">KB 314481</a>?</p><p>If the Wireshark program files directory exists but the uninstall registry keys don't then it sounds like your installation went awry somewhere. You might try looking for a file named <code>uninstall.exe</code> in the Wireshark program files directory. If it exists then it <em>should</em> remove Wireshark. If it doesn't exist or that doesn't work you might try reinstalling Wireshark, then uninstalling it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '11, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-8019" class="comments-container"><span id="8038"></span><div id="comment-8038" class="comment"><div id="post-8038-score" class="comment-score"></div><div class="comment-text"><p>I found the uninstall.exe in the Program Files directory and successfully uninstalled Wireshark. But when I reinstalled it, the same thing happened. I'm not running a 64-bit Windows machine but I do have group policies on my machine. Do you think this could be the problem?</p></div><div id="comment-8038-info" class="comment-info"><span class="comment-age">(19 Dec '11, 06:54)</span> dbhunee</div></div></div><div id="comment-tools-8019" class="comment-tools"></div><div class="clear"></div><div id="comment-8019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

