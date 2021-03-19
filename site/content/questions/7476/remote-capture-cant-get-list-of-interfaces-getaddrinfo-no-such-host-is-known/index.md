+++
type = "question"
title = "Remote capture - Can&#x27;t get list of interfaces: getaddrinfo() No such host is known."
description = '''Trying to use Wireshark Version 1.4.0rc2 (SVN Rev 33665 from /trunk-1.4) on Win XP to capture from my linux box running Wireshark Version 1.4.9 on Fedora 15 (2.6.38.6-26.rc1.fc15i386 with libcap version 1.1.1) On Capture Options, I specify &quot;Remote&quot; interface, Host &quot;rpcapd://10.2.41.11&quot; Username &quot;pat...'''
date = "2011-11-16T13:53:00Z"
lastmod = "2011-11-17T22:20:00Z"
weight = 7476
keywords = [ "remote" ]
aliases = [ "/questions/7476" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Remote capture - Can't get list of interfaces: getaddrinfo() No such host is known.](/questions/7476/remote-capture-cant-get-list-of-interfaces-getaddrinfo-no-such-host-is-known)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7476-score" class="post-score" title="current number of votes">0</div><span id="post-7476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to use Wireshark Version 1.4.0rc2 (SVN Rev 33665 from /trunk-1.4) on Win XP to capture from my linux box running Wireshark Version 1.4.9 on Fedora 15 (2.6.38.6-26.rc1.fc15i386 with libcap version 1.1.1) On Capture Options, I specify "Remote" interface, Host "rpcapd://10.2.41.11" Username "pat" and Password.</p><p>I get a error message:</p><p>"Can't get list of interfaces: getaddrinfo() No such host is known."</p><p>I have also tried: Host "rpcapd://10.2.41.11/eth0"</p><p>I am running WinPcap 4.1.2 on the Windows box.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '11, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/aea8566403ec31a5a74d0b5e2c92a9f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gooberpat&#39;s gravatar image" /><p><span>gooberpat</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gooberpat has no accepted answers">0%</span></p></div></div><div id="comments-container-7476" class="comments-container"></div><div id="comment-tools-7476" class="comment-tools"></div><div class="clear"></div><div id="comment-7476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7493"></span>

<div id="answer-container-7493" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7493-score" class="post-score" title="current number of votes">0</div><span id="post-7493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to run rpcapd on the capture target.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '11, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7493" class="comments-container"></div><div id="comment-tools-7493" class="comment-tools"></div><div class="clear"></div><div id="comment-7493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7498"></span>

<div id="answer-container-7498" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7498-score" class="post-score" title="current number of votes">0</div><span id="post-7498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>WinPcap appears to assume that it will always be handed a host name, not an dotted-quad string, for remote packet capture; it uses <code>getaddrinfo()</code> on the string for the remote packet host, and, at least as I read the Mac OS X <code>getaddrinfo()</code> man page, it expects to be handed a host name. <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/ms738520(v=vs.85).aspx">Microsoft's man page equivalent</a> says "The getaddrinfo function provides protocol-independent translation from an ANSI host name to an address.", which appears also ti indicate that it expects to be handed a host name rather than a dotted-quad string.</p><p>If the host at 10.2.41.11 has a host name, try using it instead of the dotted-quad. If it doesn't have a host name, and you can give it one (that can be resolved with a local host file, or that you can enter into the appropriate DNS or other name resolution server, e.g. NBNS/WINS), do so and then try using it instead of the dotted quad.</p><p>And then <a href="http://www.winpcap.org/bugs.htm">file a bug against WinPcap</a> for this; it's a bug that you can't use a dotted-quad or colonized-octet :-) address there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '11, 22:20</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7498" class="comments-container"></div><div id="comment-tools-7498" class="comment-tools"></div><div class="clear"></div><div id="comment-7498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

