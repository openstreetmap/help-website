+++
type = "question"
title = "Running wireshark on Ubuntu through VMware"
description = '''I&#x27;m on a windows 7 machine and part of my college labs is to capture data in &#x27;monitor mode&#x27;, as we know that is not available on the windows 7 version of wireshark. If I install it on Ubuntu through VMware on the windows machine will I be able to use the monitor mode affectingly'''
date = "2013-10-04T02:11:00Z"
lastmod = "2013-10-04T05:06:00Z"
weight = 25631
keywords = [ "vmware", "linux" ]
aliases = [ "/questions/25631" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Running wireshark on Ubuntu through VMware](/questions/25631/running-wireshark-on-ubuntu-through-vmware)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25631-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm on a windows 7 machine and part of my college labs is to capture data in 'monitor mode', as we know that is not available on the windows 7 version of wireshark. If I install it on Ubuntu through VMware on the windows machine will I be able to use the monitor mode affectingly</p></div><div id="question-tags" class="tags-container tags">vmware linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '13, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/d9330a830d5876526fb59338b0b06463?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IrishFella&#39;s gravatar image" /><p>IrishFella<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IrishFella has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Oct '13, 02:30</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-25631" class="comments-container"></div><div id="comment-tools-25631" class="comment-tools"></div><div class="clear"></div><div id="comment-25631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25639"></span>

<div id="answer-container-25639" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25639-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I <em>think</em> another possibility is to use Microsoft Network Monitor to do the capture and then to use Wireshark to analyze the capture.</p><p>See comment under <a href="http://ask.wireshark.org/questions/9102/unable-to-capture-packets-promiscuously-on-wi-fi-on-windows">unable-to-capture-packets-promiscuously-on-wi-fi-on-windows</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '13, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Oct '13, 05:07</p></div></div><div id="comments-container-25639" class="comments-container"></div><div id="comment-tools-25639" class="comment-tools"></div><div class="clear"></div><div id="comment-25639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25632"></span>

<div id="answer-container-25632" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25632-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not on the internal wlan interface as that is still handled by Windows7 and will be mapped to an ethernet interface on the linux VM.</p><p>You can either:</p><ol><li>Boot your system with a Linux Live CD (like <a href="http://www.kali.org/">Kali</a>)</li><li>Use an USB wifi adapter that is supported by your linux distro and make VMware map the USB wifi adapter to your VM instead of the Windows7 host OS.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '13, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Oct '13, 02:16</p></div></div><div id="comments-container-25632" class="comments-container"></div><div id="comment-tools-25632" class="comment-tools"></div><div class="clear"></div><div id="comment-25632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

