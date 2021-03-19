+++
type = "question"
title = "tshark to capture MAC ADDRESSES as well as src and dst ip addresses"
description = '''Hi, I am working on a project and I have the following commands to capture network traffic (using ICMP MAINLY). The commands are as follows: &quot;C://Program Files/Wireshark/tshark&quot; -i &quot;Local Area Connection&quot; -a duration:10 -w C://Temp/tsharkData  &quot;C://Program Files/Wireshark/tshark&quot; -r C:&#92;Temp&#92;tsharkDa...'''
date = "2015-03-27T08:48:00Z"
lastmod = "2015-03-27T08:55:00Z"
weight = 40941
keywords = [ "fields", "tshark" ]
aliases = [ "/questions/40941" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark to capture MAC ADDRESSES as well as src and dst ip addresses](/questions/40941/tshark-to-capture-mac-addresses-as-well-as-src-and-dst-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40941-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am working on a project and I have the following commands to capture network traffic (using ICMP MAINLY).</p><p>The commands are as follows:</p><pre><code>&quot;C://Program Files/Wireshark/tshark&quot; -i &quot;Local Area Connection&quot; -a duration:10 -w C://Temp/tsharkData</code></pre><p><code>"C://Program Files/Wireshark/tshark" -r C:\Temp\tsharkData -T fields -e frame.number -e ip.src -e ip.dst -e frame.len -e frame.time -e frame.time_relative -E header=y -E separator=, &gt; C:\\Temp\tsharkData.txt</code> (THIS IS TO CONVERT THE RAW DATA TO HUMAN READABLE FORMAT)</p><p>At this point how do I get it to capture and siaplay MAC addresses of the traffic that is being captured.</p><p>NEED COMMAND USING tshark as this will help me create my automation system for shutting down ports in a DoS attack.</p><p>ALL HELP WILL BE MUCH APPRECIATED.</p><p>THANKS IN ADVANCE</p></div><div id="question-tags" class="tags-container tags">fields tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '15, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/40e0cf05e5b1089b5c7f4db6526ec48f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naeemtania&#39;s gravatar image" /><p>naeemtania<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naeemtania has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Mar '15, 10:22</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-40941" class="comments-container"></div><div id="comment-tools-40941" class="comment-tools"></div><div class="clear"></div><div id="comment-40941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40942"></span>

<div id="answer-container-40942" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40942-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to add the fields for the mac addresses.</p><p>Assuming you're using wired Ethernet, to find the field names open any capture in Wireshark, expand the protocol tree for the Ethernet II part, and select the Destination and Source fields in turn and look at the field description in the status bar at the bottom left. The field name will be in parentheses. So for Ethernet MAC addresses you need <code>eth.dst</code> and <code>eth.src</code> and they can be added to your command line as additional <code>-e</code> options</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '15, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40942" class="comments-container"><span id="40943"></span><div id="comment-40943" class="comment"><div id="post-40943-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thanks a lot, make more sense to me however I can find the bit where I can add eth.dst and ets.src in a protocol tree.</p><p>Can you please tell me which option I need to go to in order to add the eth.dst and eth.src expressions for tshark.</p><p>Thanks a lot</p><p>Much appreciate</p><p>(ps. Not familiar with wireshark)</p></div><div id="comment-40943-info" class="comment-info"><span class="comment-age">(27 Mar '15, 09:28)</span> naeemtania</div></div><span id="40944"></span><div id="comment-40944" class="comment"><div id="post-40944-score" class="comment-score"></div><div class="comment-text"><p>Just slot the extra fields into your command line. Using the line you posted in your question:</p><p><code>"C:\Program Files\Wireshark\tshark" -r C:\Temp\tsharkData -T fields -e frame.number -e ip.src -e ip.dst -e eth.src -e eth.dst -e frame.len -e frame.time -e frame.time_relative -E header=y -E separator=, &gt; C:\Temp\tsharkData.txt</code></p></div><div id="comment-40944-info" class="comment-info"><span class="comment-age">(27 Mar '15, 10:21)</span> grahamb ♦</div></div></div><div id="comment-tools-40942" class="comment-tools"></div><div class="clear"></div><div id="comment-40942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

