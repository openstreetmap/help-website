+++
type = "question"
title = "long period capture"
description = '''Hello I use wireshark to register data exchanged on a network (UDP data). I would like to capture data during a long period (3hours, knowing that a 5minutes capture gives a 800Mo of registered data). Problem is that wireshark does not manage to treat such a size of data: is there a PC or wireshark u...'''
date = "2010-11-24T08:02:00Z"
lastmod = "2010-11-24T09:24:00Z"
weight = 1107
keywords = [ "capture", "period", "long" ]
aliases = [ "/questions/1107" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [long period capture](/questions/1107/long-period-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1107-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I use wireshark to register data exchanged on a network (UDP data). I would like to capture data during a long period (3hours, knowing that a 5minutes capture gives a 800Mo of registered data). Problem is that wireshark does not manage to treat such a size of data: is there a PC or wireshark upgrade that could solve problem ? what do you suggest ?</p><p>Thx</p><p>Note that i am not a network expert...</p></div><div id="question-tags" class="tags-container tags">capture period long</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '10, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/ffcddc96c34c11ff4805675640090a5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bruno_47&#39;s gravatar image" /><p>Bruno_47<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bruno_47 has no accepted answers">0%</span></p></div></div><div id="comments-container-1107" class="comments-container"></div><div id="comment-tools-1107" class="comment-tools"></div><div class="clear"></div><div id="comment-1107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1109"></span>

<div id="answer-container-1109" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1109-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use dumpcap (which is part of the wireshark) to do that. You can use the following command:</p><pre><code>dumpcap -i &lt;interface&gt; -w &lt;file.pcap&gt; -f &lt;filter&gt; -a filesize:65536 -a files:512</code></pre><p>This will create 512 files of 64MB and then stop, resulting in a fileset of 32GB (3hrs/5min * 800MB = +/- 29GB)</p><p>You could also create a ringbuffer of files to capture the data until a problem occurs and then stop the collection. This can be done by:</p><pre><code>dumpcap -i &lt;interface&gt; -w &lt;file.pcap&gt; -f &lt;filter&gt; -b filesize:65536 -b files:512</code></pre><p>This way after 512 files have been written, the first one will be deleted and a 513th one will be created etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '10, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1109" class="comments-container"><span id="1151"></span><div id="comment-1151" class="comment"><div id="post-1151-score" class="comment-score"></div><div class="comment-text"><p>Thanks for this idea !</p></div><div id="comment-1151-info" class="comment-info"><span class="comment-age">(29 Nov '10, 04:52)</span> Bruno_47</div></div><span id="1152"></span><div id="comment-1152" class="comment"><div id="post-1152-score" class="comment-score"></div><div class="comment-text"><p>Bruno, I converted your "answer" into a "comment" to adhere to the Q&amp;A style of this website.</p></div><div id="comment-1152-info" class="comment-info"><span class="comment-age">(29 Nov '10, 04:57)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-1109" class="comment-tools"></div><div class="clear"></div><div id="comment-1109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

