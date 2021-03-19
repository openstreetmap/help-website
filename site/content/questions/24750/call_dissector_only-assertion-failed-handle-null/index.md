+++
type = "question"
title = "(call_dissector_only): assertion failed: (handle != NULL)"
description = '''i , when i capture packets through tshark i am getting the following assertion.  ERROR : file packet.c: line 1831 (call_dissector_only): assertion failed: (handle != NULL) aborting... Command used: tshark -i eth0 -R radius -V Please help ,how this issue can be fixed'''
date = "2013-09-16T06:14:00Z"
lastmod = "2013-09-16T22:37:00Z"
weight = 24750
keywords = [ "tshark" ]
aliases = [ "/questions/24750" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [(call\_dissector\_only): assertion failed: (handle != NULL)](/questions/24750/call_dissector_only-assertion-failed-handle-null)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24750-score" class="post-score" title="current number of votes">0</div><span id="post-24750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i , when i capture packets through tshark i am getting the following assertion.</p><p><strong>ERROR</strong> : file packet.c: line 1831 (call_dissector_only): assertion failed: (handle != NULL) aborting...</p><p>Command used: tshark -i eth0 -R radius -V</p><p>Please help ,how this issue can be fixed</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '13, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/0c1a667d74db34a1ba8c5cec1558e667?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="syed&#39;s gravatar image" /><p><span>syed</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="syed has no accepted answers">0%</span></p></div></div><div id="comments-container-24750" class="comments-container"><span id="24751"></span><div id="comment-24751" class="comment"><div id="post-24751-score" class="comment-score">1</div><div class="comment-text"><p>Can you tell us which version of tshark you're using? You can run <code>tshark -v</code> for this information.</p></div><div id="comment-24751-info" class="comment-info"><span class="comment-age">(16 Sep '13, 06:15)</span> <span class="comment-user userinfo">zachad</span></div></div><span id="24752"></span><div id="comment-24752" class="comment"><div id="post-24752-score" class="comment-score"></div><div class="comment-text"><p>wireshark -1.4.3</p></div><div id="comment-24752-info" class="comment-info"><span class="comment-age">(16 Sep '13, 06:23)</span> <span class="comment-user userinfo">syed</span></div></div></div><div id="comment-tools-24750" class="comment-tools"></div><div class="clear"></div><div id="comment-24750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24754"></span>

<div id="answer-container-24754" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24754-score" class="post-score" title="current number of votes">1</div><span id="post-24754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can you use a more up to date version of Wireshark? This might fix the issue, and you'll get the benefit of all the other work that's been put into the latest versions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '13, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24754" class="comments-container"><span id="24757"></span><div id="comment-24757" class="comment"><div id="post-24757-score" class="comment-score"></div><div class="comment-text"><p>ya but this has been integrated in some other code base so cant directly upgrade .Need to fix in this version only. Can you please suggest some method /provide idea why this happens and how to analyze the issue (or) if the fix has gone u can provide me fix details.</p></div><div id="comment-24757-info" class="comment-info"><span class="comment-age">(16 Sep '13, 06:54)</span> <span class="comment-user userinfo">syed</span></div></div><span id="24765"></span><div id="comment-24765" class="comment"><div id="post-24765-score" class="comment-score"></div><div class="comment-text"><p>More to the point, Wireshark 1.4.3 was released on January 11, 2011, over 2 1/2 years ago, and Wireshark 1.4 reached End Of Life on August 30, 2012, over 1 year ago.</p></div><div id="comment-24765-info" class="comment-info"><span class="comment-age">(16 Sep '13, 07:39)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="24766"></span><div id="comment-24766" class="comment"><div id="post-24766-score" class="comment-score"></div><div class="comment-text"><p>I think you'll be on your own here, 1.4.3 is no longer supported. You might have a look though the Wireshark <a href="https://bugs.wireshark.org/bugzilla/">Bugzilla</a> to see if anything shows up.</p><p>If you at least try a newer version with your capture you should be able to tell if it has been fixed in later versions, and then you can try to narrow down which version it was and then look for relevant changes fir the svn repository.</p></div><div id="comment-24766-info" class="comment-info"><span class="comment-age">(16 Sep '13, 07:40)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="24771"></span><div id="comment-24771" class="comment"><div id="post-24771-score" class="comment-score"></div><div class="comment-text"><blockquote><p>ya but this <strong>has been integrated in some other code base</strong> so cant directly upgrade .</p></blockquote><p>and maybe the Wireshark code has been modified as well (by 'them'), which could cause that specific problem.</p><p><span>@syed</span>: You are not using your own (or a modified) Radius dissector, are you?</p><blockquote><p>Can you please suggest some method /provide idea why this happens and how to analyze the issue</p></blockquote><p>I think it boils down to: Debugger and code review.</p></div><div id="comment-24771-info" class="comment-info"><span class="comment-age">(16 Sep '13, 08:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="24795"></span><div id="comment-24795" class="comment"><div id="post-24795-score" class="comment-score"></div><div class="comment-text"><p>we are not modifying any radius dissector. It is same as given by wireshark.</p></div><div id="comment-24795-info" class="comment-info"><span class="comment-age">(16 Sep '13, 22:37)</span> <span class="comment-user userinfo">syed</span></div></div></div><div id="comment-tools-24754" class="comment-tools"></div><div class="clear"></div><div id="comment-24754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

