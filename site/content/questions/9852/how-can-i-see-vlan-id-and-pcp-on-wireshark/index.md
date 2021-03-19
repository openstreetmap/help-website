+++
type = "question"
title = "How can i see vlan id and pcp on wireshark?"
description = '''On filter when i enter vlan, the message that appears is: &quot;vlan&quot; is neither a field nor a protocol name. The following display filter isn&#x27;t a valid display filter: vlan See the help for a description of the display filter syntax. How can i see vlan id and pcp on wireshark? I am using Ubuntu 11.10 am...'''
date = "2012-03-29T16:15:00Z"
lastmod = "2012-03-29T17:43:00Z"
weight = 9852
keywords = [ "vlan" ]
aliases = [ "/questions/9852" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can i see vlan id and pcp on wireshark?](/questions/9852/how-can-i-see-vlan-id-and-pcp-on-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9852-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On filter when i enter vlan, the message that appears is:</p><p>"vlan" is neither a field nor a protocol name.</p><p>The following display filter isn't a valid display filter: vlan See the help for a description of the display filter syntax.</p><p>How can i see vlan id and pcp on wireshark?</p><p>I am using Ubuntu 11.10 amd64.</p><p>Thanks,</p><p>Diego Silva.</p></div><div id="question-tags" class="tags-container tags">vlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '12, 16:15</strong></p><img src="https://secure.gravatar.com/avatar/a2e20e4d01051429cd07791846a05689?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Diego%20Silva&#39;s gravatar image" /><p>Diego Silva<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Diego Silva has no accepted answers">0%</span></p></div></div><div id="comments-container-9852" class="comments-container"></div><div id="comment-tools-9852" class="comment-tools"></div><div class="clear"></div><div id="comment-9852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9853"></span>

<div id="answer-container-9853" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9853-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, you fail to mention which version of Wireshark you're using, but it's apparently one that was before <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=34838">r34838</a>.</p><p>Originally the filters you're interested in were <a href="http://www.wireshark.org/docs/dfref/e/eth.html">eth.vlan.id</a> and <a href="http://www.wireshark.org/docs/dfref/e/eth.html">eth.vlan.pri</a>, but they became <a href="http://www.wireshark.org/docs/dfref/v/vlan.html">vlan.id</a> and <a href="http://www.wireshark.org/docs/dfref/v/vlan.html">vlan.priority</a>, respectively, in order to attempt to resolve <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2254">bug2254</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '12, 17:43</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Mar '12, 06:32</p></div></div><div id="comments-container-9853" class="comments-container"><span id="9860"></span><div id="comment-9860" class="comment"><div id="post-9860-score" class="comment-score"></div><div class="comment-text"><p>The wireshark version is 1.6.2.</p><p>I'm using Ubuntu 11.10 (Released in 10/2011) desktop amd64.</p><p>Thanks,</p><p>Diego.</p></div><div id="comment-9860-info" class="comment-info"><span class="comment-age">(30 Mar '12, 06:24)</span> Diego Silva</div></div><span id="9861"></span><div id="comment-9861" class="comment"><div id="post-9861-score" class="comment-score"></div><div class="comment-text"><p>OK, so as the link I provided indicates, you will need to use the older <a href="http://www.wireshark.org/docs/dfref/e/eth.html">eth.vlan.id</a> and <a href="http://www.wireshark.org/docs/dfref/e/eth.html">eth.vlan.pri</a> filters instead.</p></div><div id="comment-9861-info" class="comment-info"><span class="comment-age">(30 Mar '12, 06:34)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-9853" class="comment-tools"></div><div class="clear"></div><div id="comment-9853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

