+++
type = "question"
title = "wireshark mate sip 2nd or 3rd pdu filter"
description = '''I have a wireshark capture that contains a lot of sip subscribe and notify. I am using mate to do the filtering. Each gop will contain normally 4 PDUS (Subscribe-200OK, Notify-200OK). I can filter the first and last pdu of all Gops, but I would like to filter only the 2nd or 3rd pdu of all gops. Doe...'''
date = "2016-04-21T11:37:00Z"
lastmod = "2016-04-23T08:18:00Z"
weight = 51843
keywords = [ "mate" ]
aliases = [ "/questions/51843" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark mate sip 2nd or 3rd pdu filter](/questions/51843/wireshark-mate-sip-2nd-or-3rd-pdu-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51843-score" class="post-score" title="current number of votes">0</div><span id="post-51843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a wireshark capture that contains a lot of sip subscribe and notify. I am using mate to do the filtering. Each gop will contain normally 4 PDUS (Subscribe-200OK, Notify-200OK). I can filter the first and last pdu of all Gops, but I would like to filter only the 2nd or 3rd pdu of all gops. Does anyone have an idea on how I can achieve this. Is it a filter that I don't know about or some more work in the mate script?. Here is the mate script.</p><pre><code>Transform start_stop_cond {
Match (method=&quot;SUBSCRIBE&quot;) (msg_type=start);
Match (resp_code,req_method=&quot;NOTIFY&quot;) (msg_type=stop);
};

Pdu sip_pdu Proto sip Transport ip {

Extract user From sip.from.user;
Extract user From sip.to.user;
Extract user From sip.ppi.user;
Extract callid From sip.Call-ID;
Extract method From sip.Method;
Extract cseq From sip.CSeq.seq;
Extract resp_code From sip.Status-Code;
Extract req_method From sip.CSeq.method;
Transform start_stop_cond;
};

Gop sip_gop On sip_pdu Match (callid) {

Start(msg_type=start);
Stop(msg_type=stop);
};

Done;</code></pre><p>Thanks so much in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mate" rel="tag" title="see questions tagged &#39;mate&#39;">mate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '16, 11:37</strong></p><img src="https://secure.gravatar.com/avatar/6ebdd129ea651d15f7888bf94b08d791?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carlos%20Lopez&#39;s gravatar image" /><p><span>Carlos Lopez</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carlos Lopez has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Apr '16, 13:56</strong> </span></p></div></div><div id="comments-container-51843" class="comments-container"><span id="51850"></span><div id="comment-51850" class="comment"><div id="post-51850-score" class="comment-score"></div><div class="comment-text"><p>I don't know any way to filter/refer to a PDU of a particular position within a GoP. Is your example just an example or you are really interested in the 200 to the SUBSCRIBE and/or the first and mandatory NOTIFY, or you've used that message exchange just as an example?</p></div><div id="comment-51850-info" class="comment-info"><span class="comment-age">(21 Apr '16, 16:00)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="51883"></span><div id="comment-51883" class="comment"><div id="post-51883-score" class="comment-score"></div><div class="comment-text"><p>Hi Sindy. In this case I just want to check if the Notify is seen before the 200OK for Subscribe. Any idea how to filter this?. for the whole capture? I imagined that by printing the 2nd pdu for all gops I might see the issue I am looking for. Thanks.</p></div><div id="comment-51883-info" class="comment-info"><span class="comment-age">(22 Apr '16, 12:40)</span> <span class="comment-user userinfo">Carlos Lopez</span></div></div></div><div id="comment-tools-51843" class="comment-tools"></div><div class="clear"></div><div id="comment-51843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51885"></span>

<div id="answer-container-51885" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51885-score" class="post-score" title="current number of votes">1</div><span id="post-51885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Carlos Lopez has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Okay, so we've moved from a generic requirement, which was almost impossible to fulfil, to a specific one. Much easier, I tell ya :-)</p><p>My suggestion here is to forge a dedicated GoP AVP using a <code>Transform</code> in the GoP. The principle relies on the fact that the <code>Transform</code> is invoked each time when the GoP's AVPL is modified due to assignment of a new PDU to the GoP, and that the <code>Match</code> clauses within a <code>Transform</code> are only executed until the first success.</p><p>So you'd use a "flag" AVP which would be added to the GoP's AVPL when either the 200(SUBSCRIBE) or the NOTIFY arrive while this flag AVP hasn't been created yet, and the value of this AVP would be either "200" or "NOTIFY" depending on which message has caused it to be added to the GoP's AVPL.</p><p>There is another important thing, a <code>Transform</code> used in a GoP works with the AVPL of the GoP, <strong>not</strong> with the AVPLs of the newly arrived PDUs. So we have to add a single unique AVP per each PDU to the GoP's AVPL so that the GoP's <code>Transform</code> would do what we want. This effectively means that we need to forge a single AVP distinguishing the <code>200</code> response to <code>SUBSCRIBE</code> from the <code>200</code> response to <code>NOTIFY</code> at PDU level, and <code>Extra</code> it into the GoP.</p><p>So the complete code would be something like:</p><pre><code>Transform start_stop_cond {
  Match (method=&quot;SUBSCRIBE&quot;) (msg_type=start);
  Match (resp_code,req_method=&quot;NOTIFY&quot;) (msg_type=stop);
};

Transform xtract_rsp {
  Match (resp_code, req_method=&quot;SUBSCRIBE&quot;) Insert (resp_to=&quot;SUBSCRIBE&quot;);
  Match (resp_code, req_method=&quot;NOTIFY&quot;) Insert (resp_to=&quot;NOTIFY&quot;);
};

Pdu sip_pdu Proto sip Transport ip {
  Extract user From sip.from.user;
  Extract user From sip.to.user;
  Extract user From sip.ppi.user;
  Extract callid From sip.Call-ID;
  Extract method From sip.Method;
  Extract cseq From sip.CSeq.seq;
  Extract resp_code From sip.Status-Code;
  Extract req_method From sip.CSeq.method;
  Transform start_stop_cond, xtract_rsp;
};

Transform mark_it {
  Match (first_was);
  // only this rule, which doesn&#39;t change the GoP&#39;s AVPL, is executed if the first_was AVP already exists for the GoP&#39;s AVPL, ensuring that it is added only once
  Match (method=&quot;NOTIFY&quot;) Insert (first_was=&quot;NOTIFY&quot;);
  Match (resp_to=&quot;SUBSCRIBE&quot;) Insert (first_was=&quot;RSP2SUBSCRIBE&quot;);
};

Gop sip_gop On sip_pdu Match (callid) {
  Start(msg_type=start);
  Stop(msg_type=stop);
  Extra (method,resp_to);
  Transform mark_it;
};

Done;</code></pre><p><strong>EDIT:</strong> To respond the title of the question rather than the particular need, the approach actually <strong>could</strong> be generalized in terms that you could</p><ul><li><p>organize a rudimentary PDU counter in a GoP (but the <code>increment</code> function needs to be implemented manually using a <code>Transform</code>, so the processing speed would be impacted and the number of PDUs per GoP would have to be reasonably low)</p></li><li><p>save information about several PDUs of interest (e.g. the 2nd and the 3rd) for use in display filter, but as the AVPs can only be assigned constant values, not values of other AVPs, and each protocol field may only be <code>Extract</code>ed once per PDU, there is no way to e.g. store the cseq values of these messages</p></li><li><p>delete the information from each new PDU after it has been used to modify the GoP's AVPL, using a "cleanup" <code>Transform</code>. This last step may also functionally replace the PDU's own <code>Transform</code> creating the "resp_to" AVP.</p></li></ul><p>So an example of the result would look like this:</p><pre><code>Transform start_stop_cond {
  Match (method=&quot;SUBSCRIBE&quot;) (msg_type=start);
  Match (resp_code,req_method=&quot;NOTIFY&quot;) (msg_type=stop);
};

Pdu sip_pdu Proto sip Transport ip {
  Extract user From sip.from.user;
  Extract user From sip.to.user;
  Extract user From sip.ppi.user;
  Extract callid From sip.Call-ID;
  Extract method From sip.Method;
  Extract cseq From sip.CSeq.seq;
  Extract resp_code From sip.Status-Code;
  Extract req_method From sip.CSeq.method;
  Transform start_stop_cond;
};

Transform pdu_counter {
   Match (last_pdu=9) Replace (last_pdu=&quot;max&quot;);
   Match (last_pdu=8) Replace (last_pdu=9);
   Match (last_pdu=7) Replace (last_pdu=8);
   Match (last_pdu=6) Replace (last_pdu=7);
   Match (last_pdu=5) Replace (last_pdu=6);
   Match (last_pdu=4) Replace (last_pdu=5);
   Match (last_pdu=3) Replace (last_pdu=4);
   Match (last_pdu=2) Replace (last_pdu=3);
   Match (last_pdu=1) Replace (last_pdu=2);
   Match (last_pdu=&quot;max&quot;) ();
   Match () Insert (last_pdu=1);
};

Transform record_2nd {
  Match (last_pdu{1|3|4|5|6|7|8|9|&quot;max&quot;});
//skip the rest unless we&#39;re dealing with PDU number 2
  Match (method=&quot;NOTIFY&quot;) (pdu_2=&quot;NOTIFY&quot;);
  Match (resp_code,req_method=&quot;SUBSCRIBE&quot;) (pdu_2=&quot;RSP2SUBSCRIBE&quot;);
  Match () (pdu_2=&quot;OTHER&quot;);
};

Transform record_3rd {
  Match (last_pdu{1|2|4|5|6|7|8|9|&quot;max&quot;});
//skip the rest unless we&#39;re dealing with PDU number 3
  Match (method=&quot;NOTIFY&quot;) (pdu_3=&quot;NOTIFY&quot;);
  Match (resp_code,req_method=&quot;SUBSCRIBE&quot;) (pdu_3=&quot;RSP2SUBSCRIBE&quot;);
  Match () (pdu_3=&quot;OTHER&quot;);
};

Transform drop_extra {
  Match Loose (method, resp_code,req_method) Replace ();
};

Gop sip_gop On sip_pdu Match (callid) {
  Start(msg_type=start);
  Stop(msg_type=stop);
  Extra (method,resp_code,req_method);
  Transform pdu_counter,record_2nd,record_3rd,drop_extra;
};

Done;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '16, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '16, 02:40</strong> </span></p></div></div><div id="comments-container-51885" class="comments-container"><span id="51890"></span><div id="comment-51890" class="comment"><div id="post-51890-score" class="comment-score"></div><div class="comment-text"><p>Hi Sindy. Thanks a lot for your help. The result on your first proposal, I thought I had a capture which contained the notify before the 200OK for subscribe, but I didn't. then I modified the capture I have as follows: ,(exported hex capture, reversed the order in two places of the 200OK for subscribe &lt;-&gt; notify and imported back to wireshark), then added the first proposal in mate but it always inserted in the attribute of all the Gops the following:</p><pre><code>first_was: RSP2SUBSCRIBE</code></pre><p>Then I tried your 2nd proposal and I can see in the packets I reversed, the following:<br />
</p><pre><code>pdu_3: RSP2SUBSCRIBE
pdu_2: NOTIFY</code></pre><p>On those I didn't reverse the order I saw this:<br />
</p><pre><code>pdu_3: NOTIFY  
pdu_2: RSP2SUBSCRIBE</code></pre><p>Can you spot what the issue is with the first proposal?<br />
I wonder wouldn't it be a nice feature to have the pdu order/number within the gop under the number of PDUs something like: PDU: in frame: 6 (0.000001 : 0.000001).No=2, and so on.<br />
Thanks so much.</p></div><div id="comment-51890-info" class="comment-info"><span class="comment-age">(23 Apr '16, 06:17)</span> <span class="comment-user userinfo">Carlos Lopez</span></div></div><span id="51891"></span><div id="comment-51891" class="comment"><div id="post-51891-score" class="comment-score"></div><div class="comment-text"><blockquote><p>wouldn't it be a nice feature</p></blockquote><p>if you want a Wireshark feature, you can always <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi?product=Wireshark">file a bug</a> with severity "Enhancement". But be prepared that MATE is not widely popular so enhancements to it may have a very low priority.</p><blockquote><p>Can you spot what the issue is with the first proposal?</p></blockquote><p>Seemingly not without the capture, as I cannot see anything wrong in my MATE code even now. So please publish your modified capture (i.e. the one containing some NOTIFY before 200(SUBSCRIBE)) somewhere like Cloudshark (a preferred option on this site), Google Drive, Dropbox, ... and put a login-free link to it here.</p><p>Nevertheless:</p><ul><li><p>you can reach the same goal by simply removing everything related to <code>Transform record_3rd</code> from the second proposal and renaming <code>pdu_2</code> to something you like more</p></li><li><p>by debugging the first proposal yourself, you'd obtain a better understanding how MATE works.</p></li></ul><blockquote><p>I thought I had a capture which contained the notify before the 200 OK for subscribe</p></blockquote><p>I'm wondering what is the goal of the whole exercise here. Normally, the order of <strong>sending</strong> of those two messages depends on the SIP stack processing the received SUBSCRIBE, so it should be the same for all SUBSCRIBE-initiated dialogs; the order of <strong>reception</strong> of the two messages may be swapped due to the nature of the meshed packet networks (even if no packets are lost), so the issuer of the SUBSCRIBE must be prepared for such situation and shouldn't expect the two messages to come in any particular order. The sole purpose of the first NOTIFY is to inform the subscriber about the state of the subscribed object as soon as possible, not to affect the state diagram of the dialog.</p></div><div id="comment-51891-info" class="comment-info"><span class="comment-age">(23 Apr '16, 06:46)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="51892"></span><div id="comment-51892" class="comment"><div id="post-51892-score" class="comment-score"></div><div class="comment-text"><p>The issue is that the application I am working on is throwing some errors and I suspect the reception of resp and req in different order was the culprit, for sure this is a bug, but I haven't been able to probe that, at least not until now, in any case I got your first proposal and remove the extra as last step and the result looks better now. Here it is. Thanks so much for your help. I am very grateful.<br />
</p><pre><code>Transform start_stop_cond {
  Match (method=&quot;SUBSCRIBE&quot;) (msg_type=start);
  Match (resp_code,req_method=&quot;NOTIFY&quot;) (msg_type=stop);
};

Transform xtract_rsp {
  Match (resp_code, req_method=&quot;SUBSCRIBE&quot;) Insert (resp_to=&quot;SUBSCRIBE&quot;);
  Match (resp_code, req_method=&quot;NOTIFY&quot;) Insert (resp_to=&quot;NOTIFY&quot;);
};

Pdu sip_pdu Proto sip Transport ip {
  Extract user From sip.from.user;
  Extract user From sip.to.user;
  Extract user From sip.ppi.user;
  Extract callid From sip.Call-ID;
  Extract method From sip.Method;
  Extract cseq From sip.CSeq.seq;
  Extract resp_code From sip.Status-Code;
  Extract req_method From sip.CSeq.method;
  Transform start_stop_cond, xtract_rsp;
};

Transform mark_it {
  Match (first_was);
  // only this rule, which doesn&#39;t change the GoP&#39;s AVPL, is executed if the first_was AVP already exists for the GoP&#39;s AVPL, ensuring that it is added only once
  Match (method=&quot;NOTIFY&quot;) Insert (first_was=&quot;NOTIFY&quot;);
  Match (resp_to=&quot;SUBSCRIBE&quot;) Insert (first_was=&quot;RSP2SUBSCRIBE&quot;);
};

Transform rem_extra {
  Match Loose (method, resp_to) Replace ();
};

Gop sip_gop On sip_pdu Match (callid) {
  Start(msg_type=start);
  Stop(msg_type=stop);
  Extra (method,resp_to);
  Transform mark_it, rem_extra;`enter code here`
};

Done;</code></pre></div><div id="comment-51892-info" class="comment-info"><span class="comment-age">(23 Apr '16, 07:39)</span> <span class="comment-user userinfo">Carlos Lopez</span></div></div><span id="51893"></span><div id="comment-51893" class="comment"><div id="post-51893-score" class="comment-score"></div><div class="comment-text"><blockquote><p>in any case I got your first proposal and remove the extra as last step and the result looks better now</p></blockquote><p>That's quite odd, as the first proposal contains another mechanism to ensure that the <code>first_was</code> is added only once (as that mechanism seemed to me easier to understand than the "Extra, Make use of, Remove" one, maybe I was wrong?).</p><p>Normally, the "list of PDU types already encountered in the GoP" (methods and their responses) is growing with each PDU, but the <code>first_was</code> AVP should be added only once, which is <strong>either</strong> when the GoP's AVPL has been just extended with <code>method="NOTIFY"</code> <strong>or</strong> when it has been just extended with <code>resp_to="SUBSCRIBE"</code>. There is nothing in the code that could <strong>replace</strong> an existing <code>first_was</code>, so in the worst case, there should have been <strong>both</strong> <code>first_was="NOTIFY"</code> and <code>first_was="RSP2SUBSCRIBE</code> if NOTIFY has come first and the mechanism has failed.</p><p>I went so far as to use one of the subscribe-notify captures in my archive and arrange the four packets in question both ways (using <code>Export Specified Packets</code>, <code>Time Shift</code>, and <code>Merge</code>), and it worked well - if the first packet following the SUBSCRIBE is the NOTIFY, I get <code>first_was: NOTIFY</code>, otherwise I get <code>first_was: RSP2SUBSCRIBE</code>. So I keep my proposal in the Answer as it was.</p></div><div id="comment-51893-info" class="comment-info"><span class="comment-age">(23 Apr '16, 08:18)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-51885" class="comment-tools"></div><div class="clear"></div><div id="comment-51885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

