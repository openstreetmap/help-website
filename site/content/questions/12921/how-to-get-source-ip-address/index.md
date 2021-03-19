+++
type = "question"
title = "How to get source IP address?"
description = '''I am making a custom dissector that needs to be able to find the source ip address of a packet and compare it with the IP address of the host computer. How would I be able to find the source IP address? Thanks in advance for any help.'''
date = "2012-07-23T08:23:00Z"
lastmod = "2013-06-04T23:41:00Z"
weight = 12921
keywords = [ "ip", "dissector", "address" ]
aliases = [ "/questions/12921" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to get source IP address?](/questions/12921/how-to-get-source-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12921-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am making a custom dissector that needs to be able to find the source ip address of a packet and compare it with the IP address of the host computer.</p><p>How would I be able to find the source IP address?</p><p>Thanks in advance for any help.</p></div><div id="question-tags" class="tags-container tags">ip dissector address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '12, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/f930b778c54e8c2d76dbcc36f76087ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bball2601&#39;s gravatar image" /><p>bball2601<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bball2601 has one accepted answer">50%</span></p></div></div><div id="comments-container-12921" class="comments-container"></div><div id="comment-tools-12921" class="comment-tools"></div><div class="clear"></div><div id="comment-12921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12926"></span>

<div id="answer-container-12926" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12926-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I just figured it out, but for anyone who is having trouble with the same type of thing, you can output your source ip address as a string with ip_to_str(pinfo-&gt;src.data)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '12, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/f930b778c54e8c2d76dbcc36f76087ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bball2601&#39;s gravatar image" /><p>bball2601<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bball2601 has one accepted answer">50%</span></p></div></div><div id="comments-container-12926" class="comments-container"><span id="12933"></span><div id="comment-12933" class="comment"><div id="post-12933-score" class="comment-score"></div><div class="comment-text"><p>Note that <code>ip_to_str()</code> assumes the source address is an IPv4 address. You might want to check the type of the address and handle IPv6 addresses as well.</p></div><div id="comment-12933-info" class="comment-info"><span class="comment-age">(23 Jul '12, 15:22)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-12926" class="comment-tools"></div><div class="clear"></div><div id="comment-12926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21760"></span>

<div id="answer-container-21760" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21760-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>To find the Internet IP address visit the site <a href="http://www.ip-details.com/">IP-details.com</a> here it displays the information like ISP(Internet Service Provider),IP location,country,latitude,longitude etc..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '13, 23:41</strong></p><img src="https://secure.gravatar.com/avatar/22a525d6b0891ccc4842d61db33d2407?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VelaiyatuPillai&#39;s gravatar image" /><p>VelaiyatuPillai<br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VelaiyatuPillai has no accepted answers">0%</span></p></div></div><div id="comments-container-21760" class="comments-container"></div><div id="comment-tools-21760" class="comment-tools"></div><div class="clear"></div><div id="comment-21760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

