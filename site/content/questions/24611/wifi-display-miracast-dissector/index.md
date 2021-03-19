+++
type = "question"
title = "WiFi Display (Miracast) Dissector"
description = '''Hello,  I was capturing WLAN packets and analyzing them with Wireshark (1.10.2). I noticed that under IEEE 802.11, Tagged Parameters, I saw the following:  Wi-FiAll: P2P  Wi-FiAll For the Wi-FiAll: P2P values are tag number = 221 OUI = 50-6f-9a OUI type = 9 For the Wi-FiAll values are tag number = 2...'''
date = "2013-09-12T09:53:00Z"
lastmod = "2015-04-02T10:12:00Z"
weight = 24611
keywords = [ "wifi", "miracast", "display" ]
aliases = [ "/questions/24611" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [WiFi Display (Miracast) Dissector](/questions/24611/wifi-display-miracast-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24611-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I was capturing WLAN packets and analyzing them with Wireshark (1.10.2). I noticed that under IEEE 802.11, Tagged Parameters, I saw the following: Wi-FiAll: P2P Wi-FiAll</p><p>For the Wi-FiAll: P2P values are tag number = 221 OUI = 50-6f-9a OUI type = 9</p><p>For the Wi-FiAll values are tag number = 221 OUI = 50-6f-9a OUI type = 10 According to the WiFi Display specification, the OUI type of 10 should be WiFi Display.</p><p>Are there any plans to add the dissector for WiFi Display?</p></div><div id="question-tags" class="tags-container tags">wifi miracast display</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '13, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-24611" class="comments-container"></div><div id="comment-tools-24611" class="comment-tools"></div><div class="clear"></div><div id="comment-24611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41155"></span>

<div id="answer-container-41155" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41155-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Dissectors for WiFi Display (Miracast) have been added in Wireshark. Current version of Wireshark is 1.12.4</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '15, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-41155" class="comments-container"></div><div id="comment-tools-41155" class="comment-tools"></div><div class="clear"></div><div id="comment-41155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24612"></span>

<div id="answer-container-24612" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24612-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think the Wireshark <a href="http://www.wireshark.org/faq.html#q1.11">FAQ</a> has your answer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '13, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24612" class="comments-container"><span id="24620"></span><div id="comment-24620" class="comment"><div id="post-24620-score" class="comment-score"></div><div class="comment-text"><p>Can you please direct me of how to add support for a particular protocol?</p></div><div id="comment-24620-info" class="comment-info"><span class="comment-age">(12 Sep '13, 19:02)</span> Amato_C</div></div><span id="24655"></span><div id="comment-24655" class="comment"><div id="post-24655-score" class="comment-score"></div><div class="comment-text"><p>You might want to start with the Wireshark <a href="http://www.wireshark.org/docs/wsdg_html_chunked/">Developer's Guide</a>. Be sure to read the various <code>README</code> files in the top-level and <code>doc/</code> directories, particularly <code>doc/README.developer</code> and <code>doc/README.dissector</code>.</p></div><div id="comment-24655-info" class="comment-info"><span class="comment-age">(13 Sep '13, 08:37)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-24612" class="comment-tools"></div><div class="clear"></div><div id="comment-24612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

