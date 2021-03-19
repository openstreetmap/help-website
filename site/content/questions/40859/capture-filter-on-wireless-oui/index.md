+++
type = "question"
title = "Capture filter on wireless OUI"
description = '''I am using Wireshark 1.12.4 on Fedora. I am trying to use a capture filter to lessen the quantity of data I am storing to disk at a customer&#x27;s site where I am logging traffic to trace an issue. They have 10 radios and I would like to capture all traffic to/from the radios and ignore everything else....'''
date = "2015-03-25T14:42:00Z"
lastmod = "2015-03-26T14:32:00Z"
weight = 40859
keywords = [ "wireless", "mac", "capture-filter", "oui" ]
aliases = [ "/questions/40859" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter on wireless OUI](/questions/40859/capture-filter-on-wireless-oui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40859-score" class="post-score" title="current number of votes">0</div><span id="post-40859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark 1.12.4 on Fedora. I am trying to use a capture filter to lessen the quantity of data I am storing to disk at a customer's site where I am logging traffic to trace an issue. They have 10 radios and I would like to capture all traffic to/from the radios and ignore everything else. This is rather trivial in the display filter as I can use</p><p>wlan.addr contains aa:bb:cc</p><p>with the OUI of the device since they are all the same vendor.</p><p>However, I'm not having luck with doing the same with a capture filter. The closest I have come is (wlan[0:4] &amp; 0xFFFFFF00) == 0xAABBCC00 as the capture filter at least turned green on input. However, when I tried this, I did not get any packets captured.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-oui" rel="tag" title="see questions tagged &#39;oui&#39;">oui</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '15, 14:42</strong></p><img src="https://secure.gravatar.com/avatar/b92c0b04e430e2315a7b256b2f3690a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shadowrider&#39;s gravatar image" /><p><span>shadowrider</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shadowrider has no accepted answers">0%</span></p></div></div><div id="comments-container-40859" class="comments-container"></div><div id="comment-tools-40859" class="comment-tools"></div><div class="clear"></div><div id="comment-40859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40866"></span>

<div id="answer-container-40866" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40866-score" class="post-score" title="current number of votes">0</div><span id="post-40866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Let's look at the BPF code of the following filter:</p><blockquote><p>wlan host aa:bb:cc:dd:ee:ff</p></blockquote><p>Run the following command to dump the BPF code</p><blockquote><p>dumpcap -d -f "wlan host aa:bb:cc:dd:ee:ff"</p></blockquote><p>Output:</p><pre><code>(000) ld       [8]
(001) jeq      #0xccddeeff      jt 2    jf 4
(002) ldh      [6]
(003) jeq      #0xaabb          jt 8    jf 4
(004) ld       [2]
(005) jeq      #0xccddeeff      jt 6    jf 9
(006) ldh      [0]
(007) jeq      #0xaabb          jt 8    jf 9
(008) ret      #262144
(009) ret      #0</code></pre><p>As you can see, this working wlan filter reads 4 or 2 bytes (ld, ldh) at different positions [8,6,2,0], which is equal 6 bytes for <strong>dst addr</strong> (starting at [0]) and 6 bytes for <strong>src addr</strong> (starting at [6]).<br />
</p><p>Now let's check your filter:</p><blockquote><p>dumpcap -d -f "(wlan[0:4] &amp; 0xFFFFFF00) == 0xAABBCC00"</p></blockquote><p>Output:</p><pre><code>(000) ld       [0]
(001) and      #0xffffff00
(002) jeq      #0xaabbcc00      jt 3    jf 4
(003) ret      #262144
(004) ret      #0</code></pre><p>Your filter reads 4 bytes (ld) at position [0], so it should at least capture frames with <strong>dst addr</strong> of aa:bb:cc:*</p><p>I guess you would need the frames with <strong>src addr</strong> aa:bb:cc:* as well, so what you need is a combination of both.</p><p><strong>Solution:</strong><br />
</p><blockquote><p>dumpcap -d -f "(wlan[0:4] &amp; 0xFFFFFF00) == 0xAABBCC00 or (wlan[6:4] &amp; 0xFFFFFF00) == 0xAABBCC00"</p></blockquote><p>Output:</p><pre><code>(000) ld       [0]
(001) and      #0xffffff00
(002) jeq      #0xaabbcc00      jt 6    jf 3
(003) ld       [6]
(004) and      #0xffffff00
(005) jeq      #0xaabbcc00      jt 6    jf 7
(006) ret      #262144
(007) ret      #0</code></pre><p>I did not test that filter, but the BPF code looks O.K., so it should work.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '15, 17:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-40866" class="comments-container"><span id="40887"></span><div id="comment-40887" class="comment"><div id="post-40887-score" class="comment-score"></div><div class="comment-text"><p>Well, it does appear to be a valid filter but when I apply it, I don't capture any packets.</p><p>I looked at the output of the generated code and see that it is different for the wireless interface vs the default. Not sure if that explains it. Here it is for both (OUI is 00:aa:bb)</p><pre><code>  $ dumpcap -i wlan4 -d -f &quot;(wlan[0:4] &amp; 0xFFFFFF00) == 0x00aabb00 or (wlan[6:4] &amp; 0xFFFFFF00) == 0x00aabb00&quot;
  Capturing on &#39;wlan4&#39;
  (000) ldb      [3]
  (001) lsh      #8
  (002) tax      
  (003) ldb      [2]
  (004) or       x
  (005) tax      
  (006) ld       [x + 0]
  (007) and      #0xffffff00
  (008) jeq      #0xaabb00        jt 12   jf 9
  (009) ld       [x + 6]
  (010) and      #0xffffff00
  (011) jeq      #0xaabb00        jt 12   jf 13
  (012) ret      #65535
  (013) ret      #0

  $ dumpcap  -d -f &quot;(wlan[0:4] &amp; 0xFFFFFF00) == 0x00aabb00 or (wlan[6:4] &amp; 0xFFFFFF00) == 0x00aabb00&quot;
  Capturing on &#39;eth0&#39;
  (000) ld       [0]
  (001) and      #0xffffff00
  (002) jeq      #0xaabb00        jt 6    jf 3
  (003) ld       [6]
  (004) and      #0xffffff00
  (005) jeq      #0xaabb00        jt 6    jf 7
  (006) ret      #65535
  (007) ret      #0</code></pre></div><div id="comment-40887-info" class="comment-info"><span class="comment-age">(26 Mar '15, 06:00)</span> <span class="comment-user userinfo">shadowrider</span></div></div><span id="40890"></span><div id="comment-40890" class="comment"><div id="post-40890-score" class="comment-score"></div><div class="comment-text"><p>Its also interesting that the code for the simple filter is quite different for the wireless interface vs the default:</p><pre><code>$ dumpcap  -i wlan4 -d -f &quot;wlan host aa:bb:cc:dd:ee:ff&quot;
Capturing on &#39;wlan4&#39;
(000) ldb      [3]
(001) lsh      #8
(002) tax      
(003) ldb      [2]
(004) or       x
(005) st       M[0]
(006) tax      
(007) ldb      [x + 0]
(008) jset     #0x4             jt 40   jf 9
(009) jset     #0x8             jt 10   jf 31
(010) ldb      [x + 1]
(011) jset     #0x2             jt 12   jf 21
(012) jset     #0x1             jt 13   jf 17
(013) ld       [x + 26]
(014) jeq      #0xccddeeff      jt 15   jf 27
(015) ldh      [x + 24]
(016) jeq      #0xaabb          jt 39   jf 27
(017) ld       [x + 18]
(018) jeq      #0xccddeeff      jt 19   jf 35
(019) ldh      [x + 16]
(020) jeq      #0xaabb          jt 39   jf 35
(021) ld       [x + 12]
(022) jeq      #0xccddeeff      jt 23   jf 25
(023) ldh      [x + 10]
(024) jeq      #0xaabb          jt 39   jf 25
(025) ldb      [x + 1]
(026) jset     #0x1             jt 27   jf 35
(027) ld       [x + 18]
(028) jeq      #0xccddeeff      jt 29   jf 40
(029) ldh      [x + 16]
(030) jeq      #0xaabb          jt 39   jf 40
(031) ld       [x + 12]
(032) jeq      #0xccddeeff      jt 33   jf 35
(033) ldh      [x + 10]
(034) jeq      #0xaabb          jt 39   jf 35
(035) ld       [x + 6]
(036) jeq      #0xccddeeff      jt 37   jf 40
(037) ldh      [x + 4]
(038) jeq      #0xaabb          jt 39   jf 40
(039) ret      #65535
(040) ret      #0

$ dumpcap  -d -f &quot;wlan host aa:bb:cc:dd:ee:ff&quot;
Capturing on &#39;eth0&#39;
(000) ld       [8]
(001) jeq      #0xccddeeff      jt 2    jf 4
(002) ldh      [6]
(003) jeq      #0xaabb          jt 8    jf 4
(004) ld       [2]
(005) jeq      #0xccddeeff      jt 6    jf 9
(006) ldh      [0]
(007) jeq      #0xaabb          jt 8    jf 9
(008) ret      #65535
(009) ret      #0</code></pre></div><div id="comment-40890-info" class="comment-info"><span class="comment-age">(26 Mar '15, 06:53)</span> <span class="comment-user userinfo">shadowrider</span></div></div><span id="40920"></span><div id="comment-40920" class="comment"><div id="post-40920-score" class="comment-score"></div><div class="comment-text"><p>Packets from "eth0" have Ethernet headers, which have a fixed length and format and have only two MAC addresses to test. Packets from "wlan4" have 802.11 headers, which have a <em>variable</em> length and format and have somewhere between two and four MAC addresses to test; that causes the code to be more complicated and, due to limitations in the BPF compiler's optimizer, require that the optimizer be disabled, so that the optimizer can't do any simplifications of the code.</p></div><div id="comment-40920-info" class="comment-info"><span class="comment-age">(26 Mar '15, 14:31)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="40921"></span><div id="comment-40921" class="comment"><div id="post-40921-score" class="comment-score"></div><div class="comment-text"><p>And the variable-length-and-format headers also mean that you have to know whether the packet has 2, 3, or 4 MAC addresses in order to know at what offsets the MAC addresses are.</p></div><div id="comment-40921-info" class="comment-info"><span class="comment-age">(26 Mar '15, 14:32)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-40866" class="comment-tools"></div><div class="clear"></div><div id="comment-40866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

