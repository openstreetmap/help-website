+++
type = "question"
title = "tshark can&#x27;t get the ip.src when capture packets on wlan"
description = '''hello! Recently, I try to capture packets with tshark. I execute airmon-ng start wlan0 to set my wireless network card to monitor mode, and then excute tshark -i mon0 -Tfields -e frame.time_relative -e frame.len -e radiotap.datarate -e radiotap.dbm_antsignal -e ip.src -e ip.dst -Eseparator=# &amp;gt;cha...'''
date = "2013-09-25T09:16:00Z"
lastmod = "2013-09-25T18:29:00Z"
weight = 25223
keywords = [ "capture", "wlan", "tshark" ]
aliases = [ "/questions/25223" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark can't get the ip.src when capture packets on wlan](/questions/25223/tshark-cant-get-the-ipsrc-when-capture-packets-on-wlan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25223-score" class="post-score" title="current number of votes">0</div><span id="post-25223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello! Recently, I try to capture packets with tshark. I execute <code>airmon-ng start wlan0</code> to set my wireless network card to monitor mode, and then excute <code>tshark -i mon0 -Tfields -e frame.time_relative -e frame.len -e radiotap.datarate -e radiotap.dbm_antsignal -e ip.src -e ip.dst -Eseparator=# &gt;channel_6.txt -a duration:10&amp;</code> , but ip.src and ip.dst don't display anything. I try using -V, and find that IP was not been parsed. If I don't set my wireless network card, radiotap don't display anything, but can get the ip.src. Please help me and sorry for my poor English！ Thanks again!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '13, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/c7a913c2713fdd9048a65aff89ca17e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="btk913&#39;s gravatar image" /><p><span>btk913</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="btk913 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Sep '13, 09:49</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-25223" class="comments-container"></div><div id="comment-tools-25223" class="comment-tools"></div><div class="clear"></div><div id="comment-25223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25249"></span>

<div id="answer-container-25249" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25249-score" class="post-score" title="current number of votes">1</div><span id="post-25249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>monitor mode ... ip.src and ip.dst don't display anything</p></blockquote><p>If your network is "protected", meaning it's using WEP or WPA/WPA2, the traffic on it is encrypted and, if you capture in monitor mode, the packets you get will <em>not</em> have been decrypted. You will have to configure TShark to decrypt it; see the Wireshark Wiki <a href="http://wiki.wireshark.org/HowToDecrypt802.11">"how to decrypt 802.11"</a> page. If you configure Wireshark, you've also configured TShark, as the configuration information is used by both of them. You could also configure that information by editing the Wireshark preferences file, but that's a more complicated process. Other parts of that, such as the requirement to capture the initial EAPOL handshake, also apply, so you may need to disconnect machines from the network and then reconnect them, or put them to sleep and wake them up, to force the handshake to occur. This even applies to the machine running TShark if you want to capture and decrypt its traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '13, 16:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-25249" class="comments-container"><span id="25253"></span><div id="comment-25253" class="comment"><div id="post-25253-score" class="comment-score"></div><div class="comment-text"><p>This is my first time that get right answer from forum. Thank you so much. I will try this tonight. Thanks again!</p></div><div id="comment-25253-info" class="comment-info"><span class="comment-age">(25 Sep '13, 18:29)</span> <span class="comment-user userinfo">btk913</span></div></div></div><div id="comment-tools-25249" class="comment-tools"></div><div class="clear"></div><div id="comment-25249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

