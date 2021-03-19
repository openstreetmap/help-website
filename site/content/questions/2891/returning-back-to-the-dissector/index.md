+++
type = "question"
title = "Returning back to the dissector"
description = '''I have my own dissector above tcp.  I have a signature to detect my packet. If it is not present it should return back to the wireshark where it will decide which port it should go to. How can I do this? Thanks in advance'''
date = "2011-03-17T02:05:00Z"
lastmod = "2011-03-17T06:21:00Z"
weight = 2891
keywords = [ "return", "port", "tcp" ]
aliases = [ "/questions/2891" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Returning back to the dissector](/questions/2891/returning-back-to-the-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2891-score" class="post-score" title="current number of votes">0</div><span id="post-2891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have my own dissector above tcp. I have a signature to detect my packet. If it is not present it should return back to the wireshark where it will decide which port it should go to. How can I do this? Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-return" rel="tag" title="see questions tagged &#39;return&#39;">return</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '11, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/46023e482c60329a251a137848f8f5f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niks3089&#39;s gravatar image" /><p><span>niks3089</span><br />
<span class="score" title="21 reputation points">21</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niks3089 has no accepted answers">0%</span></p></div></div><div id="comments-container-2891" class="comments-container"><span id="2892"></span><div id="comment-2892" class="comment"><div id="post-2892-score" class="comment-score"></div><div class="comment-text"><p>currently the port number is 80</p></div><div id="comment-2892-info" class="comment-info"><span class="comment-age">(17 Mar '11, 02:12)</span> <span class="comment-user userinfo">niks3089</span></div></div></div><div id="comment-tools-2891" class="comment-tools"></div><div class="clear"></div><div id="comment-2891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2900"></span>

<div id="answer-container-2900" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2900-score" class="post-score" title="current number of votes">1</div><span id="post-2900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If this is a heuristic or new-style dissector, just return FALSE or 0 to tell Wireshark that the packet is not for your protocol. Wireshark will figure out which other dissector(s) to (try to) give it to.</p><p>[Update] Don't forget to drop by and Accept this answer if it answered your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '11, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Mar '12, 07:05</strong> </span></p></div></div><div id="comments-container-2900" class="comments-container"></div><div id="comment-tools-2900" class="comment-tools"></div><div class="clear"></div><div id="comment-2900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

