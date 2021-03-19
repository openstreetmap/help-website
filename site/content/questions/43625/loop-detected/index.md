+++
type = "question"
title = "Loop Detected"
description = '''Hello What does SIP Loop Detected Error means? And how can i avoid it?'''
date = "2015-06-28T04:08:00Z"
lastmod = "2015-06-29T02:16:00Z"
weight = 43625
keywords = [ "sip" ]
aliases = [ "/questions/43625" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Loop Detected](/questions/43625/loop-detected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43625-score" class="post-score" title="current number of votes">0</div><span id="post-43625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>What does SIP Loop Detected Error means? And how can i avoid it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '15, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/f584c012804be160102179efb69191f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hayasb&#39;s gravatar image" /><p><span>hayasb</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hayasb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jun '15, 09:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-43625" class="comments-container"><span id="43626"></span><div id="comment-43626" class="comment"><div id="post-43626-score" class="comment-score"></div><div class="comment-text"><p>Are you sure that's SIP? Can you share a capture somewhere public, or at least post a screenshot of capture with the packet showing the error?</p></div><div id="comment-43626-info" class="comment-info"><span class="comment-age">(28 Jun '15, 04:22)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43627"></span><div id="comment-43627" class="comment"><div id="post-43627-score" class="comment-score"></div><div class="comment-text"><p>Please refer to the attached screenshot<img src="https://osqa-ask.wireshark.org/upfiles/Loop_Detected.PNG" alt="alt text" /></p></div><div id="comment-43627-info" class="comment-info"><span class="comment-age">(28 Jun '15, 04:25)</span> <span class="comment-user userinfo">hayasb</span></div></div></div><div id="comment-tools-43625" class="comment-tools"></div><div class="clear"></div><div id="comment-43625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43628"></span>

<div id="answer-container-43628" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43628-score" class="post-score" title="current number of votes">0</div><span id="post-43628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As per the relevant RFC (<a href="https://www.ietf.org/rfc/rfc3261.txt">3261</a>):</p><blockquote><p>21.4.20 482 Loop Detected</p><p>The server has detected a loop (Section 16.3 Item 4).</p><p>4 Optional Loop Detection check</p><pre><code>  An element MAY check for forwarding loops before forwarding a
  request.  If the request contains a Via header field with a sent-
  by value that equals a value placed into previous requests by the
  proxy, the request has been forwarded by this element before.  The
  request has either looped or is legitimately spiraling through the
  element.  To determine if the request has looped, the element MAY
  perform the branch parameter calculation described in Step 8 of
  Section 16.6 on this message and compare it to the parameter
  received in that Via header field.  If the parameters match, the
  request has looped.  If they differ, the request is spiraling, and
  processing continues.  If a loop is detected, the element MAY
  return a 482 (Loop Detected) response.</code></pre></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '15, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jun '15, 04:56</strong> </span></p></div></div><div id="comments-container-43628" class="comments-container"><span id="43629"></span><div id="comment-43629" class="comment"><div id="post-43629-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the information.</p><p>Now I had disabled the proxy server from my pc and connecting directly to the internet but still get this error!!</p></div><div id="comment-43629-info" class="comment-info"><span class="comment-age">(28 Jun '15, 05:03)</span> <span class="comment-user userinfo">hayasb</span></div></div><span id="43630"></span><div id="comment-43630" class="comment"><div id="post-43630-score" class="comment-score"></div><div class="comment-text"><p>It's hard to know the precise culprit when we can only see the packet list snapshot instead of the actual packet details, but there's one thing that's visibly wrong:</p><p>Look at the target request URI of the REGISTER request message - i.e., the "sip:188.247.67.90" - that identifies the ultimate target of the request. But "188.247.67.90" is the same IP Address as the sender of the message to begin with - in other words, the host 188.247.67.90 is sending the REGISTER message with a SIP destination of 188.247.67.90, so it's no wonder a loop is detected. My guess is that on the 188.247.67.90 computer/phone, you have the Registrar, Registrar Domain, or Address-of-Record set incorrectly.</p></div><div id="comment-43630-info" class="comment-info"><span class="comment-age">(28 Jun '15, 08:58)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="43638"></span><div id="comment-43638" class="comment"><div id="post-43638-score" class="comment-score"></div><div class="comment-text"><p>I followed the UDP stream and got the below result; To and from are using the same IP Address. I am using inGate Siparator as DMZ/LAN but don't know what am missing!!:</p><pre><code>REGISTER sip:188.247.67.90;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 10.179.128.228:49012;branch=z9hG4bK-524287-1---3d15be2bf3d75655;rport
Max-Forwards: 70
Contact: &lt;sip:[email protected]:49012;rinstance=24fc7df247922ed7;transport=UDP&gt;
To: &quot;203&quot;&lt;sip:[email protected];transport=UDP&gt;
From: &quot;203&quot;&lt;sip:[email protected];transport=UDP&gt;;tag=88f9ff4d
Call-ID: 9M-KyvmjzBrGB4TqI3H5Fg..
CSeq: 1 REGISTER
Expires: 60
Allow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE
Supported: replaces, norefersub, extended-refer, timer, outbound, path, X-cisco-serviceuri
User-Agent: Zoiper r30911
Allow-Events: presence, kpml
Content-Length: 0

SIP/2.0 482 Loop Detected
Via: SIP/2.0/UDP 10.179.128.228:49012;branch=z9hG4bK-524287-1---3d15be2bf3d75655;received=188.247.77.83;rport=33785
From: &quot;203&quot;&lt;sip:[email protected];transport=UDP&gt;;tag=88f9ff4d
Call-ID: 9M-KyvmjzBrGB4TqI3H5Fg..
CSeq: 1 REGISTER
To: &quot;203&quot;&lt;sip:[email protected];transport=UDP&gt;;tag=488579bf366f69151236
Server: SIParator/5.0.5
Content-Length: 0</code></pre></div><div id="comment-43638-info" class="comment-info"><span class="comment-age">(28 Jun '15, 12:35)</span> <span class="comment-user userinfo">hayasb</span></div></div></div><div id="comment-tools-43628" class="comment-tools"></div><div class="clear"></div><div id="comment-43628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43640"></span>

<div id="answer-container-43640" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43640-score" class="post-score" title="current number of votes">0</div><span id="post-43640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Presumably your comment meant to show this:</p><pre><code>REGISTER sip:188.247.67.90;transport=UDP SIP/2.0
Via: SIP/2.0/UDP 10.179.128.228:49012;branch=z9hG4bK-524287-1---3d15be2bf3d75655;rport
Max-Forwards: 70
Contact: sip:[email protected]:49012;rinstance=24fc7df247922ed7;transport=UDP
To: &quot;203&quot;sip:[email protected];transport=UDP
From: &quot;203&quot;sip:[email protected];transport=UDP;tag=88f9ff4d
Call-ID: 9M-KyvmjzBrGB4TqI3H5Fg..
CSeq: 1 REGISTER
Expires: 60
Allow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE
Supported: replaces, norefersub, extended-refer, timer, outbound, path, X-cisco-serviceuri
User-Agent: Zoiper r30911
Allow-Events: presence, kpml
Content-Length: 0

SIP/2.0 482 Loop Detected
Via: SIP/2.0/UDP 10.179.128.228:49012;branch=z9hG4bK-524287-1---3d15be2bf3d75655;received=188.247.77.83;rport=33785
From: &quot;203&quot;sip:[email protected];transport=UDP;tag=88f9ff4d
Call-ID: 9M-KyvmjzBrGB4TqI3H5Fg..
CSeq: 1 REGISTER
To: &quot;203&quot;sip:[email protected];transport=UDP;tag=488579bf366f69151236
Server: SIParator/5.0.5
Content-Length: 0</code></pre><p>Are those the contents of the same capture file you showed a screenshot of?</p><p>It doesn't look like it would be the same messages, but if it is that's even more confusing... because the IP layer shown in the screenshot showed the IP source address of 188.247.67.90 and destination address of 192.168.0.113 (in the third and fourth columns). Or are your columns reversed? What exactly are the IP source and destination addresses of the SIP message contents shown above (not the SIP-layer info, but the IP-layer info).</p><p>I was assuming the IP source was 188.247.67.90, sending a SIP REGISTER request message to 192.168.0.113, but with a SIP request URI of "<code>sip:188.247.67.90;transport=tcp</code>". That would cause a loop, because when the SIP device on 192.168.0.113 receives it, it will want to forward it right back to 188.247.67.90 (although it may not be a loop if it forwards it to a different TCP/UDP port, but I'll ignore that detail for now).</p><p>The "To" and the "From" headers don't actually decide how SIP messages are "routed" at the SIP layer (despite the words "To" and "From" sounding like they should). For SIP request messages, such as the REGISTER request, the "request URI" is what decides the ultimate target (along with any "Route" headers, but you don't have those). The request URI is the string "sip:188.247.67.90;transport=UDP" right after the word "REGISTER", the first line of the SIP message. The "To" header URI in a REGISTER request identifies the address-of-record being registered for, and the "From" header URI in a REGISTER request identifies the entity performing the registration - usually the same as the "To" header URI, except for third-party registrations (which does not apply to your case).</p><p>I don't know the inGate Siparator, but presumably it's a SIP ALG, such that it will replace various SIP headers to make it work though NATs and hide internal addressing. So to figure out what's going wrong we might need a capture of both the "inside" and "outside" packets - i.e., the ones sent to/from the Zoiper soft phone to the inGate, and the ones sent to/from the inGate and the SIP service provider.</p><p>But as I said before, you probably didn't configure your SIP phone correctly (the Zoiper softphone). For a Zoiper, there's a "Account Wizard" dialog box that shows up when you create the SIP account - what did you set the "<span class="__cf_email__" data-cfemail="c0b5b3a5b280a8afb3b4">[email protected]</span>" field and "domain/outbound proxy" fields to? My guess is one of those two is not set correctly. It looks like you set one of them to "188.247.67.90", when it should instead be the domain name of your SIP service provider.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '15, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43640" class="comments-container"><span id="43654"></span><div id="comment-43654" class="comment"><div id="post-43654-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>Tha configuration am doing is as the attached image.</p><p>The idea of it is remote sip extension can able to connect to the pbx without vpn connection. So 188.247.67.90 is the company public IP address. The 1st capture was trying to connect from laptop through wifi connection the other one is connected from mobile phone through data plan in both cases it gave loop detected.</p><p>So what you are suggesting is entering public ip address in the domain and the outbound proxy enter the sip domain for the pbx?<img src="https://osqa-ask.wireshark.org/upfiles/inage.PNG" alt="alt text" /></p></div><div id="comment-43654-info" class="comment-info"><span class="comment-age">(29 Jun '15, 02:16)</span> <span class="comment-user userinfo">hayasb</span></div></div></div><div id="comment-tools-43640" class="comment-tools"></div><div class="clear"></div><div id="comment-43640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

