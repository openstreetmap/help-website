+++
type = "question"
title = "DVB-S2 dissector missing in 1.8.3"
description = '''I&#x27;m not able to find the DVB-S2 protocol in the protocol setting dialogue in Wireshark 1.8.3, consequently, I&#x27;m not able to enable it. However, it does exist in my local build(rev:46080). DVB-S2 dissector seems to have been created during rev:44110, whereas 1.8.3 is svn rev 45256. What is the reason...'''
date = "2012-11-23T08:43:00Z"
lastmod = "2012-11-23T16:12:00Z"
weight = 16246
keywords = [ "dissector", "dvb-s2", "wireshark" ]
aliases = [ "/questions/16246" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [DVB-S2 dissector missing in 1.8.3](/questions/16246/dvb-s2-dissector-missing-in-183)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16246-score" class="post-score" title="current number of votes">0</div><span id="post-16246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm not able to find the DVB-S2 protocol in the protocol setting dialogue in Wireshark 1.8.3, consequently, I'm not able to enable it. However, it does exist in my local build(rev:46080). DVB-S2 dissector seems to have been created during rev:44110, whereas 1.8.3 is svn rev 45256. What is the reason for this? Is there any way I can see DVB-S2 packets in 1.8.3?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-dvb-s2" rel="tag" title="see questions tagged &#39;dvb-s2&#39;">dvb-s2</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '12, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p><span>SidR</span><br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Nov '12, 16:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-16246" class="comments-container"></div><div id="comment-tools-16246" class="comment-tools"></div><div class="clear"></div><div id="comment-16246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16261"></span>

<div id="answer-container-16261" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16261-score" class="post-score" title="current number of votes">1</div><span id="post-16261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SidR has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My understanding of the Release Policy:</p><p>Wireshark 1.8 was release on June 21, 2012<br />
</p><blockquote><p><code>http://wiki.wireshark.org/Development/LifeCycle</code><br />
</p></blockquote><p>According to the Release Policy, no new features are added to a stable release, only bugs will be fixed.</p><blockquote><p><code>http://wiki.wireshark.org/Development/ReleasePolicy</code><br />
</p></blockquote><p>The DVB-S2 dissector was added after June 21, 2012, so it's not included in Wireshark 1.8.</p><blockquote><p><code>https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7518</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '12, 14:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Nov '12, 14:05</strong> </span></p></div></div><div id="comments-container-16261" class="comments-container"><span id="16263"></span><div id="comment-16263" class="comment"><div id="post-16263-score" class="comment-score">1</div><div class="comment-text"><p>(Note also that SVN revision numbers are shared between the trunk and branches, so a build with a lower SVN revision number could have more features than a build with a higher revision number, even if no features were removed, because the higher revision number might be on a branch that never got the new features. )</p></div><div id="comment-16263-info" class="comment-info"><span class="comment-age">(23 Nov '12, 16:12)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-16261" class="comment-tools"></div><div class="clear"></div><div id="comment-16261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

