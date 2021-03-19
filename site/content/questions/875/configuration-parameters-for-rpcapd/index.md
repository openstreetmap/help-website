+++
type = "question"
title = "Configuration Parameters for rpcapd"
description = '''I am looking in chapter 3 of the study guide and i am looking at the list of rpcapd parameters for rpcapd. How do I get to the command line in rpcapd in order to change parameters?'''
date = "2010-11-09T06:07:00Z"
lastmod = "2010-11-09T06:48:00Z"
weight = 875
keywords = [ "rpcapd", "for", "parameters" ]
aliases = [ "/questions/875" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Configuration Parameters for rpcapd](/questions/875/configuration-parameters-for-rpcapd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-875-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking in chapter 3 of the study guide and i am looking at the list of rpcapd parameters for rpcapd. How do I get to the command line in rpcapd in order to change parameters?</p></div><div id="question-tags" class="tags-container tags">rpcapd for parameters</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '10, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/43c0d29f06dc00a9752ec1c8125393f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChumMaster&#39;s gravatar image" /><p>ChumMaster<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChumMaster has no accepted answers">0%</span></p></div></div><div id="comments-container-875" class="comments-container"><span id="888"></span><div id="comment-888" class="comment"><div id="post-888-score" class="comment-score"></div><div class="comment-text"><p>See Jaap's answer below. Also see http://wiki.wireshark.org/CaptureSetup/WinPcapRemote.</p></div><div id="comment-888-info" class="comment-info"><span class="comment-age">(09 Nov '10, 14:28)</span> lchappell ♦</div></div><span id="892"></span><div id="comment-892" class="comment"><div id="post-892-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Also this part of the Wireshark User's Guide could be helpful, although it could do more explaining rpcapd itself: http://www.wireshark.org/docs/wsug_html_chunked/ChCapInterfaceRemoteSection.html</p></div><div id="comment-892-info" class="comment-info"><span class="comment-age">(10 Nov '10, 00:16)</span> Jaap ♦</div></div></div><div id="comment-tools-875" class="comment-tools"></div><div class="clear"></div><div id="comment-875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="876"></span>

<div id="answer-container-876" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-876-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From <a href="http://www.winpcap.org/docs/docs_412/html/group__remote.html">the manual</a> :</p><blockquote><p>The service has a set of "standard" parameters, i.e. it it launched with the "-d" flag (in orde to make it running as a service) and the "-f rpcapd.ini" flag. The user can create a file called rpcapd.ini in the same folder of the executable, and put the configuration commands in there.</p></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '10, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-876" class="comments-container"><span id="891"></span><div id="comment-891" class="comment"><div id="post-891-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap, your answer and the wiki you pointed out helped me better understand how to use this feature....now it is time to play.</p></div><div id="comment-891-info" class="comment-info"><span class="comment-age">(09 Nov '10, 16:38)</span> ChumMaster</div></div></div><div id="comment-tools-876" class="comment-tools"></div><div class="clear"></div><div id="comment-876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

