+++
type = "question"
title = "How do you capture port"
description = '''I want to capture activities between 192.168.1.10 port 9600(2008 server) and 192.168.1.35 port 9030(Canon copier print server). In Wireshark 1.10.2, under the caption options, then capture filter, what should I type in there? Thanks, Paul '''
date = "2013-10-14T11:28:00Z"
lastmod = "2013-10-14T11:57:00Z"
weight = 25975
keywords = [ "what" ]
aliases = [ "/questions/25975" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do you capture port](/questions/25975/how-do-you-capture-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25975-score" class="post-score" title="current number of votes">0</div><span id="post-25975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to capture activities between 192.168.1.10 port 9600(2008 server) and 192.168.1.35 port 9030(Canon copier print server).</p><p>In Wireshark 1.10.2, under the caption options, then capture filter, what should I type in there?</p><p>Thanks,</p><p>Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-what" rel="tag" title="see questions tagged &#39;what&#39;">what</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '13, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/bc832a8c8f57cd939a20f982e55f94b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CSA&#39;s gravatar image" /><p><span>CSA</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CSA has no accepted answers">0%</span></p></div></div><div id="comments-container-25975" class="comments-container"></div><div id="comment-tools-25975" class="comment-tools"></div><div class="clear"></div><div id="comment-25975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25976"></span>

<div id="answer-container-25976" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25976-score" class="post-score" title="current number of votes">1</div><span id="post-25976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to exactly filter on that 4-tuple, the filter would be:</p><pre><code>((src host 192.168.1.10 and src port 9600 and dst host 192.168.1.35 and dst port 9030) or (dst host 192.168.1.10 and dst port 9600 and src host 192.168.1.35 and src port 9030))</code></pre><p>However, the following filter would generally fit your need as well:</p><pre><code>host 192.168.1.10 and host 192.168.1.35 and port 9600 and port 9030</code></pre><p>As the source port might change between sessions, you might want to drop the "port 9600" part.</p><p>Then beware of vlan tagging, if you are capturing on a link where vlan tagging is being used, make the filter:</p><pre><code>vlan and host 192.168.1.10 and host 192.168.1.35 and port 9600 and port 9030</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '13, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25976" class="comments-container"></div><div id="comment-tools-25976" class="comment-tools"></div><div class="clear"></div><div id="comment-25976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

