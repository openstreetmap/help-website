+++
type = "question"
title = "Splitting a large file"
description = '''An older capture now produces file sizes that are too large for WS to open. Is there a way to tell WS to open just a portion of the file, or to split the file into smaller pieces? It is not possible to change the capture at this time.'''
date = "2011-12-19T13:26:00Z"
lastmod = "2011-12-22T13:44:00Z"
weight = 8048
keywords = [ "split" ]
aliases = [ "/questions/8048" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Splitting a large file](/questions/8048/splitting-a-large-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8048-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>An older capture now produces file sizes that are too large for WS to open. Is there a way to tell WS to open just a portion of the file, or to split the file into smaller pieces? It is not possible to change the capture at this time.</p></div><div id="question-tags" class="tags-container tags">split</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '11, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/ec503afc725df3991f3a30d4a5e54872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="truman220&#39;s gravatar image" /><p>truman220<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="truman220 has no accepted answers">0%</span></p></div></div><div id="comments-container-8048" class="comments-container"></div><div id="comment-tools-8048" class="comment-tools"></div><div class="clear"></div><div id="comment-8048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="8049"></span>

<div id="answer-container-8049" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8049-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think editcap ought to be able to help you here. Read about it in the <a href="http://www.wireshark.org/docs/man-pages/editcap.html">man</a> page or the <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppToolseditcap.html">user guide</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '11, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-8049" class="comments-container"></div><div id="comment-tools-8049" class="comment-tools"></div><div class="clear"></div><div id="comment-8049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8085"></span>

<div id="answer-container-8085" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8085-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I used editcap -r filein fileout 1-80000 to make manageable chunks for Excel. Thanks for the help!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '11, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/ec503afc725df3991f3a30d4a5e54872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="truman220&#39;s gravatar image" /><p>truman220<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="truman220 has no accepted answers">0%</span></p></div></div><div id="comments-container-8085" class="comments-container"></div><div id="comment-tools-8085" class="comment-tools"></div><div class="clear"></div><div id="comment-8085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8052"></span>

<div id="answer-container-8052" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8052-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I use <a href="http://www.netresec.com/?page=SplitCap">SplitCap</a>. It automatically splits a capture file by "flow" (combination of Source IP/Port and Dest IP/Port)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '11, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/d2186856e30e223d442b2d98640b9d18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdwegner&#39;s gravatar image" /><p>jdwegner<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdwegner has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Dec '11, 15:38</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-8052" class="comments-container"></div><div id="comment-tools-8052" class="comment-tools"></div><div class="clear"></div><div id="comment-8052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8072"></span>

<div id="answer-container-8072" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8072-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I posted <a href="http://www.lovemytool.com/blog/2011/07/using-wiresharks-editcap-to-reduce-your-trace-file-size-by-tony-fortunato.html">a vid showing how to do this with editcap</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '11, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/dbc4d8cb6be85bd586ca4bf211e1337c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thetechfirm&#39;s gravatar image" /><p>thetechfirm<br />
<span class="score" title="64 reputation points">64</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thetechfirm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Dec '11, 14:44</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-8072" class="comments-container"></div><div id="comment-tools-8072" class="comment-tools"></div><div class="clear"></div><div id="comment-8072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8074"></span>

<div id="answer-container-8074" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8074-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>TShark and SplitCap<br />
SplitCap is a great tool, but if you have a large capture file you end up with a lot of output files.<br />
Sample capture file <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=SIP_CALL_RTP_G711">SIP_CALL_RTP_G711</a> (rename the file to SIP_CALL_RTP_G711.pcap).<br />
<br />
TShark<br />
Run this command to get an overview of the tcp and udp conversations:<br />
$ tshark –r SIP_CALL_RTP_G711.pcap –q –z conv,tcp –z conv,udp<br />
<br />
SplitCap<br />
You can use the overview to build your filter for SplitCap. You can filter on ip addresses and/or port numbers to split the file.<br />
<br />
You can use the option –s nosplit to create a single output file.<br />
<br />
Here are some examples:<br />
$ splitcap -r SIP_CALL_RTP_G711.pcap -port 23 -port 110<br />
$ splitcap -r SIP_CALL_RTP_G711.pcap -port 23 -port 110 -s nosplit<br />
$ splitcap -r SIP_CALL_RTP_G711.pcap -ip 200.73.183.213 -port 110 –s nosplit<br />
$ splitcap -r SIP_CALL_RTP_G711.pcap -ip 200.57.7.204 –s nosplit<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '11, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-8074" class="comments-container"></div><div id="comment-tools-8074" class="comment-tools"></div><div class="clear"></div><div id="comment-8074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

