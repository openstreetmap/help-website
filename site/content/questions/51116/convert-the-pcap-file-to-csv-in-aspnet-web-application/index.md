+++
type = "question"
title = "convert the pcap file to csv in asp.net web application"
description = '''Hi,  I have a pcap file and i am developing a web application from where user will upload a pcap file, then User will click on Process button. Now i want to process that pcap file and want to INSERT/Add all data of pcap file in sql server database.  So how can i do this ? I have tried to INSERT data...'''
date = "2016-03-23T03:31:00Z"
lastmod = "2016-03-29T03:18:00Z"
weight = 51116
keywords = [ "asp.net", "c#", "convert", "csv", "pcap" ]
aliases = [ "/questions/51116" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [convert the pcap file to csv in asp.net web application](/questions/51116/convert-the-pcap-file-to-csv-in-aspnet-web-application)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51116-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a pcap file and i am developing a web application from where user will upload a pcap file, then User will click on Process button. Now i want to process that pcap file and want to INSERT/Add all data of pcap file in sql server database.</p><p>So how can i do this ? I have tried to INSERT data of pcap file but the data did not added in a readable formate :-(</p><p>So now i want to know a method name to whom i will pass that pcap file and it will return a file in csv formate. Then it will be very simple to pass that file to sql server and data will be inserted in database table.</p><p>Thanks in advance, i am a newbie over here :-)</p></div><div id="question-tags" class="tags-container tags">asp.net c# convert csv pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '16, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/706c3ad6bf172dcf2fdde8b9c10cc0d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rabeeljaved&#39;s gravatar image" /><p>rabeeljaved<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rabeeljaved has one accepted answer">100%</span></p></div></div><div id="comments-container-51116" class="comments-container"></div><div id="comment-tools-51116" class="comment-tools"></div><div class="clear"></div><div id="comment-51116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51250"></span>

<div id="answer-container-51250" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51250-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Following is the command to convert a pCap file to csv format:</p><blockquote><p>tshark -T fields -n -r {the pathname of the capture file} -E separator=, -e {first field name} -e {second field name} ... &gt;{the pathname of the output file}</p></blockquote><p>Where <code>{the pathname of the capture file}</code> is the pathname of the capture file you're reading and <code>{first field name}, {second field name}</code> and so on are the names of the fields, and <code>{the pathname of the output file}</code> is the pathname of the output file.</p><p>Here is the final command of TShark to convert pCap file to CSV file format:</p><pre><code>tshark -T fields -n -r C:\capture.pcap -E separator=, -e ip.src -e ip.dst &gt;C:\output.csv</code></pre><p>Now we have the pCap file in CSV format, it is now possible to Insert/Add this in sql server database table.</p><p><strong>Note:</strong> <em><code>tshark</code></em> = <code>C:\Program Files\Wireshark\tshark.exe</code></p><p>Initiate an object of <strong>Process</strong> in your c# class and provide the path of cmd and pass above command line that will launch Tshark.exe and run the provided command and give us the output file at C:\output.csv. Now we can pick this file path and do what we want to do with this file like Insert in database table etc...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '16, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/706c3ad6bf172dcf2fdde8b9c10cc0d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rabeeljaved&#39;s gravatar image" /><p>rabeeljaved<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rabeeljaved has one accepted answer">100%</span></p></div></div><div id="comments-container-51250" class="comments-container"></div><div id="comment-tools-51250" class="comment-tools"></div><div class="clear"></div><div id="comment-51250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51118"></span>

<div id="answer-container-51118" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51118-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Note that there are already quite a few existing questions on this site regarding CSV output, have you looked at those?</p><p><a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark</a> is the command line application in the wireshark suite that will read a pcap file and return the text version of the dissection of the traffic in the file.</p><p>The input file is specfied with a <code>-r filename</code> option.</p><p>To produce output in csv format you'll need to use the <code>-T fields</code> option and then <code>-E separator=,</code> and possibly <code>-E header=y</code> and then supply a list of all fields you want to see with multiple <code>-e options</code>, e.g. <code>-e frame.number -e frame.time</code>. The field names are those used in display filters in Wireshark and can be seen by opening the capture file in Wireshark, selecting the field in the packet details pane and then looking at the details in the status bar.</p><p>Because you have to specify the required fields for "CSV" output, you may find it easier to process XML output, in this case use <code>-T pdml</code> or <code>-T psml</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '16, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Mar '16, 04:29</p></div></div><div id="comments-container-51118" class="comments-container"><span id="51122"></span><div id="comment-51122" class="comment"><div id="post-51122-score" class="comment-score"></div><div class="comment-text"><p>thanks @grahamb</p><p>But is there any way to convert pcap file in csv through a c# code/method instead of opening pcap file in Wireshark and converting it into csv or converting through command line....??? So here the thing, i want to upload the file through ASP.NET Web-Form application, after that i want to process that file and convert that file into csv??</p><p>I don't want to use command line kind of thing... :-(</p></div><div id="comment-51122-info" class="comment-info"><span class="comment-age">(23 Mar '16, 05:46)</span> rabeeljaved</div></div><span id="51124"></span><div id="comment-51124" class="comment"><div id="post-51124-score" class="comment-score"></div><div class="comment-text"><p>Do you want dissected traffic, i.e. similar to that which the Wireshark GUI displays in the packet detail list, or do you simply want the pcap headers for each frame and the raw frame data?</p><p>A pcap file contains some headers and then the raw frame data.</p><p>If you want dissected traffic, then you'll need to use some form of dissection library, which is what tshark provides.</p><p>If you just want the raw frame data, then a .net library that can handle pcap files may suffice, a quick Google search turned up <a href="https://github.com/PcapDotNet/Pcap.Net">pcap.net</a> and <a href="https://github.com/chmorgan/sharppcap">sharpcap</a>. I have no idea how well these work, or if they can output in csv and in sufficient detail for your purposes.</p></div><div id="comment-51124-info" class="comment-info"><span class="comment-age">(23 Mar '16, 06:51)</span> grahamb ♦</div></div></div><div id="comment-tools-51118" class="comment-tools"></div><div class="clear"></div><div id="comment-51118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

