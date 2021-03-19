+++
type = "question"
title = "Determining unique MAC and IP addresses in a PCAP"
description = '''Using tshark or Wireshark, is there a filter for unique MAC address, IP addresses? I would like to list all of the unique address in a PCAP. Or will this require some scripting to grep the output of tshark/tcpdump and then sort based on uniq output. Thanks'''
date = "2011-06-29T17:12:00Z"
lastmod = "2017-05-08T19:49:00Z"
weight = 4827
keywords = [ "wireshark", "mac-address", "tshark" ]
aliases = [ "/questions/4827" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Determining unique MAC and IP addresses in a PCAP](/questions/4827/determining-unique-mac-and-ip-addresses-in-a-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4827-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using tshark or Wireshark, is there a filter for unique MAC address, IP addresses? I would like to list all of the unique address in a PCAP. Or will this require some scripting to grep the output of tshark/tcpdump and then sort based on uniq output.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">wireshark mac-address tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '11, 17:12</strong></p><img src="https://secure.gravatar.com/avatar/4a373a79b0b8b47a11ec70974669f469?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pyxis&#39;s gravatar image" /><p>Pyxis<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pyxis has no accepted answers">0%</span></p></div></div><div id="comments-container-4827" class="comments-container"><span id="4828"></span><div id="comment-4828" class="comment"><div id="post-4828-score" class="comment-score"></div><div class="comment-text"><p>Other than Statistics, Conversations? Wouldn't that do what you need?</p></div><div id="comment-4828-info" class="comment-info"><span class="comment-age">(29 Jun '11, 18:38)</span> hansangb</div></div><span id="4841"></span><div id="comment-4841" class="comment"><div id="post-4841-score" class="comment-score"></div><div class="comment-text"><p>Both of your answers worked quite well...</p></div><div id="comment-4841-info" class="comment-info"><span class="comment-age">(29 Jun '11, 21:28)</span> Pyxis</div></div></div><div id="comment-tools-4827" class="comment-tools"></div><div class="clear"></div><div id="comment-4827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4831"></span>

<div id="answer-container-4831" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4831-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>Count unique IP addresses: tshark -r &lt;input.pcap&gt; -T fields -e ip.dst ip.src | sort | uniq</p><p>Count unique Ethernet addresses: tshark -r &lt;input.pcap&gt; -T fields -e eth.dst eth.src | sort | uniq</p><p>Note that e.g. ip.addr, which seems natural, actually lists out IP conversation endpoints.</p><p>(with many thanks, and a shout-out to Sake Blok)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '11, 19:40</strong></p><img src="https://secure.gravatar.com/avatar/b260fb38b621169269b5030f1ed6b766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="griff&#39;s gravatar image" /><p>griff<br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="griff has 2 accepted answers">10%</span></p></div></div><div id="comments-container-4831" class="comments-container"><span id="4832"></span><div id="comment-4832" class="comment"><div id="post-4832-score" class="comment-score"></div><div class="comment-text"><p>Sounds like you were at sharkfest!</p></div><div id="comment-4832-info" class="comment-info"><span class="comment-age">(29 Jun '11, 19:41)</span> zachad</div></div><span id="4838"></span><div id="comment-4838" class="comment"><div id="post-4838-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the feedback!</p></div><div id="comment-4838-info" class="comment-info"><span class="comment-age">(29 Jun '11, 21:26)</span> Pyxis</div></div></div><div id="comment-tools-4831" class="comment-tools"></div><div class="clear"></div><div id="comment-4831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4830"></span>

<div id="answer-container-4830" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4830-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>As <a href="http://ask.wireshark.org/users/255/hansangb/">hangsanb</a> alluded to, you can use Wireshark's <code>Statistics -&gt; Endpoints</code>, then choose the <code>Ethernet</code> tab for a list of unique MAC addresses, and choose the <code>IPv4</code> (or <code>IPv6</code>) tab for the list of unique IP addresses. You probably want to disable name resolution to see the actual values instead of the resolved OUI's or domain names. The nice thing about <code>Statistics -&gt; Endpoints</code> is that it comes equipped with a "Copy" button so you can easily copy all the relevant information about those endpoints to a text/csv file for further analysis/reporting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '11, 19:00</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4830" class="comments-container"><span id="4840"></span><div id="comment-4840" class="comment"><div id="post-4840-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the Wireshark answer, did not realize I could only mark one correct response.</p></div><div id="comment-4840-info" class="comment-info"><span class="comment-age">(29 Jun '11, 21:27)</span> Pyxis</div></div></div><div id="comment-tools-4830" class="comment-tools"></div><div class="clear"></div><div id="comment-4830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61294"></span>

<div id="answer-container-61294" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61294-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The answer from <a href="https://ask.wireshark.org/users/850/griff"></a><a href="https://ask.wireshark.org/users/850/griff">@griff</a></a> doesn't seem to work as expected, at least in WireShark/TShark 2.0.2. Instead of displaying <em>both</em> the source and destination IP/MAC addresses, it only shows results for the first <em>-e</em> field.</p><p>My workaround is displaying both fields (<em>-e ... -e ...</em>), and then replacing tabs with newlines with (<em>tr "\t" "\n"</em>). This leaves the final command as follows:</p><p><strong>Listing all unique IP addresses</strong>:</p><pre><code>tshark -r input.pcap -T fields -e ip.src -e ip.dst | tr &quot;\t&quot; &quot;\n&quot; | sort | uniq</code></pre><p><strong>Listing all unique MAC addresses</strong>:</p><pre><code>tshark -r input.pcap -T fields -e eth.src -e eth.dst | tr &quot;\t&quot; &quot;\n&quot; | sort | uniq</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '17, 19:49</strong></p><img src="https://secure.gravatar.com/avatar/ea7aaaf41d8d1270bdc3c20a8ca283d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlexAltea&#39;s gravatar image" /><p>AlexAltea<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlexAltea has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 May '17, 22:32</p></div></div><div id="comments-container-61294" class="comments-container"><span id="61309"></span><div id="comment-61309" class="comment"><div id="post-61309-score" class="comment-score">1</div><div class="comment-text"><p>I like your answer better than the accepted one.</p><p>In fact, the accepted one must have a mistake, because you need a <code>-e</code> for <em>every</em> field to be displayed, but even then you would end up with 2 IP or Ethernet addresses per line, so unless you perform the tab-to-newline trick you did, you could end up with unique <strong>pairs</strong> of addresses instead of just unique addresses, which is really what you want.</p></div><div id="comment-61309-info" class="comment-info"><span class="comment-age">(09 May '17, 06:58)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-61294" class="comment-tools"></div><div class="clear"></div><div id="comment-61294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

