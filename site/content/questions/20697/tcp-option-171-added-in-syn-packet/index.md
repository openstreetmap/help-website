+++
type = "question"
title = "TCP Option 171 added in SYN packet"
description = '''Hello, just came across a tcp option 171 : 0xab http://www.cloudshark.org/captures/1d460ea5291d shows the option added in frame 2 at the capture point as the client&#x27;s syn packet gets forwarded to the server. Maximum segment size: 1380 bytes No-Operation (NOP)  Type: 1 Window scale: 8 (multiply by 25...'''
date = "2013-04-22T02:14:00Z"
lastmod = "2013-04-22T06:35:00Z"
weight = 20697
keywords = [ "tcp-options", "tcp", "unkown", "options" ]
aliases = [ "/questions/20697" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Option 171 added in SYN packet](/questions/20697/tcp-option-171-added-in-syn-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20697-score" class="post-score" title="current number of votes">0</div><span id="post-20697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, just came across a tcp option 171 : 0xab</p><p><a href="http://www.cloudshark.org/captures/1d460ea5291d">http://www.cloudshark.org/captures/1d460ea5291d</a> shows the option added in frame 2 at the capture point as the client's syn packet gets forwarded to the server.</p><p><code>Maximum segment size: 1380 bytes No-Operation (NOP)  Type: 1 Window scale: 8 (multiply by 256) No-Operation (NOP)  Type: 1 No-Operation (NOP) TCP SACK Permitted Option: True Unknown (0xab) (6 bytes) : ab 06 00 00 00 2f 01 01</code></p><p>The HW MAC address indicates the capture point was a <a href="http://en.wikipedia.org/wiki/Radware">Radware</a> device Anyone out there that has information about this option?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp-options" rel="tag" title="see questions tagged &#39;tcp-options&#39;">tcp-options</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-unkown" rel="tag" title="see questions tagged &#39;unkown&#39;">unkown</span> <span class="post-tag tag-link-options" rel="tag" title="see questions tagged &#39;options&#39;">options</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '13, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p><span>mrEEde2</span><br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-20697" class="comments-container"><span id="20699"></span><div id="comment-20699" class="comment"><div id="post-20699-score" class="comment-score">1</div><div class="comment-text"><p>I know that there is a Citrix Netscaler use of TCP options where they try to transport client IPs, but this doesn't seem to be it... <a href="http://blogs.citrix.com/2012/08/31/using-tcp-options-for-client-ip-insertion/">http://blogs.citrix.com/2012/08/31/using-tcp-options-for-client-ip-insertion/</a></p></div><div id="comment-20699-info" class="comment-info"><span class="comment-age">(22 Apr '13, 02:54)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="20701"></span><div id="comment-20701" class="comment"><div id="post-20701-score" class="comment-score"></div><div class="comment-text"><p>What a funny option (thanks for sharing this information).</p><p>I really like the explanation for it.</p><blockquote><p>But in <strong>secured environments</strong> generally proxies are not allowed to alter HTTP header.</p></blockquote><p>O.K. so the HTTP proxy is <strong>not allowed</strong> to add a header that has been defined in the HTTP standard, BUT the load balancer <strong>is allowed</strong> to add a TCP option, 'beyond' any standard.</p><p>What a nice justification ;-))</p></div><div id="comment-20701-info" class="comment-info"><span class="comment-age">(22 Apr '13, 06:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20697" class="comment-tools"></div><div class="clear"></div><div id="comment-20697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

