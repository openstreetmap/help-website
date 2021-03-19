+++
type = "question"
title = "[Malformed Packet: RADIUS]"
description = '''After settting up a trace i found this error : User Datagram Protocol, Src Port: 23361 (23361), Dst Port: radius-acct (1813) [Malformed Packet: RADIUS]  [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]  [Message: Malformed Packet (Exception occurred)]  [Severity level: Error]  ...'''
date = "2011-08-05T07:09:00Z"
lastmod = "2011-08-05T17:38:00Z"
weight = 5526
keywords = [ "malformedpacket" ]
aliases = [ "/questions/5526" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[Malformed Packet: RADIUS\]](/questions/5526/malformed-packet-radius)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5526-score" class="post-score" title="current number of votes">0</div><span id="post-5526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After settting up a trace i found this error :</p><pre><code>User Datagram Protocol, Src Port: 23361 (23361), Dst Port: radius-acct (1813)
[Malformed Packet: RADIUS]
    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
        [Message: Malformed Packet (Exception occurred)]
        [Severity level: Error]
        [Group: Malformed]</code></pre><p>what could be the cause?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-malformedpacket" rel="tag" title="see questions tagged &#39;malformedpacket&#39;">malformedpacket</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '11, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/9d5e8a5160246eab905af25869c7e84b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jay&#39;s gravatar image" /><p><span>jay</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jay has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Aug '11, 07:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-5526" class="comments-container"></div><div id="comment-tools-5526" class="comment-tools"></div><div class="clear"></div><div id="comment-5526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5527"></span>

<div id="answer-container-5527" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5527-score" class="post-score" title="current number of votes">1</div><span id="post-5527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This either was not a radius accounting packet, but wireshark thought it was because it was sent on the radius accounting port (1813) or it was indeed a radius accounting packet, but wireshark was not able to dissect it correctly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '11, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5527" class="comments-container"><span id="5539"></span><div id="comment-5539" class="comment"><div id="post-5539-score" class="comment-score"></div><div class="comment-text"><p>We'd need to see the trace - or, at least, the offending packet from the trace - to know for sure, but my suspicion is that it wasn't a RADIUS packet but was dissected as such because it was sent to port 1813. (TCP and UDP ports, unlike, for example, Ethernet packet types, are not certain indicators of packet types.)</p></div><div id="comment-5539-info" class="comment-info"><span class="comment-age">(05 Aug '11, 17:38)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-5527" class="comment-tools"></div><div class="clear"></div><div id="comment-5527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

