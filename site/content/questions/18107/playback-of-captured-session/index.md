+++
type = "question"
title = "Playback of captured session"
description = '''Hi: Can wireshark playback a captured tcpip session between a client and a server? For the playback can the ip addresses be changed, for example the client and server are moved to a different subnet. Can the capture and playback use a mac address instead of an ip address? Thank you!'''
date = "2013-01-30T09:17:00Z"
lastmod = "2013-01-30T10:19:00Z"
weight = 18107
keywords = [ "playback" ]
aliases = [ "/questions/18107" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Playback of captured session](/questions/18107/playback-of-captured-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18107-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi:</p><p>Can wireshark playback a captured tcpip session between a client and a server? For the playback can the ip addresses be changed, for example the client and server are moved to a different subnet. Can the capture and playback use a mac address instead of an ip address?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">playback</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '13, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/7bdc9ef804160fa2f5ccc3b21601c2be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rkidd&#39;s gravatar image" /><p>rkidd<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rkidd has no accepted answers">0%</span></p></div></div><div id="comments-container-18107" class="comments-container"></div><div id="comment-tools-18107" class="comment-tools"></div><div class="clear"></div><div id="comment-18107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18109"></span>

<div id="answer-container-18109" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18109-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark does <strong>not</strong> contain playback functionality.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '13, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18109" class="comments-container"><span id="18111"></span><div id="comment-18111" class="comment"><div id="post-18111-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the quick response! Can wireshark capture a session to a file that can be played back by another tool?</p></div><div id="comment-18111-info" class="comment-info"><span class="comment-age">(30 Jan '13, 09:30)</span> rkidd</div></div><span id="18112"></span><div id="comment-18112" class="comment"><div id="post-18112-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", please see the FAQ for more info on how to best use this site)</p><p>Yes, you can capture data and save it in pcap format. This used to be the default format until version 1.8.x. Now pcap-ng is the default format (because of its extended features), but captures can still be saved in pcap format so they can be used in other applications.</p></div><div id="comment-18112-info" class="comment-info"><span class="comment-age">(30 Jan '13, 09:33)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-18109" class="comment-tools"></div><div class="clear"></div><div id="comment-18109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18114"></span>

<div id="answer-container-18114" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18114-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>you may want to take a look at tcpreplay tool.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '13, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/ceb9fa89fe77c08ded53b2ccf693aeaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aruna%20Sirigere&#39;s gravatar image" /><p>Aruna Sirigere<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aruna Sirigere has no accepted answers">0%</span></p></div></div><div id="comments-container-18114" class="comments-container"><span id="18223"></span><div id="comment-18223" class="comment"><div id="post-18223-score" class="comment-score"></div><div class="comment-text"><p>Is there a good replay for the MAC for wireshark captures?</p><p>Thanks!</p></div><div id="comment-18223-info" class="comment-info"><span class="comment-age">(01 Feb '13, 06:01)</span> rkidd</div></div><span id="18247"></span><div id="comment-18247" class="comment"><div id="post-18247-score" class="comment-score"></div><div class="comment-text"><p>If by "the MAC" you mean "Macintoshes", then, yes, there's a program that can read pcap captures, and pcap-ng captures on Snow Leopard and later, and replay them. It's called <a href="http://tcpreplay.synfin.net">tcpreplay</a>.</p></div><div id="comment-18247-info" class="comment-info"><span class="comment-age">(01 Feb '13, 15:29)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18114" class="comment-tools"></div><div class="clear"></div><div id="comment-18114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

