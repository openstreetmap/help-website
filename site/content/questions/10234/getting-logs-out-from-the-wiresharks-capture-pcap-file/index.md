+++
type = "question"
title = "Getting logs out from the Wireshark&#x27;s Capture pcap File"
description = '''I would like to get logs out of pcap files (the pcap file is converted to windows .txt file using tshark command tshark -V -r {file}) so that i can display these packet capture logs in Splunk. What is the most common,standard, correct way of getting logs out from the pcap files that are converted to...'''
date = "2012-04-18T01:42:00Z"
lastmod = "2012-04-18T11:11:00Z"
weight = 10234
keywords = [ "pcap", "log", "splunk" ]
aliases = [ "/questions/10234" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Getting logs out from the Wireshark's Capture pcap File](/questions/10234/getting-logs-out-from-the-wiresharks-capture-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10234-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to get logs out of pcap files (the pcap file is converted to windows .txt file using tshark command tshark -V -r {file}) so that i can display these packet capture logs in Splunk. What is the most common,standard, correct way of getting logs out from the pcap files that are converted to windows 7 .txt file especially when i am going to show the logs in the Splunk??</p></div><div id="question-tags" class="tags-container tags">pcap log splunk</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '12, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p>misteryuku<br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Apr '12, 01:44</p></div></div><div id="comments-container-10234" class="comments-container"><span id="10237"></span><div id="comment-10237" class="comment"><div id="post-10237-score" class="comment-score">1</div><div class="comment-text"><p>You've now asked 14 questions and have not accepted any of the answers to any of them. You do realise that folks are attempting to help you out on their own time here? Please recognise any answers that have helped by clicking the check mark icon on the answer to "accept" them.</p></div><div id="comment-10237-info" class="comment-info"><span class="comment-age">(18 Apr '12, 02:03)</span> grahamb ♦</div></div><span id="10323"></span><div id="comment-10323" class="comment"><div id="post-10323-score" class="comment-score"></div><div class="comment-text"><p>Yes sir, i understand. im very sorry about it.</p></div><div id="comment-10323-info" class="comment-info"><span class="comment-age">(19 Apr '12, 23:21)</span> misteryuku</div></div><span id="10334"></span><div id="comment-10334" class="comment"><div id="post-10334-score" class="comment-score"></div><div class="comment-text"><p>No problem, but it motivates folks to answer your questions, and helps others who may have the same question to see an "accepted" answer.</p></div><div id="comment-10334-info" class="comment-info"><span class="comment-age">(20 Apr '12, 01:56)</span> grahamb ♦</div></div></div><div id="comment-tools-10234" class="comment-tools"></div><div class="clear"></div><div id="comment-10234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10235"></span>

<div id="answer-container-10235" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10235-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As per the answers by Guy Harris to your very similar question <a href="http://ask.wireshark.org/questions/10165/using-the-wireshark-pcap-file-capture-data-as-splunk-log-data">here</a>, this is really a question for the Splunk folks, not Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '12, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10235" class="comments-container"></div><div id="comment-tools-10235" class="comment-tools"></div><div class="clear"></div><div id="comment-10235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10248"></span>

<div id="answer-container-10248" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10248-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The standard way to get log files is, as you already said in your question, to use TShark in the fashion you describe:</p><pre><code>tshark -V -r {file} &gt;log.txt</code></pre><p>as a Windows command.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '12, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10248" class="comments-container"></div><div id="comment-tools-10248" class="comment-tools"></div><div class="clear"></div><div id="comment-10248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

