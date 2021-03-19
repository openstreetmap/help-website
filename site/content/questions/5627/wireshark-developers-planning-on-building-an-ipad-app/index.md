+++
type = "question"
title = "Wireshark developers planning on building an iPad app?"
description = '''Will the Wireshark developers release an iPad application? '''
date = "2011-08-10T09:29:00Z"
lastmod = "2011-08-10T15:56:00Z"
weight = 5627
keywords = [ "ipad" ]
aliases = [ "/questions/5627" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark developers planning on building an iPad app?](/questions/5627/wireshark-developers-planning-on-building-an-ipad-app)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5627-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Will the Wireshark developers release an iPad application?</p></div><div id="question-tags" class="tags-container tags">ipad</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '11, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/5f0f397e84cd5bd9bac1d0b21d85f709?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kmcintosh78&#39;s gravatar image" /><p>kmcintosh78<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kmcintosh78 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Aug '11, 15:58</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-5627" class="comments-container"><span id="5629"></span><div id="comment-5629" class="comment"><div id="post-5629-score" class="comment-score"></div><div class="comment-text"><p>I highly doubt it. That requires too much development effort IMHO. Plus, I don't think Apple would ever approve it.</p></div><div id="comment-5629-info" class="comment-info"><span class="comment-age">(10 Aug '11, 10:44)</span> bstn</div></div><span id="17746"></span><div id="comment-17746" class="comment"><div id="post-17746-score" class="comment-score"></div><div class="comment-text"><p>So Pirni + a hypothetical iOS-ported Wireshark ver or equiv would still be pointless? Pirni packcaps via a basic MITM, i just would like to analyze the dump file while still on the iOS device.</p></div><div id="comment-17746-info" class="comment-info"><span class="comment-age">(17 Jan '13, 06:30)</span> metacym</div></div></div><div id="comment-tools-5627" class="comment-tools"></div><div class="clear"></div><div id="comment-5627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5633"></span>

<div id="answer-container-5633" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5633-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Someday, perhaps, as long as you wouldn't mind not being able to capture any traffic with it - just downloading pcap files from elsewhere and looking at them - or wouldn't mind having to have a jailbroken iPad on which to run Wireshark if you want to capture traffic on the iPad.</p><p>By default, capturing network traffic in <a href="http://en.wikipedia.org/wiki/Darwin_(operating_system)">Darwin</a>, the OS core of both Mac OS X and iOS, requires root privileges; I think one could safely say that the chances that Apple would approve an application requiring root privileges are so close to zero as to be indistinguishable from zero. Even if Apple were to change that, so that code running as the user (at least at one point, applications apparently ran as the user "mobile" in iOS) were allowed to open BPF devices, they would probably do so by sandboxing the ability to open BPF devices by default, and only approve selected applications to open BPF devices, which would require that the sandboxing mechanism allow that.</p><p>In addition, the user interface would probably have to be rethought for the smaller screen, and lack of overlapping windows, for the iPad.</p><p>A program to <em>read</em> captures, without being able to capture traffic, could probably be written for a non-jailbroken iPhone or iPad. It would not support C plugins, given that <code>dlopen()</code> and <code>dlsym()</code> are not allowed into the sandbox (so no loading additional code into the process); I don't know whether it would allow add-on Lua code. Given the user interface issues, a <em>lot</em> of work would be required to write an iPhone or iPad program to do that, <em>and</em> <strong>,</strong>given the lack of arbitrary amounts of virtual memory (as <a href="https://developer.apple.com/library/mac/#documentation/performance/conceptual/managingmemory/articles/aboutmemory.html">this Apple document</a> says, "In iPhone applications, read-only data that is already on the disk (such as code pages) is simply removed from memory and reloaded from disk as needed. Writable data is never removed from memory by the operating system. Instead, if the amount of free memory drops below a certain threshold, the system asks the running applications to free up memory voluntarily to make room for new data. Applications that fail to free up enough memory are terminated"), we'd have to do more work on reducing the address-space footprint of the program and to handle out-of-memory conditions (which would be a good thing to do, so it's more work).</p><p>So even an iOS version of Wireshark incapable of capturing packets is unlikely to exist soon.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '11, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jan '13, 11:24</p></div></div><div id="comments-container-5633" class="comments-container"></div><div id="comment-tools-5633" class="comment-tools"></div><div class="clear"></div><div id="comment-5633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

