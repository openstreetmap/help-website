+++
type = "question"
title = "using command line option to save major udp/tcp flows"
description = '''Can anyone please tell me what is the difference between wireshark, ethereal and tshark ? And which one should be used for my below problem ? i want to save the major udp/tcp flows (by major i mean having maximum number of bytes) using command line ethereal (or tshark/wireshark if not possible with ...'''
date = "2012-05-17T05:08:00Z"
lastmod = "2012-05-17T06:08:00Z"
weight = 11098
keywords = [ "tethereal", "tshark", "command-line", "wireshark" ]
aliases = [ "/questions/11098" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [using command line option to save major udp/tcp flows](/questions/11098/using-command-line-option-to-save-major-udptcp-flows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11098-score" class="post-score" title="current number of votes">0</div><span id="post-11098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone please tell me what is the difference between wireshark, ethereal and tshark ? And which one should be used for my below problem ?</p><p>i want to save the major udp/tcp flows (by major i mean having maximum number of bytes) using command line ethereal (or tshark/wireshark if not possible with ethereal) , to a separate pcap. Then sometimes, i would like to even save the 2nd major udp &amp; tcp flows (want to save udp and tcp flows separately) in a separate pcap. just to start with using command line ethereal, i used following cmd to save tcp conversation in a separate pcap file but this too doesn't work (rather it opens a gui window with tcp flows but doesn't save in separate file)</p><pre><code>ethereal -r sample.pcap -z conv,tcp -w ./sample_tcp.pcap</code></pre><p>Please let me know how can i save the major flows. any help will be greatly appreciated. thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tethereal" rel="tag" title="see questions tagged &#39;tethereal&#39;">tethereal</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '12, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/ce14610470a60c9adcc5f03599f66608?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="viks&#39;s gravatar image" /><p><span>viks</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="viks has no accepted answers">0%</span></p></div></div><div id="comments-container-11098" class="comments-container"></div><div id="comment-tools-11098" class="comment-tools"></div><div class="clear"></div><div id="comment-11098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11102"></span>

<div id="answer-container-11102" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11102-score" class="post-score" title="current number of votes">2</div><span id="post-11102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="viks has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ethereal is the old name for Wireshark and any executables of that name are obsolete and shouldn't be used.</p><p>Wireshark is a GUI protocol analyzer, tshark is the command line version of Wireshark. tshark can output conversations (the *shark name for flows) using the <code>-z conv,tcp</code> option you have listed. The output is a text table with the conversations listed in order of total number of frames.</p><p>To save each flow in the original capture file to a separate file of its own will require some scripting to:</p><ol><li>Determine the top flow in the original capture using the sort order of your choice by parsing the output of <code>z conv,tcp</code></li><li>Calculate a read filter for that flow (source and dest IP's and ports ??).</li><li>Read the original file, applying the filter obtained in 2. and outputting the result to a new file.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '12, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-11102" class="comments-container"></div><div id="comment-tools-11102" class="comment-tools"></div><div class="clear"></div><div id="comment-11102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

