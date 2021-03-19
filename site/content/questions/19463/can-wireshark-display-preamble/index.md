+++
type = "question"
title = "Can wireshark display preamble?"
description = '''Suppose I have a list of packets which will be written as PCAP file. The packets contains 8 bytes preamble. Currently I don&#x27;t write those 8 bytes to the PCAP. I am just wondering if it is possible to write preamble to the PCAP? Thanks.'''
date = "2013-03-13T10:52:00Z"
lastmod = "2013-03-18T15:08:00Z"
weight = 19463
keywords = [ "preamble" ]
aliases = [ "/questions/19463" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can wireshark display preamble?](/questions/19463/can-wireshark-display-preamble)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19463-score" class="post-score" title="current number of votes">0</div><span id="post-19463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Suppose I have a list of packets which will be written as PCAP file. The packets contains 8 bytes preamble. Currently I don't write those 8 bytes to the PCAP. I am just wondering if it is possible to write preamble to the PCAP?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-preamble" rel="tag" title="see questions tagged &#39;preamble&#39;">preamble</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '13, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/d92822259e255fc18dcce53ae5403331?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kintaro&#39;s gravatar image" /><p><span>kintaro</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kintaro has no accepted answers">0%</span></p></div></div><div id="comments-container-19463" class="comments-container"></div><div id="comment-tools-19463" class="comment-tools"></div><div class="clear"></div><div id="comment-19463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19474"></span>

<div id="answer-container-19474" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19474-score" class="post-score" title="current number of votes">1</div><span id="post-19474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kintaro has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Note there's a link type which has all this included: LINKTYPE_NETANALYZER_TRANSPARENT, see the <a href="http://www.tcpdump.org/linktypes.html">TCP dump site</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19474" class="comments-container"><span id="19484"></span><div id="comment-19484" class="comment"><div id="post-19484-score" class="comment-score"></div><div class="comment-text"><p>Ok. Let me try. Thanks.</p></div><div id="comment-19484-info" class="comment-info"><span class="comment-age">(13 Mar '13, 17:47)</span> <span class="comment-user userinfo">kintaro</span></div></div><span id="19490"></span><div id="comment-19490" class="comment"><div id="post-19490-score" class="comment-score"></div><div class="comment-text"><p>Note that you'll have to include, in addition to the preamble, the 4-byte header described <a href="http://www.tcpdump.org/linktypes/LINKTYPE_NETANALYZER.html">on the tcpdump.org page for LINKTYPE_NETANALYZER</a>.</p><p>Note also that, currently, the entire payload for LINKTYPE_NETANALYZER_TRANSPARENT is dissected as raw data; it doesn't show the preamble and SFD and then dissect the rest as an Ethernet frame.</p></div><div id="comment-19490-info" class="comment-info"><span class="comment-age">(14 Mar '13, 01:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="19621"></span><div id="comment-19621" class="comment"><div id="post-19621-score" class="comment-score"></div><div class="comment-text"><p>I try to save the file as network type 241 (LINKTYPE_NETANALYZER_TRANSPARENT) but wireshark shows error:</p><p>"Files capture.pcap is a capture for a network type that Wireshark doesn't support. (pcap: network type 241 unknown or unsupported).</p><p>Any idea why?</p></div><div id="comment-19621-info" class="comment-info"><span class="comment-age">(18 Mar '13, 11:15)</span> <span class="comment-user userinfo">kintaro</span></div></div><span id="19622"></span><div id="comment-19622" class="comment"><div id="post-19622-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any idea why?</p></blockquote><p>Because you're using a version of Wireshark that's too old to support LINKTYPE_NETANALYZER_TRANSPARENT. You need Wireshark 1.8 or later.</p></div><div id="comment-19622-info" class="comment-info"><span class="comment-age">(18 Mar '13, 11:19)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="19627"></span><div id="comment-19627" class="comment"><div id="post-19627-score" class="comment-score"></div><div class="comment-text"><p>Cool. It works. You are right, it won't decode the payload as Ethernet frame. Are we going to implement that in the future?</p></div><div id="comment-19627-info" class="comment-info"><span class="comment-age">(18 Mar '13, 15:00)</span> <span class="comment-user userinfo">kintaro</span></div></div><span id="19628"></span><div id="comment-19628" class="comment not_top_scorer"><div id="post-19628-score" class="comment-score"></div><div class="comment-text"><p>The reason why the Hilscher people didn't do that is, to quote a comment in their code:</p><pre><code>  /* do not hand off transparent packet for further Ethernet dissectors
   * as normally the transparent mode is used for low level analysis
   * where dissecting the frame&#39;s content wouldn&#39;t make much sense
   * use data dissector instead */</code></pre><p>However, "normally" doesn't mean "always", and, even then, I'm not sure what for what sort of "low-level analysis" it would be better not to dissect the Ethernet packet at all. We should probably change that at some point.</p></div><div id="comment-19628-info" class="comment-info"><span class="comment-age">(18 Mar '13, 15:08)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-19474" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-19474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19464"></span>

<div id="answer-container-19464" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19464-score" class="post-score" title="current number of votes">1</div><span id="post-19464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it is possible, because Wireshark will try to interpret the 8 bytes as part of the packet contents, which they are not. Why would you want to write the preamble to file anyway? Usually it's always the same pattern, and not very interesting unless you have a jabber going on.</p><p>So no, Wireshark can not display the preamble.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Mar '13, 11:03</strong> </span></p></div></div><div id="comments-container-19464" class="comments-container"><span id="19466"></span><div id="comment-19466" class="comment"><div id="post-19466-score" class="comment-score"></div><div class="comment-text"><p>The reason is that my PFGA can give me the whole packet (including the preamble) and I would like to display it in the PCAP file.</p></div><div id="comment-19466-info" class="comment-info"><span class="comment-age">(13 Mar '13, 11:21)</span> <span class="comment-user userinfo">kintaro</span></div></div><span id="19467"></span><div id="comment-19467" class="comment"><div id="post-19467-score" class="comment-score"></div><div class="comment-text"><p>PCAP does not include preambles, so if you need to keep them for any reason you cannot use PCAP. Maybe some other format can do this, but I don't think any commercial or open source format does. I know that the Network General CAP format has some features that go beyond what PCAP can do, but it is not well documented.</p></div><div id="comment-19467-info" class="comment-info"><span class="comment-age">(13 Mar '13, 11:50)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="19477"></span><div id="comment-19477" class="comment"><div id="post-19477-score" class="comment-score"></div><div class="comment-text"><p>pcap/pcap-ng files can, as long as there's a link-layer header type for it, contain, for example, Ethernet packets with the preamble. See Jaap's answer. A pcap file, or packets from a pcap-ng interface, with a link-layer header type of LINKTYPE_ETHERNET (corresponding to DLT_EN10MB) can't contain the preamble, but, as Jaap noted, a pcap file, or packets from a pcap-ng interface, with a link-layer header type of LINKTYPE_NETANALYZER_TRANSPARENT can - and, in fact, <em>must</em> - include a preamble (and the FCS). They must also include a pseudo-header giving some flags.</p></div><div id="comment-19477-info" class="comment-info"><span class="comment-age">(13 Mar '13, 15:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="19478"></span><div id="comment-19478" class="comment"><div id="post-19478-score" class="comment-score"></div><div class="comment-text"><p>this shows once again that one never stops learning new stuff... I didn't know that. Maybe we should uncheck my answer and accept Jaaps answer instead? I'd be fine with that, it's the better one.</p></div><div id="comment-19478-info" class="comment-info"><span class="comment-age">(13 Mar '13, 15:27)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-19464" class="comment-tools"></div><div class="clear"></div><div id="comment-19464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

