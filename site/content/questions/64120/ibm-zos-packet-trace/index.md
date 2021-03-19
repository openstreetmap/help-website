+++
type = "question"
title = "IBM z/OS packet trace"
description = '''I work with a TCP/IP monitoring tool that runs on IBM z/OS mainframes. My product can capture packets created by a TCP/IP stack that also runs under z/OS. IPCS can convert such a file to a format compatible with Wireshark. We would like to avoids using IPCS and do the conversion within our product. ...'''
date = "2017-10-23T11:39:00Z"
lastmod = "2017-10-24T11:32:00Z"
weight = 64120
keywords = [ "zos", "ibm" ]
aliases = [ "/questions/64120" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [IBM z/OS packet trace](/questions/64120/ibm-zos-packet-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64120-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I work with a TCP/IP monitoring tool that runs on IBM z/OS mainframes. My product can capture packets created by a TCP/IP stack that also runs under z/OS. IPCS can convert such a file to a format compatible with Wireshark. We would like to avoids using IPCS and do the conversion within our product. Is there code available that we can imbed into our monitor that will do the file conversion?</p></div><div id="question-tags" class="tags-container tags">zos ibm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '17, 11:39</strong></p><img src="https://secure.gravatar.com/avatar/5bb586d88aa7b283ab7987dc856b8b13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daverme&#39;s gravatar image" /><p>daverme<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daverme has no accepted answers">0%</span></p></div></div><div id="comments-container-64120" class="comments-container"></div><div id="comment-tools-64120" class="comment-tools"></div><div class="clear"></div><div id="comment-64120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="64122"></span>

<div id="answer-container-64122" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64122-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is <a href="https://pcapng.github.io/pcapng/">this</a> sufficient information to allow you to directly store the captured data in Wireshark-compatible format, rather than doing a conversion?</p><p>Any code you ask for would only cover the "store as pcapng" part but you would have to provide the "receive data from the capturing engine" part, which to me is roughly the same amount of work as to generate the file format directly.</p><p>Just to tell the full story, in addition to the advantages of pcap-ng over pcap, there is also a certain drawback of use of pcap-ng format - as of now, Wireshark still <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11370">cannot read it from a pipe</a>, but I guess this should not be of any importance for your use case (and I also hope it is not going to last forever).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '17, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-64122" class="comments-container"><span id="64147"></span><div id="comment-64147" class="comment"><div id="post-64147-score" class="comment-score"></div><div class="comment-text"><p>Great answer. Thanks for the feedback.</p></div><div id="comment-64147-info" class="comment-info"><span class="comment-age">(24 Oct '17, 04:43)</span> daverme</div></div></div><div id="comment-tools-64122" class="comment-tools"></div><div class="clear"></div><div id="comment-64122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="64161"></span>

<div id="answer-container-64161" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64161-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could also contribute code to Wireshark that allows it to read files in your format - assuming "your format" can be represented as a stream of bytes.</p><p>That means that if it's a bunch of count+data records in some z/OS access method, you'd have to represent it, to make it readable by UN*X and Windows systems, whose file systems store files as seekable byte dreams, as a sequence of records with N bytes of count followed by the bytes of data in the record.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '17, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-64161" class="comments-container"></div><div id="comment-tools-64161" class="comment-tools"></div><div class="clear"></div><div id="comment-64161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

