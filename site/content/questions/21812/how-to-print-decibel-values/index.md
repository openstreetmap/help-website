+++
type = "question"
title = "How to print decibel values?"
description = '''Wireshark capture results show -127.876344 dBm corresponding to HEX values D6 5B CC D8. Please, let me know how to incorporate this conversion in my dissector file.'''
date = "2013-06-07T00:00:00Z"
lastmod = "2013-06-08T08:59:00Z"
weight = 21812
keywords = [ "dbm" ]
aliases = [ "/questions/21812" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to print decibel values?](/questions/21812/how-to-print-decibel-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21812-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark capture results show -127.876344 dBm corresponding to HEX values D6 5B CC D8. Please, let me know how to incorporate this conversion in my dissector file.</p></div><div id="question-tags" class="tags-container tags">dbm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '13, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/dd64de546bcf7652a4faed163ff02df0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunshine&#39;s gravatar image" /><p>sunshine<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunshine has no accepted answers">0%</span></p></div></div><div id="comments-container-21812" class="comments-container"><span id="21831"></span><div id="comment-21831" class="comment"><div id="post-21831-score" class="comment-score"></div><div class="comment-text"><p>Can you paste some (4-5) samples with their hexadecimal reprensentation</p></div><div id="comment-21831-info" class="comment-info"><span class="comment-age">(08 Jun '13, 02:00)</span> mrEEde2</div></div><span id="21837"></span><div id="comment-21837" class="comment"><div id="post-21837-score" class="comment-score"></div><div class="comment-text"><p>There are several places where Wireshark reports a value in dBm. Some of them encode it as an 8-bit value, so it only corresponds to one hex digit. Which <em>particular</em> dBm value are you talking about? What does Wireshark call the value (no, it doesn't call it "dBm", it calls it something such as "Maximum Transmit Power Level" or "dBm antenna signal" or "SSI Signal" or something such as that). The way it's encoded depends on which particular value it is.</p></div><div id="comment-21837-info" class="comment-info"><span class="comment-age">(08 Jun '13, 17:10)</span> Guy Harris ♦♦</div></div><span id="21865"></span><div id="comment-21865" class="comment"><div id="post-21865-score" class="comment-score"></div><div class="comment-text"><p>The HEX values are for "Maximum per tone Rx Power measured per symbol over all Antennas" transmitted in "Ranging Measurement Indication" msg over PHY-UL in Wimax 802.16e-2005.</p><p>Ranging Measurement Indication is used to indicate the Rx Power estimate on the Ranging region in an uplink subframe.</p><p>We are not having the source code of Wireshark for the particular dissector. And in order to create one, I need to know the method of displaying 'dBm' values.</p><p>Other sample outputs are: WMX MAX MEAS VALUES: -129.998030dbm HEX : d5 70 a4 1d</p><p>WMX MAX MEAS VALUES: -130.555241dbm HEX : d5 63 13 e0</p><p>WMX MAX MEAS VALUES: -131.037723dbm HEX : d5 58 a8 f2</p></div><div id="comment-21865-info" class="comment-info"><span class="comment-age">(09 Jun '13, 22:26)</span> sunshine</div></div><span id="21875"></span><div id="comment-21875" class="comment"><div id="post-21875-score" class="comment-score"></div><div class="comment-text"><p>Well, I'm confused. You say that, <em>"Wireshark capture results show -127.876344 dBm corresponding to HEX values D6 5B CC D8."</em>; yet you then go on to mention in your comments that, <em>"We are not having the source code of Wireshark for the particular dissector. And in order to create one, I need to know the method of displaying 'dBm' values."</em></p><p>If Wireshark is presenting the hex values of D6 5B CC D8 as -127.876344 dBm, then there is a dissector doing that. Obviously it must be the WiMax dissector in this case, and you can find the WiMax source code in 3 subdirectories, <a href="http://anonsvn.wireshark.org/viewvc/trunk/plugins/wimax/">wimax</a>, <a href="http://anonsvn.wireshark.org/viewvc/trunk/plugins/wimaxasncp/">wimaxasncp</a> and <a href="http://anonsvn.wireshark.org/viewvc/trunk/plugins/wimaxmacphy/">wimaxmacphy</a> under the plugins directory.</p><p>Also, I searched the <a href="http://standards.ieee.org/getieee802/download/802.16e-2005.pdf">802.16e-2005</a> standard, but failed to find any of the text you mentioned. Which section exactly are you referring to? It would help if you could provide a small capture file.</p></div><div id="comment-21875-info" class="comment-info"><span class="comment-age">(10 Jun '13, 07:43)</span> cmaynard ♦♦</div></div><span id="22031"></span><div id="comment-22031" class="comment"><div id="post-22031-score" class="comment-score"></div><div class="comment-text"><p>A Google search for</p><pre><code>wimax &quot;ranging measurement indication&quot;</code></pre><p>finds only, err, umm, this question. Perhaps you're using the wrong terminology when you say "Ranging Measurement Indication"?</p><p>The same happens for a Google search for</p><pre><code>&quot;Maximum per tone Rx Power measured per symbol over all Antennas&quot;</code></pre><p>even <em>without</em> adding "wimax" to the search argument.</p><p>And I can't find that text in 802.16e-2005, either.</p></div><div id="comment-22031-info" class="comment-info"><span class="comment-age">(13 Jun '13, 14:37)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-21812" class="comment-tools"></div><div class="clear"></div><div id="comment-21812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21834"></span>

<div id="answer-container-21834" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21834-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try looking at the Wireshark <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/">source code</a> of the particular dissector doing the conversion.<br />
</p><p>Of course, if you know the protocol in question, you could also read the relevant RFC or specification, if it's available, to see how the dBm value is being encoded.</p><p>If you still can't figure it out, try posting a sample capture file to <a href="http://cloudshark.org/">cloudshark</a> and providing a link to it here so we'll know which protocol this pertains to and how it's being dissected and presented.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '13, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></p></div></div><div id="comments-container-21834" class="comments-container"></div><div id="comment-tools-21834" class="comment-tools"></div><div class="clear"></div><div id="comment-21834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

