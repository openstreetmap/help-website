+++
type = "question"
title = "Windows vs. Linux - difference in dissection of Profinet traffic"
description = '''I&#x27;m opening the same pcap in windows and in linux, and I get different results.  Protocol pn_rt / pn_io is shown in the linux version as fake-field-wrapper (DATA) and it is fully parsed in the windows version (both 2.0.1) any idea why it happens ? '''
date = "2016-08-09T00:40:00Z"
lastmod = "2016-08-09T03:11:00Z"
weight = 54685
keywords = [ "windows", "dissection", "profinet", "linux" ]
aliases = [ "/questions/54685" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Windows vs. Linux - difference in dissection of Profinet traffic](/questions/54685/windows-vs-linux-difference-in-dissection-of-profinet-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54685-score" class="post-score" title="current number of votes">0</div><span id="post-54685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm opening the same pcap in windows and in linux, and I get different results. Protocol pn_rt / pn_io is shown in the linux version as fake-field-wrapper (DATA) and it is fully parsed in the windows version (both 2.0.1) any idea why it happens ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-dissection" rel="tag" title="see questions tagged &#39;dissection&#39;">dissection</span> <span class="post-tag tag-link-profinet" rel="tag" title="see questions tagged &#39;profinet&#39;">profinet</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '16, 00:40</strong></p><img src="https://secure.gravatar.com/avatar/b50e05a5f1954d250dd908dacce081c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kdani&#39;s gravatar image" /><p><span>kdani</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kdani has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Aug '16, 02:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54685" class="comments-container"></div><div id="comment-tools-54685" class="comment-tools"></div><div class="clear"></div><div id="comment-54685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54688"></span>

<div id="answer-container-54688" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54688-score" class="post-score" title="current number of votes">1</div><span id="post-54688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kdani has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Profinet is dissected by a plugin, sounds as though the plugin isn't being loaded on Linux. Does the Profinet plugin show up in the Help -&gt; About Wireshark -&gt; Plugins list?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '16, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-54688" class="comments-container"><span id="54692"></span><div id="comment-54692" class="comment"><div id="post-54692-score" class="comment-score"></div><div class="comment-text"><p>I think you got it right. checking.</p></div><div id="comment-54692-info" class="comment-info"><span class="comment-age">(09 Aug '16, 03:11)</span> <span class="comment-user userinfo">kdani</span></div></div></div><div id="comment-tools-54688" class="comment-tools"></div><div class="clear"></div><div id="comment-54688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54686"></span>

<div id="answer-container-54686" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54686-score" class="post-score" title="current number of votes">1</div><span id="post-54686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is most likely caused by different Wireshark profile settings, e.g. reassembly preferences. Can you create a new profile (meaning, Wireshark will run with default settings) on both systems and compare again? If the results are identical with brand new profiles, you have something that's different in your existing settings - otherwise it's really Wireshark that's doing something different.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '16, 01:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-54686" class="comments-container"><span id="54687"></span><div id="comment-54687" class="comment"><div id="post-54687-score" class="comment-score"></div><div class="comment-text"><p>I've copied the preference file from the windows machine to the linux machine - same results. is there anything else ? I am installing a clean linux now to test a clean wireshark installation. will report soon.</p></div><div id="comment-54687-info" class="comment-info"><span class="comment-age">(09 Aug '16, 01:26)</span> <span class="comment-user userinfo">kdani</span></div></div></div><div id="comment-tools-54686" class="comment-tools"></div><div class="clear"></div><div id="comment-54686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

