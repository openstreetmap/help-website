+++
type = "question"
title = "Verify an option sent by DHCP / option 78"
description = '''Hi guys, Some AP needs the option 78 of DHCP to discover the Controller. How I can check it out if DHCP is sending this? There is no option 78 at &quot;Parameter request List Item&quot; Regards, Ronaldo.'''
date = "2012-09-12T06:13:00Z"
lastmod = "2012-09-12T09:53:00Z"
weight = 14207
keywords = [ "dhcp" ]
aliases = [ "/questions/14207" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Verify an option sent by DHCP / option 78](/questions/14207/verify-an-option-sent-by-dhcp-option-78)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14207-score" class="post-score" title="current number of votes">0</div><span id="post-14207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>Some AP needs the option 78 of DHCP to discover the Controller. How I can check it out if DHCP is sending this? There is no option 78 at "Parameter request List Item"</p><p>Regards, Ronaldo.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '12, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/57c653d0e812539d95a762fc6a7570d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ronaldo&#39;s gravatar image" /><p><span>Ronaldo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ronaldo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Sep '12, 04:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-14207" class="comments-container"></div><div id="comment-tools-14207" class="comment-tools"></div><div class="clear"></div><div id="comment-14207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14211"></span>

<div id="answer-container-14211" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14211-score" class="post-score" title="current number of votes">0</div><span id="post-14211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ronaldo, Wireshark will show you the various options inside the DHCP DISCOVER/OFFER packets. Are you saying that you don't see it in Wireshark? I read it more as "you want to <em>make sure</em> it's being sent. Capture the packets, type "bootp.dhcp" in the display filter bar. Then you'll be able to see all the DHCP related packets. In the "middle pane" (the packet details pane) you can expand the "Bootstrap Protocol" header and see the various options there. DHCP is a superset of bootp protocol so don't let the name throw you off.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '12, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-14211" class="comments-container"></div><div id="comment-tools-14211" class="comment-tools"></div><div class="clear"></div><div id="comment-14211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

