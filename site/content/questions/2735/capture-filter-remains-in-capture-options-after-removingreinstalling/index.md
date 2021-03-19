+++
type = "question"
title = "Capture filter remains in capture options after removing/reinstalling"
description = '''At some point before a capture I added a capture filter in the capture options window (I don&#x27;t recall that I ever saved the filter itself). After closing and reopening wireshark, the capture filter remains in the capture options window. I have removed wireshark (running on Windows XP), reinstalled, ...'''
date = "2011-03-09T11:15:00Z"
lastmod = "2011-03-09T12:23:00Z"
weight = 2735
keywords = [ "capture", "options" ]
aliases = [ "/questions/2735" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Capture filter remains in capture options after removing/reinstalling](/questions/2735/capture-filter-remains-in-capture-options-after-removingreinstalling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2735-score" class="post-score" title="current number of votes">0</div><span id="post-2735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>At some point before a capture I added a capture filter in the capture options window (I don't recall that I ever saved the filter itself). After closing and reopening wireshark, the capture filter remains in the capture options window. I have removed wireshark (running on Windows XP), reinstalled, and the same filter still appears. I downgraded and upgraded wireshark versions with no luck- the filter remains. I've searched the registry but cannot find any reg entry that exist with this filter in it. I've copied cfilters from other systems, but that filter keeps showing up. Any ideas of how to get rid of it without reloading the OS?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-options" rel="tag" title="see questions tagged &#39;options&#39;">options</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '11, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/79fe867941d98b77ab6421f4c13c989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ethertype0x9000&#39;s gravatar image" /><p><span>ethertype0x9000</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ethertype0x9000 has no accepted answers">0%</span></p></div></div><div id="comments-container-2735" class="comments-container"></div><div id="comment-tools-2735" class="comment-tools"></div><div class="clear"></div><div id="comment-2735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2737"></span>

<div id="answer-container-2737" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2737-score" class="post-score" title="current number of votes">1</div><span id="post-2737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ethertype0x9000 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you by any chance accessing the system you run Wireshark on remotely (by RDP or X over SSH)? In that case, Wireshark will fill in a default filter to not capture the RDP or SSH traffic. That's something built into Wireshark and it is not configurable (at the moment).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '11, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2737" class="comments-container"><span id="2739"></span><div id="comment-2739" class="comment"><div id="post-2739-score" class="comment-score"></div><div class="comment-text"><p>Actually yes. The capture filter is 'not tcp port 3389'. After logging into the same box via the console and launching wireshark, the capture filter is, of course, not there. Many thanks SYNbit.</p></div><div id="comment-2739-info" class="comment-info"><span class="comment-age">(09 Mar '11, 11:56)</span> <span class="comment-user userinfo">ethertype0x9000</span></div></div><span id="2740"></span><div id="comment-2740" class="comment"><div id="post-2740-score" class="comment-score"></div><div class="comment-text"><p>You're welcome!</p><p>(I converted your "answer" into a "comment" as that's the way this site works, see the FAQ. You might also want to "accept" the answer by clicking on the check-mark next to the answer, that way the question will not show up in the list of unanswered questions :-))</p></div><div id="comment-2740-info" class="comment-info"><span class="comment-age">(09 Mar '11, 12:11)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="2741"></span><div id="comment-2741" class="comment"><div id="post-2741-score" class="comment-score"></div><div class="comment-text"><p>Noted and again, thanks for the help.</p></div><div id="comment-2741-info" class="comment-info"><span class="comment-age">(09 Mar '11, 12:23)</span> <span class="comment-user userinfo">ethertype0x9000</span></div></div></div><div id="comment-tools-2737" class="comment-tools"></div><div class="clear"></div><div id="comment-2737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

