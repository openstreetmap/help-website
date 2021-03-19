+++
type = "question"
title = "Working of Dumpcap"
description = '''How does Dumpcap work? Does it use pcap_open() or pcap_open_live() function? I got errors while running my custom Packet injector like:  `c:&#92;pi&amp;gt; pi rpcap://my_device_name ERROR: &quot;Unable to open my_device_name. my_device_name is not supported by Winpcap.&quot;` I came to know that dumpcap use these Fun...'''
date = "2011-12-12T02:39:00Z"
lastmod = "2011-12-12T14:42:00Z"
weight = 7909
keywords = [ "winpcap", "pcap" ]
aliases = [ "/questions/7909" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Working of Dumpcap](/questions/7909/working-of-dumpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7909-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How does Dumpcap work? Does it use <code>pcap_open()</code> or <code>pcap_open_live()</code> function? I got errors while running my custom Packet injector like:</p><p>`c:\pi&gt; pi rpcap://my_device_name</p><p>ERROR: "Unable to open my_device_name. my_device_name is not supported by Winpcap."`</p><p>I came to know that dumpcap use these Functions. May I know how you Resolved this?</p></div><div id="question-tags" class="tags-container tags">winpcap pcap</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '11, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Dec '11, 01:00</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-7909" class="comments-container"></div><div id="comment-tools-7909" class="comment-tools"></div><div class="clear"></div><div id="comment-7909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7930"></span>

<div id="answer-container-7930" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7930-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>On Windows, it uses <code>pcap_open()</code>.</p><p>On UN*X, it uses <code>pcap_create()</code> and <code>pcap_activate()</code> if they're available on the machine on which it was built, and uses <code>pcap_open_live()</code> otherwise.</p><p>I assume from the <code>c:</code> in <code>c:pi&gt;</code> that this is Windows, with support for rpcap built in. If so, rpcap URLs are supported, but they have to have the syntax as documented in <a href="http://www.winpcap.org/docs/docs_412/html/group__remote__source__string.html">the WinPcap documentation</a>. The valid syntaxes are:</p><ol><li><code>rpcap://</code><em>devicename</em> - to open a local device named <em>devicename</em></li><li><code>rpcap://</code><em>host</em><code>/</code><em>devicename</em> - to open a device named <em>devicename</em> on the remote host <em>host</em></li><li><code>rpcap://</code><em>host</em><code>:</code><em>port</em><code>/</code><em>devicename</em> - to open a device named <em>devicename</em> on the remote host <em>host</em>, using port number <em>port</em> rather than the default port for the rpcap protocol</li></ol><p>Your URL is trying to open a local device named <em>my_device_name</em>; if there's no device, <em>supported by WinPcap</em>, with that name, on your machine, that will, not surprisingly, fail.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '11, 14:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7930" class="comments-container"></div><div id="comment-tools-7930" class="comment-tools"></div><div class="clear"></div><div id="comment-7930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

