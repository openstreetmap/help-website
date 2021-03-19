+++
type = "question"
title = "WS crashes when capturing to multiple files"
description = '''Hi, I have latest version 2.2.4) installed on 2 Windows servers 2008 R2 Enterprice SP1 64bit OS with 48GB RAM 2 CPUs @ 2.8GHz; and encounter following issue: when I capture traffic and send the output to multiple files, WS crashes after the first file, sometimes the 2nd file contains some data, but ...'''
date = "2017-02-28T08:27:00Z"
lastmod = "2017-03-01T07:58:00Z"
weight = 59732
keywords = [ "wireshark_crashed" ]
aliases = [ "/questions/59732" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WS crashes when capturing to multiple files](/questions/59732/ws-crashes-when-capturing-to-multiple-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59732-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have latest version 2.2.4) installed on 2 Windows servers 2008 R2 Enterprice SP1 64bit OS with 48GB RAM 2 CPUs @ 2.8GHz; and encounter following issue: when I capture traffic and send the output to multiple files, WS crashes after the first file, sometimes the 2nd file contains some data, but usually it is empty. conditions were: - capturing on 2 interfaces - with any capture filter on both i/f - output to files of 300MB, no ring buffer - Auto-Stop capture after a couple of files - no update list of packets in real-time</p><p>I have encountered this issue for many versions unfortunately, but this version is really doing very bad on this :-( Is there something that I need to take into consideration, e.g. limiting the size of the files (but tried with 100MB files gives same issue), ... ? Pls advise. Thx.</p></div><div id="question-tags" class="tags-container tags">wireshark_crashed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '17, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/4fc43c83d14e6cb53bf36dd8013dbcf1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="profke&#39;s gravatar image" /><p>profke<br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="profke has no accepted answers">0%</span></p></div></div><div id="comments-container-59732" class="comments-container"><span id="59736"></span><div id="comment-59736" class="comment"><div id="post-59736-score" class="comment-score"></div><div class="comment-text"><p>What rate of traffic are you attempting to capture on the 2 interfaces?</p><p>Are you using the 64 bit version of Wireshark?</p><p>Have you tried using tshark, or if there are no capture filters, dumpcap to perform the captures?</p></div><div id="comment-59736-info" class="comment-info"><span class="comment-age">(28 Feb '17, 09:12)</span> grahamb ♦</div></div><span id="59762"></span><div id="comment-59762" class="comment"><div id="post-59762-score" class="comment-score"></div><div class="comment-text"><p>The rate of traffic measured on the SPAN port of the switch is about 325Mb/s for the first link to the sniffer,↔︎the other one only carries about 73kb/s. In WS in the capture file stats I see the rate averages around 900 kb/s (so with a capture filter applied)</p><p>Yes, I'm using the 64bit version of WS</p><p>No, haven't tried with tshark, as I have not the habit nor knowledge to do so.</p><p>WS also crashed when I hit the stop button while a capture to a file is ongoing; fortunately the file contains data.</p><p>thx for any advise. BR.</p></div><div id="comment-59762-info" class="comment-info"><span class="comment-age">(01 Mar '17, 06:30)</span> profke</div></div></div><div id="comment-tools-59732" class="comment-tools"></div><div class="clear"></div><div id="comment-59732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59763"></span>

<div id="answer-container-59763" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59763-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would try dumpcap first, as that application performs capture using only BPF capture filters. Wireshark (and tshark) both dissect the traffic as well as capture it which puts the system under extra load at high traffic rates.</p><p>The man page for dumpcap is <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">here</a>. It's a command line program so has to be run from a shell, e.g. cmd.exe or PowerShell and you'll need to provide the full path to the application, e.g. <code>"C:\Program Files\Wireshark\dumpcap.exe ...</code>.</p><p>The <code>-b</code> option controls capturing to multiple files.</p><p>Using Google found <a href="https://www.cellstream.com/intranet/reference-reading/tipsandtricks/283-how-to-use-dumpcap-natively-on-your-computer.html">this</a> guide on dumpcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '17, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59763" class="comments-container"><span id="59827"></span><div id="comment-59827" class="comment"><div id="post-59827-score" class="comment-score"></div><div class="comment-text"><p>I haven't tried with dumpcap yet, but meanwhile I discovered that when capturing to files and leaving the "Update list of packets in real time" checked, WS doesn't crash until it comes to the saving of the last file. So this is workable for me as I have long-term capturing with all files stored. Will try with dumpcap later on. Thanks.</p></div><div id="comment-59827-info" class="comment-info"><span class="comment-age">(03 Mar '17, 05:48)</span> profke</div></div></div><div id="comment-tools-59763" class="comment-tools"></div><div class="clear"></div><div id="comment-59763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

