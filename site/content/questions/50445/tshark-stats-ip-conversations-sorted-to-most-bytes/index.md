+++
type = "question"
title = "Tshark Stats - IP conversations sorted to most bytes?"
description = '''Right now I am using: tshark -r &quot;C:&#92;Users&#92;admin&#92;Desktop&#92;capture.cap&quot; -qz &quot;conv,ip&quot; This displays host IP conversations with hosts that have the most frames topping the results. Seems typically the hosts with the most frames usually have the most bytes in their conversations, but not always. Is there...'''
date = "2016-02-23T10:24:00Z"
lastmod = "2017-07-14T15:09:00Z"
weight = 50445
keywords = [ "ip", "statistics", "bytes", "tshark", "conversations" ]
aliases = [ "/questions/50445" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark Stats - IP conversations sorted to most bytes?](/questions/50445/tshark-stats-ip-conversations-sorted-to-most-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50445-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Right now I am using: tshark -r "C:\Users\admin\Desktop\capture.cap" -qz "conv,ip"</p><p>This displays host IP conversations with hosts that have the most frames topping the results. Seems typically the hosts with the most frames usually have the most bytes in their conversations, but not always. Is there anyway to make the hosts with the most bytes in these conversations appear at the top, then descending in value by byte count?</p></div><div id="question-tags" class="tags-container tags">ip statistics bytes tshark conversations</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '16, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/7c34b5795df1aaa486754544342bfc1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zer0day&#39;s gravatar image" /><p>zer0day<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zer0day has 3 accepted answers">60%</span></p></div></div><div id="comments-container-50445" class="comments-container"></div><div id="comment-tools-50445" class="comment-tools"></div><div class="clear"></div><div id="comment-50445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50520"></span>

<div id="answer-container-50520" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50520-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=ui/cli/tap-iousers.c">source</a>, no, the sorting is hard-coded to be by the number of frames.</p><p>You could raise an <a href="https://bugs.wireshark.org">enhancement request</a> to request the functionality.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '16, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-50520" class="comments-container"><span id="50564"></span><div id="comment-50564" class="comment"><div id="post-50564-score" class="comment-score"></div><div class="comment-text"><p>Thanks for taking the time to look, much appreciated.</p></div><div id="comment-50564-info" class="comment-info"><span class="comment-age">(27 Feb '16, 17:47)</span> zer0day</div></div></div><div id="comment-tools-50520" class="comment-tools"></div><div class="clear"></div><div id="comment-50520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62790"></span>

<div id="answer-container-62790" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62790-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>Try this:</strong></p><pre><code>for aa in `ls *.pcap`; do
    echo -------------
    echo ==== $aa ====
    echo &quot;                                               |       &lt;-      | |       -&gt;      | |     Total     |    Relative    |   Duration   |&quot;
    echo &quot;                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |      Start     |              |&quot;
    tshark -r $aa -q -z conv,ip | grep -v -E &quot;====|Conversations|Filter|Total|Frames&quot; | sort -nr -k 9 | head
done</code></pre><p><strong>or just</strong></p><pre><code>tshark -r file.pcap -q -z conv,ip | grep -v -E &quot;====|Conversations|Filter|Total|Frames&quot; | sort -nr -k 9 | head</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '17, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/8485ef958bc86bbc683ebf200b5e0fcc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gag99&#39;s gravatar image" /><p>gag99<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gag99 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jul '17, 05:30</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-62790" class="comments-container"><span id="62800"></span><div id="comment-62800" class="comment"><div id="post-62800-score" class="comment-score"></div><div class="comment-text"><p>The above script appears to be bash based along with several common *nix utilities and as such, won't work for the OP who appears to be running Windows.</p><p>The OP could install a *nix compatibility tool such as Cygwin or mingw (as provided by Git for Windows) to run the scripts or convert them to something that works out of the box, e.g. PowerShell.</p></div><div id="comment-62800-info" class="comment-info"><span class="comment-age">(15 Jul '17, 07:20)</span> grahamb ♦</div></div></div><div id="comment-tools-62790" class="comment-tools"></div><div class="clear"></div><div id="comment-62790-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

