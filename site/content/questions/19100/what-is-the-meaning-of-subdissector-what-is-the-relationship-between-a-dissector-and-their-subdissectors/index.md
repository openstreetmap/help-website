+++
type = "question"
title = "What is  the meaning of subdissector? what is the relationship between a dissector and their subdissectors?"
description = '''Hi,  I&#x27;m a newcomer of wireshark.I want to know what the meaning of subdissector, what the relationship between a dissector and their subdissectors. Thank&#x27;s a lot! '''
date = "2013-03-03T00:47:00Z"
lastmod = "2013-03-03T11:09:00Z"
weight = 19100
keywords = [ "subdissector" ]
aliases = [ "/questions/19100" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What is the meaning of subdissector? what is the relationship between a dissector and their subdissectors?](/questions/19100/what-is-the-meaning-of-subdissector-what-is-the-relationship-between-a-dissector-and-their-subdissectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19100-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm a newcomer of wireshark.I want to know what the meaning of subdissector, what the relationship between a dissector and their subdissectors.</p><p>Thank's a lot!</p></div><div id="question-tags" class="tags-container tags">subdissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '13, 00:47</strong></p><img src="https://secure.gravatar.com/avatar/b9365e4208e4c3183bbc3376ec9030ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qqgeet&#39;s gravatar image" /><p>qqgeet<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qqgeet has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Mar '13, 03:42</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-19100" class="comments-container"></div><div id="comment-tools-19100" class="comment-tools"></div><div class="clear"></div><div id="comment-19100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19105"></span>

<div id="answer-container-19105" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19105-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Basically a dissector and a sub-dissector are two names for the same thing. A dissector dissects protocol headers for a certain protocol. When it comes to dissecting the payload it will hand over the remaining data to the next dissector which is then called a sub-dissector from the point of view from the dissector.</p><p>So if you have a frame like this "ETH-&gt;IP-&gt;TCP-&gt;HTTP", the following relations will exist:</p><ul><li>Dissector: Ethernet, Subdissector: IP</li><li>Dissector: IP, Subdissector: TCP</li><li>Dissector: TCP, Subdissector: HTTP</li></ul><p>And for an ICMP destination unreachable frame, it can be like this "ETH-&gt;IP-&gt;ICMP-&gt;IP" which results in the following relationships:</p><ul><li>Dissector: Ethernet, Subdissector: IP</li><li>Dissector: IP, Subdissector: ICMP</li><li>Dissector: ICMP, Subdissector: IP</li></ul><p>As you can see, the same dissector (IP) can be a dissector and a sub-dissector. It all depends on the view :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '13, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19105" class="comments-container"><span id="19112"></span><div id="comment-19112" class="comment"><div id="post-19112-score" class="comment-score"></div><div class="comment-text"><p>Thank you!</p><p>(converted to a comment in keeping with the way ask.wireshark.org works. Please see the FAQ).</p></div><div id="comment-19112-info" class="comment-info"><span class="comment-age">(03 Mar '13, 18:13)</span> qqgeet</div></div></div><div id="comment-tools-19105" class="comment-tools"></div><div class="clear"></div><div id="comment-19105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

