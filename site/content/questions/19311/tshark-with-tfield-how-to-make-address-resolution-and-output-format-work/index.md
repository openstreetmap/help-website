+++
type = "question"
title = "tshark with -Tfield: How to make address resolution and output format work?"
description = '''Hi, Is there a way to make MAC address resolution work in tshark output? I use this command: c:&#92;Program Files&#92;Wireshark&amp;gt;tshark -T fields -Eheader=y -Eseparator=, -Eaggregator=&#92;s -eframe.number -eframe.time_relative -ewlan.sa -ewlan.fc.type_subtype -ewlan.da -r sample80211.pkt And the output lines...'''
date = "2013-03-08T11:58:00Z"
lastmod = "2013-03-08T11:58:00Z"
weight = 19311
keywords = [ "csv", "tshark" ]
aliases = [ "/questions/19311" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark with -Tfield: How to make address resolution and output format work?](/questions/19311/tshark-with-tfield-how-to-make-address-resolution-and-output-format-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19311-score" class="post-score" title="current number of votes">1</div><span id="post-19311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Is there a way to make MAC address resolution work in tshark output? I use this command:</p><p><code>c:\Program Files\Wireshark&gt;tshark -T fields -Eheader=y -Eseparator=, -Eaggregator=\s -eframe.number -eframe.time_relative -ewlan.sa -ewlan.fc.type_subtype -ewlan.da -r sample80211.pkt</code></p><p>And the output lines looks like the line below:</p><p><code>22,20.556985855,00:0d:67:30:3c:1c,0x08,ff:ff:ff:ff:ff:ff</code></p><p>I cannot get the mac address resolved using global manuf file when -Tfields is used with -e. In wireshark or regular tshark output I see 'Ericsson_30:3c:1c' instead of 00:0d:67:30:3c:1c'. Perhaps I am missing something.</p><p>In general, is there anyway to format the field output? E.g to have a similar content as Wireshark shows? In the example above, tshark when used with -Tfield prints wlan.fc.type_subtype as numerical value 0x08 for a Beacon frame. If I create a column in wireshark for this field I will see the string 'Beacon' (and same if I export it to CSV). Is there a way to get the same from tshark using -Tfield/-e options?</p><p>Many thanks for help, Arezoo</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '13, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/2a6a14be49fb27be119974237d57750f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arezoo&#39;s gravatar image" /><p><span>Arezoo</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arezoo has no accepted answers">0%</span></p></div></div><div id="comments-container-19311" class="comments-container"></div><div id="comment-tools-19311" class="comment-tools"></div><div class="clear"></div><div id="comment-19311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

