+++
type = "question"
title = "Unable to capture UDP scan packets"
description = '''Hi all, I am trying to inject udp scan packets from Kali box to target machine using following command. root@kalilinux#nc -unvv -w 1 -z &amp;lt;ip address=&quot;&quot;&amp;gt; &amp;lt;port&amp;gt; nc:&amp;lt;ip address=&quot;&quot;&amp;gt; &amp;lt;port&amp;gt; is open nc:using datagram socket The scan is successful but i am not able to see the packet...'''
date = "2014-05-08T11:23:00Z"
lastmod = "2014-05-12T15:59:00Z"
weight = 32648
keywords = [ "port-scanning" ]
aliases = [ "/questions/32648" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to capture UDP scan packets](/questions/32648/unable-to-capture-udp-scan-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32648-score" class="post-score" title="current number of votes">0</div><span id="post-32648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I am trying to inject udp scan packets from Kali box to target machine using following command.</p><p><span class="__cf_email__" data-cfemail="0775686873476c666b6e6b6e69727f">[email protected]</span>#nc -unvv -w 1 -z &lt;ip address=""&gt; &lt;port&gt;</p><p>nc:&lt;ip address=""&gt; &lt;port&gt; is open nc:using datagram socket</p><p>The scan is successful but i am not able to see the packets on Wireshark running on Kali. Whereas able to see TCP connectscan packets.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-port-scanning" rel="tag" title="see questions tagged &#39;port-scanning&#39;">port-scanning</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '14, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-32648" class="comments-container"><span id="32739"></span><div id="comment-32739" class="comment"><div id="post-32739-score" class="comment-score"></div><div class="comment-text"><p>No bridging. Same Host.</p><p>On tgt [<span class="__cf_email__" data-cfemail="5c2e3333281c30333f3d3034332f28">[email protected]</span> ~]# ifconfig</p><p><strong><em>**eth0 Link encap:Ethernet HWaddr</em></strong>**</p><pre><code>      inet addr:A.B.C.D  Bcast:A.B.C.E  Mask:255.255.255.0</code></pre><p>On Kali initiator</p><p>[<span class="__cf_email__" data-cfemail="4f3d20203b0f23202c2e2327203c3b">[email protected]</span> ~]# ifconfig</p><p><strong>eth0 Link encap:Ethernet HWaddr</strong><br />
</p><pre><code>      inet addr:A.B.C.G  Bcast:A.B.C.E  Mask:255.255.255.0</code></pre></div><div id="comment-32739-info" class="comment-info"><span class="comment-age">(12 May '14, 15:59)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div></div><div id="comment-tools-32648" class="comment-tools"></div><div class="clear"></div><div id="comment-32648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32673"></span>

<div id="answer-container-32673" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32673-score" class="post-score" title="current number of votes">0</div><span id="post-32673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As you did not mention the important things, I'm going to guess....</p><p>1.) Did you send the traffic to the <strong>same system</strong> (localhost)?</p><p>If so, you won't see that traffic on eth0/eth1/ethx. Instead you should capture on the <strong>loopback interface:</strong> lo</p><p>2.) Did you send the traffic to <strong>another system</strong>, via the LAN interface?</p><p>If so: <strong>Where and how exactly</strong> did you try to capture the traffic?</p><p>3.) Do you see the traffic, if you capture with tcpdump?</p><blockquote><p>tcpdump -ni eth0 udp port 8888</p></blockquote><p>Please replace 8888 with whatever port you are using in your test.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '14, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 May '14, 11:34</strong> </span></p></div></div><div id="comments-container-32673" class="comments-container"><span id="32713"></span><div id="comment-32713" class="comment"><div id="post-32713-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply Kurt. I will perform the test as suggested but why i am seeing tcp packets but not udp? BTW both Initiator and target are virtual machine instances and interface is eth0.</p></div><div id="comment-32713-info" class="comment-info"><span class="comment-age">(11 May '14, 11:09)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="32716"></span><div id="comment-32716" class="comment"><div id="post-32716-score" class="comment-score"></div><div class="comment-text"><blockquote><p>both Initiator and target are virtual machine instances and interface is eth0</p></blockquote><p>Same VM host or different one? Bridged interface or other?</p></div><div id="comment-32716-info" class="comment-info"><span class="comment-age">(11 May '14, 16:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32673" class="comment-tools"></div><div class="clear"></div><div id="comment-32673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

