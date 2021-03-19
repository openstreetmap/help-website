+++
type = "question"
title = "pcap anonymisation of msisdn field"
description = '''Hi all, I&#x27;m trying, for security reasons, to obfuscate some fields of a pcap file (even if CRC will not be valid) The main approach is described here.  tshark -nr myexample.pcap -T fields -e frame.number -e frame.len -e gsm_map.ss.msisdn 1 138  2 218 917267415827f2 3 138  4 138  Using this command, ...'''
date = "2013-10-01T13:05:00Z"
lastmod = "2013-10-02T00:37:00Z"
weight = 25483
keywords = [ "pcap", "tshark", "anonymisation" ]
aliases = [ "/questions/25483" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [pcap anonymisation of msisdn field](/questions/25483/pcap-anonymisation-of-msisdn-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25483-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm trying, for security reasons, to obfuscate some fields of a pcap file (even if CRC will not be valid) The main approach is described <a href="http://ask.wireshark.org/questions/25437/field-obfuscation">here</a>.</p><pre><code>tshark -nr myexample.pcap -T fields -e frame.number -e frame.len -e gsm_map.ss.msisdn
1 138 
2 218 917267415827f2
3 138 
4 138</code></pre><p>Using this command, I know that the second <a href="http://wiki.wireshark.org/GSMMAP">frame</a>, len 218 bytes, has a msisdn which must be obfuscated. The "search and modify" will find <code>917267415827f2</code> and replace with <code>91726741582XXX</code> between <strong>139</strong> and <strong>139+218</strong> bytes of pcap files</p><p>Now, if I execute</p><pre><code>tshark -nr myexample.pcap -R frame.number==2 -2 -T pdml &gt; output.xml

output.xml
&lt;code&gt;
&lt;?xml version=&quot;1.0&quot;?&gt;
&lt;?xml-stylesheet type=&quot;text/xsl&quot; href=&quot;pdml2html.xsl&quot;?&gt;
&lt;!-- You can find pdml2html.xsl in c:\Programmi\Wireshark or at http://anonsvn.wireshark.org/trunk/wireshark/pdml2html.xsl. --&gt;
&lt;pdml version=&quot;0&quot; creator=&quot;wireshark/1.10.2&quot; time=&quot;Tue Oct 01 21:46:52 2013&quot; capture_file=&quot;C:\test\gsm_map_with_ussd_string.pcap&quot;&gt;
&lt;packet&gt;
  &lt;proto name=&quot;geninfo&quot; pos=&quot;0&quot; showname=&quot;General information&quot; size=&quot;218&quot;&gt;
  &lt;/proto&gt;
  &lt;proto name=&quot;frame&quot; showname=&quot;Frame 1: 218 bytes on wire (1744 bits), 218 bytes captured (1744 bits)&quot; size=&quot;218&quot; pos=&quot;0&quot;&gt;
  &lt;/proto&gt;
  &lt;proto name=&quot;eth&quot; showname=&quot;Ethernet II, Src: 01:01:01:01:01:01 (01:01:01:01:01:01), Dst: 02:02:02:02:02:02 (02:02:02:02:02:02)&quot; size=&quot;14&quot; pos=&quot;0&quot;&gt;
  &lt;/proto&gt;
  &lt;proto name=&quot;ip&quot; showname=&quot;Internet Protocol Version 4, Src: 1.1.1.1 (1.1.1.1), Dst: 2.2.2.2 (2.2.2.2)&quot; size=&quot;20&quot; pos=&quot;14&quot;&gt;
  &lt;/proto&gt;
  &lt;proto name=&quot;sctp&quot; showname=&quot;Stream Control Transmission Protocol, Src Port: 2904 (2904), Dst Port: 2904 (2904)&quot; size=&quot;28&quot; pos=&quot;34&quot;&gt;
  &lt;/proto&gt;
  &lt;proto name=&quot;m2ua&quot; showname=&quot;MTP 2 User Adaptation Layer&quot; size=&quot;156&quot; pos=&quot;62&quot;&gt;
  &lt;/proto&gt;
  &lt;proto name=&quot;mtp3&quot; showname=&quot;Message Transfer Part Level 3&quot; size=&quot;5&quot; pos=&quot;74&quot;&gt;
  &lt;/proto&gt;
  &lt;proto name=&quot;sccp&quot; showname=&quot;Signalling Connection Control Part&quot; size=&quot;137&quot; pos=&quot;79&quot;&gt;
  &lt;/proto&gt;
  &lt;proto name=&quot;tcap&quot; showname=&quot;Transaction Capabilities Application Part&quot; size=&quot;108&quot; pos=&quot;108&quot;&gt;
  &lt;/proto&gt;
&lt;proto name=&quot;gsm_map&quot; showname=&quot;GSM Mobile Application&quot; size=&quot;38&quot; pos=&quot;178&quot;&gt;
&lt;/proto&gt;
&lt;/packet&gt;
&lt;/pdml&gt;</code></pre><p>we can note that "GSM Mobile Application", which contains the msisdn, start at byte 178 and the size is 38 byte This means, that the "search and modify" inside the frame can be done between <strong>139+178</strong> and <strong>139+178+38</strong> bytes.</p><p>Now the question: Just using tshark, is there a way, maybe using filter -e, to get pos and size of protocol "GSM Mobile Application"?</p><p>Thanks, Riccardo</p></div><div id="question-tags" class="tags-container tags">pcap tshark anonymisation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '13, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/a5626909eb9fd5bbf9e3ac3861076738?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ric79&#39;s gravatar image" /><p>Ric79<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ric79 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Oct '13, 02:05</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-25483" class="comments-container"></div><div id="comment-tools-25483" class="comment-tools"></div><div class="clear"></div><div id="comment-25483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25493"></span>

<div id="answer-container-25493" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25493-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Just using tshark, is there a way, maybe using filter -e, to get pos and size of protocol "GSM Mobile Application"?</p></blockquote><p>Only by changing the code of tshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '13, 00:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-25493" class="comments-container"></div><div id="comment-tools-25493" class="comment-tools"></div><div class="clear"></div><div id="comment-25493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

