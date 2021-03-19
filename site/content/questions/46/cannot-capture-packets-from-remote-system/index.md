+++
type = "question"
title = "Cannot capture packets from remote system."
description = '''I have installed winpcap on a Win 7 Pro system, including opening tcp port 2002, and starting the service. However, I cannot capture any packets from this system. I get this error: &quot;Error while capturing packets: is the server properly installed on x.x.x.153? connect() failed: A connection attempt f...'''
date = "2010-09-13T14:19:00Z"
lastmod = "2010-09-15T21:36:00Z"
weight = 46
keywords = [ "capture", "remote", "packets" ]
aliases = [ "/questions/46" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot capture packets from remote system.](/questions/46/cannot-capture-packets-from-remote-system)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have installed winpcap on a Win 7 Pro system, including opening tcp port 2002, and starting the service. However, I cannot capture any packets from this system. I get this error: "Error while capturing packets: is the server properly installed on x.x.x.153? connect() failed: A connection attempt failed because the connection party did not properly respond after a period of time, or established connection failed because connected host has failed to respond." I have 3 remote adapters showing up for this system and I have tried all 3 with the same results. Any help is appreciated. thanks</p></div><div id="question-tags" class="tags-container tags">capture remote packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '10, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/498c3ea4699965bad06ec77d14a818aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="administrator&#39;s gravatar image" /><p>administrator<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="administrator has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 18 Sep '10, 03:35</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-46" class="comments-container"><span id="51"></span><div id="comment-51" class="comment"><div id="post-51-score" class="comment-score"></div><div class="comment-text"><p>Which service did you start?</p></div><div id="comment-51-info" class="comment-info"><span class="comment-age">(13 Sep '10, 22:29)</span> Jaap ♦</div></div></div><div id="comment-tools-46" class="comment-tools"></div><div class="clear"></div><div id="comment-46-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59"></span>

<div id="answer-container-59" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have narrowed my problem down. I turned off the Windows firewall on my Win 7 system and now I can capture packets from this system. However, I have opened the tcp port 2002 that is specified in the Wireshark users manual. What other port(s) do I need to open in order for this to work without having to turn the firewall off?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '10, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/498c3ea4699965bad06ec77d14a818aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="administrator&#39;s gravatar image" /><p>administrator<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="administrator has no accepted answers">0%</span></p></div></div><div id="comments-container-59" class="comments-container"><span id="70"></span><div id="comment-70" class="comment"><div id="post-70-score" class="comment-score"></div><div class="comment-text"><p>It looks like port 2002 is it: http://www.winpcap.org/docs/docs_412/html/group__remote.html</p></div><div id="comment-70-info" class="comment-info"><span class="comment-age">(14 Sep '10, 12:30)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-59" class="comment-tools"></div><div class="clear"></div><div id="comment-59-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="134"></span>

<div id="answer-container-134" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-134-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Make sure another process is not listening on this port. The Logmein remote access application was using tcp port 2002 on my computer. You can also specify a different port for remote capturing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '10, 21:36</strong></p><img src="https://secure.gravatar.com/avatar/e7d1d3994349a9ea0554a6430dbe2ec8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naskop&#39;s gravatar image" /><p>naskop<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naskop has no accepted answers">0%</span></p></div></div><div id="comments-container-134" class="comments-container"></div><div id="comment-tools-134" class="comment-tools"></div><div class="clear"></div><div id="comment-134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

