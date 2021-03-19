+++
type = "question"
title = "How to convert multiple .pcap files to .csv"
description = '''Hi, I would like to know if it is possible to convert multiple wireshark capture files to csv files. For example there are 3 files in a folder, is there any way to convert all three with a command or does anyone know a way to do this? Any help is appreciated. I am using a tshark command to convert o...'''
date = "2012-07-17T06:53:00Z"
lastmod = "2012-07-17T11:53:00Z"
weight = 12799
keywords = [ "csv", "export", "tshark", "loop", "batch" ]
aliases = [ "/questions/12799" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to convert multiple .pcap files to .csv](/questions/12799/how-to-convert-multiple-pcap-files-to-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12799-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to know if it is possible to convert multiple wireshark capture files to csv files. For example there are 3 files in a folder, is there any way to convert all three with a command or does anyone know a way to do this? Any help is appreciated.</p><p>I am using a tshark command to convert one file at a time,instead of test.pcap and test.csv i tried using variables as well with wildcard characters.</p><p>tshark -T fields -n -r "C:\test.pcap" -E separator=, -e frame.time -e ip.src -e ip.dst -e ip.proto -e tcp.port -e tcp.analysis.ack_rtt &gt;&gt; "C:\test.csv"</p><p>I've also tried using a for command but im running into errors with syntax. This is the full script im working with.</p><pre><code>set outfile=*.csv
set infile=*.pcap

cd C:\Program Files\Wireshark

for /f  %%f in (&#39;dir /b C:\testfolder\&#39;) do tshark -T fields -n -r &quot;C:\testfolder\%infile%&quot; -E separator=, -e frame.time -e ip.src -e ip.dst -e ip.proto -e tcp.port -e tcp.analysis.ack_rtt &gt;&gt; &quot;C:\testfolder\%outfile%&quot;  %%f </code></pre><p>Thank you in advance.</p></div><div id="question-tags" class="tags-container tags">csv export tshark loop batch</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '12, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/1e33ecfa26fea3de1d409515e786ff4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nyc&#39;s gravatar image" /><p>nyc<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nyc has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '12, 12:04</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-12799" class="comments-container"></div><div id="comment-tools-12799" class="comment-tools"></div><div class="clear"></div><div id="comment-12799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12805"></span>

<div id="answer-container-12805" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12805-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this:</p><pre><code>@echo off

set cap_files=&quot;*.cap&quot;
set cap_folder=&quot;c:\testfolder\&quot;

set outfile=c:\testfolder\outfile.txt

set tshark_cmd=&quot;c:\Program Files\Wireshark\tshark&quot;
set tshark_options=-n -T fields -E separator=, -e frame.time -e ip.src -e ip.dst -e ip.proto -e tcp.port -e tcp.analysis.ack_rtt

echo. &gt; %outfile%

for /r %cap_folder% %%f in (%cap_files%) do (
    echo Processing File: %%f

    REM echo == File:  %%f &gt;&gt; %outfile%
    %tshark_cmd%  -r %%f %tshark_options% &gt;&gt; %outfile%
)

echo.
echo Results in: %outfile% ... Cheers Kurt</code></pre><p><strong>Sample output:</strong></p><pre><code>C:\testfolder&gt; loop.cmd
Processing File: c:\testfolder\input_1.cap
Processing File: c:\testfolder\input_2.cap

Results in: c:\testfolder\outfile.txt ... Cheers Kurt</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '12, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '12, 11:57</p></div></div><div id="comments-container-12805" class="comments-container"><span id="12806"></span><div id="comment-12806" class="comment"><div id="post-12806-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>This worked perfectly for what I was trying to do, Thank you. Im going to tweak it to see if I am able to get seperate output files for each capture file.</p><p>Thanks again for your help.</p></div><div id="comment-12806-info" class="comment-info"><span class="comment-age">(17 Jul '12, 12:25)</span> nyc</div></div><span id="12807"></span><div id="comment-12807" class="comment"><div id="post-12807-score" class="comment-score"></div><div class="comment-text"><p>good luck!</p></div><div id="comment-12807-info" class="comment-info"><span class="comment-age">(17 Jul '12, 12:29)</span> Kurt Knochner ♦</div></div><span id="18389"></span><div id="comment-18389" class="comment"><div id="post-18389-score" class="comment-score"></div><div class="comment-text"><p>Will above command able to include Payload information in the txt file?</p></div><div id="comment-18389-info" class="comment-info"><span class="comment-age">(06 Feb '13, 23:15)</span> Lim Gordon</div></div><span id="18393"></span><div id="comment-18393" class="comment"><div id="post-18393-score" class="comment-score">1</div><div class="comment-text"><p>If you adjust the tshark options and depending on the type of payload you are interested: Yes.</p></div><div id="comment-18393-info" class="comment-info"><span class="comment-age">(07 Feb '13, 04:20)</span> Kurt Knochner ♦</div></div><span id="18589"></span><div id="comment-18589" class="comment not_top_scorer"><div id="post-18589-score" class="comment-score"></div><div class="comment-text"><p>Kurt, can you give me example of tshark option to include payload?</p></div><div id="comment-18589-info" class="comment-info"><span class="comment-age">(13 Feb '13, 08:32)</span> Lim Gordon</div></div><span id="18593"></span><div id="comment-18593" class="comment"><div id="post-18593-score" class="comment-score">1</div><div class="comment-text"><ul><li>What payload are you interested in? TCP, UDP, HTTP, SMTP?</li><li>Can you describe in which format you need the payload (ASCII, HEX, RAW)</li><li>Can you describe how you want to process the payload data or what you are looking for?</li></ul></div><div id="comment-18593-info" class="comment-info"><span class="comment-age">(13 Feb '13, 08:38)</span> Kurt Knochner ♦</div></div><span id="18802"></span><div id="comment-18802" class="comment not_top_scorer"><div id="post-18802-score" class="comment-score"></div><div class="comment-text"><p>• What payload are you interested in? &lt;&lt; TCP. • Can you describe in which format you need the payload. &lt;&lt; RAW. • Can you describe how you want to process the payload data or what you are looking for? &lt;&lt; Still exploring and play around data.</p></div><div id="comment-18802-info" class="comment-info"><span class="comment-age">(21 Feb '13, 08:12)</span> Lim Gordon</div></div></div><div id="comment-tools-12805" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-12805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

