+++
type = "question"
title = "MAC address"
description = '''Hello, I need to track a MAC address or a span of MAC addresses, any idea how to just filter with the MAC? As of now I have just filtered via LLC protocol it would be alot cleaner with just the mac. Thanks in advance.'''
date = "2011-06-02T07:17:00Z"
lastmod = "2011-06-08T10:04:00Z"
weight = 4333
keywords = [ "filter", "mac", "mac-address" ]
aliases = [ "/questions/4333" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [MAC address](/questions/4333/mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4333-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I need to track a MAC address or a span of MAC addresses, any idea how to just filter with the MAC? As of now I have just filtered via LLC protocol it would be alot cleaner with just the mac.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">filter mac mac-address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '11, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/91e210367995c3353d652b7b0f745381?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aplatek&#39;s gravatar image" /><p>aplatek<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aplatek has no accepted answers">0%</span></p></div></div><div id="comments-container-4333" class="comments-container"></div><div id="comment-tools-4333" class="comment-tools"></div><div class="clear"></div><div id="comment-4333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4454"></span>

<div id="answer-container-4454" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4454-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are using a display filter of eth.addr == xx:xx:xx:xx:xx:xx and you are not seeing any information being displayed/sniffed, then the traffic for that MAC address is not passing through the port you're sniffing on.</p><p>You can use a list for your MAC's in one display filter, but not a range, unless you switch to IP's instead of MAC's. For instance, tshark -i 1 -R "eth.addr eq xx:xx:xx:xx:xx:xx or eth.addr eq xx:xx:xx:xx:xx:xx"</p><p>If you are trying to trace MAC's on the switch you are also connected to, then you'll want to sniff from a port which is spanned/mirrored to the port which has inbound/outbound traffic of that switch, so that you will see all the traffic coming in and out of the switch.<br />
(I'm assuming the traffic you are looking for is traveling to a destination on another switch, outside the network, or at least to your gateway).</p><p>By specifying the MAC address filter, eth.addr eq xx:xx:xx:xx:xx:xx you are filtering for all traffic to and from that associated MAC address. Like the MAC address, The LLC logical link control protocol is also layer 2, but is upper sublayer of Data Link Layer and won't affect the ability to capture the traffic unless you specify llc as a filter and there isn't any llc traffic, then you would get the blank screen.</p><p>Hope this is helpful, John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '11, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p>John_Modlin<br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-4454" class="comments-container"><span id="4452"></span><div id="comment-4452" class="comment"><div id="post-4452-score" class="comment-score"></div><div class="comment-text"><p>eth.src == 00:0c:cc:76:5d:37 Using this filter it still will not pick up my MAC is it because of the llc protocol?</p></div><div id="comment-4452-info" class="comment-info"><span class="comment-age">(08 Jun '11, 08:09)</span> aplatek</div></div><span id="4501"></span><div id="comment-4501" class="comment"><div id="post-4501-score" class="comment-score"></div><div class="comment-text"><p>My answer above describes the relationship between LLC and the MAC addressing.<br />
Can you describe your physical connectivity of your sniffer and the device of which you are trying to capture?</p></div><div id="comment-4501-info" class="comment-info"><span class="comment-age">(10 Jun '11, 07:41)</span> John_Modlin</div></div></div><div id="comment-tools-4454" class="comment-tools"></div><div class="clear"></div><div id="comment-4454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4334"></span>

<div id="answer-container-4334" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4334-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Between the <a href="http://wiki.wireshark.org/Ethernet">Ethernet wiki page</a> and the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">user guide</a>, you should find just about everything you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '11, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></p></div></div><div id="comments-container-4334" class="comments-container"><span id="4335"></span><div id="comment-4335" class="comment"><div id="post-4335-score" class="comment-score"></div><div class="comment-text"><p>eth.dst == 00:0C:CC:76:4E:07 This filters out everything and that is right from the user guide. It makes the field blank? any ideas?</p></div><div id="comment-4335-info" class="comment-info"><span class="comment-age">(02 Jun '11, 07:47)</span> aplatek</div></div><span id="4340"></span><div id="comment-4340" class="comment"><div id="post-4340-score" class="comment-score"></div><div class="comment-text"><p>Within the packet details pane, if you right-click on a MAC address of interest and choose, "Apply as filter -&gt; Selected", what do you get?</p></div><div id="comment-4340-info" class="comment-info"><span class="comment-age">(02 Jun '11, 09:56)</span> cmaynard ♦♦</div></div><span id="4354"></span><div id="comment-4354" class="comment"><div id="post-4354-score" class="comment-score"></div><div class="comment-text"><p>By the way, if you're not actually capturing the MAC addresses you're interested in, then you might want to review your <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">capture setup</a>.</p></div><div id="comment-4354-info" class="comment-info"><span class="comment-age">(02 Jun '11, 17:39)</span> cmaynard ♦♦</div></div><span id="4453"></span><div id="comment-4453" class="comment"><div id="post-4453-score" class="comment-score"></div><div class="comment-text"><p>Blank screen.?</p></div><div id="comment-4453-info" class="comment-info"><span class="comment-age">(08 Jun '11, 08:14)</span> aplatek</div></div><span id="4455"></span><div id="comment-4455" class="comment"><div id="post-4455-score" class="comment-score"></div><div class="comment-text"><blockquote><p>eth.dst == 00:0C:CC:76:4E:07 This filters out everything and that &gt; is right from the user guide. It makes the field blank? any ideas?</p><p>Blank screen.?</p></blockquote><p>Yes. Your capture session does not have any traffic with a destination MAC address of 00:0C:CC:76:4E:07. If your packet list shows traffic before you apply this filter, and is blank after you apply this filter, then you are capturing something, but not traffic to this MAC address.</p><p>It might help people to help you if you answer cmaynard's question about what happens if you right-click a MAC address and choose "Apply as filter -&gt; Selected."</p></div><div id="comment-4455-info" class="comment-info"><span class="comment-age">(08 Jun '11, 11:25)</span> Jim Aragon</div></div></div><div id="comment-tools-4334" class="comment-tools"></div><div class="clear"></div><div id="comment-4334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4336"></span>

<div id="answer-container-4336" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4336-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are only interested in traffic concerning a device with the MAC address from your comment, you can use this capture filter: <code>ether host 00:0C:CC:76:4E:07</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '11, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-4336" class="comments-container"></div><div id="comment-tools-4336" class="comment-tools"></div><div class="clear"></div><div id="comment-4336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

