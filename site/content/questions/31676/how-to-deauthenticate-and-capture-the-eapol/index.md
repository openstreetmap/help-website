+++
type = "question"
title = "How to deauthenticate and capture the eapol?"
description = '''Im playing around with my wireless network (WPA) at home. When I start monitor mode and wireshark in backtrack, and afterwards connect my phone to the network, wireshark succesfully decrypts the packets transmitted by my phone. But when my phone is already connected to the network, then I cant just ...'''
date = "2014-04-09T10:23:00Z"
lastmod = "2014-04-10T13:27:00Z"
weight = 31676
keywords = [ "deauthenticate", "capture", "eapol", "sniff", "backtrack" ]
aliases = [ "/questions/31676" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to deauthenticate and capture the eapol?](/questions/31676/how-to-deauthenticate-and-capture-the-eapol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31676-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im playing around with my wireless network (WPA) at home. When I start monitor mode and wireshark in backtrack, and afterwards connect my phone to the network, wireshark succesfully decrypts the packets transmitted by my phone.</p><p>But when my phone is already connected to the network, then I cant just start wireshark and decrypt the phones packets. I have read that I need to kick off/deauthenticate the phone. But the problem is that in order to deauthenticate somebody I need to disconnect from my wireless network, which means I cant capture the eapol. And I cant reconnect to my network(with wireshark running) before my phone have reauthenticated.</p></div><div id="question-tags" class="tags-container tags">deauthenticate capture eapol sniff backtrack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '14, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/45d60244b59d17a4caa6ef7082105804?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jeppe%20Andersen&#39;s gravatar image" /><p>Jeppe Andersen<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jeppe Andersen has no accepted answers">0%</span></p></div></div><div id="comments-container-31676" class="comments-container"><span id="31685"></span><div id="comment-31685" class="comment"><div id="post-31685-score" class="comment-score"></div><div class="comment-text"><blockquote><p>And I cant reconnect to my network(with wireshark running) before my phone have reauthenticated.</p></blockquote><p>why is that?</p></div><div id="comment-31685-info" class="comment-info"><span class="comment-age">(09 Apr '14, 13:40)</span> Kurt Knochner ♦</div></div><span id="31691"></span><div id="comment-31691" class="comment"><div id="post-31691-score" class="comment-score"></div><div class="comment-text"><p>my phone recconects to the network like 2 sec after the deauthentication stops. While it takes me about 6 sec to reconnect my PC to the network whem im done deauthenticating.</p></div><div id="comment-31691-info" class="comment-info"><span class="comment-age">(09 Apr '14, 15:46)</span> Jeppe Andersen</div></div></div><div id="comment-tools-31676" class="comment-tools"></div><div class="clear"></div><div id="comment-31676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31693"></span>

<div id="answer-container-31693" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31693-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>While it takes me about 6 sec to reconnect my PC to the network whem im done deauthenticating.</p></blockquote><p>well, then use a second PC to deauth the client or a second wifi card in one PC.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '14, 16:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31693" class="comments-container"><span id="31695"></span><div id="comment-31695" class="comment"><div id="post-31695-score" class="comment-score"></div><div class="comment-text"><p>Yes that would work, but I only have one computer with a wifi card.</p><p>Is there really no method to do it with only one computer/wireles NIC?</p></div><div id="comment-31695-info" class="comment-info"><span class="comment-age">(09 Apr '14, 16:39)</span> Jeppe Andersen</div></div><span id="31697"></span><div id="comment-31697" class="comment"><div id="post-31697-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Is there really no method to do it with only one computer/wireles NIC?</p></blockquote><p>You say:</p><blockquote><p>And <strong>I cant reconnect</strong> to my network(with wireshark running) before my phone have reauthenticated.</p></blockquote><p>why do you have to connect to the SSID on the capturing device? monitor mode should be sufficient.</p><p>If your driver is not able to switch into monitor mode in less than the time the client needs to re-authenticate, the only options are</p><ul><li>two wifi cards, one for capturing and one for de-auth (best and cheapest option with a USB wifi dongle)</li><li>two PCs, one for capturing and one for de-auth</li><li>a different wifi card that handles the described scenario in a better/faster way</li></ul></div><div id="comment-31697-info" class="comment-info"><span class="comment-age">(09 Apr '14, 17:12)</span> Kurt Knochner ♦</div></div><span id="31711"></span><div id="comment-31711" class="comment"><div id="post-31711-score" class="comment-score"></div><div class="comment-text"><p>First off, im very new to backtrack, and im sorry if I am missunderstanding something :)</p><p>You say:</p><blockquote><p>why do you have to connect to the SSID on the capturing device? monitor mode should be sufficient.</p></blockquote><p>In order for me to decrypt my phones traffic I need to capture the eapol right?</p><p>I tried this scenario to test your solution:</p><ol><li>Enable monitor mode (airmon-ng start wlan0).</li><li>Not connecting my computer to any SSID.</li><li>Start wireshark</li><li>Grabbing my phone and connecting it to my home network.</li></ol><p>This gives me no eapol packets in wireshark.</p></div><div id="comment-31711-info" class="comment-info"><span class="comment-age">(10 Apr '14, 08:37)</span> Jeppe Andersen</div></div><span id="31720"></span><div id="comment-31720" class="comment"><div id="post-31720-score" class="comment-score"></div><div class="comment-text"><p>So, in that scenario, in step 4, what does "connecting [my phone] to my home network" mean? Do you, for example, turn the phone off and back on again, so that the phone might think it's now in a different location, and must look for Wi-Fi networks and, if it finds one, attempt to connect to it?</p></div><div id="comment-31720-info" class="comment-info"><span class="comment-age">(10 Apr '14, 10:34)</span> Guy Harris ♦♦</div></div><span id="31728"></span><div id="comment-31728" class="comment"><div id="post-31728-score" class="comment-score"></div><div class="comment-text"><p>Step 4. means enabling my wifi on the phone, which automatically connects it to my home network. I do that to generate the 4 way handshake(eapol).</p></div><div id="comment-31728-info" class="comment-info"><span class="comment-age">(10 Apr '14, 12:10)</span> Jeppe Andersen</div></div></div><div id="comment-tools-31693" class="comment-tools"></div><div class="clear"></div><div id="comment-31693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31734"></span>

<div id="answer-container-31734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31734-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You don't need to <em>deauthenticate</em> the phone. You just need to force it to reconnect.</p><p>If, for example, you can turn off its Wi-Fi and turn it back on again, that would probably force it to reconnect; even just putting it to sleep and waking it up (which is, I suspect, what the power button does) would probably suffice.</p><p>If you really need to <em>deauthenticate</em> it, and if you can't deauthenticate it from your PC while the PC is in monitor mode, you'll have to have two machines involved, one that can deauthenticate the phone and one that can capture in monitor mode, or you'll have to have two Wi-Fi interfaces on your PC, one that's connected to the network and that you use to deauthenticate the phone, and one that's in monitor mode and that you use to capture traffic. Sorry.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '14, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-31734" class="comments-container"><span id="31738"></span><div id="comment-31738" class="comment"><div id="post-31738-score" class="comment-score"></div><div class="comment-text"><p>thhanks for the help huys, I actually made it work with the scenario above. Apparently backtrack is just buggy sometimes, and would not always capture the eapols.</p><p>But now I succesfully deauthenticated and decrypted my phone and my roomates traffic.</p></div><div id="comment-31738-info" class="comment-info"><span class="comment-age">(10 Apr '14, 14:54)</span> Jeppe Andersen</div></div></div><div id="comment-tools-31734" class="comment-tools"></div><div class="clear"></div><div id="comment-31734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

