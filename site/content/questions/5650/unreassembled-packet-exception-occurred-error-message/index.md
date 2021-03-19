+++
type = "question"
title = "&quot;Unreassembled Packet (Exception occurred)&quot; error message"
description = '''While running Wireshark 1.4.4 I found that many of the TLSv1 messages were not being reassembled, but left as [Unreassembled Packet]/Ignored Unknown Record. Having checked the existing documentation on this, I made sure that in the TCP preferences, checksum validation is unchecked, and &quot;allow subdis...'''
date = "2011-08-11T08:54:00Z"
lastmod = "2013-02-28T20:04:00Z"
weight = 5650
keywords = [ "tlsv1", "reassembly", "tcp", "ssl" ]
aliases = [ "/questions/5650" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["Unreassembled Packet (Exception occurred)" error message](/questions/5650/unreassembled-packet-exception-occurred-error-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5650-score" class="post-score" title="current number of votes">0</div><span id="post-5650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While running Wireshark 1.4.4 I found that many of the TLSv1 messages were not being reassembled, but left as [Unreassembled Packet]/Ignored Unknown Record. Having checked the existing documentation on this, I made sure that in the TCP preferences, checksum validation is unchecked, and "allow subdissector to reassemble TCP streams is checked." I also made sure that "Reassemble SSL records spanning multiple TCP segements" and "Reassemble SSL Application Data spanning multiple SSL records" were checked within the SSL preferences. I also upgraded to v1.6.1, in case there was something wrong with my version. Despite all this, this problem persisted - the packets are not reassembled.</p><p>In the packets marked "[Unreassembled Packet]", there is an error message, stating:</p><p>[Expert Info (Warn/Reassemble): Unreassembled Packet (Exception occurred)] [Message: Unreassembled Packet (Exception occurred)] [Severity level: warn] [Group: Reassemble]</p><p>Your help would be appreciated.</p><p>Many thanks,</p><p>Salem</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tlsv1" rel="tag" title="see questions tagged &#39;tlsv1&#39;">tlsv1</span> <span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '11, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/aae5157d7ed2cacd7d5446babb1c9f70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Salemicus&#39;s gravatar image" /><p><span>Salemicus</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Salemicus has no accepted answers">0%</span></p></div></div><div id="comments-container-5650" class="comments-container"><span id="6387"></span><div id="comment-6387" class="comment"><div id="post-6387-score" class="comment-score"></div><div class="comment-text"><p>Hi Salem</p><p>I had the same issue as you... Have you checked that "Allow Subdissector to reassemble TCP streams" under TCP protocol settings is checked? (If you hover over the "Reassemble SSL records spanning multiple TCP segments" in the SSL properties it mentions this, that's how I figured it out ;-)</p><p>It fixed it for me!</p><p>Cheers Ian</p></div><div id="comment-6387-info" class="comment-info"><span class="comment-age">(15 Sep '11, 06:58)</span> <span class="comment-user userinfo">ipittam</span></div></div><span id="12394"></span><div id="comment-12394" class="comment"><div id="post-12394-score" class="comment-score"></div><div class="comment-text"><p>I am having the same problem, was anyone able to find what the issue was?</p></div><div id="comment-12394-info" class="comment-info"><span class="comment-age">(03 Jul '12, 06:36)</span> <span class="comment-user userinfo">juanJmtz</span></div></div></div><div id="comment-tools-5650" class="comment-tools"></div><div class="clear"></div><div id="comment-5650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12412"></span>

<div id="answer-container-12412" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12412-score" class="post-score" title="current number of votes">1</div><span id="post-12412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please make sure the following requirements are met:</p><ul><li>The packets are not truncated (so no snaplength used at capture time)</li><li>There are no duplicate packets (when spanning a vlan, make sure you only span RX packets). If there are duplicated, either remove them with "editcap -d" or use "Edit -&gt; ignore packet" on the duplicates)</li><li>In the IP protocol preferences, enable "Reassemble fragemented IPv4 datagrams"</li><li>In the TCP protocol preferences, disable "Validate the TCP checksum"</li><li>In the TCP protocol preferences, enable "allow subdissector to reassemble TCP streams"</li><li>In the SSL protocol preferences, enable "Reassemble SSL records spanning multiple TCP segements"</li><li>In the SSL protocol preferences, enable "Reassemble SSL Application Data spanning multiple SSL records"</li></ul><p>If things are still not dissected properly, please post your capture file to <a href="http://www.cloudshark.org">www.cloudshark.org</a> and paste the link to the file here in a comment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '12, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-12412" class="comments-container"><span id="12418"></span><div id="comment-12418" class="comment"><div id="post-12418-score" class="comment-score"></div><div class="comment-text"><p>The packets are truncated: headers + 32 You know for some reason editcap -d is not eliminating the duplicates, even though I am seeing them in the trace, there are too many dups to ignore them 1 by 1. The traffic is being span via a VACL allowing all IP traffic to be sent to the capturing device (I guess this is the same a doing a span on both tx and rx) IP, TCP and SSL settings are set as you recommend.</p><p>Thanks for your help.</p></div><div id="comment-12418-info" class="comment-info"><span class="comment-age">(03 Jul '12, 11:30)</span> <span class="comment-user userinfo">juanJmtz</span></div></div><span id="12421"></span><div id="comment-12421" class="comment"><div id="post-12421-score" class="comment-score"></div><div class="comment-text"><p>In your case you have double trouble (and I'm not talking about Stevie Ray Vaughan's band).</p><p>Without the full packets, reassembly will not work, so you might see more dissection with reassembly turned off.</p><p>Then with your duplicates reassembly would also be problematic. If you can filter one half of the packets with an "eth.addr==xx:xx:xx:xx:xx:xx" filter, you will be able to ignore them all at once :-)</p></div><div id="comment-12421-info" class="comment-info"><span class="comment-age">(03 Jul '12, 12:49)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="19003"></span><div id="comment-19003" class="comment"><div id="post-19003-score" class="comment-score"></div><div class="comment-text"><p>For completeness: another possibility in general is that the network has jumbo frames enabled. In this instance you actually <em>will</em> require to set a snaplength of a sensible value (eg: 9000).</p></div><div id="comment-19003-info" class="comment-info"><span class="comment-age">(28 Feb '13, 20:04)</span> <span class="comment-user userinfo">tychothecat</span></div></div></div><div id="comment-tools-12412" class="comment-tools"></div><div class="clear"></div><div id="comment-12412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

