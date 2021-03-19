+++
type = "question"
title = "Why Does 1.6.8 No Longer Populate RPCAP shortcuts?"
description = '''We are running the latest version of wireshark on workstations at our office, version 1.6.8. We have remote captures that allow users to use rpcap to capture from an interface on another server. With previous versions, this would automatically populate the interface with the proper server and interf...'''
date = "2012-08-08T10:10:00Z"
lastmod = "2012-08-10T11:56:00Z"
weight = 13475
keywords = [ "interface", "not", "1.6.8", "rpcap", "populated" ]
aliases = [ "/questions/13475" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why Does 1.6.8 No Longer Populate RPCAP shortcuts?](/questions/13475/why-does-168-no-longer-populate-rpcap-shortcuts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13475-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are running the latest version of wireshark on workstations at our office, version 1.6.8. We have remote captures that allow users to use rpcap to capture from an interface on another server. With previous versions, this would automatically populate the interface with the proper server and interface to allow ease of use. Since upgrading, the interface no longer gets automatically populated.</p><p>I have tried installing within the c:\program files directory instead of c:\program files (x86) as we have a mix of users. The rpcap shortcuts properly launch wireshark, but the interface does not populate with the specified parameters in the shortcut.<br />
</p><p>This does work on version 1.2.6</p><p>What changes need to be made to run the latest version of wireshark, and still be able to utilize shortcuts for rpcap purposes?</p></div><div id="question-tags" class="tags-container tags">interface not 1.6.8 rpcap populated</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '12, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/bc6d4b17e8e5e3d8524b29360feeccae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drumz&#39;s gravatar image" /><p>drumz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drumz has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-13475" class="comments-container"><span id="13479"></span><div id="comment-13479" class="comment"><div id="post-13479-score" class="comment-score"></div><div class="comment-text"><p>may I ask what you mean by "rpcap shortcuts"?</p></div><div id="comment-13479-info" class="comment-info"><span class="comment-age">(08 Aug '12, 13:01)</span> Kurt Knochner ♦</div></div><span id="13546"></span><div id="comment-13546" class="comment"><div id="post-13546-score" class="comment-score"></div><div class="comment-text"><p>With older versions of wireshark, you could setup a windows shortcut with a path as follows - "C:\Program Files\Wireshark\wireshark.exe" -i <span>rpcap://10.10.10.66/eth1</span> - and it would open up wireshark with eth1 on 10.10.10.66 ready to capture. This no longer happens, wireshark just opens with default options set.</p></div><div id="comment-13546-info" class="comment-info"><span class="comment-age">(10 Aug '12, 11:00)</span> drumz</div></div></div><div id="comment-tools-13475" class="comment-tools"></div><div class="clear"></div><div id="comment-13475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13547"></span>

<div id="answer-container-13547" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13547-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this:</p><blockquote><p><code>wireshark -k -i rpcap://10.10.10.66/eth1</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '12, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-13547" class="comments-container"></div><div id="comment-tools-13547" class="comment-tools"></div><div class="clear"></div><div id="comment-13547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

