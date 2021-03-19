+++
type = "question"
title = "Creating a csv file with tshark"
description = '''So here&#x27;s the deal. My goal is to take a capture from TCPDUMP and import it into a MySQL database.  I want to use wireshark to create a csv file using the &quot;tshark -r Myfile -t fields&quot; command. Once I have the csv file, i can use mysql to import the data into the database table.  I would like this cs...'''
date = "2011-03-19T18:15:00Z"
lastmod = "2013-02-28T21:34:00Z"
weight = 2935
keywords = [ "csv", "tshark" ]
aliases = [ "/questions/2935" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Creating a csv file with tshark](/questions/2935/creating-a-csv-file-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2935-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So here's the deal. My goal is to take a capture from TCPDUMP and import it into a MySQL database.</p><p>I want to use wireshark to create a csv file using the "tshark -r <em>Myfile</em> -t fields" command. Once I have the csv file, i can use mysql to import the data into the database table.</p><p>I would like this csv file to look exactly like the csv file created by using the export feature in the wireshark gui. So it should look like this:</p><p>"No.","Time","Source","Destination","Protocol","Info" "1","0.000000","IntelCor_37:d2:aa","Broadcast","ARP","Who has 192.168.1.138? Tell 0.0.0.0"</p><p>So far this is what I have: tshark -r /home/ftpuser/capture1.cap -T fields -e frame.number -e frame.time -E separator=, -E quote=d &gt; /home/ftpuser/capture1csv.csv</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">csv tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '11, 18:15</strong></p><img src="https://secure.gravatar.com/avatar/fc8e28d87818ab09a3fd00a7d941296d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mowchow&#39;s gravatar image" /><p>mowchow<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mowchow has no accepted answers">0%</span></p></div></div><div id="comments-container-2935" class="comments-container"></div><div id="comment-tools-2935" class="comment-tools"></div><div class="clear"></div><div id="comment-2935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2940"></span>

<div id="answer-container-2940" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2940-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>$ tshark -r test.pcap -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -E header=y -E separator=, -E quote=d -E occurrence=f &gt; test.csv
frame.number,frame.time,eth.src,eth.dst,ip.src,ip.dst,ip.proto
&quot;1&quot;,&quot;Mar 11, 2011 21:01:43.784303000&quot;,&quot;00:18:71:7a:90:36&quot;,&quot;00:50:56:97:2c:57&quot;,&quot;10.14.0.202&quot;,&quot;10.14.0.124&quot;,&quot;6&quot;
&quot;2&quot;,&quot;Mar 11, 2011 21:01:43.787954000&quot;,&quot;00:18:71:7a:90:36&quot;,&quot;00:50:56:97:2c:57&quot;,&quot;10.14.0.202&quot;,&quot;10.14.0.124&quot;,&quot;6&quot;
&quot;3&quot;,&quot;Mar 11, 2011 21:01:43.788908000&quot;,&quot;00:18:71:7a:90:36&quot;,&quot;00:50:56:97:2c:57&quot;,&quot;10.14.0.202&quot;,&quot;10.14.0.124&quot;,&quot;6&quot;
&quot;4&quot;,&quot;Mar 11, 2011 21:01:43.788910000&quot;,&quot;00:18:71:7a:90:36&quot;,&quot;00:50:56:97:19:17&quot;,&quot;10.14.0.202&quot;,&quot;10.14.0.128&quot;,&quot;6&quot;
&quot;5&quot;,&quot;Mar 11, 2011 21:01:43.798652000&quot;,&quot;00:00:5e:00:01:01&quot;,&quot;01:00:5e:00:00:12&quot;,&quot;10.14.7.1&quot;,&quot;224.0.0.18&quot;,&quot;112&quot;
&quot;6&quot;,&quot;Mar 11, 2011 21:01:43.801064000&quot;,&quot;00:19:bb:33:a4:b8&quot;,&quot;ff:ff:ff:ff:ff:ff&quot;,&quot;10.14.0.80&quot;,&quot;255.255.255.255&quot;,&quot;17&quot;
&quot;7&quot;,&quot;Mar 11, 2011 21:01:43.849226000&quot;,&quot;00:16:b9:1b:63:00&quot;,&quot;00:80:5a:68:ac:63&quot;,&quot;10.14.255.6&quot;,&quot;10.14.0.10&quot;,&quot;17&quot;
&quot;8&quot;,&quot;Mar 11, 2011 21:01:43.866250000&quot;,&quot;00:1e:0b:1e:7e:fe&quot;,&quot;00:80:64:60:92:2b&quot;,&quot;10.14.1.5&quot;,&quot;10.14.16.129&quot;,&quot;6&quot;
&quot;9&quot;,&quot;Mar 11, 2011 21:01:43.866723000&quot;,&quot;00:19:bb:33:a4:b8&quot;,&quot;00:19:bb:94:5c:80&quot;,&quot;10.14.0.80&quot;,&quot;10.14.7.5&quot;,&quot;17&quot;</code></pre><p>Protocol Numbers<br />
6 = tcp<br />
112 = vrrp<br />
17 = udp<br />
<a href="http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xml">Here</a> you can find more information about protocol numbers.</p><p>Note<br />
The info column is not a filterable field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '11, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-2940" class="comments-container"><span id="2946"></span><div id="comment-2946" class="comment"><div id="post-2946-score" class="comment-score"></div><div class="comment-text"><p>Thanks joke.</p><p>That will work great. I was really hoping to get that info field some how but I guess ill have to do without.</p></div><div id="comment-2946-info" class="comment-info"><span class="comment-age">(20 Mar '11, 09:23)</span> mowchow</div></div><span id="2949"></span><div id="comment-2949" class="comment"><div id="post-2949-score" class="comment-score"></div><div class="comment-text"><p>Perhaps you can add other -e fields.<br />
</p><pre><code>arp
$ tshark -r test.pcap -T fields -e arp.src.proto_ipv4 -e arp.dst.proto_ipv4 -E  header=y 
arp.src.proto_ipv4,arp.dst.proto_ipv4
&quot;10.14.1.5&quot;,&quot;10.14.1.1&quot;
&quot;10.14.1.1&quot;,&quot;10.14.1.5&quot;
http
$ tshark -r test.pcap -T fields -e http.request.method -e http.request.uri -e http.host -E  header=y 
http.request.method,http.request.uri,http.host
&quot;GET&quot;,&quot;/&quot;,&quot;www.google.nl&quot;</code></pre></div><div id="comment-2949-info" class="comment-info"><span class="comment-age">(20 Mar '11, 11:24)</span> joke</div></div><span id="61398"></span><div id="comment-61398" class="comment"><div id="post-61398-score" class="comment-score"></div><div class="comment-text"><p>Hi Joke, i had a follow up question. Could you please tell me a way to put decrypted data into a csv file.</p></div><div id="comment-61398-info" class="comment-info"><span class="comment-age">(14 May '17, 23:19)</span> ameya_k</div></div></div><div id="comment-tools-2940" class="comment-tools"></div><div class="clear"></div><div id="comment-2940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19010"></span>

<div id="answer-container-19010" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19010-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Now you can get the Info field: you have to use the latest Development Release.<br />
See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2892">Wireshark Bug 2892</a>.<br />
Download the <a href="http://www.wireshark.org/download.html">Development Release Version 1.9.0</a>.<br />
Use the following command:<br />
$ tshark -i 2 -T fields -e frame.time -e col.Info<br />
<br />
Output<br />
Feb 28, 2013 20:58:24.604635000 Who has 10.10.128.203? Tell 10.10.128.1<br />
Feb 28, 2013 20:58:24.678963000 Who has 10.10.128.163? Tell 10.10.128.1<br />
<br />
</p><p>Note<br />
-e col.Info,<br />
Use capital I</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 21:34</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-19010" class="comments-container"></div><div id="comment-tools-19010" class="comment-tools"></div><div class="clear"></div><div id="comment-19010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

