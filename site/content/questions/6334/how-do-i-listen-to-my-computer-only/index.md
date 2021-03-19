+++
type = "question"
title = "How do I listen to my computer only?"
description = '''How do I listen to my computer only? Because I only want to detect all the connections that my computer is making on a specific app.'''
date = "2011-09-13T19:35:00Z"
lastmod = "2011-09-14T00:35:00Z"
weight = 6334
keywords = [ "only", "computer", "my", "listen" ]
aliases = [ "/questions/6334" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I listen to my computer only?](/questions/6334/how-do-i-listen-to-my-computer-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6334-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I listen to my computer only?</p><p>Because I only want to detect all the connections that my computer is making on a specific app.</p></div><div id="question-tags" class="tags-container tags">only computer my listen</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '11, 19:35</strong></p><img src="https://secure.gravatar.com/avatar/ace9bcd092364d1d641e753f0691522c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chris0990&#39;s gravatar image" /><p>chris0990<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chris0990 has no accepted answers">0%</span></p></div></div><div id="comments-container-6334" class="comments-container"></div><div id="comment-tools-6334" class="comment-tools"></div><div class="clear"></div><div id="comment-6334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6337"></span>

<div id="answer-container-6337" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6337-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The easiest way is to create a capture filter for the mac-address of your computer. The syntax would be:</p><pre><code>ether host 00:01:02:03:04:05</code></pre><p>(assuming you are on an ethernet)</p><p>You can find your mac-address in each packet that your computer sends, so pick a packet that you know is from your computer and look into the Ethernet details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '11, 23:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6337" class="comments-container"></div><div id="comment-tools-6337" class="comment-tools"></div><div class="clear"></div><div id="comment-6337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6340"></span>

<div id="answer-container-6340" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6340-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Or try turning promiscuous mode off (by starting the capture with the "Options" item in the "Capture" menu and un-checking the "Capture in promiscuous" mode box in the Wireshark GUI, or by passing the "-p" option on the command line in the Wireshark command line, TShark, or dumpcap).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '11, 00:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6340" class="comments-container"><span id="6342"></span><div id="comment-6342" class="comment"><div id="post-6342-score" class="comment-score"></div><div class="comment-text"><p>That also is an option. However, you will still see multicast and broadcast traffic from other systems, which might or might not be what you want.</p></div><div id="comment-6342-info" class="comment-info"><span class="comment-age">(14 Sep '11, 01:03)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-6340" class="comment-tools"></div><div class="clear"></div><div id="comment-6340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

