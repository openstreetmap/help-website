+++
type = "question"
title = "Source Port went from 443 to astergatefax"
description = '''I have been running captures for a couple of weeks to our web service in the cloud. It using https/ssl on port 443. On the previous captures, we would send our inquiry through port 443 to the destination port of 443.  Today I see in the capture that our source port has changed from 443 to 9107 and i...'''
date = "2013-02-20T08:34:00Z"
lastmod = "2013-02-20T08:55:00Z"
weight = 18773
keywords = [ "443", "astergatefax", "webservice", "ports", "9107" ]
aliases = [ "/questions/18773" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Source Port went from 443 to astergatefax](/questions/18773/source-port-went-from-443-to-astergatefax)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18773-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been running captures for a couple of weeks to our web service in the cloud. It using https/ssl on port 443. On the previous captures, we would send our inquiry through port 443 to the destination port of 443.<br />
</p><p>Today I see in the capture that our source port has changed from 443 to 9107 and in wireshark it says "astergatefax" for the source port. It still goes to the destination port of 443 (no change there).</p><p>I'm not sure what this means and if I should be concerned. I haven't been able to find much information on the internet about astergatefax. Any help would be appreciated. Thanks.</p></div><div id="question-tags" class="tags-container tags">443 astergatefax webservice ports 9107</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '13, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/5a99095998f30a08ec58d7f6a5ece0f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sgaf&#39;s gravatar image" /><p>sgaf<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sgaf has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-18773" class="comments-container"></div><div id="comment-tools-18773" class="comment-tools"></div><div class="clear"></div><div id="comment-18773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18775"></span>

<div id="answer-container-18775" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18775-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>astergatefax</strong> is just the translation of source port 9107 done by Wireshark with the help of this file:</p><blockquote><p>Windows: <code>%ProgramFiles%\Wireshark\services</code><br />
</p></blockquote><p>There is no need to be concerned, as it is absolutely normal for TCP to have a new source port for each new connection. So, what probably happened is that either side (client or server) closed the old TCP connection and then the client opened a new connection with the source port 9107.</p><p>I'm rather 'concerned' because you say: <code>We would send our inquiry through port 443 to the destination port of 443</code>. That implies, that you had used 443 for the <strong>source</strong> and <strong>destination</strong> port. Well, that's possible, but rather unusual.</p><p>Is that intentional (design of the client software) or just coincidental (the OS picked it by chance, although none of the 'standard' OSes would do that)?</p><p>If it is intentional, then you need to figure out why the source port has changed. If it was coincidental, <strong>you</strong> don't have to care, but then <strong>I</strong> would like to know the client OS.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '13, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Feb '13, 08:56</p></div></div><div id="comments-container-18775" class="comments-container"></div><div id="comment-tools-18775" class="comment-tools"></div><div class="clear"></div><div id="comment-18775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

