+++
type = "question"
title = "Capture BLE 4.0 Packets with Wireshark and AirPcap NX"
description = '''Hi guys, Is it possible to capture BLE 4.0 packets with Wireshark and AirPCAP NX? Thanks,'''
date = "2014-04-25T01:13:00Z"
lastmod = "2014-04-27T11:42:00Z"
weight = 32171
keywords = [ "ble", "airpcap", "wireshark", "4", "bluetooth" ]
aliases = [ "/questions/32171" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture BLE 4.0 Packets with Wireshark and AirPcap NX](/questions/32171/capture-ble-40-packets-with-wireshark-and-airpcap-nx)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32171-score" class="post-score" title="current number of votes">0</div><span id="post-32171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, Is it possible to capture BLE 4.0 packets with Wireshark and AirPCAP NX? Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ble" rel="tag" title="see questions tagged &#39;ble&#39;">ble</span> <span class="post-tag tag-link-airpcap" rel="tag" title="see questions tagged &#39;airpcap&#39;">airpcap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-4" rel="tag" title="see questions tagged &#39;4&#39;">4</span> <span class="post-tag tag-link-bluetooth" rel="tag" title="see questions tagged &#39;bluetooth&#39;">bluetooth</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '14, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/8e3b19a42e7b6de5d0e7282dd769b595?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yoogi&#39;s gravatar image" /><p><span>Yoogi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yoogi has no accepted answers">0%</span></p></div></div><div id="comments-container-32171" class="comments-container"><span id="32173"></span><div id="comment-32173" class="comment"><div id="post-32173-score" class="comment-score"></div><div class="comment-text"><p>If you are refering to <a href="http://en.wikipedia.org/wiki/Bluetooth_low_energy">http://en.wikipedia.org/wiki/Bluetooth_low_energy</a> check here <a href="http://wiki.wireshark.org/Bluetooth">http://wiki.wireshark.org/Bluetooth</a> I don't think AirPCAP can capture Blouthooth as the radio interface is (probably)ddifferent.</p></div><div id="comment-32173-info" class="comment-info"><span class="comment-age">(25 Apr '14, 03:57)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-32171" class="comment-tools"></div><div class="clear"></div><div id="comment-32171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32198"></span>

<div id="answer-container-32198" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32198-score" class="post-score" title="current number of votes">1</div><span id="post-32198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the Datasheet.</p><blockquote><p><a href="http://media-cms.riverbed.com/documents/DataSheet-Riverbed-AirPcap.pdf">http://media-cms.riverbed.com/documents/DataSheet-Riverbed-AirPcap.pdf</a></p></blockquote><p>Cite:</p><pre><code>AirPcap Nx is a dual-band solution supporting packet capture and injection for 802.11n, 802.11a/b/g legacy modes, and the 4.9 GHz US public safety channels. &quot;</code></pre><p>AirPcap is a capture device for wifi/wlan traffic. Bluetooth is not mentioned anywhere in the product description. Unless it's a hidden feature of the AirPcap NX adapter (I have never heard of that), you <strong>cannot capture Bluetooth traffic</strong> with the AirPcap adapter family.</p><p>So, the answer to your question is: No</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '14, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Apr '14, 12:31</strong> </span></p></div></div><div id="comments-container-32198" class="comments-container"><span id="32218"></span><div id="comment-32218" class="comment"><div id="post-32218-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your help.</p></div><div id="comment-32218-info" class="comment-info"><span class="comment-age">(27 Apr '14, 09:23)</span> <span class="comment-user userinfo">Yoogi</span></div></div><span id="32220"></span><div id="comment-32220" class="comment"><div id="post-32220-score" class="comment-score"></div><div class="comment-text"><p>You're welcome.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-32220-info" class="comment-info"><span class="comment-age">(27 Apr '14, 11:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32198" class="comment-tools"></div><div class="clear"></div><div id="comment-32198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

