+++
type = "question"
title = "wireshark hangs up by VPN sniffing"
description = '''hello  i will observ my VPN connection. first i start my VPN and then Wireshark to sniff on tun device. after my work in VPN and stops my VPN client wireshark is &quot;dead&quot; i can only &quot;kill&quot; them. i can not save or close wireshark - only the kill helps  can i save the &quot;temp-file&quot; they wireshark make at ...'''
date = "2012-04-23T08:02:00Z"
lastmod = "2012-04-23T09:02:00Z"
weight = 10400
keywords = [ "vpn", "troubleshooting" ]
aliases = [ "/questions/10400" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark hangs up by VPN sniffing](/questions/10400/wireshark-hangs-up-by-vpn-sniffing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10400-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello</p><p>i will observ my VPN connection. first i start my VPN and then Wireshark to sniff on tun device. after my work in VPN and stops my VPN client wireshark is "dead" i can only "kill" them. i can not save or close wireshark - only the kill helps</p><p>can i save the "temp-file" they wireshark make at sniffing?</p><p>thx for help</p></div><div id="question-tags" class="tags-container tags">vpn troubleshooting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '12, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/26f96913d49a193b5a3627971b28c539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="majestyx&#39;s gravatar image" /><p>majestyx<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="majestyx has no accepted answers">0%</span></p></div></div><div id="comments-container-10400" class="comments-container"></div><div id="comment-tools-10400" class="comment-tools"></div><div class="clear"></div><div id="comment-10400-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10402"></span>

<div id="answer-container-10402" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10402-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The hang is probably due to the stopping of the VPN client which usually "disconnects" a virtual network interface. You can salvage the temp file Wireshark wrote though. While capturing you'll see the name and path of the temporary file in the status bar to the left. After you terminated Wireshark the hard way you can find the file at the specified location, usually your system temp path.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '12, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10402" class="comments-container"></div><div id="comment-tools-10402" class="comment-tools"></div><div class="clear"></div><div id="comment-10402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

