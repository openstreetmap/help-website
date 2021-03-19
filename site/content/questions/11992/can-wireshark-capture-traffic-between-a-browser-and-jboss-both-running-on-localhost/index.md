+++
type = "question"
title = "Can wireshark capture traffic between a browser and jboss (both running on localhost)?"
description = '''I&#x27;m trying to capture traffic between a web browser running on my windows 7 machine and a jboss server also running on my machine but wireshark doesn&#x27;t seem to capture it.  For what it&#x27;s worth, I&#x27;ve successfully captured the traffic if the web browser is on another machine. Is this even possible? If...'''
date = "2012-06-16T06:25:00Z"
lastmod = "2012-06-16T07:37:00Z"
weight = 11992
keywords = [ "jboss", "windows7", "localhost" ]
aliases = [ "/questions/11992" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can wireshark capture traffic between a browser and jboss (both running on localhost)?](/questions/11992/can-wireshark-capture-traffic-between-a-browser-and-jboss-both-running-on-localhost)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11992-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11992-score" class="post-score" title="current number of votes">0</div><span id="post-11992-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to capture traffic between a web browser running on my windows 7 machine and a jboss server also running on my machine but wireshark doesn't seem to capture it.</p><p>For what it's worth, I've successfully captured the traffic if the web browser is on another machine.</p><p>Is this even possible? If so, what am I missing?</p><p>Thanks in advance, Tom</p><p>PS. Wireshark is also running on my machine.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-jboss" rel="tag" title="see questions tagged &#39;jboss&#39;">jboss</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-localhost" rel="tag" title="see questions tagged &#39;localhost&#39;">localhost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '12, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/4c114f005f0568521ee358fffb2eb009?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tmuldo&#39;s gravatar image" /><p><span>tmuldo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tmuldo has no accepted answers">0%</span></p></div></div><div id="comments-container-11992" class="comments-container"></div><div id="comment-tools-11992" class="comment-tools"></div><div class="clear"></div><div id="comment-11992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11996"></span>

<div id="answer-container-11996" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11996-score" class="post-score" title="current number of votes">2</div><span id="post-11996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Kurt Mentioned, Wireshark is not the tool to use for sniffing loopback traffic on the Windows platform. As mentioned on the Wireshark wiki's <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">Loopback</a> page that Kurt also provided, you might want to try <a href="http://www.netresec.com/?page=RawCap">RawCap</a>. For me, it's been the best solution I've found so far for sniffing Windows loopback traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '12, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-11996" class="comments-container"></div><div id="comment-tools-11996" class="comment-tools"></div><div class="clear"></div><div id="comment-11996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11993"></span>

<div id="answer-container-11993" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11993-score" class="post-score" title="current number of votes">1</div><span id="post-11993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately you cannot sniff the loopback interface on Windows with Wireshark (WinPCAP).</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Loopback</code><br />
</p></blockquote><p><strong>UPDATE:</strong> Check the reference for <a href="http://www.netresec.com/?page=RawCap">RawCap</a> in that link (see answer of <span><span>@cmaynard</span></span> blow).</p><p>My preferred tool for web debugging is a proxy called Fiddler.</p><blockquote><p><code>http://www.fiddler2.com/fiddler2/</code><br />
</p></blockquote><p>Fiddler is a good companion to wireshark if you can't sniff the traffic and you need to see the whole communication (URLs, error messages, etc.).</p><p>There are also "web debugging" plugins for Firefox (and IE), like Firebug, HttpWatch and others:</p><blockquote><p><code>https://addons.mozilla.org/de/firefox/addon/firebug/</code><br />
<code>http://www.httpwatch.com/</code><br />
</p></blockquote><p>And finally, there is <strong>Nirsoft SocketSniff</strong>, which will show communication on localhost</p><blockquote><p><code>http://www.nirsoft.net/utils/socket_sniffer.html</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '12, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jun '12, 08:22</strong> </span></p></div></div><div id="comments-container-11993" class="comments-container"></div><div id="comment-tools-11993" class="comment-tools"></div><div class="clear"></div><div id="comment-11993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

