+++
type = "question"
title = "Granularity missing in latest wireshark for WMM parameters?"
description = '''In wireshark 1.2 version, we had display filters such as wlan_mgt.wme.be.ac_param.ecwmin==7, i.e. you could filter packets based on WMM parameters for a specific access category. But in latest wireshark, we can&#x27;t do that. i.e. , if I want packets which has ECWMIN for Best Effort is equal to 7, I can...'''
date = "2013-10-10T11:30:00Z"
lastmod = "2013-10-14T16:43:00Z"
weight = 25892
keywords = [ "params", "wmm" ]
aliases = [ "/questions/25892" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Granularity missing in latest wireshark for WMM parameters?](/questions/25892/granularity-missing-in-latest-wireshark-for-wmm-parameters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25892-score" class="post-score" title="current number of votes">0</div><span id="post-25892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In wireshark 1.2 version, we had display filters such as</p><p>wlan_mgt.wme.be.ac_param.ecwmin==7, i.e. you could filter packets based on WMM parameters for a specific access category.</p><p>But in latest wireshark, we can't do that. i.e. , if I want packets which has ECWMIN for Best Effort is equal to 7, I can't do that. What I can do is, packets maching ECWMIN to 7. So if I put this filter, I get packets which has WMM param ECWMIN equal to 7 for either best effort/backgroun/voice/video.</p><p>Above display filter is changed to: wlan_mgt.wfa.ie.wme.acp.ecw.min. here I can't mention for which access category I need!</p><p>I'm surprised by this change. Is it a bug? Can I request for enhancement?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-params" rel="tag" title="see questions tagged &#39;params&#39;">params</span> <span class="post-tag tag-link-wmm" rel="tag" title="see questions tagged &#39;wmm&#39;">wmm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '13, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/5c59321a66976ba615e1a50b46a4d209?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramprasad&#39;s gravatar image" /><p><span>Ramprasad</span><br />
<span class="score" title="20 reputation points">20</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramprasad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Oct '13, 11:31</strong> </span></p></div></div><div id="comments-container-25892" class="comments-container"></div><div id="comment-tools-25892" class="comment-tools"></div><div class="clear"></div><div id="comment-25892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25918"></span>

<div id="answer-container-25918" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25918-score" class="post-score" title="current number of votes">2</div><span id="post-25918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I searched the trunk-1.2 sources (as well as all other trunks) for a filter named <code>wlan_mgt.wme.be.ac_param.ecwmin</code> and came up empty. It's not listed anywhere on the on-line Wireshark <a href="http://www.wireshark.org/docs/dfref/">display filter reference page</a> either, at least not as far as I can tell. Running <code>tshark -G fields | grep "wlan_mgt\.wme\.be\.ac_param\.ecwmin"</code> also comes up empty. The supposed replacement filter of <code>wlan_mgt.wfa.ie.wme.acp.ecw.min</code> was first introduced with <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-ieee80211.c?r1=37468&amp;r2=37486">r37486</a>, and as far as I can tell, wasn't a rename of the previous filter but an entirely new one.</p><p>So maybe you can help point to where that filter previously existed because I can't find any reference to it anywhere.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '13, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-25918" class="comments-container"><span id="25947"></span><div id="comment-25947" class="comment"><div id="post-25947-score" class="comment-score"></div><div class="comment-text"><p>Yes, possible. The current version we are using is customized to meet our needs. Probably this is part of it.</p><p>Assuming this is never present, could you think of any other solution to above problem? i.e. to filter packets based on value for a particular access category?, which is not possible with current granularity level we have?</p></div><div id="comment-25947-info" class="comment-info"><span class="comment-age">(13 Oct '13, 09:04)</span> <span class="comment-user userinfo">Ramprasad</span></div></div><span id="25982"></span><div id="comment-25982" class="comment"><div id="post-25982-score" class="comment-score"></div><div class="comment-text"><p><em>could you think of any other solution to above problem?</em></p><p>I can think of a few solutions to your problem. You could:</p><ul><li>Continue to use the version you were using before that provided the functionality that you're looking for.</li><li>Implement the functionality that you need yourself.</li><li>Open a bug report and attach a patch that implements the functionality you desire so that once it's committed to the Wireshark repository you won't have to worry about this anymore.</li><li>Open a bug report asking for an enhancement for this new functionality if you are unable to provide a patch yourself, then hope that one day somebody implements this for you.</li><li>Hire someone to implement the desired functionality if you're unable to do it yourself and are unwilling to wait for someone else in the Wireshark community to maybe implement it one day.</li></ul></div><div id="comment-25982-info" class="comment-info"><span class="comment-age">(14 Oct '13, 16:43)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-25918" class="comment-tools"></div><div class="clear"></div><div id="comment-25918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

