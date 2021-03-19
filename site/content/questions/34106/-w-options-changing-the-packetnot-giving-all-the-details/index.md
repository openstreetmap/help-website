+++
type = "question"
title = "-w options changing the packet(not giving all the details)"
description = '''Hi ,  I have a pcap from which I filtered out using a display filter &quot;(http.request or http.response) and not tcp.analysis.duplicate_ack and not tcp.analysis.retransmission and not udp&quot; and stored the resulting pcaps using -w option using tshark. when I open the saved pcap in wireshark some of the h...'''
date = "2014-06-23T22:27:00Z"
lastmod = "2014-06-24T05:54:00Z"
weight = 34106
keywords = [ "reassembly", "tshark" ]
aliases = [ "/questions/34106" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [-w options changing the packet(not giving all the details)](/questions/34106/-w-options-changing-the-packetnot-giving-all-the-details)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34106-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi , I have a pcap from which I filtered out using a display filter "(http.request or http.response) and not tcp.analysis.duplicate_ack and not tcp.analysis.retransmission and not udp" and stored the resulting pcaps using -w option using tshark.</p><p>when I open the saved pcap in wireshark some of the http response or requests packets are converted to http continuation packet. I can understand that it is indeed a part of the http response but is there a way to save the reassembled data information as well.<br />
</p></div><div id="question-tags" class="tags-container tags">reassembly tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '14, 22:27</strong></p><img src="https://secure.gravatar.com/avatar/264381ee2d0be7b622fc3caaae35148f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guru_p&#39;s gravatar image" /><p>guru_p<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guru_p has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jun '14, 22:34</p></div></div><div id="comments-container-34106" class="comments-container"></div><div id="comment-tools-34106" class="comment-tools"></div><div class="clear"></div><div id="comment-34106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34116"></span>

<div id="answer-container-34116" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34116-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem you're seeing is that the saved pcap file doesn't include all of the TCP segments that comprise the full HTTP messages - the "http continuation" packets are ones that wireshark can't successfully decode as HTTP, because some packets are missing.</p><p>What exact command-line are you using for tshark? In particular, are you using the "<code>-R</code>" or the "<code>-Y</code>" option for the "<code>(http.request or http.response) and not tcp.analysis.duplicate_ack and not tcp.analysis.retransmission and not udp</code>" filter?</p><p>You should be using the "<code>-Y</code>" option as well as the "<code>-2</code>" option flag, as that will make it include the dependent frames and perform two-pass analysis, so it will save all of the TCP segments necessary to decode the HTTP messages. The "<code>-R</code>" does not include dependent frames.</p><p>(edited to add the "<code>-2</code>" flag as well)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '14, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jun '14, 10:43</p></div></div><div id="comments-container-34116" class="comments-container"><span id="34147"></span><div id="comment-34147" class="comment"><div id="post-34147-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply</p><p>tshark -r "pcap file" -T fields -e frame.number -Y "(http.response or http.request) and not tcp.analysis.duplicate_ack and not tcp.analysis.retransmission and not udp " -P -F pcap -w "writefile"; This is my exact command</p></div><div id="comment-34147-info" class="comment-info"><span class="comment-age">(24 Jun '14, 22:03)</span> guru_p</div></div><span id="34177"></span><div id="comment-34177" class="comment"><div id="post-34177-score" class="comment-score"></div><div class="comment-text"><p>Add the "<code>-2</code>" option flag. This causes a second pass through the file, which is also required to save dependent frames. (I forgot that two-pass is not automatic with the <code>-Y</code>, which it used to be for a short time during development)</p></div><div id="comment-34177-info" class="comment-info"><span class="comment-age">(25 Jun '14, 09:49)</span> Hadriel</div></div><span id="34181"></span><div id="comment-34181" class="comment"><div id="post-34181-score" class="comment-score">1</div><div class="comment-text"><p>@Hadriel, you should probably edit your answer to add the <code>-2</code> flag so late comers don't have to read down into the comments.</p></div><div id="comment-34181-info" class="comment-info"><span class="comment-age">(25 Jun '14, 10:16)</span> grahamb ♦</div></div><span id="34207"></span><div id="comment-34207" class="comment"><div id="post-34207-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer, It worked</p></div><div id="comment-34207-info" class="comment-info"><span class="comment-age">(25 Jun '14, 21:55)</span> guru_p</div></div></div><div id="comment-tools-34116" class="comment-tools"></div><div class="clear"></div><div id="comment-34116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

