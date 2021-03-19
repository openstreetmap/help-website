+++
type = "question"
title = "What is the difference between &quot;Continuation or non-HTTP traffic&quot; and &quot;TCP segment of a reassembled PDU&quot;"
description = '''I have a pcap file including 2 TCP streams from the same HTTP server.Displayed in Wireshark, in the 1st stream, the content from HTTP server shown as &quot;Continuation or non-HTTP traffic&quot;; while the 2nd stream the content shown as &quot;TCP segment of a reassembled PDU&quot;. I don&#x27;t find any difference between ...'''
date = "2014-05-24T07:27:00Z"
lastmod = "2014-05-24T08:07:00Z"
weight = 33031
keywords = [ "continuation", "reassembled", "segment" ]
aliases = [ "/questions/33031" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is the difference between "Continuation or non-HTTP traffic" and "TCP segment of a reassembled PDU"](/questions/33031/what-is-the-difference-between-continuation-or-non-http-traffic-and-tcp-segment-of-a-reassembled-pdu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33031-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap file including 2 TCP streams from the same HTTP server.Displayed in Wireshark, in the 1st stream, the content from HTTP server shown as "Continuation or non-HTTP traffic"; while the 2nd stream the content shown as "TCP segment of a reassembled PDU". I don't find any difference between the 2 kinds at TCP layer.</p><p>Could someone tell me how Wireshark identify them? Does Wireshark check HTTP header for content-length?</p><p>I have the pcap, but I don't know how to upload the file. Send me email [email protected] for the pcap if you need check for details.</p></div><div id="question-tags" class="tags-container tags">continuation reassembled segment</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '14, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/8ea322063f32998a82da4751ac7292b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shenfanren&#39;s gravatar image" /><p>shenfanren<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shenfanren has no accepted answers">0%</span></p></div></div><div id="comments-container-33031" class="comments-container"></div><div id="comment-tools-33031" class="comment-tools"></div><div class="clear"></div><div id="comment-33031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33032"></span>

<div id="answer-container-33032" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33032-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is probably just the result of the TCP stream reassembly feature. To verify, go to Edit -&gt; Preferences -&gt; Protocols -&gt; TCP and disable "Allow subdissector to reassemble TCP streams". Now both should show "Continuation or non-HTTP traffic". Basically the reassembly feature is trying to reconstruct payloads, which is often useful for content examination.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '14, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33032" class="comments-container"><span id="33033"></span><div id="comment-33033" class="comment"><div id="post-33033-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply. I did as you said and it is. I wonder why if enable "Allow subdissector to reassemble TCP streams" option, they are shown as different?</p></div><div id="comment-33033-info" class="comment-info"><span class="comment-age">(24 May '14, 07:51)</span> shenfanren</div></div><span id="33034"></span><div id="comment-33034" class="comment"><div id="post-33034-score" class="comment-score"></div><div class="comment-text"><p>send me email [email protected] if you have time to help me check the pcap file.</p></div><div id="comment-33034-info" class="comment-info"><span class="comment-age">(24 May '14, 07:54)</span> shenfanren</div></div><span id="33036"></span><div id="comment-33036" class="comment"><div id="post-33036-score" class="comment-score"></div><div class="comment-text"><p>I don't have time for that, and I see you've got it figured out already. Next time put your traces on <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and post the URL ;-)</p></div><div id="comment-33036-info" class="comment-info"><span class="comment-age">(24 May '14, 08:13)</span> Jasper ♦♦</div></div></div><div id="comment-tools-33032" class="comment-tools"></div><div class="clear"></div><div id="comment-33032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33035"></span>

<div id="answer-container-33035" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33035-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I find the most properly answer in another FAQ syas: The HTTP header "Content-Length" informs the HTTP dissector of how much data is expected and it keeps asking the TCP dissector for more until it receives the required amount.</p><p>In short word it based on if "content-length" exist or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '14, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/8ea322063f32998a82da4751ac7292b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shenfanren&#39;s gravatar image" /><p>shenfanren<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shenfanren has no accepted answers">0%</span></p></div></div><div id="comments-container-33035" class="comments-container"></div><div id="comment-tools-33035" class="comment-tools"></div><div class="clear"></div><div id="comment-33035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

