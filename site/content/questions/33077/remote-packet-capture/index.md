+++
type = "question"
title = "Remote packet capture"
description = '''How do you do a remote capture using a (Mac) Apple with Wireshark on it and a XP machine with Winpcap for a host? I guess I&#x27;m really not sure of where the remote capture with host field is located in the Mac version of Wireshark. Thanks in advance for the support. '''
date = "2014-05-26T06:18:00Z"
lastmod = "2014-05-26T16:20:00Z"
weight = 33077
keywords = [ "capture", "remote", "packet" ]
aliases = [ "/questions/33077" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Remote packet capture](/questions/33077/remote-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33077-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do you do a remote capture using a (Mac) Apple with Wireshark on it and a XP machine with Winpcap for a host? I guess I'm really not sure of where the remote capture with host field is located in the Mac version of Wireshark. Thanks in advance for the support.</p></div><div id="question-tags" class="tags-container tags">capture remote packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '14, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/242e7e7d7d037bfadcaae4964a4ff775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="entrophy&#39;s gravatar image" /><p>entrophy<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="entrophy has no accepted answers">0%</span></p></div></div><div id="comments-container-33077" class="comments-container"><span id="33079"></span><div id="comment-33079" class="comment"><div id="post-33079-score" class="comment-score"></div><div class="comment-text"><p>Found the manage interface through the interface and it looks like it may need some type of pipe configured for the remote capture device running XP. Please assist with needed pipe.</p></div><div id="comment-33079-info" class="comment-info"><span class="comment-age">(26 May '14, 06:23)</span> entrophy</div></div></div><div id="comment-tools-33077" class="comment-tools"></div><div class="clear"></div><div id="comment-33077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33078"></span>

<div id="answer-container-33078" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33078-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You mean QTShark? I don't think it has the option dialogs to add remote capture interfaces yet.</p><p>If you have the "old" Wireshark with the GTK interface go to Capture -&gt; Options -&gt; press the "Manage Interfaces" button, select "Remote Interfaces" tab and add a new interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '14, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33078" class="comments-container"><span id="33083"></span><div id="comment-33083" class="comment"><div id="post-33083-score" class="comment-score"></div><div class="comment-text"><p>Okay.... so ya installed WS on XP and the path you listed is available but, when the info is put in is does not update. I am currently using host,port,and null authentication.</p></div><div id="comment-33083-info" class="comment-info"><span class="comment-age">(26 May '14, 07:00)</span> entrophy</div></div><span id="33084"></span><div id="comment-33084" class="comment"><div id="post-33084-score" class="comment-score"></div><div class="comment-text"><p>Usually you should get a new interface in your interface list. If not, it could be that the feature does not work for you. Remote captures are not always working as expected unfortunately.</p></div><div id="comment-33084-info" class="comment-info"><span class="comment-age">(26 May '14, 07:09)</span> Jasper ♦♦</div></div><span id="33085"></span><div id="comment-33085" class="comment"><div id="post-33085-score" class="comment-score"></div><div class="comment-text"><p>So got it to stop freezing on the XP machine by forwarding a port on the router but, I still get a error message saying a server is not configured correctly in both authenticated and non authentication .</p></div><div id="comment-33085-info" class="comment-info"><span class="comment-age">(26 May '14, 07:14)</span> entrophy</div></div></div><div id="comment-tools-33078" class="comment-tools"></div><div class="clear"></div><div id="comment-33078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33095"></span>

<div id="answer-container-33095" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33095-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you start rpcapd.exe on the Windows box manually? It won't be started automatically.</p><blockquote><p><a href="http://www.winpcap.org/docs/docs_40_2/html/group__remote.html">http://www.winpcap.org/docs/docs_40_2/html/group__remote.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '14, 16:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33095" class="comments-container"></div><div id="comment-tools-33095" class="comment-tools"></div><div class="clear"></div><div id="comment-33095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

