+++
type = "question"
title = "Error while compiling Wireshark source : epan/.libs/libwireshark.so: undefined reference to `proto_reg_handoff_PROTOABBREV&#x27;"
description = '''I have written a new dissector for wireshark. I have made changes to Makefile.common and CMakelist.txt. Now when I try to compile the Wireshark source, I get this error. epan/.libs/libwireshark.so: undefined reference to proto_reg_handoff_PROTOABBREV&#x27; collect2: ld returned 1 exit status make[2]: ***...'''
date = "2011-01-31T04:53:00Z"
lastmod = "2011-01-31T22:25:00Z"
weight = 2037
keywords = [ "wireshark" ]
aliases = [ "/questions/2037" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error while compiling Wireshark source : epan/.libs/libwireshark.so: undefined reference to \`proto\_reg\_handoff\_PROTOABBREV'](/questions/2037/error-while-compiling-wireshark-source-epanlibslibwiresharkso-undefined-reference-to-proto_reg_handoff_protoabbrev)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2037-score" class="post-score" title="current number of votes">0</div><span id="post-2037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have written a new dissector for wireshark. I have made changes to Makefile.common and CMakelist.txt. Now when I try to compile the Wireshark source, I get this error.</p><p>epan/.libs/libwireshark.so: undefined reference to <code>proto_reg_handoff_PROTOABBREV' collect2: ld returned 1 exit status make[2]: *** [wireshark] Error 1 make[2]: Leaving directory</code>/home/sid/ws/wireshark-1.4.3' make[1]: <strong><em>[all-recursive] Error 1 make[1]: Leaving directory `/home/sid/ws/wireshark-1.4.3' make:</em></strong> [all] Error 2</p><p>Any suggestions??</p><p>Thanks, Sidharth</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '11, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p><span>sid</span><br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-2037" class="comments-container"></div><div id="comment-tools-2037" class="comment-tools"></div><div class="clear"></div><div id="comment-2037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2047"></span>

<div id="answer-container-2047" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2047-score" class="post-score" title="current number of votes">0</div><span id="post-2047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>./autogen.sh
./configure
make</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '11, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2047" class="comments-container"><span id="2056"></span><div id="comment-2056" class="comment"><div id="post-2056-score" class="comment-score"></div><div class="comment-text"><p>thanks jaap,</p><p>i have done the same thing..after the make i get this error..any help??</p></div><div id="comment-2056-info" class="comment-info"><span class="comment-age">(31 Jan '11, 20:54)</span> <span class="comment-user userinfo">sid</span></div></div><span id="2058"></span><div id="comment-2058" class="comment"><div id="post-2058-score" class="comment-score"></div><div class="comment-text"><p>Is the symbol 'proto_reg_handoff_PROTOABBREV' literally present in your dissector code?</p></div><div id="comment-2058-info" class="comment-info"><span class="comment-age">(31 Jan '11, 22:25)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-2047" class="comment-tools"></div><div class="clear"></div><div id="comment-2047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

