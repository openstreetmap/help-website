+++
type = "question"
title = "Showing Live session on Wireshark?"
description = '''I was asked to show a live demo on capturing plain texts on network using wireshark. Nowadays we cant able to see http protocol anywhere, everything got converted to https and I am unsure of showing the demo capturing the plain texts transfer across network. Can someone guide me pls? Also it would b...'''
date = "2013-10-06T17:31:00Z"
lastmod = "2013-10-07T00:52:00Z"
weight = 25683
keywords = [ "live" ]
aliases = [ "/questions/25683" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Showing Live session on Wireshark?](/questions/25683/showing-live-session-on-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25683-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was asked to show a live demo on capturing plain texts on network using wireshark. Nowadays we cant able to see http protocol anywhere, everything got converted to https and I am unsure of showing the demo capturing the plain texts transfer across network. Can someone guide me pls? Also it would be nice if something interesting could be shown to users live that create awarness among people. More suggestions are welcome. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">live</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '13, 17:31</strong></p><img src="https://secure.gravatar.com/avatar/b41802fe7f333c0b2b2b68be7da4f757?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karthick&#39;s gravatar image" /><p>Karthick<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karthick has no accepted answers">0%</span></p></div></div><div id="comments-container-25683" class="comments-container"></div><div id="comment-tools-25683" class="comment-tools"></div><div class="clear"></div><div id="comment-25683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25698"></span>

<div id="answer-container-25698" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25698-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't capture plain text passwords if the protocol in use is HTTPS - I'd even go as far as saying that passwords transmitted via HTTPS aren't "plain text" anymore. So Wireshark won't help you here as long as the requirements are that a third party should steal plain text passwords. You can of course decode SSL sessions with Wireshark under the right circumstances, but an attacker without additional intel should not be able to do that.</p><p>So I see three demo options here:</p><ol><li>Find something that isn't HTTPS and demo it</li><li>Pretend that the SSL private server key got compromised and decode the HTTPS traffic. This is pretty much noch in the area of an awareness training, unless your attendees are SSL server admins that need another hint that they need to keep their SSL private keys protected</li><li>Do someting like a Man-in-the-Middle by using a proxy to get into the communication, like <a href="http://fiddler2.com/">Fiddler</a>. This, once again, is not really a good setup for an awareness training, because people would have to accept bad (forged) SSL certificates before it works - unless, once again, that this is in your scope of the training.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25698" class="comments-container"><span id="25713"></span><div id="comment-25713" class="comment"><div id="post-25713-score" class="comment-score"></div><div class="comment-text"><p>plus show something about ARP spoofing (cain and abel). Most people are totally unaware of that problem.</p><blockquote><p><a href="http://www.chmag.in/article/feb2012/cain-and-abel-black-art-arp-poisoning">http://www.chmag.in/article/feb2012/cain-and-abel-black-art-arp-poisoning</a></p></blockquote></div><div id="comment-25713-info" class="comment-info"><span class="comment-age">(07 Oct '13, 08:06)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25698" class="comment-tools"></div><div class="clear"></div><div id="comment-25698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

