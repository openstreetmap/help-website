+++
type = "question"
title = "Microsoft Exchange 2007"
description = '''How do I capture and filter Microsoft Exchange 2007 traffic coming from the MX server to my desktop? I have Wireshark on my box.'''
date = "2010-11-19T10:40:00Z"
lastmod = "2010-11-19T12:44:00Z"
weight = 1026
keywords = [ "mail", "traffic" ]
aliases = [ "/questions/1026" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Microsoft Exchange 2007](/questions/1026/microsoft-exchange-2007)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1026-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I capture and filter Microsoft Exchange 2007 traffic coming from the MX server to my desktop? I have Wireshark on my box.</p></div><div id="question-tags" class="tags-container tags">mail traffic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '10, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/69cf0ee6435eb6df0ea2636d7bebb9b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Delfino&#39;s gravatar image" /><p>Delfino<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Delfino has no accepted answers">0%</span></p></div></div><div id="comments-container-1026" class="comments-container"></div><div id="comment-tools-1026" class="comment-tools"></div><div class="clear"></div><div id="comment-1026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1027"></span>

<div id="answer-container-1027" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1027-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Open the capture dialog box and use this as your filter "host 1.1.1.1 or host 2.2.2.2 or host 3.3.3.3" where 1.1.1.1 is your exchange server, 2.2.2.2 is your active directory server, and 3.3.3.3 is where your PST file is stored. You may have some group address servers etc so you can also try capturing w/o any filters.</p><p>Do uncheck the "capture promiscous" mode option so you won't see unnecessary traffic. Be sure to close down all other applications before capturing.</p><p>Finally, the RPC that Exchange negotiates is dynamic, so you may not see the same tcp ports on subsequent captures.<br />
</p><p>Good luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '10, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div></div><div id="comments-container-1027" class="comments-container"></div><div id="comment-tools-1027" class="comment-tools"></div><div class="clear"></div><div id="comment-1027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

