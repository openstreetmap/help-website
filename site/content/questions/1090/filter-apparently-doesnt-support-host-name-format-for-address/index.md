+++
type = "question"
title = "Filter Apparently Doesn&#x27;t Support Host Name format for Address"
description = '''The documentation states that this filter will work: ip.dst eq www.mit.edu But when I try to use it, Wireshark gives me an error &#x27; &quot;www.mit.edu&quot; is not a valid hostname or IPv4 address&#x27; I cut-and-pasted the sample into the filter, so I expected it to work!'''
date = "2010-11-23T16:26:00Z"
lastmod = "2014-12-08T20:22:00Z"
weight = 1090
keywords = [ "hostname", "filters" ]
aliases = [ "/questions/1090" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filter Apparently Doesn't Support Host Name format for Address](/questions/1090/filter-apparently-doesnt-support-host-name-format-for-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1090-score" class="post-score" title="current number of votes">1</div><span id="post-1090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The documentation states that this filter will work: ip.dst eq www.mit.edu</p><p>But when I try to use it, Wireshark gives me an error ' "www.mit.edu" is not a valid hostname or IPv4 address'</p><p>I cut-and-pasted the sample into the filter, so I expected it to work!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hostname" rel="tag" title="see questions tagged &#39;hostname&#39;">hostname</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '10, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/3b8a4f21d2910124c8a2e4a70a46c186?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ActualRandy&#39;s gravatar image" /><p><span>ActualRandy</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ActualRandy has no accepted answers">0%</span></p></div></div><div id="comments-container-1090" class="comments-container"></div><div id="comment-tools-1090" class="comment-tools"></div><div class="clear"></div><div id="comment-1090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1096"></span>

<div id="answer-container-1096" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1096-score" class="post-score" title="current number of votes">1</div><span id="post-1096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try using <code>ip.dst_host eq www.mit.edu</code>. That should resolve the syntax error issue. If you still don't see any traffic try turning on network name resolutions to see what www.mit.edu traffic is really resolving to (for example, www.wireshark.org actually resolves to media-2.cacetech.com.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '10, 17:11</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-1096" class="comments-container"><span id="1097"></span><div id="comment-1097" class="comment"><div id="post-1097-score" class="comment-score"></div><div class="comment-text"><p>Thanks lchappell - that did the trick :-)</p><p>However, being a stickler of sorts, I hope Gerald will re-write the documentation, since the example looks wrong.</p></div><div id="comment-1097-info" class="comment-info"><span class="comment-age">(23 Nov '10, 17:25)</span> <span class="comment-user userinfo">ActualRandy</span></div></div><span id="1103"></span><div id="comment-1103" class="comment"><div id="post-1103-score" class="comment-score"></div><div class="comment-text"><p>Or you could add to the wiki page or the manuals or... &lt;grin&gt;</p></div><div id="comment-1103-info" class="comment-info"><span class="comment-age">(23 Nov '10, 19:09)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div><span id="38452"></span><div id="comment-38452" class="comment"><div id="post-38452-score" class="comment-score"></div><div class="comment-text"><p>note: you have to enable Name Resolution on the preferences for this to work (disabled by default).</p></div><div id="comment-38452-info" class="comment-info"><span class="comment-age">(08 Dec '14, 14:35)</span> <span class="comment-user userinfo">Ciro Santilli</span></div></div><span id="38459"></span><div id="comment-38459" class="comment"><div id="post-38459-score" class="comment-score"></div><div class="comment-text"><blockquote><p>However, being a stickler of sorts, I hope Gerald will re-write the documentation, since the example looks wrong.</p></blockquote><p>I don't know what Gerald will do, but Guy will ask you to file a bug on this, because that's really badly broken; if our display-filter parser can't figure out that you can compare an IP address with a domain name, that's just horribly bad - it violates the Principle of Least Surprise.</p></div><div id="comment-38459-info" class="comment-info"><span class="comment-age">(08 Dec '14, 20:22)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-1096" class="comment-tools"></div><div class="clear"></div><div id="comment-1096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1091"></span>

<div id="answer-container-1091" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1091-score" class="post-score" title="current number of votes">0</div><span id="post-1091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Using hostnames in filters only work when they can be resolved. Do you have DNS configured on the system that you are running Wireshark on? And is the system able to resolve www.mit.edu?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '10, 16:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1091" class="comments-container"><span id="1092"></span><div id="comment-1092" class="comment"><div id="post-1092-score" class="comment-score"></div><div class="comment-text"><p>Hey Synbit - thanks for the response.</p><p>I can resolve www.mit.edu - I ran nslookup on it and received the ip 192.168.1.1</p><p>Regarding whether the system has DNS configured, I can't say; it is a public wireless access point</p><p>I ran it while in a live session, as opposed to a stored one, and it gave me a slightly different message: <strong>The following display filter isn't a valid display filter: ip.dst eq www.mit.edu</strong></p><p>In this message, it is clearly saying that it thinks I have an invalid filter.</p></div><div id="comment-1092-info" class="comment-info"><span class="comment-age">(23 Nov '10, 16:47)</span> <span class="comment-user userinfo">ActualRandy</span></div></div></div><div id="comment-tools-1091" class="comment-tools"></div><div class="clear"></div><div id="comment-1091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

