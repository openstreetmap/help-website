+++
type = "question"
title = "tshark not converting decoded pcap to text file"
description = '''Hi, I have a pcap in tcp which I decode as Diameter on wireshark gui. I then save it. I confirmed after saving by re-opening the pcap that the tcp packets are decoded to Diameter protocol. Now, I have the decoded pcap in Diameter saved and confirmed. I need to use that decoded pcap into a script for...'''
date = "2015-11-19T07:17:00Z"
lastmod = "2015-11-19T10:52:00Z"
weight = 47748
keywords = [ "tshark" ]
aliases = [ "/questions/47748" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [tshark not converting decoded pcap to text file](/questions/47748/tshark-not-converting-decoded-pcap-to-text-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47748-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a pcap in tcp which I decode as Diameter on wireshark gui. I then save it. I confirmed after saving by re-opening the pcap that the tcp packets are decoded to Diameter protocol.</p><p>Now, I have the decoded pcap in Diameter saved and confirmed. I need to use that decoded pcap into a script for post processing. I use tshark command in the script to convert that decoded pcap to text file but the tshark converts it to zero byte text file. Below is the tshark command inside the script, assuming the pcap is decoded into Diameter protocol.</p><p>&amp; 'C:\Program Files\Wireshark\tshark.exe' -Y "diameter.Subscription-Id-Data == $a" -V -r $Server &gt; C:\text4111.txt</p><p>The result text file text4111.txt is zero byte, not succesfully converted.</p><p>Any idea, how to make this work?</p><p>Thanks Amit</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '15, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/07c93b10850aecd4916c119cc5d62bae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amitmraval&#39;s gravatar image" /><p>amitmraval<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amitmraval has no accepted answers">0%</span></p></div></div><div id="comments-container-47748" class="comments-container"></div><div id="comment-tools-47748" class="comment-tools"></div><div class="clear"></div><div id="comment-47748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47769"></span>

<div id="answer-container-47769" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47769-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do I read your question right that you had to use "Decode as" to manually tell the GUI Wireshark to decode that tcp flow as Diameter? If so, you're likely using a non-standard tcp port for Diameter, and you need to use a parameter to tell tshark the same. From <embed src="https://www.wireshark.org/docs/man-pages/tshark.html" />:</p><p><code>-d &lt; layer type&gt;==&lt; selector&gt;,&lt; decode-as protocol&gt;</code></p><p>Like Wireshark's <code>Decode As...</code> feature, this lets you specify how a layer type should be dissected. If the layer type in question (for example, <code>tcp.port</code> or <code>udp.port</code> for a TCP or UDP port number) has the specified selector value, packets should be dissected as the specified protocol.</p><p>Example: <code>-d tcp.port==&lt; your non-standard port number&gt;, diameter</code> will decode any traffic running over TCP port &lt;your non-standard="" port="" number=""&gt; as diameter.</p><p>The pcap(ng) file does <strong>not</strong> store information about manual "decode as" mappings. On the other hand, a running Wireshark session remembers them. So by saving, closing and re-opening the pcap file without closing Wireshark itself you could obtain a false feeling that the "decode as" mappings got saved to the file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '15, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Oct '16, 12:55</p></div></div><div id="comments-container-47769" class="comments-container"><span id="47794"></span><div id="comment-47794" class="comment"><div id="post-47794-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt.</p><p>Sindy, you are right. I was under impression that after decoding to Diameter on GUI wireshark, it will save for lifetime in decoded format, but it is not.</p><p>So, finally made it work by below command where I put on both the filters on single tshark command. First it decodes it to diameter protocol and then a particular diameter filter expression, all into a text file which I was looking for.</p><p>&amp; 'C:\Program Files\Wireshark\tshark.exe' -d "tcp.port==3998,diameter" -Y "diameter.Subscription-Id-Data == $a" -V -r $Server &gt; C:\text4111.txt</p><p>Thanks again for your inputs.</p><p>Regards, Amit</p></div><div id="comment-47794-info" class="comment-info"><span class="comment-age">(20 Nov '15, 08:22)</span> amitmraval</div></div><span id="47795"></span><div id="comment-47795" class="comment"><div id="post-47795-score" class="comment-score"></div><div class="comment-text"><p>For the background,</p><p>$a is the input from the user when script is executed.</p><p>$Server is the raw undecoded PCAP selected by the user before the tshark command.</p><p>$a is nothing but the Subscriber number which user wants to check and for which I put the filter in the tshark command copied above.</p></div><div id="comment-47795-info" class="comment-info"><span class="comment-age">(20 Nov '15, 08:25)</span> amitmraval</div></div></div><div id="comment-tools-47769" class="comment-tools"></div><div class="clear"></div><div id="comment-47769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47761"></span>

<div id="answer-container-47761" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47761-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Any idea, how to make this work?</p></blockquote><p>If there is nothing in the file, then your filter was not applied. As you are using a variable in the filter ($a), I guess that has not been expanded. And frankly, variables on Windows (DOS box) will be %variable% and not $variable (which is Unix style). So I guess <strong>that's</strong> the problem.</p><p>What do you get if you run this in a DOS box?</p><blockquote><p>echo $a</p></blockquote><p>If you get <strong>$a</strong> in the output, it's like I said and Wireshark/tshark would have looked for the string "$a" in <strong>diameter.Subscription-Id-Data</strong>, which makes not much sense.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '15, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-47761" class="comments-container"><span id="47765"></span><div id="comment-47765" class="comment"><div id="post-47765-score" class="comment-score"></div><div class="comment-text"><blockquote>What do you get if you run this in a DOS box?</blockquote><p>It's a PowerShell command, so simply type <code>$a</code> to show the value.</p></div><div id="comment-47765-info" class="comment-info"><span class="comment-age">(19 Nov '15, 10:01)</span> grahamb ♦</div></div></div><div id="comment-tools-47761" class="comment-tools"></div><div class="clear"></div><div id="comment-47761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

