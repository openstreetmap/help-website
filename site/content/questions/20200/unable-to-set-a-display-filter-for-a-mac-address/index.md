+++
type = "question"
title = "Unable to set a display filter for a MAC address"
description = '''Using Wireshark with a wireless interface card, I have been foiled at using display filters for a MAC address. After capturing traffic and seeing the desired MAC address in many Source and Destination rows, the right-click &amp;gt; Apply as Filter &amp;gt; Selected command fills in the Filter: field with th...'''
date = "2013-04-08T13:39:00Z"
lastmod = "2013-04-08T15:42:00Z"
weight = 20200
keywords = [ "filter", "eth", "mac", "display" ]
aliases = [ "/questions/20200" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to set a display filter for a MAC address](/questions/20200/unable-to-set-a-display-filter-for-a-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20200-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Wireshark with a wireless interface card, I have been foiled at using display filters for a MAC address.</p><p>After capturing traffic and seeing the desired MAC address in many Source and Destination rows, the right-click &gt; Apply as Filter &gt; Selected command fills in the Filter: field with the apparently correct eth.src statement with the desired MAC address, but this causes all displayed rows to go blank. Clearing the filter brings back all the rows.</p><p>I'm running Wireshark on a MacBook Air.</p><p>Thanks in advance for your help!</p></div><div id="question-tags" class="tags-container tags">filter eth mac display</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '13, 13:39</strong></p><img src="https://secure.gravatar.com/avatar/f8c9295de767e10e7cfe22381e79cbad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SwiftAero&#39;s gravatar image" /><p>SwiftAero<br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SwiftAero has no accepted answers">0%</span></p></div></div><div id="comments-container-20200" class="comments-container"></div><div id="comment-tools-20200" class="comment-tools"></div><div class="clear"></div><div id="comment-20200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20212"></span>

<div id="answer-container-20212" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20212-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you try one of these display filters:</p><blockquote><p><code>Source Addr: wlan.sa == xx:xx:xx:xx:xx:xx</code><br />
<code>Destination Addr: wlan.da == xx:xx:xx:xx:xx:xx</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 15:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Apr '13, 15:59</p></div></div><div id="comments-container-20212" class="comments-container"><span id="20225"></span><div id="comment-20225" class="comment"><div id="post-20225-score" class="comment-score"></div><div class="comment-text"><p>Excellent! That works great. Thank you very much!</p><p>I'm also interested in understanding why eth.src == xx:xx:xx:xx:xx:xx does not work, especially because Wireshark suggests that when the column is right-clicked. Any thoughts?</p></div><div id="comment-20225-info" class="comment-info"><span class="comment-age">(08 Apr '13, 18:05)</span> SwiftAero</div></div><span id="20233"></span><div id="comment-20233" class="comment"><div id="post-20233-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'm also interested in understanding why eth.src == xx:xx:xx:xx:xx:xx does not work,</p></blockquote><p>because there is no ethernet header.</p><blockquote><p>especially because Wireshark suggests that when the column is right-clicked. Any thoughts?</p></blockquote><p>I think the GUI-generated display filters are not 'prepared' to handle situations when there is no ethernet header. You can add an enhancement bug at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> if you want that 'fixed'</p></div><div id="comment-20233-info" class="comment-info"><span class="comment-age">(09 Apr '13, 03:07)</span> Kurt Knochner ♦</div></div><span id="20259"></span><div id="comment-20259" class="comment"><div id="post-20259-score" class="comment-score"></div><div class="comment-text"><p>It doesn't work because the addresses in question are put into the protocol tree as part of the 802.11 link-layer header, and thus begin with "wlan."; Ethernet addresses are put in as part of the Ethernet header, and thus begin with "eth."</p><p>What Wireshark <em>should</em> have is something such as "{src,dot} host XX:XX:XX:XX:XX:XX", i.e. a syntax like the libpcap capture filter syntax, which will look for packets where the {source,destination} link-layer address (or either address, if neither "src" nor "dot" are specified) is equal to the specified address, regardless of whether the packet is Ethernet or 802.11 or... (as long as it <em>has</em> IEEE 802-style MAC addresses; not all link layers do).</p><p>It currently doesn't. However, the development version should, if you have 802.11 packets, suggest "wlan.sa = XX:XX:XX:XX:XX:XX" if you Command-click the Src column and "wlan.da = XX:XX:XX:XX:XX:XX" if you Command-click the Dst column.</p></div><div id="comment-20259-info" class="comment-info"><span class="comment-age">(09 Apr '13, 20:05)</span> Guy Harris ♦♦</div></div><span id="20261"></span><div id="comment-20261" class="comment"><div id="post-20261-score" class="comment-score"></div><div class="comment-text"><p>TTE dissector solves this differently, it picks up the id's of "eth.src" and "eth.dst" and uses those to add proto tree items. These could be added as hidden (gasp) items to ieee80211 wlan.sa and wlan.da items.</p><p>The real solution would be to register (per frame) with the column type what hf is applicable for the current contents of the column, so proper filter expressions can be composed.</p></div><div id="comment-20261-info" class="comment-info"><span class="comment-age">(09 Apr '13, 23:12)</span> Jaap ♦</div></div></div><div id="comment-tools-20212" class="comment-tools"></div><div class="clear"></div><div id="comment-20212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

