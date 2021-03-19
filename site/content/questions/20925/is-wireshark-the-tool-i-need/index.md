+++
type = "question"
title = "Is Wireshark the tool I need?"
description = '''Greetings Wireshark Wizes! Tonight I downloaded the tool and read through some of the documentation. Without tunneling too much further, I wanted to see if the pros think there is gold at the end of my tunnel. What I&#x27;m looking for is this: A background TCP monitoring program that will alert me and r...'''
date = "2013-05-03T02:44:00Z"
lastmod = "2013-05-03T03:16:00Z"
weight = 20925
keywords = [ "trigger", "run", "event", "stream", "script" ]
aliases = [ "/questions/20925" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is Wireshark the tool I need?](/questions/20925/is-wireshark-the-tool-i-need)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20925-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings Wireshark Wizes! Tonight I downloaded the tool and read through some of the documentation. Without tunneling too much further, I wanted to see if the pros think there is gold at the end of my tunnel. What I'm looking for is this: A background TCP monitoring program that will alert me and run a script when a certain IP sends me a packet, or when a certain packet is received regardless of the source.</p><p>Based on playing around with Wireshark for 5 minutes, it should have NO problem observing and filtering traffic to find what I'm looking for. However, I'm having a hard time seeing how you would run a script when a certain packet is received. In the documentation(5.7.4) I see it is possible to export filtered data to a C array (although I don't see where it explains how to do that). Could the data be constantly streamed to some buffer location where I can sort through it using another program?</p><p>I play around with a script building program called AutoHotkey, so if I could read the packet information with AutoHotkey, my problems would be solved. What do you think? Is this the right place for me? If not, does anyone have any recommendations? Thanks! JD</p></div><div id="question-tags" class="tags-container tags">trigger run event stream script</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '13, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/3e730e166d26edc1b8d04e2e3b8e69b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoroaster&#39;s gravatar image" /><p>Zoroaster<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoroaster has no accepted answers">0%</span></p></div></div><div id="comments-container-20925" class="comments-container"><span id="21000"></span><div id="comment-21000" class="comment"><div id="post-21000-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys for the fast response! I got swamped with other projects, so this will have to wait for a while, but thanks for saving me a bunch of time, and pointing me in some new directions. When I get a chance, I'll followup with y'alls suggestions/questions. thanks! JD</p></div><div id="comment-21000-info" class="comment-info"><span class="comment-age">(07 May '13, 02:42)</span> Zoroaster</div></div></div><div id="comment-tools-20925" class="comment-tools"></div><div class="clear"></div><div id="comment-20925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20926"></span>

<div id="answer-container-20926" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20926-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi JD, wireshark is <strong>NOT</strong> the tool for your purpose. Wireshark is great as an analyzer, but not good as a monitoring tool, as it keeps state of session for doing further analysis. This means you will run out of memory doing long term capturing.</p><p>You can use dumpcap (included with wireshark) for long-term capturing and use a ringbuffer of X files to make your harddrive not fill up. I have used this setup for months in a row. You can then write a script that processes each completed file (with tshark for instance) to see whether there is a packet of interest and based on the result fire another script.</p><p>The big questions are: - how much traffic do you need to keep up with - how soon must you be notified after the packets of interest were seen</p><p>Answer to these questions will determine the sizing of the box needed and the parameters for dumpcap to make this happen.</p><p>In short, wireshark itself is not the tool for you, but the accompanied dumpcap and tshark and a little scripting can do the trick.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '13, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20926" class="comments-container"></div><div id="comment-tools-20926" class="comment-tools"></div><div class="clear"></div><div id="comment-20926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20930"></span>

<div id="answer-container-20930" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20930-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>A combination of <a href="http://ngrep.sourceforge.net/">ngrep</a> and some scripting might be the better tool for you.</p><blockquote><p>A background TCP monitoring program that will alert me and run a script when a certain IP sends me a packet, or when a certain packet is received regardless of the source.</p></blockquote><p>BTW: What are your trying to do? Why do you need to capture a packet with a sniffer that is sent to your system or an application on your system? Wouldn't it be easier to handle that packet in the application?!?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '13, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20930" class="comments-container"></div><div id="comment-tools-20930" class="comment-tools"></div><div class="clear"></div><div id="comment-20930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

