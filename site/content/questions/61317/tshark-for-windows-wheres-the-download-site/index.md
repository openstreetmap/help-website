+++
type = "question"
title = "TShark for Windows - Where&#x27;s the download site?"
description = '''I can find the TShark documentation but the links to download it are invalid. Anyone know where I can download Wireshark for Windows? Thanks'''
date = "2017-05-09T21:57:00Z"
lastmod = "2017-05-10T00:18:00Z"
weight = 61317
keywords = [ "download", "installer", "link", "tshark", "location" ]
aliases = [ "/questions/61317" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TShark for Windows - Where's the download site?](/questions/61317/tshark-for-windows-wheres-the-download-site)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61317-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can find the TShark documentation but the links to download it are invalid. Anyone know where I can download Wireshark for Windows?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">download installer link tshark location</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '17, 21:57</strong></p><img src="https://secure.gravatar.com/avatar/97ea735c14c6ab8964c27283351e1500?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Doug-Spindler&#39;s gravatar image" /><p>Doug-Spindler<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Doug-Spindler has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 May '17, 06:13</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-61317" class="comments-container"><span id="61334"></span><div id="comment-61334" class="comment"><div id="post-61334-score" class="comment-score"></div><div class="comment-text"><p><em>but the links to download it are invalid</em></p><p>Which links are invalid? Maybe contact the site administrator(s) and ask them to update their invalid links.</p></div><div id="comment-61334-info" class="comment-info"><span class="comment-age">(10 May '17, 06:14)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-61317" class="comment-tools"></div><div class="clear"></div><div id="comment-61317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61319"></span>

<div id="answer-container-61319" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61319-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Tshark is part of the Wireshark installer that can be downloaded <a href="https://www.wireshark.org/#download">here</a>. During the installation, you can choose to install tshark (actvated by default) and once completed, you will find it in your installation folder.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '17, 00:18</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-61319" class="comments-container"><span id="61322"></span><div id="comment-61322" class="comment"><div id="post-61322-score" class="comment-score"></div><div class="comment-text"><p>Note that the Wireshark installer does NOT add the Wireshark binary directory to the path.</p><p>To use <code>tshark.exe</code> you can:</p><ol><li>Type the full path every time you use <code>tshark.exe</code>, e.g., <code>C:\Program Files\Wireshark\tshark.exe</code></li><li>Change directories to the Wireshark installation directory before running <code>tshark.exe</code>, just don't attempt to write capture files to that directory.</li><li>Manually add the Wireshark installation directory to your path before running <code>tshark.exe</code>, e.g., <code>SET "PATH=%PATH%;C:\Program Files\Wireshark"</code>, assuming that's where Wireshark is installed on your system.</li><li>Modify your <code>%PATH%</code> environment variable to include the Wireshark installation directory so you don't have to keep manually modifying it each time. For Windows 10: <em>Start Menu -&gt; Control Panel -&gt; All Control Panel Items -&gt; System -&gt; Advanced system settings -&gt; Environment Variables... -&gt; System variables -&gt; Path -&gt; Edit -&gt; New -&gt; C:\Program Files\Wireshark -&gt; OK -&gt; OK -&gt; OK</em> You will need to restart your <code>cmd.exe</code> command prompt for the <code>%PATH%</code> to be updated.</li><li>If you have moved on from cmd.exe and embraced Powershell, then set up an alias, e.g. <code>New-Alias tshark "C:\Program Files\Wireshark\tshark.exe"</code>, I have such an entry (alongside the other executables in the Wireshark suite) in my PS profile.</li></ol></div><div id="comment-61322-info" class="comment-info"><span class="comment-age">(10 May '17, 03:48)</span> grahamb ♦</div></div></div><div id="comment-tools-61319" class="comment-tools"></div><div class="clear"></div><div id="comment-61319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

