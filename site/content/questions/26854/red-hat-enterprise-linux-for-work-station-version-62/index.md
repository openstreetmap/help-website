+++
type = "question"
title = "Red Hat Enterprise linux for work station version 6.2"
description = '''Hello,  I have Red Hat Enterprise linux for work station version 6.2 OS in my computer and I want to install Wireshark in it. I am not a linux guy, I did see some people say to try these yum install wireshark yum install wireshark-gnome I did but I got wireshark package is not available. Can someone...'''
date = "2013-11-11T12:34:00Z"
lastmod = "2013-11-12T04:31:00Z"
weight = 26854
keywords = [ "install", "redhat" ]
aliases = [ "/questions/26854" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Red Hat Enterprise linux for work station version 6.2](/questions/26854/red-hat-enterprise-linux-for-work-station-version-62)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26854-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have Red Hat Enterprise linux for work station version 6.2 OS in my computer and I want to install Wireshark in it. I am not a linux guy, I did see some people say to try these</p><p>yum install wireshark</p><p>yum install wireshark-gnome</p><p>I did but I got wireshark package is not available.</p><p>Can someone please advise me?</p><p>Thanks Tony.</p></div><div id="question-tags" class="tags-container tags">install redhat</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '13, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/36861d74c9c88021d212085a2e32f99b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tony007&#39;s gravatar image" /><p>Tony007<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tony007 has no accepted answers">0%</span></p></div></div><div id="comments-container-26854" class="comments-container"></div><div id="comment-tools-26854" class="comment-tools"></div><div class="clear"></div><div id="comment-26854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26886"></span>

<div id="answer-container-26886" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26886-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer (and the comments) to a similar question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/23138/wireshark-for-red-hat-enterprise-linux">http://ask.wireshark.org/questions/23138/wireshark-for-red-hat-enterprise-linux</a></p></blockquote><p>If you are running the following command:</p><blockquote><p>yum list wireshark</p></blockquote><p>Do you get the following error message?</p><blockquote><p>This system is <strong>not registered with RHN</strong>.</p></blockquote><p>If so, you did not register your machine with the RedHat support machinery. As you don't pay for the support (or did not yet add the system to your RHN account), Red Hat is not willing to give your system any updates or packages from their online repositories.</p><p><strong>Solution(s):</strong><br />
</p><ul><li>buy a Red Hat subscription/support contract</li><li>install Wireshark from the RedHat installation CDs</li><li>use a different distribution (CentOS, Ubuntu, Kali, etc.)</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '13, 04:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Nov '13, 06:29</p></div></div><div id="comments-container-26886" class="comments-container"><span id="26899"></span><div id="comment-26899" class="comment"><div id="post-26899-score" class="comment-score"></div><div class="comment-text"><p><strong>Solution(s)</strong> (continued) - Build your own version of Wireshark (while this is a bunch more work and a bit of a pain, it will also yield a <em>much</em> more modern Wireshark than what Redhat delivers)</p></div><div id="comment-26899-info" class="comment-info"><span class="comment-age">(12 Nov '13, 07:58)</span> JeffMorriss ♦</div></div><span id="26900"></span><div id="comment-26900" class="comment"><div id="post-26900-score" class="comment-score"></div><div class="comment-text"><p>I wonder why Redhat (and thus also CentOS) does not update the Wireshark package, at least occasionally. Did you ever have contact to those guys at Redhat?</p></div><div id="comment-26900-info" class="comment-info"><span class="comment-age">(12 Nov '13, 08:06)</span> Kurt Knochner ♦</div></div><span id="26902"></span><div id="comment-26902" class="comment"><div id="post-26902-score" class="comment-score"></div><div class="comment-text"><p>Well, the EL product line is designed for stability where stability is (I think) defined as "lack of change." Meaning: only bug fixes and realistically often only security fixes.</p><p>However I remember reading a while back that they did start updating (at least) Firefox and Thunderbird as it's really unreasonable to use a 5-year-old Firefox. I wonder what it would take to get onto that "desktop use" list. (OTOH I did recently break one of our test department's test scripts with a botched Wireshark/tshark change--it took a little bit before the development team realized it was actually my fault!)</p><p>I have gotten some of the RPM generation work I did in Wireshark pushed upstream; Fedora 19 now has Wireshark 1.10.x and is (supposedly--I haven't checked) using less of Redhat's homegrown stuff to generate the RPM. But I suspect getting them to changing Wireshark versions might be a bit tougher...</p></div><div id="comment-26902-info" class="comment-info"><span class="comment-age">(12 Nov '13, 08:45)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-26886" class="comment-tools"></div><div class="clear"></div><div id="comment-26886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

