+++
type = "question"
title = "&quot;Continuation&quot; in info column of SIP traffic"
description = '''In collected traces, we are seeing that Continuation message in sip protocol.There are continuation line and continuation protocol which are empty in this sip message. According to the wireshark logs,soft client VOIP program is sending this,however we are not facing any sip message which has contina...'''
date = "2013-11-19T05:44:00Z"
lastmod = "2014-01-31T21:28:00Z"
weight = 27098
keywords = [ "continuation", "message" ]
aliases = [ "/questions/27098" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# ["Continuation" in info column of SIP traffic](/questions/27098/continuation-in-info-column-of-sip-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27098-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In collected traces, we are seeing that Continuation message in sip protocol.There are continuation line and continuation protocol which are empty in this sip message. According to the wireshark logs,soft client VOIP program is sending this,however we are not facing any sip message which has contination name. when we investigate this soft clients logs. Can you explain why Wireshark is showing a message like that.</p><p>In addition network elements are using TCP protocol for sip messaging.</p><p>Regards,</p><p>Gizem Arslan.</p></div><div id="question-tags" class="tags-container tags">continuation message</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '13, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/5244b2a35deda22fea7fe96ad888a96f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gizem%20arslan&#39;s gravatar image" /><p>gizem arslan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gizem arslan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jan '14, 09:07</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-27098" class="comments-container"><span id="28866"></span><div id="comment-28866" class="comment"><div id="post-28866-score" class="comment-score"></div><div class="comment-text"><p>I am having similar issue with SIP TCP packets showing up as "Continuation". I am on the latest build of Wireshark. About shows the following: Version 1.10.5 (SVN Rev 54262 from /trunk-1.10)</p></div><div id="comment-28866-info" class="comment-info"><span class="comment-age">(14 Jan '14, 08:14)</span> buddhaholic420</div></div><span id="28870"></span><div id="comment-28870" class="comment"><div id="post-28870-score" class="comment-score"></div><div class="comment-text"><p>according to packet-sip.c, that's a sign for a SIP 'command' that's unknown to wireshark.</p><p>Hint: parts of the code removed!!</p><pre><code>    switch (line_type) {
case REQUEST_LINE:
            ....
    descr = is_known_request ? &quot;Request&quot; : &quot;Unknown request&quot;;
    col_add_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;%s: %s&quot;,
                 descr,
                 tvb_format_text(tvb, offset, linelen - SIP2_HDR_LEN - 1));
    break;

case STATUS_LINE:
    descr = &quot;Status&quot;;
    col_add_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;Status: %s&quot;,
                 tvb_format_text(tvb, offset + SIP2_HDR_LEN + 1, linelen - SIP2_HDR_LEN - 1));

case OTHER_LINE:
default: /* Squelch compiler complaints */
    &lt;b&gt;descr = &quot;Continuation&quot;;&lt;/b&gt;
    col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot;Continuation&quot;);
    break;
}</code></pre></pre><p>If you can post a sample capture we can have a look and find the explanation for it in the data (like wrong number of whitespace, etc.)</p></div><div id="comment-28870-info" class="comment-info"><span class="comment-age">(14 Jan '14, 09:06)</span> Kurt Knochner ♦</div></div><span id="28880"></span><div id="comment-28880" class="comment"><div id="post-28880-score" class="comment-score"></div><div class="comment-text"><p>Or (by inspecting the code above) a SIP 'command' of "OTHER_LINE" as both that and the default (i.e. an unknown 'command') will add the "Continuation" string.</p></div><div id="comment-28880-info" class="comment-info"><span class="comment-age">(14 Jan '14, 10:26)</span> grahamb ♦</div></div></div><div id="comment-tools-27098" class="comment-tools"></div><div class="clear"></div><div id="comment-27098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29362"></span>

<div id="answer-container-29362" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29362-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's perfectly normal, assuming you're capturing live SIP data - when you start Wireshark capturing, and there's SIP/TCP traffic already going back/forth, then some of the initial packets Wireshark sees will be the ending/trailing TCP segments of SIP messages. Wireshark simply doesn't have the whole SIP message in such cases, but instead only some ending portion of them. The SIP parser can't reasonably decode such messages, so it just calls them "continuation" until it finds a start line later.</p><p>Since TCP defines no message boundary/framing for its payload application, the SIP parser in Wireshark has to assume that anything not matching a SIP message start line, in a new TCP stream it hasn't seen before, is a "continuation" of a previous SIP message that wireshark didn't capture the beginning of. So it calls it "continuation", until it finds the beginning of a new SIP message, and from then on in that TCP stream (ie, for the same 5-tuple) it shouldn't happen again, and instead wireshark can parse the rest of the SIP messages correctly. (i.e., the TCP segments get reassembled into a whole message, because the SIP parser can figure out what a whole message is)</p><p>If you see this in a wireshark capture where you know you've got all the packets - for example if you generated those packets using a tool or SIP device only after starting wireshark, then there's something wrong if you see "continuation".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '14, 21:28</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-29362" class="comments-container"></div><div id="comment-tools-29362" class="comment-tools"></div><div class="clear"></div><div id="comment-29362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27110"></span>

<div id="answer-container-27110" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27110-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"continuation" is probably because Wireshark fails to reasemble the messages. What version of Wireshark are you using? It might be a bug in Wireshark or something in the message makes Wireshark fail to recognize the segments.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '13, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-27110" class="comments-container"></div><div id="comment-tools-27110" class="comment-tools"></div><div class="clear"></div><div id="comment-27110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

