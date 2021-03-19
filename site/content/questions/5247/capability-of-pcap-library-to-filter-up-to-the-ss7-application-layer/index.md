+++
type = "question"
title = "Capability of PCAP library to filter up to the ss7 application layer?"
description = '''According to the ebook, pg 245(reader)/pg 222(book), the paragraph right above &quot;Writing Capture Filters&quot;, the author states that the PCAP library aka Capture Filter may not be as powerful as the Display Filter of Wireshark, resulting in the latter requires more execution time. My question: is Captur...'''
date = "2011-07-26T03:17:00Z"
lastmod = "2011-07-26T07:29:00Z"
weight = 5247
keywords = [ "capture-filter", "wireshark", "display-filter" ]
aliases = [ "/questions/5247" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Capability of PCAP library to filter up to the ss7 application layer?](/questions/5247/capability-of-pcap-library-to-filter-up-to-the-ss7-application-layer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5247-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>According to the <a href="http://comes.umy.ac.id/file.php/1/Pengumuman_FT/E-Book_TI/Wireshark_and_Ethereal.pdf">ebook</a>, pg 245(reader)/pg 222(book), the paragraph right above "Writing Capture Filters", the author states that the PCAP library aka Capture Filter may not be as powerful as the Display Filter of Wireshark, resulting in the latter requires more execution time.</p><p>My question: is Capture Filter (libpcap / Winpcap) capable of filtering data as deep as the SS7 application layer..</p><p>Thanks</p><p>Regards,</p><p>Eddie Choo</p></div><div id="question-tags" class="tags-container tags">capture-filter wireshark display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '11, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/c1dac05d0e75992546b5da006c6b718e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eddie%20choo&#39;s gravatar image" /><p>eddie choo<br />
<span class="score" title="66 reputation points">66</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eddie choo has 2 accepted answers">66%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jul '11, 03:18</p></div></div><div id="comments-container-5247" class="comments-container"><span id="5248"></span><div id="comment-5248" class="comment"><div id="post-5248-score" class="comment-score"></div><div class="comment-text"><p>i just noticed this paragraph:</p><blockquote><p>While tcpdump can decode protocols, it cannot directly address many of them.The keywords defined in the tcpdump filter language are oriented toward Link layer (layer 2) and Transmission Control Protocol/Internet Protocol (TCP/IP) filtering.</p></blockquote><p>pg 223(book)/pg 246 (reader)</p><p>Since it is always assumed that the MTP3 layer is equivalent to the TCP/IP layer and the Link Layer is equivalent to the MTP 1-2 layers, i think the answer to my question is no?</p><p>Thanks</p></div><div id="comment-5248-info" class="comment-info"><span class="comment-age">(26 Jul '11, 03:24)</span> eddie choo</div></div><span id="5288"></span><div id="comment-5288" class="comment"><div id="post-5288-score" class="comment-score">1</div><div class="comment-text"><p>Yes. As per my response to Jeff Morriss's answer, there are libpcap filters for MTP2 and MTP3 - not currently documented, which is a libpcap bug - but not for anything above that layer.</p></div><div id="comment-5288-info" class="comment-info"><span class="comment-age">(26 Jul '11, 19:13)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-5247" class="comment-tools"></div><div class="clear"></div><div id="comment-5247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5258"></span>

<div id="answer-container-5258" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5258-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Correct: libpcap does not currently have (capture) filters for SS7. It's not that it could not, but no one has implemented it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '11, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-5258" class="comments-container"><span id="5287"></span><div id="comment-5287" class="comment"><div id="post-5287-score" class="comment-score">1</div><div class="comment-text"><p>More accurately, it doesn't have capture filters for SS7 above MTP3. The pcap-filter man page needs to be updated to describe the MTP2 and MTP3 filters libpcap <em>does</em> implement.</p></div><div id="comment-5287-info" class="comment-info"><span class="comment-age">(26 Jul '11, 19:12)</span> Guy Harris ♦♦</div></div><span id="5309"></span><div id="comment-5309" class="comment"><div id="post-5309-score" class="comment-score"></div><div class="comment-text"><p>Doh! Silly me, looked at the documentation. (Actually I did try to look at the source, but couldn't figure it out enough to find anything... &lt;sigh&gt;)</p></div><div id="comment-5309-info" class="comment-info"><span class="comment-age">(27 Jul '11, 06:15)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-5258" class="comment-tools"></div><div class="clear"></div><div id="comment-5258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5260"></span>

<div id="answer-container-5260" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5260-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Depending on your requirements you could work around those limitations.</p><p>1) You could extend the wireshark/tshark with lua and packet tap which would save packets that match certain filters into separate files</p><p>2) You could capture files with tcpdump/dumpcap pipe them them to tshark which can then apply -R "display_filter" option</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '11, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-5260" class="comments-container"><span id="5294"></span><div id="comment-5294" class="comment"><div id="post-5294-score" class="comment-score"></div><div class="comment-text"><p>You could filter for SCTP if that's the transport protocol and/or IP/port combination(s) to limit the captured packets.</p></div><div id="comment-5294-info" class="comment-info"><span class="comment-age">(26 Jul '11, 21:35)</span> Anders ♦</div></div></div><div id="comment-tools-5260" class="comment-tools"></div><div class="clear"></div><div id="comment-5260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

