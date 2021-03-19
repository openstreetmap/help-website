+++
type = "question"
title = "ESP sequence check for lost packets ?"
description = '''Is there a way to check the correct sequence of ESP packets, looking for lost ones ? Without knowing any key or encryption algorithm,  a basic quality check of an encrypted flow could be to check the esp.sequence field,  that should be monotonically increasing within the same flow,  identified by th...'''
date = "2010-11-03T11:09:00Z"
lastmod = "2013-12-03T13:02:00Z"
weight = 792
keywords = [ "spi", "sequence", "packet", "lost", "esp" ]
aliases = [ "/questions/792" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ESP sequence check for lost packets ?](/questions/792/esp-sequence-check-for-lost-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-792-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to check the correct sequence of ESP packets, looking for lost ones ?</p><p>Without knowing any key or encryption algorithm, a basic quality check of an encrypted flow could be to check the <code>esp.sequence</code> field, that should be monotonically increasing within the same flow, identified by the <code>esp.spi</code> field.</p><p>My first idea would be to extract the fields at the command line and continue with perl, but a nice feature in wireshark would be to colorize the lost packets as in TCP.</p></div><div id="question-tags" class="tags-container tags">spi sequence packet lost esp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '10, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/449c0829813aecd7a23d1f4992e1e5b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="S%20Peters&#39;s gravatar image" /><p>S Peters<br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="S Peters has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Nov '10, 11:10</p></div></div><div id="comments-container-792" class="comments-container"><span id="27678"></span><div id="comment-27678" class="comment"><div id="post-27678-score" class="comment-score"></div><div class="comment-text"><p>This sounds like a good idea to me as well. Not much to it, it seems. I guess I'm going to have to hack something up myself for now.</p></div><div id="comment-27678-info" class="comment-info"><span class="comment-age">(02 Dec '13, 15:17)</span> mbs</div></div></div><div id="comment-tools-792" class="comment-tools"></div><div class="clear"></div><div id="comment-792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27735"></span>

<div id="answer-container-27735" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27735-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This feature does not yet exist but you can file an enhancement bug report if you wish at <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a>.</p><p>Until then, you might want to use <code>tshark</code> to find all <code>esp</code> packets matching a specific SPI and then extract the <code>esp.sequence</code> field. Write the packet number and sequence number to a file that can then be analyzed in Excel or whatever your favorite spreadsheet application happens to be.</p><p>For example:</p><pre><code>tshark -r esp.pcap -Y esp.spi==0xTBD -T fields -E header=y -e frame.number -e esp.sequence</code></pre><p>While the above is probably the best method to use at this time (or the best method I can think of at least), there are some other things you could do in Wireshark, such as:</p><ul><li>Add the <code>esp.sequence</code> (and possibly <code>esp.spi</code>) field as a custom column. Gaps still might not be very obvious though, but at least you'd be able to see the values more easily and be able to sort the packets by that column.</li><li>Just to find out if there are any missing packets, you can sort by the <code>esp.sequence</code> column, noting the <code>MINseq</code> and <code>MAXseq</code> values, then use the Advanced I/O Graphs to plot all packets containing the <code>esp.sequence</code> field, choosing <code>Calc: SUM(*)</code> of <code>esp.sequence</code>. Set the Tick interval as large as possible, i.e., 10 min. Finally, click the "Copy" button and paste the results into your spreadsheet. Sum all these values until you have 1 final value, which is basically a sum of all the <code>esp.sequence</code> values. I'll call this total <code>TOTALseq</code>. Next, apply the following formula:</li></ul><p><code>     [MAXseq * (MAXseq + 1) - MINseq * (MINseq - 1)] / 2 - TOTALseq</code></p><p>If there are no gaps, then the result will be zero; if you do have gaps, then what's left is the sum of all missing ESP sequence numbers. This won't necessarily tell you which ones are missing (unless you happen to get lucky where only one is missing), but it will at least tell you if there are any missing or not. Unfortunately, this method breaks down if there are any duplicate ESP packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '13, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '13, 13:03</p></div></div><div id="comments-container-27735" class="comments-container"><span id="60618"></span><div id="comment-60618" class="comment"><div id="post-60618-score" class="comment-score"></div><div class="comment-text"><p>See also to my answer to this question on SuperUser, <a href="https://superuser.com/questions/1169105/wireshark-highlight-missing-sequence-number"><em>Wireshark highlight missing sequence number</em></a>. There I include a method for using your spreadsheet software to help identify gaps that I think is much easier and more reliable than my original answer here.</p></div><div id="comment-60618-info" class="comment-info"><span class="comment-age">(06 Apr '17, 09:22)</span> cmaynard ♦♦</div></div><span id="60619"></span><div id="comment-60619" class="comment"><div id="post-60619-score" class="comment-score"></div><div class="comment-text"><p>For completeness, there has been sequence number analysis for ESP since September 2014, and it is enabled by default.</p></div><div id="comment-60619-info" class="comment-info"><span class="comment-age">(06 Apr '17, 09:35)</span> MartinM</div></div><span id="60621"></span><div id="comment-60621" class="comment"><div id="post-60621-score" class="comment-score"></div><div class="comment-text"><p>Ah, so there is. Thanks for pointing that out. The version of Wireshark I use most of the time due to the proprietary dissectors we need does not have that option. Updating our dissectors has been on my <em>TODO</em> list so we can finally make use of all of Wireshark's shiny new features again. For anyone else, just use the latest version of Wireshark then.</p></div><div id="comment-60621-info" class="comment-info"><span class="comment-age">(06 Apr '17, 09:42)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-27735" class="comment-tools"></div><div class="clear"></div><div id="comment-27735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

