+++
type = "question"
title = "Trigger event on selection in packet list"
description = '''I&#x27;d like to run some analysis code when the user selects a packet in the packet list. I know nothing about the Wireshark codebase. Is there an event model? Where do I start looking? Can something like this be done in a dissector? Thanks.'''
date = "2011-01-18T11:16:00Z"
lastmod = "2011-01-18T14:12:00Z"
weight = 1792
keywords = [ "selection", "list", "event", "packet" ]
aliases = [ "/questions/1792" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trigger event on selection in packet list](/questions/1792/trigger-event-on-selection-in-packet-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1792-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to run some analysis code when the user selects a packet in the packet list. I know nothing about the Wireshark codebase. Is there an event model? Where do I start looking?</p><p>Can something like this be done in a dissector?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">selection list event packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '11, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/76eb2c6a0cfeb06a01fbbdf4aa9ce39b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joebrucepnnl&#39;s gravatar image" /><p>joebrucepnnl<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joebrucepnnl has no accepted answers">0%</span></p></div></div><div id="comments-container-1792" class="comments-container"></div><div id="comment-tools-1792" class="comment-tools"></div><div class="clear"></div><div id="comment-1792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1795"></span>

<div id="answer-container-1795" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1795-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Running <em>some analysis code when the user selects a packet</em> is basically what Wireshark does for a living. That analysis is called <em>dissection</em>, and tries to analyze all bits in the frame.</p><p>If you want to read up on Wireshark development I suggest going for the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/PartDevelopment.html">Developer's Guide</a> and <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.developer">README.developer</a>. Although not complete they should give you a pretty good start.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '11, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1795" class="comments-container"></div><div id="comment-tools-1795" class="comment-tools"></div><div class="clear"></div><div id="comment-1795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

