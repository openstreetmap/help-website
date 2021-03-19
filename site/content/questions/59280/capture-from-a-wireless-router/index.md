+++
type = "question"
title = "Capture from a Wireless Router"
description = '''Hi all, This is the Wireshark version from Linux Command Prompt. wireshark 1.12.1, libpcap 1.6.2 and libz 1.2.8. Our aim is to run the Wireshark in monitor mode to sniff a DLink DWR 116 router data. Launch wireshark and for mono interface monitor mode is enabled and capture is started. After that DL...'''
date = "2017-02-09T05:01:00Z"
lastmod = "2017-02-09T05:01:00Z"
weight = 59280
keywords = [ "dlink" ]
aliases = [ "/questions/59280" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture from a Wireless Router](/questions/59280/capture-from-a-wireless-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59280-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>This is the Wireshark version from Linux Command Prompt. wireshark 1.12.1, libpcap 1.6.2 and libz 1.2.8.</p><p>Our aim is to run the Wireshark in monitor mode to sniff a DLink DWR 116 router data. Launch wireshark and for mono interface monitor mode is enabled and capture is started. After that DLink router is started. I do not see any data being capture by wireshark.</p><p>Any help is appreciated.</p></div><div id="question-tags" class="tags-container tags">dlink</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '17, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/a48047c391dcd3cf78fb91f244e4ee15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gsr&#39;s gravatar image" /><p>gsr<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gsr has no accepted answers">0%</span></p></div></div><div id="comments-container-59280" class="comments-container"><span id="59290"></span><div id="comment-59290" class="comment"><div id="post-59290-score" class="comment-score"></div><div class="comment-text"><p>OK, let's start at the beginning. Have you read the following Wiki?</p><p><a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a></p><p>What do you mean by data? Are you seeing any WiFi frames in your capture (i.e., control and management frames)?</p><p>Are you capturing on the correct channel?</p><p>Configure the router with lowest possible modulation/coding scheme (MCS). For 2.4GHz band this would be 11b/g. For 5GHz band, this would be 11a. This will prevent any mismatches between what the AP supports and your WiFi capture interface supports from happening.</p></div><div id="comment-59290-info" class="comment-info"><span class="comment-age">(09 Feb '17, 07:38)</span> Amato_C</div></div></div><div id="comment-tools-59280" class="comment-tools"></div><div class="clear"></div><div id="comment-59280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

