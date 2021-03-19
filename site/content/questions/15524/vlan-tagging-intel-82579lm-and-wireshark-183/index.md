+++
type = "question"
title = "VLAN Tagging Intel 82579LM and Wireshark 1.8.3"
description = '''Hi all, I&#x27;m use wireshark 1.8.3 and a dell E6410 with intel 82579lm network adapter. I can&#x27;t see any vlan information in a capture although I have configured tagging in the networkcard settings and the networkconnection is working very well. What I have to do in addition? Greetings Hartmut '''
date = "2012-11-04T07:29:00Z"
lastmod = "2012-11-04T11:58:00Z"
weight = 15524
keywords = [ "vlan", "intel", "tagging", "82579lm" ]
aliases = [ "/questions/15524" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [VLAN Tagging Intel 82579LM and Wireshark 1.8.3](/questions/15524/vlan-tagging-intel-82579lm-and-wireshark-183)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15524-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm use wireshark 1.8.3 and a dell E6410 with intel 82579lm network adapter. I can't see any vlan information in a capture although I have configured tagging in the networkcard settings and the networkconnection is working very well. What I have to do in addition? Greetings Hartmut</p></div><div id="question-tags" class="tags-container tags">vlan intel tagging 82579lm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '12, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/8e21ecc2d227132d67217fbf084bdada?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hartmut&#39;s gravatar image" /><p>Hartmut<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hartmut has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Dec '12, 04:04</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-15524" class="comments-container"></div><div id="comment-tools-15524" class="comment-tools"></div><div class="clear"></div><div id="comment-15524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15527"></span>

<div id="answer-container-15527" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15527-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please check the answer of @KeithFrench in the following question.</p><blockquote><p><code>http://ask.wireshark.org/questions/1983/vlan-capture-setup-for-intel-network-card</code><br />
</p></blockquote><p>It's about a the driver parameters <strong>MonitorMode</strong> and <strong>MonitorModeEnabled</strong> in the registry.</p><p>Additionally check also the explanation of Intel about this issue:</p><blockquote><p><code>http://www.intel.com/support/network/sb/cs-005897.htm</code><br />
</p></blockquote><p>See also here:</p><blockquote><p><code>http://dot1x.blogspot.de/2010/03/sniffing-dot1q-tags-with-wireshark.html</code><br />
</p></blockquote><p>If that does not work, please check my answer in the following question:</p><blockquote><p><code>http://ask.wireshark.org/questions/14075/can-not-see-packets-from-local-machine</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '12, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-15527" class="comments-container"><span id="15639"></span><div id="comment-15639" class="comment"><div id="post-15639-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt Thank you, now it works fine. Regards Hartmut</p></div><div id="comment-15639-info" class="comment-info"><span class="comment-age">(07 Nov '12, 05:32)</span> Hartmut</div></div><span id="15640"></span><div id="comment-15640" class="comment"><div id="post-15640-score" class="comment-score"></div><div class="comment-text"><p>@Hartmut,</p><p>If the answer has solved your problem please accept the answer by clicking the checkmark icon next to the answer. This allows other users to easily see which questions have good answers.</p></div><div id="comment-15640-info" class="comment-info"><span class="comment-age">(07 Nov '12, 05:39)</span> grahamb ♦</div></div><span id="15653"></span><div id="comment-15653" class="comment"><div id="post-15653-score" class="comment-score"></div><div class="comment-text"><p>@Hartmut: What did you change? MonitorMode or MonitorModeEnabled?</p></div><div id="comment-15653-info" class="comment-info"><span class="comment-age">(07 Nov '12, 08:19)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-15527" class="comment-tools"></div><div class="clear"></div><div id="comment-15527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

