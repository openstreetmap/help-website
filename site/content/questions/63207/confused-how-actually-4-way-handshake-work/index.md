+++
type = "question"
title = "confused how actually 4 way handshake work"
description = '''Captured handshake and password have been found using brut forcing tools of kali Linux now i interested in how its work so i did following steps:  Generated PMK form PSK and SSID using online calculator Generated PTK using online calculator HMAC-SHA-1 from following input Data = Min_MAC Address, MAX...'''
date = "2017-07-28T03:59:00Z"
lastmod = "2017-07-28T03:59:00Z"
weight = 63207
keywords = [ "handshake", "hmacsha1", "hmac_aes", "wifiptk" ]
aliases = [ "/questions/63207" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [confused how actually 4 way handshake work](/questions/63207/confused-how-actually-4-way-handshake-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63207-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Captured handshake and password have been found using brut forcing tools of kali Linux now i interested in how its work so i did following steps:</p><ul><li>Generated PMK form PSK and SSID using online calculator</li><li>Generated PTK using online calculator HMAC-SHA-1 from following input</li><li>Data = Min_MAC Address, MAX_MAC Address, Min_Nonce, Max_Nonce.</li><li>key = PMK</li><li>from which i get 384 bit PTK</li><li>this PTK divided in three parts (KCK, KEK, TK)</li><li>KCK encrypt with KEK by using AES-128 using online calculator where data</li><li>data = KCK</li><li>key = KEK</li><li>That KCK should be matched with the MIC, i founded using kali Linux tools (the MIC of second packet of handshake) which is not the same</li></ul><p>Now the question is! What I missed here please help me I m so tired</p></div><div id="question-tags" class="tags-container tags">handshake hmacsha1 hmac_aes wifiptk</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '17, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/8593adc68309199a4f1c6e378c40debb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aziz88&#39;s gravatar image" /><p>Aziz88<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aziz88 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jul '17, 04:18</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-63207" class="comments-container"></div><div id="comment-tools-63207" class="comment-tools"></div><div class="clear"></div><div id="comment-63207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

