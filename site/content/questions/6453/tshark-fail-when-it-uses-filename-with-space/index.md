+++
type = "question"
title = "tshark fail when it uses filename with space"
description = '''tshark in commonline fail if the pcap file name contain spaces. example1: tshark -r d:中文 test.pcap example2: tshark -r C:Documents and SettingsAdministrator桌面test.pcap why wireshark GUI can open and disscet the file whose name contain spaces, how to solve the problem when using tshark?'''
date = "2011-09-19T23:37:00Z"
lastmod = "2011-09-19T23:50:00Z"
weight = 6453
keywords = [ "tshark", "space" ]
aliases = [ "/questions/6453" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark fail when it uses filename with space](/questions/6453/tshark-fail-when-it-uses-filename-with-space)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6453-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>tshark in commonline fail if the pcap file name contain spaces.</p><p>example1: tshark -r d:中文 test.pcap example2: tshark -r C:Documents and SettingsAdministrator桌面test.pcap</p><p>why wireshark GUI can open and disscet the file whose name contain spaces, how to solve the problem when using tshark?</p></div><div id="question-tags" class="tags-container tags">tshark space</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '11, 23:37</strong></p><img src="https://secure.gravatar.com/avatar/a5a3214300b3b17fc46c3b656b7bed01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ylda_ljm0620&#39;s gravatar image" /><p>ylda_ljm0620<br />
<span class="score" title="31 reputation points">31</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ylda_ljm0620 has no accepted answers">0%</span></p></div></div><div id="comments-container-6453" class="comments-container"></div><div id="comment-tools-6453" class="comment-tools"></div><div class="clear"></div><div id="comment-6453-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6454"></span>

<div id="answer-container-6454" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6454-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Because the Wireshark GUI, unlike the Windows cmd.exe command line and the UN*X command line, does not use spaces as command-line token separators.</p><p>If you want to access, from the command line, a file whose name contains spaces - or any <em>other</em> character that's a special character to the command interpreter - you have to quote it:</p><pre><code>tshark -r &quot;C:\\Documents and Settings\\Administrator\\桌面test.pcap&quot;</code></pre><p>This applies to <em>all</em> programs, not just TShark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '11, 23:50</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6454" class="comments-container"></div><div id="comment-tools-6454" class="comment-tools"></div><div class="clear"></div><div id="comment-6454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

