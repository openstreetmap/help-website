+++
type = "question"
title = "Wireshark MATE correlation multiple GOPs"
description = '''Hi Experts, I want to correlate multiple GoPs based on certain attribute from each PDU. How can I build a logic using MATE scenario (e.g) SIP packet which has media port information H248 packet which also has media port information I want to group SIP and H248 packet where the media port is of same ...'''
date = "2015-09-14T15:55:00Z"
lastmod = "2015-09-21T17:53:00Z"
weight = 45835
keywords = [ "mate", "sip", "rtp", "correlation" ]
aliases = [ "/questions/45835" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark MATE correlation multiple GOPs](/questions/45835/wireshark-mate-correlation-multiple-gops)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45835-score" class="post-score" title="current number of votes">0</div><span id="post-45835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>I want to correlate multiple GoPs based on certain attribute from each PDU. How can I build a logic using MATE</p><p>scenario (e.g) SIP packet which has media port information H248 packet which also has media port information</p><p>I want to group SIP and H248 packet where the media port is of same value</p><p>BR, sshark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mate" rel="tag" title="see questions tagged &#39;mate&#39;">mate</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-correlation" rel="tag" title="see questions tagged &#39;correlation&#39;">correlation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '15, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/4a2a1ab8f8fa05aa1d21e5b43f767aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sshark&#39;s gravatar image" /><p><span>sshark</span><br />
<span class="score" title="6 reputation points">6</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sshark has no accepted answers">0%</span></p></div></div><div id="comments-container-45835" class="comments-container"></div><div id="comment-tools-45835" class="comment-tools"></div><div class="clear"></div><div id="comment-45835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45852"></span>

<div id="answer-container-45852" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45852-score" class="post-score" title="current number of votes">1</div><span id="post-45852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you want to correlate multiple GoPs or create a new GoP which contains the SIP and H248 packets?</p><p>If the former then you want to <a href="https://wiki.wireshark.org/Mate/Manual#Telling_MATE_what_could_be_a_Gog_member">create a Group of Groups</a>. In that example <code>host</code> is what ties the GoPs together (obviously both GoPs would need a <code>host</code> field).</p><p>If the latter then, well, just create another GoP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '15, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Feb '16, 13:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-45852" class="comments-container"><span id="45853"></span><div id="comment-45853" class="comment"><div id="post-45853-score" class="comment-score"></div><div class="comment-text"><p>I would be happy if a GoG serves my purpose. Pls refer the attached mate config example. I am having issues or confusion on how to compare two attributes</p><ol><li>Within GoG, how can I compare mport of Megaco PDU and mport of SIP PDU (does it match one to one)</li><li><p>When I use this value, for some SIP packets, I get below error in wireshark when I open a capture file Expert Info (Error/Malformed): proto.c:3487: field mate.released_time is not of type FT_FLOAT</p><p>Pdu sip_pdu Proto sip Transport ip {</p><pre><code>Extract user From sip.From;
Extract user From sip.To;
Extract user From sip.P-Asserted-Identity;
Extract user From sip.P-Served-User;
Extract callid From sip.Call-ID;
Extract method From sip.Method;
Extract mport From sdp.media.port;</code></pre><p>};</p><p>Gop sipp On sip_pdu Match (callid) {</p><pre><code>Start(method {&quot;INVITE&quot;|&quot;REGISTER&quot;|&quot;MESSAGE&quot;|&quot;BYE&quot;|&quot;CANCEL&quot;|&quot;PRACK&quot;|&quot;SUBSCRIBE&quot;|&quot;NOTIFY&quot;});
Stop(never);

// Store the user in the GOP
Extra(user,mport);</code></pre><p>};</p><p>Pdu megaco_pdu Proto megaco Transport sctp {</p><pre><code>Extract mgtrans From megaco.transid;
Extract taction From megaco.transaction;
Extract mport From sdp.media.port;</code></pre><p>};</p><p>Gop mco On megaco_pdu Match (mgtrans) {</p><pre><code>Start(taction=&quot;Request&quot;);
Stop(taction=&quot;Reply&quot;);
Extra(mport);</code></pre><p>};</p><p>Gog tester {</p><pre><code>Member sipp(user);
Member mco (mport);

Extra(user);</code></pre><p>};</p><p>Done;</p></li></ol></div><div id="comment-45853-info" class="comment-info"><span class="comment-age">(15 Sep '15, 07:16)</span> <span class="comment-user userinfo">sshark</span></div></div><span id="45856"></span><div id="comment-45856" class="comment"><div id="post-45856-score" class="comment-score"></div><div class="comment-text"><p>(FYI I converted your Answer to a Comment--see the FAQ.)</p><p>For (1), yes, you'd need to put mport in both the <code>sipp</code> and <code>mco</code> lines to get MATE to include only GoPs whose mport match. I'm not sure what you mean by "one for one": if the mport is equal then the GoP will be included.</p><p>For (2): that's a bug in Wireshark. I submitted <a href="https://code.wireshark.org/review/10537">a change</a> to have that fixed.</p></div><div id="comment-45856-info" class="comment-info"><span class="comment-age">(15 Sep '15, 08:00)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="45942"></span><div id="comment-45942" class="comment"><div id="post-45942-score" class="comment-score"></div><div class="comment-text"><p>So, do you think - this should be a valid configuration for my purpose My actual display filter would be - mate.tester.user == xyz to filter all related SIP &amp; H248 packets</p><pre><code>Pdu sip_pdu Proto sip Transport ip {

Extract user From sip.From;
Extract user From sip.To;
Extract user From sip.P-Asserted-Identity;
Extract user From sip.P-Served-User;
Extract callid From sip.Call-ID;
Extract method From sip.Method;
Extract mport From sdp.media.port;
};

Gop sipp On sip_pdu Match (callid) {

Start(method {&quot;INVITE&quot;|&quot;REGISTER&quot;|&quot;MESSAGE&quot;|&quot;BYE&quot;|&quot;CANCEL&quot;|&quot;PRACK&quot;|&quot;SUBSCRIBE&quot;|&quot;NOTIFY&quot;});
Stop(never);

// Store the user in the GOP
Extra(user,mport);
};

Pdu megaco_pdu Proto megaco Transport sctp {

Extract mgtrans From megaco.transid;
Extract taction From megaco.transaction;
Extract mport From sdp.media.port;
};

Gop mco On megaco_pdu Match (mgtrans) {

Start(taction=&quot;Request&quot;);
Stop(taction=&quot;Reply&quot;);
Extra(mport);
};

Gog tester {

Member sipp(user,mport);
Member mco (mport);

Extra(user);
};

Done;</code></pre></div><div id="comment-45942-info" class="comment-info"><span class="comment-age">(18 Sep '15, 01:26)</span> <span class="comment-user userinfo">sshark</span></div></div><span id="45950"></span><div id="comment-45950" class="comment"><div id="post-45950-score" class="comment-score"></div><div class="comment-text"><p>That looks about right. I'm not sure about the "user" part in this line:</p><pre><code>Member sipp(user,mport);</code></pre><p>I suspect that might break things but who knows...</p></div><div id="comment-45950-info" class="comment-info"><span class="comment-age">(18 Sep '15, 10:48)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="45961"></span><div id="comment-45961" class="comment"><div id="post-45961-score" class="comment-score"></div><div class="comment-text"><p>Ok, user is needed as I have to filter the trace based on user and not based on media port.</p><p>Above works, except the mate.released_time related error I reported before</p><p>One last question - I do have some megaco packets before the initial SIP packet, hence I could not get those megaco packets as I could not match the mport. Is it possible to process PDUs/GoPs in reverse direction or after certain PDUs are processed ?</p></div><div id="comment-45961-info" class="comment-info"><span class="comment-age">(19 Sep '15, 05:49)</span> <span class="comment-user userinfo">sshark</span></div></div><span id="46042"></span><div id="comment-46042" class="comment not_top_scorer"><div id="post-46042-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Ok, user is needed as I have to filter the trace based on user and not based on media port.</p></blockquote><p>Hmm, I thought that would be covered by the "Extra(user)" part rather than the "Member" part. But then again I'm not sure I've ever used a GoG in anger.</p><blockquote><p>Above works, except the mate.released_time related error I reported before</p></blockquote><p>Excellent. If you pick up an automated build then that error will go away (the change was merged).</p><p>For your last question: I actually would have thought it would have worked like that today since the <code>mco</code> is matching based on <code>transid</code> not <code>mport</code>. IOW the <code>mco</code> will contain all <code>megaco_pdu</code>s with the same <code>transid</code> regardless of the <code>mport</code> value and whether there's been SIP signaling before. Then <code>tester</code> will contain an <code>mco</code> and a <code>sipp</code>.</p></div><div id="comment-46042-info" class="comment-info"><span class="comment-age">(21 Sep '15, 17:53)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-45852" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-45852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

