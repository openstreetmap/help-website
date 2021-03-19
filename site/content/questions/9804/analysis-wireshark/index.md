+++
type = "question"
title = "analysis wireshark"
description = '''What is the mean of search &amp;gt; agent &amp;gt; 33689 [ACK} seq=4 ...................... ?'''
date = "2012-03-27T18:57:00Z"
lastmod = "2012-03-28T03:17:00Z"
weight = 9804
keywords = [ "messages" ]
aliases = [ "/questions/9804" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [analysis wireshark](/questions/9804/analysis-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9804-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the mean of search &gt; agent &gt; 33689 [ACK} seq=4 ...................... ?</p></div><div id="question-tags" class="tags-container tags">messages</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '12, 18:57</strong></p><img src="https://secure.gravatar.com/avatar/29f0a637a77e223df4167f6ab8493fa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="djedje&#39;s gravatar image" /><p>djedje<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="djedje has no accepted answers">0%</span></p></div></div><div id="comments-container-9804" class="comments-container"></div><div id="comment-tools-9804" class="comment-tools"></div><div class="clear"></div><div id="comment-9804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9808"></span>

<div id="answer-container-9808" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9808-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you wonder about "search-agent" being shown in the packet list. It is the service name that was officially registered for port 1234, and Wireshark will replace that port number by default with the name. There's a file called "services" in the Wireshark program directory where it is looked up from.</p><p>If you prefer seeing the real port numbers in the packet list you can disable the Transport layer name resolution in the View -&gt; Name Resolution menu (temporarily), or in the preferences (survives a restart of Wireshark).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '12, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9808" class="comments-container"></div><div id="comment-tools-9808" class="comment-tools"></div><div class="clear"></div><div id="comment-9808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

