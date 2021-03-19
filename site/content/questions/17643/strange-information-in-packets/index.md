+++
type = "question"
title = "Strange information in packets"
description = '''I have Wireshark running on a Thinkpad T42 laptop which is connected to web server on an embedded device on a LAN. The laptop is connected to the server via web browser (Firefox). In the &quot;Info&quot; column in Wireshark, I&#x27;m seeing many packets that contain strange names such as:  radio-sm orbplus-iiop  p...'''
date = "2013-01-12T09:28:00Z"
lastmod = "2013-01-12T11:13:00Z"
weight = 17643
keywords = [ "strange", "streams" ]
aliases = [ "/questions/17643" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Strange information in packets](/questions/17643/strange-information-in-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17643-score" class="post-score" title="current number of votes">0</div><span id="post-17643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark running on a Thinkpad T42 laptop which is connected to web server on an embedded device on a LAN. The laptop is connected to the server via web browser (Firefox).</p><p>In the "Info" column in Wireshark, I'm seeing many packets that contain strange names such as:</p><ul><li>radio-sm</li><li>orbplus-iiop</li><li>picknfs</li></ul><p>Here's just a snippet of the Wireshark session - notice, in the info column, these strange names:</p><p>"10.10.6.240","10.10.6.106","TCP","54","<strong>radio-sm</strong> &gt; http [ACK] Seq=355 Ack=2 Win=65534 Len=0"</p><p>"10.10.6.240","10.10.6.107","TCP","62","<strong>orbplus-iiop</strong> &gt; http [SYN] Seq=0 Win=65535 Len=0 MSS=1460 SACK_PERM=1"</p><p>"10.10.6.106","TCP","54","<strong>picknfs</strong> &gt; http [ACK] Seq=355 Ack=691 Win=64846 Len=0"</p><p>"10.10.6.107","TCP","62","<strong>simbaservices</strong> &gt; http [SYN] Seq=0 Win=65535 Len=0 MSS=1460 SACK_PERM=1"</p><p>"10.10.6.240","10.10.6.107","TCP","54","<strong>aas</strong> &gt; http [ACK] Seq=354 Ack=331 Win=65206 Len=0"</p><p>What are these names referring to? And why do they appear in the stream?</p><p>For whatever it's worth, when I run Wireshark from a different computer, these strange names do not appear in the streams.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-strange" rel="tag" title="see questions tagged &#39;strange&#39;">strange</span> <span class="post-tag tag-link-streams" rel="tag" title="see questions tagged &#39;streams&#39;">streams</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '13, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/1259897b9b42059302967b55c0dc2228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KTM&#39;s gravatar image" /><p><span>KTM</span><br />
<span class="score" title="76 reputation points">76</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KTM has one accepted answer">100%</span></p></div></div><div id="comments-container-17643" class="comments-container"></div><div id="comment-tools-17643" class="comment-tools"></div><div class="clear"></div><div id="comment-17643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17646"></span>

<div id="answer-container-17646" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17646-score" class="post-score" title="current number of votes">2</div><span id="post-17646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="KTM has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Those are the TCP ports in use. You have transport name resolution turned on, so Wireshark is displaying port names instead of port numbers. For example, in your first frame "radio-sm &gt; http" means the source port is 1596 (radio-sm) and the destination port is 80 (http). This is probably traffic to a web server that's listening on port 80, so "http" is meaningful. However, 1596 is the ephemeral port that was chosen dynamically by the client for this session. It's not actually radio-sm traffic.</p><p>To turn off transport name resolution and see port numbers instead of names, select View &gt; Name Resolution, and uncheck "Enable for Transport Layer."</p><p>The port number-to-name mappings are found in the <em>services</em> file, which is in the Wireshark program directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '13, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-17646" class="comments-container"></div><div id="comment-tools-17646" class="comment-tools"></div><div class="clear"></div><div id="comment-17646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17645"></span>

<div id="answer-container-17645" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17645-score" class="post-score" title="current number of votes">1</div><span id="post-17645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's just the 'random' source ports of the TCP connections, which Wireshark tries to resolve to names.</p><p>See: <code>%ProgramFiles%\Wireshark\services</code></p><p>You can ignore it or change the behavior of Wireshark</p><blockquote><p><code>Edit -&gt; Preferences -&gt; Name Resolution -&gt; Enable transport name resolution</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '13, 11:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jan '13, 11:09</strong> </span></p></div></div><div id="comments-container-17645" class="comments-container"></div><div id="comment-tools-17645" class="comment-tools"></div><div class="clear"></div><div id="comment-17645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

