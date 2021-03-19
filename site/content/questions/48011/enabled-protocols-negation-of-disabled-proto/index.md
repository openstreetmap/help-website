+++
type = "question"
title = "Enabled protocols (negation of disabled proto)"
description = '''I&#x27;m using tshark and I&#x27;m interested in only dissecting eth and tcp for performance issues. How can I easily disable all protocols except eth and tcp? Do I have to list all protocols, and disable them except eth/tcp, or there&#x27;s an easy &quot;dissect only these protocols&quot; option? I&#x27;ve thought about reducin...'''
date = "2015-11-26T09:31:00Z"
lastmod = "2015-11-27T01:41:00Z"
weight = 48011
keywords = [ "capture", "disable", "protocol", "tshark" ]
aliases = [ "/questions/48011" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Enabled protocols (negation of disabled proto)](/questions/48011/enabled-protocols-negation-of-disabled-proto)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48011-score" class="post-score" title="current number of votes">0</div><span id="post-48011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using tshark and I'm interested in only dissecting eth and tcp for performance issues.</p><p>How can I easily disable all protocols except eth and tcp? Do I have to list all protocols, and disable them except eth/tcp, or there's an easy "dissect only these protocols" option?</p><p>I've thought about reducing snaplen, but you never know length of IP/TCP options...</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-disable" rel="tag" title="see questions tagged &#39;disable&#39;">disable</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '15, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p><span>TomLaBaude</span><br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-48011" class="comments-container"></div><div id="comment-tools-48011" class="comment-tools"></div><div class="clear"></div><div id="comment-48011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48012"></span>

<div id="answer-container-48012" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48012-score" class="post-score" title="current number of votes">1</div><span id="post-48012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TomLaBaude has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How can I easily disable all protocols except eth and tcp?</p></blockquote><p>If you do <em>exactly</em> that, you will not see any TCP traffic, because TCP runs atop IPv4 and IPv6, and if you disable <em>all</em> protocols except Ethernet and TCP, you will disable IPv4 and IPv6, so they won't ever dissect anything and thus won't hand anything to the TCP dissector.</p><p>So what you need to do is to disable everything except Ethernet, IPv4, IPv6, and TCP.</p><blockquote><p>Do I have to list all protocols, and disable them except eth/tcp</p></blockquote><p>You can't conveniently do that in TShark - it's a <em>big</em> list - but you can, at least with newer versions of Wireshark, somewhat conveniently disable them in Wireshark and then use TShark, which will use the same list of enabled and disabled protocols.</p><p>What you'd do would be to open the "Disabled Protocols" dialog, click "Disable All", and then enable Ethernet, IPv4, IPv6, and TCP.</p><p>With current versions of Wireshark, you will also have to enable a protocol named "Ethertype"; that's not a real protocol, and it shouldn't be possible to disable it, but, currently, it is possible. I've fixed that so that you don't have to enable it, but that won't show up until there's a 2.0.1 release.</p><p>That's a persistent change, so if you <em>do</em> want to dissect other protocols in the future, you'll have to re-enable all protocols.</p><blockquote><p>or there's an easy "dissect only these protocols" option?</p></blockquote><p>No, there isn't. In order to be able to do it non-persistently with a TShark command-line option, a "disable all protocols other than these" option would have to be added to TShark; if you want that, file a request on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '15, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-48012" class="comments-container"><span id="48017"></span><div id="comment-48017" class="comment"><div id="post-48017-score" class="comment-score"></div><div class="comment-text"><p>Thanks for answer Guy (and thanks to remind me that there's life between layer 2 and layer 4!)</p><p>So my plan is to create a profile in wireshark and generate a disabled_protos file from the GUI, and then use this personal profile in tshark</p></div><div id="comment-48017-info" class="comment-info"><span class="comment-age">(27 Nov '15, 01:41)</span> <span class="comment-user userinfo">TomLaBaude</span></div></div></div><div id="comment-tools-48012" class="comment-tools"></div><div class="clear"></div><div id="comment-48012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

