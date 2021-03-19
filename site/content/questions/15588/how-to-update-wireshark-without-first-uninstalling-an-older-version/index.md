+++
type = "question"
title = "How to update wireshark without first uninstalling an older version"
description = '''Hello, I&#x27;d like to update wireshark (on windows xp) but without first uninstalling the previous version in order not to lose my configurations. Can someone tell how? Many thanks in advance.'''
date = "2012-11-06T08:39:00Z"
lastmod = "2012-11-06T08:53:00Z"
weight = 15588
keywords = [ "configuration", "update", "install" ]
aliases = [ "/questions/15588" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to update wireshark without first uninstalling an older version](/questions/15588/how-to-update-wireshark-without-first-uninstalling-an-older-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15588-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'd like to update wireshark (on windows xp) but without first uninstalling the previous version in order not to lose my configurations. Can someone tell how?</p><p>Many thanks in advance.</p></div><div id="question-tags" class="tags-container tags">configuration update install</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '12, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/8b48b19068e4fb96fdc1a73a9811edc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nouvelle&#39;s gravatar image" /><p>nouvelle<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nouvelle has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Nov '12, 12:55</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-15588" class="comments-container"></div><div id="comment-tools-15588" class="comment-tools"></div><div class="clear"></div><div id="comment-15588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15589"></span>

<div id="answer-container-15589" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15589-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can just deinstall the old version and tell the uninstaller to leave your configuration files where they are. That way you can upgrade without losing anything.</p><p>If you do not trust the deinstallation routine to do it right you can also backup your settings manually first. They're at C:\Documents and Settings\YourUserName\Application Data\Wireshark. Just copy the files to a safe location.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '12, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Nov '12, 08:47</p></div></div><div id="comments-container-15589" class="comments-container"></div><div id="comment-tools-15589" class="comment-tools"></div><div class="clear"></div><div id="comment-15589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15591"></span>

<div id="answer-container-15591" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15591-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There should be no problem at all if you just install a new version over an older one.</p><p>Two reasons:</p><ol><li><p>During installation you will be asked, if the older version shall be uninstalled first. If you answer with NO, the installation routine will just install the new version over the old one. You won't loose your configuration.</p></li><li><p>If you decide to uninstall the old version, the uninstall routine will ask you if you want to keep your personal data. If you keep them, you won't loose your configuration.</p></li></ol><p>An alternative would be the portable version of Wireshark. You don't have to install that version, just unpack it to a folder. HOWEVER: You must install WinPcap, if you want to capture data from an interface.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '12, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-15591" class="comments-container"></div><div id="comment-tools-15591" class="comment-tools"></div><div class="clear"></div><div id="comment-15591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

