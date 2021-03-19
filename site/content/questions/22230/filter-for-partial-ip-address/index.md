+++
type = "question"
title = "filter for partial IP address"
description = '''I would like to create a display filter for an with the last 2 octets of an IP address. In this case I want to filter for the IP address xxx.xxx.149.195 . What is the display filter expression using the offset and slice operators or a wildcard expression that I would need to use?'''
date = "2013-06-21T14:06:00Z"
lastmod = "2015-01-02T13:11:00Z"
weight = 22230
keywords = [ "display-filter", "wildcard", "offset" ]
aliases = [ "/questions/22230" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [filter for partial IP address](/questions/22230/filter-for-partial-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22230-score" class="post-score" title="current number of votes">1</div><span id="post-22230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to create a display filter for an with the last 2 octets of an IP address. In this case I want to filter for the IP address xxx.xxx.149.195 . What is the display filter expression using the offset and slice operators or a wildcard expression that I would need to use?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span> <span class="post-tag tag-link-wildcard" rel="tag" title="see questions tagged &#39;wildcard&#39;">wildcard</span> <span class="post-tag tag-link-offset" rel="tag" title="see questions tagged &#39;offset&#39;">offset</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '13, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/07df7b283ffac0db1a014e08155b0b65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrproject&#39;s gravatar image" /><p><span>mrproject</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrproject has no accepted answers">0%</span></p></div></div><div id="comments-container-22230" class="comments-container"></div><div id="comment-tools-22230" class="comment-tools"></div><div class="clear"></div><div id="comment-22230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="22237"></span>

<div id="answer-container-22237" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22237-score" class="post-score" title="current number of votes">5</div><span id="post-22237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrproject has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you are looking for a Wireshark display filter that matches either the source or the destination address, then you can use:</p><pre><code>ip.host matches &quot;\.149\.195$&quot;</code></pre><p>If you only want the source address:</p><pre><code>ip.src_host matches &quot;\.149\.195$&quot;</code></pre><p>And if you only want the destination address:</p><pre><code>ip.dst_host matches &quot;\.149\.195$&quot;</code></pre><p>For more information on wireshark filters, refer to the <a href="http://www.wireshark.org/docs/man-pages/wireshark-filter.html">wireshark-filter</a> man page. Further links are provided there for more information on the <em>"matches"</em> operator, although one of them appears to be broken, so you can use this one instead: <a href="https://developer.gnome.org/glib/2.34/glib-regex-syntax.html">https://developer.gnome.org/glib/2.34/glib-regex-syntax.html</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '13, 19:58</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-22237" class="comments-container"></div><div id="comment-tools-22237" class="comment-tools"></div><div class="clear"></div><div id="comment-22237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22232"></span>

<div id="answer-container-22232" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22232-score" class="post-score" title="current number of votes">0</div><span id="post-22232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try this one:</p><p>ip[14:2] eq 95c3 or ip[18:2] eq 95c3</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '13, 14:35</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p><span>mrEEde2</span><br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-22232" class="comments-container"></div><div id="comment-tools-22232" class="comment-tools"></div><div class="clear"></div><div id="comment-22232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38854"></span>

<div id="answer-container-38854" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38854-score" class="post-score" title="current number of votes">0</div><span id="post-38854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>But the negative form of this does not work.</p><p>For example, if I want to filter out all traffic from 149.195.<em>.</em>/16, none of the below work. Did mrproject not post his ip address correctly? Was he trying to filter out 149.195.<em>.</em> or <em>.</em>.149.195?</p><p>ip.host !matches ".149.195$"</p><p>!ip.host matches ".149.195$"</p><p>ip.host !== ".149.195$"</p><p>I thought I had found the answer here: <a href="http://wiki.wireshark.org/DisplayFilters">http://wiki.wireshark.org/DisplayFilters</a></p><p>!ip.host==192.168.0.0/16</p><p>but the above doesn't work, neither does ip.host != 192.168.0.0/16</p><p>Final edit:</p><p>I got it working with !ip.addr == 192.168.0.0/24. I didn't realize that ip.host is deprecated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '15, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/f70161294b019c9a68e8f494bb2bbe63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Justin%20Goldberg&#39;s gravatar image" /><p><span>Justin Goldberg</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Justin Goldberg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jan '15, 10:27</strong> </span></p></div></div><div id="comments-container-38854" class="comments-container"><span id="38855"></span><div id="comment-38855" class="comment"><div id="post-38855-score" class="comment-score">1</div><div class="comment-text"><p>he was specifically filtering on the last two octets, so CIDR filters will not help. You need to use regex expressions.</p></div><div id="comment-38855-info" class="comment-info"><span class="comment-age">(02 Jan '15, 13:11)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-38854" class="comment-tools"></div><div class="clear"></div><div id="comment-38854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

