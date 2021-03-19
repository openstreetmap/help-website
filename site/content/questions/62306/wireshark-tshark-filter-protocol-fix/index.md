+++
type = "question"
title = "Wireshark Tshark filter protocol FIX"
description = '''Can someone help me? I can not save file. C:&#92;Program Files&#92;Wireshark&amp;gt;Tshark -i rpcap://[172.16.254.6]/&#92;Device&#92;NPF_{CF9CFF4 6-79FF-4A97-802A-F6CEF5896D29} -Y fix -w C:&#92;ts.pcap tshark: Display filters aren&#x27;t supported when capturing and saving the captured packets. '''
date = "2017-06-26T11:37:00Z"
lastmod = "2017-06-26T11:40:00Z"
weight = 62306
keywords = [ "fix", "wireshark" ]
aliases = [ "/questions/62306" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Tshark filter protocol FIX](/questions/62306/wireshark-tshark-filter-protocol-fix)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62306-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone help me? I can not save file.</p><pre><code>C:\Program Files\Wireshark&gt;Tshark -i rpcap://[172.16.254.6]/\Device\NPF_{CF9CFF4
6-79FF-4A97-802A-F6CEF5896D29} -Y fix -w C:\ts.pcap
tshark: Display filters aren&#39;t supported when capturing and saving the captured
packets.</code></pre></div><div id="question-tags" class="tags-container tags">fix wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '17, 11:37</strong></p><img src="https://secure.gravatar.com/avatar/a95becaa9162bc901663cdd569efda99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JorgeMiguelr210&#39;s gravatar image" /><p>JorgeMiguelr210<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JorgeMiguelr210 has no accepted answers">0%</span></p></div></div><div id="comments-container-62306" class="comments-container"></div><div id="comment-tools-62306" class="comment-tools"></div><div class="clear"></div><div id="comment-62306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62307"></span>

<div id="answer-container-62307" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62307-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to use "-f" instead of "-Y", because during capture you can only use capture filters (in BPF syntax). Which probably means that you cannot filter on "fix" that way, because that is a display filter...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '17, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-62307" class="comments-container"><span id="62308"></span><div id="comment-62308" class="comment"><div id="post-62308-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your help. I did some testing here I can filter as icmp. I wanted to filter only the fix messages</p><p><code> C:\Program Files\Wireshark&gt;Tshark -i rpcap://[172.16.254.6]/\Device\NPF_{CF9CFF46-79FF-4A97-802A-F6CEF5896D29} -f fix Capturing on 'rpcap://[172.16.254.6]/\Device\NPF_{CF9CFF46-79FF-4A97-802A-F6CEF5 896D29}' tshark: Invalid capture filter "fix" for interface 'rpcap://[172.16.254.6]/\Device\NPF_{CF9CFF46-79FF-4A97-802A-F6CEF5896D29}'.</code></p><p><code></code></p><p><code>That string looks like a valid display filter; however, it isn't a valid capture filter (syntax error).</code></p></div><div id="comment-62308-info" class="comment-info"><span class="comment-age">(26 Jun '17, 11:50)</span> JorgeMiguelr210</div></div><span id="62309"></span><div id="comment-62309" class="comment"><div id="post-62309-score" class="comment-score">1</div><div class="comment-text"><p>As I indicated in <a href="https://stackoverflow.com/questions/44763546/tshark-filter-protocol-fix">my answer</a> to your question over at Stack Overflow, you can <em>probably</em> use a capture filter of <code>-f "tcp[20:4]=0x383D4649 and tcp[24:1]=0x58"</code>. That filter was supplied by Kurt Knochner in his answer to <a href="https://ask.wireshark.org/questions/29829/fix-protocol-capturing">this</a> question.</p></div><div id="comment-62309-info" class="comment-info"><span class="comment-age">(26 Jun '17, 12:00)</span> cmaynard ♦♦</div></div><span id="62377"></span><div id="comment-62377" class="comment"><div id="post-62377-score" class="comment-score"></div><div class="comment-text"><p>This question is about filter FIX traffic. If you have another question, don't keep adding more comments or "answers" to this one. I have deleted all content unrelated to filtering of FIX traffic.</p><p>Also, if an answer has resolved your question, then you should mark it as accepted. Please read the FAQ.</p></div><div id="comment-62377-info" class="comment-info"><span class="comment-age">(28 Jun '17, 11:45)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-62307" class="comment-tools"></div><div class="clear"></div><div id="comment-62307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

