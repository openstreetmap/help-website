+++
type = "question"
title = "IPV4/IPv6 address"
description = '''I would like to know if an IPv4 adress have also configurated an IPv6 adress.. Can anyone explain me how can I do it? Thanks in advance.'''
date = "2014-05-25T03:07:00Z"
lastmod = "2014-05-25T03:52:00Z"
weight = 33046
keywords = [ "ipv4" ]
aliases = [ "/questions/33046" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [IPV4/IPv6 address](/questions/33046/ipv4ipv6-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33046-score" class="post-score" title="current number of votes">0</div><span id="post-33046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know if an IPv4 adress have also configurated an IPv6 adress.. Can anyone explain me how can I do it? Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipv4" rel="tag" title="see questions tagged &#39;ipv4&#39;">ipv4</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '14, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/e7791a76dfd358e21aa3ce09047c0c03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="meri&#39;s gravatar image" /><p><span>meri</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="meri has no accepted answers">0%</span></p></div></div><div id="comments-container-33046" class="comments-container"></div><div id="comment-tools-33046" class="comment-tools"></div><div class="clear"></div><div id="comment-33046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33047"></span>

<div id="answer-container-33047" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33047-score" class="post-score" title="current number of votes">1</div><span id="post-33047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>IPv4 and IPv6 addresses are two completely different things, so I'm not sure what you're trying to do. You can assign an IPv4 address to a network card, and one or many IPv6 addresses as well, if the network card is enabled for IPv6. So these addresses are assigned to network cards, not IPv6 to IPv4.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '14, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33047" class="comments-container"><span id="33051"></span><div id="comment-33051" class="comment"><div id="post-33051-score" class="comment-score"></div><div class="comment-text"><p>For example if I know that in my capture there are 4 IPV6 addresses (I know thanks of Statistics-Conversations) I would like to know if this addresses have also an IPv4 address of the same machine configurated. Sorry for my "stupid" questions, I hope you understand me. I'm new in wireshark.</p></div><div id="comment-33051-info" class="comment-info"><span class="comment-age">(25 May '14, 03:41)</span> <span class="comment-user userinfo">meri</span></div></div><span id="33052"></span><div id="comment-33052" class="comment"><div id="post-33052-score" class="comment-score">1</div><div class="comment-text"><p>A host (or more specifically a network adaptor) can have multiple IP addresses of both IPv4 and IPv6 flavours.</p><p>So if your capture happens to cover the same host running both IPv4 &amp; IPv6 conversations, then yes they will both show up.</p></div><div id="comment-33052-info" class="comment-info"><span class="comment-age">(25 May '14, 03:49)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="33053"></span><div id="comment-33053" class="comment"><div id="post-33053-score" class="comment-score">2</div><div class="comment-text"><p>if you want to match IPv4 and IPv6 addresses to the same host you may have a chance by identifying them through their Ethernet MAC address. Same MAC may mean same PC, but keep in mind that MAC addresses are only valid in the local network segment. As soon as a packet crosses a router you can't tell anymore, because all packets will have the router MAC.</p><p>And no worries about being new to Wireshark, just ask and if something is unclear we'll ask back until the question is clear ;-)</p></div><div id="comment-33053-info" class="comment-info"><span class="comment-age">(25 May '14, 03:52)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-33047" class="comment-tools"></div><div class="clear"></div><div id="comment-33047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

