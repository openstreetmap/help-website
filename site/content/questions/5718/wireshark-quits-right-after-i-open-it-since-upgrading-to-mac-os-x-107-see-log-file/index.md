+++
type = "question"
title = "Wireshark quits right after I open it since upgrading to Mac OS X 10.7 see log file"
description = '''Worked great on 10.6 and prior. Upgraded to 10.7, did not work. Uninstalled and reinstalled ver 1.6.1, same ver that was running fine before the upgrade. X11 is not opening in conjunction with Wireshark, but it did in 10.6. See log file. Searched MAC for &quot;_iconv&quot;, no hits. Any ideas? Thank you in ad...'''
date = "2011-08-16T22:49:00Z"
lastmod = "2011-09-06T13:50:00Z"
weight = 5718
keywords = [ "startup", "osx", "mac", "crash", "lion" ]
aliases = [ "/questions/5718" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark quits right after I open it since upgrading to Mac OS X 10.7 see log file](/questions/5718/wireshark-quits-right-after-i-open-it-since-upgrading-to-mac-os-x-107-see-log-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5718-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Worked great on 10.6 and prior. Upgraded to 10.7, did not work. Uninstalled and reinstalled ver 1.6.1, same ver that was running fine before the upgrade. X11 is not opening in conjunction with Wireshark, but it did in 10.6. See log file. Searched MAC for "_iconv", no hits. Any ideas? Thank you in advance.</p><pre><code>Process:         wireshark-bin [470]
Path:            /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin
Identifier:      wireshark-bin
Version:         ??? (???)
Code Type:       X86-64 (Native)
Parent Process:  Wireshark [467]

Date/Time:       2011-08-16 22:34:13.941 -0700
OS Version:      Mac OS X 10.7 (11A511)
Report Version:  9

Crashed Thread:  0

Exception Type:  EXC_BREAKPOINT (SIGTRAP)
Exception Codes: 0x0000000000000002, 0x0000000000000000

Application Specific Information:
dyld: launch, loading dependent libraries

Dyld Error Message:
  Symbol not found: _iconv
  Referenced from: /usr/lib/libcups.2.dylib
  Expected in: /Applications/Wireshark.app/Contents/Resources/lib/libiconv.2.dylib
 in /usr/lib/libcups.2.dylib</code></pre></div><div id="question-tags" class="tags-container tags">startup osx mac crash lion</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '11, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/a7c5f42228cdc29ff61e05c89367891c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brianv&#39;s gravatar image" /><p>brianv<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brianv has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Aug '11, 23:22</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5718" class="comments-container"></div><div id="comment-tools-5718" class="comment-tools"></div><div class="clear"></div><div id="comment-5718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6139"></span>

<div id="answer-container-6139" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6139-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I see this too - X11 doesn't open, so then wireshark doesn't open. If I open X11 first, WS opens, and I can look at an existing pcap - but does not capture properly on en1. I have not yet tested en0. hope this helps -</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '11, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/52ff5d6b59bd5798a667a6f346a52421?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packetlevel&#39;s gravatar image" /><p>packetlevel<br />
<span class="score" title="1 reputation points">1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packetlevel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Sep '11, 13:50</p></div></div><div id="comments-container-6139" class="comments-container"><span id="6781"></span><div id="comment-6781" class="comment"><div id="post-6781-score" class="comment-score"></div><div class="comment-text"><p>I have the same issue, but I can't even get Wireshark to start if X11 is open first....</p></div><div id="comment-6781-info" class="comment-info"><span class="comment-age">(07 Oct '11, 06:01)</span> James Dore</div></div><span id="6795"></span><div id="comment-6795" class="comment"><div id="post-6795-score" class="comment-score"></div><div class="comment-text"><p>What happens if you try to capture on en1?</p></div><div id="comment-6795-info" class="comment-info"><span class="comment-age">(07 Oct '11, 13:26)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-6139" class="comment-tools"></div><div class="clear"></div><div id="comment-6139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

