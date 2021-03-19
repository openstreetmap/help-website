+++
type = "question"
title = "Converting multiple pcap files to csv"
description = '''I already found a post that does this, but in windows, and I&#x27;d like to make the same for linux, but I&#x27;m kind of a newbie when it comes to the shell environment. I&#x27;d like it to work on .gz files, more than .cap files, as the windows topic suggests. Could someone hint me on how to do this? http://ask....'''
date = "2014-01-02T19:14:00Z"
lastmod = "2014-01-09T09:40:00Z"
weight = 28542
keywords = [ "pcap", "automated", "csv", "multiple", "linux" ]
aliases = [ "/questions/28542" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Converting multiple pcap files to csv](/questions/28542/converting-multiple-pcap-files-to-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28542-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I already found a post that does this, but in windows, and I'd like to make the same for linux, but I'm kind of a newbie when it comes to the shell environment. I'd like it to work on .gz files, more than .cap files, as the windows topic suggests.</p><p>Could someone hint me on how to do this?</p><p><a href="http://ask.wireshark.org/questions/12799/how-to-convert-multiple-pcap-files-to-csv">http://ask.wireshark.org/questions/12799/how-to-convert-multiple-pcap-files-to-csv</a></p><p>That is the windows topic for it.</p></div><div id="question-tags" class="tags-container tags">pcap automated csv multiple linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '14, 19:14</strong></p><img src="https://secure.gravatar.com/avatar/e5e57d1e21f6a1bbbf1278f4215f9e43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twolf&#39;s gravatar image" /><p>twolf<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twolf has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jan '14, 05:21</p></div></div><div id="comments-container-28542" class="comments-container"></div><div id="comment-tools-28542" class="comment-tools"></div><div class="clear"></div><div id="comment-28542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28739"></span>

<div id="answer-container-28739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28739-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Although this is not exactly a Wireshark question, I'm going to answer it, as I answered the other questions as well.</p><p>So, here we go.</p><pre><code>#!/bin/bash

# please change the path names if necessary
cap_files=&#39;/tmp/*.pcap.gz&#39;

outfile=&#39;/tmp/outfile.csv&#39;
tmpfile=&#39;/tmp/tmp_file.pcap&#39;

tshark_cmd=&#39;tshark&#39;
tshark_options=&#39;-n -T fields -E separator=, -e frame.time -e ip.src -e ip.dst -e ip.proto -e tcp.port -e tcp.analysis.ack_rtt&#39;

for file in $cap_files
do
   echo &quot;processing file: $file&quot;
   gunzip -c $file &gt; $tmpfile
   echo &quot;== File:  $file&quot;  &gt;&gt; $outfile
   $tshark_cmd -r $tmpfile $tshark_options &gt;&gt; $outfile
done
rm $tmpfile

echo &quot;Results in: $outfile ... Cheers Kurt&quot;</code></pre><p>This is just a small (working) example. Please modify it to your needs. <strong>However</strong> if you need further help with shell scripting, I suggest to ask the people at <a href="http://stackoverflow.com/">http://stackoverflow.com/</a> or <a href="http://superuser.com/">http://superuser.com/</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '14, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28739" class="comments-container"></div><div id="comment-tools-28739" class="comment-tools"></div><div class="clear"></div><div id="comment-28739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

