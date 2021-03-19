+++
type = "question"
title = "download Wireshark for AIX"
description = '''Please can anybody let me know if we can user wireshark on AIX 6.1, if so please guide me to a download link.  Or please suggest a good tool which can be used for network analysis of a AIX 6.1. Regards,  Dhrajj'''
date = "2011-03-02T17:00:00Z"
lastmod = "2013-07-25T18:14:00Z"
weight = 2643
keywords = [ "dowload", "aix", "for", "wireshark" ]
aliases = [ "/questions/2643" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [download Wireshark for AIX](/questions/2643/download-wireshark-for-aix)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2643-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Please can anybody let me know if we can user wireshark on AIX 6.1, if so please guide me to a download link. Or please suggest a good tool which can be used for network analysis of a AIX 6.1.</p><p>Regards, Dhrajj</p></div><div id="question-tags" class="tags-container tags">dowload aix for wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '11, 17:00</strong></p><img src="https://secure.gravatar.com/avatar/641d24d4e02df5c6058a0a1a482a5985?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dhrajj&#39;s gravatar image" /><p>dhrajj<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dhrajj has no accepted answers">0%</span></p></div></div><div id="comments-container-2643" class="comments-container"></div><div id="comment-tools-2643" class="comment-tools"></div><div class="clear"></div><div id="comment-2643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23345"></span>

<div id="answer-container-23345" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23345-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The third-party packages section of [the Wireshark download page[1] has a "*/*" entry, which is a perhaps somewhat cryptic way of saying "several vendors and several platforms"; it points to the site for a company called <a href="http://www.thewrittenword.com">The Written Word</a>, who offer pre-compiled binaries of various packages for various operating systems. They charge for the packages, but provide support.</p><p>perzl.org also offers free-software binaries for AIX; it has <a href="http://www.perzl.org/aix/index.php?n=Main.Wireshark">a Wireshark package</a>. They appear to be packaged as RPMs; I don't know what tools are required to install RPMs on AIX.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '13, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23345" class="comments-container"></div><div id="comment-tools-23345" class="comment-tools"></div><div class="clear"></div><div id="comment-23345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23373"></span>

<div id="answer-container-23373" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23373-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>AIX ships with iptrace(1) and tcpdump(1), either of which can be used for packet captures.</p><p>Wireshark will read/display iptrace files, but the other utilities (mergecap, editcap, etc.) won't work on iptrace files without playing some games with options. Of course, Wireshark and all its utilities read tcpdump(1) files, since they're written in pcap format.</p><p>I usually recommend that AIX folks collect data with tcpdump, then use Wireshark on another system (e.g. a Windows/Mac/Linux desktop/laptop) to analyze the results. Building Wireshark from source on AIX can be a chore, especially if you want to build in support for other third-party libraries like GNU crypto, Kerberos, c-ares, and the like...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '13, 18:14</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-23373" class="comments-container"></div><div id="comment-tools-23373" class="comment-tools"></div><div class="clear"></div><div id="comment-23373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

