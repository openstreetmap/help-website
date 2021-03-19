+++
type = "question"
title = "derive WPA session key from PSK and 4way handshake"
description = '''Hello Forum a friend(which owns a small business) told me that he replaced his WEP based AP by a new AP with WPA PSK encryption. He believes that from now on, nobody(even between his employees using the same PSK) can intercept/decrypt the traffic of other legitimate users. My idea is that with the P...'''
date = "2016-07-07T08:29:00Z"
lastmod = "2016-09-18T03:08:00Z"
weight = 53905
keywords = [ "session", "wpa", "key" ]
aliases = [ "/questions/53905" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [derive WPA session key from PSK and 4way handshake](/questions/53905/derive-wpa-session-key-from-psk-and-4way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53905-score" class="post-score" title="current number of votes">0</div><span id="post-53905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Forum</p><p>a friend(which owns a small business) told me that he replaced his WEP based AP by a new AP with WPA PSK encryption. He believes that from now on, nobody(even between his employees using the same PSK) can intercept/decrypt the traffic of other legitimate users. My idea is that with the PSK and the 4way handshake it's not too difficult to decrypt his traffic and I would like to show him this fact:-)</p><p>Question: Is Wireshark to tool of choice for deriving the WPA session key from the PSK and the 4way handshake?</p><p>Thank's a lot for any feedback! Joe</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-session" rel="tag" title="see questions tagged &#39;session&#39;">session</span> <span class="post-tag tag-link-wpa" rel="tag" title="see questions tagged &#39;wpa&#39;">wpa</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '16, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/c08acf577aad3b14e932ee8f48cf7d20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joseph123&#39;s gravatar image" /><p><span>joseph123</span><br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joseph123 has no accepted answers">0%</span></p></div></div><div id="comments-container-53905" class="comments-container"></div><div id="comment-tools-53905" class="comment-tools"></div><div class="clear"></div><div id="comment-53905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53912"></span>

<div id="answer-container-53912" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53912-score" class="post-score" title="current number of votes">1</div><span id="post-53912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You are correct, Wireshark can decrypt WPA encrypted communications. I assume you have seen this:</p><p><a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a></p><p>There are some other tools, but Wireshark is straightforward and easy to use, with instructions.</p><p>It is correct that each user will have a unique encryption key which is called the PTK. This is based off the master key whcih everyone shares - this is derived fro the Passphrase (i.e. PSK) and SSID. But with this PMK, and the handshake, each unique PTK can be derived so traffic can be encrypted.<br />
</p><p>If your friend moves to WPA-Enterprise, then each client gets a separate PMK, making it harder for others to get at unencrypted data. The PMK will likely change on a session timeout, so that is another tool to reduce the ability of others to get at the data.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '16, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></br></p></div></div><div id="comments-container-53912" class="comments-container"><span id="55616"></span><div id="comment-55616" class="comment"><div id="post-55616-score" class="comment-score"></div><div class="comment-text"><p>Hello again! I took me some time to get back to this interesting case. Sorry for that delay!</p><p>My friend told me "even if you are watching all this videos on Youtube you wont be able to decrypt my personal communication. Did you know by the way, how much i spent for this new equipment" and "you can stay as long as you want beside my AP and try, as long you are not cheating by connecting my LAN directly via the Ethernet"</p><p>Ok.. I do know the AP-password(the PSK which is the same for all users connecting to that AP), the SSID and did successfully capture the 4way-handshake. As i understand, with the help of the PMK each unique PTK can be derived.</p><p>I dont have the impression that <a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a> does address this task.</p><p>Question: What are the next steps to get to know the PMK each unique PTK in order to be able to decrypt the traffic?</p><p>Any feedback is appreciated very much! Thank's.</p><p>Joe</p></div><div id="comment-55616-info" class="comment-info"><span class="comment-age">(17 Sep '16, 05:33)</span> <span class="comment-user userinfo">joseph123</span></div></div><span id="55622"></span><div id="comment-55622" class="comment"><div id="post-55622-score" class="comment-score"></div><div class="comment-text"><blockquote><blockquote><p>I do know the AP-password(the PSK which is the same for all users connecting to that AP), the SSID and did successfully capture the 4way-handshake.</p></blockquote></blockquote><p>Therefore you should be able to decrypt the traffic regardless of what your friend says. Are you sure you have wireless traffic to decrypt?</p><blockquote><blockquote><p>Question: What are the next steps to get to know the PMK each unique PTK in order to be able to decrypt the traffic?</p></blockquote></blockquote><p>The PMK is derived from the Passphrase (Wireshark calls WPA-PWD) and the SSID that is entered. If you want the details, see 802.11-2012 and it indicates the method to convert the (Passphrase,SSID) --&gt; PMK. Wireshark does it for you, and there are websites around that will do it too. If you have the information as claimed and it is correct, follow the Wireshark directions and you should start to see decrypted traffic. A couple of tips:</p><ol><li><p>Make sure you have all four eapol messages. They are labeled 1 of 4, 2 of 4, etc. You can have RETRIES, but one of each type must be present. As soon as the next set comes around, the previous PTK would be invalid and you need another full set or your decryption capability will suddenly cease.</p></li><li><p>Reload the trace after you enter the key if they are not decrypted. There are some other points in the Wireshark document to check if it is not working. Also test the process with the sample provided at that link. Until you successfully decrypt the sample, you likely won't be able to do a real trace.</p></li><li><p>Make sure you have data frames to decrypt from the devices in question. You should be able to identify type QoS-Data (likely) or Data frames from the devices/BSSID under review in the trace. It's somewhat common to not have data frames as these are unicast and you need proper capture equipment/methods to be able to get them. Sometimes, we see the complaint 'I can't decrypt' but root cause is really improper capture technique as there are no data frames to decrypt.<br />
</p></li><li><p>The other option for entering key information into Wireshark (ignoring WEP as that is basically no security) is WPA-PSK. To use this, we need to generate the PMK outside of Wireshark (through something like this <a href="https://www.wireshark.org/tools/wpa-psk.html).">https://www.wireshark.org/tools/wpa-psk.html).</a> Note that Wireshark does this step for you, so you do not need to use this unless you want to when using WPA2-Personal.<br />
</p></li><li><p>To gain proficiency, setup your own wifi infrastrucuture for test with WPA2 and generate traffic to be sure you can decrypt.</p></li></ol></div><div id="comment-55622-info" class="comment-info"><span class="comment-age">(18 Sep '16, 03:08)</span> <span class="comment-user userinfo">Bob Jones</span></div></div></div><div id="comment-tools-53912" class="comment-tools"></div><div class="clear"></div><div id="comment-53912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

