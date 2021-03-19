+++
type = "question"
title = "Wireshark and WinPcap on Win 7"
description = '''Hi, I have worked with WinPcap site with no luck when I try and install WinPcap native or through Wireshark I get a message it is already installed when this is a new win 7 install. I can see that others have had this problem but I see no solutions? I have a network down and need help Thanks!'''
date = "2012-05-16T09:05:00Z"
lastmod = "2012-05-16T09:58:00Z"
weight = 11050
keywords = [ "winpcap", "installation" ]
aliases = [ "/questions/11050" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark and WinPcap on Win 7](/questions/11050/wireshark-and-winpcap-on-win-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11050-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have worked with WinPcap site with no luck when I try and install WinPcap native or through Wireshark I get a message it is already installed when this is a new win 7 install.</p><p>I can see that others have had this problem but I see no solutions?</p><p>I have a network down and need help</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">winpcap installation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '12, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/6f703ed8c6924804dff964225f073a46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="melliott-aerohive&#39;s gravatar image" /><p>melliott-aer...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="melliott-aerohive has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '12, 13:13</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-11050" class="comments-container"></div><div id="comment-tools-11050" class="comment-tools"></div><div class="clear"></div><div id="comment-11050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11056"></span>

<div id="answer-container-11056" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11056-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ul><li>What version of Winpcap did you try to install (maybe the version you tried is not supported on windows 7 (64bit)?</li><li><p>What is the output of this command:</p><blockquote><p><code>runas /user:administrator sc qc npf</code></p></blockquote></li><li>What version of Win7 (32/64 Bit, SP1) is installed?</li><li>Does this file exist on your system: system32/drivers/npf.sys?</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '12, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '12, 10:38</p></div></div><div id="comments-container-11056" class="comments-container"><span id="11057"></span><div id="comment-11057" class="comment"><div id="post-11057-score" class="comment-score"></div><div class="comment-text"><p>Win 7, 64bit, SP1</p><p>Yes there is a npf.sys and npfs.sys</p></div><div id="comment-11057-info" class="comment-info"><span class="comment-age">(16 May '12, 10:39)</span> melliott-aer...</div></div><span id="11058"></span><div id="comment-11058" class="comment"><div id="post-11058-score" class="comment-score"></div><div class="comment-text"><p>on a clean system?</p></div><div id="comment-11058-info" class="comment-info"><span class="comment-age">(16 May '12, 10:43)</span> Kurt Knochner ♦</div></div><span id="11060"></span><div id="comment-11060" class="comment"><div id="post-11060-score" class="comment-score"></div><div class="comment-text"><p>except for a failed wireshark install yes</p></div><div id="comment-11060-info" class="comment-info"><span class="comment-age">(16 May '12, 11:27)</span> melliott-aer...</div></div><span id="11077"></span><div id="comment-11077" class="comment"><div id="post-11077-score" class="comment-score"></div><div class="comment-text"><p>OK, my network is dead and I really need to capture some packets to find out what is going on.</p><p>Is there anyway to get pcap loaded on a new win 7 sp1 64bit machine where it keeps saying there is already a version running when the only thing I have loaded is wireshark that gave me the initial failure to load pcap.<br />
</p><p>I can't believe that this should be so hard on an state of the art machine</p></div><div id="comment-11077-info" class="comment-info"><span class="comment-age">(16 May '12, 21:07)</span> melliott-aer...</div></div><span id="11083"></span><div id="comment-11083" class="comment"><div id="post-11083-score" class="comment-score"></div><div class="comment-text"><p>you did not provide the output of</p><blockquote><p><code>runas /user:administrator sc qc npf</code></p></blockquote><p>If you want help, you need to give information ;-)</p></div><div id="comment-11083-info" class="comment-info"><span class="comment-age">(17 May '12, 00:32)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11056" class="comment-tools"></div><div class="clear"></div><div id="comment-11056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

