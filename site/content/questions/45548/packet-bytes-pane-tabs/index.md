+++
type = "question"
title = "packet bytes  pane tabs"
description = '''I am trying to get my Wireshark to decrypt SSL traffic from my PC when I authenticate to a site to see what format is used when sending the username to the server. I am following the instructions on a tutorial from this site https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wiresh...'''
date = "2015-08-31T09:56:00Z"
lastmod = "2015-08-31T18:00:00Z"
weight = 45548
keywords = [ "tabs", "wireshark" ]
aliases = [ "/questions/45548" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [packet bytes pane tabs](/questions/45548/packet-bytes-pane-tabs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45548-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to get my Wireshark to decrypt SSL traffic from my PC when I authenticate to a site to see what format is used when sending the username to the server. I am following the instructions on a tutorial from this site <a href="https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/">https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/</a></p><p>Problem is I do not see any tabs at the bottom of the screen in the packet bytes pane. Is there a setting to display those? For what I see in the tutorial, there is a Frame tab, Reassembled TCP tab and Decrypted SSL Data but I do not see any of them on mine.</p><p>Any pointers, ideas or thoughts?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">tabs wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '15, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/f554e51bc7f58f36be9bab382018204e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="troubleshooter141&#39;s gravatar image" /><p>troubleshoot...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="troubleshooter141 has no accepted answers">0%</span></p></div></div><div id="comments-container-45548" class="comments-container"></div><div id="comment-tools-45548" class="comment-tools"></div><div class="clear"></div><div id="comment-45548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45557"></span>

<div id="answer-container-45557" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45557-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Problem is I do not see any tabs at the bottom of the screen in the packet bytes pane. Is there a setting to display those? For what I see in the tutorial, there is a Frame tab, Reassembled TCP tab and Decrypted SSL Data but I do not see any of them on mine.</p></blockquote><p>Perhaps 1) there's no reassembly being done and 2) there's no decrypting being done, so there's nothing to display in those tabs, so Wireshark can't and doesn't display them (there's the raw frame data, but you won't get tabs if there's only one source of data).</p><p>We'd have to see your capture to determine what's going on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '15, 18:00</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-45557" class="comments-container"></div><div id="comment-tools-45557" class="comment-tools"></div><div class="clear"></div><div id="comment-45557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

