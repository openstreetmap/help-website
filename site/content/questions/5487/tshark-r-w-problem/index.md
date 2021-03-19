+++
type = "question"
title = "tshark -R -w problem"
description = '''Hello,  i try to solve one problem.  I have one capture stream taken with tshark. In this file is many VOIP calls( SIP/RTP/G729 ).  In wireshark GUI i can do what i can, but when i try filter some call from cmd is there big problem.  When i use this: tshark -r capturedfile -R &quot;ip.src==10.1.0.11&quot; -w ...'''
date = "2011-08-04T03:46:00Z"
lastmod = "2011-11-20T09:03:00Z"
weight = 5487
keywords = [ "tshark", "rtp" ]
aliases = [ "/questions/5487" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark -R -w problem](/questions/5487/tshark-r-w-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5487-score" class="post-score" title="current number of votes">0</div><span id="post-5487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>i try to solve one problem.</p><p>I have one capture stream taken with tshark. In this file is many VOIP calls( SIP/RTP/G729 ).</p><p>In wireshark GUI i can do what i can, but when i try filter some call from cmd is there big problem.</p><p>When i use this:</p><pre><code>tshark -r capturedfile -R &quot;ip.src==10.1.0.11&quot; -w call.raw</code></pre><p>I get right (SIP, UPD, TCP etc...) load in <code>call.raw</code>. But when i try to be more specific in <code>-R</code> option:</p><pre><code>tshark -r capturedfile -R &quot;ip.src==10.1.0.11 &amp;&amp; rtp.ssrc==0x3A11&quot; -w call.raw</code></pre><p>i get all load in call.raw as UDP. I need to get RTP.</p><p>I use TShark 1.6.1 on GNU/Linux CentOS 6. Please anyone have some sugestion?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '11, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/93bbd111e442fb491518c2c54e97ed53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesBorg&#39;s gravatar image" /><p><span>JamesBorg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesBorg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Aug '11, 16:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5487" class="comments-container"></div><div id="comment-tools-5487" class="comment-tools"></div><div class="clear"></div><div id="comment-5487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5492"></span>

<div id="answer-container-5492" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5492-score" class="post-score" title="current number of votes">5</div><span id="post-5492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your filter probably excluded the call-setup packets from the trace file which Wireshark uses to know when to dissect UDP as RTP. Try setting the RTP preference "Try to decode RTP outside of conversations".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '11, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-5492" class="comments-container"><span id="5494"></span><div id="comment-5494" class="comment"><div id="post-5494-score" class="comment-score"></div><div class="comment-text"><p>thanks for ansver. I try something new :</p><p>tshark -r capturefile -R "ip.src==10.1.0.12 &amp;&amp; udp.srcport==52140 &amp;&amp; ip.dst==10.1.0.11 &amp;&amp; udp.dstport==52382 &amp;&amp; rtp.ssrc==0x9B0" -d udp.port==52140,rtp -w outstream</p><p>it is now work for me, but how can i save payload of rtp from outstream? In wireshark GUI i know (telephony -&gt; rtp -&gt; show all stream -&gt; analize -&gt; save payload) Question is how can I do this in cmd?</p></div><div id="comment-5494-info" class="comment-info"><span class="comment-age">(04 Aug '11, 06:19)</span> <span class="comment-user userinfo">JamesBorg</span></div></div><span id="5497"></span><div id="comment-5497" class="comment"><div id="post-5497-score" class="comment-score"></div><div class="comment-text"><p>That's really a new question which, coincidentally, is the same as <a href="http://ask.wireshark.org/questions/5165/how-to-decode-rtp-and-save-as-raw-file-from-command-line-using-linux">this one</a>.</p></div><div id="comment-5497-info" class="comment-info"><span class="comment-age">(04 Aug '11, 06:34)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="5500"></span><div id="comment-5500" class="comment"><div id="post-5500-score" class="comment-score"></div><div class="comment-text"><p>not same, but OK:). But no ansver there :(</p></div><div id="comment-5500-info" class="comment-info"><span class="comment-age">(04 Aug '11, 07:00)</span> <span class="comment-user userinfo">JamesBorg</span></div></div><span id="5501"></span><div id="comment-5501" class="comment"><div id="post-5501-score" class="comment-score"></div><div class="comment-text"><p>OK, sorry, sounded the same to me. Anyway, I think there's no answer because it's not possible--but I don't work with RTP.</p></div><div id="comment-5501-info" class="comment-info"><span class="comment-age">(04 Aug '11, 07:07)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-5492" class="comment-tools"></div><div class="clear"></div><div id="comment-5492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7520"></span>

<div id="answer-container-7520" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7520-score" class="post-score" title="current number of votes">0</div><span id="post-7520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can concatenate raw payloads and put them in a file. Note that this will not work all the time, for example if your RTP flow contains rfc2833/4733 DTMF or DTX packets. With the RTP preference "Try to decode RTP outside of conversations" enabled, use this :</p><pre><code>tshark -n -r sip-rtp-g711a.pcap -R rtp -R &#39;rtp.ssrc == 0xd2bd4e3e&#39; -T fields -e rtp.payload | tee payloads</code></pre><p>You will see hexadecimal payloads. This output can then be converted to raw bytes using :</p><pre><code>for payload in `cat payloads`; do IFS=:; for byte in $payload; do printf &quot;\\x$byte&quot; &gt;&gt; sound.raw; done; done</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '11, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/4cc3065318bcf3043e92cc6f15c590a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guillaume%20teissier&#39;s gravatar image" /><p><span>guillaume te...</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guillaume teissier has no accepted answers">0%</span></p></div></div><div id="comments-container-7520" class="comments-container"></div><div id="comment-tools-7520" class="comment-tools"></div><div class="clear"></div><div id="comment-7520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

