+++
type = "question"
title = "PC &gt;(wire)&gt; Router + Laptop &gt;(wifi)&gt;Router sniffing?"
description = '''Hello, my home network looks like this: Legend: &#x27;- -&#x27; = Wifi &#x27;---&#x27; = Wire  Is there any way that every packet I send from PC to internet is copied and also send to my laptop? Or is there just a way to setup wireshark so I can capture PC&#x27;s packets on my laptop? Was looking for a way whole day, testin...'''
date = "2014-12-30T10:33:00Z"
lastmod = "2014-12-30T13:58:00Z"
weight = 38801
keywords = [ "router", "computer", "packet-capture" ]
aliases = [ "/questions/38801" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PC &gt;(wire)&gt; Router + Laptop &gt;(wifi)&gt;Router sniffing?](/questions/38801/pc-wire-router-laptop-wifirouter-sniffing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38801-score" class="post-score" title="current number of votes">0</div><span id="post-38801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, my home network looks like this:</p><p>Legend:</p><p>'- -' = Wifi</p><p>'---' = Wire</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Zrzut_ekranu_2014-12-30_19.33.40.png" alt="alt text" /></p><p>Is there any way that every packet I send from PC to internet is copied and also send to my laptop?</p><p>Or is there just a way to setup wireshark so I can capture PC's packets on my laptop?</p><p>Was looking for a way whole day, testing everything, changing settings etc. etc. etc., but nothing seems to work for me.</p><p>Also, I was reading about sharing in windows, so packets from my PC also go to laptop, but I'm too stupid to set it up.</p><p>Good to know:</p><p>PC and Laptop are see themselves, also as I see in wireshark, there's dropbox's 'Lan sync discovery protocol' connection between them.</p><p>tl;dr</p><p>I want laptop to be able to see every packet that PC sends/receives.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-computer" rel="tag" title="see questions tagged &#39;computer&#39;">computer</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '14, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/08003d77dba99083f82b41854ab41cf0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pysiek&#39;s gravatar image" /><p><span>Pysiek</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pysiek has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Dec '14, 12:28</strong> </span></p></div></div><div id="comments-container-38801" class="comments-container"></div><div id="comment-tools-38801" class="comment-tools"></div><div class="clear"></div><div id="comment-38801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38806"></span>

<div id="answer-container-38806" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38806-score" class="post-score" title="current number of votes">1</div><span id="post-38806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please read the following Wiki entries</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a><br />
<a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></blockquote><p>To make a long story short: If you want to capture PCs traffic on your Latop, that won't work in your environment, unless your router</p><ul><li>supports port mirroring (which is very unlikely for a wifi connection)</li><li>supports packet capturing on the router itself</li></ul><p>If neither of the above works, you'll need what is described in the Wiki pages, meaning either a real Hub (hard to get these days) or a <a href="https://ask.wireshark.org/questions/13892/port-mirror-switch">small switch with port mirroring capabilities.</a></p><p>Alternatively you can try to install <a href="https://openwrt.org/">OpenWRT</a>, <a href="http://www.dd-wrt.com/site/index">DD-WRT</a> or <a href="https://www.gargoyle-router.com/">Gargoyle</a> (or any other supported OS, like <a href="http://polarcloud.com/tomato">Tomato</a>, etc.) on your router (if it the mentioned OSes support your model) and then do some traffic capturing there with <a href="http://www.tcpdump.org/">tcpdump</a>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '14, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-38806" class="comments-container"></div><div id="comment-tools-38806" class="comment-tools"></div><div class="clear"></div><div id="comment-38806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

