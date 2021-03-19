+++
type = "question"
title = "Assign name to ip-address?"
description = '''I would like to see the names in the packet list in run time. But even after I mention the ip-address &amp;amp; name in &quot;hosts&quot; file under %application data%/wireshark, I dont see the names being shown in wireshark. The same thing works for mac-address naming? I tried changing &quot;columns&quot; under preference...'''
date = "2010-09-17T02:07:00Z"
lastmod = "2010-09-17T04:11:00Z"
weight = 165
keywords = [ "name-resolving" ]
aliases = [ "/questions/165" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Assign name to ip-address?](/questions/165/assign-name-to-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-165-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to see the names in the packet list in run time. But even after I mention the ip-address &amp; name in "hosts" file under %application data%/wireshark, I dont see the names being shown in wireshark.</p><p>The same thing works for mac-address naming?</p><p>I tried changing "columns" under preferences from src.address/dst.address --&gt; src/dst address(resolved), still I dont see the names.</p><p>Any idea what am I missing?</p></div><div id="question-tags" class="tags-container tags">name-resolving</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '10, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/5c59321a66976ba615e1a50b46a4d209?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramprasad&#39;s gravatar image" /><p>Ramprasad<br />
<span class="score" title="20 reputation points">20</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramprasad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 17 Sep '10, 11:25</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-165" class="comments-container"><span id="24183"></span><div id="comment-24183" class="comment"><div id="post-24183-score" class="comment-score"></div><div class="comment-text"><p>How can i do the same for the Mac OS</p></div><div id="comment-24183-info" class="comment-info"><span class="comment-age">(29 Aug '13, 22:57)</span> icomixx</div></div></div><div id="comment-tools-165" class="comment-tools"></div><div class="clear"></div><div id="comment-165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="168"></span>

<div id="answer-container-168" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-168-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Enable <em>Network name resolution</em> in the preferences.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '10, 04:11</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-168" class="comments-container"><span id="178"></span><div id="comment-178" class="comment"><div id="post-178-score" class="comment-score"></div><div class="comment-text"><p>But for network name resolution, you need a DNS server right?, I dont have any DNS server which can resolve them. I want static mapping of ip-address to name.</p><p>Any idea how do I do that?</p></div><div id="comment-178-info" class="comment-info"><span class="comment-age">(17 Sep '10, 05:40)</span> Ramprasad</div></div><span id="181"></span><div id="comment-181" class="comment"><div id="post-181-score" class="comment-score"></div><div class="comment-text"><p>Add the entries to the hosts file, or add them manually from the packet list.</p></div><div id="comment-181-info" class="comment-info"><span class="comment-age">(17 Sep '10, 08:21)</span> Jaap ♦</div></div><span id="212"></span><div id="comment-212" class="comment"><div id="post-212-score" class="comment-score"></div><div class="comment-text"><p>I tried that as my first attempt. That didnt work!</p><p>Any idea what am I missing?</p></div><div id="comment-212-info" class="comment-info"><span class="comment-age">(18 Sep '10, 06:30)</span> Ramprasad</div></div></div><div id="comment-tools-168" class="comment-tools"></div><div class="clear"></div><div id="comment-168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

