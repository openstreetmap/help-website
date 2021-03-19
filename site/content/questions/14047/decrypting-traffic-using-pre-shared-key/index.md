+++
type = "question"
title = "Decrypting traffic using pre-shared key"
description = '''Hi, Due to security restrictions I can only get a private key on a certain pc. I saved the trace and pre-shared key so I could look at it on my laptop however, when I configure the SSL preferences to use this key I can see in the SSL debug file that the traffic is being decrypted but in wireshark it...'''
date = "2012-09-04T15:51:00Z"
lastmod = "2012-09-04T23:18:00Z"
weight = 14047
keywords = [ "master-key" ]
aliases = [ "/questions/14047" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting traffic using pre-shared key](/questions/14047/decrypting-traffic-using-pre-shared-key)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14047-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Due to security restrictions I can only get a private key on a certain pc. I saved the trace and pre-shared key so I could look at it on my laptop however, when I configure the SSL preferences to use this key I can see in the SSL debug file that the traffic is being decrypted but in wireshark itself it is still showing the encrypted traffic.</p><p>Most likely I'm doing something wrong but not sure what. I configured this under Protocol Preferences | SSL: SSL Debug file: c:\wireshark-ssl-debug.log (Pre)-Master-Secret log filename: c:\<a href="http://session-key.txt">session-key.txt</a></p><p>I left all the other settings default.</p><p>Using build 44520 (1.8.2). Has anyone successfully used this option?</p><p>Many thanks, Edward</p></div><div id="question-tags" class="tags-container tags">master-key</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '12, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/511eb018dbeabefba9c93b511143e332?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edward&#39;s gravatar image" /><p>Edward<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edward has no accepted answers">0%</span></p></div></div><div id="comments-container-14047" class="comments-container"></div><div id="comment-tools-14047" class="comment-tools"></div><div class="clear"></div><div id="comment-14047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14053"></span>

<div id="answer-container-14053" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14053-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, I have used this option repeatedly.</p><p>There is however a bug. When you point to the correct key file and click OK, focus comes back to the main window and not to the SSL protocol preferences. Since that window is behind the main window, you don't notice that you need to click on OK in the SSL protocol preferences to make the new settings active.</p><p>If it is still not working for you, is your file <a href="http://session-key.txt">session-key.txt</a> in the following format:</p><pre><code>RSA Session-ID:63375a39fd0e5c4a527b3e460e1e7c55f2083c1f0b236f58cca20f9c8af9d9b6 Master-Key:f3671e0b55fa8897034884d177e69c6bdd019b9e63e96d7af1b0d846835d5638edbbdbeb97e70edb84076b764f14b219</code></pre><p>... and is there an entry for each SSL SessionID found in your trace (look at the ServerHello messages)?</p><p>If that does not help you, can you post the capture file (you can leave out the application data) on <a href="http://www.cloudshark.org">www.cloudshark.org</a> and post the contents of the <a href="http://session-key.txt">session-key.txt</a> file here for further analysis?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '12, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Sep '12, 01:54</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-14053" class="comments-container"><span id="14069"></span><div id="comment-14069" class="comment"><div id="post-14069-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>The key etc is definitely 'accepted' as when I look in the debug file I can see the decrypted traffic. Are you running the same build or an older one?</p><p>Thanks, Edward</p></div><div id="comment-14069-info" class="comment-info"><span class="comment-age">(05 Sep '12, 16:47)</span> Edward</div></div><span id="14076"></span><div id="comment-14076" class="comment"><div id="post-14076-score" class="comment-score"></div><div class="comment-text"><p>I recently used version 1.8.2 (official release) at a customer and could use the SSL session key log to decrypt traffic. On my own system I use 1.9.0 SVN 44562 at the moment.</p><p>I'm just wondering, what protocol is inside the SSL traffic and is it using a standard port? Do you see the "Finished" handshake messages or does the SSL negotiation end with "Encrypted Handshake"?</p></div><div id="comment-14076-info" class="comment-info"><span class="comment-age">(05 Sep '12, 23:34)</span> SYN-bit ♦♦</div></div><span id="14144"></span><div id="comment-14144" class="comment"><div id="post-14144-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>The protocol being used is http and yeah, it is using a different port. The ssl negotiation finishes with a 'encrypted handshake message' and the packet after that is from the client with Application Data which wireshark sees as TLSv1.</p><p>Thanks, Edward</p></div><div id="comment-14144-info" class="comment-info"><span class="comment-age">(09 Sep '12, 06:15)</span> Edward</div></div><span id="27567"></span><div id="comment-27567" class="comment"><div id="post-27567-score" class="comment-score"></div><div class="comment-text"><p>I am seeing the same problem as Edward. I did the following from the command prompt:</p><p>set SSLKEYLOGFILE=c:\sslKeyLogOWA.txt<br />
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"</p><p>then I accessed the HTTPS website from the opened browser to get the session keys and pointed Wireshark's SSL protocol to the created sslKeyLogOWA.txt file.</p><p>As I continue to browse the site in Chrome, I see the HTTPS traffic pass through, but Following SSL Stream returns an empty window.</p><p>I can't seem to find ServerHello mentioned by SYN-bit, is it in TCP section of the header?</p></div><div id="comment-27567-info" class="comment-info"><span class="comment-age">(29 Nov '13, 07:26)</span> net_tech</div></div><span id="27568"></span><div id="comment-27568" class="comment"><div id="post-27568-score" class="comment-score"></div><div class="comment-text"><p>just looked at the sslKeyLogOWA.txt. I have CLIENT_RANDOM field instead of Master-Key. Is this why I am not able to decrypt the traffic?</p></div><div id="comment-27568-info" class="comment-info"><span class="comment-age">(29 Nov '13, 07:31)</span> net_tech</div></div></div><div id="comment-tools-14053" class="comment-tools"></div><div class="clear"></div><div id="comment-14053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

