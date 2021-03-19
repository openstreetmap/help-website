+++
type = "question"
title = "Capture SOAP traffic from a virtual Windows to Mac OS X host?"
description = '''My host is a Mac OS X 10.8 machine with a virtual Windows 8 residing in Parallels 8. The Mac&#x27;s ethernet address is 172.168.10.100, the Win machine shows 172.168.10.115 and is &quot;pc-rrupp-win8.testdomain.com&quot;. Parallel&#x27;s is setup to use &quot;bridged network over Ethernet&quot;. On the Windows machine, I&#x27;m runni...'''
date = "2013-05-20T09:44:00Z"
lastmod = "2013-05-20T12:07:00Z"
weight = 21319
keywords = [ "windows8", "macosx", "soap", "parallel" ]
aliases = [ "/questions/21319" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture SOAP traffic from a virtual Windows to Mac OS X host?](/questions/21319/capture-soap-traffic-from-a-virtual-windows-to-mac-os-x-host)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21319-score" class="post-score" title="current number of votes">0</div><span id="post-21319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My host is a Mac OS X 10.8 machine with a virtual Windows 8 residing in Parallels 8. The Mac's ethernet address is 172.168.10.100, the Win machine shows 172.168.10.115 and is "pc-rrupp-win8.testdomain.com". Parallel's is setup to use "bridged network over Ethernet". On the Windows machine, I'm running a web service which is called from a Mono C# application that is running on the Mac host. I would like to capture all the reply XML that is sent back by the Windows' service. However all I get is: nothing :-( I tried to use the ethernet adapter, as well as the loopback device but filtering for 172.168.10.115 does not show any responses. However, I can see the response in my Mac's C# application.</p><p>Is there maybe a sample around that would show the usage of Wireshark in combination with Parallels?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows8" rel="tag" title="see questions tagged &#39;windows8&#39;">windows8</span> <span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-soap" rel="tag" title="see questions tagged &#39;soap&#39;">soap</span> <span class="post-tag tag-link-parallel" rel="tag" title="see questions tagged &#39;parallel&#39;">parallel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '13, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/a21028a7240fe7a9ad350d80b040cf7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Krumelur&#39;s gravatar image" /><p><span>Krumelur</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Krumelur has no accepted answers">0%</span></p></div></div><div id="comments-container-21319" class="comments-container"></div><div id="comment-tools-21319" class="comment-tools"></div><div class="clear"></div><div id="comment-21319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21328"></span>

<div id="answer-container-21328" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21328-score" class="post-score" title="current number of votes">0</div><span id="post-21328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could run Wireshark in your Windows 8 virtual machine and capture the traffic there.</p><blockquote><p>device but filtering for 172.168.10.115 does not show any responses.</p></blockquote><p>What was your display filter for this?</p><p>BTW: Can you post the output of the following command?</p><blockquote><p><code>ifconfig -a</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 May '13, 11:55</strong> </span></p></div></div><div id="comments-container-21328" class="comments-container"><span id="21329"></span><div id="comment-21329" class="comment"><div id="post-21329-score" class="comment-score"></div><div class="comment-text"><p>I'll try that. The reason why I wanted to do it on the Mac: I'm hunting a bug here that has to do with corrupt network traffic (deserialization fails). I tried with Fiddler on Windows but as soon as I do that to analyze the traffic, it starts working. But maybe Wireshark is less "intrusive".</p></div><div id="comment-21329-info" class="comment-info"><span class="comment-age">(20 May '13, 11:58)</span> <span class="comment-user userinfo">Krumelur</span></div></div><span id="21330"></span><div id="comment-21330" class="comment"><div id="post-21330-score" class="comment-score"></div><div class="comment-text"><p>Fiddler is a HTTP/HTTPS proxy. Usually it will simply forward the request, but in certain situations it will change the communication behavior. Wireshark is 'non-intrusive' (even on Windows) and it will show the whole communication, as it is sent to the NIC. So, you should be able to troubleshoot your problem with Wireshark on Windows.</p></div><div id="comment-21330-info" class="comment-info"><span class="comment-age">(20 May '13, 12:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-21328" class="comment-tools"></div><div class="clear"></div><div id="comment-21328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

