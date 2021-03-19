+++
type = "question"
title = "pcap: File has more bytes than defined"
description = '''Hi Wireshark Version: 1.12.4, RHEL 6.0 I have PCAP file with only one Frame of 683922 bytes, is there any size constraint to be lessthan or equal to 262144 Request your help Please find the below screenshot for the error message  Thanks Dinesh'''
date = "2015-09-02T01:17:00Z"
lastmod = "2015-09-02T10:24:00Z"
weight = 45588
keywords = [ "capture", "pcap", "wireshark" ]
aliases = [ "/questions/45588" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [pcap: File has more bytes than defined](/questions/45588/pcap-file-has-more-bytes-than-defined)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45588-score" class="post-score" title="current number of votes">0</div><span id="post-45588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Wireshark Version: 1.12.4, RHEL 6.0</p><p>I have PCAP file with only one Frame of 683922 bytes, is there any size constraint to be lessthan or equal to 262144</p><p>Request your help</p><p>Please find the below screenshot for the error message <img src="https://osqa-ask.wireshark.org/upfiles/111111_Size_Error.jpeg" alt="alt text" /></p><p>Thanks Dinesh</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '15, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/04334c27cb629065a13d61a61b611038?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinesh%20Babu%20Sadu&#39;s gravatar image" /><p><span>Dinesh Babu ...</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinesh Babu Sadu has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Sep '15, 02:25</strong> </span></p></div></div><div id="comments-container-45588" class="comments-container"></div><div id="comment-tools-45588" class="comment-tools"></div><div class="clear"></div><div id="comment-45588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45602"></span>

<div id="answer-container-45602" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45602-score" class="post-score" title="current number of votes">0</div><span id="post-45602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As the error message says, your file is corrupt. One way this happens is if you transfer the file from one system to another using FTP. Most FTP clients default to ASCII mode, but Wireshark trace files need to be transferred in Binary mode, not ASCII mode. If that's what happened here, and you still have the original file, then just repeat the transfer but this time put your FTP client in binary mode. For a command-line FTP client, the command "Type I" will do it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '15, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-45602" class="comments-container"></div><div id="comment-tools-45602" class="comment-tools"></div><div class="clear"></div><div id="comment-45602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

