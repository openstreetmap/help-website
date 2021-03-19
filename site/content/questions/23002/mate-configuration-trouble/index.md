+++
type = "question"
title = "mate configuration trouble"
description = '''Hello,  I try to build a mate configuration that for a given sip call I can filter immediately on signaling and media for this call.  therefore I need to create a pdu for every sip call, make gop&#x27;s on callid where the start is the invite request line and the end the bye line.  I created a simple mat...'''
date = "2013-07-16T04:43:00Z"
lastmod = "2013-07-16T07:51:00Z"
weight = 23002
keywords = [ "mate", "sip" ]
aliases = [ "/questions/23002" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [mate configuration trouble](/questions/23002/mate-configuration-trouble)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23002-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I try to build a mate configuration that for a given sip call I can filter immediately on signaling and media for this call.</p><p>therefore I need to create a pdu for every sip call, make gop's on callid where the start is the invite request line and the end the bye line.</p><p>I created a simple mate file for this, although I don't see a single GOP being created.</p><p>Hence can somebody explain me how to debug mate configuration ?</p><pre><code>Pdu sip_pdu Proto sip Transport ip {
        Extract sip_method From sip.Request-Line;
        Extract call_id From sip.Call-ID;
        Extract conn_addr From sdp.connection_info;
        Extract conn_part From sdp.media;
};

Gop sip_call On sip_pdu Match (call_id) {
    Start (sip_method~&quot;INVITE&quot;);
    Stop (sip_method~&quot;BYE&quot;);
};

Done;</code></pre></div><div id="question-tags" class="tags-container tags">mate sip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '13, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/fa02a5bdb81d1e724dbb04b1afc0f1b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohanDemocon&#39;s gravatar image" /><p>JohanDemocon<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohanDemocon has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '13, 08:38</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23002" class="comments-container"></div><div id="comment-tools-23002" class="comment-tools"></div><div class="clear"></div><div id="comment-23002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23037"></span>

<div id="answer-container-23037" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23037-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Oof, MATE can be a pain. I've never seen the ~ operator actually used so that might be the problem. Can you try changing it to</p><p><code>Start();     Stop(never);</code></p><p>to see if you get a GOP then?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '13, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '13, 07:56</p></div></div><div id="comments-container-23037" class="comments-container"><span id="23063"></span><div id="comment-23063" class="comment"><div id="post-23063-score" class="comment-score"></div><div class="comment-text"><p>Yes then I have one. Hence you are right it's the ~ not working properly.</p></div><div id="comment-23063-info" class="comment-info"><span class="comment-age">(17 Jul '13, 01:29)</span> JohanDemocon</div></div><span id="23064"></span><div id="comment-23064" class="comment"><div id="post-23064-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-23064-info" class="comment-info"><span class="comment-age">(17 Jul '13, 01:57)</span> grahamb ♦</div></div><span id="23073"></span><div id="comment-23073" class="comment"><div id="post-23073-score" class="comment-score"></div><div class="comment-text"><p>A little digging found me this routine in mate_util.c:</p><p><code>/** * match_avp:  * @src: an src to be compared agains an "op" avp  * @op: the "op" avp that will be matched against the src avp  *  * Checks whether or not two avp's match.  *  * Return value: a pointer to the src avp if there's a match.  *  **/ extern AVP* match_avp(AVP* src, AVP* op) {</code></p><p>At the end it has this code snippet:</p><p><code>case AVP_OP_CONTAINS:                         /* TODO */                         return NULL;</code></p><p>so it appears that, yes, the ~ operator is not implemented.</p><p>I'd suggest <a href="https://bugs.wireshark.org">opening a bug</a> for that.</p></div><div id="comment-23073-info" class="comment-info"><span class="comment-age">(17 Jul '13, 08:22)</span> JeffMorriss ♦</div></div><span id="50160"></span><div id="comment-50160" class="comment"><div id="post-50160-score" class="comment-score"></div><div class="comment-text"><p>The bug opened was <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9025">bug 9025</a> and it has been <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=c913a61c742ccf98248afb5ba921464a9ee8f50a">fixed</a>, so <code>~</code> should now work.</p><p>Incidentally, in this case the <code>^</code> operator could have been used instead.</p></div><div id="comment-50160-info" class="comment-info"><span class="comment-age">(12 Feb '16, 10:52)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-23037" class="comment-tools"></div><div class="clear"></div><div id="comment-23037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

