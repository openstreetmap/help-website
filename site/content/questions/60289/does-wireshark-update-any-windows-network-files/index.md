+++
type = "question"
title = "Does Wireshark update any windows network files?"
description = '''It has come to my attention here at work, when one of the programmers here was testing calls to an application he noticed that it takes 270ms to get a response. He then installed Wireshark and ran the same test calls to the same app and the response time was 200ms faster. So when I found out about t...'''
date = "2017-03-23T12:44:00Z"
lastmod = "2017-03-25T05:03:00Z"
weight = 60289
keywords = [ "network" ]
aliases = [ "/questions/60289" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark update any windows network files?](/questions/60289/does-wireshark-update-any-windows-network-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60289-score" class="post-score" title="current number of votes">0</div><span id="post-60289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It has come to my attention here at work, when one of the programmers here was testing calls to an application he noticed that it takes 270ms to get a response. He then installed Wireshark and ran the same test calls to the same app and the response time was 200ms faster. So when I found out about this I tested on 2 machines one with Wireshark and one without. The one without, the test calls responded at 270ms. The one with Wireshark responded at 70ms.</p><p>So my question is what network files does Wireshark update that would cause such a change?</p><p>Thank you, Greg Forster Sr. Network Engineer<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '17, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/e6ade7d7ab0de0be8923baad39ade6f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gforster67&#39;s gravatar image" /><p><span>gforster67</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gforster67 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-60289" class="comments-container"></div><div id="comment-tools-60289" class="comment-tools"></div><div class="clear"></div><div id="comment-60289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60290"></span>

<div id="answer-container-60290" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60290-score" class="post-score" title="current number of votes">0</div><span id="post-60290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not entirely sure what you mean by "network files" - probably you talk about the system's network stack?</p><p>The most common reason for things working differently when Wireshark is running is that it enables promiscuous mode on the network card it captures on. That results in packets being accepted that otherwise would not have been, for which the most common reason is a wrong destination MAC address. Or in other words: if a packet arrives with a MAC address different than the one of the network card, it will not be accepted unless Wireshark is capturing.</p><p>So my advice would be this:</p><ul><li>check the destination MAC addresses of the incoming packets. Compare them to the network card MAC. Almost always the MAC is slightly off.</li><li>if the MAC is correct, check if the application is also faster when Wireshark isn't running. If it's also faster without Wireshark running (but being installed), something in the network stack is behaving differently.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '17, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Mar '17, 12:54</strong> </span></p></div></div><div id="comments-container-60290" class="comments-container"><span id="60291"></span><div id="comment-60291" class="comment"><div id="post-60291-score" class="comment-score"></div><div class="comment-text"><p>Jasper,</p><p>I understand your answer and it is not when Wireshark is running vs. not running. It is when Wireshark is installed vs. not installed that this is happening.</p></div><div id="comment-60291-info" class="comment-info"><span class="comment-age">(23 Mar '17, 13:06)</span> <span class="comment-user userinfo">gforster67</span></div></div><span id="60292"></span><div id="comment-60292" class="comment"><div id="post-60292-score" class="comment-score"></div><div class="comment-text"><p>Interesting, I think that's the first time I hear that. Is this Windows, and WinPCAP, or are you using npcap instead?</p><p>If it's Windows: can you check if you can uninstall Wireshark but keep WinPCAP installed to check if it still makes a difference?</p></div><div id="comment-60292-info" class="comment-info"><span class="comment-age">(23 Mar '17, 13:12)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="60293"></span><div id="comment-60293" class="comment"><div id="post-60293-score" class="comment-score"></div><div class="comment-text"><p>I am working on that now as soon as I am done I will let you know.</p></div><div id="comment-60293-info" class="comment-info"><span class="comment-age">(23 Mar '17, 13:14)</span> <span class="comment-user userinfo">gforster67</span></div></div><span id="60310"></span><div id="comment-60310" class="comment"><div id="post-60310-score" class="comment-score"></div><div class="comment-text"><p>It looks like WinPCAP is what makes the change. With WinPCAP uninstalled the response is 270ms-300ms, with WinPCAP installed the response time changes to 50ms-75ms.</p></div><div id="comment-60310-info" class="comment-info"><span class="comment-age">(24 Mar '17, 05:09)</span> <span class="comment-user userinfo">gforster67</span></div></div><span id="60318"></span><div id="comment-60318" class="comment"><div id="post-60318-score" class="comment-score"></div><div class="comment-text"><p>Hm okay, in this case we need someone who knows what WinPCAP does exactly... I'll see if I can get someone to take a look at this.</p></div><div id="comment-60318-info" class="comment-info"><span class="comment-age">(24 Mar '17, 14:27)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="60320"></span><div id="comment-60320" class="comment not_top_scorer"><div id="post-60320-score" class="comment-score"></div><div class="comment-text"><p>If memory serves me right, WinPCAP installs a service. Depending on your settings, this service may be started automatically (default?) or not. What happens if you stop that service?</p></div><div id="comment-60320-info" class="comment-info"><span class="comment-age">(24 Mar '17, 23:48)</span> <span class="comment-user userinfo">jmayer</span></div></div><span id="60321"></span><div id="comment-60321" class="comment not_top_scorer"><div id="post-60321-score" class="comment-score"></div><div class="comment-text"><p>There's some info <a href="https://www.winpcap.org/docs/docs_412/html/group__NPF.html">here</a> about WinPcap internals, in particular the NPF driver and how it fits in the stack.</p><p>Just guessing out loud, but if installing WinPcap improves latency, I suspect that it might be inadvertently "removing" or "diverting" something else from the stack that's adding the latency.</p></div><div id="comment-60321-info" class="comment-info"><span class="comment-age">(25 Mar '17, 05:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-60290" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-60290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

