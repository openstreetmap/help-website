+++
type = "question"
title = "can&#x27;t decrypt 802.11 traffic"
description = '''I have tried to decrypt radioTap pcap, but it won&#x27;t work. Wonder what could have gone wrong. Here is snapshot for enter WPA password to wireshark (ver 1,8,2). Any ideas? Thanks.'''
date = "2015-09-16T08:02:00Z"
lastmod = "2015-09-17T08:19:00Z"
weight = 45881
keywords = [ "wireshark" ]
aliases = [ "/questions/45881" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [can't decrypt 802.11 traffic](/questions/45881/cant-decrypt-80211-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45881-score" class="post-score" title="current number of votes">0</div><span id="post-45881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have tried to decrypt radioTap pcap, but it won't work. Wonder what could have gone wrong. Here is <a href="http://imgur.com/WvzMvtD">snapshot</a> for enter WPA password to wireshark (ver 1,8,2).</p><p>Any ideas? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '15, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-45881" class="comments-container"><span id="45885"></span><div id="comment-45885" class="comment"><div id="post-45885-score" class="comment-score"></div><div class="comment-text"><p>Could you share the related trace?</p></div><div id="comment-45885-info" class="comment-info"><span class="comment-age">(16 Sep '15, 10:07)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="45889"></span><div id="comment-45889" class="comment"><div id="post-45889-score" class="comment-score"></div><div class="comment-text"><p>unfortunately can't share it due to confidential info. My basic question is, does it take just a WPA password for wireshark to be able to decrypt it? Thanks.</p></div><div id="comment-45889-info" class="comment-info"><span class="comment-age">(16 Sep '15, 14:40)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="45891"></span><div id="comment-45891" class="comment"><div id="post-45891-score" class="comment-score"></div><div class="comment-text"><p>Have you read this question: <a href="https://ask.wireshark.org/questions/41945/80211-decryption-doesnt-always-work-even-with-the-full-eapol-handshake">https://ask.wireshark.org/questions/41945/80211-decryption-doesnt-always-work-even-with-the-full-eapol-handshake</a></p><p>In this question a lot of trace examples with keys are given.</p></div><div id="comment-45891-info" class="comment-info"><span class="comment-age">(16 Sep '15, 15:27)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="45896"></span><div id="comment-45896" class="comment"><div id="post-45896-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@christian_r</span> for the link, it has lots of content. Unfortunately I can't follow one of the instructions. This instruction shows there is a Decryption Key button but I can't find it on mine (ver 1.10.6). <a href="http://imgur.com/a/bT3Kd.">http://imgur.com/a/bT3Kd.</a> Tried it on Wireshark 1.12.7 and got the same story.</p></div><div id="comment-45896-info" class="comment-info"><span class="comment-age">(16 Sep '15, 20:41)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-45881" class="comment-tools"></div><div class="clear"></div><div id="comment-45881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45921"></span>

<div id="answer-container-45921" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45921-score" class="post-score" title="current number of votes">1</div><span id="post-45921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try this:</p><ol><li>In Wireshark, select Edit / Preferences</li><li>Expand Protocols in the left-side pane. Scroll down to IEEE 802.11 and select it</li><li>On the right-side pane, select the Edit... key next to the Decryption Keys</li><li>When the new window is displayed, select New.</li><li>Key type = wpa-pwd</li><li>Key = passphrase:SSID</li></ol><p>For example, if your SSID is Test and your passphrase is testing123, then enter the following:</p><p>testing123:Test</p><p>Click OK and then Apply.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '15, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-45921" class="comments-container"><span id="45923"></span><div id="comment-45923" class="comment"><div id="post-45923-score" class="comment-score"></div><div class="comment-text"><p>Worked great. Thanks! "When in doubt, go to Edit/preferences, Protocols" :-)</p></div><div id="comment-45923-info" class="comment-info"><span class="comment-age">(17 Sep '15, 08:19)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-45921" class="comment-tools"></div><div class="clear"></div><div id="comment-45921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

