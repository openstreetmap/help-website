+++
type = "question"
title = "Dump packet &#x27;Leftover Data Capture&#x27; field only?"
description = '''I have usb traffic pcap files that I would like to take the value from the &#x27;Leftover capture data&#x27; field and have all of the data from that field in every packet save to a new file. I can do this by right clicking on the field and selecting &quot;Export selected package bytes...&quot; for a single packet, but...'''
date = "2015-06-18T07:38:00Z"
lastmod = "2015-06-18T14:17:00Z"
weight = 43330
keywords = [ "output", "data", "usb" ]
aliases = [ "/questions/43330" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dump packet 'Leftover Data Capture' field only?](/questions/43330/dump-packet-leftover-data-capture-field-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43330-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have usb traffic pcap files that I would like to take the value from the 'Leftover capture data' field and have all of the data from that field in every packet save to a new file. I can do this by right clicking on the field and selecting "Export selected package bytes..." for a single packet, but I need a fast way to do it for all of them. Does anyone know if there is a way to do this?</p><p>Windows based solutions would also be preferred.</p></div><div id="question-tags" class="tags-container tags">output data usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '15, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/e11c789e2599b67daa0b0db281ac60d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dippy&#39;s gravatar image" /><p>dippy<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dippy has no accepted answers">0%</span></p></div></div><div id="comments-container-43330" class="comments-container"></div><div id="comment-tools-43330" class="comment-tools"></div><div class="clear"></div><div id="comment-43330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43344"></span>

<div id="answer-container-43344" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43344-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand you right then just need the content of the field "usb.capdata" (USB Leftover) printed in a single file. This goal could be reached quick and easy with the following tshark windows command line example:</p><p>tshark -r "C:\Temp\USB_Leftover.pcap" -T fields -e usb.capdata &gt; C:\Temp\output.txt</p><p>The Output contains only the value of the field "usb.capdata". Every Packet is represented by a line. If a line is empty, then the specific packet doesn´t contain the field "usb.capdata"</p><p>Example:</p><pre><code>41:6e:00:65:00:77::ff

74:68:69:73:20:69::00</code></pre><p>Or do you need further field informations?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '15, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-43344" class="comments-container"><span id="43366"></span><div id="comment-43366" class="comment"><div id="post-43366-score" class="comment-score"></div><div class="comment-text"><p>I need the character representation of the hex/ascii to print out. So if the value is 61 (hex) I need that to be a.</p></div><div id="comment-43366-info" class="comment-info"><span class="comment-age">(19 Jun '15, 06:00)</span> dippy</div></div><span id="43386"></span><div id="comment-43386" class="comment"><div id="post-43386-score" class="comment-score"></div><div class="comment-text"><p>You could try this:</p><pre><code>tshark -r &quot;C:\Temp\USB_Leftover.pcap&quot; -T fields -e usb.capdata -Y usb.capdata &gt;C:\Temp\test3.txt</code></pre><p>After that you could do the following steps:</p><p>1. Open the file C:\Temp\test3.txt with an editor and remove all ":"</p><p>2. Then copy the data and paste it into a the hex view of a hex editor. (I tried PSPad)</p></div><div id="comment-43386-info" class="comment-info"><span class="comment-age">(19 Jun '15, 13:45)</span> Christian_R</div></div><span id="43389"></span><div id="comment-43389" class="comment"><div id="post-43389-score" class="comment-score"></div><div class="comment-text"><p>Further remark:</p><p>Under Linux you can use the command xxd to convert the hex dump into a binary. This tool is part of the vim for windows port and can be found here:</p><p><a href="https://bitbucket.org/Haroogan/vim-for-windows/downloads">https://bitbucket.org/Haroogan/vim-for-windows/downloads</a></p><p>Regarding to my last comment the command you can use instead of step 2 is:</p><pre><code>xxd -r  -ps C:\temp\test3.txt &gt; c:\temp\test3.bin</code></pre></div><div id="comment-43389-info" class="comment-info"><span class="comment-age">(19 Jun '15, 14:46)</span> Christian_R</div></div></div><div id="comment-tools-43344" class="comment-tools"></div><div class="clear"></div><div id="comment-43344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

