+++
type = "question"
title = "rawshark example"
description = '''I am looking for a good documentation on rawshark with good examples(other than the man page). I tried using the rawshark man page but I can not find any practical examples embedded in the man page. '''
date = "2010-12-27T08:25:00Z"
lastmod = "2011-01-04T01:50:00Z"
weight = 1489
keywords = [ "rawshark" ]
aliases = [ "/questions/1489" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [rawshark example](/questions/1489/rawshark-example)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1489-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking for a good documentation on rawshark with good examples(other than the man page). I tried using the rawshark man page but I can not find any practical examples embedded in the man page.</p></div><div id="question-tags" class="tags-container tags">rawshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '10, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/64f007f3459dbfd425cd4f57393b2295?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="averageguy&#39;s gravatar image" /><p>averageguy<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="averageguy has no accepted answers">0%</span></p></div></div><div id="comments-container-1489" class="comments-container"></div><div id="comment-tools-1489" class="comment-tools"></div><div class="clear"></div><div id="comment-1489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1615"></span>

<div id="answer-container-1615" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1615-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I've been circling around this rawshark for a day now, and here's my two cents :</p><p><em>sudo dumpcap -w- -i eth2 -f "tcp port 80" | rawshark -d encap:EN10MB -l -r- -s -F ip.dst -F http.host</em></p><p>explanation : dumpcap provides the input (tcp port 80 from eth2). -w- means writing to stdout, rawshark : -d encap:EN10MB means we read ethernet packets (most likely you too. you can find out by readin dumpcap messages) -l means to flush the output -r- means read from stdin -s means skip the pcap headers (this is what took me most time to figure ) -F ... lists the fields we want to parse</p><p>hope someone finds this useful</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '11, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/7eff7b23646c5be465e00815aabcf9b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yoav&#39;s gravatar image" /><p>yoav<br />
<span class="score" title="86 reputation points">86</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yoav has no accepted answers">0%</span></p></div></div><div id="comments-container-1615" class="comments-container"></div><div id="comment-tools-1615" class="comment-tools"></div><div class="clear"></div><div id="comment-1615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

