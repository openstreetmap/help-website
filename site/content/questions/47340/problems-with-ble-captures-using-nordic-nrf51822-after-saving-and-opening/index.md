+++
type = "question"
title = "Problems with BLE captures using Nordic nRF51822 after saving and opening"
description = '''When the Nordic sniffer sends the capture to Wireshark, it adds a very useful extra &quot;header&quot; (Nordic BLE sniffer meta) that includes the direction of the packet, freq channel, etc. Wireshark has no problem parsing this header and everything looks good. If one saves the capture and then opens it agai...'''
date = "2015-11-06T08:32:00Z"
lastmod = "2015-11-06T10:41:00Z"
weight = 47340
keywords = [ "ble", "problem", "nordic", "bluetooth" ]
aliases = [ "/questions/47340" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problems with BLE captures using Nordic nRF51822 after saving and opening](/questions/47340/problems-with-ble-captures-using-nordic-nrf51822-after-saving-and-opening)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47340-score" class="post-score" title="current number of votes">0</div><span id="post-47340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When the Nordic sniffer sends the capture to Wireshark, it adds a very useful extra "header" (Nordic BLE sniffer meta) that includes the direction of the packet, freq channel, etc. Wireshark has no problem parsing this header and everything looks good.</p><p>If one saves the capture and then opens it again, the capture gets all messed up because Wireshark does not parse the "Nodic BLE sniffer meta" header and starts analyzing the packet as if the "Nordic meta" header was the beginning of the BLE packet. Is there any way to fix this or force Wireshark to digest the "Nordic meta" header?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ble" rel="tag" title="see questions tagged &#39;ble&#39;">ble</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-nordic" rel="tag" title="see questions tagged &#39;nordic&#39;">nordic</span> <span class="post-tag tag-link-bluetooth" rel="tag" title="see questions tagged &#39;bluetooth&#39;">bluetooth</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '15, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/4c3c30e47e582092a02e66a27c7a536f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="softhandover&#39;s gravatar image" /><p><span>softhandover</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="softhandover has no accepted answers">0%</span></p></div></div><div id="comments-container-47340" class="comments-container"></div><div id="comment-tools-47340" class="comment-tools"></div><div class="clear"></div><div id="comment-47340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47342"></span>

<div id="answer-container-47342" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47342-score" class="post-score" title="current number of votes">0</div><span id="post-47342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The issue is likely to be with the Nordic BLE Sniffer plugin produced by Nordic, you'll have to ask them for support.</p><del>Note that as I can't locate the sources for the plugins on the Nordic site, they *might* be committing a GPL violation by distributing the plugins without a) the GPL licence, b) making an offer to make the sources available.</del> <del>The licence in the plugin [download](<a href="https://www.nordicsemi.com/eng/nordic/download_resource/31920/14/87700316)">https://www.nordicsemi.com/eng/nordic/download_resource/31920/14/87700316)</a> doesn't appear to be GPL compliant, nor mention GPL components.</del><p><strong>Update</strong></p><p>I've now found the source and the GPL for the plugins in the <a href="https://www.nordicsemi.com/eng/nordic/download_resource/31920/14/87700316">download</a>, in the sub-zip SnifferAPI.zip.</p><p>Apologies to Nordic, they are distributing the sources, under the GPL, but you still need to get support for the plugins from them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '15, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Nov '15, 09:22</strong> </span></p></div></div><div id="comments-container-47342" class="comments-container"><span id="47345"></span><div id="comment-47345" class="comment"><div id="post-47345-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for the reply! Adafruit also provides the code for the Nordic BLE dissector: <a href="https://github.com/adafruit/Adafruit_BLESniffer_Python/blob/master/wireshark_dissector_source/packet-nordic_ble.c">https://github.com/adafruit/Adafruit_BLESniffer_Python/blob/master/wireshark_dissector_source/packet-nordic_ble.c</a></p><p>It is also included in the SnifferAPI.zip file (packet-btle.c and packet-nordic_ble.c). I will try compiling them into Wireshark. In C:\Program Files\Wireshark\plugins\1.12.7 there is a nordic_ble.dll already, but I am not sure if that includes both packet types, though.</p><p>Thanks!!!</p></div><div id="comment-47345-info" class="comment-info"><span class="comment-age">(06 Nov '15, 10:17)</span> <span class="comment-user userinfo">softhandover</span></div></div><span id="47346"></span><div id="comment-47346" class="comment"><div id="post-47346-score" class="comment-score"></div><div class="comment-text"><p>The plugin you have in ...\plugins\1.2.7 definitely came from Nordic, as Wireshark does not distribute a plugin with that name.</p></div><div id="comment-47346-info" class="comment-info"><span class="comment-age">(06 Nov '15, 10:41)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-47342" class="comment-tools"></div><div class="clear"></div><div id="comment-47342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

