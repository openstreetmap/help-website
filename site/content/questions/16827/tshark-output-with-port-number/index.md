+++
type = "question"
title = "tshark output with port number"
description = '''greetings! I&#x27;d like to know if it&#x27;s possible to make tshark output packets with port number. For example, I use the following command: tshark -R &quot;ip.addr==1.1.1.1&quot; and I get: 163.742781 2.2.2.2 -&amp;gt; 1.1.1.1 SIP Request: INVITE sip:79107949272@1.1.1.1;user=phone 163.743301 1.1.1.1 -&amp;gt; 2.2.2.2 ICMP...'''
date = "2012-12-13T02:00:00Z"
lastmod = "2012-12-14T07:19:00Z"
weight = 16827
keywords = [ "attribute", "tshark", "options" ]
aliases = [ "/questions/16827" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark output with port number](/questions/16827/tshark-output-with-port-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16827-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>greetings!</p><p>I'd like to know if it's possible to make tshark output packets with port number. For example, I use the following command:</p><p>tshark -R "ip.addr==1.1.1.1"</p><p>and I get:</p><p>163.742781 2.2.2.2 -&gt; 1.1.1.1 SIP Request: INVITE sip:[email protected];user=phone</p><p>163.743301 1.1.1.1 -&gt; 2.2.2.2 ICMP Destination unreachable (Port unreachable)</p><p>and here I don't see what port the INVITE was sent to. Is there an option to have a port in the output?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">attribute tshark options</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '12, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/edcbd91a6646415652791302627a3370?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ky4k0b&#39;s gravatar image" /><p>ky4k0b<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ky4k0b has no accepted answers">0%</span></p></div></div><div id="comments-container-16827" class="comments-container"></div><div id="comment-tools-16827" class="comment-tools"></div><div class="clear"></div><div id="comment-16827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16883"></span>

<div id="answer-container-16883" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16883-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could try to build your own customized output.</p><blockquote><p><code>tshark -r input.cap -R "ip.add == 1.1.1.1" -T fields -e frame.number -e frame.time -e ip.src -e ip.dst -xxx</code><br />
</p></blockquote><p>where XXX is all SIP/VOIP fields you are interested in. The port number would be <strong><code>sdp.media.port</code></strong> (-e sdb.media.port). You will get all available fields with</p><blockquote><p><code>tshark -G fields</code><br />
</p></blockquote><p>Suggestion (please adjust to your needs!)</p><blockquote><p><code>tshark -r input.cap -R "ip.addr == 1.1.1.1" -T fields -e frame.number -e frame.time_delta -e ip.src -e ip.dst -e "sip.Request-Line -e sdp.media.port</code><br />
</p></blockquote><p>BTW: the ICMP port unreachable message directly after the SIP INVITE makes me believe, that your system 1.1.1.1 does not accept traffic to port UDP 5060 (SIP) and thus it sends a "port unreachable" message.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16883" class="comments-container"><span id="17084"></span><div id="comment-17084" class="comment"><div id="post-17084-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot Kurt!</p><p>I knew that I can do it with -e flag and add custom params. I was just wondering if there's a dummy mode (like another flag) to display port in the output :)</p></div><div id="comment-17084-info" class="comment-info"><span class="comment-age">(20 Dec '12, 02:13)</span> ky4k0b</div></div><span id="17088"></span><div id="comment-17088" class="comment"><div id="post-17088-score" class="comment-score"></div><div class="comment-text"><p>well, you can use the option <strong><code>-V</code></strong> or <strong><code>-T pdml</code></strong> but then you get a lot of data and you need some script to extract the parts you are interested in.</p></div><div id="comment-17088-info" class="comment-info"><span class="comment-age">(20 Dec '12, 03:34)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16883" class="comment-tools"></div><div class="clear"></div><div id="comment-16883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

