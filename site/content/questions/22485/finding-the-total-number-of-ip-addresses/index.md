+++
type = "question"
title = "finding the total number of IP addresses"
description = '''How to find the total number of IP addresses observed in a trace? I tried using &quot;conversations&quot; and &quot;IP addresses&quot;, which are under statistics option, but didn&#x27;t work.'''
date = "2013-06-30T08:44:00Z"
lastmod = "2013-07-01T21:59:00Z"
weight = 22485
keywords = [ "ip", "trace", "wireshark" ]
aliases = [ "/questions/22485" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [finding the total number of IP addresses](/questions/22485/finding-the-total-number-of-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22485-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to find the total number of IP addresses observed in a trace?</p><p>I tried using "conversations" and "IP addresses", which are under statistics option, but didn't work.</p></div><div id="question-tags" class="tags-container tags">ip trace wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '13, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/03b3862efeee5519aa5b05e0e01d6e98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Irock732&#39;s gravatar image" /><p>Irock732<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Irock732 has no accepted answers">0%</span></p></div></div><div id="comments-container-22485" class="comments-container"></div><div id="comment-tools-22485" class="comment-tools"></div><div class="clear"></div><div id="comment-22485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22534"></span>

<div id="answer-container-22534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22534-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try this:</p><p>Windows</p><blockquote><p>tshark -nr input.pcap -q -z ip_hosts,tree | find "Addresses"</p></blockquote><p>Linux</p><blockquote><p>tshark -nr input.pcap -q -z ip_hosts,tree | grep "Addresses"</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '13, 21:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22534" class="comments-container"><span id="22547"></span><div id="comment-22547" class="comment"><div id="post-22547-score" class="comment-score"></div><div class="comment-text"><p>can you explain this command? I've used wireshark here, to capture network packets and saved the trace. I want to find the total number of IP addresses observed in this trace.</p></div><div id="comment-22547-info" class="comment-info"><span class="comment-age">(02 Jul '13, 01:00)</span> Irock732</div></div><span id="22548"></span><div id="comment-22548" class="comment"><div id="post-22548-score" class="comment-score"></div><div class="comment-text"><p>if you run that command at the CLI (tshark is part of Wireshark - a CLI tool), you will see something like this:</p><pre><code> IP Addresses            value          rate         percent
 IP Addresses             485       0.005124</code></pre><p>My sample capture file contain 485 different IP addresses.</p></div><div id="comment-22548-info" class="comment-info"><span class="comment-age">(02 Jul '13, 01:03)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22534" class="comment-tools"></div><div class="clear"></div><div id="comment-22534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22486"></span>

<div id="answer-container-22486" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22486-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try</p><p>Statistics&gt;EndPoint List&gt;IPV4</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '13, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-22486" class="comments-container"></div><div id="comment-tools-22486" class="comment-tools"></div><div class="clear"></div><div id="comment-22486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

