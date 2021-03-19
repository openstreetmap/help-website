+++
type = "question"
title = "How to see traffic from specific internet line?"
description = '''Hi, We have 3 internet connection in our organization, how to see traffic from only one internet line in Wireshark. We are ok with display as well as capture filter.  Thanks.'''
date = "2013-09-30T00:21:00Z"
lastmod = "2013-09-30T02:34:00Z"
weight = 25359
keywords = [ "sniffing", "capture", "interface" ]
aliases = [ "/questions/25359" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to see traffic from specific internet line?](/questions/25359/how-to-see-traffic-from-specific-internet-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25359-score" class="post-score" title="current number of votes">0</div><span id="post-25359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We have 3 internet connection in our organization, how to see traffic from only one internet line in Wireshark. We are ok with display as well as capture filter.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '13, 00:21</strong></p><img src="https://secure.gravatar.com/avatar/4d5a1d4ba48122bcddd239a84b8bf3e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pranitkothari&#39;s gravatar image" /><p><span>pranitkothari</span><br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pranitkothari has one accepted answer">100%</span></p></div></div><div id="comments-container-25359" class="comments-container"></div><div id="comment-tools-25359" class="comment-tools"></div><div class="clear"></div><div id="comment-25359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25363"></span>

<div id="answer-container-25363" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25363-score" class="post-score" title="current number of votes">1</div><span id="post-25363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How to see traffic from specific internet line?</p></blockquote><p>It depends on your setup.</p><p><strong>Case #1:</strong></p><pre><code>ISP1 --------+
             |
ISP2 ------router ---- switch ---- LAN/PC
             |
ISP3---------+</code></pre><p>You need to capture <strong>on</strong> the router to be able to separate the traffic of the three lines (DSL/Cable/whatever), as the router will distribute the traffic over the three lines at its will. If the router does not support packet capturing, your chances to separate the traffic are limited or even bad, as capturing on the physical line to each provider is usually only possible with special hardware (depends on the nature of those links - DSL, Cable, ISDN, T1, etc.).</p><p><strong>Case #2:</strong></p><p>Without thinking about the 'problem' of the default route.</p><pre><code>ISP1 --- router 1 ---+
                     |
ISP2 --- router 2 --switch ---- LAN/PC
                     |
ISP3 --- router 3 ---+</code></pre><p>You need to capture in front of each router (<a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">by using a TAP or port mirroring on the switch</a>) to be able to separate the traffic to the three ISPs.</p><p><strong>++ UPDATE ++</strong></p><p><strong>Case #3:</strong></p><p>See comments below.</p><pre><code>ISP1 router ---+
               |
ISP2 router ---+---router/gateway ---- switch ---- LAN/PC
               |
ISP3 router ---+</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Sep '13, 02:50</strong> </span></p></div></div><div id="comments-container-25363" class="comments-container"><span id="25364"></span><div id="comment-25364" class="comment"><div id="post-25364-score" class="comment-score"></div><div class="comment-text"><p>I am on Gateway, that means all traffic pass through my machine. I just wanted to check, traffic from particular internet line.</p></div><div id="comment-25364-info" class="comment-info"><span class="comment-age">(30 Sep '13, 02:27)</span> <span class="comment-user userinfo">pranitkothari</span></div></div><span id="25367"></span><div id="comment-25367" class="comment"><div id="post-25367-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I am on Gateway, that means all traffic pass through my machine.</p></blockquote><p>What does that mean? Your PC is the router for all three internet lines? So, Case #1 is true for your environment, with your PC being the router?</p><p>If that is true, your PC should have either</p><ul><li>three interfaces which you can capture on to separate the traffic (please add more information about the interfaces and your OS on the gateway in this case)</li></ul><p>or</p><ul><li>three gateways where it distributes traffic to (e.g. 3 DSL routers) like Case #3 (see the UPDATE in may answer). In that case, you can use the MAC address of the routers to distinguish the traffic</li></ul><p>Capture Filter: <code>ether host 00:01:02:03:04:11</code><br />
Display Filter: <code>eth.addr eq 00:01:02:03:04:11</code></p></div><div id="comment-25367-info" class="comment-info"><span class="comment-age">(30 Sep '13, 02:34)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-25363" class="comment-tools"></div><div class="clear"></div><div id="comment-25363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

