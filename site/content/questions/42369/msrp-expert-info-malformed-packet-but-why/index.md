+++
type = "question"
title = "MSRP expert Info: Malformed Packet. But why?"
description = '''Hi, I use wireshark to debug msrp traffic.  For some msg I got the following expert info: Malformed Packet (Exception occured) Severity level: Error Group: Malformed The msrp msg is fragmented into 2 segments. First segment has the malformed error. Second frame is not recognized as MSRP and only ren...'''
date = "2015-05-13T08:18:00Z"
lastmod = "2015-05-21T05:23:00Z"
weight = 42369
keywords = [ "msrp", "malformed", "packet" ]
aliases = [ "/questions/42369" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [MSRP expert Info: Malformed Packet. But why?](/questions/42369/msrp-expert-info-malformed-packet-but-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42369-score" class="post-score" title="current number of votes">0</div><span id="post-42369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I use wireshark to debug msrp traffic. For some msg I got the following expert info:</p><p>Malformed Packet (Exception occured)</p><p>Severity level: Error</p><p>Group: Malformed</p><p>The msrp msg is fragmented into 2 segments. First segment has the malformed error. Second frame is not recognized as MSRP and only rendered as TCP frame.</p><p>Problem is that the msrp data in both frames is not accessible in wireshark.</p><p>Can you see why the 1st msg is malformed and why the 2nd msg is not recognized as msrp?</p><p>Thank you</p><p>Frame 1</p><pre><code>MSRP TdNKjhyTcVJQQU74lzUcxmy5vHUZ SEND
To-Path: msrp://priv.ip.addr.rem:port/n38s00i7t0+74003;tcp
From-Path: msrp://priv.ip.addr.rem:port/cboter5ltNeG;tcp</code></pre><p>Frame 2</p><pre><code>Message-ID: b7NgfwQfPn8Jx
Success-Report: no
Failure-Report: yes
Byte-Range: 1-560/560
Content-Type: message/cpim

From: &lt;sip: [email protected]&gt;
To: &lt;sip: [email protected]&gt;
DateTime: 2015-05-13T15:04:08Z
NS: imdn &lt;urn:ietf:params:imdn&gt;
imdn.Message-ID: Hr1BCcvDlKmJRpDryyKTDJ4OZpkR
Content-Disposition: notification

Content-type: message/imdn+xml
Content-Length: 274

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;imdn xmlns=&quot;urn:ietf:params:xml:ns:imdn&quot;&gt;
  &lt;message-id&gt;MsggOfzN1UHCA&lt;/message-id&gt;
  &lt;datetime&gt;2015-05-13T15:04:08Z&lt;/datetime&gt;
  &lt;delivery-notification&gt;
    &lt;status&gt;
      &lt;delivered/&gt;
    &lt;/status&gt;
  &lt;/delivery-notification&gt;
&lt;/imdn&gt;

-------TdNKjhyTcVJQQU74lzUcxmy5vHUZ$</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-msrp" rel="tag" title="see questions tagged &#39;msrp&#39;">msrp</span> <span class="post-tag tag-link-malformed" rel="tag" title="see questions tagged &#39;malformed&#39;">malformed</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '15, 08:18</strong></p><img src="https://secure.gravatar.com/avatar/61d79b0a4b4832bea7944286ff4997fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="supisupi&#39;s gravatar image" /><p><span>supisupi</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="supisupi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '15, 08:32</strong> </span></p></div></div><div id="comments-container-42369" class="comments-container"></div><div id="comment-tools-42369" class="comment-tools"></div><div class="clear"></div><div id="comment-42369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42372"></span>

<div id="answer-container-42372" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42372-score" class="post-score" title="current number of votes">1</div><span id="post-42372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After double checking the code, it appears that MSRP dissector does not take into account TCP fragmentation. Could you fill a bug on <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a> with a sample pcap attached?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '15, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-42372" class="comments-container"><span id="42599"></span><div id="comment-42599" class="comment"><div id="post-42599-score" class="comment-score"></div><div class="comment-text"><p>Pascal, I have opened bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11217">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11217</a> with the hope that it will be fixed soon.</p><p>Thank you.</p><p>Kindest rgds,</p><p>Markus</p></div><div id="comment-42599-info" class="comment-info"><span class="comment-age">(21 May '15, 05:23)</span> <span class="comment-user userinfo">supisupi</span></div></div></div><div id="comment-tools-42372" class="comment-tools"></div><div class="clear"></div><div id="comment-42372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

