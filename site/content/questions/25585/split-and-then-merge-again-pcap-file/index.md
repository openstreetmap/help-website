+++
type = "question"
title = "Split and then merge again pcap file"
description = '''Hi all, I split a pcap in 3 small pcap files and then I merged back altogether. I was supposing that the merged one is equal to initial file, but I found many differences. Could someone explain to me why? Thanks editcap test_initial.pcap test_A.pcap 1-300 tshark -nr test_initial.pcap -R &quot;frame.numbe...'''
date = "2013-10-03T06:17:00Z"
lastmod = "2013-10-03T07:22:00Z"
weight = 25585
keywords = [ "editcap", "mergecap" ]
aliases = [ "/questions/25585" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Split and then merge again pcap file](/questions/25585/split-and-then-merge-again-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25585-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I split a pcap in 3 small pcap files and then I merged back altogether. I was supposing that the merged one is equal to initial file, but I found many differences. Could someone explain to me why?</p><p>Thanks</p><pre><code>editcap test_initial.pcap test_A.pcap 1-300
tshark -nr test_initial.pcap -R &quot;frame.number==301&quot; -w test_B.pcap
editcap test_initial.pcap test_C.pcap 302-999999999

mergecap -w test_merged.pcap \
            test_A.pcap \
            test_B.pcap \
            test_C.pcap 

tshark -nr test_initial.pcap -T pdml &gt; test_initial.xml
tshark -nr test_merged.pcap -T pdml &gt; test_merged.xml
diff test_initial.xml test_merged.xml</code></pre></div><div id="question-tags" class="tags-container tags">editcap mergecap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '13, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/a5626909eb9fd5bbf9e3ac3861076738?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ric79&#39;s gravatar image" /><p>Ric79<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ric79 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Oct '13, 06:18</p></div></div><div id="comments-container-25585" class="comments-container"><span id="25586"></span><div id="comment-25586" class="comment"><div id="post-25586-score" class="comment-score"></div><div class="comment-text"><p>Can you post the initial pcap anywhere folks could have a look? What's the capinfos report on the initial and merged pcaps?</p></div><div id="comment-25586-info" class="comment-info"><span class="comment-age">(03 Oct '13, 06:23)</span> grahamb ♦</div></div><span id="25618"></span><div id="comment-25618" class="comment"><div id="post-25618-score" class="comment-score"></div><div class="comment-text"><p>@grahamb You can use a generic test_initial.pcap file...</p></div><div id="comment-25618-info" class="comment-info"><span class="comment-age">(03 Oct '13, 23:17)</span> Ric79</div></div></div><div id="comment-tools-25585" class="comment-tools"></div><div class="clear"></div><div id="comment-25585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25588"></span>

<div id="answer-container-25588" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25588-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>editcap will not save the listed packets by default. You need to use the "-r" flag to save frames 1-300 to a new file like this:</p><pre><code>editcap -r test_initial.pcap test_A.pcap 1-300</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '13, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25588" class="comments-container"><span id="25620"></span><div id="comment-25620" class="comment"><div id="post-25620-score" class="comment-score"></div><div class="comment-text"><p>Thanks.. after adding a "-r" flag to editcap, the process works nicely! Is there a way to use editcap also for extracting just ONE frame?</p></div><div id="comment-25620-info" class="comment-info"><span class="comment-age">(03 Oct '13, 23:19)</span> Ric79</div></div><span id="25621"></span><div id="comment-25621" class="comment"><div id="post-25621-score" class="comment-score">1</div><div class="comment-text"><p>Maybe try "editcap -r test_initial.pcap test.pcap 1-1"? :-)</p></div><div id="comment-25621-info" class="comment-info"><span class="comment-age">(03 Oct '13, 23:24)</span> Jasper ♦♦</div></div><span id="25622"></span><div id="comment-25622" class="comment"><div id="post-25622-score" class="comment-score"></div><div class="comment-text"><p>Or just use "1":</p><pre><code>$ editcap -r http.cap /tmp/x.pcap 1
Add_Selected: 1
Not inclusive ... 1
$ capinfos -Tc /tmp/x.pcap 
File name   Number of packets
/tmp/x.pcap 1

$</code></pre></div><div id="comment-25622-info" class="comment-info"><span class="comment-age">(04 Oct '13, 00:14)</span> SYN-bit ♦♦</div></div><span id="25627"></span><div id="comment-25627" class="comment"><div id="post-25627-score" class="comment-score"></div><div class="comment-text"><p>@Jasper ... your solution is nice also for n-th frame, not just for the first one</p><pre><code>editcap -r test_initial.pcap test_B.pcap 301-301</code></pre></div><div id="comment-25627-info" class="comment-info"><span class="comment-age">(04 Oct '13, 01:58)</span> Ric79</div></div></div><div id="comment-tools-25588" class="comment-tools"></div><div class="clear"></div><div id="comment-25588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

