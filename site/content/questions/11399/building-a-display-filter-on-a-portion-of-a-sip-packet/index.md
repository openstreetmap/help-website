+++
type = "question"
title = "Building a Display filter on a portion of a SIP packet"
description = '''I have a capture of a VoIP call showing lots of dropped packets do to jitter and wrong time stamps that occur only at the very beginning of the call - according to the WS Player - and have figured out the cause (too many packets hitting at once for the router to handle). The packets in question are ...'''
date = "2012-05-27T06:51:00Z"
lastmod = "2012-05-27T12:22:00Z"
weight = 11399
keywords = [ "sip", "display-filter" ]
aliases = [ "/questions/11399" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Building a Display filter on a portion of a SIP packet](/questions/11399/building-a-display-filter-on-a-portion-of-a-sip-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11399-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture of a VoIP call showing lots of dropped packets do to jitter and wrong time stamps that occur only at the very beginning of the call - according to the WS Player - and have figured out the cause (too many packets hitting at once for the router to handle). The packets in question are the SIP "Notify" ones with &lt;state&gt;early&lt;state&gt;\n in the "Message Body". When I build a filter on most of those packets I get this</p><p>frame[714:21] == 3c:73:74:61:74:65:3e:65:61:72:6c:79:3c:2f:73:74:61:74:65:3e:0a on others I will get this</p><p>frame[713:21] == 3c:73:74:61:74:65:3e:65:61:72:6c:79:3c:2f:73:74:61:74:65:3e:0a</p><p>or frame[715:21] == 3c:73:74:61:74:65:3e:65:61:72:6c:79:3c:2f:73:74:61:74:65:3e:0a</p><p>The only difference being at the begining.<br />
How do I build a display filter based just on the value and not on the frame location &amp; value? Btw, the file is pretty small (16sec) and I am willing to upload this but not sure how. Thanks Eric</p></div><div id="question-tags" class="tags-container tags">sip display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '12, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p>EricKnaus<br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-11399" class="comments-container"></div><div id="comment-tools-11399" class="comment-tools"></div><div class="clear"></div><div id="comment-11399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11400"></span>

<div id="answer-container-11400" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11400-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It would probably require a code change as you want to filter on the body content. What is the Content-Type: something XML? If so it's easy to add it to the xml dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '12, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-11400" class="comments-container"><span id="11401"></span><div id="comment-11401" class="comment"><div id="post-11401-score" class="comment-score"></div><div class="comment-text"><p>Thanks - I think this is what you are asking about</p><p>\n</p><p>If this is it, great although I have never done anything to the dissectors.</p></div><div id="comment-11401-info" class="comment-info"><span class="comment-age">(27 May '12, 11:15)</span> EricKnaus</div></div><span id="11402"></span><div id="comment-11402" class="comment"><div id="post-11402-score" class="comment-score"></div><div class="comment-text"><p>"&lt;?xml version="1.0"?&gt;\n"</p></div><div id="comment-11402-info" class="comment-info"><span class="comment-age">(27 May '12, 11:17)</span> EricKnaus</div></div><span id="11411"></span><div id="comment-11411" class="comment"><div id="post-11411-score" class="comment-score"></div><div class="comment-text"><p>No, as an exaple when the body contains SDP there is this line Content-Type: application/sdp What is the Content-Type: in your case?</p></div><div id="comment-11411-info" class="comment-info"><span class="comment-age">(27 May '12, 13:39)</span> Anders ♦</div></div></div><div id="comment-tools-11400" class="comment-tools"></div><div class="clear"></div><div id="comment-11400-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11406"></span>

<div id="answer-container-11406" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11406-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Can you please try one of these filters (depends on the protocol):</p><blockquote><p><code>sip contains 3c:73:74:61:74:65:3e:65</code><br />
<code>rtp contains 3c:73:74:61:74:65:3e:65</code><br />
<code>rtp.payload contains 3c:73:74:61:74:65:3e:65</code><br />
</p></blockquote><p>more general</p><blockquote><p><code>udp contains 3c:73:74:61:74:65:3e:65</code><br />
<code>tcp contains 3c:73:74:61:74:65:3e:65</code><br />
<code>ip contains 3c:73:74:61:74:65:3e:65</code><br />
</p></blockquote><p>Change the HEX string to whatever you need.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '12, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 May '12, 12:28</p></div></div><div id="comments-container-11406" class="comments-container"></div><div id="comment-tools-11406" class="comment-tools"></div><div class="clear"></div><div id="comment-11406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

