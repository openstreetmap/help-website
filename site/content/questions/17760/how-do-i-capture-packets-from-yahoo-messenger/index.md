+++
type = "question"
title = "How do I capture packets from Yahoo Messenger?"
description = '''How do I capture packets from Yahoo Messenger only? Or maybe I have to set a filter after capture? I know very little about Wireshark - am working on the Windows platform.'''
date = "2013-01-17T12:49:00Z"
lastmod = "2013-01-17T13:42:00Z"
weight = 17760
keywords = [ "messenger", "yahoo" ]
aliases = [ "/questions/17760" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I capture packets from Yahoo Messenger?](/questions/17760/how-do-i-capture-packets-from-yahoo-messenger)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17760-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I capture packets from Yahoo Messenger only? Or maybe I have to set a filter after capture? I know very little about Wireshark - am working on the Windows platform.</p></div><div id="question-tags" class="tags-container tags">messenger yahoo</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '13, 12:49</strong></p><img src="https://secure.gravatar.com/avatar/97c48ddf6a1e7bfb1f8bced446a86d0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marcerickson&#39;s gravatar image" /><p>marcerickson<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marcerickson has no accepted answers">0%</span></p></div></div><div id="comments-container-17760" class="comments-container"></div><div id="comment-tools-17760" class="comment-tools"></div><div class="clear"></div><div id="comment-17760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17762"></span>

<div id="answer-container-17762" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17762-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you know what port Yahoo Messenger uses or what IP address you're communicating with, you can set a capture filter for either the port or the IP address. For example: "tcp port 5050" or "ip host 192.168.1.10". I think, though, that Yahoo Messenger can use a range of ports, so you won't always know in advance what port will be used.</p><p>If you're new to Wireshark, I recommend that you capture everything to/from your PC and then use a display filter later to focus on the Yahoo Messenger traffic. If you use the wrong capture filter, the traffic you're interested in will not be captured. If you use the wrong display filter, you won't see the traffic you're interested in, but you can just correct your display filter. Note that capture filters and display filters use different syntax. Display filters have more capability than capture filters.</p><p>Here's a link to the Wireshark wiki page on <a href="http://wiki.wireshark.org/CaptureFilters">capture filters</a> and here's the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">display filters</a> section of the User's Guide.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '13, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-17762" class="comments-container"><span id="17763"></span><div id="comment-17763" class="comment"><div id="post-17763-score" class="comment-score"></div><div class="comment-text"><p>Useful. Thanks.</p></div><div id="comment-17763-info" class="comment-info"><span class="comment-age">(17 Jan '13, 15:14)</span> marcerickson</div></div></div><div id="comment-tools-17762" class="comment-tools"></div><div class="clear"></div><div id="comment-17762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

