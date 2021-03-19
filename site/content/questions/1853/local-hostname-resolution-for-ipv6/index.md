+++
type = "question"
title = "local hostname resolution for ipv6"
description = '''like a previous poster, i would like to use a local host file to apply short names to ipv6 addresses in my captures. including link-scope addresses (regardless of the missing interface identifier). that is, if wireshark captures and displays a link-scope address in the IPv6 header, i want to identif...'''
date = "2011-01-21T11:19:00Z"
lastmod = "2011-01-24T04:03:00Z"
weight = 1853
keywords = [ "labels", "hosts", "ipv6" ]
aliases = [ "/questions/1853" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [local hostname resolution for ipv6](/questions/1853/local-hostname-resolution-for-ipv6)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1853-score" class="post-score" title="current number of votes">0</div><span id="post-1853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>like a previous poster, i would like to use a local host file to apply short names to ipv6 addresses in my captures. <em>including</em> link-scope addresses (regardless of the missing interface identifier). that is, if wireshark captures and displays a link-scope address in the IPv6 header, i want to identify at least which host it came from, quickly.</p><p>it's not a question about routing (where the interface identifier is critical) - it's about using wireshark to identify where (which host) the packets came from.</p><p>is this impossible, using a local host file?</p><p>steve froelich</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-labels" rel="tag" title="see questions tagged &#39;labels&#39;">labels</span> <span class="post-tag tag-link-hosts" rel="tag" title="see questions tagged &#39;hosts&#39;">hosts</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '11, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/c8fd79f90d1b83a0ca254987a20c6bf7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sffroelich&#39;s gravatar image" /><p><span>sffroelich</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sffroelich has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jan '11, 15:46</strong> </span></p></div></div><div id="comments-container-1853" class="comments-container"></div><div id="comment-tools-1853" class="comment-tools"></div><div class="clear"></div><div id="comment-1853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1903"></span>

<div id="answer-container-1903" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1903-score" class="post-score" title="current number of votes">0</div><span id="post-1903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Currently it's not possible. The name resolving function filters out Link Local and Multicast addresses for IPv6 resolving (see <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/addr_resolv.c?revision=35082&amp;view=markup">get_hostname6()</a>). That's been in since inception in <a href="http://anonsvn.wireshark.org/viewvc?view=rev&amp;revision=229">r229</a>, added over 11 years ago.</p><p>In that time it may have made sense. Now it seems like a viable improvement to drop them. Please file a bug report in <a href="https://bugs.wireshark.org">bugs.wireshark.org</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '11, 04:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1903" class="comments-container"></div><div id="comment-tools-1903" class="comment-tools"></div><div class="clear"></div><div id="comment-1903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

