+++
type = "question"
title = "tshark change/choose outfile name"
description = '''Hi,  I was wondering if it&#x27;s possible to chose the name of the output file of tshark.  tshark automatically adds the timestamp to the name I give (e.g. &quot;file&quot;), but I would like to get rid of that and instead have just a number, like &quot;file1&quot;, &quot;file2&quot;, &quot;file3&quot;, ... Is that possible? Thanks!'''
date = "2015-07-13T02:34:00Z"
lastmod = "2015-07-15T13:00:00Z"
weight = 44085
keywords = [ "outfile", "tshark", "name" ]
aliases = [ "/questions/44085" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark change/choose outfile name](/questions/44085/tshark-changechoose-outfile-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44085-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I was wondering if it's possible to chose the name of the output file of tshark. tshark automatically adds the timestamp to the name I give (e.g. "file"), but I would like to get rid of that and instead have just a number, like "file1", "file2", "file3", ... Is that possible? Thanks!</p></div><div id="question-tags" class="tags-container tags">outfile tshark name</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '15, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/8a56219cf3e2541560a4721d37353cc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pat_celine&#39;s gravatar image" /><p>pat_celine<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pat_celine has no accepted answers">0%</span></p></div></div><div id="comments-container-44085" class="comments-container"><span id="44123"></span><div id="comment-44123" class="comment"><div id="post-44123-score" class="comment-score"></div><div class="comment-text"><p>Can you provide the command? Default behavior of tshark output file names is not something like you said. Maybe you are using some extra options.</p></div><div id="comment-44123-info" class="comment-info"><span class="comment-age">(14 Jul '15, 01:14)</span> xmikro</div></div><span id="44124"></span><div id="comment-44124" class="comment"><div id="post-44124-score" class="comment-score"></div><div class="comment-text"><p>Hi! Something like tshark -i 2 -a files:10 -b duration:300 -w "analysis\file.pcap" This outputs file_00001_20150714102556 as the first file (the last part is the timestamp). I'd like to get just file_0001, for example Thanks!</p></div><div id="comment-44124-info" class="comment-info"><span class="comment-age">(14 Jul '15, 01:27)</span> pat_celine</div></div></div><div id="comment-tools-44085" class="comment-tools"></div><div class="clear"></div><div id="comment-44085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44187"></span>

<div id="answer-container-44187" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44187-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is currently not possible to override the formatting of the file name. Either you have a static filename or you enable the "ringbuffer" mode. The exact (simple) format is defined <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=ringbuffer.c;h=4873c34c4824054fdb096e545592822f013c4e18;hb=HEAD#l112">source code of ringbuffer.c</a>.</p><p>If you need a customizable output filename, please open a feature request at <a href="https://bugzilla.wireshark.org/.">https://bugzilla.wireshark.org/.</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '15, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-44187" class="comments-container"></div><div id="comment-tools-44187" class="comment-tools"></div><div class="clear"></div><div id="comment-44187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

