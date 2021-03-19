+++
type = "question"
title = "Issues with VALS and/or RVALS macros when used in custom dissector"
description = '''Recently found that Wireshark would completely crash when loading certain capture files which activated a custom dissector. After some basic debugging I determined that removing the use of those macros from my definition of static &quot;hf_register_info&quot; data made the problem go away. This sounds a lot l...'''
date = "2017-06-21T07:02:00Z"
lastmod = "2017-06-21T13:10:00Z"
weight = 62207
keywords = [ "vals", "hf_register_info", "rvals", "dissector" ]
aliases = [ "/questions/62207" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Issues with VALS and/or RVALS macros when used in custom dissector](/questions/62207/issues-with-vals-andor-rvals-macros-when-used-in-custom-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62207-score" class="post-score" title="current number of votes">0</div><span id="post-62207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Recently found that Wireshark would completely crash when loading certain capture files which activated a custom dissector. After some basic debugging I determined that removing the use of those macros from my definition of static "hf_register_info" data made the problem go away. This sounds a lot like a coincidence (e.g. change just masked a bug) but haven't been able to put my finger on alternative cause just yet.</p><p>In most cases Wireshark would just crash upon loading/dissecting but I also did find instances where the crash would not occur until I selected a certain packet. This sort of implies that the act of de-referencing the array or displaying the text is causing the issue, so I am pursuing that angle, but wanted to see if there were any known issues or limitations with the use of the VALS and/or RVALS arrays.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vals" rel="tag" title="see questions tagged &#39;vals&#39;">vals</span> <span class="post-tag tag-link-hf_register_info" rel="tag" title="see questions tagged &#39;hf_register_info&#39;">hf_register_info</span> <span class="post-tag tag-link-rvals" rel="tag" title="see questions tagged &#39;rvals&#39;">rvals</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '17, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/f5a6a32440657fdf63b9db18f3922c70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wittynickname&#39;s gravatar image" /><p><span>wittynickname</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wittynickname has one accepted answer">50%</span></p></div></div><div id="comments-container-62207" class="comments-container"><span id="62209"></span><div id="comment-62209" class="comment"><div id="post-62209-score" class="comment-score"></div><div class="comment-text"><p>Never mind, pretty sure I found it... my arrays were not terminated with {0, NULL} which seems to be the convention.</p></div><div id="comment-62209-info" class="comment-info"><span class="comment-age">(21 Jun '17, 07:23)</span> <span class="comment-user userinfo">wittynickname</span></div></div></div><div id="comment-tools-62207" class="comment-tools"></div><div class="clear"></div><div id="comment-62207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62210"></span>

<div id="answer-container-62210" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62210-score" class="post-score" title="current number of votes">0</div><span id="post-62210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wittynickname has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Slowly removing egg from face...</p><p>Confirmed, these lists must be terminated with either {0, NULL} or {0,0,NULL} entry as appropriate.</p><p>There appear to be some additional MACROs to help with this but none of the examples I looked at in the standard source base used them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '17, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/f5a6a32440657fdf63b9db18f3922c70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wittynickname&#39;s gravatar image" /><p><span>wittynickname</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wittynickname has one accepted answer">50%</span></p></div></div><div id="comments-container-62210" class="comments-container"><span id="62219"></span><div id="comment-62219" class="comment"><div id="post-62219-score" class="comment-score">1</div><div class="comment-text"><p>FYI: You might want to run the various perl scripts such as <code>checkAPIs.pl</code>, <code>checkfiltername.pl</code>, and <code>checkhf.pl</code> against your dissectors to help automatically catch errors such as this.</p><p>For example, I temporarily removed the <code>{0,NULL}</code> value string terminator from one of the IP dissector's value strings and ran <code>checkAPIs.pl</code> against it. Here's the output:</p><pre><code>perl tools\checkAPIs.pl epan/dissectors/packet-ip.c
Error: epan/dissectors/packet-ip.c        : {0, NULL} is required as the last value_string array entry: value_string ipopt_type_class_vals[]</code></pre></div><div id="comment-62219-info" class="comment-info"><span class="comment-age">(21 Jun '17, 13:10)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-62210" class="comment-tools"></div><div class="clear"></div><div id="comment-62210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

