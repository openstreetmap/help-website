+++
type = "question"
title = "sip for only calls capture required and IPV6 capture filter not working"
description = '''In wireshark telephony --&amp;gt; VOIP calls will show only calls. We are running performance with 100 calls per second. File size is huge and contains register, subscriber other messages.Is there any capture filter to get only VOIP calls ? capturefilter sip takes everything Another issue in Linux im us...'''
date = "2013-12-05T05:19:00Z"
lastmod = "2014-01-31T21:43:00Z"
weight = 27805
keywords = [ "capture-filter" ]
aliases = [ "/questions/27805" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [sip for only calls capture required and IPV6 capture filter not working](/questions/27805/sip-for-only-calls-capture-required-and-ipv6-capture-filter-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27805-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In wireshark telephony --&gt; VOIP calls will show only calls. We are running performance with 100 calls per second. File size is huge and contains register, subscriber other messages.Is there any capture filter to get only VOIP calls ? capturefilter sip takes everything</p><p>Another issue in Linux im using below filter to avoid traffic capture from below network range.But it is getting captured. Can anyone please suggest for this?</p><p>tshark -i any -f "not net 2001:1234:5678:9abc:2729::/80 or not net 2001:1234:5678:9abc:2730::/80” -R "sip" -w test.pcap<br />
</p><p>Thanks, Santhosh<br />
</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '13, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/53003e4930d93213103c673c2fc87c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Santhosh%20Mohan&#39;s gravatar image" /><p>Santhosh Mohan<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Santhosh Mohan has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-27805" class="comments-container"></div><div id="comment-tools-27805" class="comment-tools"></div><div class="clear"></div><div id="comment-27805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29363"></span>

<div id="answer-container-29363" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29363-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>For capturing only call-related messages, you could use a filter like "sip.Method != REGISTER &amp;&amp; sip.Method != OPTIONS &amp;&amp; sip.Method != SUBSCRIBE &amp;&amp; sip.Method != NOTIFY &amp;&amp; sip.Method != PUBLISH". Or the opposite: "sip.Method == INVITE || sip.Method == ACK || sip.Method == PRACK || sip.Method == BYE || sip.Method == INFO". I haven't tried that with tshark's read filter (the -R option), so ymmv.</p><p>For the second problem of IPv6 subnets not being excluded, I think you want the word "and" instead of "or" in that line. :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '14, 21:43</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-29363" class="comments-container"><span id="29365"></span><div id="comment-29365" class="comment"><div id="post-29365-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help Hadriel. For the IPV6 issue, i dont think so "and" make a change, Still i will try your suggestion :)</p></div><div id="comment-29365-info" class="comment-info"><span class="comment-age">(01 Feb '14, 04:51)</span> Santhosh Mohan</div></div></div><div id="comment-tools-29363" class="comment-tools"></div><div class="clear"></div><div id="comment-29363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

