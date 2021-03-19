+++
type = "question"
title = "Incoming UDP only works while capturing packages with Wireshark"
description = '''I have a question that is pretty similar to this post here:  https://ask.wireshark.org/questions/26732/incoming-udp-only-works-while-capturing-packages-with-wireshark I tried everything listed there but I&#x27;m still stuck. Im using a separate program to listen to any ip/port number I specify. I can onl...'''
date = "2017-01-23T10:27:00Z"
lastmod = "2017-01-23T10:35:00Z"
weight = 58985
keywords = [ "checksum", "udp", "promiscuous-mode", "packet" ]
aliases = [ "/questions/58985" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Incoming UDP only works while capturing packages with Wireshark](/questions/58985/incoming-udp-only-works-while-capturing-packages-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58985-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a question that is pretty similar to this post here: <a href="https://ask.wireshark.org/questions/26732/incoming-udp-only-works-while-capturing-packages-with-wireshark">https://ask.wireshark.org/questions/26732/incoming-udp-only-works-while-capturing-packages-with-wireshark</a></p><p>I tried everything listed there but I'm still stuck. Im using a separate program to listen to any ip/port number I specify. I can only see my data in that program when wireshark is running.</p><p>My dest mac address is pointing to my nic card. My source mac is my boards mac. My ip addresses I picked randomly. On my receiving computer I am listening to my destination ip and udp port I specified in the packet. My checksum is correct, but I had to go into the wireshark settings and enable verification. I'm not sure if that should have happened by default.</p><p>I constructed the entire packet myself on the send end so I can change any values I want. Here is my capture. I can add more data if that would be useful but all the packets have the exact same headers. <a href="https://www.cloudshark.org/captures/2a1cfeb30168">my capture 1 packet</a></p><p>Could this have something to do with windows throwing away the packet unless wireshark (in promiscuous mode) keeps the packet. Then my program can see the data?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">checksum udp promiscuous-mode packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '17, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/b68a0e85a290d94759364b4a2d362044?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfpentek&#39;s gravatar image" /><p>mfpentek<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfpentek has no accepted answers">0%</span></p></div></div><div id="comments-container-58985" class="comments-container"></div><div id="comment-tools-58985" class="comment-tools"></div><div class="clear"></div><div id="comment-58985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58986"></span>

<div id="answer-container-58986" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58986-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Normally, that kind of behavior is caused by the receiving NIC being in Promiscuous Mode during a capture, accepting <strong>all</strong> MAC addresses - so you should take a very close look and check if the destination MAC really matches the NIC MAC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '17, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-58986" class="comments-container"><span id="58987"></span><div id="comment-58987" class="comment"><div id="post-58987-score" class="comment-score">1</div><div class="comment-text"><p>Yup, looking over the mac again, its off by one bit. 2nd answer where you saved my behind, you really know your stuff. Thank you so much!</p></div><div id="comment-58987-info" class="comment-info"><span class="comment-age">(23 Jan '17, 12:05)</span> mfpentek</div></div><span id="58988"></span><div id="comment-58988" class="comment"><div id="post-58988-score" class="comment-score"></div><div class="comment-text"><p>You're welcome!</p></div><div id="comment-58988-info" class="comment-info"><span class="comment-age">(23 Jan '17, 12:27)</span> Jasper ♦♦</div></div></div><div id="comment-tools-58986" class="comment-tools"></div><div class="clear"></div><div id="comment-58986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

