+++
type = "question"
title = "tshark command just to capture TCP, no ARP, DHCP, etc just TCP"
description = '''hello everyone im trying to capture just a TCP files with TSHARK. tshark -g -s 65535 -b duration:43200 -a files:1 -i eth0 –I eth1 -w /home/pi/DATA/info im using this right now and want to add a filter'''
date = "2017-10-08T17:53:00Z"
lastmod = "2017-10-10T00:33:00Z"
weight = 63748
keywords = [ "tshark" ]
aliases = [ "/questions/63748" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark command just to capture TCP, no ARP, DHCP, etc just TCP](/questions/63748/tshark-command-just-to-capture-tcp-no-arp-dhcp-etc-just-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63748-score" class="post-score" title="current number of votes">0</div><span id="post-63748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello everyone im trying to capture just a TCP files with TSHARK.</p><p>tshark -g -s 65535 -b duration:43200 -a files:1 -i eth0 –I eth1 -w /home/pi/DATA/info</p><p>im using this right now and want to add a filter</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '17, 17:53</strong></p><img src="https://secure.gravatar.com/avatar/143f79fb6cac7278de259bca80947d28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jcgarcia007&#39;s gravatar image" /><p><span>jcgarcia007</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jcgarcia007 has no accepted answers">0%</span></p></div></div><div id="comments-container-63748" class="comments-container"></div><div id="comment-tools-63748" class="comment-tools"></div><div class="clear"></div><div id="comment-63748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63751"></span>

<div id="answer-container-63751" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63751-score" class="post-score" title="current number of votes">0</div><span id="post-63751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jcgarcia007 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can add capture filter to tshark with '-f pcap-filter-expr' (s. also <a href="https://wiki.wireshark.org/CaptureFilters).">https://wiki.wireshark.org/CaptureFilters).</a></p><p>To filter only tcp packets, use '-f tcp'</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '17, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-63751" class="comments-container"><span id="63752"></span><div id="comment-63752" class="comment"><div id="post-63752-score" class="comment-score"></div><div class="comment-text"><p>Are there any rules for using quotes in that case? Tried to add '-f tcp' to the line above in the question, and it didn't work for me.. Errors are:</p><p>'tshark: A capture filter was specified both with "-f" and with additional command-line arguments.'</p><p>or 'Illegal token'</p></div><div id="comment-63752-info" class="comment-info"><span class="comment-age">(09 Oct '17, 01:59)</span> <span class="comment-user userinfo">Packet_vlad</span></div></div><span id="63755"></span><div id="comment-63755" class="comment"><div id="post-63755-score" class="comment-score">1</div><div class="comment-text"><p>I haven't read the syntax of the inital question right:</p><p>The '-I' flag is for running in monitor mode. 'eth1' is interpreted as a capture filter.</p><p>Therefore when using '-f tcp' and having 'eth1' there are two capturing filters.</p><p><a href="https://ask.wireshark.org/users/43081/jcgarcia007">@jcgarcia007</a>: What's the purpose of 'eth1' in your command?</p></div><div id="comment-63755-info" class="comment-info"><span class="comment-age">(09 Oct '17, 02:57)</span> <span class="comment-user userinfo">Uli</span></div></div><span id="63774"></span><div id="comment-63774" class="comment"><div id="post-63774-score" class="comment-score"></div><div class="comment-text"><p>thanks, this filter work perfectly</p></div><div id="comment-63774-info" class="comment-info"><span class="comment-age">(09 Oct '17, 14:42)</span> <span class="comment-user userinfo">jcgarcia007</span></div></div><span id="63782"></span><div id="comment-63782" class="comment"><div id="post-63782-score" class="comment-score"></div><div class="comment-text"><p>Presumably what was <em>intended</em> was</p><pre><code>tshark -g -s 65535 -b duration:43200 -a files:1 -i eth0 –i eth1 -w /home/pi/DATA/info</code></pre><p>I.e., lower-case "i" rather than capital "I", meaning that there are two <code>-i</code> flags, one specifying <code>eth0</code> and one specifying <code>eth1</code>, so that TShark will capture on both <code>eth0</code> and <code>eth1</code>.</p></div><div id="comment-63782-info" class="comment-info"><span class="comment-age">(10 Oct '17, 00:33)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-63751" class="comment-tools"></div><div class="clear"></div><div id="comment-63751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

