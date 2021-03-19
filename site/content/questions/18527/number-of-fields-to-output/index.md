+++
type = "question"
title = "Number of fields to output"
description = '''Hi, I&#x27;m using TSHARK with the -T fields option and it worked great until I had a few more fields to output. If I delete a few of the fields ( NO matter which ones) it works. Is there a number of maximum (12) fields that wireshark can output at once? If so how can I change that?'''
date = "2013-02-11T22:32:00Z"
lastmod = "2013-02-12T02:36:00Z"
weight = 18527
keywords = [ "fields", "tshark", "maximum" ]
aliases = [ "/questions/18527" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Number of fields to output](/questions/18527/number-of-fields-to-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18527-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm using TSHARK with the -T fields option and it worked great until I had a few more fields to output.</p><p>If I delete a few of the fields ( NO matter which ones) it works.</p><p>Is there a number of maximum (12) fields that wireshark can output at once?</p><p>If so how can I change that?</p></div><div id="question-tags" class="tags-container tags">fields tshark maximum</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '13, 22:32</strong></p><img src="https://secure.gravatar.com/avatar/ec94123bfb15406bab7362dbcdc35f9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WiresharkUser332&#39;s gravatar image" /><p>WiresharkUse...<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WiresharkUser332 has no accepted answers">0%</span></p></div></div><div id="comments-container-18527" class="comments-container"></div><div id="comment-tools-18527" class="comment-tools"></div><div class="clear"></div><div id="comment-18527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18534"></span>

<div id="answer-container-18534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18534-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I know there is no limit in the number of fields. <strong>However</strong> there may be a limit of the command line length of your shell (rather large for Linux, <a href="http://support.microsoft.com/kb/830473">much shorter for Windows</a>).</p><ul><li>What is you OS?</li><li>Can you post the tshark command that does <strong>not</strong> work?</li><li>Are there any error messages?</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '13, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Feb '13, 02:37</p></div></div><div id="comments-container-18534" class="comments-container"><span id="18536"></span><div id="comment-18536" class="comment"><div id="post-18536-score" class="comment-score"></div><div class="comment-text"><p>I'm using windows.</p><p>The tshark command is just "tshark.exe -r file path -T fields -e ip.src -e ip.dst ...."</p><p>I'm not getting any errors but in when I'm looking at the output, the fields after the 12th field just don't exists. All the fields are ok beacuse if I'm deleting the first fields it works great...</p></div><div id="comment-18536-info" class="comment-info"><span class="comment-age">(12 Feb '13, 03:07)</span> WiresharkUse...</div></div><span id="18540"></span><div id="comment-18540" class="comment"><div id="post-18540-score" class="comment-score"></div><div class="comment-text"><p>O.K. can you please add ALL fields, so I can test myself?</p><p>BTW: What is your tshark version (tshark -v)?</p><p>The following command (16 fields) works for me on Windows (tshark 1.8.4):</p><blockquote><p><code>tshark -nr input.pcap -T fields -e frame.number -e frame.time -e frame.len -e eth.type -e eth.src -e eth.dst -e ip.version -e ip.hdr_len -e ip.dsfield -e ip.len -e ip.id -e ip.flags -e ip.dst -e ip.src -e ip.proto -e ip.ttl</code></p></blockquote><p>Does that work on your system as well? If so, it's probably related to the fields you are using (please post your tshark command with <strong>all</strong> parameters).</p></div><div id="comment-18540-info" class="comment-info"><span class="comment-age">(12 Feb '13, 04:00)</span> Kurt Knochner ♦</div></div><span id="18556"></span><div id="comment-18556" class="comment"><div id="post-18556-score" class="comment-score"></div><div class="comment-text"><p>I was wrong the magic number is 15 not 12, the 16th field don't work.</p><p>I'm using version 1.8.1</p></div><div id="comment-18556-info" class="comment-info"><span class="comment-age">(12 Feb '13, 09:41)</span> WiresharkUse...</div></div><span id="18560"></span><div id="comment-18560" class="comment"><div id="post-18560-score" class="comment-score"></div><div class="comment-text"><p>Some questions you did <strong>not</strong> yet answer. If you don't answer these questions, it's almost impossible to help you.</p><ul><li>does my command (16 fields) work on your system? If no: Can you please post the output of the <strong>following</strong> command?</li></ul><blockquote><p><code>tshark -nr input.pcap -T fields -e frame.number -e frame.time -e frame.len -e eth.type -e eth.src -e eth.dst -e ip.version -e ip.hdr_len -e ip.dsfield -e ip.len -e ip.id -e ip.flags -e ip.dst -e ip.src -e ip.proto -e ip.ttl -E header=y</code><br />
</p></blockquote><ul><li>what is the <strong>full output</strong> of <strong>tshark -v</strong></li><li>can you please post <strong>your</strong> command with <strong>all</strong> options</li></ul><p>Some new questions:</p><ul><li>how do you start tshark? From a DOS windows (if so, is it the standard command interpreter cmd.exe?)? From Java or any other programming language?</li><li>can you please upgrade to the latest 1.8. release. Maybe it's a bug that has been fixed.</li></ul></div><div id="comment-18560-info" class="comment-info"><span class="comment-age">(12 Feb '13, 11:22)</span> Kurt Knochner ♦</div></div><span id="18574"></span><div id="comment-18574" class="comment"><div id="post-18574-score" class="comment-score"></div><div class="comment-text"><p>Hi, first of all thank you for your help!</p><p>I'm using tshark 1.8.1 x32 on windows XP.</p><p>I tried your command and it worked after changing nr with r , nr is not recognize by my tshark. It worked but when I added another 2 fields they stop showing!</p><p>My real command is just a very simliar to what you post here I'm just trying to output a lot of fields from ip and tcp for a tcp analysis project ( I can't post it here now beacuse it is on a different computer)</p></div><div id="comment-18574-info" class="comment-info"><span class="comment-age">(12 Feb '13, 23:28)</span> WiresharkUse...</div></div><span id="18575"></span><div id="comment-18575" class="comment not_top_scorer"><div id="post-18575-score" class="comment-score"></div><div class="comment-text"><blockquote><p>It worked but when I added another 2 fields they stop showing!</p></blockquote><p>What are those two fields?</p></div><div id="comment-18575-info" class="comment-info"><span class="comment-age">(13 Feb '13, 01:08)</span> Kurt Knochner ♦</div></div><span id="18588"></span><div id="comment-18588" class="comment not_top_scorer"><div id="post-18588-score" class="comment-score"></div><div class="comment-text"><p>-e top.len -e tcp.seq</p></div><div id="comment-18588-info" class="comment-info"><span class="comment-age">(13 Feb '13, 08:03)</span> WiresharkUse...</div></div><span id="18592"></span><div id="comment-18592" class="comment not_top_scorer"><div id="post-18592-score" class="comment-score"></div><div class="comment-text"><p>It works on my system.</p><p>I'm sorry, but if you don't post the non-working output (I asked several times for it), I really can't help you. I need to see the output of the command listed below for any capture file that causes the effect on your system.</p><blockquote><p>tshark -nr input.cap -T fields -e frame.number -e frame.time -e frame.len -e eth.type -e eth.src -e eth.dst -e ip.version -e ip.hdr_len -e ip.dsfield -e ip.len -e ip.id -e ip.flags -e ip.dst -e ip.src -e tcp.len -e tcp.seq -e tcp.ack -E header=y -E separator=;</p></blockquote><p>You can use a <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=http.cap">sample capture file</a>, if you don't want to expose your addresses/data.</p><p>You don't need to upgrade to 1.8.4. It works with 1.8.1 on my system as well, so it seems to be related to your PC.</p><p>BTW: You still did not answer the following question!</p><ul><li>how do you start tshark? From a DOS windows (if so, is it the standard command interpreter cmd.exe?)? From Java or any other programming language?</li></ul></div><div id="comment-18592-info" class="comment-info"><span class="comment-age">(13 Feb '13, 08:34)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18534" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-18534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

