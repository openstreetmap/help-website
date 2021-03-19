+++
type = "question"
title = "How to capture specific DNS request when payload pattern changes places"
description = '''I am trying to create a capture filter for a DNS request. I can match the hex but specific payload pattern changes places.  udp[18:4]=0x* or udp[19:4]=0x* or udp[20:4]=0x** can I match specific payload at several packet/locations using a easier capture expression? perhaps rex?  Can anyone help me pl...'''
date = "2017-01-23T08:07:00Z"
lastmod = "2017-01-24T02:28:00Z"
weight = 58983
keywords = [ "capture-filter", "dnsquery" ]
aliases = [ "/questions/58983" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture specific DNS request when payload pattern changes places](/questions/58983/how-to-capture-specific-dns-request-when-payload-pattern-changes-places)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58983-score" class="post-score" title="current number of votes">0</div><span id="post-58983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to create a capture filter for a DNS request. I can match the hex but specific payload pattern changes places.</p><p>udp[18:4]=0x<strong><em>*</em></strong> <em>or udp[19:4]=0x<strong><em>*</em></strong></em> or udp[20:4]=0x<strong><em>*</em></strong>*</p><p>can I match specific payload at several packet/locations using a easier capture expression? perhaps rex?</p><p>Can anyone help me please ?</p><p>Thanks you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-dnsquery" rel="tag" title="see questions tagged &#39;dnsquery&#39;">dnsquery</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '17, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/1de99f33f2a0acaca16ce8cb95175dbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Oskarino&#39;s gravatar image" /><p><span>Oskarino</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Oskarino has no accepted answers">0%</span></p></div></div><div id="comments-container-58983" class="comments-container"><span id="59007"></span><div id="comment-59007" class="comment"><div id="post-59007-score" class="comment-score">1</div><div class="comment-text"><p>There was a gorgeous talk (<a href="https://youtu.be/DS4j9pwVuog)">https://youtu.be/DS4j9pwVuog)</a> by Sake at Sharkfest explaining BPF (capture filter) in detail. The presentation is also available (<a href="https://sharkfest.wireshark.org/assets/presentations16/13.pdf).">https://sharkfest.wireshark.org/assets/presentations16/13.pdf).</a></p><p>Maybe this helps.</p></div><div id="comment-59007-info" class="comment-info"><span class="comment-age">(24 Jan '17, 02:28)</span> <span class="comment-user userinfo">Uli</span></div></div></div><div id="comment-tools-58983" class="comment-tools"></div><div class="clear"></div><div id="comment-58983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

