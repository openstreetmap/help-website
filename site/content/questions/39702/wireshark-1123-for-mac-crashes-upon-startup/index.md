+++
type = "question"
title = "Wireshark 1.12.3 for Mac crashes upon startup"
description = '''I just downloaded the new Wireshark for Mac 1.12.3 and it crashes immediately upon startup. I&#x27;m running Yosemite. Here&#x27;s the dump. What am I doing wrong?  Process: wireshark-bin [14809] Path: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin Identifier: wireshark-bin Version: ??? Code...'''
date = "2015-02-08T01:52:00Z"
lastmod = "2015-02-08T15:12:00Z"
weight = 39702
keywords = [ "crash" ]
aliases = [ "/questions/39702" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.12.3 for Mac crashes upon startup](/questions/39702/wireshark-1123-for-mac-crashes-upon-startup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39702-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just downloaded the new Wireshark for Mac 1.12.3 and it crashes immediately upon startup. I'm running Yosemite. Here's the dump. What am I doing wrong?</p><pre><code>Process:               wireshark-bin [14809]
Path:                  /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin
Identifier:            wireshark-bin
Version:               ???
Code Type:             X86-64 (Native)
Parent Process:        Wireshark [14805]
Responsible:           Wireshark [14805]
User ID:               502

Date/Time:             2015-02-08 10:45:46.714 +0100
OS Version:            Mac OS X 10.10.2 (14C109)
Report Version:        11
Anonymous UUID:        B6D0E547-EE0D-B7D9-CEE1-A2F48DBEDF6D

Sleep/Wake UUID:       D8DEFC83-7EB3-41C9-B0E3-04239B692443

Time Awake Since Boot: 600000 seconds

Crashed Thread:        0

Exception Type:        EXC_BREAKPOINT (SIGTRAP)
Exception Codes:       0x0000000000000002, 0x0000000000000000

Application Specific Information:
dyld: launch, loading dependent libraries

Dyld Error Message:
  Library not loaded: /usr/X11/lib/libcairo.2.dylib
  Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin
  Reason: image not found</code></pre></div><div id="question-tags" class="tags-container tags">crash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '15, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/fdd8fac068461505a4f39532f6790aa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Holdrege&#39;s gravatar image" /><p>Holdrege<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Holdrege has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Feb '15, 14:37</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-39702" class="comments-container"></div><div id="comment-tools-39702" class="comment-tools"></div><div class="clear"></div><div id="comment-39702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39704"></span>

<div id="answer-container-39704" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39704-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does /usr/X11 exist? If not you may need to reinstall XQuartz or manually link /opt/X11 as described at <a href="https://ask.wireshark.org/questions/36367/wireshark-doesnt-start-after-upgrading-to-mac-os-x-yosemite.">https://ask.wireshark.org/questions/36367/wireshark-doesnt-start-after-upgrading-to-mac-os-x-yosemite.</a></p><p>Also note that the 1.99.x release train does not require X11, although you might want to wait for 1.99.3 if you choose to go that route.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '15, 15:12</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-39704" class="comments-container"><span id="39706"></span><div id="comment-39706" class="comment"><div id="post-39706-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help.</p></div><div id="comment-39706-info" class="comment-info"><span class="comment-age">(09 Feb '15, 00:07)</span> Holdrege</div></div><span id="40481"></span><div id="comment-40481" class="comment"><div id="post-40481-score" class="comment-score"></div><div class="comment-text"><p>1.99.3 works mostly fine on Yosemite (10.10.2) except I have had it crash with large Windows captured PCAP files.</p></div><div id="comment-40481-info" class="comment-info"><span class="comment-age">(11 Mar '15, 12:57)</span> razamattaz</div></div></div><div id="comment-tools-39704" class="comment-tools"></div><div class="clear"></div><div id="comment-39704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

