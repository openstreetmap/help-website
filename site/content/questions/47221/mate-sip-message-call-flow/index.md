+++
type = "question"
title = "MATE - SIP MESSAGE call flow"
description = '''Hello Experts, I need your help on the Gop per SIP MESSAGE call flow. The complete SIP MESSAGE call flow is like Client ------SIP MESSAGE with sip.Call-ID=&quot;a1&quot;-----------&amp;gt; Sever (this is client sends MESSAGE) Client &amp;lt;----SIP 202 Accepted with sip.Call-ID=&quot;a1&quot;--------- Sever Client &amp;lt;----SIP ...'''
date = "2015-11-04T02:24:00Z"
lastmod = "2015-11-13T00:11:00Z"
weight = 47221
keywords = [ "mate" ]
aliases = [ "/questions/47221" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MATE - SIP MESSAGE call flow](/questions/47221/mate-sip-message-call-flow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47221-score" class="post-score" title="current number of votes">0</div><span id="post-47221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Experts,</p><p>I need your help on the Gop per SIP MESSAGE call flow.</p><p>The complete SIP MESSAGE call flow is like</p><pre><code>Client   ------SIP MESSAGE with sip.Call-ID=&quot;a1&quot;-----------&gt; Sever  (this is client sends MESSAGE)
Client   &lt;----SIP 202 Accepted with sip.Call-ID=&quot;a1&quot;--------- Sever
Client   &lt;----SIP MESSAGE with sip.Call-ID=&quot;b1&quot; and sip.In-Reply-To=&quot;a1&quot;----------- Sever (this is status report from server to Client)
Client   -----SIP 200 OK with sip.Call-ID=&quot;b1&quot;-----------&gt; Sever</code></pre><p>The question is how can use Gop to extract both transactions with either sip.In-Reply-To or sip.Status.Code?</p><pre><code>// Create a &quot;SIP-pdu&quot; that contains various pieces of the processed SIP
// message.
Pdu sip_pdu Proto sip Transport udp {
        Extract callid From sip.Call-ID;
        Extract callid From sip.In-Reply-To;
        Extract cseq_method From sip.CSeq.method;
        Extract status_code From sip.Status-Code;
};
// Then create a GOP (Group Of Pdus) where the each GOP contains all the PDUs
// (msgs) that whose call-id, sip.CSeq.seq,and sip.CSeq.method match.
Gop sip_transaction On sip_pdu Match (callid,cseq_method) {
        Start();
        Stop(never);
    // Store the result code in the GOP
    Extra(status_code);</code></pre><p>};</p><p>Done;</p></pre>Thank you so much!</div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mate" rel="tag" title="see questions tagged &#39;mate&#39;">mate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '15, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/c6d2de8ff58f1dc3175ac84d437c5931?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex%20Lu&#39;s gravatar image" /><p><span>Alex Lu</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex Lu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Nov '15, 04:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-47221" class="comments-container"></div><div id="comment-tools-47221" class="comment-tools"></div><div class="clear"></div><div id="comment-47221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47489"></span>

<div id="answer-container-47489" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47489-score" class="post-score" title="current number of votes">0</div><span id="post-47489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hmmm, I'm not sure you could get the 2 transactions (I guess you want all the transactions where sip.In-Reply-To or sip.Call-Id have the value "a1", for example) into one GoP.</p><p>To do this I think you'd need to create a GoP that contains each transaction and then a GoG (Group of Groups) that contains the 2 transactions. Something like:</p><pre><code>Gog sip_thingy {
    Member callid (call);
    Member inreplyto (call)
};</code></pre><p>(Of course your gop would need to put Call-Id and In-Reply-To into separate fields named <code>callid</code> and <code>inreplyto</code>, respectively.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '15, 17:14</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Nov '15, 18:04</strong> </span></p></div></div><div id="comments-container-47489" class="comments-container"><span id="47504"></span><div id="comment-47504" class="comment"><div id="post-47504-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jeff for the insight!</p><p>However the key here is to use sip.Call-ID as the SIP Response on 2nd part is only showing the sip.Call-Id not including the sip.In-Reply-To.</p><p>each Gop need trap sip.Call-Id and it will trigger alarm if used in multiple Gops.</p></div><div id="comment-47504-info" class="comment-info"><span class="comment-age">(10 Nov '15, 22:36)</span> <span class="comment-user userinfo">Alex Lu</span></div></div><span id="47525"></span><div id="comment-47525" class="comment"><div id="post-47525-score" class="comment-score"></div><div class="comment-text"><p>Hmm, I <em>think</em> it should work. You'll end up with 2 GoPs: one with <code>callid</code> of "a1" (and no <code>inreplyto</code>) and a 2nd with <code>callid</code> of "b1" and <code>inreplyto</code> of "a1".</p><p>The GoG will then group these 2 GoPs together because the first's <code>callid</code> matches the 2nd's <code>inreplyto</code>.</p><p>Admittedly I haven't tried it...</p></div><div id="comment-47525-info" class="comment-info"><span class="comment-age">(11 Nov '15, 18:09)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="47558"></span><div id="comment-47558" class="comment"><div id="post-47558-score" class="comment-score"></div><div class="comment-text"><p>Thanks again for the details and I will try that out.</p></div><div id="comment-47558-info" class="comment-info"><span class="comment-age">(13 Nov '15, 00:11)</span> <span class="comment-user userinfo">Alex Lu</span></div></div></div><div id="comment-tools-47489" class="comment-tools"></div><div class="clear"></div><div id="comment-47489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

