+++
type = "question"
title = "TCP OPTION 0x26 added to SYN packet"
description = '''Hello, I just came across this very strange unknown TCP option: Options: (28 bytes), Maximum segment size, No-Operation (NOP), No-Operation (NOP), SACK permitted, End of Option List (EOL)  Maximum segment size: 1460 bytes  No-Operation (NOP)  No-Operation (NOP)  TCP SACK Permitted Option: True  Unkn...'''
date = "2013-05-13T06:00:00Z"
lastmod = "2013-05-13T14:37:00Z"
weight = 21112
keywords = [ "option", "tcp" ]
aliases = [ "/questions/21112" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [TCP OPTION 0x26 added to SYN packet](/questions/21112/tcp-option-0x26-added-to-syn-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21112-score" class="post-score" title="current number of votes">0</div><span id="post-21112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I just came across this very strange unknown TCP option:</p><p>Options: (28 bytes), Maximum segment size, No-Operation (NOP), No-Operation (NOP), SACK permitted, End of Option List (EOL)</p><pre><code>    Maximum segment size: 1460 bytes
    No-Operation (NOP)
    No-Operation (NOP)
    TCP SACK Permitted Option: True
    Unknown (0x26) (18 bytes)
    End of Option List (EOL)</code></pre><p>It is 18 bytes long and contains the MAC address and IP address of the PC:</p><p>26|12|<strong>18|a9|05|cf|58</strong>|1a|cd|01|<strong>0a|63|c0|91</strong>|22|00|00|00</p><p>Anyone any idea ? SHould i be thinking virus ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-option" rel="tag" title="see questions tagged &#39;option&#39;">option</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '13, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/4e1f11275965a4ecbc9abef70305008a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geert&#39;s gravatar image" /><p><span>geert</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geert has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '13, 06:01</strong> </span></p></div></div><div id="comments-container-21112" class="comments-container"></div><div id="comment-tools-21112" class="comment-tools"></div><div class="clear"></div><div id="comment-21112-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="21119"></span>

<div id="answer-container-21119" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21119-score" class="post-score" title="current number of votes">1</div><span id="post-21119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have found it myself. It seems to be an option inserted by JunOS Pulse VPN software when you enable JunOS WAN optimisation. problem is that it changes all packets even when the software is not active and it is incompatible with Riverbed optimisation because it takes to much space in the TCP option headers :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '13, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/4e1f11275965a4ecbc9abef70305008a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geert&#39;s gravatar image" /><p><span>geert</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geert has no accepted answers">0%</span></p></div></div><div id="comments-container-21119" class="comments-container"><span id="21120"></span><div id="comment-21120" class="comment"><div id="post-21120-score" class="comment-score"></div><div class="comment-text"><p>As I said, a WAN acceleration solution ;-)</p></div><div id="comment-21120-info" class="comment-info"><span class="comment-age">(13 May '13, 14:37)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-21119" class="comment-tools"></div><div class="clear"></div><div id="comment-21119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21113"></span>

<div id="answer-container-21113" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21113-score" class="post-score" title="current number of votes">0</div><span id="post-21113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's probably a load balancer (or a WAN accelerator) that uses this feature to add information about the original client connection (IP and MAC) to the load balanced backend server (or the next lb).</p><p>See a similar question: <a href="http://ask.wireshark.org/questions/20697/tcp-option-171-added-in-syn-packet">http://ask.wireshark.org/questions/20697/tcp-option-171-added-in-syn-packet</a></p><p>What is the MAC address of the packet. Maybe the vendor code of the MAC address reveals a possible load balancing (or WAN acceleration) product.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '13, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '13, 06:09</strong> </span></p></div></div><div id="comments-container-21113" class="comments-container"></div><div id="comment-tools-21113" class="comment-tools"></div><div class="clear"></div><div id="comment-21113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21114"></span>

<div id="answer-container-21114" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21114-score" class="post-score" title="current number of votes">0</div><span id="post-21114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>According to <a href="http://www.iana.org/assignments/tcp-parameters/tcp-parameters.xml">http://www.iana.org/assignments/tcp-parameters/tcp-parameters.xml</a> this option is a compression setting. Looks like the client has some kind of unusual/experimental stack setup and tries to negotiate/establish additional TCP parameters.</p><p>I don't think this is a virus.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '13, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21114" class="comments-container"></div><div id="comment-tools-21114" class="comment-tools"></div><div class="clear"></div><div id="comment-21114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

