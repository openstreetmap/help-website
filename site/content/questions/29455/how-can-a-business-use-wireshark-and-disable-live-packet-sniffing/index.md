+++
type = "question"
title = "How can a business use Wireshark and disable Live Packet Sniffing?"
description = '''Our business may need to use Wire Shark for looking at packet data for a client, However, with this program being shared with all employees in the company. We don&#x27;t want anyone to actually look at our internal data. Is there a way that we can disable the Live Packet Sniff part of the program?'''
date = "2014-02-05T05:07:00Z"
lastmod = "2014-02-05T05:23:00Z"
weight = 29455
keywords = [ "sniffing", "packet", "wireshark" ]
aliases = [ "/questions/29455" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can a business use Wireshark and disable Live Packet Sniffing?](/questions/29455/how-can-a-business-use-wireshark-and-disable-live-packet-sniffing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29455-score" class="post-score" title="current number of votes">0</div><span id="post-29455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Our business may need to use Wire Shark for looking at packet data for a client, However, with this program being shared with all employees in the company. We don't want anyone to actually look at our internal data.</p><p>Is there a way that we can disable the Live Packet Sniff part of the program?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '14, 05:07</strong></p><img src="https://secure.gravatar.com/avatar/4ac176cf139f0b2e1ea87fd5fed4b271?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="countryboy456&#39;s gravatar image" /><p><span>countryboy456</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="countryboy456 has no accepted answers">0%</span></p></div></div><div id="comments-container-29455" class="comments-container"></div><div id="comment-tools-29455" class="comment-tools"></div><div class="clear"></div><div id="comment-29455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29457"></span>

<div id="answer-container-29457" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29457-score" class="post-score" title="current number of votes">1</div><span id="post-29457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way that we can disable the Live Packet Sniff part of the program?</p></blockquote><p>Yes, you can do one of the following</p><ul><li>'distribute' the <a href="https://1.eu.dl.wireshark.org/win32/WiresharkPortable-1.10.5.paf.exe">portable version of Wireshark</a> and <strong>don't</strong> install WinPcap on the company systems.</li><li>build your own installation package that does <strong>not include</strong> WinPcap, by using your preferred software distribution tool to create a 'snapshot' of a system with Wireshark (but without WinPcap).</li><li>use the silent installation of the default package. Run the installation package with option /S on Windows, as that does not install WinPcap. See also here: <a href="http://ask.wireshark.org/questions/27392/silent-installuninstal">http://ask.wireshark.org/questions/27392/silent-installuninstal</a></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '14, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Feb '14, 06:34</strong> </span></p></div></div><div id="comments-container-29457" class="comments-container"></div><div id="comment-tools-29457" class="comment-tools"></div><div class="clear"></div><div id="comment-29457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

