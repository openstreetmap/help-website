+++
type = "question"
title = "Listen on other channels"
description = '''Got it to work using tcpdump on backtrack and am curious now if it works as well for Wireshark.  While using tcpdump, my iPad shows traffic in both directions (src and dst) on channel 44 (5.2 GHz). Channel 6 (2.437 GHz) for example just reports the response (SYN-ACK, ACK, FIN) but not the request (S...'''
date = "2012-04-17T11:13:00Z"
lastmod = "2012-04-17T12:09:00Z"
weight = 10222
keywords = [ "channel" ]
aliases = [ "/questions/10222" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Listen on other channels](/questions/10222/listen-on-other-channels)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10222-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Got it to work using tcpdump on backtrack and am curious now if it works as well for Wireshark. While using tcpdump, my iPad shows traffic in both directions (src and dst) on channel 44 (5.2 GHz). Channel 6 (2.437 GHz) for example just reports the response (SYN-ACK, ACK, FIN) but not the request (SYN). Is there an option to change channels in Wireshark? Looks like that one is just listening on channel 6 since I get the same response as on backtrack for that specific channel.</p></div><div id="question-tags" class="tags-container tags">channel</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '12, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/226ddde2171f24757130ed8d47d5374c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="albert&#39;s gravatar image" /><p>albert<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="albert has no accepted answers">0%</span></p></div></div><div id="comments-container-10222" class="comments-container"></div><div id="comment-tools-10222" class="comment-tools"></div><div class="clear"></div><div id="comment-10222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10224"></span>

<div id="answer-container-10224" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10224-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If "backtrace" means Backtrack Linux, no, there's currently no option <em>in Wireshark</em> to change channels; the only current Wireshark UI for controlling channels is for the Windows-only AirPcap adapter. You'd have to change the channel yourself, from the command line (which is what you've presumably done with tcpdump, as it has no channel-changing option either).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '12, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10224" class="comments-container"></div><div id="comment-tools-10224" class="comment-tools"></div><div class="clear"></div><div id="comment-10224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

