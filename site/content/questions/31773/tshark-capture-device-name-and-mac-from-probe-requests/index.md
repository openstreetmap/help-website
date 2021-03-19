+++
type = "question"
title = "tshark capture device name and mac from probe requests"
description = '''Hi, When i run -&amp;gt; sudo tshark -S -l -i mon0 -R &#x27;wlan.fc.type_subtype eq 4&#x27; , I get 12.841925 Apple_11:11:11 -&amp;gt; Broadcast 802.11 151 Probe Request, SN=1932, FN=0, Flags=........C, SSID=Broadcast It gives me the device name(Apple_11:11:11) and SSID but not mac address. When i run -&amp;gt; sudo tsha...'''
date = "2014-04-13T19:38:00Z"
lastmod = "2014-04-14T08:09:00Z"
weight = 31773
keywords = [ "tshark" ]
aliases = [ "/questions/31773" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark capture device name and mac from probe requests](/questions/31773/tshark-capture-device-name-and-mac-from-probe-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31773-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>When i run -&gt; sudo tshark -S -l -i mon0 -R 'wlan.fc.type_subtype eq 4' , I get</p><p>12.841925 Apple_11:11:11 -&gt; Broadcast 802.11 151 Probe Request, SN=1932, FN=0, Flags=........C, SSID=Broadcast</p><p>It gives me the device name(Apple_11:11:11) and SSID but not mac address.</p><p>When i run -&gt; sudo tshark -S -l -i mon0 -R 'wlan.fc.type_subtype eq 4' -T fields -e wlan.sa -e wlan_mgt.ssid</p><p>i get MACADDRESS SSIDName , mac address does not have device name.</p><p>I need to get device name and MAC address for the device from a single command. Please help with the options</p><p>I want output as below</p><p>Apple , Inc . | 40: a6 : d9 : ee : | -28 dB | 1 | ''</p><p>SAMSUNG ELECTRO | 20:64:32: c1 : | -45 dB | 1 | ''</p><p>Murata Manufact | 00:37:6 d: ea : | -88 dB | 1 | ''</p><p>Thanks Sandeep</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '14, 19:38</strong></p><img src="https://secure.gravatar.com/avatar/a9a5f24be19664f4be8be18756e73b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnsandeep&#39;s gravatar image" /><p>gnsandeep<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnsandeep has no accepted answers">0%</span></p></div></div><div id="comments-container-31773" class="comments-container"></div><div id="comment-tools-31773" class="comment-tools"></div><div class="clear"></div><div id="comment-31773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31794"></span>

<div id="answer-container-31794" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31794-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As of <a href="http://anonsvn.wireshark.org/viewvc?revision=51742&amp;view=revision">revision 51742</a>, you can use:</p><pre><code>-T fields -e wlan.sa_resolved -e wlan.sa</code></pre><p>See the answer I provided to <a href="http://ask.wireshark.org/questions/24314/possible-to-use-the-mac-info-in-the-wireshark-manuf-file-as-part-of-display-filter">this</a> question for more details. And here are two more related questions:</p><ul><li><a href="http://ask.wireshark.org/questions/25673/creating-an-wlanta-column-does-not-provide-mac-addr-name-resolution">http://ask.wireshark.org/questions/25673/creating-an-wlanta-column-does-not-provide-mac-addr-name-resolution</a></li><li><a href="http://ask.wireshark.org/questions/25197/mac-address-resolution-in-tshark">http://ask.wireshark.org/questions/25197/mac-address-resolution-in-tshark</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '14, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-31794" class="comments-container"></div><div id="comment-tools-31794" class="comment-tools"></div><div class="clear"></div><div id="comment-31794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

