+++
type = "question"
title = "How can I open different pcap files in Wsh portable?"
description = '''Hello! Since Wireshark Version 2.x.x it is impossible to open more than one pcap File. If one pcap file is already openend and I try to open a further one, I got an error message (from Wireshark Portable PortableApps.com Launcher) that one instance of wireshark is still running and that I should clo...'''
date = "2016-09-09T00:15:00Z"
lastmod = "2016-09-09T08:23:00Z"
weight = 55415
keywords = [ "portable" ]
aliases = [ "/questions/55415" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I open different pcap files in Wsh portable?](/questions/55415/how-can-i-open-different-pcap-files-in-wsh-portable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55415-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! Since Wireshark Version 2.x.x it is impossible to open more than one pcap File. If one pcap file is already openend and I try to open a further one, I got an error message (from Wireshark Portable PortableApps.com Launcher) that one instance of wireshark is still running and that I should close all instances. What can I do that I can open more than one pcap file? At present I still use Wireshark Portable Version 1.12.8. to avoid this problem.</p><p>Best regards Andreas</p></div><div id="question-tags" class="tags-container tags">portable</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '16, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/f840458e6277e1cdb3262f4bf6f8fd05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boettcher&#39;s gravatar image" /><p>Boettcher<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boettcher has no accepted answers">0%</span></p></div></div><div id="comments-container-55415" class="comments-container"></div><div id="comment-tools-55415" class="comment-tools"></div><div class="clear"></div><div id="comment-55415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55436"></span>

<div id="answer-container-55436" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55436-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Andreas,</p><p>as far as I know this is a limitation of the PortableApps.com launcher, not from Wireshark (done on purpose if I remember properly to handle the registry redirection). Wireshark 1.12 was built with an older version of PA.com Launcher that was not doing this check.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '16, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-55436" class="comments-container"><span id="55450"></span><div id="comment-55450" class="comment"><div id="post-55450-score" class="comment-score"></div><div class="comment-text"><p>According to the PA.c documentation this should work by default, but it looks like we have to set the [Launch]SingleAppInstance key: <a href="https://code.wireshark.org/review/#/c/17616">https://code.wireshark.org/review/#/c/17616</a></p></div><div id="comment-55450-info" class="comment-info"><span class="comment-age">(09 Sep '16, 15:22)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-55436" class="comment-tools"></div><div class="clear"></div><div id="comment-55436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

