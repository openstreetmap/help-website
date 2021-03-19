+++
type = "question"
title = "DNP3 as default decoding?"
description = '''From question: https://ask.wireshark.org/questions/7439/dnp3-decode-as-setting-in-wireshark-163? The port 20000 spec for DNP3 is mostly observed in the breach (as in, like, never. Even, or especially, with vendors that should know better). How do I set wireshark up to look for the 0564 that&#x27;s at the...'''
date = "2015-10-19T17:35:00Z"
lastmod = "2016-11-04T17:50:00Z"
weight = 46739
keywords = [ "dnp3" ]
aliases = [ "/questions/46739" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DNP3 as default decoding?](/questions/46739/dnp3-as-default-decoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46739-score" class="post-score" title="current number of votes">0</div><span id="post-46739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From question:</p><p><a href="https://ask.wireshark.org/questions/7439/dnp3-decode-as-setting-in-wireshark-163?">https://ask.wireshark.org/questions/7439/dnp3-decode-as-setting-in-wireshark-163?</a></p><p>The port 20000 spec for DNP3 is mostly observed in the breach (as in, like, never. Even, or especially, with vendors that should know better).</p><p>How do I set wireshark up to look for the 0564 that's at the beginning of a DNP3 communication, and then decode that transmission as DNP3 by default, no matter what ports it's talking to?</p><p>If that's not doable, then how do I configure IP addresses that any TCP communications to/from will be decoded as DNP3?</p><p>And, barring that...we are lucky in that all our DNP3 comm is on it's own physical network. So all TCP on that LAN is DNP. Can I leverage that to make life easier?</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dnp3" rel="tag" title="see questions tagged &#39;dnp3&#39;">dnp3</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '15, 17:35</strong></p><img src="https://secure.gravatar.com/avatar/13ec1ac4f9af45bf68093ef2e5d9ad47?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeauxbleaux&#39;s gravatar image" /><p><span>jeauxbleaux</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeauxbleaux has no accepted answers">0%</span></p></div></div><div id="comments-container-46739" class="comments-container"></div><div id="comment-tools-46739" class="comment-tools"></div><div class="clear"></div><div id="comment-46739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46774"></span>

<div id="answer-container-46774" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46774-score" class="post-score" title="current number of votes">0</div><span id="post-46774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Some time ago I added a DNP3 option to heuristically dissect data, you can find it in the DNP 3.0 Protocol options (Edit -&gt; Preferences -&gt; Protocols).</p><p>The caveat on that option working correctly is that the data segments must contain the complete data link header, i.e. 10 bytes.</p><p>Give the above caveat, enabling that option, and possibly the TCP &amp; UDP option "Try heuristic sub-dissectors first", should allow all DNP3 traffic to be dissected regardless of the port.</p><p>If you have a capture of DNP 3.0 traffic where that doesn't work I'd like to see at least a few frames of that to try to fix the issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '15, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-46774" class="comments-container"><span id="57004"></span><div id="comment-57004" class="comment"><div id="post-57004-score" class="comment-score"></div><div class="comment-text"><p>Wireshark capture traffic DNP3 without any further adjustment, the problem is the version of Wireshark to win 7, to install an earlier version win 7 the problem remains not see traffic DNP3, it has installed the x86 version and not to run into 7. what win I had to do is enable a virtual machine on an x64 processor, run and install winXP commensurate for this operating system version and it worked. In the win XP you can see DNP3 packages without making any adjustments in Wireshark.</p></div><div id="comment-57004-info" class="comment-info"><span class="comment-age">(04 Nov '16, 17:36)</span> <span class="comment-user userinfo">Marcos Valarezo</span></div></div><span id="57006"></span><div id="comment-57006" class="comment"><div id="post-57006-score" class="comment-score"></div><div class="comment-text"><p>I capture DNP3 most days on Win 7 and 10 without issue. The OS used should not affect DNP3 (or any other protocols) ,but other software installed on the system, e.g. VPN, Endpoint Protection etc. can affect captures.</p><p>When using Win 7, can you capture the traffic on the expected port at all, regardless of whether it's dissected as DNP3?</p><p>What version of Wireshark are you using on both systems?</p></div><div id="comment-57006-info" class="comment-info"><span class="comment-age">(04 Nov '16, 17:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-46774" class="comment-tools"></div><div class="clear"></div><div id="comment-46774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

