+++
type = "question"
title = "Wireshark uses wrong DNS to resolve network addresses"
description = '''Hi, before I file a bug I wanted to ask here for help: I&#x27;m working with two different networks:Ethernet LAN in a 172.19.0.0 network (work) and Wireless in a 192.168.2.0 network (home).  For testing purposes, I activated preferences-&amp;gt;name resolution-&amp;gt;resolve network (IP) addresses in my home ne...'''
date = "2015-07-02T22:42:00Z"
lastmod = "2015-07-03T00:16:00Z"
weight = 43835
keywords = [ "resolution", "dns", "address" ]
aliases = [ "/questions/43835" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark uses wrong DNS to resolve network addresses](/questions/43835/wireshark-uses-wrong-dns-to-resolve-network-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43835-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>before I file a bug I wanted to ask here for help:</p><p>I'm working with two different networks:Ethernet LAN in a 172.19.0.0 network (work) and Wireless in a 192.168.2.0 network (home).</p><p>For testing purposes, I activated preferences-&gt;name resolution-&gt;resolve network (IP) addresses in my home network. Since then, if resolve network addresses is activated, wireshark uses the home dns (192.168.2.1) server and not the dns-server which win7 uses (something with 172..., checked with ipconfig /all). Option use an external network name resolver is checked. The problem is reproducable.</p><p>Is there any option in wireshark 1.12.6 (v1.12.6-0-gee1fce6 from master-1.12) to force change the dns server it uses?</p></div><div id="question-tags" class="tags-container tags">resolution dns address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '15, 22:42</strong></p><img src="https://secure.gravatar.com/avatar/2354335128d206362c0fb3f6b7d93cf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="godone&#39;s gravatar image" /><p>godone<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="godone has no accepted answers">0%</span></p></div></div><div id="comments-container-43835" class="comments-container"></div><div id="comment-tools-43835" class="comment-tools"></div><div class="clear"></div><div id="comment-43835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43838"></span>

<div id="answer-container-43838" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43838-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are no options in Wireshark to specify the name resolver to use.</p><p>Wireshark uses either the <a href="http://c-ares.haxx.se">c-ares</a> asynchronous DNS resolver, the <a href="http://www.chiark.greenend.org.uk/~ian/adns/">GNU adns</a> asynchronous DNS resolver, or the (synchronous) DNS resolver the system provides, depending on how Wireshark was compiled. The Windows releases are, I think, compiled to use c-ares; from a quick look at its code, c-ares <em>should</em> use the same DNS servers that the system's DNS resolver does, although it might not re-check for the DNS servers to use if the machine moves from one network to another.</p><p>You should file a bug on this on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>; please give the full Wireshark "about" information when you fill out the bug form (so that we know what version of which DNS resolver your version of Wireshark is using), and indicate whether this problem shows up if you shut down all instances of Wireshark and then, when connected to your work network, start up a new instance of Wireshark, or if it only shows up if you start it on the home network and then take the machine to work and run it there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '15, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-43838" class="comments-container"><span id="43877"></span><div id="comment-43877" class="comment"><div id="post-43877-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I filed this as bug 11339 <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11339">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11339</a> .</p></div><div id="comment-43877-info" class="comment-info"><span class="comment-age">(05 Jul '15, 22:15)</span> godone</div></div></div><div id="comment-tools-43838" class="comment-tools"></div><div class="clear"></div><div id="comment-43838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

