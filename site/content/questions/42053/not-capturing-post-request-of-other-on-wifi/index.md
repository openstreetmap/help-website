+++
type = "question"
title = "Not capturing POST request of other on wifi?"
description = '''i used the filter http.request.method==&quot;POST&quot; on wifi network.when i filled the login of unsecured website on my machine itself it displayed the POST request but when i used my android mobile to do the same it didnt show anything,...'''
date = "2015-05-04T03:10:00Z"
lastmod = "2015-05-04T20:14:00Z"
weight = 42053
keywords = [ "wireless", "capture", "post", "wireshark" ]
aliases = [ "/questions/42053" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Not capturing POST request of other on wifi?](/questions/42053/not-capturing-post-request-of-other-on-wifi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42053-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i used the filter http.request.method=="POST" on wifi network.when i filled the login of unsecured website on my machine itself it displayed the POST request but when i used my android mobile to do the same it didnt show anything,...</p></div><div id="question-tags" class="tags-container tags">wireless capture post wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '15, 03:10</strong></p><img src="https://secure.gravatar.com/avatar/5cf70ab70c394f6940b100af1609ad58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Money&#39;s gravatar image" /><p>Money<br />
<span class="score" title="2 reputation points">2</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Money has no accepted answers">0%</span></p></div></div><div id="comments-container-42053" class="comments-container"><span id="42067"></span><div id="comment-42067" class="comment"><div id="post-42067-score" class="comment-score">1</div><div class="comment-text"><p>Are you capturing in monitor mode (or with an AirPcap adapter on Windows)?</p><p>Is this a "protected" network, using WEP or WPA/WPA2?</p><p>What do you see if you <em>don't</em> filter the display? Do you just see a bunch of "802.11" packets that are 802.11 data frames with the "Protected" bit set in the Frame Control field?</p></div><div id="comment-42067-info" class="comment-info"><span class="comment-age">(04 May '15, 15:17)</span> Guy Harris ♦♦</div></div><span id="42074"></span><div id="comment-42074" class="comment"><div id="post-42074-score" class="comment-score"></div><div class="comment-text"><p>Yes i m capturing in monitor mode and if i dont apply the filter i can see a bunch of encrypted packets . And as i wrote earlier i am able to intercept post request going from the machine itself but not of others....</p></div><div id="comment-42074-info" class="comment-info"><span class="comment-age">(04 May '15, 20:01)</span> Money</div></div></div><div id="comment-tools-42053" class="comment-tools"></div><div class="clear"></div><div id="comment-42053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42075"></span>

<div id="answer-container-42075" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42075-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Presumably the adapter is decrypting packets sent to the machine doing the capturing, but not other packets. Wireshark will have to decrypt the other packets itself; you will, at minimum, need to supply it with the password for your network, and will probably also need to capture the initial "EAPOL handshake" for the Android phone when it joins the network, for example, by turning the phone off and on again while you're capturing.</p><p>See <a href="https://wiki.wireshark.org/HowToDecrypt802.11">the Wireshark Wiki's "how to decrypt 802.11" page</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '15, 20:14</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-42075" class="comments-container"></div><div id="comment-tools-42075" class="comment-tools"></div><div class="clear"></div><div id="comment-42075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

