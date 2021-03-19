+++
type = "question"
title = "Display Filters - Importing Kismet pcapdump - Can I get unique MAC addresses?"
description = '''I have scanned wireless networks (access points) with Kismet. Kismet gives me different files, including pcapdump, which I can open in Wireshark. I am very new to Wireshark, but I am reading and trying to grasp the concepts. My main goal is to find the percentage of population using different encryp...'''
date = "2012-06-18T17:54:00Z"
lastmod = "2012-06-18T17:54:00Z"
weight = 12036
keywords = [ "wireless", "encryption", "statistics", "mac-address", "display-filter" ]
aliases = [ "/questions/12036" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display Filters - Importing Kismet pcapdump - Can I get unique MAC addresses?](/questions/12036/display-filters-importing-kismet-pcapdump-can-i-get-unique-mac-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12036-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have scanned wireless networks (access points) with Kismet. Kismet gives me different files, including pcapdump, which I can open in Wireshark. I am very new to Wireshark, but I am reading and trying to grasp the concepts.</p><p>My main goal is to find the percentage of population using different encryption types, like WEP, WPA, WPA2 etc. Can I get such statistics from Wireshark or am I barking up the wrong tree?</p><p>Would I start using the Filter Display and get unique MAC addresses first? Or would that be going about it the wrong way?</p><p>[The scanning part of my project is now complete. I have 10.000 wireless access points in about 40 different filesets. Eventually they will be merged so no duplicates exist. Right now I feel very lost and overwhelmed with different programs and security terminology, but trying to keep my head above water.]</p></div><div id="question-tags" class="tags-container tags">wireless encryption statistics mac-address display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '12, 17:54</strong></p><img src="https://secure.gravatar.com/avatar/05b8574a3ad229cb4d1c3730a563093a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hashes&#39;s gravatar image" /><p>Hashes<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hashes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jun '12, 19:07</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-12036" class="comments-container"><span id="12575"></span><div id="comment-12575" class="comment"><div id="post-12575-score" class="comment-score"></div><div class="comment-text"><p>I have got a little further in my research. I am obviously not barking up the wrong tree. I know the information is to be found in Wireshark. But I still need help. So far:</p><p>In Wireshark: wlan_mgt.fixed.capabilities.ess and wlan.fc.subtype==8</p><p>wlan_mgt.fixed.capabilities.ess because in the management frame under capabilities it states ESS capabilities: Transmitter is an AP.</p><p>wlan.fc.subtype==8 because the beacon frame only comes from the AP and I remove all information coming to the AP from other laptops etc.</p><p>I am still getting duplicates. (Not identical duplicates, but like 50 beacons from the same APs.)</p><p>In Tshark I am getting a little further, when it comes to getting rid of duplicates, but not sure I am grabbing the correct information.</p><p>tshark -r ./kis1.pcapdump -T fields -e wlan_mgt.ssid | sort | uniq</p><p>Am I on the right track? How can I get unique AP's in Wireshark? Any help is appreciated.</p></div><div id="comment-12575-info" class="comment-info"><span class="comment-age">(10 Jul '12, 14:19)</span> Hashes</div></div></div><div id="comment-tools-12036" class="comment-tools"></div><div class="clear"></div><div id="comment-12036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

