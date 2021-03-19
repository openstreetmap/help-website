+++
type = "question"
title = "SOAP HTTP Calls are not recognized"
description = '''I&#x27;m a newbe, so my question might be pretty trivial. I have developed a SOAP client &amp;amp; am testing it by calling a remote server. When tracing with wire shark while issuing a call via SOAP-UI, all packages are only recognized by wireshark as &#x27;TCP&#x27;, not as HTTP or XML.  The result is that debugging...'''
date = "2012-08-14T07:52:00Z"
lastmod = "2012-08-14T16:08:00Z"
weight = 13614
keywords = [ "soap" ]
aliases = [ "/questions/13614" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SOAP HTTP Calls are not recognized](/questions/13614/soap-http-calls-are-not-recognized)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13614-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm a newbe, so my question might be pretty trivial.</p><p>I have developed a SOAP client &amp; am testing it by calling a remote server. When tracing with wire shark while issuing a call via SOAP-UI, all packages are only recognized by wireshark as 'TCP', not as HTTP or XML.</p><p>The result is that debugging is a nightmare, since I have to leave through all traffic to that destination and source IP address. Once found, i can use 'show stream' to see the entire xml message, but finding it is horror.</p><p>Am I doing something wrong? How can I configure WireShark to only show me the http/xml soap messages?</p><p>Many thanks in advance</p></div><div id="question-tags" class="tags-container tags">soap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '12, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/0ed291169bcf33ef20389b20300b2258?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lxkern&#39;s gravatar image" /><p>lxkern<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lxkern has no accepted answers">0%</span></p></div></div><div id="comments-container-13614" class="comments-container"></div><div id="comment-tools-13614" class="comment-tools"></div><div class="clear"></div><div id="comment-13614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13638"></span>

<div id="answer-container-13638" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13638-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your HTTP server does not run on one of the default ports (configurable for the HTTP dissector), Wireshark will not detect HTTP as such.</p><p>What can you do?</p><ul><li>change the settings of the HTTP dissector. Add "your" port to the list of TCP Ports.</li></ul><blockquote><p><code>Edit -&gt; Preferences -&gt; Protocols -&gt; HTTP -&gt; TCP Ports</code><br />
</p></blockquote><ul><li>right click on a packet of the communication and select "Decode As". Then choose HTTP for the Transport decoding</li><li>Change the port of your application to one of the ports Wireshark dissects as HTTP</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-13638" class="comments-container"></div><div id="comment-tools-13638" class="comment-tools"></div><div class="clear"></div><div id="comment-13638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

