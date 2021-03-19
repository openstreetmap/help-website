+++
type = "question"
title = "how to extract Hex data from SSL"
description = '''Hello, i want to extract the hex data from this SSL but when i type tshark -Vnr -r pcap -R (filter) &amp;gt; textfile i only get the details of the pcap without the hex part so i want to know if there is a way to extract the hex data with the details not the details only, i don&#x27;t want to decrypt or anyt...'''
date = "2013-09-30T04:35:00Z"
lastmod = "2013-09-30T13:42:00Z"
weight = 25371
keywords = [ "tshark" ]
aliases = [ "/questions/25371" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [how to extract Hex data from SSL](/questions/25371/how-to-extract-hex-data-from-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25371-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i want to extract the hex data from this SSL but when i type tshark -Vnr -r pcap -R (filter) &gt; textfile i only get the details of the pcap without the hex part so i want to know if there is a way to extract the hex data with the details not the details only, i don't want to decrypt or anything i just want to extract it to a plain text, thanks.!</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '13, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/27e19b1f6c0b00e4469bfa2fba760e79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ziad%20Kiwan&#39;s gravatar image" /><p>Ziad Kiwan<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ziad Kiwan has no accepted answers">0%</span></p></div></div><div id="comments-container-25371" class="comments-container"><span id="25375"></span><div id="comment-25375" class="comment"><div id="post-25375-score" class="comment-score"></div><div class="comment-text"><blockquote><p>i want to extract the hex data from this SSL</p></blockquote><p>do you mean the <strong>decrypted</strong> payload?</p></div><div id="comment-25375-info" class="comment-info"><span class="comment-age">(30 Sep '13, 07:00)</span> Kurt Knochner ♦</div></div><span id="25376"></span><div id="comment-25376" class="comment"><div id="post-25376-score" class="comment-score"></div><div class="comment-text"><p>when you open the pcap file using wireshark you see the detailed information and the hex information i want to retrieve them "all" using tshark is there a way ?</p></div><div id="comment-25376-info" class="comment-info"><span class="comment-age">(30 Sep '13, 07:02)</span> Ziad Kiwan</div></div><span id="25378"></span><div id="comment-25378" class="comment"><div id="post-25378-score" class="comment-score"></div><div class="comment-text"><p>So, you need the 'raw' TCP payload, regardless of SSL decryption?</p></div><div id="comment-25378-info" class="comment-info"><span class="comment-age">(30 Sep '13, 07:08)</span> Kurt Knochner ♦</div></div><span id="25379"></span><div id="comment-25379" class="comment"><div id="post-25379-score" class="comment-score"></div><div class="comment-text"><p>exactly! i want the raw data</p></div><div id="comment-25379-info" class="comment-info"><span class="comment-age">(30 Sep '13, 07:09)</span> Ziad Kiwan</div></div></div><div id="comment-tools-25371" class="comment-tools"></div><div class="clear"></div><div id="comment-25371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25415"></span>

<div id="answer-container-25415" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25415-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried using the "-x" command line option?</p><p>In your case:</p><pre><code>tshark -Vnxr pcap -R (filter) &gt; textfile</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25415" class="comments-container"><span id="25417"></span><div id="comment-25417" class="comment"><div id="post-25417-score" class="comment-score"></div><div class="comment-text"><p>sorry i'm not that good in wireshark and tshark what does vnxr do ?</p></div><div id="comment-25417-info" class="comment-info"><span class="comment-age">(30 Sep '13, 13:51)</span> Ziad Kiwan</div></div><span id="25418"></span><div id="comment-25418" class="comment"><div id="post-25418-score" class="comment-score"></div><div class="comment-text"><p>I added the "-x" option to the options you already mentioned in your original question, as that option adds the output of the hex dump.</p><pre><code>$ tshark -h | fgrep -e &quot; -V&quot; -e &quot; -x&quot; -e &quot; -r&quot; -e &quot; -n&quot;
  -r &lt;infile&gt;              set the filename to read from (no pipes or stdin!)
  -n                       disable all name resolutions (def: all enabled)
  -V                       add output of packet tree        (Packet Details)
  -x                       add output of hex and ASCII dump (Packet Bytes)
$</code></pre></div><div id="comment-25418-info" class="comment-info"><span class="comment-age">(30 Sep '13, 14:22)</span> SYN-bit ♦♦</div></div><span id="25464"></span><div id="comment-25464" class="comment"><div id="post-25464-score" class="comment-score"></div><div class="comment-text"><p>okay thanks for the information, that something good to learn!</p></div><div id="comment-25464-info" class="comment-info"><span class="comment-age">(01 Oct '13, 04:53)</span> Ziad Kiwan</div></div></div><div id="comment-tools-25415" class="comment-tools"></div><div class="clear"></div><div id="comment-25415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25380"></span>

<div id="answer-container-25380" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25380-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>exactly! i want the raw data</p></blockquote><p>O.K. please check these similar questions:</p><p>see my (last) comment regarding disabling protocols to get the payload!</p><blockquote><p><a href="http://ask.wireshark.org/questions/12431/how-to-add-data-length-column-in-wireshark-display-or-plot-payload-length-vs-packet-no">http://ask.wireshark.org/questions/12431/how-to-add-data-length-column-in-wireshark-display-or-plot-payload-length-vs-packet-no</a><br />
</p></blockquote><p>also here</p><blockquote><p><a href="http://ask.wireshark.org/questions/23827/get-tcp-and-udp-payloads-with-tshark">http://ask.wireshark.org/questions/23827/get-tcp-and-udp-payloads-with-tshark</a><br />
</p></blockquote><p>and here</p><p><a href="http://ask.wireshark.org/questions/16592/tcp-stream-output-in-pdml-format">http://ask.wireshark.org/questions/16592/tcp-stream-output-in-pdml-format</a><br />
<a href="http://ask.wireshark.org/questions/16268/how-do-i-extract-all-the-data-sections">http://ask.wireshark.org/questions/16268/how-do-i-extract-all-the-data-sections</a><br />
<a href="http://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only">http://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only</a><br />
</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Sep '13, 07:17</p></div></div><div id="comments-container-25380" class="comments-container"><span id="25383"></span><div id="comment-25383" class="comment"><div id="post-25383-score" class="comment-score"></div><div class="comment-text"><p>can i apply a a filter in this and it will keep working ? i saw this before and tried it and the data stayed the same</p></div><div id="comment-25383-info" class="comment-info"><span class="comment-age">(30 Sep '13, 07:29)</span> Ziad Kiwan</div></div><span id="25385"></span><div id="comment-25385" class="comment"><div id="post-25385-score" class="comment-score"></div><div class="comment-text"><blockquote><p>can i apply a a filter in this and it will keep working ?</p></blockquote><p>what do you mean? Which filter?</p></div><div id="comment-25385-info" class="comment-info"><span class="comment-age">(30 Sep '13, 07:55)</span> Kurt Knochner ♦</div></div><span id="25413"></span><div id="comment-25413" class="comment"><div id="post-25413-score" class="comment-score"></div><div class="comment-text"><p>its not working i'm not getting the ssl hex data out of the pcap using any of the methods you suggested, about the filter i use a filter to filter the pcap's and then i add them in a plain text</p></div><div id="comment-25413-info" class="comment-info"><span class="comment-age">(30 Sep '13, 13:37)</span> Ziad Kiwan</div></div></div><div id="comment-tools-25380" class="comment-tools"></div><div class="clear"></div><div id="comment-25380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

