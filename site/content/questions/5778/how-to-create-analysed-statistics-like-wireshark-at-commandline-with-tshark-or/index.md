+++
type = "question"
title = "How to create analysed statistics like wireshark at commandline (with tshark or ...)"
description = '''Hi.. Thanks for wonderful Wireshark! I want to know how can I have analytical statistics (like the image below) like wireshark in commandline. Is it possible to have it on commandline so that we can read the results to draw graph? (f.x. with tshark, tcpdump,..)  please note that it is important for ...'''
date = "2011-08-20T08:20:00Z"
lastmod = "2013-04-19T06:09:00Z"
weight = 5778
keywords = [ "commandline", "tshark", "wireshark" ]
aliases = [ "/questions/5778" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to create analysed statistics like wireshark at commandline (with tshark or ...)](/questions/5778/how-to-create-analysed-statistics-like-wireshark-at-commandline-with-tshark-or)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5778-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi..<br />
Thanks for wonderful Wireshark!<br />
I want to know how can I have analytical statistics (like the image below) like wireshark in commandline.<br />
Is it possible to have it on commandline so that we can read the results to draw graph? (f.x. with tshark, tcpdump,..)<br />
<img src="http://i.imgur.com/PagH1.png" alt="alt text" /> please note that it is important for me to have them real-time like wireshark</p><p>Thanks in Advance.</p></div><div id="question-tags" class="tags-container tags">commandline tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '11, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/62b40c872dc85bb241751b713075daf8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smc&#39;s gravatar image" /><p>smc<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smc has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 20 Aug '11, 11:12</p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span></br></p></div></div><div id="comments-container-5778" class="comments-container"><span id="5780"></span><div id="comment-5780" class="comment"><div id="post-5780-score" class="comment-score"></div><div class="comment-text"><p>What sort of graph are you thinking of drawing with that statistic? It's not a graph in the sense of a 2D graph of two variables against each other; it might be, for example, a bar graph.</p><p>What do you mean by "real-time"? Do you mean that the graph should be displayed in real time and be updated continuously as new packets come in?</p></div><div id="comment-5780-info" class="comment-info"><span class="comment-age">(20 Aug '11, 11:55)</span> Guy Harris ♦♦</div></div><span id="5782"></span><div id="comment-5782" class="comment"><div id="post-5782-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your attention.. I want to graph number of SMPP requests and responses as shown in the wireshark graph.</p></div><div id="comment-5782-info" class="comment-info"><span class="comment-age">(20 Aug '11, 22:29)</span> smc</div></div><span id="5783"></span><div id="comment-5783" class="comment"><div id="post-5783-score" class="comment-score"></div><div class="comment-text"><p>There is no Wireshark graph shown there in your screenshot. There is a window with SMPP statistics shown as <em>text</em>, but there's no <em>graph</em>. To what graph are you referring?</p></div><div id="comment-5783-info" class="comment-info"><span class="comment-age">(21 Aug '11, 00:06)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-5778" class="comment-tools"></div><div class="clear"></div><div id="comment-5778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="5779"></span>

<div id="answer-container-5779" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5779-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Capture filter<br />
According to the <a href="http://wiki.wireshark.org/SMPP">Wireshark Wiki</a> you cannot directly filter SMPP protocols while capturing.<br />
<br />
You can use <a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark</a> with the option -T fields and send the output to a csv file.<br />
</p><pre><code>$ tshark -r smpp.cap -T fields -e frame.number -e smpp.command_id -e smpp.command_status -E header=y &gt; smpp.csv
frame.number    smpp.command_id smpp.command_status
1
2
3
4       0x00000002
5       0x80000002      0x00000000
6
7       0x00000015
8       0x80000015      0x00000000
9       0x00000004
10      0x80000004      0x00000000
11
12      0x00000006
13      0x80000006      0x00000000
14
15
16
17</code></pre><p>Display filter<br />
See the <a href="http://www.wireshark.org/docs/dfref/s/smpp.html">Display Filter Reference</a> for a list of SMPP display filter fields.<br />
<br />
Hope this helps somehow.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '11, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-5779" class="comments-container"></div><div id="comment-tools-5779" class="comment-tools"></div><div class="clear"></div><div id="comment-5779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5784"></span>

<div id="answer-container-5784" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5784-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>Can TShark statistics help you?

Count the number of SMPP Commands
$ tshark -r smpp.cap -q -z io,stat,60,COUNT&quot;(smpp.command_id)smpp.command_id&quot;,COUNT&quot;(smpp.command_status)smpp.command_status&quot;
============================================================================
IO Statistics
Interval:  60.000000 secs
Column #0: COUNT(smpp.command_id)smpp.command_id
Column #1: COUNT(smpp.command_status)smpp.command_status
                        |    Column #0   |    Column #1   |
Time                    |      COUNT     |      COUNT     |
0000.000000-0060.000000                 8                4
============================================================================

Count the number of occurances per SMPP Command ID
$ tshark -r smpp.cap -q -z io,stat,60,COUNT&quot;(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x00000002&quot;,COUNT&quot;(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x80000002&quot;,COUNT&quot;(smpp.command_id)
smpp.command_id&amp;&amp;smpp.command_id==0x00000015&quot;,COUNT&quot;(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x80000015&quot;,COUNT&quot;(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x00000004&quot;,COUNT&quot;(smpp.com
mand_id)smpp.command_id&amp;&amp;smpp.command_id==0x80000004&quot;,COUNT&quot;(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x00000006&quot;,COUNT&quot;(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x80000006&quot;,COUNT&quot;(
smpp.command_status)smpp.command_status&amp;&amp;smpp.command_status==0x00000000&quot;
==================================================================================================================================================================================
IO Statistics
Interval:  60.000000 secs
Column #0: COUNT(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x00000002
Column #1: COUNT(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x80000002
Column #2: COUNT(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x00000015
Column #3: COUNT(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x80000015
Column #4: COUNT(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x00000004
Column #5: COUNT(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x80000004
Column #6: COUNT(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x00000006
Column #7: COUNT(smpp.command_id)smpp.command_id&amp;&amp;smpp.command_id==0x80000006
Column #8: COUNT(smpp.command_status)smpp.command_status&amp;&amp;smpp.command_status==0x00000000
                        |    Column #0   |    Column #1   |    Column #2   |    Column #3   |    Column #4   |    Column #5   |    Column #6   |    Column #7   |    Column #8   |
Time                    |      COUNT     |      COUNT     |      COUNT     |      COUNT     |      COUNT     |      COUNT     |      COUNT     |      COUNT     |      COUNT     |
0000.000000-0060.000000                 1                1                1                1                1                1                1                1                4
==================================================================================================================================================================================</code></pre><br />
<br />
SMPP Command ID<br />
SMPP Requests<br />
Bind\_transmitter (0x00000002)<br />
Enquire\_link (0x00000015)<br />
Submit\_sm (0x00000004)<br />
Unbind (0x00000006)<br />
<br />
SMPP Responses<br />
Bind\_transmitter - resp (0x80000002)<br />
Enquire\_link - resp (0x80000015)<br />
Submit\_sm - resp (0x80000004)<br />
Unbind - resp (0x80000006)<br />
<br />
SMPP Response Status<br />
Ok (0x00000000)<br />
Here you can find an overview of the SMPP Command ID's:<br />
http://92.61.226.39/pbook/tcpip9.htm<br />
<br />
BTW<br />
You can use this while capture, but you will only see the packet list.<br />
The statistics show up after stopping the capture process by hitting CTRL+C.<br />
$ tshark -i name or idx of interface -z io,stat,60,COUNT"(smpp.command\_id)smpp.command\_id",COUNT"(smpp.command\_status)smpp.command\_status"</div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '11, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Aug '11, 06:30</p></div></div><div id="comments-container-5784" class="comments-container"><span id="6425"></span><div id="comment-6425" class="comment"><div id="post-6425-score" class="comment-score"></div><div class="comment-text"><p>Hi I got different results when I get statistics for a sample SMPP captured file with tshark and wireshark!!</p><p>in Tshark with command bellow I have below resulat</p><pre><code>tshark -r sample_src_w  -qz io,stat,777777,COUNT&quot;(smpp.command_id)&quot;smpp.command_id==0x80000005,COUNT&quot;(smpp.command_id)&quot;smpp.command_id==0x80000005
Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.

===================================================================
IO Statistics
Interval: 777777.000 secs
Column #0: COUNT(smpp.command_id)smpp.command_id==0x80000005
Column #1: COUNT(smpp.command_id)smpp.command_id==0x80000005
                |   Column #0    |   Column #1
Time            |          COUNT |          COUNT
000.000-777777.000              8724             8724
===================================================================</code></pre><p>but when I count with wireshark it says I have "5343" 'Deliver - resp' packages</p><p>I also use perl regular expression to count thees packets(tshrak -r smpp.cap | perl mycounter.pl), but I have 5341 packets there...</p><p>Could some one help me why is it so and why I have diffrents results for the same file??!</p><p>Thanks in Advance.</p></div><div id="comment-6425-info" class="comment-info"><span class="comment-age">(16 Sep '11, 10:09)</span> shahab</div></div><span id="6437"></span><div id="comment-6437" class="comment"><div id="post-6437-score" class="comment-score"></div><div class="comment-text"><p>any idea?</p><p>I totally got confused :((</p></div><div id="comment-6437-info" class="comment-info"><span class="comment-age">(18 Sep '11, 07:31)</span> shahab</div></div><span id="20630"></span><div id="comment-20630" class="comment"><div id="post-20630-score" class="comment-score"></div><div class="comment-text"><p>did you check the time in secs while you are running the tshark command? are the same in wireshark?</p></div><div id="comment-20630-info" class="comment-info"><span class="comment-age">(19 Apr '13, 07:19)</span> fachav2</div></div></div><div id="comment-tools-5784" class="comment-tools"></div><div class="clear"></div><div id="comment-5784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20621"></span>

<div id="answer-container-20621" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20621-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>try this tshark -nr input.pcap -q -z smpp_commands,tree</p><p>this is an answer from kurt here: <a href="http://ask.wireshark.org/questions/20589/use-tshark-to-get-smpp-operations-results">http://ask.wireshark.org/questions/20589/use-tshark-to-get-smpp-operations-results</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '13, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/ca20bac738bbb8b012045602a77d7115?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fachav2&#39;s gravatar image" /><p>fachav2<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fachav2 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-20621" class="comments-container"><span id="20690"></span><div id="comment-20690" class="comment"><div id="post-20690-score" class="comment-score"></div><div class="comment-text"><p>Awesome! That's what I want, thanks!!</p></div><div id="comment-20690-info" class="comment-info"><span class="comment-age">(21 Apr '13, 23:52)</span> smc</div></div></div><div id="comment-tools-20621" class="comment-tools"></div><div class="clear"></div><div id="comment-20621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

