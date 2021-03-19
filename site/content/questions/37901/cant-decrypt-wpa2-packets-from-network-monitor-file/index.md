+++
type = "question"
title = "Can&#x27;t decrypt WPA2 packets from Network Monitor File"
description = '''Hi, I have a lot of captured packets (captured in monitor mode) in a .cap file, captured with microsoft network monitor 3.4. I would like to analyze those, but all I can see in wireshark are the high-level 802.11 packets. I don&#x27;t see any HTTP traffic. I entered my WPA2-passphrase, but wireshark does...'''
date = "2014-11-17T08:01:00Z"
lastmod = "2017-05-22T02:29:00Z"
weight = 37901
keywords = [ "decryption", "wpa2", "802.11" ]
aliases = [ "/questions/37901" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't decrypt WPA2 packets from Network Monitor File](/questions/37901/cant-decrypt-wpa2-packets-from-network-monitor-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37901-score" class="post-score" title="current number of votes">0</div><span id="post-37901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a lot of captured packets (captured in monitor mode) in a .cap file, captured with microsoft network monitor 3.4. I would like to analyze those, but all I can see in wireshark are the high-level 802.11 packets. I don't see any HTTP traffic. I entered my WPA2-passphrase, but wireshark does not seem to decrypt anything. I googled a lot, and I found a stackoverflow question <a href="http://superuser.com/questions/785526/how-can-i-tell-if-wireshark-has-sucessfully-decrypted-a-capture">http://superuser.com/questions/785526/how-can-i-tell-if-wireshark-has-sucessfully-decrypted-a-capture</a> where a user states "There appears to be problems with Wireshark being able to decrypt Network Monitor 3.4 captured WPA2 traffic.".</p><p>I cannot capture the data again, I need to analyze the current captured files. Can anyone help me?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '14, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/2237898cd2f78529786cf5efcc3951e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohnSmith007&#39;s gravatar image" /><p><span>JohnSmith007</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohnSmith007 has no accepted answers">0%</span></p></div></div><div id="comments-container-37901" class="comments-container"></div><div id="comment-tools-37901" class="comment-tools"></div><div class="clear"></div><div id="comment-37901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37925"></span>

<div id="answer-container-37925" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37925-score" class="post-score" title="current number of votes">0</div><span id="post-37925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Does your capture include the full EAPOL handshakes (i.e., all 4 EAPOL "Key (Message n of 4)" messages) for the hosts whose traffic you're trying to decrypt? If not, then it'll be impossible to decrypt the traffic, as this is WPA, not WEP.</p><p>If so, then, in the frames it's not decrypting, is the "Protected" flag set in the Flags subfield of the Frame Control field?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '14, 16:51</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-37925" class="comments-container"><span id="61532"></span><div id="comment-61532" class="comment"><div id="post-61532-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy Harris,</p><p>I have captured full four EAPOL handshakes,and then try to decrypt 802.11 protocol by using wpa-pwd and wpa-psk ... However, the captured data were still covered by 802.11 protocols. I cannot decrypt the data.</p><p>Can you give some directions to decrypt the data. Do I move to another solution such as: Evil Twin attack or MitM attack?</p><p>Thanks, --William</p></div><div id="comment-61532-info" class="comment-info"><span class="comment-age">(22 May '17, 00:48)</span> <span class="comment-user userinfo">dknovo</span></div></div><span id="61535"></span><div id="comment-61535" class="comment"><div id="post-61535-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/31939/dknovo"></a><a href="https://ask.wireshark.org/users/31939/dknovo">@dknovo</a>,</p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>It's also best to keep all such comments on your specific <a href="https://ask.wireshark.org/questions/61469/unable-to-decrypt-wifi-data">question</a> (created when I promoted your other similar "answer" to it's own question), not attempt to hijack one that's 2.5 years old.</p></div><div id="comment-61535-info" class="comment-info"><span class="comment-age">(22 May '17, 02:29)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-37925" class="comment-tools"></div><div class="clear"></div><div id="comment-37925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

