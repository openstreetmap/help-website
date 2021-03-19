+++
type = "question"
title = "Convert PCAP to CSV using tshark puts new lines in the middle of a CSV line"
description = '''Hi, I have a problem in the data within the fields of a PCAP file.  Some values contain &#92;n, when I export the PCAP to CSV it&#x27;s OK. (The info column contains the characters &#92;n when I&#x27;m using tshark to convert multiple PCAPs I have a new line in the data and the CSV is corrupted. Any ideas how I can f...'''
date = "2015-07-01T08:20:00Z"
lastmod = "2015-07-06T15:52:00Z"
weight = 43787
keywords = [ "csv", "tshark" ]
aliases = [ "/questions/43787" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Convert PCAP to CSV using tshark puts new lines in the middle of a CSV line](/questions/43787/convert-pcap-to-csv-using-tshark-puts-new-lines-in-the-middle-of-a-csv-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43787-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a problem in the data within the fields of a PCAP file. Some values contain \n, when I export the PCAP to CSV it's OK. (The info column contains the characters \n when I'm using tshark to convert multiple PCAPs I have a new line in the data and the CSV is corrupted.</p><p>Any ideas how I can fix that? To replace the character manually will be a problem. Does anybody know if the export to CSV functionality uses TSHARK or something else?</p><p>BTW I'm using Windows 8.1 if there's any difference.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">csv tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '15, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/0f47c64b3bde4085a511f07ddbdef820?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="glev&#39;s gravatar image" /><p>glev<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="glev has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Jul '15, 16:32</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-43787" class="comments-container"><span id="43833"></span><div id="comment-43833" class="comment"><div id="post-43833-score" class="comment-score"></div><div class="comment-text"><p>what is your Wireshark version and what are the tshark CLI options?</p></div><div id="comment-43833-info" class="comment-info"><span class="comment-age">(02 Jul '15, 16:41)</span> Kurt Knochner ♦</div></div><span id="43836"></span><div id="comment-43836" class="comment"><div id="post-43836-score" class="comment-score"></div><div class="comment-text"><p>my wireshark version is the most updated and the tshark options are: tshark -T fields -n -r capture.pcap -E separator=, -e ip.src -e ip.dst -e col.info &gt; output.txt</p></div><div id="comment-43836-info" class="comment-info"><span class="comment-age">(02 Jul '15, 23:43)</span> glev</div></div><span id="43841"></span><div id="comment-43841" class="comment"><div id="post-43841-score" class="comment-score"></div><div class="comment-text"><p>We would like to know the exact version, please add a comment with the contents of the Help -&gt; About Wireshark dialog.</p></div><div id="comment-43841-info" class="comment-info"><span class="comment-age">(03 Jul '15, 02:45)</span> grahamb ♦</div></div><span id="43844"></span><div id="comment-43844" class="comment"><div id="post-43844-score" class="comment-score"></div><div class="comment-text"><p>Version 1.12.6 (v1.12.6-0-gee1fce6 from master-1.12)</p><p>the info col is _ws.col.info in the cli command. The problem is that the info contains new lines and I need them to be encoded or replaced by \n string.</p></div><div id="comment-43844-info" class="comment-info"><span class="comment-age">(03 Jul '15, 03:56)</span> glev</div></div><span id="43846"></span><div id="comment-43846" class="comment not_top_scorer"><div id="post-43846-score" class="comment-score"></div><div class="comment-text"><p>Tried to reproduce, but I failed. Could you provide a trace ?</p></div><div id="comment-43846-info" class="comment-info"><span class="comment-age">(03 Jul '15, 04:34)</span> Christian_R</div></div><span id="43847"></span><div id="comment-43847" class="comment not_top_scorer"><div id="post-43847-score" class="comment-score"></div><div class="comment-text"><p>I don't have an error. The command is OK and everything is working, the only problem is that if I have a new line character in the info the result CSV output is with new line and not encoded character and it's corrupted CSV.</p></div><div id="comment-43847-info" class="comment-info"><span class="comment-age">(03 Jul '15, 05:05)</span> glev</div></div><span id="43874"></span><div id="comment-43874" class="comment not_top_scorer"><div id="post-43874-score" class="comment-score"></div><div class="comment-text"><p>The command works OK, the result I'm getting is corrupted CSV file with '\n' which corrupting the file instead of encoded one. This situation occurs when I have \n in the _ws.col.Info data.</p><p>To reproduce you can take any PCAP with \n in the info (HTTP request for example) and convert it with tshark to CSV and the result will be a CSV file with a new line instead of encoded new line.</p><p>For example:</p><p>Correct csv should be:</p><p>"192.168.0.1","Data info with new line\n some more data"</p><p>What you get from tshark: "192.168.0.1","Data info with new line some more data"</p></div><div id="comment-43874-info" class="comment-info"><span class="comment-age">(05 Jul '15, 03:54)</span> glev</div></div><span id="43875"></span><div id="comment-43875" class="comment"><div id="post-43875-score" class="comment-score">1</div><div class="comment-text"><p>What protocol put a newline character in the INFO column?</p></div><div id="comment-43875-info" class="comment-info"><span class="comment-age">(05 Jul '15, 07:43)</span> Hadriel</div></div><span id="43903"></span><div id="comment-43903" class="comment not_top_scorer"><div id="post-43903-score" class="comment-score"></div><div class="comment-text"><p>The protocol is MYSQL</p></div><div id="comment-43903-info" class="comment-info"><span class="comment-age">(06 Jul '15, 13:44)</span> glev</div></div></div><div id="comment-tools-43787" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-43787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43907"></span>

<div id="answer-container-43907" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43907-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's a bug. I submitted bug 11344 for you, at: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11344">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11344</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '15, 15:52</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43907" class="comments-container"><span id="43908"></span><div id="comment-43908" class="comment"><div id="post-43908-score" class="comment-score"></div><div class="comment-text"><p>@glev: any chance you could attach your capture file to that bug? I can make the attachment private afterward if it contains something sensitive. It would be good to have something to test against.</p></div><div id="comment-43908-info" class="comment-info"><span class="comment-age">(06 Jul '15, 15:55)</span> Hadriel</div></div><span id="43942"></span><div id="comment-43942" class="comment"><div id="post-43942-score" class="comment-score"></div><div class="comment-text"><p>Fixed in Wireshark 1.99, back-ported to 1.12, and 1.10. Should be available for you to use/verify right now in the <a href="https://www.wireshark.org/download/automated/">automated builds server</a> in: 1.99.8-324 or higher, and 1.12.7rc0-24 or higher.</p></div><div id="comment-43942-info" class="comment-info"><span class="comment-age">(07 Jul '15, 14:34)</span> Hadriel</div></div></div><div id="comment-tools-43907" class="comment-tools"></div><div class="clear"></div><div id="comment-43907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

