+++
type = "question"
title = "Alternate display for Packet List Pane"
description = '''For the situation whereby multiple payload messages are in a single TCP/UDP packet, it would be nice to be able to display the Info for each payload on adjacent rows of the Packet List Pane. What would be the appropriate API calls to display the Info in any of the following formats within a custom d...'''
date = "2012-08-06T14:09:00Z"
lastmod = "2012-08-06T19:07:00Z"
weight = 13402
keywords = [ "development", "packetlist" ]
aliases = [ "/questions/13402" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Alternate display for Packet List Pane](/questions/13402/alternate-display-for-packet-list-pane)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13402-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For the situation whereby multiple payload messages are in a single TCP/UDP packet, it would be nice to be able to display the Info for each payload on adjacent rows of the Packet List Pane.</p><p>What would be the appropriate API calls to display the Info in any of the following formats within a custom dissector plug-in code?</p><p>e.g. – Currently, my dissector performs the correction dissection on both messages, but I’m having to display the information for both messages on the same row within the “Info” column</p><p>So it looks like:</p><pre><code>No.   Time  Source    Destination  Protocol  Info
1     232.1 10.1.1.1  10.1.1.2     XXXX      DOG CAT</code></pre><p>What do I need to do to make the presentation look like:</p><pre><code>No.   Time  Source    Destination  Protocol  Info
1     232.1 10.1.1.1  10.1.1.2     XXXX      DOG
                                             CAT</code></pre><p>or even:</p><pre><code>No.   Time  Source    Destination  Protocol  Info
1     232.1 10.1.1.1  10.1.1.2     XXXX      DOG
1     232.1 10.1.1.1  10.1.1.2     XXXX      CAT</code></pre><p>or perhaps:</p><pre><code>No.   Time  Source    Destination  Protocol  Info
1     232.1 10.1.1.1  10.1.1.2     XXXX      DOG
2     232.1 10.1.1.1  10.1.1.2     XXXX      CAT</code></pre><p>This is along the lines of Wireshark Wishlist item <a href="http://wiki.wireshark.org/WishList#line-185">#24</a>.</p></div><div id="question-tags" class="tags-container tags">development packetlist</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '12, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/aa113408c3b312aac94702bb9639bbea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joeEmbed&#39;s gravatar image" /><p>joeEmbed<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joeEmbed has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Aug '12, 14:20</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-13402" class="comments-container"><span id="13403"></span><div id="comment-13403" class="comment"><div id="post-13403-score" class="comment-score"></div><div class="comment-text"><p>ref: <a href="http://www.wireshark.org/lists/wireshark-dev/201208/msg00026.html">http://www.wireshark.org/lists/wireshark-dev/201208/msg00026.html</a></p></div><div id="comment-13403-info" class="comment-info"><span class="comment-age">(06 Aug '12, 14:14)</span> helloworld</div></div></div><div id="comment-tools-13402" class="comment-tools"></div><div class="clear"></div><div id="comment-13402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13409"></span>

<div id="answer-container-13409" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13409-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>As per <a href="http://www.wireshark.org/lists/wireshark-dev/201208/msg00028.html">the followup message to the one helloworld cited</a>, there <em>are</em> no appropriate API calls for doing that - "All the information goes on the one row. The rows are frame-oriented, not PDU-oriented."</p><p>A display of that sort would require enhancements to Wireshark, as per the "along the lines" citing a wishlist item (i.e., an request by somebody who wishes for something to be added to Wireshark) and <a href="http://www.wireshark.org/lists/wireshark-dev/200606/msg00147.html">this mail message</a>, which was a followup to <a href="https://www.wireshark.org/lists/ethereal-dev/200606/msg00210.html">this (ethereal-dev!) mail message</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '12, 19:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Mar '14, 09:13</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-13409" class="comments-container"></div><div id="comment-tools-13409" class="comment-tools"></div><div class="clear"></div><div id="comment-13409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

