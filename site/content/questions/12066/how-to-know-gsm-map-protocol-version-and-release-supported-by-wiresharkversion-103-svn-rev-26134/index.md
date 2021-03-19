+++
type = "question"
title = "How to know GSM MAP protocol version and release supported by wireshark(Version 1.0.3 (SVN Rev 26134))"
description = '''How to know GSM MAP protocol version and latest release supported by wire shark. Is there any way So, that user can find out which protocol version and Release supported by wireshark release Version 1.0.3 (SVN Rev 26134)'''
date = "2012-06-20T02:03:00Z"
lastmod = "2012-06-20T17:48:00Z"
weight = 12066
keywords = [ "gsm", "wireshark" ]
aliases = [ "/questions/12066" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to know GSM MAP protocol version and release supported by wireshark(Version 1.0.3 (SVN Rev 26134))](/questions/12066/how-to-know-gsm-map-protocol-version-and-release-supported-by-wiresharkversion-103-svn-rev-26134)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12066-score" class="post-score" title="current number of votes">0</div><span id="post-12066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to know GSM MAP protocol version and latest release supported by wire shark. Is there any way So, that user can find out which protocol version and Release supported by wireshark release Version 1.0.3 (SVN Rev 26134)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gsm" rel="tag" title="see questions tagged &#39;gsm&#39;">gsm</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '12, 02:03</strong></p><img src="https://secure.gravatar.com/avatar/d684361041267598602bc5dfdaebae16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amankalra13&#39;s gravatar image" /><p><span>amankalra13</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amankalra13 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jun '12, 02:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-12066" class="comments-container"><span id="12070"></span><div id="comment-12070" class="comment"><div id="post-12070-score" class="comment-score"></div><div class="comment-text"><p>Can anybody have no idea regarding this?</p></div><div id="comment-12070-info" class="comment-info"><span class="comment-age">(20 Jun '12, 04:42)</span> <span class="comment-user userinfo">amankalra13</span></div></div></div><div id="comment-tools-12066" class="comment-tools"></div><div class="clear"></div><div id="comment-12066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12072"></span>

<div id="answer-container-12072" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12072-score" class="post-score" title="current number of votes">0</div><span id="post-12072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No ther is no reliable way to determine which GSM_MAP version is supported other than reading the sources. In general we have tried to make it backwards compatible but realy old releases are more likely to have miss dissection then newer ones. 1.0.3 is quite old, you are much better off with 1.6 or the soon to be released 1.8 (1.8.rc (release candidate is available).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '12, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-12072" class="comments-container"><span id="12073"></span><div id="comment-12073" class="comment"><div id="post-12073-score" class="comment-score"></div><div class="comment-text"><p>Now I have installed our System with Wire shark 1.6 Version. So,Is there any way to find out that which GSM_MAP version is supported.</p><p>I just want to confirm that either it supports ETSI TS 129 002 V10.6.0 (2012-04)SPEC or not?</p><p>Is it possible to find out through source code? Please let me know ASAP</p></div><div id="comment-12073-info" class="comment-info"><span class="comment-age">(20 Jun '12, 06:23)</span> <span class="comment-user userinfo">amankalra13</span></div></div><span id="12074"></span><div id="comment-12074" class="comment"><div id="post-12074-score" class="comment-score"></div><div class="comment-text"><p>Top of tree supports <a href="http://anonsvn.wireshark.org/viewvc/trunk/asn1/gsm_map/MAP-ApplicationContexts.asn?revision=39386&amp;view=markup&amp;pathrev=43342">http://anonsvn.wireshark.org/viewvc/trunk/asn1/gsm_map/MAP-ApplicationContexts.asn?revision=39386&amp;view=markup&amp;pathrev=43342</a> V10.4.0 (2011-09) And 1.6 <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.8/asn1/gsm_map/MAP-ApplicationContexts.asn?revision=43119&amp;view=markup&amp;pathrev=43342">http://anonsvn.wireshark.org/viewvc/trunk-1.8/asn1/gsm_map/MAP-ApplicationContexts.asn?revision=43119&amp;view=markup&amp;pathrev=43342</a> the same.</p></div><div id="comment-12074-info" class="comment-info"><span class="comment-age">(20 Jun '12, 07:39)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="12092"></span><div id="comment-12092" class="comment"><div id="post-12092-score" class="comment-score"></div><div class="comment-text"><p>That's great.Thanks for addressing this query.I will suggest that there should be an option in Wireshark--&gt;Help notes from which user can know regarding protocol version and Release supported</p><p>Thanks a lot again.</p><p>I hope to see Wireshark version with ETSI TS 129 002 V10.6.0 (2012-04)</p></div><div id="comment-12092-info" class="comment-info"><span class="comment-age">(20 Jun '12, 17:48)</span> <span class="comment-user userinfo">amankalra13</span></div></div></div><div id="comment-tools-12072" class="comment-tools"></div><div class="clear"></div><div id="comment-12072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

