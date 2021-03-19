+++
type = "question"
title = "Protocol column shows 0x0800 instead of HTTP"
description = '''Using Wiresharks release 1.6.1, running on Windows 7. Wiresharks used to show protocol HTTP for a http packet. However, recently it cannot correctly show the protocol names, instead, it shows 0x0800 in the Protocol column. It seems Wiresharks cannot identify it is a http packet. The same problems ha...'''
date = "2011-09-08T09:36:00Z"
lastmod = "2014-08-19T06:37:00Z"
weight = 6212
keywords = [ "0x0800" ]
aliases = [ "/questions/6212" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Protocol column shows 0x0800 instead of HTTP](/questions/6212/protocol-column-shows-0x0800-instead-of-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6212-score" class="post-score" title="current number of votes">0</div><span id="post-6212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Wiresharks release 1.6.1, running on Windows 7. Wiresharks used to show protocol HTTP for a http packet. However, recently it cannot correctly show the protocol names, instead, it shows 0x0800 in the Protocol column. It seems Wiresharks cannot identify it is a http packet. The same problems happen to all the protocols above the IP layer. Reinstalled Wiresharks several times, got the same problem. Anything wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-0x0800" rel="tag" title="see questions tagged &#39;0x0800&#39;">0x0800</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '11, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/a84138712fc6b564760b3636ae4060d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wfun&#39;s gravatar image" /><p><span>wfun</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wfun has no accepted answers">0%</span></p></div></div><div id="comments-container-6212" class="comments-container"></div><div id="comment-tools-6212" class="comment-tools"></div><div class="clear"></div><div id="comment-6212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6214"></span>

<div id="answer-container-6214" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6214-score" class="post-score" title="current number of votes">4</div><span id="post-6214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If it's showing 0x0800 in the Protocol column, it's not even identifying it as an <em>IPv4</em> packet, which explains why it's not identifying anything above the IP layer. Try the "Enabled Protocols" item in the "Analyze" menu, and see whether there's a checkmark next to IPv4. If not, check that checkbox and click "OK", and see if that fixes the problem; if so, that means that, somehow, the IPv4 dissector got disabled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '11, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6214" class="comments-container"></div><div id="comment-tools-6214" class="comment-tools"></div><div class="clear"></div><div id="comment-6214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35556"></span>

<div id="answer-container-35556" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35556-score" class="post-score" title="current number of votes">0</div><span id="post-35556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nothing wrong, I would say: 0x0800 indicates the IP protocol in the protocol code field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '14, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/1682e9e4a3959dcaea20a82537df5d72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sophia&#39;s gravatar image" /><p><span>Sophia</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sophia has no accepted answers">0%</span></p></div></div><div id="comments-container-35556" class="comments-container"><span id="35560"></span><div id="comment-35560" class="comment"><div id="post-35560-score" class="comment-score"></div><div class="comment-text"><p>In general, as far as I know: From IANA: Ethernet assigned numbers. IEEE: Registration authority.</p><p>Ethertype</p><p>0x0000 and 0x05DC = IEEE 802.3 length.</p><p>0x0600 = XEROX NS IDP.</p><p>0x0660 and 0x0661 = DLOG.</p><p>0x0800 = IP, Internet Protocol</p><p>0x0801 = X.75 Internet.</p><p>0x0802 = NBS Internet.</p><p>0x0803 = ECMA Internet.</p><p>0x0804 = Chaosnet.</p><p>0x0805 = X.25 Level 3.</p><p>0x0806 = ARP, Address Resolution Protocol.</p><p>0x0807 = XNS compatibility.</p><p>0x0808 = Frame Relay ARP.</p><p>0x8035 = DRARP, Dynamic RARP. RARP, Reverse Address Resolution Protocol.</p><p>0x80F3 = AARP, AppleTalk Address Resolution Protocol.</p><p>See: <a href="http://www.networksorcery.com/enp/protocol/802/ethertypes.htm">http://www.networksorcery.com/enp/protocol/802/ethertypes.htm</a></p></div><div id="comment-35560-info" class="comment-info"><span class="comment-age">(19 Aug '14, 03:25)</span> <span class="comment-user userinfo">Sophia</span></div></div><span id="35575"></span><div id="comment-35575" class="comment"><div id="post-35575-score" class="comment-score"></div><div class="comment-text"><p>Well there is an RFC about it: <a href="http://www.rfc-base.org/txt/rfc-894.txt">894</a></p></div><div id="comment-35575-info" class="comment-info"><span class="comment-age">(19 Aug '14, 06:37)</span> <span class="comment-user userinfo">Sophia</span></div></div></div><div id="comment-tools-35556" class="comment-tools"></div><div class="clear"></div><div id="comment-35556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

