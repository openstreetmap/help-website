+++
type = "question"
title = "question on ARP"
description = '''Can someone help me, wht this question mean? and how can i get the answer?  How many bytes from the very beginning of the Ethernet frame does the ARP opcode field begin? '''
date = "2014-02-14T22:15:00Z"
lastmod = "2014-02-15T03:14:00Z"
weight = 29880
keywords = [ "arp" ]
aliases = [ "/questions/29880" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [question on ARP](/questions/29880/question-on-arp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29880-score" class="post-score" title="current number of votes">0</div><span id="post-29880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone help me, wht this question mean? and how can i get the answer? How many bytes from the very beginning of the Ethernet frame does the ARP opcode field begin?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '14, 22:15</strong></p><img src="https://secure.gravatar.com/avatar/e80797780f41f6aa7fe5cd8a7f3aebbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="popo88&#39;s gravatar image" /><p><span>popo88</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="popo88 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-29880" class="comments-container"><span id="29883"></span><div id="comment-29883" class="comment"><div id="post-29883-score" class="comment-score">1</div><div class="comment-text"><p>I found the answer to that question here</p><blockquote><p><a href="http://bit.ly/1c91E9t">http://bit.ly/1c91E9t</a></p></blockquote></div><div id="comment-29883-info" class="comment-info"><span class="comment-age">(15 Feb '14, 03:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29880" class="comment-tools"></div><div class="clear"></div><div id="comment-29880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29881"></span>

<div id="answer-container-29881" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29881-score" class="post-score" title="current number of votes">0</div><span id="post-29881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Should be easy enough:</p><ol><li>Run Wireshark</li><li>capture on your network card</li><li>wait until you see an ARP packet</li><li>expand the ARP header decode of that packet</li><li>look for the opcode field</li><li>determine the offset</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '14, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-29881" class="comments-container"></div><div id="comment-tools-29881" class="comment-tools"></div><div class="clear"></div><div id="comment-29881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

