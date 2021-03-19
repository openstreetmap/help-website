+++
type = "question"
title = "Detect DDoS at application level"
description = '''Hello everybody. I am running a small community private game server and in the last few days I got a ddos targeted at the application (tcp ports 10000,9958,5816) The problem is that I don&#x27;t know how to figure out who is the attacker. My server application is made in c# and uses beginaccept for incom...'''
date = "2015-10-18T05:33:00Z"
lastmod = "2015-10-19T10:21:00Z"
weight = 46662
keywords = [ "application", "ddos", "layer" ]
aliases = [ "/questions/46662" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Detect DDoS at application level](/questions/46662/detect-ddos-at-application-level)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46662-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody.</p><p>I am running a small community private game server and in the last few days I got a ddos targeted at the application (tcp ports 10000,9958,5816)</p><p>The problem is that I don't know how to figure out who is the attacker.</p><p>My server application is made in c# and uses beginaccept for incoming connections and in the last few days the server was using 300-400 threads when normally it would use 25-30 at maximum.</p><p>I made several captures using wireshark, I tired uploading them to cloudshark but the limit is few mbs and I have captures of bigger size.</p><p>First (23mb): <a href="https://drive.google.com/file/d/0B_2B5b9OCNu6T3lnbEk4b1JHSGs/view?usp=sharing">https://drive.google.com/file/d/0B_2B5b9OCNu6T3lnbEk4b1JHSGs/view?usp=sharing</a></p><p>Second (26mb): <a href="https://drive.google.com/file/d/0B_2B5b9OCNu6YV9SRnJERnN2MlE/view?usp=sharing">https://drive.google.com/file/d/0B_2B5b9OCNu6YV9SRnJERnN2MlE/view?usp=sharing</a></p><p>Third (529mb): <a href="https://drive.google.com/file/d/0B_2B5b9OCNu6RGQzX0VkMDJ2NU0/view?usp=sharing">https://drive.google.com/file/d/0B_2B5b9OCNu6RGQzX0VkMDJ2NU0/view?usp=sharing</a></p><p>Fourth (859mb): <a href="https://drive.google.com/file/d/0B_2B5b9OCNu6UDFaM09NbTRHd1E/view?usp=sharing">https://drive.google.com/file/d/0B_2B5b9OCNu6UDFaM09NbTRHd1E/view?usp=sharing</a></p><p>Fifth (8mb): <a href="https://drive.google.com/file/d/0B_2B5b9OCNu6dGxYT2dQVXNQMFU/view?usp=sharing">https://drive.google.com/file/d/0B_2B5b9OCNu6dGxYT2dQVXNQMFU/view?usp=sharing</a></p><p>I made my own filters at the application level (server) that took the last 10 connections from an ip and checked if the average frequency between connections is less than 5 seconds or the smallest frequency between to consequent connections is less than 1 second.</p><p>This filter only works for connections that were already accepted because there is no way to get the IP before using the endaccept and retrieving the socket.</p><p>This way I got to suspect some IPs (don't know if I got them right or they are spoofed or if it recorded anything at all, as if the connnections sent did not succeed the filter was in vain)</p><p>IPs suspected:</p><p>49.145.41.222</p><p>77.28.218.85</p><p>49.145.26.220</p><p>180.191.82.192</p><p>180.191.84.55</p><p>If I could get any help on this issue of mine I would appreciate.</p><p>Right now the server is hosted with leaseweb but they don't offer ddos protection or support, only hardware firewalls and I don't have one therefore I would like to move to ovh because they do offer ddos protection.</p><p>Thanks in advance for any help or response received.</p><p>Valentin</p></div><div id="question-tags" class="tags-container tags">application ddos layer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '15, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/93401a801e57fda1bceda1445e0770db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ryuchetval&#39;s gravatar image" /><p>Ryuchetval<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ryuchetval has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '15, 05:47</p></div></div><div id="comments-container-46662" class="comments-container"><span id="46694"></span><div id="comment-46694" class="comment"><div id="post-46694-score" class="comment-score"></div><div class="comment-text"><p>I have my game server hosted on a dedicated server with leaseweb so I can't access the router as there is none attached. Right now I moved to ovh and I hope they will be able to sort things out for me</p></div><div id="comment-46694-info" class="comment-info"><span class="comment-age">(19 Oct '15, 07:04)</span> Ryuchetval</div></div></div><div id="comment-tools-46662" class="comment-tools"></div><div class="clear"></div><div id="comment-46662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46691"></span>

<div id="answer-container-46691" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46691-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use this <a href="http://www.19216811login.org/" title="192.168.I.I">192.168.I.I</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/3feb107c7bdea2e0fb21a46cbc14940e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="websunil007&#39;s gravatar image" /><p>websunil007<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="websunil007 has no accepted answers">0%</span></p></div></div><div id="comments-container-46691" class="comments-container"></div><div id="comment-tools-46691" class="comment-tools"></div><div class="clear"></div><div id="comment-46691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46703"></span>

<div id="answer-container-46703" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46703-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It appears that some clients are driving the server to be super busy.</p><p>Analyzed the 859mb pcap "Fourth" and found that there are a few clients that caused the server to send a huge number of TCP data packets. See the <a href="http://pastebin.com/J1n0XuZp">link</a> for detail.</p><p>Please let me know if this help you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-46703" class="comments-container"><span id="46755"></span><div id="comment-46755" class="comment"><div id="post-46755-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help, I appreciate it.</p><p>Could you let me know how you sorted/filtered the incoming/ongoing packets based on the client and the amount of packets? It might be useful on the future to figure out attacks on my own.</p><p>Thanks again.</p></div><div id="comment-46755-info" class="comment-info"><span class="comment-age">(20 Oct '15, 06:36)</span> Ryuchetval</div></div><span id="46781"></span><div id="comment-46781" class="comment"><div id="post-46781-score" class="comment-score"></div><div class="comment-text"><p>Hi @Ryuchetval, here are some more info: <a href="http://pastebin.com/raw.php?i=zzWTyTLw">http://pastebin.com/raw.php?i=zzWTyTLw</a> Hope it helps.</p></div><div id="comment-46781-info" class="comment-info"><span class="comment-age">(20 Oct '15, 15:08)</span> pktUser1001</div></div></div><div id="comment-tools-46703" class="comment-tools"></div><div class="clear"></div><div id="comment-46703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

