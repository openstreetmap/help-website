+++
type = "question"
title = "command line usage?"
description = '''I need to take a pcap file import it into wire shark, filter it for dicom and then export the Packet Dissections as plain text. I&#x27;m doing it manually at the moment in wireshark, but was wondering if there was a way to do this from the command line. TIA. B.'''
date = "2014-06-12T13:09:00Z"
lastmod = "2014-06-12T13:30:00Z"
weight = 33738
keywords = [ "filter", "import", "line", "command", "export" ]
aliases = [ "/questions/33738" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [command line usage?](/questions/33738/command-line-usage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33738-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to take a pcap file import it into wire shark, filter it for dicom and then export the Packet Dissections as plain text. I'm doing it manually at the moment in wireshark, but was wondering if there was a way to do this from the command line.</p><p>TIA. B.</p></div><div id="question-tags" class="tags-container tags">filter import line command export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '14, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/6e0f6d1c74f4bc26b86c95e81ad62d8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BJOBrien&#39;s gravatar image" /><p>BJOBrien<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BJOBrien has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jun '14, 13:10</p></div></div><div id="comments-container-33738" class="comments-container"></div><div id="comment-tools-33738" class="comment-tools"></div><div class="clear"></div><div id="comment-33738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33741"></span>

<div id="answer-container-33741" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33741-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>tshark -Y dicom -V -r {your file}</code></pre><p>(or <code>-R dicom</code> in older versions).</p><p>You might have to use <code>-o dicom.tcp.port:NNNN</code> if the DICOM traffic is on port NNNN rather than the default port, 104.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '14, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-33741" class="comments-container"><span id="33745"></span><div id="comment-33745" class="comment"><div id="post-33745-score" class="comment-score"></div><div class="comment-text"><p>I didn't find any tshark executable on my Mac</p></div><div id="comment-33745-info" class="comment-info"><span class="comment-age">(12 Jun '14, 13:40)</span> BJOBrien</div></div><span id="33747"></span><div id="comment-33747" class="comment"><div id="post-33747-score" class="comment-score"></div><div class="comment-text"><p>If you installed Wireshark from a dmg downloaded from Wireshark.org, try re-installing it, and don't un-check the install option for the command-line tools. That should put a tshark command in <code>/usr/local/bin</code>.</p><p>If you installed Wireshark from somewhere else, check with whatever source provided Wireshark to see how to get the command-line tools installed.</p></div><div id="comment-33747-info" class="comment-info"><span class="comment-age">(12 Jun '14, 13:52)</span> Guy Harris ♦♦</div></div><span id="33748"></span><div id="comment-33748" class="comment"><div id="post-33748-score" class="comment-score"></div><div class="comment-text"><p>if my dicom server is listening on port 11112 Woud filtering on dicom (within wireshark) work or does dicom filtering assume port 104?</p></div><div id="comment-33748-info" class="comment-info"><span class="comment-age">(12 Jun '14, 14:00)</span> BJOBrien</div></div><span id="33749"></span><div id="comment-33749" class="comment"><div id="post-33749-score" class="comment-score"></div><div class="comment-text"><p>DICOM filtering assumes that Wireshark/TShark/whatever dissected the packet as DICOM.</p><p>DICOM <em>dissection</em> assumes port 104 <em>by default</em>; that's why I said "You might have to use <code>-o dicom.tcp.port:NNNN</code> if the DICOM traffic is on port NNNN rather than the default port, 104."</p><p>So, if the DICOM server is listening on port 11112, you'd need to do</p><pre><code>tshark -o dicom.tcp.port:11112 -Y dicom -V -r {your file}</code></pre><p>in TShark, and would need to change the DICOM preference "DICOM ports" to include port 11112 in Wireshark.</p></div><div id="comment-33749-info" class="comment-info"><span class="comment-age">(12 Jun '14, 14:08)</span> Guy Harris ♦♦</div></div><span id="33752"></span><div id="comment-33752" class="comment"><div id="post-33752-score" class="comment-score"></div><div class="comment-text"><p>So if I want dicom on both port 104 and port 11112 then I specify both separated by a comma in the prefrenced?</p><p>P.S. I had different columns selected in wireshark, like Source Port and Destination Port. I assume those columns that I want to include in my text export can be specified on the tshark command line as well?</p><p>What if I don't want the TCP/IP portion of the text output but just the DICOM message?</p></div><div id="comment-33752-info" class="comment-info"><span class="comment-age">(12 Jun '14, 14:38)</span> BJOBrien</div></div><span id="33753"></span><div id="comment-33753" class="comment not_top_scorer"><div id="post-33753-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So if I want dicom on both port 104 and port 11112 then I specify both separated by a comma in the prefrenced?</p></blockquote><p>Yes.</p><blockquote><p>P.S. I had different columns selected in wireshark, like Source Port and Destination Port. I assume those columns that I want to include in my text export can be specified on the tshark command line as well?</p></blockquote><p>You said "export the Packet Dissections as plain text"; I assume you meant you just wanted the information that shows up in the "packet details" pane in Wireshark. What <em>exactly</em> do you want the text output to contain? Summary pane (the columns)? Detail pane? Hex dump?</p><blockquote><p>What if I don't want the TCP/IP portion of the text output but just the DICOM message?</p></blockquote><p>You can't completely eliminate the TCP/IP portion, but <code>-O dicom</code> should cause the TShark output to look like the packet detail pane with eveything but DICOM closed.</p></div><div id="comment-33753-info" class="comment-info"><span class="comment-age">(12 Jun '14, 14:47)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-33741" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-33741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33742"></span>

<div id="answer-container-33742" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33742-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this</p><blockquote><p>tshark -nr input.pcap -Y 'dicom' -V</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '14, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33742" class="comments-container"><span id="33743"></span><div id="comment-33743" class="comment"><div id="post-33743-score" class="comment-score"></div><div class="comment-text"><p>O.k. @Guy Harris was 28 seconds faster ;-)</p></div><div id="comment-33743-info" class="comment-info"><span class="comment-age">(12 Jun '14, 13:31)</span> Kurt Knochner ♦</div></div><span id="33746"></span><div id="comment-33746" class="comment"><div id="post-33746-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I didn't find any tshark executable on my Mac<br />
</p></blockquote><p>See the answer to this question</p><blockquote><p><a href="http://ask.wireshark.org/questions/30819/how-to-setup-and-run-tshark-on-os-x-1092">http://ask.wireshark.org/questions/30819/how-to-setup-and-run-tshark-on-os-x-1092</a></p></blockquote></div><div id="comment-33746-info" class="comment-info"><span class="comment-age">(12 Jun '14, 13:52)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-33742" class="comment-tools"></div><div class="clear"></div><div id="comment-33742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

