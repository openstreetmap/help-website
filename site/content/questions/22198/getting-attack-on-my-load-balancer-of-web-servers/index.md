+++
type = "question"
title = "Getting attack on my load balancer of web servers?"
description = '''Hi, This afternoon I was getting swamped by an attack from a host in Malaysia.  I am pretty new with wireshark. And would like to know if this traffic from the host 175.136.20.105 to my load balancer had any other anomalies. I also noticed that there were a lot of TCP dup acks and zero len acks.  Af...'''
date = "2013-06-20T06:26:00Z"
lastmod = "2013-06-20T10:17:00Z"
weight = 22198
keywords = [ "load-balancer", "wireshark" ]
aliases = [ "/questions/22198" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting attack on my load balancer of web servers?](/questions/22198/getting-attack-on-my-load-balancer-of-web-servers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22198-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>This afternoon I was getting swamped by an attack from a host in Malaysia.</p><p>I am pretty new with wireshark. And would like to know if this traffic from the host 175.136.20.105 to my load balancer had any other anomalies. I also noticed that there were a lot of TCP dup acks and zero len acks.</p><p>After blocking this IP, my site recovered. Is there something in these packets that can give me additional insights?</p><p>The capture can be found on <a href="http://www.cloudshark.org/captures/4922bebc6d4f">http://www.cloudshark.org/captures/4922bebc6d4f</a></p><p>Would appreciate help from any kind soul.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">load-balancer wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '13, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/72758a015ff182650c5d36355fb0223b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="diden&#39;s gravatar image" /><p>diden<br />
<span class="score" title="8 reputation points">8</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="diden has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jun '13, 08:25</p></div></div><div id="comments-container-22198" class="comments-container"></div><div id="comment-tools-22198" class="comment-tools"></div><div class="clear"></div><div id="comment-22198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22204"></span>

<div id="answer-container-22204" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22204-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can see lot of GET Requests from this guy(175.136.20.105). He is looking for some real estate details and property news.Hope he will be your customer in future(Kidding).</p><p>My 2 Cents here. Open the capture using T-Shark and collect all the http GETs from him,save them to a text file,Open and start analyzing for any anomaly. Example: tshark -r &lt;yoursuspiciouscapturefile.pcap&gt; -Y http -Tfields -e http.request.uri &gt; file.txt</p><p>file.txt contains all the URIs that 175.136.20.105 requested which might give you an idea what he is doing..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '13, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jun '13, 10:18</p></div></div><div id="comments-container-22204" class="comments-container"></div><div id="comment-tools-22204" class="comment-tools"></div><div class="clear"></div><div id="comment-22204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

