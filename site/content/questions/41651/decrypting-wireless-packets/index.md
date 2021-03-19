+++
type = "question"
title = "Decrypting wireless packets?"
description = '''Sorry if this has been posted before, but I can&#x27;t find a solution. I&#x27;m using an Alfa awus036nha usb adapter under Kali (32-bit, bare metal if it matters). I am attempting to capture wireless traffic in monitor mode, but all I&#x27;m getting are broadcast packets. I gave wireshark my PSK, but no luck. I a...'''
date = "2015-04-21T18:41:00Z"
lastmod = "2015-04-23T00:59:00Z"
weight = 41651
keywords = [ "broadcast", "decrypt", "wpa" ]
aliases = [ "/questions/41651" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting wireless packets?](/questions/41651/decrypting-wireless-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41651-score" class="post-score" title="current number of votes">0</div><span id="post-41651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Sorry if this has been posted before, but I can't find a solution.</p><p>I'm using an Alfa awus036nha usb adapter under Kali (32-bit, bare metal if it matters). I am attempting to capture wireless traffic in monitor mode, but all I'm getting are broadcast packets.</p><p>I gave wireshark my PSK, but no luck. I also cleared the key, saved the capture and then entered the key thinking it may need to stop capture before it can decrypt, still no go. I know my adapter supports promiscuous mode as I use it in other utilities with success. Any ideas what I may be doing wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadcast" rel="tag" title="see questions tagged &#39;broadcast&#39;">broadcast</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span> <span class="post-tag tag-link-wpa" rel="tag" title="see questions tagged &#39;wpa&#39;">wpa</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '15, 18:41</strong></p><img src="https://secure.gravatar.com/avatar/159cc64345e622a454de465778fc3b56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmorrow132&#39;s gravatar image" /><p><span>cmorrow132</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmorrow132 has no accepted answers">0%</span></p></div></div><div id="comments-container-41651" class="comments-container"><span id="41691"></span><div id="comment-41691" class="comment"><div id="post-41691-score" class="comment-score"></div><div class="comment-text"><p>How did you put the card in monitor mode? iwconfig or airmon-ng? What interface did you select in Wireshark? What channel did you select in Wireshark? Are you not able to decrypt the packets or are you not seeing data packets at all? Can you upload a packet capture?</p></div><div id="comment-41691-info" class="comment-info"><span class="comment-age">(22 Apr '15, 08:23)</span> <span class="comment-user userinfo">Roland</span></div></div><span id="41699"></span><div id="comment-41699" class="comment"><div id="post-41699-score" class="comment-score"></div><div class="comment-text"><p>Something does not make sense. You claim that only broadcast packets are being captured, but then ask why decryption is not working. In order to decrypt any traffic, you must capture EAPOL packets which is unicast traffic. So my question is: Do you see any unicast traffic, either EAPOL, Null Data or Data frames? If not, then the problem is not with decryption, but with capturing the traffic.</p></div><div id="comment-41699-info" class="comment-info"><span class="comment-age">(22 Apr '15, 09:37)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="41705"></span><div id="comment-41705" class="comment"><div id="post-41705-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the replies. I am setting the adapter to monitor mode with airmon-ng, and then starting wireshark (gksudo wireshark). I selected mon0 in wireshark and then told it to start capturing, but I don't recall any place to set the channel. I don't see a way to attach a capture file, but here is a screenshot:</p><p><a href="http://s29.postimg.org/k0c0ogjyf/Capture.png">http://s29.postimg.org/k0c0ogjyf/Capture.png</a></p></div><div id="comment-41705-info" class="comment-info"><span class="comment-age">(22 Apr '15, 12:42)</span> <span class="comment-user userinfo">cmorrow132</span></div></div><span id="41706"></span><div id="comment-41706" class="comment"><div id="post-41706-score" class="comment-score"></div><div class="comment-text"><p>Also, the mt1932a ssid is the one I am trying to decrypt.</p></div><div id="comment-41706-info" class="comment-info"><span class="comment-age">(22 Apr '15, 12:43)</span> <span class="comment-user userinfo">cmorrow132</span></div></div></div><div id="comment-tools-41651" class="comment-tools"></div><div class="clear"></div><div id="comment-41651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41708"></span>

<div id="answer-container-41708" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41708-score" class="post-score" title="current number of votes">0</div><span id="post-41708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can select the Wireless Toolbar under View.</p><p>You can upload packet captures to CloudShark.</p><p>To decrypt WPA2 go to Edit &gt; Preferences &gt; Protocols &gt; IEEE802.11 and click on Edit &gt; New. Key Type should be wpa-pwd and the Key in the format password:ssid. Make sure you also select Enable decryption. Now that everything is set up, reconnect your test client. You should see the four EAPOL packets. Sometimes you will have to try a few times until it captures all four. Please remember you can't decrypt the traffic without them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '15, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-41708" class="comments-container"><span id="41711"></span><div id="comment-41711" class="comment"><div id="post-41711-score" class="comment-score"></div><div class="comment-text"><p>Thank you! When I read "reconnect your test client" it clicked. The clients were already connected, and so that's why I wasn't capturing EAPOL. I sent a deauth with aireplay to the client, and was able to see it reauthenticate and I began to capture data packets. Everything is working now.</p></div><div id="comment-41711-info" class="comment-info"><span class="comment-age">(22 Apr '15, 20:08)</span> <span class="comment-user userinfo">cmorrow132</span></div></div><span id="41719"></span><div id="comment-41719" class="comment"><div id="post-41719-score" class="comment-score"></div><div class="comment-text"><p>You're welcome. If the answer was good, please accept the answer by clicking on the check mark next to it.</p></div><div id="comment-41719-info" class="comment-info"><span class="comment-age">(23 Apr '15, 00:59)</span> <span class="comment-user userinfo">Roland</span></div></div></div><div id="comment-tools-41708" class="comment-tools"></div><div class="clear"></div><div id="comment-41708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

