+++
type = "question"
title = "Capture Filter ether dst not working"
description = '''Hi, I have the following assignment. My problem is that when I type in ether in the filter, it turns red. Is that supposed to happen? When I type in ether src and then my mac address, it still doesn&#x27;t work. Am I doing something wrong? Any help is appreciated. Thanks.  Find out which network interfac...'''
date = "2013-12-08T19:40:00Z"
lastmod = "2013-12-08T19:59:00Z"
weight = 27935
keywords = [ "src", "dst", "ether" ]
aliases = [ "/questions/27935" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Filter ether dst not working](/questions/27935/capture-filter-ether-dst-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27935-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have the following assignment. My problem is that when I type in ether in the filter, it turns red. Is that supposed to happen? When I type in ether src and then my mac address, it still doesn't work. Am I doing something wrong? Any help is appreciated. Thanks.</p><pre><code>Find out which network interface is the active interface using Wireshark, and then use that interface to complete the rest of the activities.

Find out the Media Access Control address (MAC address, or Ethernet address) on the active interface.

Read the documentation on www.wireshark.org and learn what is Capture Filter.

Learn to use capture filter to record interested packets.</code></pre><p>Examples of capture filters (replace the MAC address with the one you find in step 2)</p><pre><code>    record Ethernet frame with destination address of “00:25:00:41:96:62”:</code></pre><p>ether dst 00:25:00:41:96:62</p><pre><code>    record Ethernet frame with source address of “00:25:00:41:96:62”:</code></pre><p>ether src 00:25:00:41:96:62</p><pre><code>    record only multicast frames</code></pre><p>multicast and not ether dst ff:ff:ff:ff:ff:ff</p><pre><code>    record only broadcast frames :</code></pre><p>broadcast and ether dst ff:ff:ff:ff:ff:ff</p></div><div id="question-tags" class="tags-container tags">src dst ether</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '13, 19:40</strong></p><img src="https://secure.gravatar.com/avatar/17e5bf929e1f288ce2e76f2a2f90c69f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="heisenberg55&#39;s gravatar image" /><p>heisenberg55<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="heisenberg55 has no accepted answers">0%</span></p></div></div><div id="comments-container-27935" class="comments-container"></div><div id="comment-tools-27935" class="comment-tools"></div><div class="clear"></div><div id="comment-27935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27937"></span>

<div id="answer-container-27937" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27937-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Let me just give you a hint...</p><p>Please read about 'Capture Filters' and 'Display Filters' in the Wireshark documentation.</p><p>They are different; each type is entered in a different place in the GUI.</p><p>(A web search for 'wireshark "display filter" "capture filter"' will also give lots of info).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '13, 19:59</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-27937" class="comments-container"><span id="27938"></span><div id="comment-27938" class="comment"><div id="post-27938-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response. I looked around and found the codes eth.src and eth.dst. Maybe the code was wrong on the assignment or maybe I have a newer or older version of wireshark?</p></div><div id="comment-27938-info" class="comment-info"><span class="comment-age">(08 Dec '13, 20:12)</span> heisenberg55</div></div><span id="27939"></span><div id="comment-27939" class="comment"><div id="post-27939-score" class="comment-score">1</div><div class="comment-text"><p>Again: I'm going to suggest that you do some reading &amp; research to understand the difference between a "capture filter" and a "display filter" in Wireshark. :)</p><p>The syntax and verbs, etc used for each are different and are entered in different places in the GUI.</p><p>Your assignment specifically mentions using a "capture filter".</p></div><div id="comment-27939-info" class="comment-info"><span class="comment-age">(08 Dec '13, 20:27)</span> Bill Meier ♦♦</div></div><span id="27940"></span><div id="comment-27940" class="comment"><div id="post-27940-score" class="comment-score"></div><div class="comment-text"><p>I figured it out! I was supposed to use capture options. Thanks for the help. I appreciate it.</p></div><div id="comment-27940-info" class="comment-info"><span class="comment-age">(08 Dec '13, 21:56)</span> heisenberg55</div></div></div><div id="comment-tools-27937" class="comment-tools"></div><div class="clear"></div><div id="comment-27937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

