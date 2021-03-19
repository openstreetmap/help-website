+++
type = "question"
title = "Can&#x27; t see http traffic in monitor mode."
description = '''I used airmon to create monitor interface, when i starting interface monitoring in wireshark i can see only probes, beacons and QoS exchanges. I&#x27;m actually testing from two laptops. '''
date = "2014-02-11T06:10:00Z"
lastmod = "2014-02-15T03:50:00Z"
weight = 29691
keywords = [ "http" ]
aliases = [ "/questions/29691" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can' t see http traffic in monitor mode.](/questions/29691/can-t-see-http-traffic-in-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29691-score" class="post-score" title="current number of votes">0</div><span id="post-29691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I used airmon to create monitor interface, when i starting interface monitoring in wireshark i can see only probes, beacons and QoS exchanges. I'm actually testing from two laptops.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/2dc2dce97c04e173e2dd1e0bee21edcc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Emiliano%20Riva&#39;s gravatar image" /><p><span>Emiliano Riva</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Emiliano Riva has no accepted answers">0%</span></p></div></div><div id="comments-container-29691" class="comments-container"><span id="29695"></span><div id="comment-29695" class="comment"><div id="post-29695-score" class="comment-score"></div><div class="comment-text"><p>Some questions:</p><ul><li>what is your OS and OS version of the Wireshark system?</li><li>what is your Wireshark version?</li><li>how do you capture the traffic (with Wireshark, or other tools)?</li><li>on which interface do you capture (wlan0 or mon0)?</li><li>is it possible to post a sample capture file somewhere (google drive, dropbox, cloudshark.org)?</li></ul></div><div id="comment-29695-info" class="comment-info"><span class="comment-age">(11 Feb '14, 06:37)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29707"></span><div id="comment-29707" class="comment"><div id="post-29707-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply, i'm on ubuntu 13.10 with b43 drivers for b4312 chipset, actually i'm capturing traffic with Wireshark Version 1.10.2 on mon0 interface created with airmon-ng. GemetekTe is my laptop EdimaxTe my desktop</p><p><a href="https://dl.dropboxusercontent.com/u/75167669/capture.txt">https://dl.dropboxusercontent.com/u/75167669/capture.txt</a> this is the link of a captured text with Tshark.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wire_small_2.png" alt="alt text" /></p></div><div id="comment-29707-info" class="comment-info"><span class="comment-age">(11 Feb '14, 07:48)</span> <span class="comment-user userinfo">Emiliano Riva</span></div></div><span id="29709"></span><div id="comment-29709" class="comment"><div id="post-29709-score" class="comment-score"></div><div class="comment-text"><p>Now that i have disabled wpa2 from the router i can see also other packages. Can' t Wireshark work with encrypted data? I tried to enable decription and then i set one key resulting in my litteral password, is this correct?<br />
</p></div><div id="comment-29709-info" class="comment-info"><span class="comment-age">(11 Feb '14, 10:15)</span> <span class="comment-user userinfo">Emiliano Riva</span></div></div></div><div id="comment-tools-29691" class="comment-tools"></div><div class="clear"></div><div id="comment-29691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29720"></span>

<div id="answer-container-29720" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29720-score" class="post-score" title="current number of votes">0</div><span id="post-29720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can' t Wireshark work with encrypted data?</p></blockquote><p>Sure, see the Wireshark Wiki page on <a href="http://wiki.wireshark.org/HowToDecrypt802.11">decrypting 802.11 traffic</a>.</p><p>This question comes up a lot though so search for other questions and answers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '14, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Feb '14, 18:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-29720" class="comments-container"><span id="29874"></span><div id="comment-29874" class="comment"><div id="post-29874-score" class="comment-score"></div><div class="comment-text"><p>So, thanks for reply, i tested to decrypt the example in the bottom of the page and it work properly, but not with traffic in my network.</p><p>This is my level of encryption:</p><p><code>IE: IEEE 802.11i/WPA2 Version 1 Group Cipher : TKIP Pairwise Ciphers (2) : TKIP CCMP Authentication Suites (1) : PSK Preauthentication Supported</code></p><p>I have capture the four EAPOL required.</p><p>What am I doing wrong?</p></div><div id="comment-29874-info" class="comment-info"><span class="comment-age">(14 Feb '14, 15:40)</span> <span class="comment-user userinfo">Emiliano Riva</span></div></div><span id="29876"></span><div id="comment-29876" class="comment"><div id="post-29876-score" class="comment-score"></div><div class="comment-text"><p>What does it do instead of working correctly? Does it still show the data packets as just data, rather than decrypting them? Does it decrypt them but give garbage data? Does it do something else?</p></div><div id="comment-29876-info" class="comment-info"><span class="comment-age">(14 Feb '14, 18:04)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="29884"></span><div id="comment-29884" class="comment"><div id="post-29884-score" class="comment-score"></div><div class="comment-text"><p>Yes,packets are showed only as data, I solved disabling Protection bit and initialization vector.</p></div><div id="comment-29884-info" class="comment-info"><span class="comment-age">(15 Feb '14, 03:50)</span> <span class="comment-user userinfo">Emiliano Riva</span></div></div></div><div id="comment-tools-29720" class="comment-tools"></div><div class="clear"></div><div id="comment-29720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

