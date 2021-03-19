+++
type = "question"
title = "capture pcap file causing exceptions in java when generated via ssh"
description = '''hi guys i have this really serious problem, i am using ssh, java and Wireshark in a loop, i remotely using ssh run wireshark on a remote machine and save a certain no. of captures in a pcap file in a certain directory, then automatically java code takes this pcap file,runs and outputs files with res...'''
date = "2015-06-16T12:18:00Z"
lastmod = "2015-06-16T12:18:00Z"
weight = 43216
keywords = [ "wireshark", "java", "ssh", "tcp", "script" ]
aliases = [ "/questions/43216" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture pcap file causing exceptions in java when generated via ssh](/questions/43216/capture-pcap-file-causing-exceptions-in-java-when-generated-via-ssh)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43216-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys i have this really serious problem, i am using ssh, java and Wireshark in a loop, i remotely using ssh run wireshark on a remote machine and save a certain no. of captures in a pcap file in a certain directory, then automatically java code takes this pcap file,runs and outputs files with results, the problem is : my code works just fine when i run it over a pcap file that i generate Without using ssh! even though the saved pcap file looks so normal, BUT when the loop comes to the point when it runs the java code it crashes with exceptions caused by the pcap reader class in the library i am using, now i do not understand what might be causing this but i'm almost sure the problem is with the pcap file generated through ssh, but i am NEW TO SSH and i do not have any idea what might cause this ! any suggestions ??? also i filter the pcap file for tcp packets only, do i need to like filter the ssh packets or sth do they have weird format ?</p><p>Script for ssh</p><pre><code>#!/bin/bash

for (( c=1; c&lt;=$1; c++ ))
do
    iperf -s &amp;
    sleep 2
    ssh labpc3 -X /home/yasmin/command.sh 
    killall iperf
    ssh labpc3 java -jar /home/yasmin/Desktop/code.jar $c
    ssh labpc3 /home/yasmin/plot.sh $c
done</code></pre><p>the script for running wireshark</p></div><div id="question-tags" class="tags-container tags">wireshark java ssh tcp script</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '15, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p>yas1234<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jun '15, 12:24</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-43216" class="comments-container"><span id="43218"></span><div id="comment-43218" class="comment"><div id="post-43218-score" class="comment-score"></div><div class="comment-text"><p>So how are those files being generated? What command are you using to generate the pcap files?</p><p>What Java library are you using to read the pcap files?</p></div><div id="comment-43218-info" class="comment-info"><span class="comment-age">(16 Jun '15, 12:26)</span> Guy Harris ♦♦</div></div><span id="43220"></span><div id="comment-43220" class="comment"><div id="post-43220-score" class="comment-score"></div><div class="comment-text"><p>i am using iperf to generate traffic from computer a to computer b ..and i just run wireshark and capture those packets on the sender side, and i save it on the computer ..using this script</p><pre><code>#!/bin/bash
wireshark -i eth1 -k -c 700 -w  ~/dev/shm/new.pcap   &amp;
sleep  5</code></pre><p>and goes back to that loop in my Q and the java takes the saved pcap file as input...etc the library is not the prroblem it"s a library in my university used by only us, it's trusted ,the problem is in the ssh with wireshark</p></div><div id="comment-43220-info" class="comment-info"><span class="comment-age">(16 Jun '15, 13:31)</span> yas1234</div></div><span id="43221"></span><div id="comment-43221" class="comment"><div id="post-43221-score" class="comment-score"></div><div class="comment-text"><p>because when i don"t use ssh as i said before and i run wireshark locally and save the file..the java code takes the file and runs the way it should..but when the input to the java code is generated remotely i get exceptions..so there's something i do not know about ssh that may be causing this..that's my own vision of the problem ..maybe im wrong...</p></div><div id="comment-43221-info" class="comment-info"><span class="comment-age">(16 Jun '15, 13:32)</span> yas1234</div></div><span id="43224"></span><div id="comment-43224" class="comment"><div id="post-43224-score" class="comment-score"></div><div class="comment-text"><blockquote><p>the library is not the prroblem</p></blockquote><p>Does that library support reading pcap-ng files? If not, then the library <em>IS</em> the problem, as Wireshark writes pcap-ng files, not pcap files, by default.</p></div><div id="comment-43224-info" class="comment-info"><span class="comment-age">(16 Jun '15, 18:02)</span> Guy Harris ♦♦</div></div><span id="43234"></span><div id="comment-43234" class="comment"><div id="post-43234-score" class="comment-score"></div><div class="comment-text"><p>no it just supports pcap files, but i added in my command -X pcap and still it is not working...so what u think?</p></div><div id="comment-43234-info" class="comment-info"><span class="comment-age">(17 Jun '15, 01:49)</span> yas1234</div></div><span id="43251"></span><div id="comment-43251" class="comment not_top_scorer"><div id="post-43251-score" class="comment-score"></div><div class="comment-text"><p>what do you get if you run the following commands on the created capture file that is causing the java exception?</p><blockquote><p>file new.pcap<br />
capinfos new.pcap</p></blockquote></div><div id="comment-43251-info" class="comment-info"><span class="comment-age">(17 Jun '15, 06:43)</span> Kurt Knochner ♦</div></div><span id="43274"></span><div id="comment-43274" class="comment not_top_scorer"><div id="post-43274-score" class="comment-score"></div><div class="comment-text"><p>I think you need to read the Wireshark documentation, which does <em>NOT</em> say that <code>-X pcap</code> will cause Wireshark to write pcap files rather than pcap-ng files. It says so because it <em>WON'T</em> do so.</p><p>I also think that, unless you actually want a Wireshark window to pop up, you should just use dumpcap to produce the capture files; dumpcap has a <code>-P</code> option to force pcap files.</p></div><div id="comment-43274-info" class="comment-info"><span class="comment-age">(17 Jun '15, 10:34)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-43216" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-43216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

