+++
type = "question"
title = "IPv4 total length exceeds packet length"
description = '''What would be causes for this expert info errpr &quot;IPv4 total length exceeds packet length? See trace below. https://www.cloudshark.org/captures/e21319ae9105 Frame 1 has this error (I think most frames do). Is this a capture issue? This trace was gathered from tcpdump-uw from VMware ESXi. Or could it ...'''
date = "2016-05-16T13:48:00Z"
lastmod = "2016-05-16T14:42:00Z"
weight = 52648
keywords = [ "length", "framelength", "ipv4" ]
aliases = [ "/questions/52648" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [IPv4 total length exceeds packet length](/questions/52648/ipv4-total-length-exceeds-packet-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52648-score" class="post-score" title="current number of votes">0</div><span id="post-52648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What would be causes for this expert info errpr "IPv4 total length exceeds packet length?</p><p>See trace below. <a href="https://www.cloudshark.org/captures/e21319ae9105">https://www.cloudshark.org/captures/e21319ae9105</a></p><p>Frame 1 has this error (I think most frames do).</p><p>Is this a capture issue?</p><p>This trace was gathered from tcpdump-uw from VMware ESXi.</p><p>Or could it be a MTU issue?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-framelength" rel="tag" title="see questions tagged &#39;framelength&#39;">framelength</span> <span class="post-tag tag-link-ipv4" rel="tag" title="see questions tagged &#39;ipv4&#39;">ipv4</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '16, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/a472d068843eefd8a4ef69c4f94e4160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gipper&#39;s gravatar image" /><p><span>gipper</span><br />
<span class="score" title="30 reputation points">30</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gipper has no accepted answers">0%</span></p></div></div><div id="comments-container-52648" class="comments-container"></div><div id="comment-tools-52648" class="comment-tools"></div><div class="clear"></div><div id="comment-52648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52649"></span>

<div id="answer-container-52649" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52649-score" class="post-score" title="current number of votes">0</div><span id="post-52649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's probably some form of TCP segmentation offloading - if this is traffic between virtual machines, i.e. traffic not going over a real network, that might be happening at the VMware level - causing strange packets to be supplied to the packet capture mechanism.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '16, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-52649" class="comments-container"></div><div id="comment-tools-52649" class="comment-tools"></div><div class="clear"></div><div id="comment-52649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52650"></span>

<div id="answer-container-52650" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52650-score" class="post-score" title="current number of votes">0</div><span id="post-52650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is most likely a capture issue. You can see in the IPv4 header of frame 1 that the total length is 8292, which is probably a jumbo frame (since it's iSCSI traffic it's highly likely that it is). You can also see in the frame header that the "Bytes on Wire" is 96 bytes, and the "Bytes captured" is also 96 bytes. So the IP length is exceeding the packet length.</p><p>I guess someone set up a capture job and limited the amount of bytes captured per packet to 96 bytes maximum. Problem is, the capture job should set "Bytes captured" accordingly, and keep the original true length as "Bytes on Wire" (which is what Wireshark does if you set it to capture only 96 bytes).</p><p>As far as I've checked there is only the -s parameter to have tcpdump-uw capture a specific amount bytes per packet, so if that's what was used I doubt you can change that behavior. If you need to fix this problem you can use <a href="https://www.tracewrangler.com">TraceWrangler</a>.</p><p>I also wrote a blog post some time ago about slicing: <a href="https://blog.packet-foo.com/2015/08/frame-bytes-vs-frame-file-headers/">https://blog.packet-foo.com/2015/08/frame-bytes-vs-frame-file-headers/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '16, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-52650" class="comments-container"><span id="52651"></span><div id="comment-52651" class="comment"><div id="post-52651-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Problem is, the capture job should set "Bytes captured" accordingly, and keep the original true length as "Bytes on Wire" (which is what Wireshark does if you set it to capture only 96 bytes).</p></blockquote><p>Yes. In fact, <em>any</em> tool using a normal version of libpcap, atop a normal OS packet capture mechanism, would do that, so, if that's what happened, there's a bug somewhere in the capture mechanism, whether it's in tcpdump-uw, the libpcap it uses, or the packet capture mechanism that version of libpcap uses. <span></span><span>@gipper</span> should complain to VMware about this.</p></div><div id="comment-52651-info" class="comment-info"><span class="comment-age">(16 May '16, 14:40)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="52653"></span><div id="comment-52653" class="comment"><div id="post-52653-score" class="comment-score"></div><div class="comment-text"><p>Yes, it's a good idea to have VMware fix this.</p></div><div id="comment-52653-info" class="comment-info"><span class="comment-age">(16 May '16, 14:42)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-52650" class="comment-tools"></div><div class="clear"></div><div id="comment-52650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

