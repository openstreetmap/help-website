+++
type = "question"
title = "Show packet data in real-time during capture"
description = '''Is there a way to view a packet stream in real time? What I mean by this can kind of be simulated by holding ctrl+end during a capture and watching the Packet Bytes view. Not all packets need to be displayed, just the latest one. This is useful in certain situations such as monitoring a live udp str...'''
date = "2011-05-12T09:10:00Z"
lastmod = "2011-05-13T10:49:00Z"
weight = 4052
keywords = [ "selection", "packet", "real-time" ]
aliases = [ "/questions/4052" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Show packet data in real-time during capture](/questions/4052/show-packet-data-in-real-time-during-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4052-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to view a packet stream in real time? What I mean by this can kind of be simulated by holding ctrl+end during a capture and watching the Packet Bytes view. Not all packets need to be displayed, just the latest one.</p><p>This is useful in certain situations such as monitoring a live udp stream while manipulating an application.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">selection packet real-time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '11, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/02a92612e364909068c5f4b91b01ad3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hugh%20Jeffner&#39;s gravatar image" /><p>Hugh Jeffner<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hugh Jeffner has no accepted answers">0%</span></p></div></div><div id="comments-container-4052" class="comments-container"><span id="4055"></span><div id="comment-4055" class="comment"><div id="post-4055-score" class="comment-score"></div><div class="comment-text"><p>You can turn on <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChUseViewMenuSection.html">Auto Scroll in Live Capture</a>, but you still need to hit CTRL+end to view the packet bytes of the last packet.</p></div><div id="comment-4055-info" class="comment-info"><span class="comment-age">(12 May '11, 10:21)</span> joke</div></div></div><div id="comment-tools-4052" class="comment-tools"></div><div class="clear"></div><div id="comment-4052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4069"></span>

<div id="answer-container-4069" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4069-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Stealing Geralds idea and enhancing it with some awk magic might do the trick for you:</p><pre><code>tcpdump -nlX -i en1 | awk &#39;$1~&quot;..:..:..&quot; {system(&quot;clear&quot;)} {print}&#39;</code></pre><p>This will capture traffic and shows it straight away (without name-resolving nor buffering). Then the awk will clear the screen on every first line of tcpdump output of each packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '11, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4069" class="comments-container"><span id="4084"></span><div id="comment-4084" class="comment"><div id="post-4084-score" class="comment-score"></div><div class="comment-text"><p>It doesn't have the performance I was hoping for but it does work. -Thanks</p></div><div id="comment-4084-info" class="comment-info"><span class="comment-age">(13 May '11, 17:04)</span> Hugh Jeffner</div></div></div><div id="comment-tools-4069" class="comment-tools"></div><div class="clear"></div><div id="comment-4069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4056"></span>

<div id="answer-container-4056" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4056-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can sort of do this in the GUI as Joke describes, but it might make more sense to do this on the command line using <code>tshark -x</code> or <code>tcpdump -X</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '11, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-4056" class="comments-container"><span id="4061"></span><div id="comment-4061" class="comment"><div id="post-4061-score" class="comment-score"></div><div class="comment-text"><p>This looks promising, but it scrolls by way too fast. Is there an easy way to pipe the output to display only the most recent packet? I basically need to write each packet output to the same area of the screen.</p></div><div id="comment-4061-info" class="comment-info"><span class="comment-age">(12 May '11, 12:56)</span> Hugh Jeffner</div></div></div><div id="comment-tools-4056" class="comment-tools"></div><div class="clear"></div><div id="comment-4056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

