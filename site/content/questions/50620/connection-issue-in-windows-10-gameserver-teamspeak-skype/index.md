+++
type = "question"
title = "Connection issue in Windows 10 (gameserver, teamspeak, skype)"
description = '''Hello, with Windows 10 I have problems connecting to the servers of a certain game. The same connection via WLAN and my Win7 Laptop works without problem. It&#x27;s most certainly not a firewall (Windows) or Antivirus (Panda) issue since I turned both off and experience the same problem. The serverlist c...'''
date = "2016-03-01T10:53:00Z"
lastmod = "2016-03-01T12:33:00Z"
weight = 50620
keywords = [ "windows10", "tcp" ]
aliases = [ "/questions/50620" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Connection issue in Windows 10 (gameserver, teamspeak, skype)](/questions/50620/connection-issue-in-windows-10-gameserver-teamspeak-skype)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50620-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>with Windows 10 I have problems connecting to the servers of a certain game. The same connection via WLAN and my Win7 Laptop works without problem. It's most certainly not a firewall (Windows) or Antivirus (Panda) issue since I turned both off and experience the same problem. The serverlist cannot be loaded at all. Moreover I discovered that I can't load Teamspeak servers as well and cant connect to Skype too. Everything else works just fine. I captured the Ethernet traffic while trying to connect to the Game-Servers but I don't know what to look for. Hopefully some of you can help me with that.</p><p><a href="http://www.blankwebsite.com">Link deleted</a></p><p>Many thanks in advance.</p></div><div id="question-tags" class="tags-container tags">windows10 tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '16, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/e0e3704fa3e09e6019036a6266a774f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nikola&#39;s gravatar image" /><p>Nikola<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nikola has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Mar '16, 12:35</p></div></div><div id="comments-container-50620" class="comments-container"></div><div id="comment-tools-50620" class="comment-tools"></div><div class="clear"></div><div id="comment-50620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50633"></span>

<div id="answer-container-50633" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50633-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The issue is related with Panda Free Antivirus after all. In the Network adapter properties, there is a entry "Network Activity Hook Server LightWeight Filter Driver" (NAHSD). That is causing the issue, even when the protection is turned off. Unselecting this element in the properties fixes the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '16, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/e0e3704fa3e09e6019036a6266a774f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nikola&#39;s gravatar image" /><p>Nikola<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nikola has one accepted answer">100%</span></p></div></div><div id="comments-container-50633" class="comments-container"></div><div id="comment-tools-50633" class="comment-tools"></div><div class="clear"></div><div id="comment-50633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

