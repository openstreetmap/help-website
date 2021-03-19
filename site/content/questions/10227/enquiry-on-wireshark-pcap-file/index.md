+++
type = "question"
title = "Enquiry on Wireshark pcap file"
description = '''I would like to know if a wireshark pcap file when converted to a windows 7 .txt file using the tshark command tshark -V -r {file} is considered a log file?'''
date = "2012-04-17T19:55:00Z"
lastmod = "2012-04-18T11:25:00Z"
weight = 10227
keywords = [ "txt", "pcap", "log" ]
aliases = [ "/questions/10227" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Enquiry on Wireshark pcap file](/questions/10227/enquiry-on-wireshark-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10227-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know if a wireshark pcap file when converted to a windows 7 .txt file using the tshark command tshark -V -r {file} is considered a log file?</p></div><div id="question-tags" class="tags-container tags">txt pcap log</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '12, 19:55</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p>misteryuku<br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Apr '12, 19:56</p></div></div><div id="comments-container-10227" class="comments-container"></div><div id="comment-tools-10227" class="comment-tools"></div><div class="clear"></div><div id="comment-10227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10229"></span>

<div id="answer-container-10229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10229-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No. It's a text file containing the dissection of the network data in the pcap file. The dissection may not be complete if the pcap file contains data that tshark doesn't know how to dissect.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '12, 23:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10229" class="comments-container"></div><div id="comment-tools-10229" class="comment-tools"></div><div class="clear"></div><div id="comment-10229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10251"></span>

<div id="answer-container-10251" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10251-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Considered by <em>whom</em>, or by <em>what</em>, to be a log file? If that's "considered by Splunk", you'd have to ask the Splunk people about that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '12, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10251" class="comments-container"></div><div id="comment-tools-10251" class="comment-tools"></div><div class="clear"></div><div id="comment-10251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

