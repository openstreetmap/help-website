+++
type = "question"
title = "getting more info on TCP packets"
description = '''I am trying to analyze Wireshark TCP capture in Excel. I&#x27;d like to have some TCP info like TSval, TSecr, SACK edges in separate columns but it seems that since these values are stored in TCP options rather than in dedicated TCP header fields Wireshark does not create such custom columns. I can see t...'''
date = "2010-11-30T06:31:00Z"
lastmod = "2011-04-10T16:37:00Z"
weight = 1177
keywords = [ "tcp-options", "columns", "tcp" ]
aliases = [ "/questions/1177" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [getting more info on TCP packets](/questions/1177/getting-more-info-on-tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1177-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to analyze Wireshark TCP capture in Excel. I'd like to have some TCP info like TSval, TSecr, SACK edges in separate columns but it seems that since these values are stored in TCP options rather than in dedicated TCP header fields Wireshark does not create such custom columns.</p><p>I can see these values in the info column but they are shown only for client ACK packets. For server packets the info columns always shows [TCP segment of a reassembled PDU] and I need to see them in both direction. Any ideas how these values can be listed for every packet?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">tcp-options columns tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '10, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/234f359fd915ac46d92b477dc55a13fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jackhab&#39;s gravatar image" /><p>jackhab<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jackhab has no accepted answers">0%</span></p></div></div><div id="comments-container-1177" class="comments-container"></div><div id="comment-tools-1177" class="comment-tools"></div><div class="clear"></div><div id="comment-1177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="1179"></span>

<div id="answer-container-1179" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1179-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use custom columns with the following fields:</p><ul><li>tcp.options.timestamp.tsval</li><li>tcp.options.timestamp.tsecr</li><li>tcp.options.sack_le</li><li>tcp.options.sack_re</li></ul><p>Or use tshark like this:</p><pre><code>tshark -r &lt;file&gt; -R tcp -T fields \
     -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport \
     -e tcp.options.timestamp.tsval -e tcp.options.timestamp.tsecr \
     -e tcp.options.sack_le -e tcp.options.sack_re</code></pre><p>Hope this helps!</p><p>(See also: <a href="http://www.wireshark.org/docs/dfref/t/tcp.html">http://www.wireshark.org/docs/dfref/t/tcp.html</a>)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '10, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Nov '10, 07:26</p></div></div><div id="comments-container-1179" class="comments-container"><span id="2190"></span><div id="comment-2190" class="comment"><div id="post-2190-score" class="comment-score"></div><div class="comment-text"><p>I could not find tcp.options.timestamp.tsval and tcp.options.timestamp.tsecr neither in custom columns options nor in the documentation under the provided link.</p></div><div id="comment-2190-info" class="comment-info"><span class="comment-age">(07 Feb '11, 06:40)</span> jackhab</div></div><span id="2191"></span><div id="comment-2191" class="comment"><div id="post-2191-score" class="comment-score"></div><div class="comment-text"><p>Which version of wireshark are you using? I think they were added in 1.4.0, but it could also be that they are only available in the 1.5.0 development release.</p></div><div id="comment-2191-info" class="comment-info"><span class="comment-age">(07 Feb '11, 07:31)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-1179" class="comment-tools"></div><div class="clear"></div><div id="comment-1179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2269"></span>

<div id="answer-container-2269" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2269-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>For analyzing TCP SACK Edges i used a simple trick which - although not perfectly effective - did the job in pulling out the desired info:</p><p>Use Export -&gt; .csv to throw trace file data into excel readable .csv and import that Data into Excel. Then you have trace file date including coloumns as specified in wireshark.</p><p>The trick for pulling out SACK info for me was to use the "text to coloumns" button in Excel, which normally seperates comma-seperated stuff from inside one coloumn into many.</p><p>I marked the "Info" coloumn in Excel and replaced "SRE" to "$RE" and "SLE" to "$SLE". After that you can use "text to coloumns" and give it a user-defined seperator "$", which will perfectly pull out those Info lines containing SACK related edges and place it into new coloums to the right, each still labeled with it's RE or LE after stripping "$"</p><p>Hope that helps</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '11, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-2269" class="comments-container"></div><div id="comment-tools-2269" class="comment-tools"></div><div class="clear"></div><div id="comment-2269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3431"></span>

<div id="answer-container-3431" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3431-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Dogan lol stop scamming people's account on the cafe by using wireshark</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '11, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/10384556eba509bd0867e78e9dd47fdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alvnfer&#39;s gravatar image" /><p>alvnfer<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alvnfer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '11, 16:38</p></div></div><div id="comments-container-3431" class="comments-container"></div><div id="comment-tools-3431" class="comment-tools"></div><div class="clear"></div><div id="comment-3431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3345"></span>

<div id="answer-container-3345" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3345-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, im usong wireshark to pinpoint a ragnarok servers ports and ip, when i enter for filter eth contains "username" it doesnt show up, i am following this guide btw. http://wiki.openkore.com/index.php/Connectivity_Guide thank you. ps: windows 7</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '11, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/52f79ea7ab8dbe8b4d860d6566496eec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Do%C4%9Fan%20Erdo%C4%9Fan&#39;s gravatar image" /><p>Doğan Erdoğan<br />
<span class="score" title="0 reputation points">0</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Doğan Erdoğan has no accepted answers">0%</span></p></div></div><div id="comments-container-3345" class="comments-container"></div><div id="comment-tools-3345" class="comment-tools"></div><div class="clear"></div><div id="comment-3345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

