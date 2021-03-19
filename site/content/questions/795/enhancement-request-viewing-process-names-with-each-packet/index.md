+++
type = "question"
title = "Enhancement Request: Viewing process names with each packet"
description = '''For any OS Wireshark runs on, this would be great (my example is based on Windows).  TCPView by Mark Russinovich of Sysinternals has one feature that would great to see in Wireshark: the ability to see which process is originating traffic. If possible, it could be one of the displayed columns and co...'''
date = "2010-11-03T14:16:00Z"
lastmod = "2011-01-01T10:09:00Z"
weight = 795
keywords = [ "process", "enhancement" ]
aliases = [ "/questions/795" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Enhancement Request: Viewing process names with each packet](/questions/795/enhancement-request-viewing-process-names-with-each-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-795-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For any OS Wireshark runs on, this would be great (my example is based on Windows).</p><p>TCPView by Mark Russinovich of Sysinternals has one feature that would great to see in Wireshark: the ability to see which process is originating traffic. If possible, it could be one of the displayed columns and could be turned on or off as desired.</p><p>I find a feature like this to be not only useful in general, but quite helpful when crafting firewall policies for filtering outbound traffic. For example, recently I had a client who runs Kaspersky Internet Security on their workstations which uses outbound https and udp port 2001 to communicate with many different kis servers. It would have saved me a lot if time of Wireshark could have shown me the process that was originating those packets, in this case, avp.exe.</p><p>I hope others would find this feature useful and would agree it great to see implemented.</p></div><div id="question-tags" class="tags-container tags">process enhancement</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '10, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/7df3f9a4b16eae9f77feb6eabe92919e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eelarry&#39;s gravatar image" /><p>eelarry<br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eelarry has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Nov '10, 00:07</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-795" class="comments-container"><span id="813"></span><div id="comment-813" class="comment"><div id="post-813-score" class="comment-score"></div><div class="comment-text"><p>Bug reports and enhancement requests really belong on</p><pre><code>http://bugs.wireshark.org/</code></pre><p>as that's where we track those.</p></div><div id="comment-813-info" class="comment-info"><span class="comment-age">(03 Nov '10, 20:40)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-795" class="comment-tools"></div><div class="clear"></div><div id="comment-795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="808"></span>

<div id="answer-container-808" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-808-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I hate to rain on your parade, but trying to code that that strikes me as a portability nightmare.</p><p>I've had customers use fport (<a href="http://www.foundstone.com/us/resources/proddesc/fport.htm">http://www.foundstone.com/us/resources/proddesc/fport.htm</a>) in a batch file with tshark to grab that info as a plaintext file on Windows boxes...and lsof in the Unix world.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '10, 20:14</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-808" class="comments-container"><span id="811"></span><div id="comment-811" class="comment"><div id="post-811-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the link.</p><p>No question the code would be different for different platforms, but conditional compilation would allow building the executable appropriately for each OS. I haven't seen the WS code, but I'd be surprised to learn it was 100% portable with no conditional compilation.</p></div><div id="comment-811-info" class="comment-info"><span class="comment-age">(03 Nov '10, 20:26)</span> eelarry</div></div><span id="6449"></span><div id="comment-6449" class="comment"><div id="post-6449-score" class="comment-score"></div><div class="comment-text"><p>wesmorgan1, could you share your batch file content with us :) ?</p></div><div id="comment-6449-info" class="comment-info"><span class="comment-age">(19 Sep '11, 21:44)</span> minhtrietpha...</div></div></div><div id="comment-tools-808" class="comment-tools"></div><div class="clear"></div><div id="comment-808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1572"></span>

<div id="answer-container-1572" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1572-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Dunno about the issues wesmorgan1 raised but I would also like to see that. I am looking for a tool like that. I would be cool though I have to point out that tcpview is also rather limited as one cannot control in it. It offers a very basic view. Some of the things I am not able to manipulate are a. Able to view only one process which I'm interested in, say all 'Google Chrome processes' only b. Able to view the upload and download transactions in KB or MB.</p><p>and things like that.</p><p>Why am I going on about this is simply because I see that Wireshark could do all of this but perhaps it would need lot of work either by a user to get a nice view like that.<br />
</p><p>There is another possibility that some nice soul (read developer) makes something that makes understanding and manipulating the output easier in human-readable manner.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '11, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/ae02b958f33b24e42b2a34802d1b801c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shiish&#39;s gravatar image" /><p>shiish<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shiish has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-1572" class="comments-container"></div><div id="comment-tools-1572" class="comment-tools"></div><div class="clear"></div><div id="comment-1572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1573"></span>

<div id="answer-container-1573" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1573-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wish I could edit my answer, another thing the URL has changed for fport its now listed at http://www.mcafee.com/us/downloads/free-tools/fport.aspx</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '11, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/ae02b958f33b24e42b2a34802d1b801c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shiish&#39;s gravatar image" /><p>shiish<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shiish has no accepted answers">0%</span></p></div></div><div id="comments-container-1573" class="comments-container"></div><div id="comment-tools-1573" class="comment-tools"></div><div class="clear"></div><div id="comment-1573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1575"></span>

<div id="answer-container-1575" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1575-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is my opinion that this is NOT a feature that should be in the Wireshark base product. I do see it as very useful, but Wireshark is about packets. So we'd need a feature added into it that would only be usable when it is capturing traffic sourced or destined to the local host. It would be really, really sweet to extend all of the filtering capabilities all the way to a process. Wireshark is a great sniffer, but I see something that is capable of this being more of a hybrid process/packet analyzer that would definitely have OS dependent hooks.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '11, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1575" class="comments-container"></div><div id="comment-tools-1575" class="comment-tools"></div><div class="clear"></div><div id="comment-1575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

