+++
type = "question"
title = "Desktop client tracking"
description = '''I created a desktop client connects to Postgresql database and I want to be sure that this application uses SSL (I don&#x27;t want to expose users authentications over the network). How can I be sure that my desktop client connections over SSL or not? I couldn&#x27;t find a way to make Wireshark track my appl...'''
date = "2013-07-21T02:28:00Z"
lastmod = "2013-07-21T10:21:00Z"
weight = 23204
keywords = [ "ssl", "desktop" ]
aliases = [ "/questions/23204" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Desktop client tracking](/questions/23204/desktop-client-tracking)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23204-score" class="post-score" title="current number of votes">0</div><span id="post-23204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I created a desktop client connects to Postgresql database and I want to be sure that this application uses SSL (I don't want to expose users authentications over the network).</p><p>How can I be sure that my desktop client connections over SSL or not?</p><p>I couldn't find a way to make Wireshark track my application's process so tried to use a simple filter because I know the destination ip and the port but this didn't help me very much!</p><pre><code>ip.dst == 192.168.0.74 &amp;&amp; tcp.port==5433</code></pre><p>P.S. Sorry for silly question because I'm still a newbie and I couldn't find an answer to my question after searching here.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-desktop" rel="tag" title="see questions tagged &#39;desktop&#39;">desktop</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '13, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/c662972b7f745e8b1fe576b9279edbdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbnoimi&#39;s gravatar image" /><p><span>mbnoimi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbnoimi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jul '13, 05:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23204" class="comments-container"></div><div id="comment-tools-23204" class="comment-tools"></div><div class="clear"></div><div id="comment-23204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23205"></span>

<div id="answer-container-23205" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23205-score" class="post-score" title="current number of votes">0</div><span id="post-23205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can't track traffic on a per process basis but can do so by IP address and port.</p><p>What do you see with your filter?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '13, 05:29</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23205" class="comments-container"><span id="23208"></span><div id="comment-23208" class="comment"><div id="post-23208-score" class="comment-score"></div><div class="comment-text"><blockquote><p>What do you see with your filter?</p></blockquote><p>How can I tell you what I saw, In case you want Wireshark's log you can download <a href="https://files.one.ubuntu.com/WvMDe5KHRN-yPEyhx9RENA">this link</a> (K12 text file)</p></div><div id="comment-23208-info" class="comment-info"><span class="comment-age">(21 Jul '13, 07:26)</span> <span class="comment-user userinfo">mbnoimi</span></div></div><span id="23209"></span><div id="comment-23209" class="comment"><div id="post-23209-score" class="comment-score"></div><div class="comment-text"><p>It would be more helpful to just post the Wireshark capture (pcap) somewhere easily accessible, such as <a href="http://cloudshark.org">Cloudshark</a>. Make sure the capture doesn't contain any sensitive info before posting it.</p></div><div id="comment-23209-info" class="comment-info"><span class="comment-age">(21 Jul '13, 10:21)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-23205" class="comment-tools"></div><div class="clear"></div><div id="comment-23205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

