+++
type = "question"
title = "Remote capturing"
description = '''Hi, I am trying to use remote capturing between two machines running win7 32b. When I try to add a remote interface in Wireshark, I see the error &quot;can&#x27;t get the list of interfaces: getaddrinfo() the requested name is valid but no data of the requested type was found&quot; How can I solve the problem?'''
date = "2012-10-02T05:56:00Z"
lastmod = "2012-10-08T12:31:00Z"
weight = 14636
keywords = [ "getaddrinfo", "rpcap", "remote" ]
aliases = [ "/questions/14636" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Remote capturing](/questions/14636/remote-capturing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14636-score" class="post-score" title="current number of votes">0</div><span id="post-14636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to use remote capturing between two machines running win7 32b. When I try to add a remote interface in Wireshark, I see the error "can't get the list of interfaces: getaddrinfo() the requested name is valid but no data of the requested type was found" How can I solve the problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-getaddrinfo" rel="tag" title="see questions tagged &#39;getaddrinfo&#39;">getaddrinfo</span> <span class="post-tag tag-link-rpcap" rel="tag" title="see questions tagged &#39;rpcap&#39;">rpcap</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '12, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/f52b4177248702275af6f6bc3940b682?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mah&#39;s gravatar image" /><p><span>mah</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mah has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Oct '12, 07:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-14636" class="comments-container"></div><div id="comment-tools-14636" class="comment-tools"></div><div class="clear"></div><div id="comment-14636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14637"></span>

<div id="answer-container-14637" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14637-score" class="post-score" title="current number of votes">0</div><span id="post-14637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To be able to do a remote capture this way you need to run rpdapd.exe on the other machine, which means that you need to install WinPCAP (which contains rpcapd.exe). This is necessary because Wireshark needs a capture process to connect to, and that process is rpcapd.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '12, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14637" class="comments-container"><span id="14638"></span><div id="comment-14638" class="comment"><div id="post-14638-score" class="comment-score"></div><div class="comment-text"><p>I have installed WinPCAp and run rpcapd.exe on the remote machine.I also have enabled port 2002 in windows firewall.</p></div><div id="comment-14638-info" class="comment-info"><span class="comment-age">(02 Oct '12, 06:30)</span> <span class="comment-user userinfo">mah</span></div></div><span id="14639"></span><div id="comment-14639" class="comment"><div id="post-14639-score" class="comment-score"></div><div class="comment-text"><p>and you still get the same error?</p></div><div id="comment-14639-info" class="comment-info"><span class="comment-age">(02 Oct '12, 08:49)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-14637" class="comment-tools"></div><div class="clear"></div><div id="comment-14637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14789"></span>

<div id="answer-container-14789" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14789-score" class="post-score" title="current number of votes">0</div><span id="post-14789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>getaddrinfo() the requested name is valid but no data of the requested type was found</p></blockquote><p>That's a windows API error, indicating that the name resolver on your Wireshark system was not able to resolve the specified name to a valid IP address (no A record or possibly the IPv6 AAA record returned first).</p><blockquote><p><code>http://msdn.microsoft.com/en-us/library/windows/desktop/ms740668%28v=vs.85%29.aspx#WSANO_DATA</code><br />
<code>http://msdn.microsoft.com/en-us/library/windows/desktop/ms738520%28v=vs.85%29.aspx</code><br />
</p></blockquote><p>I suggest to test name resolving on the CLI. Open a DOS box and run these commands.</p><blockquote><p><code>c:&gt;nslookup hostname</code><br />
<code>c:&gt;ping hostname</code><br />
</p></blockquote><p>Where <strong>hostname</strong> is the same string you entered in the Wireshark GUI.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '12, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14789" class="comments-container"></div><div id="comment-tools-14789" class="comment-tools"></div><div class="clear"></div><div id="comment-14789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

