+++
type = "question"
title = "decode RPC net_logon"
description = '''Hello,  I work in a shop that uses wireshark to support a product, and we use the RPC Net_logon decode function frequently to tell if the domain controller is responding as expected. As of 1.12 this function seems to have disappeared. It is not vital for us to update to 1.12, but it would be nice to...'''
date = "2014-08-05T11:24:00Z"
lastmod = "2014-08-12T20:09:00Z"
weight = 35230
keywords = [ "decode" ]
aliases = [ "/questions/35230" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [decode RPC net\_logon](/questions/35230/decode-rpc-net_logon)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35230-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I work in a shop that uses wireshark to support a product, and we use the RPC Net_logon decode function frequently to tell if the domain controller is responding as expected. As of 1.12 this function seems to have disappeared. It is not vital for us to update to 1.12, but it would be nice to know where this useful function went.</p></div><div id="question-tags" class="tags-container tags">decode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '14, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/5115a34ce66b0260069e51c489e521ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmadsen&#39;s gravatar image" /><p>jmadsen<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmadsen has no accepted answers">0%</span></p></div></div><div id="comments-container-35230" class="comments-container"><span id="35379"></span><div id="comment-35379" class="comment"><div id="post-35379-score" class="comment-score"></div><div class="comment-text"><blockquote><p>and we use the RPC Net_logon decode function frequently to tell</p></blockquote><p>could you please add more details? Is that a function in the wireshark source code, or a display filter (if so, which one), or something totally different?</p></div><div id="comment-35379-info" class="comment-info"><span class="comment-age">(10 Aug '14, 08:24)</span> Kurt Knochner ♦</div></div><span id="35405"></span><div id="comment-35405" class="comment"><div id="post-35405-score" class="comment-score"></div><div class="comment-text"><p>Not sure if it is a function of the source code, but there used to be a way to use "decode as" to specify how you wanted RPC calls to be examined and interpreted that seems to be missing now. It may have been we were one of the few places that needed to examine RPC in detail, but it is a rather important function for us so we will be holding off on updating until we find out what happened to this function.</p></div><div id="comment-35405-info" class="comment-info"><span class="comment-age">(11 Aug '14, 06:34)</span> jmadsen</div></div><span id="35406"></span><div id="comment-35406" class="comment"><div id="post-35406-score" class="comment-score"></div><div class="comment-text"><p>can you provide a small sample capture file that works in 1.10.9 and does not work in 1.12.0? You can publish the capture file on google drive, dropbox or cloudshark.org and then post the link here.</p></div><div id="comment-35406-info" class="comment-info"><span class="comment-age">(11 Aug '14, 06:46)</span> Kurt Knochner ♦</div></div><span id="35438"></span><div id="comment-35438" class="comment"><div id="post-35438-score" class="comment-score"></div><div class="comment-text"><p>I don't think a capture would illustrate my point, so I took screen shots of both and uploaded them to better explain what I am talking about. link to screen shot of 10 with the function: <a href="http://imgur.com/NTmDQFJ,pWHGofK#0">http://imgur.com/NTmDQFJ,pWHGofK#0</a> link to screen shot of 12 without function: <a href="http://imgur.com/NTmDQFJ,pWHGofK#1">http://imgur.com/NTmDQFJ,pWHGofK#1</a> hope that helps</p></div><div id="comment-35438-info" class="comment-info"><span class="comment-age">(12 Aug '14, 11:45)</span> jmadsen</div></div></div><div id="comment-tools-35230" class="comment-tools"></div><div class="clear"></div><div id="comment-35230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35446"></span>

<div id="answer-container-35446" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35446-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There was a massive change to the "decode as" functionality.</p><blockquote><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9450">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9450</a></p></blockquote><p>Looks like the new way of "decode as" does not work properly for DCE-RPC. Please submit a notice to that bug and add as much information as possible (screenshots, link to this question, etc.)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '14, 20:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35446" class="comments-container"><span id="35451"></span><div id="comment-35451" class="comment"><div id="post-35451-score" class="comment-score"></div><div class="comment-text"><p>From the comments on the bug:</p><blockquote>5. BER and DCERPC have more opportunity to use Decode As now that they are selected based on dissector presense, not packet_info values.</blockquote><p>To get this investigated I'm almost certain the OP will have to provide a capture illustrating the issue. If the capture has sensitive information then it can be marked "private" such that only the core developers have access to it.</p><p>See the <a href="http://wiki.wireshark.org/ReportingBugs">Reporting Bugs</a> wiki page</p></div><div id="comment-35451-info" class="comment-info"><span class="comment-age">(13 Aug '14, 03:53)</span> grahamb ♦</div></div><span id="35455"></span><div id="comment-35455" class="comment"><div id="post-35455-score" class="comment-score">1</div><div class="comment-text"><p>The effect is also 'visible' with anyone of the following DCE-RPC capture files.</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures#DCE.2FRPC_and_MSRPC-based_protocols">http://wiki.wireshark.org/SampleCaptures#DCE.2FRPC_and_MSRPC-based_protocols</a></p></blockquote><p>If you select one of the DCERPC frames, and choose "Decode as", the <strong>DCE-RPC tab</strong> is missing in 1.12.x, as shown in the screenshots of the OP.</p></div><div id="comment-35455-info" class="comment-info"><span class="comment-age">(13 Aug '14, 05:36)</span> Kurt Knochner ♦</div></div><span id="35459"></span><div id="comment-35459" class="comment"><div id="post-35459-score" class="comment-score"></div><div class="comment-text"><p>Now in Bugzilla as bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10368">10368</a>.</p></div><div id="comment-35459-info" class="comment-info"><span class="comment-age">(13 Aug '14, 07:54)</span> grahamb ♦</div></div></div><div id="comment-tools-35446" class="comment-tools"></div><div class="clear"></div><div id="comment-35446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

