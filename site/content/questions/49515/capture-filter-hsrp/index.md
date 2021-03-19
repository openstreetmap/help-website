+++
type = "question"
title = "Capture filter hsrp"
description = '''Hello, I&#x27;m finding the capture filters utterly impenetrable. Could someone help me out please? - all I want to do is filter out HSRP packets (I&#x27;m capturing from a mirror port on a switch). Thank you'''
date = "2016-01-26T07:14:00Z"
lastmod = "2016-01-26T12:32:00Z"
weight = 49515
keywords = [ "filter", "capture", "hsrp" ]
aliases = [ "/questions/49515" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter hsrp](/questions/49515/capture-filter-hsrp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49515-score" class="post-score" title="current number of votes">1</div><span id="post-49515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm finding the capture filters utterly impenetrable. Could someone help me out please? - all I want to do is filter out HSRP packets (I'm capturing from a mirror port on a switch).</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-hsrp" rel="tag" title="see questions tagged &#39;hsrp&#39;">hsrp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '16, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/a3bd8e55dd705241b1e923a11b64f535?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cauliflower&#39;s gravatar image" /><p><span>Cauliflower</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cauliflower has no accepted answers">0%</span></p></div></div><div id="comments-container-49515" class="comments-container"></div><div id="comment-tools-49515" class="comment-tools"></div><div class="clear"></div><div id="comment-49515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49516"></span>

<div id="answer-container-49516" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49516-score" class="post-score" title="current number of votes">2</div><span id="post-49516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Capture filters, as they have to run at high speed to not drop packets when capturing are thus simpler than display filters and have less "knowledge" about protocols and nothing at all about HSRP in particular.</p><p>What you can do, though is filter on those aspects of HSRP that capture filters can handle, e.g. the udp port or the mac address using a capture filter such as <code>udp port 1985 or udp port 2029</code> or if that's too wide using <code>ether[0:5] = 00:00:0c:07:ac or ether[7:5] = 00:00:0c:07:ac</code> changing the partial MAC address for the variant of HSRP you're using.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '16, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49516" class="comments-container"><span id="49518"></span><div id="comment-49518" class="comment"><div id="post-49518-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I'm giving this a try:</p><p>not udp port 1985 and not udp port 2029</p></div><div id="comment-49518-info" class="comment-info"><span class="comment-age">(26 Jan '16, 08:46)</span> <span class="comment-user userinfo">Cauliflower</span></div></div><span id="49519"></span><div id="comment-49519" class="comment"><div id="post-49519-score" class="comment-score"></div><div class="comment-text"><p>Ah, I misread the "filter out" bit. I think you might want to try the filter <code>not(udp port 1985 or udp port 2029)</code>.</p></div><div id="comment-49519-info" class="comment-info"><span class="comment-age">(26 Jan '16, 09:10)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="49520"></span><div id="comment-49520" class="comment"><div id="post-49520-score" class="comment-score">1</div><div class="comment-text"><p>I would be careful with filtering packets out by MAC address prefix because if used alone, it would also be too wide in my understanding of how the HSRP works.</p><p>If I understand <span>@Cauliflower</span> right, (s)he wants to get rid only of the HSRP packets themselves (we might call it "HSRP <em>management</em>" traffic), while all the other packets to or from the HSRP virtual MAC address (which represents the IP of the virtual gateway) should most likely not be filtered out as they are the real traffic running through the gateway.</p><p>So my suggestion of the capture filter would be <code>not(udp and dst host 224.0.0.2 and port 1985)</code> for HSRPv1, and <code>not (udp and (dst host 224.0.0.102 and port 1985) or (dst host ff02::66 and port 2029))</code> for HSRPv2.</p><p>And only if <em>that</em> is still too wide, add <code>and ether[7]=0 and ether[8]=0 and ether[9]=0xc and ether[10]=0x9f and ether[11]&amp;0xf0=0xf0</code> to the IPv4 part of the HSRPv2 filter, and accordingly modified expressions for HSRPv1 and/or the IPv6 part of HSRPv2 filter (different MAC addresses in both cases).</p></div><div id="comment-49520-info" class="comment-info"><span class="comment-age">(26 Jan '16, 10:59)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="49522"></span><div id="comment-49522" class="comment"><div id="post-49522-score" class="comment-score"></div><div class="comment-text"><p>Thanks both, yes sindy is right, I want to exclude the HSRP 'management' traffic (Hello's etc) not traffic to/from the HSRP virtual IP/MAC.</p><p>I'll try <code>not (udp and (dst host 224.0.0.102 and port 1985) or (dst host ff02::66 and port 2029))</code></p></div><div id="comment-49522-info" class="comment-info"><span class="comment-age">(26 Jan '16, 12:32)</span> <span class="comment-user userinfo">Cauliflower</span></div></div></div><div id="comment-tools-49516" class="comment-tools"></div><div class="clear"></div><div id="comment-49516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

