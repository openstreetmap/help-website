+++
type = "question"
title = "How to group subscribe-notify SIP messages?"
description = '''Hi All, I am new wireshark and SIP user :). I want to know that is there some way I can group all the SUBSCRIBE-NOTIFY messages and find response times of NOTIFY for the SUBSCRIBE. What I already tried is that I added CallId as column and sorted, this apparently shows the related SUBSCRIBE/200/NOTIF...'''
date = "2016-02-16T22:55:00Z"
lastmod = "2016-02-22T08:16:00Z"
weight = 50252
keywords = [ "subscribe", "sip", "notify" ]
aliases = [ "/questions/50252" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to group subscribe-notify SIP messages?](/questions/50252/how-to-group-subscribe-notify-sip-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50252-score" class="post-score" title="current number of votes">0</div><span id="post-50252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am new wireshark and SIP user :). I want to know that is there some way I can group all the SUBSCRIBE-NOTIFY messages and find response times of NOTIFY for the SUBSCRIBE.</p><p>What I already tried is that I added CallId as column and sorted, this apparently shows the related SUBSCRIBE/200/NOTIFY together. Then there's response time in 200, I added that also as the column, now I can see the response time of 200 but still for Notify I need to manually calculate. See image.<img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_hFcJ1Bv.jpg" alt="alt text" /></p><p>I think flow view can do that but I am testing it from single machine using SIPP therefore the flow, UDP stream shows all the traffic together.</p><p>I can provide the sample pcap too if required.</p><p>Thanks, Surya</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-subscribe" rel="tag" title="see questions tagged &#39;subscribe&#39;">subscribe</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-notify" rel="tag" title="see questions tagged &#39;notify&#39;">notify</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '16, 22:55</strong></p><img src="https://secure.gravatar.com/avatar/e617c0f91dbd05d376e67b3e86d9520f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="suryaveer&#39;s gravatar image" /><p><span>suryaveer</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="suryaveer has no accepted answers">0%</span></p></img></div></div><div id="comments-container-50252" class="comments-container"></div><div id="comment-tools-50252" class="comment-tools"></div><div class="clear"></div><div id="comment-50252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50256"></span>

<div id="answer-container-50256" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50256-score" class="post-score" title="current number of votes">0</div><span id="post-50256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could use <a href="https://wiki.wireshark.org/Mate">MATE</a> for this purpose, grouping the SUBSCRIBE, NOTIFY, and their relevant 200s by <code>sip.Call-ID</code> and calculating the response time as a difference of the <code>frame.time_epoch</code> fields of the two requests, but I'm sure that use of SIPP's own tools for the purpose will require much less initial effort.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '16, 00:58</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50256" class="comments-container"><span id="50276"></span><div id="comment-50276" class="comment"><div id="post-50276-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer. I understand SIPP already provide this feature and I am using that but in SIPP I am noticing really high response times, therefore, I just want to verify when the message enters the presence server and when the response leaves.</p></div><div id="comment-50276-info" class="comment-info"><span class="comment-age">(17 Feb '16, 10:09)</span> <span class="comment-user userinfo">suryaveer</span></div></div><span id="50289"></span><div id="comment-50289" class="comment"><div id="post-50289-score" class="comment-score"></div><div class="comment-text"><p>Need help!! I tried something but don't know what exactly I did and what to do next.</p><pre><code>Pdu sip_pdu Proto sip Transport ip {
    Extract call_id From sip.Call-ID ;
};
Gop sip On sip_pdu Match (call_id) {
Start(method {&quot;SUBSCRIBE&quot;|&quot;NOTIFY&quot;});
Stop(never);
};</code></pre><p>This added a new MATE tree in packet details view as:</p><pre><code>MATE sip_pdu:9
--sip_pdu:9
----sip_pdu time: 39.9063
----sip_pdu Attributes
-------call_id: 1-123</code></pre></div><div id="comment-50289-info" class="comment-info"><span class="comment-age">(17 Feb '16, 19:44)</span> <span class="comment-user userinfo">suryaveer</span></div></div><span id="50292"></span><div id="comment-50292" class="comment"><div id="post-50292-score" class="comment-score"></div><div class="comment-text"><p>Sorry for</p><blockquote><p>calculating the response time as a difference of the frame.time_epoch fields of the two requests</p></blockquote><p>This is actually something MATE does for you automatically.</p><p>I <em>think</em> you forgot to</p><pre><code>Extract method From sip.Method ;</code></pre><p>so the <code>Start</code> has nothing to catch on.</p><p>(but please do <em>not</em> add the <code>method</code> to the <code>Gop sip On...</code>)</p><p>The next thing you need to do is to change your <code>Start</code> and <code>Stop</code> clauses the following way:</p><pre><code>Start(method {&quot;SUBSCRIBE&quot;});
Stop(method {&quot;NOTIFY&quot;});</code></pre><p>If you do that, MATE will create for you (among others) an item <code>mate.sip.Duration</code> in the tree, containing the time elapsed between the SUBSCRIBE (<code>Start</code>) and NOTIFY (<code>Stop</code>) messages.</p><p>So to see the round-trip times in Wireshark, you should be able to make <code>mate.sip.Duration</code> a column in the packet list, and by applying a display filter</p><pre><code>sip.Method == &quot;NOTIFY&quot;</code></pre><p>you would display only the frames carrying the NOTIFY.</p><p>For tshark, you should be able to use</p><pre><code>-Y &quot;sip.Method = \&quot;NOTIFY\&quot;&quot; -T fields -e mate.sip.Duration</code></pre><p>to output <em>only</em> the response times, so that you could then use some post-processing to analyze them.</p><p>Be aware that things go confusing very quickly if your capture contains more than a single NOTIFY per each SUBSCRIBE; you would have to add additional conditions to the display filter so that the proper (i.e. the first) NOTIFY packets would be displayed, such as <code>sip.CSeq.seq == 1</code> if your server numbers CSeq from 1 in each dialog.</p></div><div id="comment-50292-info" class="comment-info"><span class="comment-age">(17 Feb '16, 22:16)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="50315"></span><div id="comment-50315" class="comment"><div id="post-50315-score" class="comment-score"></div><div class="comment-text"><p>OK, so one more correction after I've found a minute to check it. The distance between the <code>SUBSCRIBE</code> and the first <code>NOTIFY</code> is the <code>mate.sip.Time</code> (displayed in the MATE tree as "sip <em>hold</em> time").</p><p>There is a difference in behaviour between Wireshark and tshark:</p><ul><li><p>in Wireshark, the <code>sip.mate.Time</code> is shown already in the SUBSCRIBE (both in packet dissection pane and packet list pane if added there as column);</p></li><li><p>in tshark's output, it is not shown until the first NOTIFY is processed; to my surprise, use of <code>-2</code> (two-pass analysis) has caused it to not to be shown at all instead of causing it to be shown already for the SUBSCRIBE.</p></li></ul><p>The idea was to use <code>-Y "sip.Method == SUBSCRIBE"</code> rather than <code>-Y "sip.Method == NOTIFY and sip.CSeq.seq == 1</code> to output a single <code>sip.mate.Time</code> value per dialog but it has failed.</p></div><div id="comment-50315-info" class="comment-info"><span class="comment-age">(18 Feb '16, 13:43)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="50362"></span><div id="comment-50362" class="comment"><div id="post-50362-score" class="comment-score"></div><div class="comment-text"><p><span>@sindy</span> Hey, thanks. I didn't get a notification so totally missed this. I'll try this and get back.</p></div><div id="comment-50362-info" class="comment-info"><span class="comment-age">(19 Feb '16, 18:18)</span> <span class="comment-user userinfo">suryaveer</span></div></div><span id="50407"></span><div id="comment-50407" class="comment not_top_scorer"><div id="post-50407-score" class="comment-score"></div><div class="comment-text"><p>As what tshark does (no MATE fields are output at all if you use <code>-2</code>) seems to be a regression preventing you from displaying the <code>mate.sip.Time</code> for the SUBSCRIBE packet, the workaround to display that field only once per each dialog if more than one NOTIFY packet belongs to a dialog is to use the following display filter:</p><p><code>-Y "sip.Method == \"NOTIFY\" and mate.sip_pdu.TimeInGop == mate.sip.Time"</code></p></div><div id="comment-50407-info" class="comment-info"><span class="comment-age">(22 Feb '16, 08:16)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-50256" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-50256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

