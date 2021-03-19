+++
type = "question"
title = "cisco switchport input errors"
description = '''As of last week, I started receiving numerous input errors on three switchports of a cisco 3750 12 port fiber switch. For example, 21439 input errors, 3 CRC. Switchports on other switches connected to this fiber switch show 0 input errors. I am monitoring three ports in question and captured 5 minut...'''
date = "2013-01-29T09:08:00Z"
lastmod = "2013-01-29T19:52:00Z"
weight = 18041
keywords = [ "input", "errors", "cisco", "switchport" ]
aliases = [ "/questions/18041" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [cisco switchport input errors](/questions/18041/cisco-switchport-input-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18041-score" class="post-score" title="current number of votes">0</div><span id="post-18041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As of last week, I started receiving numerous input errors on three switchports of a cisco 3750 12 port fiber switch. For example, 21439 input errors, 3 CRC. Switchports on other switches connected to this fiber switch show 0 input errors. I am monitoring three ports in question and captured 5 minutes of traffic. What is the best way to analyze capture to possibly determine source of input errors?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-input" rel="tag" title="see questions tagged &#39;input&#39;">input</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span> <span class="post-tag tag-link-switchport" rel="tag" title="see questions tagged &#39;switchport&#39;">switchport</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '13, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/10822f26fc10b4189a856cf74b5c38a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws-dmoore&#39;s gravatar image" /><p><span>ws-dmoore</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws-dmoore has no accepted answers">0%</span></p></div></div><div id="comments-container-18041" class="comments-container"></div><div id="comment-tools-18041" class="comment-tools"></div><div class="clear"></div><div id="comment-18041-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18044"></span>

<div id="answer-container-18044" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18044-score" class="post-score" title="current number of votes">1</div><span id="post-18044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>AS they are input errors, they will not be duplicated with a monitor session. The only way to catch them would be to place a TAP on the ports and use a sniffer that does not drop frames with a bad FCS. Or maybe do some analysis of bad frames.</p><p>What kind of errors are they if they are not CRC errors?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18044" class="comments-container"></div><div id="comment-tools-18044" class="comment-tools"></div><div class="clear"></div><div id="comment-18044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18074"></span>

<div id="answer-container-18074" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18074-score" class="post-score" title="current number of votes">0</div><span id="post-18074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please make sure it's not something simple like a L2 device sending DTP (Dynamic Trunking PRotocol) to your L3 3750 (if it's L3). Router interfaces don't know what DTP is, and will cause input error counters to increment.<br />
</p><p>Also, Cisco has some nice documents on how to troubleshoot input errors. If you google for it, I'm sure you'll find several articles that can guide you.</p><p>Wireshark isn't the best tool because w/o a tap, you'll never see it in Wireshark. Even with a tap, you may not see damaged frames. So troubleshoot with Cisco CLI first (show controllers, sho ip counters, etc.) Good luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 19:52</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div></div><div id="comments-container-18074" class="comments-container"></div><div id="comment-tools-18074" class="comment-tools"></div><div class="clear"></div><div id="comment-18074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

