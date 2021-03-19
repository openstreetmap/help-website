+++
type = "question"
title = "How can i capture and play back thick windows client  server interactions"
description = '''Hi All I am not a networking nerd. But I am trying to capture and play back thick windows client &amp;lt;--&amp;gt; server interactions.(TCP/IP and ODBC). Basically i want to capture client server interactions and use them to play back within multiple threads to simulate concurrent user sessions of the clie...'''
date = "2013-03-14T15:43:00Z"
lastmod = "2013-03-15T04:10:00Z"
weight = 19522
keywords = [ "performance", "capture", "playback", "sessions" ]
aliases = [ "/questions/19522" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can i capture and play back thick windows client server interactions](/questions/19522/how-can-i-capture-and-play-back-thick-windows-client-server-interactions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19522-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All I am not a networking nerd. But I am trying to capture and play back thick windows client &lt;--&gt; server interactions.(TCP/IP and ODBC).</p><p>Basically i want to capture client server interactions and use them to play back within multiple threads to simulate concurrent user sessions of the client server interaction.</p><p>Is it possible to use wireshark for this?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">performance capture playback sessions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '13, 15:43</strong></p><img src="https://secure.gravatar.com/avatar/5b09a163dffd52d3cbb2aa4791e1ee50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wireshark4Noopy&#39;s gravatar image" /><p>Wireshark4Noopy<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wireshark4Noopy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '13, 04:15</p></div></div><div id="comments-container-19522" class="comments-container"></div><div id="comment-tools-19522" class="comment-tools"></div><div class="clear"></div><div id="comment-19522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19523"></span>

<div id="answer-container-19523" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19523-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not with Wireshark. Wireshark is a packet analysis tool and does not have any replay capabilities. Wireshark can capture traffic that could be used by other tools to replay the interactions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '13, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19523" class="comments-container"><span id="19533"></span><div id="comment-19533" class="comment"><div id="post-19533-score" class="comment-score"></div><div class="comment-text"><p>Are there other tools with capure and replay capabilities of the TCP/ip traffic?</p></div><div id="comment-19533-info" class="comment-info"><span class="comment-age">(15 Mar '13, 04:04)</span> Wireshark4Noopy</div></div></div><div id="comment-tools-19523" class="comment-tools"></div><div class="clear"></div><div id="comment-19523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19534"></span>

<div id="answer-container-19534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19534-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can't do this, but other tools are available:</p><ul><li><a href="http://tcpreplay.synfin.net/wiki/tcprewrite">tcprewrite</a></li><li><a href="http://bittwist.sourceforge.net/">bittwist</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '13, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19534" class="comments-container"></div><div id="comment-tools-19534" class="comment-tools"></div><div class="clear"></div><div id="comment-19534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

