+++
type = "question"
title = "How to capture real time Network traffic? Also, what are the various network parameters which can be used to perform anomaly analysis?"
description = '''I am new to networking. I would like to capture real time network traffic with which i can determine a normal network behavior. I would like to make an Anomaly based Intrusion detection system. I would like to know how to implement this. I would like to know the following 1) How to capture real time...'''
date = "2011-03-15T16:37:00Z"
lastmod = "2011-03-15T17:01:00Z"
weight = 2847
keywords = [ "capture", "network", "capture-file", "parameters", "ids" ]
aliases = [ "/questions/2847" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to capture real time Network traffic? Also, what are the various network parameters which can be used to perform anomaly analysis?](/questions/2847/how-to-capture-real-time-network-traffic-also-what-are-the-various-network-parameters-which-can-be-used-to-perform-anomaly-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2847-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to networking. I would like to capture real time network traffic with which i can determine a normal network behavior. I would like to make an Anomaly based Intrusion detection system. I would like to know how to implement this. I would like to know the following</p><p>1) How to capture real time network traffic ? 2) What all network parameters does the collected data have? 3) What is the significance of each parameter in determining anomalies in normal network behavior? 4) I have a laptop and wifi internet. Can i implement this using these two things? If not, please suggest some simple method with which i can implement this. Advices and suggestions deeply appreciated.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">capture network capture-file parameters ids</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '11, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/5afd35d48236f1537c85b15a8e035259?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="varkeyed&#39;s gravatar image" /><p>varkeyed<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="varkeyed has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '11, 16:41</p></div></div><div id="comments-container-2847" class="comments-container"></div><div id="comment-tools-2847" class="comment-tools"></div><div class="clear"></div><div id="comment-2847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2850"></span>

<div id="answer-container-2850" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2850-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you really want to do all this you're in for a lot of work, so let's see if I can break it down for you:</p><p>1) You can capture real time network traffic using Wireshark, tshark, dumpcap or tcpdump, which usually results in one or more network trace files (recorded packets) to be written to disk. For this you might need large amount of storage space and a fast PC architecture that is able to write data as fast to the disks as it is coming in the network card used to capture it.</p><p>2) Not really sure what you mean by network parameters - if you decide to capture full packets you'll get everything that was transmitted over the network at the point of capture. Keep in mind that (at least for wired networks) it is usually not possible to have one single capture recording everything that happens in your network, but you'll have to concentrate on one or more specific choke points. Even with wireless installations you might not be able to record everything that is going on since you might capture in a spot that doesn't see all radio activity going on.</p><p>3) This is the complicated part - if you want to do anomaly detection you first need to know what's normal and what isn't. This is a huge area and not something you can easily do in a short amount of time. Anomaly detection requires the ability to compare packets with each other, track certain events over time, and (in the most simple cases) to detect invalid packet structures (for example, TCP headers with SYN and FIN bit being set at the same time). If you take a look around at IPS/IDS solutions you'll see that all of them struggle to detect as much as possible, and still there are tons of anomalies (by dedicated hacking techniques or by faulty stack implementations) that they don't detect.</p><p>4) a laptop and a wifi card that is supported by Wireshark is the most basic thing you'd need, and you can start with it. It is good enough to capture packets and look at them, but if you're interested in doing fully automated live traffic inspection you'll have to code some kind of application that reads the live recorded trace files and processes them. You'll have to give it all the expert functionality to detect what is correct traffic patterns and what isn't. Not trying to scare you off, but it can easily turn into a huge project ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '11, 17:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '11, 17:04</p></div></div><div id="comments-container-2850" class="comments-container"><span id="2873"></span><div id="comment-2873" class="comment"><div id="post-2873-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper. Actually,i want to do signature analysis on incoming network traffic. For that i will have to use Netflow coming to my system. I want to know what this "Netflow" contains. This is what i mean by network traffic parameters.In simple terms, i mean the content of "Netflow" ..something like source and dest ip, packet delay etc with which i can do analysis.....(continued in next comment..)</p></div><div id="comment-2873-info" class="comment-info"><span class="comment-age">(16 Mar '11, 10:54)</span> varkeyed</div></div><span id="2874"></span><div id="comment-2874" class="comment"><div id="post-2874-score" class="comment-score"></div><div class="comment-text"><p>I heard about something called KDD dataset which contains predefined intrusion patterns. So i would like to create a database using that dataset and want to compare incoming netflow with those database entries for performing signature analysis.Please tell me if it is possible. Also, i would like to use Artificial Neural Networks for anomaly analysis... I would like to train the Neural Network using the "Netflow" and making it learn that it is the normal behavior..and an entirely different Netflow can be taken as an anomaly..I would like to do these things..Please advice me on what to do.. :)</p></div><div id="comment-2874-info" class="comment-info"><span class="comment-age">(16 Mar '11, 11:00)</span> varkeyed</div></div><span id="2878"></span><div id="comment-2878" class="comment"><div id="post-2878-score" class="comment-score"></div><div class="comment-text"><p>Well if you want to be able to receive netflow records you need to write an application that opens a UDP socket and listens to the incoming UDP packets containing the data. I've written a windows service application like that for netflow version 5 to do traffic accounting, and if I remember correctly I used the format details from http://netflow.caligare.com/netflow_v5.htm, which will also tell you the contents of such a netflow packet.</p><p>I don't know if you have experience in Neural Network programming, but you're still aiming pretty high I'd say :-)</p></div><div id="comment-2878-info" class="comment-info"><span class="comment-age">(16 Mar '11, 12:21)</span> Jasper ♦♦</div></div></div><div id="comment-tools-2850" class="comment-tools"></div><div class="clear"></div><div id="comment-2850-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

