+++
type = "question"
title = "Unable to display IP addresses correctly..!!"
description = '''I have created a dissector for cluster heartbeat messages. Everything works okay except the IP addresses. An IP of 10.102.1.71 is displayed by the dissector as 71.1.102.10. How correct this? Do i need to apply host to network transformation or the other way around?? And most importantly, how to appl...'''
date = "2011-07-13T04:53:00Z"
lastmod = "2011-07-13T10:41:00Z"
weight = 5013
keywords = [ "wireshark" ]
aliases = [ "/questions/5013" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to display IP addresses correctly..!!](/questions/5013/unable-to-display-ip-addresses-correctly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5013-score" class="post-score" title="current number of votes">0</div><span id="post-5013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have created a dissector for cluster heartbeat messages. Everything works okay except the IP addresses. An IP of 10.102.1.71 is displayed by the dissector as 71.1.102.10.</p><p>How correct this? Do i need to apply host to network transformation or the other way around??</p><p>And most importantly, how to apply that transformation??</p><p>Regards, Sidharth</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '11, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p><span>sid</span><br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-5013" class="comments-container"><span id="5028"></span><div id="comment-5028" class="comment"><div id="post-5028-score" class="comment-score"></div><div class="comment-text"><p>What is the exact code you're using to fetch the IP address and put it into the protocol tree?</p><p>You're not supposed to apply <em>any</em> byte-order transformation to IP addresses.</p></div><div id="comment-5028-info" class="comment-info"><span class="comment-age">(13 Jul '11, 10:41)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-5013" class="comment-tools"></div><div class="clear"></div><div id="comment-5013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5017"></span>

<div id="answer-container-5017" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5017-score" class="post-score" title="current number of votes">0</div><span id="post-5017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Set the final parameter of <code>proto_tree_add_item()</code> for adding the IP addresses to <code>ENC_LITTLE_ENDIAN</code> (or <code>TRUE</code> if you're working with trunk-1.4 based code).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '11, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jul '11, 01:43</strong> </span></p></div></div><div id="comments-container-5017" class="comments-container"></div><div id="comment-tools-5017" class="comment-tools"></div><div class="clear"></div><div id="comment-5017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

