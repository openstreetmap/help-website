+++
type = "question"
title = "how to capture telnet traffic in &quot;cooked&quot; (per-line) mode?"
description = '''Hi Experts, I found these two captures: http://wiki.wireshark.org/SampleCaptures#Telnet telnet-cooked.pcap (libpcap) A telnet session in &quot;cooked&quot; (per-line) mode. telnet-raw.pcap (libpcap) A telnet session in &quot;raw&quot; (per-character) mode.  How can I capture traffic just in &quot;cooked&quot; mode?'''
date = "2013-08-14T10:48:00Z"
lastmod = "2013-08-15T09:36:00Z"
weight = 23778
keywords = [ "cooked", "per-line", "mode", "telnet" ]
aliases = [ "/questions/23778" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to capture telnet traffic in "cooked" (per-line) mode?](/questions/23778/how-to-capture-telnet-traffic-in-cooked-per-line-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23778-score" class="post-score" title="current number of votes">0</div><span id="post-23778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>I found these two captures: <a href="http://wiki.wireshark.org/SampleCaptures#Telnet">http://wiki.wireshark.org/SampleCaptures#Telnet</a></p><p>telnet-cooked.pcap (libpcap) A telnet session in "cooked" (per-line) mode. telnet-raw.pcap (libpcap) A telnet session in "raw" (per-character) mode.</p><p>How can I capture traffic just in "cooked" mode?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cooked" rel="tag" title="see questions tagged &#39;cooked&#39;">cooked</span> <span class="post-tag tag-link-per-line" rel="tag" title="see questions tagged &#39;per-line&#39;">per-line</span> <span class="post-tag tag-link-mode" rel="tag" title="see questions tagged &#39;mode&#39;">mode</span> <span class="post-tag tag-link-telnet" rel="tag" title="see questions tagged &#39;telnet&#39;">telnet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '13, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/f697d55a7a5a16d8e1582edceda33c15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jomajo&#39;s gravatar image" /><p><span>jomajo</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jomajo has one accepted answer">100%</span></p></div></div><div id="comments-container-23778" class="comments-container"></div><div id="comment-tools-23778" class="comment-tools"></div><div class="clear"></div><div id="comment-23778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23782"></span>

<div id="answer-container-23782" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23782-score" class="post-score" title="current number of votes">1</div><span id="post-23782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How can I capture traffic just in "cooked" mode?</p></blockquote><p>"Cooked" mode is called <a href="http://tools.ietf.org/html/rfc1184">linemode</a>, so you'd need to use a Telnet client that supports linemode, talking to a server that supports linemode, with the client configured, if necessary, to use linemode, and capture while those clients are communicating.</p><p><a href="http://pic.dhe.ibm.com/infocenter/zos/v1r13/index.jsp?topic=%2Fcom.ibm.zos.r13.halz002%2Ff1a1b3b0175.htm">z/OS's Telnet server apparently supports linemode and advertises it when you connect to it</a>. The OS X telnetd man page implies that it can be compiled with linemode support; it's probably a fairly standard BSD Telnet server, so that probably applies to many other UN*Xes as well, but I don't know whether that's the way it's compiled on OS X or any other UN*Xes. I don't know what other servers do.</p><p>The OS X telnet man page says</p><pre><code> Once a connection has been opened, telnet will attempt to enable the
 TELNET LINEMODE option.  If this fails, then telnet will revert to one of
 two input modes: either ``character at a time&#39;&#39; or ``old line by line&#39;&#39;
 depending on what the remote system supports.</code></pre><p>and it's probably just a fairly standard BSD Telnet client, so recent Telnet clients on other UN*Xes probably also support it. I don't know what other clients do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '13, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23782" class="comments-container"><span id="23795"></span><div id="comment-23795" class="comment"><div id="post-23795-score" class="comment-score"></div><div class="comment-text"><p>thanks Guy,</p><p>I would like to use Putty telnet client with Cisco IOS devices. I can see "double-characters" (client-to-server, and server-to-client).</p><p>That is not very nice to read :)</p></div><div id="comment-23795-info" class="comment-info"><span class="comment-age">(15 Aug '13, 05:53)</span> <span class="comment-user userinfo">jomajo</span></div></div><span id="23801"></span><div id="comment-23801" class="comment"><div id="post-23801-score" class="comment-score"></div><div class="comment-text"><p>Sounds like a job for, err, umm, Wireshark. Perhaps Putty and IOS are negotiating linemode on, and Putty's doing local echo, but they're not negotiating echo off, so that IOS is doing remote echo.</p></div><div id="comment-23801-info" class="comment-info"><span class="comment-age">(15 Aug '13, 09:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-23782" class="comment-tools"></div><div class="clear"></div><div id="comment-23782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

