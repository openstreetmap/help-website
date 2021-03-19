+++
type = "question"
title = "Porting wireshark dissector from linux to windows machine..??"
description = '''I have some wireshark dissectors on linux m/c and i want to port these disscetors to windows m/c... so please tell me the procedure for that..'''
date = "2013-03-21T22:42:00Z"
lastmod = "2013-03-25T22:12:00Z"
weight = 19742
keywords = [ "wireshark" ]
aliases = [ "/questions/19742" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Porting wireshark dissector from linux to windows machine..??](/questions/19742/porting-wireshark-dissector-from-linux-to-windows-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19742-score" class="post-score" title="current number of votes">0</div><span id="post-19742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some wireshark dissectors on linux m/c and i want to port these disscetors to windows m/c... so please tell me the procedure for that..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '13, 22:42</strong></p><img src="https://secure.gravatar.com/avatar/ede7d1c603f2c4a9305de8d3ef8ecbc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neha&#39;s gravatar image" /><p><span>neha</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neha has no accepted answers">0%</span></p></div></div><div id="comments-container-19742" class="comments-container"><span id="19743"></span><div id="comment-19743" class="comment"><div id="post-19743-score" class="comment-score"></div><div class="comment-text"><p>Build-in dissectors or plugin?</p></div><div id="comment-19743-info" class="comment-info"><span class="comment-age">(21 Mar '13, 23:57)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-19742" class="comment-tools"></div><div class="clear"></div><div id="comment-19742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19744"></span>

<div id="answer-container-19744" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19744-score" class="post-score" title="current number of votes">2</div><span id="post-19744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As dissector code is OS independent, you would just need to compile it on Windows. You have to set up a windows build environment (as described in the README.developer file).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 23:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Mar '13, 03:15</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-19744" class="comments-container"><span id="19748"></span><div id="comment-19748" class="comment"><div id="post-19748-score" class="comment-score"></div><div class="comment-text"><p>For detailed information on setting up a Windows build environment see:</p><p><a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html</a></p></div><div id="comment-19748-info" class="comment-info"><span class="comment-age">(22 Mar '13, 05:29)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="19750"></span><div id="comment-19750" class="comment"><div id="post-19750-score" class="comment-score"></div><div class="comment-text"><p>And follow it to the letter as any deviation will result in problems :-)</p></div><div id="comment-19750-info" class="comment-info"><span class="comment-age">(22 Mar '13, 06:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="19796"></span><div id="comment-19796" class="comment"><div id="post-19796-score" class="comment-score"></div><div class="comment-text"><p>as i am doing ds on Windows XP then also do i have to follow the same steps?</p></div><div id="comment-19796-info" class="comment-info"><span class="comment-age">(25 Mar '13, 00:03)</span> <span class="comment-user userinfo">neha</span></div></div><span id="19802"></span><div id="comment-19802" class="comment"><div id="post-19802-score" class="comment-score"></div><div class="comment-text"><p>Yes. Exactly as written.</p></div><div id="comment-19802-info" class="comment-info"><span class="comment-age">(25 Mar '13, 05:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="19827"></span><div id="comment-19827" class="comment"><div id="post-19827-score" class="comment-score"></div><div class="comment-text"><p>okk.. thank you grahamb.. i will try.. if there will be some problem i will ask again.. ;-)</p></div><div id="comment-19827-info" class="comment-info"><span class="comment-age">(25 Mar '13, 22:12)</span> <span class="comment-user userinfo">neha</span></div></div></div><div id="comment-tools-19744" class="comment-tools"></div><div class="clear"></div><div id="comment-19744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

