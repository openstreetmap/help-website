+++
type = "question"
title = "Windows cannot find &#x27;C:&#92;Program Files (x86)&#92;Wireshark&#92;Wireshark.exe&#x27;"
description = '''Hello whenever i open wireshark it says Windows cannot find &#x27;C:&#92;Program Files (x86)&#92;Wireshark&#92;Wireshark.exe&#x27; i don&#x27;t know what it is but i try reinstalling wireshark nothing happens just keep saying same thing whenever i re open it please help!'''
date = "2017-03-11T18:21:00Z"
lastmod = "2017-03-12T14:56:00Z"
weight = 60009
keywords = [ "start", "wireshark" ]
aliases = [ "/questions/60009" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Windows cannot find 'C:\\Program Files (x86)\\Wireshark\\Wireshark.exe'](/questions/60009/windows-cannot-find-cprogram-files-x86wiresharkwiresharkexe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60009-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello whenever i open wireshark it says Windows cannot find 'C:\Program Files (x86)\Wireshark\Wireshark.exe' i don't know what it is but i try reinstalling wireshark nothing happens just keep saying same thing whenever i re open it please help!</p></div><div id="question-tags" class="tags-container tags">start wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '17, 18:21</strong></p><img src="https://secure.gravatar.com/avatar/5a6edd4e6833cf5563129f198fb0c5f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiresharkuser600&#39;s gravatar image" /><p>wiresharkuse...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiresharkuser600 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Mar '17, 14:57</p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span></p></div></div><div id="comments-container-60009" class="comments-container"></div><div id="comment-tools-60009" class="comment-tools"></div><div class="clear"></div><div id="comment-60009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60018"></span>

<div id="answer-container-60018" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60018-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you using the 64-bit version or the 32-bit version of Wireshark?</p><p>Windows is using the following scheme to store applications:</p><p><strong>32-bit systems</strong></p><p>On 32-bit systems all applications will be stored in a subdirectory of C:\Program Files</p><p><strong>64-bit systems</strong></p><p>On 64-bit systems the destination folder depends on the architecture, for which is was build:</p><ul><li>64-bit applications will be stored in C:\Program Files</li><li>32-bit applications running on a 64-bit system will be stored in C:\Program Files (x86)</li></ul><p><strong>Your error message ...</strong></p><p>... might be the result of a version mixup. Wireshark is available as 32-bit and 64-bit version.</p><p>If you were using 32-bit version of Wireshark an created a desktop icon, this would launch the application. When updating to a 64-bit version without changing the icon properties you might get an error message.</p><p><strong>... and how to get around it</strong></p><p>The are multiple ways to launch Wireshark:</p><ul><li>Use the Windows explorer to navigate to the correct folder and doubleclick Wireshark.exe</li><li>Right-click the Wireshark icon that triggers the error message, select properties and update the target to point to the correct destination</li><li>Trust in the Wireshark installer and let the installer create a desktop icon</li><li>Use the application link from the start button.</li></ul><p>Good hunting</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '17, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-60018" class="comments-container"></div><div id="comment-tools-60018" class="comment-tools"></div><div class="clear"></div><div id="comment-60018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

